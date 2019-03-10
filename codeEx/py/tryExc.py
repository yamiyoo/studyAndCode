#coding=utf-8
try:
    open('anjianc.txt')
    print(abc)

#except (NameError,FileNotFoundError) as result:
#    print("异常%s\n"%result)
except Exception as result:
    print("异常%s\n"%result)
except :
    print("........")
else:
    print("正常")

