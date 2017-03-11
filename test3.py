import matplotlib.pyplot as plt
from pylab import *
import pandas as pd
import numpy as np

df = pd.read_csv('data2.csv',header=None)
df1 =df.ix[:,1]

# figure related code
fig = plt.figure()
fig.suptitle('Letter Recognition', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
ax.boxplot(df1)

#ax.set_title('axes title')
ax.set_xlabel('group')
ax.set_ylabel('horizontal position of box')

#plt.boxplot(df1)
plt.show()



