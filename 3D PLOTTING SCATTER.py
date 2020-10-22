
# example of binary classification task
"""
from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
from matplotlib import pyplot
# define dataset
x, y = make_blobs(n_samples=10000, centers=8, random_state=1)
# summarize dataset shape
print(x.shape, y.shape)
# summarize observations by class label
counter = Counter(y)
print(counter)
# summarize first few examples
for i in range(10):
    print(x[i], y[i])
# plot the dataset and color the by class label
for label, _ in counter.items():
    row_ix = where(y == label)[0]
    pyplot.scatter(x[row_ix, 0], x[row_ix, 1], label=str(label))
pyplot.legend()
pyplot.show()
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.tri as mtri


x=[]
y=[]
z=[]
S=[]
with open('sfreq22.txt', "r") as f:
   Lines = f.readlines()# HERE "600" IS NUMBER OF UNITS TO BE READ,CAN BE CHANGED
   for l in Lines:
       
       a=str(l).replace("\t"," ").replace("\n","").split(" ")
       
       
       x.append(float(a[0]))
       
       y.append(float(a[1]))
       z.append(float(a[2]))
       S.append(float(a[3]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
c = z
Z=[]
for i in z:
    Z.append(i*50)
img=ax.scatter(x, y,S ,s=Z, c=z, alpha=1,marker="o", cmap=plt.hot())#edgecolor="skyblue"
plt.ylabel('Latitude',color='green',fontsize=12,fontweight="bold",fontstyle="normal")
plt.xlabel('longitude',color='red',fontsize=12,fontweight="bold",fontstyle="normal")




ax.set_zlabel('Site No',color='b',fontsize=12,fontweight="bold",fontstyle="normal");
surf=ax.plot_trisurf(x, y,S ,cmap="YlGnBu", alpha=0.3, linewidth = 0.2);
#surf.set_array(colors); surf.autoscale();
cbar = fig.colorbar(surf, shrink=0.75, aspect=10,pad = 0.05, orientation = 'horizontal');
cbar.ax.set_xlabel("ABCD", rotation = 0);
#ax.plot(x, y,z, 'green', lw=1)
#ax.grid(which='minor', color="#FF00FF", linestyle='solid',axis='x')
#ax.grid(which='minor', color='blue', linestyle='solid',axis='y')
#ax.grid(which='minor', color='blue', linestyle='solid',axis='z')
#plt.grid(color="#FF00FF", which='major', axis='x')
#plt.grid(color="blue", which='major', axis='y')
#plt.grid(color="blue", which='major', axis='z')
ax.w_xaxis.pane.set_color("m");
ax.w_yaxis.pane.set_color('w');
ax.w_zaxis.pane.set_color('grey');

plt.colorbar(img).set_label('Frequency(Hz)',fontsize=16,fontweight="bold",fontstyle="normal")
plt.show()

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


x=[]
y=[]
z=[]
with open('sfreq22.txt', "r") as f:
   Lines = f.readlines()# HERE "600" IS NUMBER OF UNITS TO BE READ,CAN BE CHANGED
   for l in Lines:
       
       a=str(l).replace("\t"," ").replace("\n","").split(" ")
       
       
       x.append(float(a[0]))
       
       y.append(float(a[1]))
       z.append(float(a[2]))
       

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
c = z
Z=[]
for i in z:
    Z.append(i*50)
img=ax.scatter(x, y, z,s=Z, c=c, alpha=1,marker="o", cmap=plt.hot())#edgecolor="skyblue"
plt.ylabel('Longitude',color='green',fontsize=12,fontweight="bold",fontstyle="normal")
plt.xlabel('Latitude',color='red',fontsize=12,fontweight="bold",fontstyle="normal")




ax.set_zlabel('Frequency',color='k',fontsize=12,fontweight="bold",fontstyle="normal")
#ax.plot(x, y,z, 'green', lw=1)
#ax.grid(which='minor', color="#FF00FF", linestyle='solid',axis='x')
#ax.grid(which='minor', color='blue', linestyle='solid',axis='y')
#ax.grid(which='minor', color='blue', linestyle='solid',axis='z')
#plt.grid(color="#FF00FF", which='major', axis='x')
#plt.grid(color="blue", which='major', axis='y')
#plt.grid(color="blue", which='major', axis='z')
ax.w_xaxis.pane.set_color("m");
ax.w_yaxis.pane.set_color('w');
ax.w_zaxis.pane.set_color('k');

plt.colorbar(img).set_label('Frequency(Hz)',fontsize=16,fontweight="bold",fontstyle="normal")
plt.show()
"""
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
a=[]
b=[]
c=[]
with open('xxxxx.txt', "r") as f:
   Lines = f.readlines()# HERE "600" IS NUMBER OF UNITS TO BE READ,CAN BE CHANGED
   for l in Lines:
       
       a=a=str(l).replace("\t"," ").replace("\n","").split(" ")
       
       a=a[:1]
       b=[float(i) for i in a]
       altitude.append(b)
x =a
y =b
z =c



ax.scatter(x, y, z,s=10, c="b", alpha=1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
#ax.plot(x, y,z, 'green', lw=1)
ax.grid(which='minor', color="#FF00FF", linestyle='solid',axis='x')
ax.grid(which='minor', color='blue', linestyle='solid',axis='y')
plt.grid(color="#FF00FF", which='major', axis='x')
plt.grid(color="blue", which='major', axis='y')
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

altitude=[]

a,b,c=np.loadtxt("SCATTER.txt", delimiter=",",  skiprows=0, usecols=(0,1,2), unpack=3, ndmin=0, encoding='bytes', max_rows=None)

       
print(a)
x=b
y=a
# Lines on top of scatter
fig, ax = plt.subplots(figsize=(10, 8))

i=np.arange(min(x),max(x),0.05)


ax.plot(x, y, 'green', lw=1)
ax.scatter(x, y, s=10, c="r", alpha=0.5)
#
plt.ylabel('y-axis',color='#9E0508',fontsize=20,fontweight="bold",fontstyle="normal")
plt.xlabel('x-axis',color='#9E0508',fontsize=20,fontweight="bold",fontstyle="normal")
l = plt.legend("xy")
l.set_zorder(20)  # put the legend on top
#ax.xticks(i)

# Change minor ticks to show every 5. (20/4 = 5)
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
# Turn grid on for both major and minor ticks and style minor slightly
# differently.
#ax.grid(which='major', color='green', linestyle='--')
ax.grid(which='minor', color="#FF00FF", linestyle='solid',axis='x')
ax.grid(which='minor', color='blue', linestyle='solid',axis='y')

plt.grid(color="#FF00FF", which='major', axis='x')
plt.grid(color="blue", which='major', axis='y')
plt.show()
"""
