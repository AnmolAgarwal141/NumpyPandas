import pandas as pd

excelfile=pd.ExcelFile('demo2.xlsx')
df=excelfile.parse('Sheet1')
print(df)