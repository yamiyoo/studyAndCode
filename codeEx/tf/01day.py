import tensorflow as tf
import numpy as np

#creat data#
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 +0.3


###creat start###
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))
#tf.Variable描述y参数
y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
###creat end###

init = tf.global_variables_initializer()  
# 初始化所有之前定义的Variable

sess = tf.Session()
sess.run(init)          # Very important
#Session 来执行 init 初始化步骤. 并且, 用 Session 来 run 
#每一次 training 的数据. 逐步提升神经网络的预测准确性.

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

#在TensorFlow的世界里，变量的定义和初始化是分开的，
#所有关于图变量的赋值和计算都要通过tf.Session的run来进行。
#想要将所有图变量进行集体初始化时
#应该使用tf.global_variables_initializer