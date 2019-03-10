class Cat(object):
    #类名属性方法
    num = 0#当创建不同对象可通过类属性计数
    #类属性
    def __init__(self):
        self.age = 1
        #实例属性
        #如果类属性名字和实例属性相同,那么
        #通过对象去后去的num时,会获取实例属性的值
        self.num =100
    def run(self):
        print("_____cat run_____")

mao = Cat()
#类属性跟着类走,实力例属性通过类调用
print(mao.num)
print(Cat.num)
Cat.num += 1
print(mao.num)
print(Cat.num)

