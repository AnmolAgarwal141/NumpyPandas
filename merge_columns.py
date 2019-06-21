import numpy as np
import  pandas as pd
from pandas import DataFrame

df1=DataFrame({'reference':['ola','uber','lyft','gojek','grab'],'revenue':[1,2,3,4,5]})
df2=DataFrame({'reference':['ola','uber','uber','ola'],'revenue':[1,2,3,4]})
df3=pd.merge(df1,df2)
print(df3)
df4=pd.merge(df1,df2,on='reference')
print(df4)
df5=pd.merge(df1,df2,on='reference',how='left')
print(df5)
df6=pd.merge(df1,df2,on='reference',how='right')
print(df6)
df7=pd.merge(df1,df2,on='reference',how='right')
print(df7)
df8=DataFrame({'reference':['ola','ola','lyft'],'revenue':['one','two','three'],'profit':[1,2,3]})
df9=DataFrame({'reference':['ola','ola','lyft','lyft'],'revenue':['one','one','one','three'],'profit':[4,5,6,7]})
print(pd.merge(df8,df9,on=['reference','revenue'],how='outer'))
print(pd.merge(df8,df9,on=['reference','revenue'],how='outer',suffixes=('_first','_second')))