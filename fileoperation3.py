import pandas as pd
from pandas import DataFrame
from pandas import read_html
url="https://countrycode.org/"
dfList=pd.io.html.read_html(url)
dframe=dfList[0]
print(dframe)
print(dframe.columns.values)