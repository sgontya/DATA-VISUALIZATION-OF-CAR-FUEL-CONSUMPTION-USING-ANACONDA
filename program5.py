# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:59:54 2019

@author: sai kiran gontyala
"""

import pandas as pd

car_fuel = pd.read_csv("measurements.csv")
print(car_fuel)

car_fuel.to_csv('car_clean.csv')

car_fuel.to_csv('car_clean.csv', index=False)