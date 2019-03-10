#两个对象交互
#对象隐藏,讲获取修改属性新建方法
class Home:

    def __init__(self,area):
        self.area = area#剩余面积
        self.light = "on"#开灯
        self.containsItem = []
    def addItem(self,item):
        if self.area > item.getArea():
            self.containsItem.append(item)
            self.area -= item.getArea()    
    def turnOff(self):
        self.light = "off"
        for temp in self.containsItem:
            temp.turnoff()
    def __str__(self):
        msg = "家当前可用面积"+str(self.area)
        if len(self.containsItem)>0:    
            msg += "\t"
            msg += "物品:"
            #msg += ",".join(self.containsItem)
            for temp in self.containsItem:
                msg += temp.getName() + ","
            msg = msg[:-1]
            if self.light == "on":
                msg += "\t" + "灯开可见"
            else:   
                msg += "\t" + "黑灯瞎火"
        return msg 

class Bed:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        self.light = "on"
    def __str__(self):
        msg = self.name+"占面积"+str(self.area)
        if self.light == "on":
            msg += "灯开可见"
        else:
            msg += "黑灯瞎火"
        return msg
    def getName(self):
        return self.name
    def getArea(self):
        return self.area
    def turnoff(self):
        self.light = "off"

#创建对象,默认面积
home = Home(128)
print(home)

bed = Bed("席梦思",4)
print(bed)
home.addItem(bed)

cBed = Bed("儿童床",3)
print(cBed)
home.addItem(cBed)

print(home)
print("=========关灯===========")
home.turnOff()
print(bed)
print(home)
