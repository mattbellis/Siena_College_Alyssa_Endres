# wechsler_gals_100k
# columns are right ascension, declination, z redshift

import math
import numpy as np
import matplotlib.pylab as plt

import sys

#infiled = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\wechsler_gals_100k.dat")
#infiled = open("../data/wechsler_gals_100k.dat")
infiled = open(sys.argv[1])

vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]

npts = len(r)

ngalaxies = nentries/3

print "ngalaxies: ",ngalaxies

# indicies of sorted values
sorted_indices = np.argsort(z)


# lines per file
nlines_per_file = 1000000
increment = 100000

# ourput file- z, r, d
end_line = increment
j = 0
while end_line <= ngalaxies + increment:
    #filename = 'C:\Users\Alyssa\Documents\Python Scripts\wechsler'+'output_'+str(j)+'.dat'
    filename = 'galaxy_slices/output_wechsler'+'output_'+str(j)+'.dat'

    print j

    output=open(filename,'w')
    for i in range(nlines_per_file):    
        index=increment*j+i    
        if index > (npts-1):
            break
        output.write('%6.5e %6.5e %6.5e \n'%(r[sorted_indices[index]],d[sorted_indices[index]], z[sorted_indices[index]]))
    output.close()
        
    end_line += increment
    j += 1
                


