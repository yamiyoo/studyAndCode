#定义父类,默认继承object
'''class Cat(object):
	def __init__(self):
		self.__name = "abc"
	
	def run(self):
		print("_____run_____")

	def test(self):
		print(self.__name)
	
#子类,父类私有属性和方法不能使用在子类里
class Bosi(Cat):
	def test
		

bosi = Bosi()
bosi.run()
bosi.test()
'''

'''#多继承
class Ma(object):
	def run(self):
		print("________run 100km/h________")

class Lv(object):
	def take(self):
		print("_________take away_________")
		
class Luozi(Ma,Lv):
	pass

luozi = Louzi()
luozi.run()
luozi.take()
#当父类有同样命名的方法,则实现MROPEN机制中的类的方法
对象.__mro__#显示查找先后顺序
'''

#多态
#"鸭子类型"
#定义类型和运行类型不一致
'''弱类型语言:会随着类型改变
int a = 100强类型语言
def Fun(父类 obj):
	Fun函数需要接受一个F1类型或者F1子类类型

封装:方法,类

类方法 静态方法
@classmethon
#装饰器
def setNum(cls,newNum):
	cls.num = newNum
可通过类名或者对象调用方法修改类属性
不能通过类名访问实例属性实例方法

类中普通方法需要加上 @staticmethon








