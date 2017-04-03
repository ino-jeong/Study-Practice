import tensorflow as tf

# let our hypothesis as H(x) = Wx + b
# then cost = 1/m * sum(H(x)-y)^2  / m : number of data

# ** use placeholder!

# x_train = [1, 2, 3]
# y_train = [1, 2, 3]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]), name='weight')  # [1] : rank is 1
b = tf.Variable(tf.random_normal([1]), name='bias')

# hypothesis = x_train * W + b
hypothesis = X * W + b

# cost = tf.reduce_mean(tf.square(hypothesis - y_train))  # reduce_mean() : return mean value
cost = tf.reduce_mean(tf.square(hypothesis - Y))


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())  # global_variables_initializer() : initialize Variable(). shoud be executed before main job

for step in range(2001):
    # sess.run(train)
    cost_val, W_val, b_bal, train_val = sess.run([cost, W, b, train], feed_dict={X: [1, 2, 3], Y: [1, 2, 3]})

    if step % 20 == 0:
        # print(step, sess.run(cost), sess.run(W), sess.run(b))
        print(step, cost_val, W_val, b_bal)


# after train, testing model

print(sess.run(hypothesis, feed_dict={X: [5]}))
print(sess.run(hypothesis, feed_dict={X: [2, 7, 8.3]}))

