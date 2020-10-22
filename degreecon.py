import pyproj
restdata =[]
proj_wgs84 = pyproj.Proj(init="epsg:4326")
proj_gk4 = pyproj.Proj(init="epsg:32743")
lat = []
lon = []
with open("latlongcon.txt") as f:
    Lines = f.readlines()
    for l in Lines:
        
        a=str(l).replace("\t"," ").replace("\n","").split(" ")
        a=[i for i in a if i is not '']
        
        restdata.append([float(a[2]),float(a[3])])
        lat.append(float(a[0]))
        lon.append(float(a[1]))
    



proj_wgs84 = pyproj.Proj(init="epsg:4326")
proj_gk4 = pyproj.Proj(init="epsg:32743")
x, y = pyproj.transform(proj_wgs84, proj_gk4, lon, lat)


import os
#SELF-CREATE-OUTPUT_FOLDER
current_directory=os.getcwd()
folder_name="LAT_LON_CON"
out_dir_path = os.path.join(current_directory,folder_name)
os.makedirs(out_dir_path, exist_ok=True)
new_file=os.path.join(out_dir_path,"lat_lon_con.txt")

file = open(new_file, "w")
for data,i,j in zip(restdata,x,y):
    file.write(str(j)+"\t"+str(i)+"\t"+str(data[0])+"\t"+str(data[1])+"\n") 
file.close()

