import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy import  random

A1=random.randn(25).reshape(5,5)
B1=np.arange(25).reshape(5,5)
print(A1)
print(B1)
print(np.concatenate([A1,B1],axis=1))
print(np.concatenate([A1,B1],axis=0))

s1=Series([100,200,300],index=['a','b','c'])
s2=Series([400,500],index=['d','e'])
print(pd.concat([s1,s2]))
print(pd.concat([s1,s2],axis=1))

d1=DataFrame(random.rand(4,3),columns=['A','B','C'])
d2=DataFrame(random.rand(3,3),columns=['B','D','A'])
print(pd.concat([d1,d2]))
print(pd.concat([d1,d2],ignore_index=True))
print(pd.concat([d1,d2],axis=1))