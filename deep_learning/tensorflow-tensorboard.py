# import tensorflow as tf
#
# #상수
# a = tf.constant(20, name="a")
# b = tf.constant(30, name="b")
# mul_op = a*b
#
# session = tf.Session()
#
# #tensorboard
# tw = tf.summary.FileWriter("log_dir", graph=session.graph)
#
# print(session.run(mul_op))




import tensorflow as tf

a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(0, name="v")

calc_op = a+b*c
assign_op = tf.assign(v, calc_op)

session = tf.Session()

tw = tf.summary.FileWriter("log_dir", graph=session.graph)

session.run(assign_op)
print(session.run(v))