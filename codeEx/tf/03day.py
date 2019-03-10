import tensorflow as tf 
 
state = tf.Variable(3,name = 'counter')
#print(state.name)
one = tf.constant(6)#常亮one,每次加的值

new_value = tf.add(state,one)#加法
update = tf.assign(state, new_value)#分配值到new\_value中

init = tf.initialize_all_variables()
#must have if define variable

with tf.Session() as sess:
	sess.run(init)
	for _ in range(3):
		sess.run(update)
		print(sess.run(state))