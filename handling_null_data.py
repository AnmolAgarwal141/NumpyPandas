import pandas as pd
import numpy as np
from pandas import Series,DataFrame

series1=Series(['a','b','c',np.nan])
print(series1.isnull())
print(series1.dropna())

df1=DataFrame([[1,2,3],[4,5,np.nan],[7,np.nan,10],[np.nan,np.nan,np.nan]])
print(df1)
print(df1.dropna())
print(df1.dropna(how='all'))
print(df1.dropna(axis=1))

df2=DataFrame([[1,2,3,np.nan],[4,5,6,7],[8,9,np.nan,np.nan],[12,np.nan,np.nan,np.nan]])
print(df2)
print(df2.dropna(thresh=3))
print(df2.dropna(thresh=2))
print(df2.fillna(0))
print(df2.fillna({0:0,1:50,2:100,3:200}))

