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

# plot histogram of z values
print z[0:100]
print z[-100:]

z_width = 0.01

z_min = 0.0
z_max = 0.35

nslices = int((z_max-z_min)/z_width)

for i in range(0,nslices):

    print "nslices: ",i,nslices
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)


    ax.hist (z, bins=nslices, range=(z_min,z_max))
    #ax.set_title ("range of z")

    cut_index0 = z>z_min + i*z_width
    cut_index1 = z<z_min + i*z_width + 0.03
    ax.hist(z[cut_index0*cut_index1],bins=nslices,range=(z_min,z_max))

    title = "z=%4.2f-%4.2f" % (z_min + i*z_width,z_min + (i+1)*z_width)
    ax.set_title(title)
    ax.set_xlabel("z (redshift)")
    #plt.show()

    rdum = r[cut_index0*cut_index1]
    ddum = d[cut_index0*cut_index1]

    filename = "galaxy_slices/output_wechsler_%04d.dat" % (i)

    output=open(filename,'w')
    output.write('%d\n'%(len(rdum)))

    for ir,idec in zip(rdum,ddum):
        output.write('%6.5e %6.5e\n'%(ir,idec))
    output.close()





'''
spread = 0.1
step = 0.05

# plots histogram for some z range
# 0-10,000; 1,000-11,000; 2,000-12,000
for j in range (0, 0.35/step):
start = step * j
end = start + spread
plt.hist (z[start < z <end], bins=25, range=(0, 0.35))
plt.show ()



'''




