class sweetPotato():
    #初始化
    def __init__(self):
        self.cookLever = 0
        self.cookString = "生"
        self.condiment = []

    def cook(self,lever):
        self.cookLever += lever
        if self.cookLever=="1":
            self.cookString = "半生"
        elif self.cookLever == 2:
            self.cookString = "半熟"
        elif self.cookLever == 3:
            self.cookString = "熟"
        elif self.cookLever > 3:
            self.cookString = "焦"
    
    def addCondiment(self,temp):
        self.condiment.append(temp)

    def __str__(self):
        
        msg = "烤了"+ str(self.cookLever)
        msg += " 成熟度"+ self.cookString
        if len(self.condiment)>0:    
            msg += " 作料"
            
            for temps in self.condiment:
                msg += temps + ","
            #切除末尾,
            #return msg[:-1]
        else:
            msg += "添加佐料"
        return msg[:-1]


cookSP = sweetPotato()
print(cookSP)

cookSP.cook(2)
cookSP.addCondiment("孜然")
print(cookSP)
cookSP.addCondiment("芥末")
cookSP.cook(1)
print(cookSP)
