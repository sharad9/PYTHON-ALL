import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.interpolate import griddata
import math
# domains
#x = np.logspace(-1.,np.log10(5),200) # [0.1, 5]
#y = np.linspace(6,9,200)             # [6, 9]
#z = np.linspace(-1,1,200)            # [-1, 1]



x=[]
y=[]
z=[]
z_=[]
with open('Book1.txt', "r") as f:
   Lines = f.readlines()# HERE "600" IS NUMBER OF UNITS TO BE READ,CAN BE CHANGED
   for l in Lines:
       
       a=str(l).replace("\t"," ").replace("\n","").split(" ")
       
       
       x.append(float(a[0]))
       
       y.append(float(a[1]))
       z.append(float(a[3]))
       z_.append(float(a[2]))






#convert to 2d matrices
z = np.array(z)


# 50x50
z_ = np.array(z_)
C = np.outer(z_.T,z_)    
X, Y = np.meshgrid(x, y)    # 50x50


Z = griddata( (x, y), z, (X, Y), method='cubic', fill_value = 0);
Z[Z < min(z)] = min(z)
#Z = np.outer(z.T,z)
C = griddata( (x, y), z_, (X,Y), method='cubic', fill_value = 0);
C[C < min(z_)] = min(z_);


# fourth dimention - colormap
# create colormap according to x-value (can use any 50x50 array)
color_dimension = C # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(color_dimension)

# plot
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

C = np.linspace(min(z_), max(z_), C.size).reshape(C.shape)
norm = matplotlib.colors.Normalize(minn, maxx)
scamap = plt.cm.ScalarMappable(cmap='inferno')
fcolors = scamap.to_rgba(C)
ax.plot_surface(X, Y, Z, facecolors=fcolors, cmap='inferno')
fig.colorbar(scamap)
plt.show()