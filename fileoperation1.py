import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#df=pd.read_csv('demo.csv')
df=pd.read_csv('demo.csv',header=None)
print(df)
df1=pd.read_table('demo.csv',sep=',',header=None)
print(df1)
print(pd.read_csv('demo.csv',nrows=2,header=None))
#df1.to_csv('output.csv',sep=',')
df1.to_csv('output.csv',sep=':')
df.to_csv('output1.csv',columns=[1,2])
