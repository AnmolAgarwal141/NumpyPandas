import numpy as np
import pandas as pd
from pandas import Series,DataFrame

Series1=Series([100,200,300],index=['a','b','c'])
print(Series1)
print(Series1['b'])
print(Series1[['a','b']])
print(Series1[0])
print(Series1[0:2])
print(Series1[Series1>150])
print(Series1[Series1==300])

df1=DataFrame(np.arange(9).reshape(3,3),index=["car","bike","cycle"],columns=['a','b','c'])
print(df1)
print(df1['a'])
print(df1[['a','b']])
print(df1.ix["bike"])
print(df1.ix[1])
