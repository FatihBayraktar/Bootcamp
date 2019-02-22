# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:06:34 2019

@author: USER
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Veri çerçevesi

kod=["A","B","C","D","E","F","G","H","I","J"]
cerceve=pd.DataFrame(index=kod)
cerceve["Asal"]=[1,2,3,5,7,11,13,17,19,23]
cerceve["Fibonacci"]=[1,1,2,3,5,8,13,21,34,55]
cerceve.index.name="Sıra"
cerceve


#Train.csv sorusu

train=pd.read_csv("train.csv",index_col=0)
train
male_female_mean=train.groupby(by="Sex").mean()["Age"]



male_survived=len(train[train["Sex"]=="male"])
female_survived=len(train[train["Sex"]=="female"])

total_30_survival=len(train[(train["Age"]<30) & (train["Survived"]==1)])


total_female_survival=len(train[(train["Sex"]=="female") 
    & (train["Survived"]==1)])
total_male_survival=len(train[(train["Sex"]=="male") 
    & (train["Survived"]==1)])
total_male_survival
male_survival_ratio=male_survived/total_male_survival
female_survival_ratio=female_survived/total_female_survival
print(female_survival_ratio)
print(male_survival_ratio)
print(total_30_survival)
print(male_female_mean)