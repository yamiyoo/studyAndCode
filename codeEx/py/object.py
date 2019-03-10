class Dog:
    def __init__(self,newColor):
        self.color = newColor
    
    def brak(self):
        print("旺旺")

    def changeColor(self,newColor):
        self.color = newColor
        print("颜色:%s"%self.color)

    def __str__(self):
        return "当前颜色:"+self.color

    def printInfo(self):
        print(self.color)

def test(name):
    name.printInfo()
    name.changeColor("黑")

wangcai = Dog("白")
##wangcai.color = "白"
##print(wangcai.color)
#wangcai.printInfo()
#wangcai.changeColor("黑")
#wangcai.brak()

test(wangcai)

print(wangcai)
print(id(wangcai))
