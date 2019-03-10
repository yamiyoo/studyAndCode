#保护对象属性
#self.__属性私有属性,外面无法访问,如果zai外面添加属性后
#(动态访问不影响原值),则可访问
class person:
	
	def __init__(self,name,age):
		self.name = name
		self.__age = age
	def setAge(self,age):
		if age > 0 and age<100:
			self.__age = age
		else:
			print("年龄超标")
	def getAge(self):
		print(self.__age)
		return self.__age
	def  __del__(self):
		print("____完全删除引用计数器___")
		#删除对象,当其为0时候才打印


laowang = person("langwang",30)
#laowang.age += 1
laowang.setAge(310)
laowang.getAge()
#手动删除
laozhang = laowang
#引用计数器(硬链接)
#软连接类似快捷键
del laowang
#引用计数器减一,删除老王对象,不能使用老张