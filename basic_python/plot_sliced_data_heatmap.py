################################################################################
# This is a very fast way of reading in a text file, when
# you know how the data is formatted, e.g. how many columns
# there are.
# 
# Depending on the size of the file, this still may take some time (~5-20 sec),
# but is still faster than other traditional ways of reading in files.
#
# The trade-off is that this method works best when you have a good amount of 
# memory (RAM) available.
################################################################################

import matplotlib.pyplot as plt
import numpy as np

import sys

# We need to give the full path to the directory. This will obviously be 
# different on your machine, so you will want to edit this by hand. 
#infile = open('/home/bellis/Work/Astronomy/catalogs/Wechsler/wechsler_gals.cat')
infile = open(sys.argv[1])
tag = int(sys.argv[2])

# This command will take the entire file, split it into different values using
# whitespace (tab,space,end-of-line), and iterpret the entries as floats 
# (as opposed to strings, characters, or integers).
content = np.array(infile.read().split()).astype('float')

# Now we have this *huge* array. We want to pull out the values we want. 
# In this case, we know that the columns are RA, Dec, and z. 

# First, how big is this array.
nentries = len(content)

# Next, how many galaxies are in this file?
ncolumns = 2
ngals = nentries/ncolumns
print "# galaxies: %d" % (ngals)

# Now we just need to make an array that has the index of each value we
# want to extract. 
index = np.arange(1,nentries,ncolumns)
# So for three columns, this index array looks like
# [0,3,6,9,12,...,nentries-2]
# We can use this now to pull out the columns we want!
ra =  content[index]
dec = content[index+1]

# Let's make sure these arrays at least have the same size.
print "\nNumber of entries in coordinate arrays"
print "# ra coords:  %d" % (len(ra))
print "# dec coords: %d" % (len(dec))

# And just for the heck of it, we can dump the first 5 entries of each array.
print "\nFirst five entries in arrays."
print ra[0:5]
print dec[0:5]
print "\n"

# Convert arcseconds back to degrees
ra /= 3600.0
dec /= 3600.0

theta = np.deg2rad(ra)
phi = np.deg2rad(90-dec)

x = theta
y = np.cos(phi)
#z = radius*np.sin(phi)

# Plotting RA vs. Dec
fig = plt.figure(figsize=(1.618*5,5),dpi=(100))
ax = fig.add_subplot(1,1,1)
fig.subplots_adjust(top=0.95,bottom=0.15,right=0.99,left=0.05)
#ax = plt.subplot(111,polar=True)
#ax = fig.add_axes([0.1, -0.75, 0.8, 1.6], projection='polar')
#ax = fig.add_axes([0.1, -0.75, 0.8, 1.6])

# Heat map
heatmap, xedges, yedges = np.histogram2d(x, y, bins=700)
#heatmap, xedges, yedges = np.histogram2d(x, y, bins=200)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#print heatmap
#print xedges
#print yedges

#exit()

#print "EXTENT:" 
#print extent

heatmap = np.log10(heatmap)

print type(heatmap)
print max(map(max,heatmap))

#plt.clf()
#plt.imshow(heatmap,extent=extent,cmap=plt.cm.winter)
#plt.imshow(heatmap,extent=extent,cmap=plt.cm.autumn,vmin=0.01,vmax=2.5)
#plt.imshow(heatmap,extent=extent,cmap=plt.cm.bone)
ax.imshow(heatmap,extent=extent,cmap=plt.cm.jet,vmin=0,vmax=2.8) # log10 binning
#ax.imshow(heatmap,extent=extent,cmap=plt.cm.Dark2,vmin=0,vmax=2.8) # log10 binning
#ax.imshow(heatmap,extent=extent,cmap=plt.cm.jet,vmin=0,vmax=1000) # normal binning

# Draw plot
ax.set_title('RA v. Dec for slices of Z')
ax.set_xlabel('Right Ascension')
ax.set_ylabel('Declination')


# Save plot file
name = "Plots/slice_%04d.png" % (tag)
fig.savefig(name)

#plt.show()
