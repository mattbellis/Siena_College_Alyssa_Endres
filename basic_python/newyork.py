"""
Plotting boundaries of NYS
"""

import numpy as np
import matplotlib.pylab as plt
from numpy import random

#infile = open("C:\Users\Alyssa\Documents\GitHub\Siena_College_Alyssa_Endres\data\ny_boundaries.txt")

#infile = open("../data/ny_boundaries.txt")
#infile = open("../data/newyork_borders.txt")
#infile = open("../data/texas_border.txt")
infile = open("../data/wyoming_border.txt")
#latitude, longitude

vals = (np.array(infile.read().split())).astype(float)
nentries = len(vals)
ncols = 2
index = np.arange(0,nentries,2)
lat = vals[index]
lon = vals[index+1]

plt.plot(lon,lat,'k.',markersize=10)

xmin = min(lon) 
xmax = max(lon)
ymin = min(lat)
ymax = max(lat)




###############################################################################

#need 2 random numbers, (x, y)
#ranges btwn xmin, xmax, ymin, ymax

#random.uniform(a,b) -> range

npts = 1000
xpts = random.uniform(xmin,xmax,npts)
ypts = random.uniform(ymin,ymax,npts)



###############################################################################
# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.

   
def point_in_poly(x,y,poly):

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


x = 1
y = 1

#poly = [(0,0), (2,0), (2,2), (0,2)]    
poly = []
for x,y in zip(lon,lat):
    poly.append((x,y))

accpts = [[],[]]
rejpts = [[],[]]
for x,y in zip(xpts,ypts):
    if point_in_poly(x,y,poly):
        accpts[0].append(x)
        accpts[1].append(y)
    else:
        rejpts[0].append(x)
        rejpts[1].append(y)
        
#plt.figure()
plt.plot(accpts[0],accpts[1],'ro',markersize=4)
plt.plot(rejpts[0],rejpts[1],'bo',markersize=4)
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)