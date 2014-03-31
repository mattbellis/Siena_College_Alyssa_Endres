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
x,y,z = np.loadtxt(sys.argv[1],skiprows=1,usecols=(0,1,2),unpack=True)

tag = ""
if sys.argv[1].find('NY')>=0:
    tag = "NY"
elif sys.argv[1].find('GA')>=0:
    tag = "GA"
elif sys.argv[1].find('WY')>=0:
    tag = "WY"

if sys.argv[1].find('flat')>=0:
    tag = "%s_flat" % (tag)

# This command will take the entire file, split it into different values using
# whitespace (tab,space,end-of-line), and iterpret the entries as floats 
# (as opposed to strings, characters, or integers).


# And just for the heck of it, we can dump the first 5 entries of each array.
print "\nFirst five entries in arrays."
print x[0:5]
print y[0:5]
print z[0:5]
print "\n"

# Plotting RA vs. Dec
fig = plt.figure(figsize=(14,9))
ax = plt.subplot(1,1,1)
#ax = plt.subplot(111,polar=True)
#ax = fig.add_axes([0.1, -0.75, 0.8, 1.6], projection='polar')
#ax = fig.add_axes([0.1, -0.75, 0.8, 1.6])

# Heat map
heatmap, xedges, yedges = np.histogram2d(-y, x, bins=500)
#heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]

heatmap = np.log10(heatmap)

plt.clf()
#plt.imshow(heatmap,extent=extent,cmap=plt.cm.winter)
#plt.imshow(heatmap,extent=extent,cmap=plt.cm.autumn)
#plt.imshow(heatmap,extent=extent,cmap=plt.cm.bone)
plt.imshow(heatmap,extent=extent,cmap=plt.cm.jet)

# Draw plot
#ax.set_title('RA v. Dec for slices of Z')
#ax.set_xlabel('Right Ascension')
#ax.set_ylabel('Declination')

fig.subplots_adjust(left=0.05,right=0.99,wspace=0.00,hspace=0.00)

plt.axis('off')

# Save plot file
name = "Plots/pop_state_%s.png" % (tag)
fig.savefig(name)

plt.show()
