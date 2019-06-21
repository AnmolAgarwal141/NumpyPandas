import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds=sns.load_dataset('diamonds').sample(frac=1).head(100)
print(ds)
sns.lmplot('price','carat',ds).savefig('reg1.png')
sns.lmplot('price','carat',ds,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'red','linewidth':1}).savefig('reg2.png')
sns.lmplot('price','carat',ds,order=4,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'red','linewidth':1}).savefig('reg3.png')
sns.lmplot('price','carat',ds,fit_reg=False).savefig('reg4.png')
sns.lmplot('price','carat',ds,hue='cut',markers=['.','v','^','<','>']).savefig('reg5.png')
sns.lmplot('price','carat',ds,hue='cut').savefig('reg6.png')
sns.lmplot('price','carat',ds,lowess=True).savefig('reg7.png')
sns.regplot('price','carat',ds).get_figure().savefig('reg8.png')
#subplot
image,(plt1,plt2)=plt.subplots(1,2,sharey=True)
sns.regplot('price','carat',ds,ax=plt1).get_figure().savefig('reg9.png')
sns.boxplot(ds['carat'],ds['depth'],color='green',ax=plt2).get_figure().savefig('reg9.png')