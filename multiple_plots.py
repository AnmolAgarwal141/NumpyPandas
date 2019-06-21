import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series


ds=randn(100)
fig=sns.distplot(ds,bins=15).get_figure()
fig.savefig('plot1.png')
fig1=sns.distplot(ds,hist=False,rug=True,bins=10).get_figure()
fig1.savefig('plot2.png')
fig2=sns.distplot(ds,bins=15,kde_kws={'color':'red','label':'KDE_GRAPH'},hist_kws={'label':'Histogram','color':'green','alpha':0.5}).get_figure()
fig2.savefig('plot3.png')

s1=Series(ds,name='s1')
fig3=sns.distplot(s1,bins=15,rug=True).get_figure()
fig3.savefig('plot4.png')