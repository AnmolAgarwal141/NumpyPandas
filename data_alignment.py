import numpy as np
import pandas as pd
from pandas import Series,DataFrame
ser_a=Series([100,200,300],index=['a','b','c'])
ser_b=Series([100,200,300,400],index=['a','b','c','d'])

print(ser_a+ser_b)

d1=DataFrame(np.arange(4).reshape(2,2),index=["car","bike"],columns=['a','b'])
print(d1)
d2=DataFrame(np.arange(9).reshape(3,3),index=["car","bike","cycle"],columns=['a','b','c'])
print(d2)
print(d1+d2)
d1=d1.add(d2,fill_value=0)
print(d1)

ser_c=d2.ix[0]
print(d2)
print(ser_c)
print(d2-ser_c)
