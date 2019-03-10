import numpy as py
import pandas as pd
dataser = pd.Series([4.9,5.1,4.6,5.0,5.1,4.7,4.4,4.7,4.6])
sample_mean = dataser.mean()#平均值
sample_std = dataser.std()#标准差
sample_size = 5
print(sample_mean,sample_std)

SE = sample_std / py.sqrt(9)
print(SE)


