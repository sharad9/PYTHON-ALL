import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getJSON ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_json (import_file_path)
    
browseButton_JSON = tk.Button(text="      Import JSON File     ", command=getJSON, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JSON)

def convertToCSV ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None, header=True)

saveAsButton_CSV = tk.Button(text='Convert JSON to CSV', command=convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()