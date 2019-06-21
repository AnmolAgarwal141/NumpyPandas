import numpy as np
import  pandas as pd
from pandas import DataFrame

df1=DataFrame({'reference':['o','u','l','o','u'],'data':range(5)})
df2=DataFrame({'profit':[10,20]},index=['o','u'])
print(pd.merge(df1,df2,left_on='reference',right_index=True))

df3=DataFrame({'ref1':['a','a','a','o','o'],'ref2':[5,10,15,20,25],'ref3':[0,1,2,3,4]})
df4=DataFrame(np.arange(10).reshape(5,2),index=[['a','a','o','o','o'],[20,10,10,10,20]],columns=['col1','col2'])
print(df4)
print(pd.merge(df3,df4,left_on=['ref1','ref2'],right_index=True))
df5=DataFrame({'ref1':['a','a','o','o','o'],'ref2':[15,20,25,30,35],'ref3':[2,3,4,5,6]})
print(df3.join(df5,lsuffix='x',rsuffix='y'))
