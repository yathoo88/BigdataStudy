import tensorflow as tf
import pandas as pd
import numpy as np


#csv load (pandas)
csv = pd.read_csv("bmi.csv")

# 데이터 정규화
csv["height"] = csv["height"]/200
csv["weight"] = csv["weight"]/100
bclass = {"thin" : [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x :np.array(bclass[x]))

test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_answer = list(test_csv["label_pat"])

#데이터플로우
x = tf.placeholder(tf.float32, [None,2], name="x")    #키, 몸무게
y_ = tf.placeholder(tf.float32, [None,3], name="y_")   #정답

with tf.name_scope('interface') as scope :
    w = tf.Variable(tf.zeros([2,3]),name="w")    #가중치
    b = tf.Variable(tf.zeros([3]),name="b")
    
    #softmax 회귀 정의
    with tf.name_scope('softmax') as scope :
        y = tf.nn.softmax(tf.matmul(x, w) + b)

#훈련
with tf.name_scope('loss') as scope:    #loss 계산율 
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
with tf.name_scope('training') as scope:    # traning 계산
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(cross_entropy)

#정답률
predict = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

#session
session = tf.Session()
session.run(tf.global_variables_initializer())  #변수 초기화

#학습
for step in range(500):
    i = (step * 100) % 14000
    rows = csv[1+i : 1+i+100]
    x_pat = rows[["weight","height"]]
    y_answer = list(rows["label_pat"])
    fd = {x : x_pat, y_: y_answer}
    session.run(train, feed_dict=fd)
    if step%100 == 0 :
        cre = session.run(cross_entropy, feed_dict=fd)
        acc = session.run(accuracy, feed_dict={x:test_pat, y_:test_answer})
        print("step=",step, " cre=",cre," acc=",acc)

#tensorboard
tw = tf.summary.FileWriter("log_dir", graph=session.graph)

#최종
acc = session.run(accuracy, feed_dict={x: test_pat, y_:test_answer})
print("최종 정답률  : ", acc)
