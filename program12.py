# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:44:26 2019

@author: sai kiran gontyala
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

car_fuel = pd.read_csv("car_clean.csv")

car_fuel['distance']=car_fuel['distance'].str.replace(',','.').astype(float)
car_fuel['consume']=car_fuel['consume'].str.replace(',','.').astype(float)

minac=car_fuel.query('AC==0.000000')
maxac=car_fuel.query('AC==1.000000')

sns.lmplot('distance','consume',data=minac,)
sns.lmplot('distance','consume',data=maxac,)
plt.show()

