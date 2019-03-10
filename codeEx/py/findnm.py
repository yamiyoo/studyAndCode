#coding=utf-8
#定义列表
names = ["XH","XM","LW"]
#获取要查询名字
insertNm = input("姓名")
#判断重复
findFlag = 0
for name in names:
    if name==insertNm:
        findFlag = 1
        break
if findFlag == 1:
    print("找到")
else:
     print("无")
     names.append(insertNm)
     print(names)
if insertNm in names:
    print("找到")
else:
    print("无")

