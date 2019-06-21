import pandas as pd
from pandas import Series
import numpy as np
x
revenue=Series([20,80,40,35],index=['ola','uber','grab','gojek'])
print(revenue['ola'])
print(revenue[revenue>=35])

print('ola' in revenue)
dict=revenue.to_dict()
print(dict)

index2=['ola','uber','grab','gojek','lyft']
revenue2=Series(revenue,index=index2)
print(revenue2)

print(pd.isnull(revenue2))
print(pd.notnull(revenue2))

print(revenue+revenue2)
revenue2.name="company revenue"
revenue2.index.name="company name"
print(revenue2)