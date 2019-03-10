#提示获取文件名
name = input("选择文件:")

#打开文件
f_read = open(name,"r")

#创建新文件
endName = name.rfind(".")
newName = name[:endName] + "[复制]" +name[endName:]
f_write = open(newName,"w")

#copy
#content = f_read.read()
#f_write.write(content)
#for lineContent in f_read.readlines():
#    f_write.write(lineContent)
while True:
    lineContent = f_read.readline()
    if len(lineContent)>0:
        f_write.write(lineContent)
    else:
        break

#关闭
f_read.close()
f_write.close()
