import numpy as np
import pandas as pd
from pandas import Series
from numpy.random import randn

Ser1=Series([500,1000,1500],index=['a','c','b'])
print(Ser1)
print(Ser1.rank())
print(Ser1.sort_index())
print(Ser1.sort_values())
print(Ser1.rank())
ser2=Series(randn(10))
print(ser2)
print(ser2.rank())
#print(ser2.sort_values())
ser2=ser2.sort_values()
print(ser2.rank())