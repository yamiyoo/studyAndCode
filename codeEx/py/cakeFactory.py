class Cake(object):
    def __init__(self,taste='甜'):
        self.taste = taste

class CreamCake(object):
    def __init__(self,taste='奶油'):
        self.taste = taste

class fruitCake(object):
    def __init__(self,taste='水果'):
        self.taste = taste
class CakeFactory(object):
    def createCake(self,taste):    
        if taste == "奶油":
            cake = CreamCake()
        elif taste == "水果":
            cake = FruitCake()
        else :
            cake = Cake()
        return cake
class Sale(object):
    def __init__(self):
        self.factory = CakeFactory()
    def order(self,taste):
        cake = self.factory.createCake(taste)
        print("__味道%s__"%cake.taste)

a = Sale()
a.order("奶油")
