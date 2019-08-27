import gspread
import os.path
import sys, string, os
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime, date, time
from oauth2client.service_account import ServiceAccountCredentials
from tkinter.scrolledtext import ScrolledText
def add_one(textg):
    vl = wks.get_all_values()
    wks.update_cell(len(vl) + 1, 1, textg)
def generate_msg(event):
    mt = datetime.today()
    tt = mt.timetuple()
    timestring = '[' + str(tt[0]) + '/' + str(tt[1]) + '/' + str(tt[2]) + ', ' + str(tt[3]) + ':' + str(tt[4]) + ':' + str(tt[5]) + ']'
    datastring = 'Имя: ' + e0.get() + ', ' + 'Журнал: *' + e.get() + '*, ' + 'Пришел? ' + str(cvar1.get()) + ', ' + 'Ушел? ' + str(cvar3.get()) + ', ' + 'Поправки: ' + 'Отметки: ' + str(cvar2.get()) + ', ' + 'Отсутствующие: ' + str(cvar4.get()) + ', ' + 'Другое: ' + str(cvar5.get()) + ', ' + 'Передан через: ' + e3.get() + ', ' + 'Передан в: |' + e4.get() + '|'
    add_one(timestring+datastring)
    old = myname[0]
    new = e0.get()
    if old!=new:
        myname.insert(0, new)
        file = open("name.txt", "w")
        forawrite = ""
        for i in myname:
            forawrite = forawrite + i + "\n"
        file.write(forawrite)
        file.close()

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/key.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1PmA0BSTfaHZIBoDC7G2kmed5nEheBIo4NNdBp1LJ410').sheet1
#add_one()
#get_all()
if not os.path.exists('name.txt'):
    f = open('name.txt', 'tw', encoding='utf-8')
    f.close()
myname = []
f = open('name.txt')
line = f.readline()
while line:
    myname.append(line)
    line = f.readline()
f.close()
root = tk.Tk()
root.title("Где журнал?")
l0 = Label(root, width=20, text = "Я - ")
e0 = ttk.Combobox(root, width=20, values = myname)
e0.set(myname[0])
l = Label(root, width=20, text="У меня журнал...")
e = Entry(root, width=20)
l2 = Label(root, width=20, text="И журнал...")
cvar1 = BooleanVar()
cvar1.set(0)
c1 = Checkbutton(text="Пришел ко мне", variable=cvar1, onvalue=1, offvalue=0)
cvar3 = BooleanVar()
cvar3.set(0)
c3 = Checkbutton(text="Ушел от меня", variable=cvar3, onvalue=1, offvalue=0)
l3 = Label(root, width=20, text="Я внес в него")
l4 = Label(root,width=20, text = "следующие поправки:")
cvar2 = BooleanVar()
cvar2.set(0)
t1 = Checkbutton(text="Проставил оценки", variable=cvar2, onvalue=1, offvalue=0)
cvar4 = BooleanVar()
cvar4.set(0)
t4 = Checkbutton(text="Отм. отсутствующих", variable=cvar4, onvalue=1, offvalue=0)
cvar5 = BooleanVar()
cvar5.set(0)
t5 = Checkbutton(text="Другое", variable=cvar5, onvalue=1, offvalue=0)
l5 = Label(root, width=20, text="И я передал его")
l6 = Label(root, width=20, text="через...")
e3 = Entry(root, width=20)
l7 = Label(root, width=20, text="в")
e4 = Entry(root, width=20)
l8 = Label(root, width=20, text="И мой комментарий(необ.):")
t2 = ScrolledText(root, width=15, height=5)
b = Button(root, text="Записать")
l0.pack(anchor=W)
e0.pack()
l.pack(anchor=W)
e.pack()
l2.pack(anchor=W)
c1.pack(anchor=W)
c3.pack(anchor=W)
l3.pack(anchor=W)
l4.pack(anchor=W)
t1.pack(anchor=W)
t4.pack(anchor=W)
t5.pack(anchor=W)
l5.pack()
l6.pack()
e3.pack()
l7.pack()
e4.pack()
l8.pack()
t2.pack()
b.pack()
b.bind('<Button-1>', generate_msg)
root.mainloop()