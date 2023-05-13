import numpy as np
# print(np.__version__)
import tensorflow as tf
print(tf.__version__)
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
# # Define a variable tensor
# # x = tf.Variable(tf.zeros([None, 2]), dtype=tf.float32)
# @tf.function
# def return_x():
#     x = tf.placeholder(tf.float32, shape=[None, 2])
#     return x
# x=return_x()
# # import tensorflow as tf

# # shape = tf.TensorShape([10, 2])
# # x = tf.Variable(tf.zeros(shape), dtype=tf.float32)

# # Define a simple computation
# y = x + 1

# # Create a TensorFlow session and run the computation
# with tf.compat.v1.Session() as sess:
#     sess.run(tf.compat.v1.global_variables_initializer())
#     result = sess.run(y, feed_dict={x: [[1, 2], [3, 4]]})
#     print(result)

