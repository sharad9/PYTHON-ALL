from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pylab as pl
from PIL import Image
import numpy as np
import pylab

img = Image.open('corona.jpg').convert('L')
z   = np.asarray(img)
#slice notation: "start:stop:step" - here it's referring to the z matrix's x and y dimensions, get the whole of each
mydata = z[::1,::1]
fig = pl.figure(facecolor='w')
# subplot(nrows, ncols, plotnumber)
ax1 = fig.add_subplot(1,2,1)
# im = ax1.imshow(mydata,interpolation='nearest',cmap=pl.cm.jet)
im = ax1.imshow(mydata,interpolation='none',cmap=pl.cm.jet)
ax1.set_title('2D')
zipper=[1 for i in range(190)]
ax2 = fig.add_subplot(1,2,2,projection='3d')
x,y = np.mgrid[:mydata.shape[0],:mydata.shape[1]]
ax2.plot_surface(x,y,zipper,cmap=pl.cm.jet,rstride=10,cstride=10,linewidth=0,antialiased=False)
ax2.set_title('3D')
ax2.set_zlim3d(0,255)
pl.show()