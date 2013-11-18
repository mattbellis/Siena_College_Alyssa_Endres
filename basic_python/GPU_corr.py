# code to generate the two-point correlation with the wechsler galaxy data 

import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot

# data-data
infiled = open("log10binning_GPU_10k_data_data_arcmin.dat")
vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
dd_th_hi = vals[index]
dd_th_lo = vals[index+1]
dd = vals[index+2]

dd_th_avg = (dd_th_hi + dd_th_lo) / 2


# data-flat
infiled = open("log10binning_GPU_10k_data_flat_arcmin.dat")
vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
df_th_hi = vals[index]
df_th_lo = vals[index+1]
df = vals[index+2]

df_th_avg = (df_th_hi + df_th_lo) / 2


# flat-flat
infiled = open("log10binning_GPU_10k_flat_flat_arcmin.dat")
vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
ff_th_hi = vals[index]
ff_th_lo = vals[index+1]
ff = vals[index+2]

ff_th_avg = (ff_th_hi + ff_th_lo) / 2


# calculate the two-point correlation function
W = (dd-(2*df)+ff)/ff.astype('float')
print W


plt.figure()
plt.plot(dd_th_avg,W,'ko')
pyplot.xscale('log')
plt.show()