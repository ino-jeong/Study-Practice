import tensorflow as tf

x = tf.constant([[0,1,2],[2,1,0]], dtype=tf.float32, shape=[2,3])

sess = tf.Session()
print(sess.run(x))

print(sess.run(tf.arg_max(x, 0)))  #return index of max number.


print(sess.run(tf.ones_like(x)))
print(sess.run(tf.zeros_like(x)))


