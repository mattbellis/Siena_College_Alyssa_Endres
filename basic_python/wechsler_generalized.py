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

# sort galxies by z, return indices
sorted_indices = np.argsort(z)
r_sort = r[sorted_indices]
d_sort = d[sorted_indices]
z_sort = z[sorted_indices]

# plot histogram of z values
print z[0:100]
print z[-100:]
plt.hist(z,bins=50)
#plt.xlim(0,5)
plt.title("Sample Pop 0 y")
plt.show()


## IndexError: index 10895781 is out of bounds for size 10895780


#npts = len(r)
#
## lines per file
#nlines = 10000
#start_increment=1000
#nfiles=npts/(1.*start_increment)
#nfilemax=npts-nlines
#
#
## ourput file- z, r, d
#for j in range (0,91):
#    #filename = 'C:\Users\Alyssa\Documents\Python Scripts\wechsler'+'output_'+str(j)+'.dat'
#    filename = 'output_wechsler'+'output_'+str(j)+'.dat'
#    output=open(filename,'w')
#    for i in range(nlines):    
#        index=start_increment*j+i    
#        if index > (npts-1):
#            break
#        output.write('%6.5e %6.5e %6.5e \n'%(z[sorted_indices[index]],r[sorted_indices[index]],d[sorted_indices[index]]))
#    output.close()
#        
#                


