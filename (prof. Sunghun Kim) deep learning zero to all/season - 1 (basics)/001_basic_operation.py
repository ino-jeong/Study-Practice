import tensorflow as tf

hello = tf.constant('hello, TF!!')
sess = tf.Session()

print(sess.run(hello))

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)
node3 = tf.add(node1, node2)
# node3 = node1 + node2

print("node 1:", node1, "/ node 2:", node2)
print("node 3:", node3,'\n')

print('by session : node 1:',sess.run(node1),'node 2:',sess.run(node2))
print('node 3 :',sess.run(node3))


# placeholder
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))  # result : 7.5
print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))  # result : [3. , 7.]

test_tensor1 = tf.constant(4)
test_tensor2 = tf.constant([4])
test_tensor3 = tf.constant([[4],[5]])

print(test_tensor1)
print(test_tensor2)
print(test_tensor3)

# 3 # a rank 0 tensor; this is a scalar with shape []
# [1. ,2., 3.] # a rank 1 tensor; this is a vector with shape [3]
# [[1., 2., 3.], [4., 5., 6.]] # a rank 2 tensor; a matrix with shape [2, 3]
# [[[1., 2., 3.]], [[7., 8., 9.]]] # a rank 3 tensor with shape [2, 1, 3]