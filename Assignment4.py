import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
df=pd.read_csv('IRIS.csv')
print(df)
msk = np.random.rand(len(df)) < 0.7
train = df[msk]
test = df[~msk]
print('\n\n\n\n')
print(train)
print('\n\n\n\n')
print(test)