# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:27:33 2019

@author: USER
"""

import numpy as np
import pandas as pd
import statistics

df=pd.DataFrame()
df['score']=[15,25,32,88,56,45,95,100,42,29,66,78,56]
df['age']=[22,15,14,16,15,12,18,35,55,82,16,15,17]
df['weight']=[56,45,80,66,55,50,42,75,89,120,55,92,60]

#Ortalama

mean_score=sum(df['score'])/len(df['score'])
print(mean_score)
print(np.mean(df['score']))

mean_age=sum(df['age'])/len(df['age'])
print(mean_age)
print(np.mean(df['age']))

mean_weight=sum(df['weight'])/len(df['weight'])
print(mean_weight)
print(np.mean(df['weight']))

#Medyan

print(statistics.median(df['score']))
print(np.median(df['score']))

print(statistics.median(df['age']))
print(np.median(df['age']))

print(statistics.median(df['weight']))
print(np.median(df['weight']))

#Mode

statistics.mode(df['score'])
(values,counts)=np.unique(df['score'],return_counts=True)
a=np.argmax(counts)
values[a]

statistics.mode(df['age'])
(values,counts)=np.unique(df['age'],return_counts=True)
b=np.argmax(counts)
values[b]

statistics.mode(df['weight'])
(values,counts)=np.unique(df['weight'],return_counts=True)
c=np.argmax(counts)
values[c]

#Varyans

n=len(df['age'])
m_age= np.mean(df['age'])

def V(x,n):
    x=float(x)
    s=0
    for x in df['age']:
        s+=((x-m_age)**2)/(n-1)
    return s
print(V(x,n))

print(np.var(df['age'],ddof=1))
print(df['age'].var())

#Standart sapma

ss=np.sqrt(V(x,n))
print(ss)

np.std(df['age'],ddof=1)

#Standart hata

se=ss/np.sqrt(n)
print(se)

np.std(df['age'],ddof=1)/np.sqrt(n)

























