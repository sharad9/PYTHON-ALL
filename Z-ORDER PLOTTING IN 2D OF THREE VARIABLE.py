mport matplotlib.pyplot as plt
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