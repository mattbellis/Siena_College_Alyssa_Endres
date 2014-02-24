"""
Plotting boundaries of NYS
"""

import numpy as np
import matplotlib.pylab as plt
import random

#infile = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\ny_boundaries.txt")
infile = open("../data/ny_boundaries.txt")
#latitude, longitude

vals = (np.array(infile.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
lat = vals[index]
lon = vals[index+1]

plt.plot(lon,lat,'.')


# a is starting value, b-a is range of values
#a = 1
#b = 5
#random.random() * a + (b-a)
#print random.randrange(0,10)