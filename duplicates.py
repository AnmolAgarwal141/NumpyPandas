import numpy as np
import pandas as pd
from pandas import  Series ,DataFrame

df1=DataFrame({'col1':['uber','uber','uber','uber','grab'],
               'col2':[5,4,3,3,5]})
print(df1)
print(df1.duplicated())
print(df1.drop_duplicates())
print(df1.drop_duplicates(['col1']))
print(df1.drop_duplicates(['col2']))
print(df1.drop_duplicates(['col1'],keep='last'))