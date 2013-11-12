# wechsler_gals_100k
# columns are right ascension, declination, z redshift

import numpy as np
import matplotlib.pylab as plt

#infiled = open("C:\Users\Alyssa\Dropbox\Astro data\Wechsler data\wechsler_gals.cat")
infiled = open("/data/Astronomy/catalogs/Wechsler//wechsler_gals.cat")


vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]

<<<<<<< HEAD
# plot histogram of all z values
plt.hist (z, bins=50, range=(0, 0.35))
plt.title ("range of z")
plt.show ()
=======
# sort galxies by z, return indices
sorted_indices = np.argsort(z)
r_sort = r[sorted_indices]
d_sort = d[sorted_indices]
z_sort = z[sorted_indices]

# plot histogram of z values
print z[0:100]
print z[-100:]
plt.hist(z,bins=50,range=(0.0,0.4))
cut_index0 = z>0.1
cut_index1 = z<0.2
plt.hist(z[cut_index0*cut_index1],bins=50,range=(0.0,0.4))
#plt.xlim(0,5)
plt.title("Sample Pop 0 y")
plt.show()


## IndexError: index 10895781 is out of bounds for size 10895780
>>>>>>> 79a2b17093c51af19ebafb9bb76527a24e7fcc24


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
        
        
       
        

        
                
