import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('gapminder-FiveYearData.csv')
print(df)
df1=df.pivot_table(index='continent', columns='year', values='lifeExp')
print(df1)
sns.heatmap(df1,annot=True).get_figure().savefig('heatmap.png')