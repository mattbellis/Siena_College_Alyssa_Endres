# wechsler_gals_100k
# columns are right ascension, declination, z redshift

import math
import numpy as np
import matplotlib.pylab as plt

infiler = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\wechsler_gals_100k.dat")

vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]

nptsd = len(r)
