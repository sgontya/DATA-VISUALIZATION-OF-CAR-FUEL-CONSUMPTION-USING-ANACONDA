# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:22:07 2019

@author: sai kiran gontyala
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

car_fuel = pd.read_csv("car_clean.csv")

sns.countplot(car_fuel['gas_type'])
plt.show()