# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:20:13 2019

@author: sai kiran gontyala
"""

import pandas as pd

car_fuel =pd.read_csv("car_clean.csv")

stat = car_fuel['speed'].describe()

print(stat)