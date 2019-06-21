import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

series1=Series([1,2,3,4],index=['a','b','c','d'])
print(series1)
series2=series1.reindex(['a','b','c','d','e','f'])
print(series2)
series2=series2.reindex(['a','b','c','d','e','f','g'],fill_value=10)
print(series2)
cars=Series(["BMW","Audi","merc"],index=[0,4,8])
print(cars)
ranger=range(13)
print(ranger)
cars=cars.reindex(ranger,method="ffill")
print(cars)

df1=DataFrame(randn(25).reshape(5,5),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
print(df1)
df2=df1.reindex(['a','b','c','d','e','f'])
print(df2)
df3=df2.reindex(columns=['c1','c2','c3','c4','c5','c6'])
print(df3)
#df4=df1.ix[['a','b','c','d','e','f'],['c1','c2','c3','c4','c5','c6']]
#print(df4)

df1=DataFrame(randn(9).reshape(3,3),index=['a','b','c'],columns=['c1','c2','c3'])
print(df1)
print(df1.head(2))
print(df1.tail(2))
print(df1.ix[0])