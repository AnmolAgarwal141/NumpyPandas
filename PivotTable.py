import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url="https://en.wikipedia.org/wiki/Pivot_table"
df_list=pd.io.html.read_html(url)
df=df_list[0]
print(df)

#new_header=df.iloc[0]
#df=df[1:]
#df.columns=new_header
#print(df)
print(df.pivot('Date of sale','Sales person','Total price'))