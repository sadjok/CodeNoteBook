from tkinter import *

def Get_info(module):
	"Get function helps"
	helper = Tk()
	helper.title("Module")
	#helper.iconbitmap("Help.ico")
	helper.resizable(width = True, height = True)
	Helpframe = Frame(helper)
	scrollbarx = Scrollbar(Helpframe)
	scrollbary = Scrollbar(Helpframe, orient = HORIZONTAL)
	lineframe = Frame(Helpframe,width = 30)

	Help = Text(Helpframe,yscrollcommand = scrollbarx.set,xscrollcommand = scrollbary.set,wrap = "none",highlightthickness = 0,highlightbackground = "white",insertborderwidth = 0,insertontime = 750,relief = "flat",selectbackground = "grey")
	Help.focus_set()
	Help.config(tabs=("1c","2c"))
	Help.configure(font=("Consolas", 10, "normal"))
	Help.insert(INSERT,"Module : " + module + "\n")
	modules = dir(module)
	Help.insert(INSERT,"Modules { \n")
	for m in modules:
		Help.insert(INSERT,"	" + m + " {" + "\n")
		docs = m.__doc__.split("\n")
		value = 0
		for i in docs:
			if value > len(docs):
				break
			else:
				Help.insert(INSERT,"	" + docs[value] + "\n")
				value += 1
		Help.insert(INSERT,"	" + "}" + "\n")
		Help.insert(INSERT,"\n")
	Help.insert(INSERT,"}")
	scrollbarx.config(command = Help.yview)
	scrollbary.config(command = Help.xview)
	scrollbarx.pack(side = RIGHT, fill = Y)
	scrollbary.pack(side = BOTTOM, fill = X)
	Help.pack(fill = BOTH, expand = True)
	Helpframe.pack(fill = BOTH, expand = True)
	helper.mainloop()

def Get_help_to_file(module):
	import sys
	out = sys.stdout
	sys.stdout = open(module, "w",buffering = 1,encoding = "utf-8")
	help(module)
	sys.stdout.close()
	sys.stdout = out

def Get_help_from_file(module):
	helper = Tk()
	helper.title("Module")
	#helper.iconbitmap("Help.ico")
	helper.resizable(width = True, height = True)
	Helpframe = Frame(helper)
	scrollbarx = Scrollbar(Helpframe)
	scrollbary = Scrollbar(Helpframe, orient = HORIZONTAL)
	lineframe = Frame(Helpframe,width = 30)

	Help = Text(Helpframe,yscrollcommand = scrollbarx.set,xscrollcommand = scrollbary.set,wrap = "none",highlightthickness = 0,highlightbackground = "white",insertborderwidth = 0,insertontime = 750,relief = "flat",selectbackground = "grey")
	Help.focus_set()
	Help.config(tabs=("1c","2c"))
	Help.configure(font=("Consolas", 10, "normal"))
	texts = open(module,encoding = "utf-8")
	Help.insert(INSERT,"Module : " + module + "\n")
	Help.insert(INSERT,"Helps : " + "\n")
	for i in texts:
		texts.read(0)
		Help.insert(INSERT,i)
	scrollbarx.config(command = Help.yview)
	scrollbary.config(command = Help.xview)
	scrollbarx.pack(side = RIGHT, fill = Y)
	scrollbary.pack(side = BOTTOM, fill = X)
	Help.pack(fill = BOTH, expand = True)
	Helpframe.pack(fill = BOTH, expand = True)
	helper.mainloop()
			
def Get_help(module):
	import os
	Get_help_to_file(module)
	Get_help_from_file(module)
	os.remove(module)




