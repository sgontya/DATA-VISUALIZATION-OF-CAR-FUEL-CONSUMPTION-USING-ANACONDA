# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:53:35 2019

@author: sai kiran gontyala
"""
import pandas as pd

car_fuel = pd.read_csv("car_clean.csv")

x = ("rain", "sun", "refill_liters", "refill_gas")
y = list(x)
y[1] = "hot_sun"
x = tuple(y)

print(x)