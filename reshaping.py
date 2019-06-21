import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df1=DataFrame(np.arange(8).reshape(2,4),index=pd.Index(['ola','uber'],name='cabs'),columns=pd.Index(['c1','c2','c3','c4'],name='attribute'))
print(df1)
df2=df1.stack()
print(df2)
dfunstack=df2.unstack()
print(dfunstack)
df3=df2.unstack('cabs')
print(df3)
df4=df2.unstack('attribute')
print(df4)

s1=Series([5,10,15],index=['a','b','c'])
s2=Series([15,20,25],index=['b','c','d'])
s3=pd.concat([s1,s2],keys=['k1','k2'])
print(s3)

df=s3.unstack()
print(df)
print(df.stack())
print(df.stack(dropna=False))