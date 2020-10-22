import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import csv



sns.mpl.rc('figure', figsize=(10,6))
shp_path = 'D:/THONY Programs/Sharad/Sharad/Igismap/Indian_States.dbf'

sf = shp.Reader(shp_path)
print (len(sf.shapes()))
print(sf.records()[0][0])

STATE={'Andaman & Nicobar Island':'AN',
'Andhra Pradesh':'AP',
'Arunanchal Pradesh':'AR',
'Assam':'AS',
'Bihar':'BR',
'Chandigarh':'CH',
'Chhattisgarh':'CT',
'Dadara & Nagar Havelli':'DH',
'Daman & Diu':'DD',      
'NCT of Delhi':'DL',
'Goa':'GA',
'Gujarat':'GJ',
'Haryana':'HR',
'Himachal Pradesh':'HP',
'Jammu & Kashmir':'JK',
'Jharkhand':'JH',
'Karnataka':'KA',
'Kerala':'KL',
'Ladakh':'LA',
'Lakshadweep':'LD' ,      
'Madhya Pradesh':'MP',
'Maharashtra':'MH',
'Manipur':'MN         ',
'Meghalaya':'ML',
'Mizoram':'MZ',
'Nagaland':'NL',      
'Odisha':'OR',
'Puducherry':'PY',
'Punjab':'PB',
'Rajasthan':'RJ',
'Sikkim':'SK'  ,    
'Tamil Nadu':'TN',
'Telangana':'TL',
'Tripura':'TR',
'Uttarakhand':'UT',
'Uttar Pradesh':'UP',
'West Bengal':'WB'

     }





States=['Andaman & Nicobar Island',
'Andhra Pradesh',
'Arunanchal Pradesh',
'Assam',
'Bihar',
'Chandigarh',
'Chhattisgarh',
'Dadara & Nagar Havelli',
'Daman & Diu',      
'NCT of Delhi',
'Goa',
'Gujarat',
'Haryana',
'Himachal Pradesh',
'Jammu & Kashmir',
'Jharkhand',
'Karnataka',
'Kerala',
'Ladakh',
'Lakshadweep' ,      
'Madhya Pradesh',
'Maharashtra',
'Manipur',
'Meghalaya',
'Mizoram',
'Nagaland',      
'Odisha',
'Puducherry',
'Punjab',
'Rajasthan',
'Sikkim' ,    
'Tamil Nadu',
'Telangana',
'Tripura',
'Uttarakhand',
'Uttar Pradesh',
'West Bengal'
]
DATE=["21MAR","2MAR","4MAR","21MAR","19MAR","24MAR","10APR","5MAR","27MAR","16MAR","2APR    ","10MAR","18MAR","14MAR",
      "4MAR","6APR","27APR","5MAR","17MAR","18MAR","17APR","  18MAR","21MAR","2MAR","17MAR","3MAR",
      "2MAR","2MAR","7MAR","21MAR","6APR","4MAR","16MAR","17MAR","2APR","12MAR"]


def stateArrangedInAscendingOrder():
    
    
    month=[i.strip()[len(i.strip())-3:]  for i in DATE ]
    
    date=[int(i.strip()[:len(i.strip())-3] or 0)  for i in DATE ]
    
    
    marMonth=[i for i in range(len(month)) if month[i] =='MAR']
    marDate=[date[i] for i in marMonth]
    dictMar={}
    for i,j in zip(marMonth,marDate):
        dictMar.update({i:j})
        
    sorted_mar_dict=sorted(dictMar.items(),key=lambda x:x[1])
    print(sorted_mar_dict)
    sortedMarMonth=list(dict(sorted_mar_dict).keys())   

    
    aprMonth=[i for i in range(len(month)) if month[i] =='APR']
    aprDate=[date[i] for i in aprMonth]
    dictApr={}
    for i,j in zip(aprMonth,aprDate):
        dictApr.update({i:j})
    sorted_apr_dict=sorted(dictApr.items(),key=lambda x:x[1])      
    sortedAprMonth=list(dict(sorted_apr_dict).keys())
        

    sortedNullMonth=sorted(set([i for i in range(len(month))])-set(marMonth)-set(aprMonth))
 
 
    Mar=[sf.records()[i][0] for i in sortedMarMonth]

    Apr=[sf.records()[i][0] for i in sortedAprMonth]
    Null=[sf.records()[i][0] for i in sortedNullMonth]
    
    return Mar+Apr+Null
    
    
order="*FIRST CASE"    
for i in (stateArrangedInAscendingOrder()):
    order=order+"\n"+i


def plot_map(sf, x_lim=None, y_lim=None, figsize=(11, 10)):
  
    #Plot map with lim coordinates
   
   
    fig, ax = plt.subplots(figsize = figsize)
    #plt.figure(figsize=figsize)
    an2=ax.annotate(order, xy=(94.9,14.7), xycoords="data",  # 'top', 'bottom', 'center', 'baseline', 'center_baseline'
                  xytext=(0, 0), textcoords="offset points",size=8,
                  va="center", ha="left",
                  bbox=dict(boxstyle="Square", fc="skyblue"),
                  arrowprops=dict(arrowstyle="->"))
    plt.text(70, 37.5, "ONSET INDIAN MAP OF FIRST CASE COVID-19", fontsize=16,fontweight="bold")
    id = 0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
       
        y = [i[1] for i in shape.shape.points[:]]
        ax.scatter(x, y,s=1, alpha=1,marker=".",c="skyblue")

        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            #
            plt.text(x0-0.5,y0+0.5, STATE[sf.records()[id][0]], fontsize=8,c="k",fontweight="bold")
           
            an2=ax.annotate(" "+DATE[id].lower()+"", xy=(x0,y0), xycoords="data",  # 'top', 'bottom', 'center', 'baseline', 'center_baseline'
                  xytext=(0, 0), textcoords="offset points",
                  va="center_baseline", ha="center",size=6,weight="bold",
                  bbox=dict(boxstyle="round", fc="w"),
                  arrowprops=dict(arrowstyle="<-"))
           
        id = id + 1

    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)

plot_map(sf)

plt.savefig("ONSET INDIAN MAP OF COVID 19.PNG", bbox_inches='tight')
plt.show()

