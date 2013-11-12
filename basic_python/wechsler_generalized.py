# wechsler_gals_100k
# columns are right ascension, declination, z redshift

import numpy as np
import matplotlib.pylab as plt

infiled = open("C:\Users\Alyssa\Dropbox\Astro data\Wechsler data\wechsler_gals.cat")


vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]

# plot histogram of all z values
plt.hist (z, bins=50, range=(0, 0.35))
plt.title ("range of z")
plt.show ()


#npts = len(r)
## 10,895,780
#
## lines per file
#nlines = 100000
#start_increment = 10000
#nfiles = npts / (1.*start_increment)
#nfilemax = npts - nlines


spread = 0.1
step = 0.05

# plots histogram for some z range
# 0-10,000; 1,000-11,000; 2,000-12,000
for j in range (0, 0.35/step):
        start = step * j
        end = start + spread
        plt.hist (z[start < z <end], bins=25, range=(0, 0.35))
        plt.show ()
        
        
       
        

        
                