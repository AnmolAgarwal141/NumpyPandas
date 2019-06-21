import numpy as np
import  pandas as pd
from pandas import  Series,DataFrame

s1=Series([5,np.nan,6,np.nan],index=['a','b','c','d'])
print(s1)
s2=Series(np.arange(4),dtype=np.float64,index=s1.index)
print(s2)
s3=Series(np.where(pd.isnull(s1),s2,s1))
print(s3)
s4=s1.combine_first(s2)
print(s4)

df1=DataFrame({'col1':[5,np.nan,15],'col2':[20,25,np.nan],'col3':[np.nan,np.nan,35]})
print(df1)
df2=DataFrame({'col1':[0,10,20],'col2':[10,20,30]})
print(df2)
print(df1.combine_first(df2))