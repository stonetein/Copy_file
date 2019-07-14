from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import xlrd
import os
import shutil


window = Tk()
filepath = StringVar()
path = StringVar()
path2 = StringVar()
var = IntVar()


def selfile():
    window.filename = filedialog.askopenfilename()
    filepath.set(window.filename)


def selectPath():
    window.path = askdirectory()
    path.set(window.path)


def selectPath2():
    window.path2 = askdirectory()
    path2.set(window.path2)


def Export():
    filename = window.filename
    file_path = window.path
    Export_path = window.path2
    full_datalist = []
    datalist = []


    # oepn file by xlsx
    book = xlrd.open_workbook(filename)
    # search First form
    sheet_1 = book.sheet_by_index(0)
    # The set row
    datalist.extend(sheet_1.col_values(0))


    for dirpath, dirName, fileNames in os.walk(file_path):
        for file in fileNames:
            full_data = os.path.join(dirpath, file)
            full_datalist.append(full_data)


    print(full_datalist)


    for dataname in full_datalist:
        datasource = os.path.basename(dataname)
        if datasource.split(".")[0] in datalist:
            dataname = os.path.join(dirpath, dataname)
            shutil.copy(dataname, Export_path)
            f = open("D:\log_check_list.txt", 'a')
            f.write(str(os.path.basename(dataname.split(".")[0] + ".....Copy completed!") + "\n"))
            f = open("D:\log_check_list.txt", 'r')
            l = f.read()
        else:
            f = open("D:\log_check_list.txt", 'a')
            f.write(str(os.path.basename(dataname.split(".")[0] + ".....Not get!") + "\n"))
            f.close()
            # print ("Not get..........."+dataname)'''


window.title("Copy File Tool")
window.resizable(width=False, height=False)
window.configure(bg='#3B3B3B')


lbl = Label(window, text="File source.xles :",width=13,height=0, fg='#BDC0BA',bg='#3B3B3B')
lbl.grid( row=0, column=0, sticky=W)
Ery = Entry(window, textvariable = filepath, fg="#EDEDED",bg="#2B2B2B")
Ery.grid(row=0, column =1)
btn = Button(window, text="Select..",command = selfile,padx=10, relief="ridge", borderwidth= 1,width=5,height=0,fg="#E3E3E3", bg='#5E5E5E')
btn.grid(row=0, column=2)


lbl = Label(window, text="From folder :",width=13,height=0, fg='#BDC0BA' ,bg='#3B3B3B')
lbl.grid( row=1, column=0, sticky=W)
Ery = Entry(window, textvariable = path, fg="#EDEDED",bg="#2B2B2B")
Ery.grid(row=1, column = 1 )
btn2 = Button(window, text="Select..",command = selectPath,padx=10, relief="ridge", borderwidth= 1,width=5,height=0,fg="#E3E3E3", bg='#5E5E5E')
btn2.grid(row=1, column=2)


lbl = Label(window, text="Export folder :",width=13,height=0,fg='#BDC0BA', bg='#3B3B3B')
lbl.grid( row=2, column=0, sticky=W )
Ery = Entry(window, textvariable = path2,fg="#EDEDED", bg="#2B2B2B")
Ery.grid(row=2, column = 1 )
btn3 = Button(window, text="Select..",command = selectPath2, padx=10,relief="ridge", borderwidth= 1,width=5,height=0,fg="#E3E3E3",bg='#5E5E5E')
btn3.grid(row=2, column=2)


btn4 = Button(window, text="Copy File!", command = Export, fg="#E3E3E3", bg='#545454')
btn4.grid(row=3,column=1,sticky=W+E,padx=2, pady=2)
btn5 = Button(window, text="Cencel", padx=10, fg="#E3E3E3", bg='#545454')
btn5.grid(row=3,column=2,sticky=E+S, padx=2, pady=2)


checkbutton = Checkbutton(window, text='Save as log..', variable=var,fg='#BDC0BA',bg='#3B3B3B')
checkbutton.grid(row=3, sticky=W)


'''photo = PhotoImage(file='19-512.png')
label = Label(image=photo)
label.image = photo
label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)'''




'''txt = Entry(window,width=10, state='disabled')
txt.grid(column=1, row=0)''' #----------lock text


'''def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)'''


window.mainloop()