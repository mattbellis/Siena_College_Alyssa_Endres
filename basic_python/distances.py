import math
import numpy as np
import matplotlib.pylab as plt

infile = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\sample_pop0.dat")

vals = (np.array(infile.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
x = vals[index]
y = vals[index+1]

npts = len(x)
        
def distance():
    #distances=[]
    N=(npts**2-npts)/2
    distances=np.zeros(N)    
    i=0
    j=0
    count=0
    for i in range (0,npts):
        for j in range (i+1,npts):
            x0=x[i]
            y0=y[i]
            x1=x[j]
            y1=y[j]
    
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
plt.hist(distances,bins=100,range=(0,1.5))
plt.show()        