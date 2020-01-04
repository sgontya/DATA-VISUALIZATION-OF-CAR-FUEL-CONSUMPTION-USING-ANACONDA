# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:32:22 2019

@author: sai kiran gontyala
"""

import pandas as pd

car_fuel = pd.read_csv("car_clean.csv")

car_fuel['temp_inside']=car_fuel['temp_inside'].str.replace(',','.').astype(float)

t_inside_mean = car_fuel.temp_inside.mean()
t_outside_mean = car_fuel.temp_outside.mean()

t_inside_median = car_fuel.temp_inside.median()
t_outside_median = car_fuel.temp_outside.median()

t_inside_std = car_fuel.temp_inside.std()
t_outside_std = car_fuel.temp_outside.std()

print(t_inside_mean)
print(t_outside_mean)

print(t_inside_median)
print(t_outside_median)

print(t_inside_std)
print(t_outside_std)