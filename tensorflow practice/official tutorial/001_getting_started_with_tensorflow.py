'''
3 : rank 0 (scalar)
[1,2,3] : rank 1, shape [3]
[[1,2,3], [4,5,6]] : rank 2, shape [2, 3]
...

'''

import tensorflow as tf

'''
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)

node3 = tf.add(node1, node2)
# node3 = node1 + node2

sess = tf.Session()
print(sess.run([node1, node2]))
print(sess.run(node3))


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, feed_dict={a: 7, b: 5}))
print(sess.run(adder_node, feed_dict={a: [1,3,4], b: [-1,-2,-3]}))


# setting variables

print('\n**test linear model**\n')

W = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)


# note that unless init called in sess.run(), Variables are not initialized
init = tf.global_variables_initializer()
sess.run(init)
feed_dict = {x: [1,2,3,4], y: [0, -1, -2, -3]}
print(sess.run(linear_model, feed_dict))
print(sess.run(loss, feed_dict))


# if we assign W and b values manually, use tf.assign()
# fixW = tf.assign(W, [-1])
# fixb = tf.assign(b, [1])
# sess.run([fixW, fixb])
# print(sess.run(loss, feed_dict))


# use optimizer
optimizer = tf.train.GradientDescentOptimizer(0.05)
train = optimizer.minimize(loss)

sess.run(init)
for i in range(500):
    sess.run(train, feed_dict)

print(sess.run([W, b]))
'''

# rewritten complete program

# model parameters
W = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)

# input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(500):
    sess.run(train, {x: x_train, y: y_train})
    # evaluate training accuracy
    final_W, final_b, final_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
    print('*** W :', final_W, 'b :', final_b, 'loss :', final_loss)


