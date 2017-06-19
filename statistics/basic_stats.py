#!/bin/env python3


a = [ 163.1, 162.2, 210.5, 201.0, 188.7, 182.6, 153.0, 173.5, 146.6, 148.0 ]
print('a = ' + repr(a))
print('min a = ' + repr(min(a)))
print('max a = ' + repr(max(a)))
print('len a = ' + repr(len(a)))

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

nda = np.ndarray((10,), buffer=np.array(a))
print('numpy.ndarray nda = ' + repr(nda))

df = pd.DataFrame(data=nda)
print('pandas.DataFram df = ' + repr(df))
print(df.info(verbose=True))
print(df.describe())
# print('info df = ' + repr(df.info))
df.hist(bins=4)
#plt.plot(p)

