# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:18:42 2019

@author: sai kiran gontyala
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

car_fuel = pd.read_csv("car_clean.csv")


car_fuel['speed'].plot.hist(bins=10, align='left', color='k', edgecolor='red', linewidth=3)
plt.show()



