# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:25:21 2019

@author: sai kiran gontyala
"""

import pandas as pd
import matplotlib.pylab as plt

car_fuel = pd.read_csv("car_clean.csv")

car_fuel['distance']=car_fuel['distance'].str.replace(',','.').astype(float)
car_fuel['consume']=car_fuel['consume'].str.replace(',','.').astype(float)

car_fuel.plot(kind = 'scatter', x='distance', y='consume')

plt.show()