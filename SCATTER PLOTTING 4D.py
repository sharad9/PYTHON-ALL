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