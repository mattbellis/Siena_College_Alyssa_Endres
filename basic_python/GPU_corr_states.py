# code to generate the two-point correlation with the wechsler galaxy data looping over all the files to create time slices

import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot

import sys

#dirname = './'
dirname = '/home/bellis//ccogs/angular_correlation/examples'
#state = 'GA'
state = 'NY'
if len(sys.argv)>1:
    state = sys.argv[1]

#tag = "1Mflat"
tag = "1Mdata"
#bintype = "log"
#binwidth = "0.04"
#bintype = "norm"
#binwidth = "2k"
bintype = "norm"
binwidth = "200"
#binwidth = "2k"

#infiledd = open("../data/log10binning_GPU_10k_data_data_arcmin.dat")
#infileff = open("../data/log10binning_GPU_10k_flat_flat_arcmin.dat")
#infiledf = open("../data/log10binning_GPU_10k_data_flat_arcmin.dat")


#################### total number of calculations on GPU
#infile_num_calc = open("../data/num_calculations.txt")

#vals = (np.array(infile_num_calc.read().split())).astype(float)
#nentries = len(vals)
#ncols = 1
#index = np.arange(0,nentries,1)
#count_calc = vals[index]

#num_calculations = sum(count_calc)
#num_calculations = 100000
# print num_calculations
# 3.10748804901e+13

###################### number of data galaxies
#infile_num_data = open("../data/numbers_of_data_galaxies.txt")

#vals = (np.array(infile_num_data.read().split())).astype(float)
#nentries = len(vals)
#ncols = 1
#index = np.arange(0,nentries,1)
#count_data = vals[index] - 1
count_data = 1000000

###################### number of flat galaxies
#infile_num_flat = open("../data/numbers_of_flat_galaxies.txt")

#vals = (np.array(infile_num_flat.read().split())).astype(float)
#nentries = len(vals)
#ncols = 1
#index = np.arange(0,nentries,1)
#count_flat = vals[index]
count_flat = 100000
if state=="GA":
    count_flat = 1335659
elif state=="NY":
    count_flat = 1186634
elif state=="WY":
    count_flat = 1096036
    count_data = 563626


print "# data: %d" % (count_data)
print "# flat: %d" % (count_flat)

######################### calculate 2 pt corr function
for i in range (0,1):

    #print i


    N_dd = float(count_data**2.0 - count_data) / 2.0
    N_ff = float(count_flat**2.0 - count_flat) / 2.0
    N_df = float(count_data * count_flat)


    name = "%s/%sbinning_%s_%sbins_%s_data_data_arcmin.dat" % (dirname,bintype,state,binwidth,tag)
    infiledd = open(name)
    name = "%s/%sbinning_%s_%sbins_%s_data_flat_arcmin.dat" % (dirname,bintype,state,binwidth,tag)
    infiledf = open(name)
    name = "%s/%sbinning_%s_%sbins_%s_flat_flat_arcmin.dat" % (dirname,bintype,state,binwidth,tag)
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
    pyplot.ylim(0.10)
    #pyplot.ylim(7.00,100000)
    pyplot.ylim(0.01,10000000)
    plt.xlabel("meters")
    plt.ylabel(r"w (m)")
    plt.title("W %s %s" % (tag,state))
    plt.savefig('../data/log10binning_%s_%s_W.png'  % (tag,state) , bbox_inches='tight')

    plt.show()
