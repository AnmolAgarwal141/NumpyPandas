import numpy as np
import pandas as pd

prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

no_bins=[0,10,20,30,40,50]
category=pd.cut(prime,no_bins)
print(category)
print(category.categories)
print(pd.value_counts(category))
print(pd.cut(prime,3,precision=1))