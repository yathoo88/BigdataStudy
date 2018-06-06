# import tensorflow as tf
#
# #placeholder 생성 (정수 자료형 3개를 가진 배열)
# a = tf.placeholder(tf.int32, [3])
#
# b = tf.constant(2)
# x2_op = a*b #모든 값을 x2 해준다
#
# session = tf.Session()
#
# r1 = session.run(x2_op, feed_dict={a:[1,2,3]})
# print(r1)
# r2 = session.run(x2_op, feed_dict={a:[10,20,30]})
# print(r2)






import tensorflow as tf

#placeholder 생성 (요소 개수를 정하지 않고 생성)
a = tf.placeholder(tf.int32, [None])

b = tf.constant(2)
x2_op = a*b #모든 값을 x2 해준다

session = tf.Session()

r1 = session.run(x2_op, feed_dict={a:[1,2,3,4,5]})
print(r1)
r2 = session.run(x2_op, feed_dict={a:[10,20]})
print(r2)