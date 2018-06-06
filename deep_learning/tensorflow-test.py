import tensorflow as tf

#상수
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")

#변수
v = tf.Variable(0, name="v")

calc_op = a+b+c
assign_op = tf.assign(v, calc_op)

session = tf.Session()
session.run(assign_op)

print(session.run(v))