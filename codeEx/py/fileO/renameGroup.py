import os

#输入批量保存文件夹
RenameFile = input("文件夹")
#列出文件名
all_name = os.listdir("./"+RenameFile)
#循环修改
for name in all_name:
    #os.rename("./test/"+name,"./test/"+"[学艺]"+name)
    os.rename("./"+RenameFile+"/"+name,
            "./"+RenameFile+"/"+"[学艺]"+name)



