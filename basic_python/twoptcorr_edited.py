# 2-point correlation function

import math
import numpy as np
import matplotlib.pylab as plt

################################################################################
# Distances calculation
################################################################################
def distance(xpts0,ypts0,xpts1,ypts1,same='False'):

    npts0 = len(xpts0)
    npts1 = len(xpts1)

    N = 0
    if same is True:
        N=(npts0**2-npts0)/2
    else:
        N=npts0*npts1

    distances=np.zeros(N)    

    # Passed in the same arrays
    if same is True:
        i = 0
        index_start = 0
        index_end = npts-1
        for i in range(0,len(x)):

            dist_new = np.sqrt((x0[i] - x1[i+1:])**2 + (y0[i] - y1[i+1:])**2)
            #print len(dist_new)
            #print index_start,index_end
            distances[index_start:index_end] = dist_new[:]
            i += 1

            index_start += (npts-i)
            index_end = index_start + (npts-(i+1))

        print "len: %d" % (len(distances))

    # Two arrays are different
    else:
        for i in range(0,len(x)):

            dist_new = np.sqrt((x0[i] - x1)**2 + (y[i] - y1)**2)
            
            index = i*npts1
            index = (i+1)*npts1
            distances[index:index_end] = dist_new

        print "len: %d" % (len(distances))



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
        
    #plt.hist(distances,bins=100,range=(0,100))
    #plt.show()
distances=distance()
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
dd = plt.hist(distances,bins=25,range=(0,1.5))
N=(nptsd**2-nptsd)/2
DD = dd[0] / float(N)

###############################################################################


vals = (np.array(infiler.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
xr = vals[index]
yr = vals[index+1]

nptsr = len(xr)
        
def distance():
    #distances=[]
    N=(nptsr**2-nptsr)/2
    distances=np.zeros(N)    
    i=0
    j=0
    count=0
    for i in range (0,nptsr):
        for j in range (i+1,nptsr):
            x0=xr[i]
            y0=yr[i]
            x1=xr[j]
            y1=yr[j]
    
            sq1 = (x1-x0)**2
            sq2 = (y1-y0)**2
            dist = math.sqrt(sq1 + sq2)
            #distances.append(dist)
            distances[count]=dist
            count+=1            
            j+=1
        i+=1       
    return distances        
    #plt.hist(distances,bins=100,range=(0,100))
    #plt.show()
distances=distance()
plt.subplot(1,3,2)
rr = plt.hist(distances,bins=25,range=(0,1.5))
N=(nptsr**2-nptsr)/2
RR = rr[0] / float(N)





def distance():
    #distances=[]
    N=nptsr*nptsd
    distances=np.zeros(N)    
    i=0
    j=0
    count=0
    for i in range (0,nptsr):
        for j in range (0,nptsd):
            x0=xr[i]
            y0=yr[i]
            x1=xd[j]
            y1=yd[j]
    
            sq1 = (x1-x0)**2
            sq2 = (y1-y0)**2
            dist = math.sqrt(sq1 + sq2)
            #distances.append(dist)
            distances[count]=dist
            count+=1            
            j+=1
        i+=1       
    return distances        
    #plt.hist(distances,bins=100,range=(0,100))
    #plt.show()
distances=distance()
plt.subplot(1,3,3)
dr = plt.hist(distances,bins=25,range=(0,1.5))
N=nptsr*nptsd
DR = dr[0] / float(N)








W = (DD-2*DR+RR)/DD.astype('float')
print W

x=dd[1][:-1] +.015/2 #shifts to center of 
print len(W),len(x)

plt.figure()
plt.plot(x,W,'ko')

plt.show()



