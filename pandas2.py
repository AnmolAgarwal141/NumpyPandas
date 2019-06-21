import pandas as pd
from pandas import Series,DataFrame
import numpy as np
revenue=pd.read_clipboard()
print(revenue)
print('\n',revenue.columns)
print('\n',revenue['Walmart'])

print(DataFrame(revenue,columns=['1','Walmart','Retail']))

revenue2=DataFrame(revenue,columns=['1','Walmart','Retail','yo'])
print(revenue2)

print(revenue2.head(2))
print(revenue2.tail(2))
print(revenue.ix[0])

arraynp=np.array([100,200,300,400,500])
revenue2['yo']=arraynp
print(revenue2)

arrayseries=Series([200,500],index=[2,3])
revenue2['yo']=arrayseries
print(revenue2)

del revenue2['yo']
print(revenue2)

sample={ 'company':['a','b'],'profit':[1000,2000]}
print(sample)
smaple2=DataFrame(sample)
print(smaple2)
