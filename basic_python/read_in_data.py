import numpy as np
import matplotlib.pylab as plt

import sys

# infile = open(sys.argv[1])
infile = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop1.dat")

vals = (np.array(infile.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
x = vals[index]
y = vals[index+1]

plt.plot(x,y,'o',markersize=1.0)
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()
