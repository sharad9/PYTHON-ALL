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

ax.scatter(x, y, z,s=10, c="b", alpha=1,marker="o", edgecolor="skyblue")
plt.ylabel('Longitude',color='green',fontsize=12,fontweight="bold",fontstyle="normal")
plt.xlabel('Latitude',color='red',fontsize=12,fontweight="bold",fontstyle="normal")


ax.set_zlabel('Frequency',color='k',fontsize=12,fontweight="bold",fontstyle="normal")
ax.plot(x, y,z, 'green', lw=1)
#ax.grid(which='minor', color="#FF00FF", linestyle='solid',axis='x')
#ax.grid(which='minor', color='blue', linestyle='solid',axis='y')
#ax.grid(which='minor', color='blue', linestyle='solid',axis='z')
#plt.grid(color="#FF00FF", which='major', axis='x')
#plt.grid(color="blue", which='major', axis='y')
#plt.grid(color="blue", which='major', axis='z')
ax.w_xaxis.pane.set_color("m");
ax.w_yaxis.pane.set_color('w');
ax.w_zaxis.pane.set_color('k');


plt.show()