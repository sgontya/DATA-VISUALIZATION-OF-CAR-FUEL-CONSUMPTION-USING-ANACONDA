# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:36:16 2019

@author: sai kiran gontyala
"""

import pandas as pd

car_fuel = pd.read_csv("car_clean.csv")

car_fuel['distance']=car_fuel['distance'].str.replace(',','.').astype(float)
car_fuel['consume']=car_fuel['consume'].str.replace(',','.').astype(float)
car_fuel['temp_inside']=car_fuel['temp_inside'].str.replace(',','.').astype(float)

print(car_fuel)