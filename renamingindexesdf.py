import numpy as np
import pandas as pd
from pandas import  Series,DataFrame

df=DataFrame(np.arange(25).reshape(5,5),index=['ola','uber','gozek','grab','lyft'],columns=['RE','QU','LO','GR','AG'])
print(df)

df.index=df.index.map(str.upper)
print(df)

print(df.rename(index=str.title,columns=str.lower))
print(df.rename(index={'UBER':'The Best Taxi'},columns={'RE':'Revenue','QU':'Quality'}))
df.rename(index={'UBER':'The Best Taxi'},columns={'RE':'Revenue','QU':'Quality'},inplace=True)
print(df)