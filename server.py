import gspread
import os.path
import sys, string, os
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime, date, time
from oauth2client.service_account import ServiceAccountCredentials
from tkinter.scrolledtext import ScrolledText
from itertools import groupby
import collections
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
def search(text_widget, keyword, tag):
    pos = '1.0'
    while True:
        idx = text_widget.search(keyword, pos, END)
        if not idx:
            break
        pos = '{}+{}c'.format(idx, len(keyword))
        text_widget.tag_add(tag, idx, pos)
def get_all(event):
	vl = wks.get_all_values()
	for  line in vl:
		textbox.insert(tk.END, line[0] + '\n')
	partext = textbox.get(1.0, END)
	isgood = False
	isgood2 = False
	classes = []
	tocl = []
	txt = ''
	txt2 = ''
	for s in partext:
		if isgood and s != "*":
			txt = txt + s
		if s == '*':
			isgood = not isgood
			if isgood != True:
				classes.append(txt)
				txt = ""
		if isgood2 and s != '|':
			txt2 = txt2 + s
		if s == '|':
			isgood2 = not isgood2
			if isgood2 != True:
				tocl.append(txt2)
				txt2 = ''
	revc = reversed(classes)
	revtoc = reversed(tocl)
	classess = []
	for c in range(len(classes[::-1])):
		classess.append([classes[::-1][c], tocl[::-1][c]])
	out = ["..."]
	res = False
	for x in classess:
		out.append(x)
	outtest = []
	second1test = []
	foremove = []
	for i in out:
		outtest.append(i[1])
	for i in out:
		second1test.append(i)
	secondtest = []
	for i in second1test:
		secondtest.append(i[0])
	reeeees = True
	while reeeees:
		temp = collections.Counter(outtest)
		reeeees = False
		for i in temp:
			#print(temp[i])

			if temp[i] > 1:
				#print("k")
				#print(outtest.index(i))
				foremove.append(outtest.index(i))
				del outtest[outtest.index(i)]
				reeeees = True
	print(secondtest)
	for i in foremove:
		del secondtest[i]
	out = []
	print(outtest)
	for i in range(len(outtest)):
		out.append([secondtest[i], outtest[i]])
	print(outtest)
	#print(partext)
	search(textbox, 'False', 'False')
	search(textbox, 'True', 'True')
	search(textbox, 'Имя:', 'Имя:')
	search(textbox, 'Журнал: *', 'Журнал: *')
	search(textbox, 'Пришел?', 'Пришел?')
	search(textbox, 'Ушел?', 'Ушел?')
	search(textbox, 'Поправки:', 'Поправки:')
	search(textbox, 'Отметки:', 'Отметки:')
	search(textbox, 'Отсутствующие:', 'Отсутствующие:')
	search(textbox, 'Другое:', 'Другое:')
	search(textbox, 'Передан', 'Передан')
	search(textbox, 'через:', 'через:')
	search(textbox, 'в:', 'в:')
	search(textbox, 'Кабинет:', 'Кабинет:')
	table = Table(root, headings=('Класс', 'Кабинет'), rows=out)
	table.pack(expand=tk.YES, fill=tk.BOTH)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/key.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1PmA0BSTfaHZIBoDC7G2kmed5nEheBIo4NNdBp1LJ410').sheet1
#add_one()
#get_all()
root = tk.Tk()
root.title("Где журнал? - Сервер")
textbox = Text(root)

logb = Button(root, text="Перемещение журнала")
textbox.pack()
logb.pack()
logb.bind('<Button-1>', get_all)
textbox.tag_config('False', background='red')
textbox.tag_config('True', background='blue')
textbox.tag_config('Имя:', background='yellow')
textbox.tag_config('Журнал: *', background='yellow')
textbox.tag_config('Пришел?', background='yellow')
textbox.tag_config('Ушел?', background='yellow')
textbox.tag_config('Поправки:', background='yellow')
textbox.tag_config('Отметки:', background='yellow')
textbox.tag_config('Отсутствующие:', background='yellow')
textbox.tag_config('Другое:', background='yellow')
textbox.tag_config('Передан', background='yellow')
textbox.tag_config('через:', background='yellow')
textbox.tag_config('в:', background='yellow')
textbox.tag_config('Кабинет:', background='yellow')
root.mainloop()