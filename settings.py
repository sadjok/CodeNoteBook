from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from os import chdir,getcwd
from language import *

# Datas
save_flag = False
flag = False
path = "resource\\"

# Functions

def Quits():
	"Really Quit"
	Settings.destroy()
	exit(0)
	
def Applys():
	"Apply settings"
	pass
	Quits()
	
def Finishs():
	"Finishs settings"
	Applys()
	Quits()

def Exits():
	"If not save ask want to save it ?"
	flag = askyesno("Settings","Do you want to save ?")
	if flag:
		Finishs()
	else:
		Quits()

def Cancels():
	"Cancel settings"
	flag = askyesno("Settings","Really Cancel Settings ?")
	if flag:
		if save_flag:
			Quits()
		else:
			Exits()
	else:
		pass

def Checks():
	"Check for WM_DELETE_WINDOW"
	if flag:
		Finishs()
	else:
		Cancels()

# Windows
Settings = Tk()
Settings.title("Settings")
Settings.iconbitmap(path + "Settings.ico")
Settings.tk.call('source', 'themes\\themes.tcl')
Settings.tk.call('set_theme', 'light')

width = 983
height = 591
screenwidth = Settings.winfo_screenwidth()
screenheight = Settings.winfo_screenheight()
Settings.geometry("%dx%d+%d+%d" % (width, height, (screenwidth-width)/2, (screenheight-height)/2))
Settings.resizable(width = False, height = False)

# Tools

# NoteBook
style = Style(Settings)
style.configure('lefttab.TNotebook', tabposition='wne')

notebook = Notebook(Settings, style='lefttab.TNotebook', width=943, height=551)
Language = Frame(notebook)
Editor = Frame(notebook)
Option = Frame(notebook)

head = "\n	"
end = "	\n"

value = 0
frames = [Language,Editor,Option]
options = [head + "Language" + end,head + "  Editor      " + end,head + " Options   " + end]
for i in range(len(options)):
	notebook.add(frames[value],text = options[value])
	value += 1
	
notebook.pack(fill = X,expand = True)

# Frames
ButtonFrame = Frame(Settings)

# Buttons
Apply = Button(ButtonFrame,text = "Apply",command = Applys)
Finish = Button(ButtonFrame,text = "Finish",command = Finishs)
Cancel = Button(ButtonFrame,text = "Cancel",command = Cancels)

# Packs
Cancel.pack(fill = X ,side = RIGHT,padx = 2,pady = 3)
Finish.pack(fill = X ,side = RIGHT,padx = 2)
Apply.pack(fill = X ,side = RIGHT,padx = 2)
ButtonFrame.pack(fill = X,side = BOTTOM)

# Mainloop
#Settings.protocol("WM_DELETE_WINDOW",Checks)
Settings.attributes("-alpha",0.98752)
Settings.mainloop()
