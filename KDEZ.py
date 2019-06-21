import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mean=[0,0]
covariance=[[1,0],[0,100]]
ds=np.random.multivariate_normal(mean,covariance,500)
#print(ds)

dframe=pd.DataFrame(ds,columns=['col1','col2'])
#print(dframe)
fig=sns.kdeplot(dframe).get_figure()
fig.savefig('KDE.png')
fig2=sns.kdeplot(dframe,shade=True).get_figure()
fig2.savefig('KDE2.png')
fig3=sns.kdeplot(dframe,bw=1.1).get_figure()
fig3.savefig('KDE3.png')
#fig3=sns.kdeplot(dframe,bw='silverman').get_figure()
#fig3.savefig('KDE3.png')
fig4=sns.jointplot('col1','col2',dframe,kind='kde')
fig4.savefig('KDE4.png')