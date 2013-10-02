import numpy as np
import matplotlib.pylab as plt

infile = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop0.dat")

vals = (np.array(infile.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
x = vals[index]
y = vals[index+1]

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)

# plots positions
plt.plot(x,y,'o',markersize=1.0)
plt.xlim(0,1)
plt.ylim(0,1)
plt.title("Sample Pop 0")

# histogram in x
plt.subplot(1,3,2)
plt.hist(x,bins=20,range=(0,1))
plt.title("Sample Pop 0 x")

# histogram in y
plt.subplot(1,3,3)
plt.hist(y,bins=20,range=(0,1))
plt.title("Sample Pop 0 y")
plt.show()


##############################################################
infile = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop1.dat")

vals = (np.array(infile.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
x = vals[index]
y = vals[index+1]

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)

# plots positions
plt.plot(x,y,'o',markersize=1.0)
plt.xlim(0,1)
plt.ylim(0,1)
plt.title("Sample Pop 1")

# histogram in x
plt.subplot(1,3,2)
plt.hist(x,bins=100,range=(-1,2))
plt.title("Sample Pop 1 x")

# histogram in y
plt.subplot(1,3,3)
plt.hist(y,bins=100,range=(-1,2))
plt.title("Sample Pop 1 y")
plt.show()

