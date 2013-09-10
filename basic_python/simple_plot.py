import numpy as np
import matplotlib.pylab as plt

x = np.random.random(1000)

plt.hist(x,bins=100,range=(-1,2))
plt.show()
