# 2-point correlation function

import numpy as np
import matplotlib.pylab as plt

################################################################################
# Distances calculation
################################################################################
def distance(x0,y0,x1,y1,same=False):
    #print x0,y0,x1,y1,same

    npts0 = len(x0)
    npts1 = len(x1)

    N = 0
    if same is True:
        N=(npts0**2-npts0)/2
    else:
        N=npts0*npts1

    distances=np.zeros(N)    

    i = 0
    index_start = 0
    index_end = npts1-1

    if same is False:
        index_end = npts1

    # Passed in the same arrays
    if same is True:
        i = 0
        index_start = 0
        index_end = npts1-1
        for i in range(0,npts0):

            dist_new = np.sqrt((x0[i] - x1[i+1:])**2 + (y0[i] - y1[i+1:])**2)
            #print len(dist_new)
            #print index_start,index_end
            distances[index_start:index_end] = dist_new[:]
            i += 1

            index_start += (npts1-i)
            index_end = index_start + (npts1-(i+1))

        print "len: %d" % (len(distances))

    # Two arrays are different
    else:
        for i in range(0,npts0):

            dist_new = np.sqrt((x0[i] - x1)**2 + (y0[i] - y1)**2)
            
            index = i*npts1
            index_end = (i+1)*npts1
            distances[index:index_end] = dist_new

            index_start += npts1
            index_end = index_start + npts1


        print "len: %d" % (len(distances))

    return distances



################################################################################
# Read in the data.
################################################################################
#infiled = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop1.dat")
infiled = open("../data/sample_pop1.dat")
#infiler = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop0.dat")
infiler = open("../data/sample_pop0.dat")

vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
xd = vals[index]
yd = vals[index+1]

nptsd = len(xd)


vals = (np.array(infiler.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
xr = vals[index]
yr = vals[index+1]

nptsr = len(xr)

        
################################################################################
# Do the calculations
################################################################################
plt.figure(figsize=(15,5))

print "Starting DD........."
distances=distance(xd,yd,xd,yd,same=True)
plt.subplot(1,3,1)
dd = plt.hist(distances,bins=100,range=(0,1.5))
plt.xlim(0,1.5)
N=((nptsd**2)-nptsd)/2.0
print "DD norm: ",N
DD = dd[0] / float(N)

print "Starting RR........."
distances=distance(xr,yr,xr,yr,same=True)
plt.subplot(1,3,2)
rr = plt.hist(distances,bins=100,range=(0,1.5))
plt.xlim(0,1.5)
N=((nptsr**2)-nptsr)/2.0
print "RR norm: ",N
RR = rr[0] / float(N)


print "Starting DR........."
distances=distance(xd,yd,xr,yr,same=False)
plt.subplot(1,3,3)
plt.xlim(0,1.5)
dr = plt.hist(distances,bins=100,range=(0,1.5))
N=nptsr*nptsd
print "DR norm: ",N
DR = dr[0] / float(N)

W = (DD-(2*DR)+RR)/RR.astype('float')
print W

x=dd[1][:-1] +(dd[1][1]-dd[1][0])/2.0 #shifts to center of 
print len(W),len(x)

i = 10
print dd[1][i],DD[i],RR[i],DR[i],W[i]

plt.figure()
plt.plot(x,W,'ko')
plt.ylim(-5,15)

plt.show()



