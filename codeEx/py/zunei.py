#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
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
        return [niu,sigma,niu3]
                #期望方差E(x^3)

#偏度峰值
def calc_stat(data):
    [niu, sigma, niu3]=calc(data)
    n=len(data)
    niu4=0.0 # niu4计算峰度计算公式的分子
    for a in data:
        a -= niu
        niu4 += a**4
    niu4 /= n

    skew =(niu3 -3*niu*sigma**2-niu**3)/(sigma**3) # 偏度计算公式
    kurt=niu4/(sigma**4) # 峰度计算公式:
    #下方为方差的平方即为标准差的四次方
    return [niu, sigma,skew,kurt]
#概率密度函数                               
def normfun(x,mui, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

def main():
    
    e = eval(input('数据'))
    data = list(e)
    print(data)
    list_data = []
    list_data = calc_stat(data)
    [niu, sigma, skew, kurt] = calc_stat(data)
    print (list_data)
    info = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' %(niu,sigma, skew, kurt) # 字典标注
    plt.text(1,0.38,info,bbox=dict(facecolor='blue',alpha=0.25))
    n, bins, patches = plt.hist(data,15,density=True,facecolor='b',alpha=0.9)
    plt.title('ability histogram')
    
    #模拟曲线
    u = list_data[0]
    s = list_data[1]
    #print(u,s)
    #x = np.arange(u - 3*s,u + 3*s,0.1)
    #y_sig = np.exp(-(x - u) ** 2 /(2* s **2))/(math.sqrt(2*math.pi)*s)
    #plt.plot(x, y_sig, "r-", linewidth=2)
    y = scipy.stats.norm.pdf(bins, u, s)
    plt.plot(bins, y*100, 'r--')
    
    plt.subplots_adjust(left = 0.15)
    plt.grid(True)
    plt.show()

main()
