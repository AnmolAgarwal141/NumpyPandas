import pandas as pd
from pandas import Series,DataFrame
series1=Series([20,30,40,50],index=['a','b','c','d'])
print(series1)

indexes=series1.index
print(indexes)
print(indexes[2])
print(indexes[1:])
print(indexes[1:-2])
print(indexes[-2:])
print(indexes[2:4])
#indexes[0]='c'
#print(indexes)