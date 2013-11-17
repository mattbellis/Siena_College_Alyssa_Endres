

infiled = open("log10binning_GPU_10k_data_data_arcmin.dat")
vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]



infiled = open("log10binning_GPU_10k_data_flat_arcmin.dat")
vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]


infiled = open("log10binning_GPU_10k_flat_flat_arcmin.dat")
vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 3
index = np.arange(0,nentries,3)
r = vals[index]
d = vals[index+1]
z = vals[index+2]


