import os

output_hv_file_directory="D:/THONY Programs/VISHAL-HVRSPY-DATA-FILES-OUTPUT/"

data_file_directory="D:/THONY Programs/VISHAL-HVRSPY-DATA-FILES/Sharad/"

hv_files=os.listdir(output_hv_file_directory)

data_files=os.listdir(data_file_directory)

lat_lon_site_list=[]

peak_freq_site_list=[]

site_lat_lon_peak_freq_list=[]


def peak_freq_collector_hv(files):
    for file in files:
        if (file.split(".")[1]=="hv"):
            file_name=os.path.join(output_hv_file_directory,file)
            with open (file_name,"r") as f:
        
                lines=f.readlines()
            for line in lines:
                if line.startswith("# Median Curve Peak Frequency (Hz) [f0mc,AZ],"):
                    peak_freq=float(line.split(",")[2])
                    peak_freq_site_list.append([peak_freq,file.split("-")[0]])
                    
                    
        

def lat_lon_collector_txt(files):
    for file in files:
        
        if (file.split(".")[1]=="txt"):
            file_name=os.path.join(data_file_directory,file)
            with open (file_name,"r") as f:        
                lines=f.readlines()
            for line in lines:
                if line.startswith("#Latitude:"):
                    lat=float(line.split(":\t")[1])
                if line.startswith("#Longitude:"):    
                    lon=float(line.split(":\t")[1])
                    lat_lon_site_list.append([lat,lon,file.split(".")[0]]) 
                   
            
peak_freq_collector_hv(hv_files)
lat_lon_collector_txt(data_files)
            
            
for i in range(len(lat_lon_site_list)):
    for j in range(len(peak_freq_site_list)):
        if(lat_lon_site_list[i][2]==peak_freq_site_list[j][1]):
            site_lat_lon_peak_freq_list.append([lat_lon_site_list[i][2],lat_lon_site_list[i][1],lat_lon_site_list[i][0],peak_freq_site_list[j][0]])


#SELF-CREATE-OUTPUT_FOLDER
current_directory=os.getcwd()
folder_name="SITE_NAME_LAT_LON_PEAK_FREQ"
out_dir_path = os.path.join(current_directory,folder_name)
os.makedirs(out_dir_path, exist_ok=True)
new_file=os.path.join(out_dir_path,"new_txt_site_lat_lon_peak_freq.txt")

file = open(new_file, "w")

for data in site_lat_lon_peak_freq_list:
    file.write(str(data[0])+"\t"+str(data[1])+"\t"+str(data[2])+"\t"+str(data[3])+"\n") 
file.close()

            
            
            
         