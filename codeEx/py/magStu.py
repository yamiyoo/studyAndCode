#coding=utf-8
#定义列表
StuInfo = []

def PrintMu():
	print("+"*30)
	print("     学生管理     ")
	print("1.添加")
	print("2.删除")
	print("3.修改")
	print("4.查询")
	print("5.显示")
        print("6.保存")
	print("0.退出")
	print("+"*30)

def addStd():
	newName = input("姓名:")
	newSex = input("性别:")
	newPhone = input("电话:")
	newStd = {}
	newStd['name'] = newName
	newStd['sex'] = newSex
	newStd['phone'] = newPhone
	return newStd

def PrintStd():
	print("学生信息:")
	print("序号  姓名  性别  电话")
	i = 1
	for tempInfo in StuInfo:
		print("%d     %s  %s    %s"%(i,tempInfo['name'],tempInfo['sex'],tempInfo['phone']))
		i+=1
def save2file():
        f = open("backup.data","w")
        f.write(str(StuInfo))
        f.close()

def recoverData():
        global StuInfo
        f = open("backup.data")
        content = f.read()
        StuInfo = eval(content)
        f.close()

def main():
        recoverData()
        while True:
                PrintMu()
                key = input("操作码")

                if key == "1":
                        StuInfo.append(addStd())
                elif key == "2":
                        index = input("序号")
                        del StuInfo[index-1]
                elif key == "3":
                        index = input("序号")
                        StuInfo[index-1] = addStd()
                elif key == "4":
                        index = input("序号")
                        print(StuInfo[index-1])
                elif key == "5":
                        PrintStd()
                elif key == "6":
                        save2file()
                elif key == "0":
                        break

main()
