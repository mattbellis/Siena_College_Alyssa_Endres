# wechsler_gals_100k
# columns are right ascension, declination, z redshift

import numpy as np
import matplotlib.pylab as plt

#infiled = open("C:\Users\Alyssa\Dropbox\Astro data\Wechsler data\wechsler_gals.cat")
#infiled = open("/data/Astronomy/catalogs/Wechsler//wechsler_gals.cat")
infiled = open("/data/MICE/586/z_586_uniq.dat")


vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
print vals[10]
ncols = 2
index = np.arange(0,nentries,ncols)
n = vals[index]
z = vals[index+1]
#n,z = np.loadtxt(infiled,usecols=(0,1))

# plot histogram of z values
print z[0:100]
print z[-100:]

z_width = 0.01
z_step = 0.005

z_min = 0.0
z_max = 0.5

nslices = int((z_max-z_min)/z_step)

#for i in range(0,nslices):
for i in range(0,1):

    print "nslices: ",i,nslices
    
    fig = plt.figure(figsize=(1.618*5,5),dpi=100)
    ax = fig.add_subplot(1,1,1)

    fig.subplots_adjust(top=0.95,bottom=0.15,right=0.99,left=0.15)

    ax.hist (z, bins=nslices, range=(z_min,z_max),histtype='stepfilled',weight=n)
    #ax.set_title ("range of z")

    cut_index0 = z>z_min + i*z_step
    cut_index1 = z<z_min + i*z_step + z_width
    ax.hist(z[cut_index0*cut_index1],bins=nslices,range=(z_min,z_max),histtype='stepfilled')

    title = "z=%4.2f-%4.2f" % (z_min + i*z_width,z_min + (i+1)*z_width)
    ax.set_title(title)
    ax.set_ylabel("# galaxies")
    ax.set_xlabel("z (redshift)")
    ax.set_xlim(0,0.35)
    plt.show()

    #rdum = r[cut_index0*cut_index1]
    #ddum = d[cut_index0*cut_index1]

    #filename = "galaxy_slices/output_wechsler_%04d.dat" % (i)

    #output=open(filename,'w')
    #output.write('%d\n'%(len(rdum)))

    #for ir,idec in zip(rdum,ddum):
        #output.write('%6.5e %6.5e\n'%(ir,idec))
    #output.close()

    name = "Plots/mice_zslice_hist_%04d.png" % (i)
    fig.savefig(name)
