# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
  
np.random.seed(10**7)
n_bins = 20
x = np.random.randn(10000, 3)
  
colors = ['green', 'blue', 'lime']
  
plt.hist(x, n_bins, density = True,
    histtype ='bar',
    color = colors,
    label = colors,
    rwidth = 0.5)
  
plt.legend(prop ={'size': 10})
  
plt.title('matplotlib.pyplot.hist() function Example\n\n',fontweight ="bold")
  
plt.show()
