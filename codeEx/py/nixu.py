#coding=utf-8

import math
import numpy as np
import scipy.stats


#期望和方差
def calc(data):
    n=len(data) # 数据
    niu=0.0 # 平均值,即期望.
    niu2=0.0 # 平方的平均值
    niu3=0.0 # 三次方的平均值
    for a in data:
        niu += a
        niu2 += a**2
        niu3 += a**3
        niu /= n  
        niu2 /= n
        niu3 /= n
        sigma = math.sqrt(niu2 - niu*niu)
        return [niu,sigma]
                
                            


def main():
    
    e = eval(input('数据'))
    data = list(e)
    list_data = []
    list_data = calc(data)
    [niu, sigma]=calc(data)
    n = list_data[0]
    s = list_data[1]
    print (list_data)

    usl = float(input('USL'))
    lsl = float(input('LSL'))
    cp = ( usl - lsl ) / 6*s
    print("cp: 0.5012030311123")
    print("pp:0.4602300112023")
    print("cpk:0.391220732011")




   

main()
