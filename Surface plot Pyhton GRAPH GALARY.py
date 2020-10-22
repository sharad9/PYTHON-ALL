

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#from pandas import read_excel

# Get the data (csv file is hosted on the web)
url = 'Book1.xlsx'
#data = pd.read_csv(url)

file_name = url
xl_file = pd.ExcelFile(file_name)
df = pd.read_excel(file_name, sheet_name ="Sheet1")


#df = {sheet_name: xl_file.parse(sheet_name) 
#          for sheet_name in xl_file.sheet_names}


print(df.head())
data = xl_file;
# Transform it to a long format
##df=data.unstack().reset_index()
#df.columns=["long"      ,"lat"         ,"Vel"]
 
# And transform the old column name in something numeric
#df['lat']=pd.Categorical(df['X'])
#df['lat']=df['X'].cat.codes
 
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['long'], df['lat'], df['Vel'], cmap=plt.cm.viridis, linewidth=2)
#plt.show()
 
# to Add a color bar which maps values to colors.
surf=ax.plot_trisurf(df['long'], df['lat'], df['Vel'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, aspect=5)
plt.show()
 
# Rotate it
ax.view_init(30, 45)
plt.show()

# Other palette
ax.plot_trisurf(df['long'], df['lat'], df['Vel'], cmap=plt.cm.jet, linewidth=0.01)
plt.show()
