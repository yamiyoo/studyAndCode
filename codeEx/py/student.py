stuInfos = []
print("1.添加")
print("2.删除")
print("3.修改")
print("4.查询")
print("5.打印")
print("0.退出")

while True:
    key =input("输入操作")

    if key == "1":
        newname = input("姓名")
        newsex = input("性别")
        newInfos = {}
        newInfos['name'] = newname
        newInfos['sex'] = newsex
        stuInfos.append(newInfos)
    elif key =="3":
        pass
        stuId = int(input("序号"))
        newname = input("姓名")
        newsex = input("性别")
        stuInfos[stuId-1]['name'] = newname
        stuInfos[stuId-1]['sex'] = newsex
        
    elif key =="5":
        i = 1
        for tempInfo in stuInfos:
            print("%d %s %s "%(i,tempInfo['name'],tempInfo['sex']))
            i = i+1  
   # elif key =="0":
