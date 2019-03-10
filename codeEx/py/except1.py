class Test(Exception):
    def __init__(self,length,atleast):
        self.length = length
        self.atleast = atleast
try :
    raise Test(1,2)
except Test as result:
    print("异常%s"%result)
