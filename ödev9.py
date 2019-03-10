# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:41:50 2019

@author: USER
"""


#1. Soru


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats
import seaborn as sns
sns.set()


dg=np.random.normal([12,13,19,81,88,90,91,92,146,149,1,3,5,6,
                       11,44,65,79,80,100,112,113,114,120,132,
                       150,180,190,195,55,22,32,35,21,36,45,55],
[120, 122, 118, 126, 122, 126, 120, 114, 125, 
                       117, 114, 113, 119, 113, 118, 124, 127, 127, 
                       122, 120, 119, 130, 117, 121, 116, 107, 117, 
                       131, 125, 125, 127, 113, 115, 121, 111, 115, 121])
plt.hist(dg)

plt.figure(figsize=(10,4), dpi = 100)
res = stats.probplot(dg, plot=plt)
plt.title("Q-Q Çizgesi")
plt.xlabel("Teorik Değerler")
plt.ylabel("Örnek Veriler")
plt.show()


#2.Soru

prices=pd.read_csv("GOOGL.csv")

data=prices['Adj Close']
    
data.head()

odd=(data/data.shift(1))-1
profit=np.log(data/data.shift(1))

plt.plot(profit)
plt.show()















