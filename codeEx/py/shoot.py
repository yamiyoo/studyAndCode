class Person:
    def __init__(self,name,blood):
        self.name = name
        self.blood = blood
    def addBullet(self,clip,bullet):
        clip.saveBullet(bullet)
    def addClip(self,gun,clip):
        gun.saveClip(clip)
    def withGun(self,gun):
        self.gun = gun
    def aim(self,person):
        self.gun.shoot(person)
    def outBlood(self,value):
        self.blood -= value
    def __str__(self):
        return self.name +"血量"+ str(self.blood)

#抢
class Gun:
    def __init__(self):
        self.clip = None
        
    def __str__(self):
        if self.clip:
            return "有弹夹"
        else:
            return "无弹夹"
    def saveClip(self,clip):
        if not self.clip:
            self.clip = clip
    def shoot(self,person):
        bullet = self.clip.outBullet()
        if bullet:
            bullet.hurt(person)
        else:
            print("空枪")

#子弹
class Bullet:
    def __init__(self,value):
        self.value = value
    def hurt(self,person):
        person.outBlood(self.value)
#夹
class Clip:
    def __init__(self):
        self.contain = 20
        self.bulletList = []
    def saveBullet(self,bullet):
        if len(self.bulletList)<self.contain:
            self.bulletList.append(bullet)
    def outBullet(self):
        if len(self.bulletList)>0:
            bullet = self.bulletList[-1]
            self.bulletList.pop()
            return bullet
        else:
            return None
    def __str__(self):
        return "弹夹容量"+str(len(self.bulletList))+"/"+str(self.contain)


def pushBullet(int):
    bullet = Bullet(5)
    i = 0
    while i<int:
        laowang.addBullet(clip,bullet)
        i+=1
def countShoot(int):
    i = 0
    while i<int:    
        laowang.aim(xiaozhang)
        print(xiaozhang)
        print(clip)
        print(gun)
        i+=1

class Ak47(Gun):
    #重写父类方法
    def shoot(self,person):
        i = 0
        while i<3:
            #调用父类
            super().shoot(person)
            i += 1

        

laowang = Person("老王",100,)
xiaozhang = Person("小张",100)
print(xiaozhang)

clip = Clip()
print(clip)

#bullet = Bullet()
gun = Ak47()
print("+++++装子弹+++++")
laowang.addClip(gun,clip)
pushBullet(5)
print(gun)
laowang.withGun(gun)
print(clip)
#laowang.aim(xiaozhang)
print("+++++射两枪+++++")
countShoot(2)


