# code to generate the two-point correlation with the wechsler galaxy data looping over all the files to create time slices

import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot

#infiledd = open("../data/log10binning_GPU_10k_data_data_arcmin.dat")
#infileff = open("../data/log10binning_GPU_10k_flat_flat_arcmin.dat")
#infiledf = open("../data/log10binning_GPU_10k_data_flat_arcmin.dat")


for i in range (0,26):

    print i

    #dirname = './'
    dirname = '../data/'
    tag = "%04d" % (i)

    name = "%s/log10binning_GPU_%s_data_data_arcmin.dat" % (dirname,tag)
    infiledd = open(name)
    name = "%s/log10binning_GPU_%s_data_flat_arcmin.dat" % (dirname,tag)
    infiledf = open(name)
    name = "%s/log10binning_GPU_%s_flat_flat_arcmin.dat" % (dirname,tag)
    infileff = open(name)


    # data-data
    vals = (np.array(infiledd.read().split())).astype(float)
    nentries = len(vals)
    ncols = 3
    index = np.arange(0,nentries,3)
    dd_th_hi = vals[index]
    dd_th_lo = vals[index+1]
    dd = vals[index+2]
    
    dd /= sum(dd)

    dd_th_avg = (dd_th_hi + dd_th_lo) / 2


    # data-flat
    vals = (np.array(infiledf.read().split())).astype(float)
    nentries = len(vals)
    ncols = 3
    index = np.arange(0,nentries,3)
    df_th_hi = vals[index]
    df_th_lo = vals[index+1]
    df = vals[index+2]
    
    df /= sum(df)
    
    df_th_avg = (df_th_hi + df_th_lo) / 2
    
    
    # flat-flat
    vals = (np.array(infileff.read().split())).astype(float)
    nentries = len(vals)
    ncols = 3
    index = np.arange(0,nentries,3)
    ff_th_hi = vals[index]
    ff_th_lo = vals[index+1]
    ff = vals[index+2]
    
    ff /= sum(ff)
    
    ff_th_avg = (ff_th_hi + ff_th_lo) / 2
    
    
    # calculate the two-point correlation function
    W = (dd-(2*df)+ff)/ff.astype('float')
    #print W
    
    
    plt.figure()
    plt.plot(dd_th_avg,W,'ko')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.ylim(0.001,20)
    plt.xlabel("arcseconds")
    plt.ylabel(r"w ($\theta$)")
    plt.title("W %s" % (tag))
    plt.savefig('log10binning_GPU_%s_W.png'  % (tag) , bbox_inches='tight')
    
    #plt.show()