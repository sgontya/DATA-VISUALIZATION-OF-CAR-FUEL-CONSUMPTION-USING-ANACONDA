# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:59:39 2019

@author: sai kiran gontyala
"""

import pandas as pd

car_fuel = pd.read_csv("car_clean.csv")

car_fuel['distance']=car_fuel['distance'].str.replace(',','.').astype(float)
car_fuel['consume']=car_fuel['consume'].str.replace(',','.').astype(float)
car_fuel['refill_liters']=car_fuel['refill_liters'].str.replace(',','.').astype(float)
car_fuel['temp_inside']=car_fuel['temp_inside'].str.replace(',','.').astype(float)

rl_mean = car_fuel.refill_liters.mean()
t_inside_mean = car_fuel.temp_inside.mean()

#print(rl_mean)
#print(t_inside_mean)

#Replacing missing values in refill_liters, refill_gas, temp_inside with mean
car_fuel['refill_liters'] = car_fuel.refill_liters.fillna(rl_mean)
car_fuel['temp_inside'] = car_fuel.temp_inside.fillna(t_inside_mean)

#print(car_fuel)

#To get complete info about data

car_fuel.info()