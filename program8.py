# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:47:47 2019

@author: sai kiran gontyala
"""

import pandas as pd
import numpy as np

car_fuel = pd.read_csv('car_clean.csv')

car_fuel['distance']=car_fuel['distance'].str.replace(',','.').astype(float)
car_fuel['consume']=car_fuel['consume'].str.replace(',','.').astype(float)
car_fuel['refill_liters']=car_fuel['refill_liters'].str.replace(',','.').astype(float)
car_fuel['temp_inside']=car_fuel['temp_inside'].str.replace(',','.').astype(float)

rl_mean = car_fuel.refill_liters.mean()
t_inside_mean = car_fuel.temp_inside.mean()

car_fuel['refill_liters'] = car_fuel.refill_liters.fillna(rl_mean)
car_fuel['temp_inside'] = car_fuel.temp_inside.fillna(t_inside_mean)

def recode_gas_type(gas):
    
    if gas == 'E10':
        return 0
    elif gas == 'SP98':
        return 1
    else:
        return np.nun
    
car_fuel['recode'] = car_fuel.gas_type.apply(recode_gas_type)

print(car_fuel)