import math
import numpy as np
import matplotlib.pylab as plt

infiled = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop1_10k.dat")

vals = (np.array(infiled.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
xd = vals[index]
yd = vals[index+1]

nptsd = len(xd)
        
def distance():
    #distances=[]
    N=(nptsd**2-nptsd)/2
    distances=np.zeros(N)    
    i=0
    j=0
    count=0
    for i in range (0,nptsd):
        for j in range (i+1,nptsd):
            x0=xd[i]
            y0=yd[i]
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
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
dd = plt.hist(distances,bins=25,range=(0,1.5))
N=(nptsd**2-nptsd)/2
DD = dd[0] / float(N)

###############################################################################

infiler = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop0_10k.dat")

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



