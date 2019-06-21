import numpy as np
import pandas as pd
from pandas import DataFrame

df=DataFrame(np.random.randn(1000,5))
print(df.head())
print(df.tail())
print(df.describe())
column=df[0]
print(column.head())
print('\n')
print(column[np.abs(column)>3])
print('\n')
print(df[(np.abs(df)>3).any(1)])
df[(np.abs(df)>3)]=np.sign(df)*5
print(df.describe())