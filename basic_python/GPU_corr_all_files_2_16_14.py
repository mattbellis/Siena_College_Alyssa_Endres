# code to generate the two-point correlation with the wechsler galaxy data looping over all the files to create time slices

import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot

#infiledd = open("../data/log10binning_GPU_10k_data_data_arcmin.dat")
#infileff = open("../data/log10binning_GPU_10k_flat_flat_arcmin.dat")
#infiledf = open("../data/log10binning_GPU_10k_data_flat_arcmin.dat")


#################### total number of calculations on GPU
#infile_num_calc = open("../data/num_calculations.txt")
#
#vals = (np.array(infile_num_calc.read().split())).astype(float)
#nentries = len(vals)
#ncols = 1
#index = np.arange(0,nentries,1)
#count_calc = vals[index]
#
#num_calculations = sum(count_calc)
# print num_calculations
# 3.10748804901e+13

###################### number of data galaxies
infile_num_data = open("../data/data_counts.txt")

vals = (np.array(infile_num_data.read().split())).astype(str)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,ncols)
count_data = vals[index]
count_data = count_data.astype(float)

###################### number of flat galaxies
infile_num_flat = open("../data/flat_counts.txt")

vals = (np.array(infile_num_flat.read().split())).astype(str)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,ncols)
count_flat = vals[index]
count_flat = count_flat.astype(float)


######################### calculate 2 pt corr function
#for i in range (0,33):
for i in range (134,143):
    #print i


    N_dd = (count_data[i]**2.0 - count_data[i]) / 2.0
    N_ff = (count_flat[i]**2.0 - count_flat[i]) / 2.0
    N_df = count_data[i] * count_flat[i]


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
    dd = vals[index+2] / N_dd
    
    ##dd /= sum(dd)

    dd_th_avg = (dd_th_hi + dd_th_lo) / 2


    # data-flat
    vals = (np.array(infiledf.read().split())).astype(float)
    nentries = len(vals)
    ncols = 3
    index = np.arange(0,nentries,3)
    df_th_hi = vals[index]
    df_th_lo = vals[index+1]
    df = vals[index+2] / float(N_df)
    
    ##df /= sum(df)
    
    df_th_avg = (df_th_hi + df_th_lo) / 2
    
    
    # flat-flat
    vals = (np.array(infileff.read().split())).astype(float)
    nentries = len(vals)
    ncols = 3
    index = np.arange(0,nentries,3)
    ff_th_hi = vals[index]
    ff_th_lo = vals[index+1]
    ff = vals[index+2] / N_ff
    
    ##ff /= sum(ff)
    
    ff_th_avg = (ff_th_hi + ff_th_lo) / 2
    
    
    # calculate the two-point correlation function
    W = (dd-(2*df)+ff)/ff.astype('float')
    #print W
    
    
    plt.figure()
    plt.plot(dd_th_avg,W,'ko')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.ylim(0.001,1000)
    plt.xlabel("arcseconds")
    plt.ylabel(r"w ($\theta$)")
    plt.title("W %s" % (tag))
    plt.savefig('../data/log10binning_GPU_%s_W.png'  % (tag) , bbox_inches='tight')
