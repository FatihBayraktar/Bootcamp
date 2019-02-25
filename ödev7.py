# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 16:19:20 2019

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


wur=pd.read_csv('timesData.csv',sep=',')
wur_harvard=wur.loc[wur['university_name']=='Harvard University',['teaching','year']]
wur_metu=wur.loc[wur['university_name']=='Middle East Technical University',['teaching','year']]

plt.subplot(1,2,1)
plt.ylabel("Teaching Score")
plt.xlabel("Year")
plt.title("Harvard University")
plt.tight_layout()
plt.bar(wur_harvard['year'],wur_harvard['teaching'],color="cyan")

plt.subplot(1,2,2)
plt.ylabel("Teaching Score")
plt.xlabel("Year")
plt.title("Middle East Technical University")
plt.tight_layout()
plt.bar(wur_metu['year'],wur_metu['teaching'],color="red")