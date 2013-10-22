# wechsler_gals_100k
# columns are right ascension, declination, z redshift

import math
import numpy as np
import matplotlib.pylab as plt

infiled = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\wechsler_gals_100k.dat")

vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]

npts = len(r)

# indicies of sorted values
sorted_indices = np.argsort(z)


# lines per file
nlines = 10000
start_increment=1000
nfiles=npts/(1.*start_increment)
nfilemax=npts-nlines


# ourput file- z, r, d
for j in range (0,91):
    filename = 'C:\Users\Alyssa\Documents\Python Scripts\wechsler'+'output_'+str(j)+'.dat'
    output=open(filename,'w')
    for i in range(nlines):    
        index=start_increment*j+i    
        if index > (npts-1):
            break
        output.write('%6.5e %6.5e %6.5e \n'%(z[sorted_indices[index]],r[sorted_indices[index]],d[sorted_indices[index]]))
    output.close()
        
                


