import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import numpy as np
from fpdf import FPDF
import PyPDF2
import pandas as pd
import tabula
import matplotlib.pyplot as plt;
from PIL import Image,ImageOps
from matplotlib.offsetbox import OffsetImage,AnnotationBbox
import os
import time

# HERE YOU ARE GETTING TIME OF EXECUTION
obj = time.localtime()
t = time.asctime(obj)
time=t
print(time)



extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

URL = 'https://www.worldometers.info/coronavirus/#countries'
 # can be changed as per requirement
SHORT_HEADERS = ['Country', 'Active Cases', 'Death/1M POP']

response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('td'))

stats = []
NewStatus = []
all_rows = soup.find_all('tr')

# HERE 415 IS TOTAL NO OF COUNTRIES IN WEB_PAGE
Rows = [i for i in range(227) if i > 8]  
Cols = [1, 8]
Rows2 = []

def changeHere(rows, cols):
    for i in range(len(rows)):
        stat = extract_contents(all_rows[rows[i]].find_all('td'))
     
        stat2 = [x[1] for x in enumerate(stat) if x[0] in cols]
        stats.append(stat2)


def currentStatus(Country, rows):
    for i in range(len(rows)):
        if stats[i][0] == Country:
            print(str(i)+"__"+Country)
            return i


def addingCountries(countries, rows):
    for i in countries:
        
        
        pos = currentStatus(i, rows)
       
        Rows2.append(pos+9)


def descendingRateOfDeath(countries):
    store = []
    positions = []

    for i in range(len(countries)):
        print(countries[i]+":"+str(i)+":"+str(stats[i][1]))
        
        if stats[i][1] == '': stats[i][1] = "0"
        x = stats[i][1].replace(",", "")
        store.append(float(x))

    s = sorted(store)
    s = s[::-1]
    store = []
    NoRepeat = []
    for i in range(len(s)):
        for j in range(len(countries)):
            if s[i] == float(stats[j][1].replace(",", "")):
                if j in NoRepeat:
                    continue
                else:
                    store.append(j)
                    NoRepeat.append(j)
                    break

    return store


def addingCasesinPdf(rows, cols, Table):
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times', '', 20.0)
    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 4
    pdf.set_font('Times', 'B', 20.0)
    pdf.cell(epw, 0.0, "COVID-19 LIVE STATUS OF GFZ FRIENDS'S COUNTRIES ", align='C')
    pdf.set_font('Times', 'B', 18.0)
    pdf.ln(0.5)
    th = pdf.font_size
    for i in range(len(rows) + 1):
        for j in range(len(cols)):
            if i > 0: pdf.set_font('Times', '', 14.0)
            pdf.cell(col_width, th, str(Table[i][j]), border=1, align='C')
        pdf.ln(th)
    pdf_name= str(time)   
    pdf.output('pdf_name.pdf', 'F')

def get_flag(name):
    path="D:\THONY Programs\CountryImages\CountryImages\Flag_of_"
    #"C:/Users/user/AppData/Local/Programs/Python/Python38-32/CountryImages/Flag_of_"
    #"D:\THONY Programs\CountryImages\CountryImages\Flag_of_"
    path =  path+name+".png"
    im = plt.imread(path)
    return im

def offset_image(coord, name, ax):
    img = get_flag(name)
    im = OffsetImage(img, zoom=0.09)
    im.image.axes = ax

    ab = AnnotationBbox(im, (0,coord),  xybox=(-10., -2.5), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)



# COLLECTING ALL RECORDS
changeHere(Rows, Cols)

# TAKING ONLY SELECTED COUNTRIES
#Countries = ["China", "India","Argentina","Germany", "Iceland", "Kyrgyzstan", "Uzbekistan","Iran", "Turkey", "Nicaragua", "Costa Rica", "Indonesia", "Egypt",
#             "DRC", "Trinidad and Tobago", "Thailand", "Afghanistan", "Pakistan",
#             "Oman", "Colombia", "North Macedonia", "Madagascar","Mongolia", "Albania", "Vietnam", "South Africa", "USA"]
Countries = ["China", "India","Argentina","Germany", "Iceland", "Kyrgyzstan", "Uzbekistan","Iran", "Turkey", "Nicaragua", "Costa Rica", "Indonesia", "Egypt",
             "DRC", "Trinidad and Tobago", "Thailand", "Afghanistan", "Pakistan",
             "Oman", "Colombia", "North Macedonia", "Madagascar","Mongolia", "Albania",]
# HERE WE ARE SELECTING COUNTRIES
addingCountries(Countries, Rows)

# CLEARING LAST RECORD
stats = []

# ADD THE NEW RECORDS
changeHere(Rows2, Cols)
print(stats)
# GETTING DESCENDING ORDER POSITIONS \\DEATH RATE
DeathOrder = descendingRateOfDeath(Countries)

# ARRANGEMENT WITH ORDER
for i in range(len(DeathOrder)):
    NewStatus.append(stats[DeathOrder[i]])
table = tabulate(NewStatus, headers=SHORT_HEADERS)


NewStatus.insert(0, SHORT_HEADERS)

# CONVERTING IN PDF FORMAT
addingCasesinPdf(Rows2, Cols, NewStatus)
NewStatus.remove(SHORT_HEADERS)

# COLLECTING PERFORMANCE
performance = []
for i in range(len(Countries)):
    performance.insert(i, int(NewStatus[i][1].replace(",", "")))

# COLLECTING  ARRANGED COUNTRIES
Country = []
for i in range(len(Countries)):
    Country.insert(i, NewStatus[i][0])

h = {'fontname': 'Sans'}

# BAR GRAPH REPRESENTATION
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.16, bottom=0.19, top=0.82)
plt.title("COVID-19 LIVE STATUS OF GFZ FRIEND'S COUNTRIES "+time, **h, color='#9E0508', fontsize=21, fontweight="bold",  
          fontstyle="italic", family="fantasy")
ax.text(2000, 21, "#Stay at Home & Stay Safe #Have Optimistic & Happy Attitude", style='italic',
        bbox={'facecolor': '#DDDDFF', 'alpha': 0, 'pad':0,},fontweight="bold",fontsize=14)
ax.set_facecolor("#DDDDFF")
ax.barh(range(len(Country)),performance,align='center', alpha=1, color='red', edgecolor='blue')
ax.set_yticks(range(len(Country)))
ax.set_yticklabels(Country,rotation=0,fontweight="bold")
ax.tick_params(axis='y', which='major', pad=17)
plt.xlabel('ACTIVE CASES', **h, color='#9E0508', fontsize=20, fontweight="bold", fontstyle="normal")

fig_size = plt.gcf().get_size_inches()
sizefactor = 1.5
plt.gcf().set_size_inches(sizefactor * fig_size)

for i, c in enumerate(Country):
   
    offset_image(i, c, ax)
plt.savefig('NEW IMAGE.png', bbox_inches='tight')

 #HERE LOGO IS ADDED
Image1 = Image.open('NEW IMAGE.png')


Image1copy = Image1.copy()
Image2 = Image.open('corona.jpg')


#HERE YOU ARE SETTING SIZE OF THE LOGO
size = (100, 100)
Image2 = ImageOps.fit(Image2, size, Image.ANTIALIAS)

Image2copy = Image2.copy()

#HERE YOU ARE SETTING POSITION OF THE LOGO
Image1copy.paste(Image2copy, (1000,50))


Image1copy.save('NEW IMAGE.png')
plt.show()