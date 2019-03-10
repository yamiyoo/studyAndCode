class Test(object):

	#初始化,完成对象属性设置
	def __init__(self):
		self.num = 0
		print("__init__")
	
	#完成创建一个对象
	def __new__(cls):
		print("___new__")
		print(cls)
		return super().__new__(cls)
		#将创建的对象 返回后存储 使init方法中self接受

	#更改print(a)的值
	def __str__(self):
		return "略略略"


a = Test()
#当创建对象后首先执行__new__方法完成创建对象,然后__init__初始化

print(a.num)
print(a)