import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds=randn(80)
sns.boxplot(ds).get_figure().savefig('box1.png')
sns.boxplot(ds,orient='v').get_figure().savefig('box2.png')
sns.boxplot(ds,whis=np.inf).get_figure().savefig('box3.png')
