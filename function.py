# A really lde by grade 6 student
# 3.2.0 Fixed a tons of bugs (huff) and make the window beautifully (beta)
# /usr/bin/env python 3.9

# Main {
# Import {
try:
	from messagebox import *
except:
	from tkinter.messagebox import *

from tkinter import *

# Check
import check
import os
firstpath = os.getcwd()
filepath = os.getcwd() + "\\resource\\"

class Check():
	"Check files"
	def self_check():
		"Check need python dlls"
		return check.Check("messagebox.pyd","load.pyd","function.pyd").output_error()

	def show_check():
		"Show lost dlls"
		list = Check.self_check()
		for value in range(0,len(list)):
			showerror("Lost" + " -" + list[value],"Lost Lib" + " -" + list[value])

#Check.show_check()
os.chdir(firstpath)
import threading
from PIL import Image as Imageopen
from PIL import ImageTk
from tkinter.ttk import *
from tkinter.font import *
from tkinter import filedialog
import ctypes
from ctypes import *
import py_compile
import windnd
from module import Get_help,Get_info,Get_help_from_file,Get_help_to_file
from language import output,changelanguage
from tkinter.messagebox import askokcancel
from run import *
from tooltip import *

# }

# Other {
from idlelib.colorizer import *
from idlelib.percolator import Percolator
# }

# data {
flag = False

hasfile = False
# }

# Log {
"""
import logging
import time
os.chdir("workspace")
os.chdir("log")

logging.basicConfig(level = logging.DEBUG,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("DEBUG")

formatter = logging.Formatter("%(relativeCreated)d - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(str(int(time.time()))+"DEBUG.log")
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)
"""
#logger.info("Start program")
#logger.info("Module : DEBUG")
#logger.info(__Version__)
#logger.info("Start load functions & tools")

# }

# String {

__Version__ = output("version")

__information__ = """
	Info:
		This is a LDE for python coder

	Requirements:
		windows operation system version(>= 7)(Best)
		Windows 7 or 10, 11
		python 3.*
		python libs:
		tkinter
		tkinter.ttk
		traceback
		ctypes
		py_compile
		windnd

	create date time: 2021/5/31
	version : 3.2.0
	code : in github(not newest)
	copyright : Sadfjok
	Author : Sadfjok
	Made Time: 2021/11/21 20:40:21

"""


__addtext__ = """
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Version : 3.2.2
#  Filename : None
#  Using : CodeNoteBook
#  Author : sadjok
#  |### Auto create ###|

def main(args):
	return 0

if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv))
"""

# }

# Function {

def aboutlde(give = ""):
	"Show about lde"
	initpath(firstpath)
	showinfo(output("about"),__information__)

def aboutlicense(give = ""):
	"Show LICENSE"
	text = ""
	LICENSE = open("LICENSE","r",encoding = "utf-8")
	for line in LICENSE:
		LICENSE.read(0)
		text = text + line
	showinfo(output("license"),text,True)

def aboutupdate(give = ""):
	"Show what update"
	text = ""
	LICENSE = open("Update.txt","r",encoding = "utf-8")
	for line in LICENSE:
		LICENSE.read(0)
		text = text + line
	showinfo(output("license"),text,True)

def aboutauthor():
	"Show author" # try to encode the stange code ---------------------------------||||||||||||||||||||||||||||||||
	__author__ = "sadjok"
	showinfo(output("Author"),str(output("Author")) + " : " + __author__ + "\n" + "F9728E86130785763E6FB227419E747C")
	
def aboutversion():
	"Show version"
	showinfo(output("version"),str(output("version")) + " : " + str(output("Version")))	
	
def aboutgui():
	"Abouts gui"
	import tkinter.ttk
	abouts = Toplevel()
	abouts.transient(lde)
	abouts.title(output("about"))
	abouts.iconbitmap(filepath + "helps.ico")
	abouts.minsize(250,75)
	abouts.resizable(width = False, height = False)
	infos = tkinter.ttk.Frame(abouts)
	info = tkinter.ttk.Label(infos,text = str(output("help")) + " : ")
	aboutldes = tkinter.ttk.Button(infos,text = output("about"),command = aboutlde)
	licenses = tkinter.ttk.Button(infos,text = output("license"),command = aboutlicense)
	updates = tkinter.ttk.Button(infos,text = output("update"),command = aboutupdate)
	info.pack(fill = "x",padx = 1)
	aboutldes.pack(fill = "x",side = "left",padx = 5)
	licenses.pack(fill = "x",side = "left",padx = 5)
	updates.pack(fill = "x",side = "right",padx = 5)
	infos.pack(fill = "x",side = "top",padx = 1)
	mores = tkinter.ttk.Frame(abouts)
	more = tkinter.ttk.Label(mores,text = str(output("more")) + " : ")
	authors = tkinter.ttk.Button(mores,text = output("author"),command = aboutauthor)
	versions = tkinter.ttk.Button(mores,text = output("version"),command = aboutversion)
	more.pack(fill = "x",padx = 1)
	authors.pack(fill = "x",side = "left",padx = 7)
	versions.pack(fill = "x",side = "left",padx = 10)
	mores.pack(fill = "x",side = "bottom")
	abouts.mainloop()

def autoindent(event):
	"If flag then indent with types"
	global flag
	tab = "	"
	widget = event.widget
	line = widget.get("insert linestart", "insert lineend")
	if "return" in line:
		widget.insert(INSERT,"\n")
	else:
		if flag:
			match = re.match(r'^(\s+)', line)
			current_indent = len(match.group(0)) if match else 0
			new_indent = current_indent + 1
			widget.insert(INSERT,event.char)
			widget.insert(INSERT,"\n" + tab*new_indent)
		else:
			match = re.match(r'^(\s+)', line)
			current_indent = len(match.group(0)) if match else 0
			if current_indent:
				widget.insert(INSERT,event.char)
				widget.insert(INSERT,"\n" + tab*current_indent)
			else:
				widget.insert(INSERT,"\n")
		flag = False
	text.focus_set()
	return "break"

def click(active):
	"Post editmenu"
	editmenu.post(active.x_root, active.y_root)

def undo():
	"Undo"
	text["undo"] = True
	try:
		text.edit_undo()
	except:
		pass
	
def copy():
	"Copy"
	try:
		text.clipboard_clear()
		text.clipboard_append(text.selection_get())
	except:
		pass

def cut():
	"Cut"
	copy()
	try:
		text.delete(SEL_FIRST, SEL_LAST)
	except:
		pass
		
def createcompilefile(filepath = ""):
	"Complie files and output"
	try:
		py_compile.compile(filepath)
		initpath(firstpath)
		showinfo("CodeNoteBook",output("compliefile2") + " " + filepath)
	except:
		initpath(firstpath)
		showerror("CodeNoteBook",output("complieerror") + " " + filepath)

def changefontandsize(give = ""):
	import tkinter.ttk
	"Change text's font and size"
	fonts = Toplevel()
	fonts.transient(lde)
	fonts.title("Font")
	fonts.geometry("500x50")
	fonts.iconbitmap(filepath + "fonts.ico")
	fonts.resizable(width = False, height = False)
	
	font_tuple = families()
	font_family = StringVar()
	
	font_box = tkinter.ttk.Combobox(fonts, width=30,textvariable=font_family,state='readonly')
	font_box['values'] = font_tuple
	font_box.current(font_tuple.index('Arial'))
	font_box.pack(fill = "x",side = "left",padx = 3)
	
	def fontchanger():
		"Change font"
		global current_font_family
		global current_font_size
		
		current_font_family=font_family.get()
		current_font_size=size_var.get()
		text.configure(font=(current_font_family,current_font_size))
		fonts.destroy()
		
	size_var = IntVar()
	font_size = tkinter.ttk.Combobox(fonts, width=15, textvariable=size_var, state='readonly')
	font_size['values'] = tuple(range(8,81))
	font_size.current(0)
	font_size.pack(fill = "x",side = "left",padx = 3)

	changefont = tkinter.ttk.Button(fonts,text = "Apply",command = fontchanger)
	changefont.pack(fill = "x",side = "right",padx = 5)
	
	fonts.mainloop()
	
def changelanguages(give = ""):
	"Change CodeNoteBook's language"
	changelanguage()
	showinfo("CodeNoteBook","You have to restart CodeNoteBook")
	
def Clear_menu():
	"Clear view menu"
	filemenu.delete(4,6)
	viewfilemenu = Menu(menubar,tearoff=0)
	filemenu.add_cascade(label=output("viewfile"),menu=viewfilemenu,command=open_file())
	viewfilemenu.add_command(label=output("clear"),command=Clear_menu)
	filemenu.add_separator()
	filemenu.add_command(label=output("quit"), command=ldequit)

def checkindent(event):
	"If : in with the right word then flag = True "
	global flag
	flag = False
	words = ["class","def","for","while","if","elif","else"]
	widget = event.widget
	line = widget.get("insert linestart", "insert lineend")
	value = 0
	for i in words:
		if value > len(words):
			widget.insert(INSERT,event.char)
		if words[value] not in line:
			value += 1
		else:
			flag = True
			break	
	widget.insert(INSERT,event.char)
	return "break"
	
def countfuncandclassandimport(give=""):
	"Count def and class and import then Update"
	total = text.get("0.0","end")
	define = total.count("def ")
	classes = total.count("class ")
	froms = total.count("from ")
	imports = total.count("import ")
	statusbar.set_label("import","Imp: %d" % (froms + imports))
	statusbar.set_label("func","Func: %d" % define)
	statusbar.set_label("class","Cls: %d" % classes)
	
def dragged_files(file):
	"Read dragged file to text"
	try:
		file = "\n".join((item.decode("utf-8") for item in file))
	except:
		file = "\n".join((item.decode("gbk") for item in file))
	else:
		open_file(file,False)

def exitsave():
	"If exit and file not save then show do you want to save"
	if lde.title() == "CodeNoteBook" or output("newfile"):
		ldequit()
	else:
		flag = askokcancel("CodeNoteBook",output("savemsg"))
		if flag == True:
			save_file()
			ldequit()
		else:
			ldequit()

def find(give = ""):
	import tkinter.ttk
	"Find string in text if created text"
	def close():
		"Close window"
		text.tag_remove('match', '1.0',END)
		Find.destroy()
	
	def finds():
		"Find function"
		word = find_input.get()
		text.tag_remove('match', '1.0',END)
		matches = 0
		if word:
			start_pos = '1.0'
			while True:
				start_pos = text.search(word, start_pos, stopindex=END)
				if not start_pos:
					break 
				end_pos = f'{start_pos}+{len(word)}c'
				text.tag_add('match', start_pos, end_pos)
				matches += 1
				start_pos = end_pos
				text.tag_config('match', foreground='yellow', background='orange')
		
	def replace():
		word = find_input.get()
		replace_text = replace_input.get()
		content = text.get(1.0, END)
		new_content = content.replace(word,replace_text)
		text.delete(1.0, END)
		text.insert(1.0, new_content)

	Find = Toplevel()
	Find.iconbitmap(filepath + "find.ico")
	Find.transient(lde)
	Find.geometry('450x155')
	Find.title('Find')
	Find.resizable(False,False)

	find_frame = tkinter.ttk.LabelFrame(Find, text='Find/Replace')
	find_frame.pack(fill = "x",side = "top",padx = 10)

	text_find_label = tkinter.ttk.Label(find_frame, text='Find : ')
	text_replace_label = tkinter.ttk.Label(find_frame, text= 'Replace :')
	
	find_input = tkinter.ttk.Entry(find_frame, width=30)
	replace_input = tkinter.ttk.Entry(find_frame, width=30)

	find_button = tkinter.ttk.Button(find_frame, text='Find', command=finds)
	replace_button = tkinter.ttk.Button(find_frame, text= 'Replace', command=replace)
	exit_button = tkinter.ttk.Button(find_frame, text = "Exit", command=close)

	text_find_label.pack(fill = "x",side = "top",padx = 5)
	find_input.pack(fill = "x",side = "top",padx = 5)
	text_replace_label.pack(fill = "x",side = "top",padx = 5)
	replace_input.pack(fill = "x",side = "top",padx = 5)

	find_button.pack(fill = "x",side = "left",padx = 7)
	replace_button.pack(fill = "x",side = "left",padx = 10)
	exit_button.pack(fill = "x",side = "right",padx = 10,pady = 2)
	
	Find.mainloop()

def getmouselines(give=""):
	"Use mouse to get how many lines in text"
	line, column = map(str,str(text.index("insert")).split("."))
	statusbar.set_label("column", "Col: %s" % column)
	statusbar.set_label("line", "Ln: %s" % line)

def initpath(path):
	"Change path...?"
	chdir(path)

def ldequit():
	"Quit lde"
	lde.destroy()
	exit(0)

def modulehelps():
	"Show module helps"
	def Get_helps():
		"Use function to get helps"
		getmodulename = modulename.get()
		Get_info(getmodulename)
		Get_help(getmodulename)
			
	helps = Toplevel()
	modulename = tkinter.ttk.Entry(helps)
	finishinput = tkinter.ttk.Button(helps,text = "Finish",command = Get_helps)
	modulename.pack(fill = "x",side = "left")
	finishinput.pack(fill = "x",side = "right")
	helps.mainloop()

def new_file(give = ""):
	"Create a new file in text"
	text.delete("0.0","end")
	text.pack(fill = BOTH, expand = True)
	statusbar.set_label("type","New" + " file",side = "left")
	lde.title(output("newfile"))
	text.insert(INSERT,__addtext__)
	#text.unbind_class("create","<Button-1>")

def open_file(give = "",status = True):
	"Open file and read it to text"
	"Status : Show the dialog or don't"
	if status:
		text.delete("0.0","end")
		Foldername = filedialog.askopenfilename(title = output("openfile"), filetypes=[("Python Files", "*.py"),("Python Files (no console)", "*.pyw"),("All Files", "*")])
		try:
			file = open(Foldername,"r",1024,encoding = "utf-8")
			for line in file:
				file.read(0)
				text.insert(INSERT,line)
				lde.update()
		except:
			try:
				file = open(Foldername,"r",1024,encoding = "gbk")
				for line in file.readlines():
					text.insert(INSERT,line)
			except:
				if Foldername == "":
					pass
				else:
					initpath(firstpath)
					showerror("CodeNoteBook",output("saveerror") + " " + Foldername)

		else:
			viewfilemenu.add_command(label = Foldername)# ,command = open_file(Foldername)
			text.pack(fill = BOTH, expand = True)
			lde.title(Foldername)
			Foldername = Foldername.split(".")
			Foldername = Foldername[-1]
			statusbar.set_label("type",Foldername + " file",side = "left")
	else:
		text.delete("0.0","end")
		try:
			file = open(give,"r",encoding = "utf-8")
			for line in file.readlines():
				text.insert(INSERT,line)
		except:
			try:
				file = open(give,"r",encoding = "gbk")
				for line in file.readlines():
					text.insert(INSERT,line)			
			except:
				if give == "":
					pass
				else:
					initpath(firstpath)
					showerror("CodeNoteBook",output("saveerror") + " " + give)
		else:
			viewfilemenu.add_command(label = give) #,command = open_file(give)
			text.pack(fill = BOTH, expand = True)
			lde.title(give)
			give = give.split(".")
			give = give[-1]
			statusbar.set_label("type",give + "file",side = "left")
			
def openpythonhelp():
	"Open python's help"
	docpath = os.getcwd() + "\\resource\\"
	os.system("hh " + docpath + "PythonHelpDoc.chm")

def openldehelp():
	"Open CodeNoteBook's help"
	docpath = os.getcwd() + "\\resource\\"
	os.system("hh " + docpath + "CodeNoteBook.chm")

def paste():
	"Paste"
	try:
		text.insert(SEL_FIRST, text.clipboard_get())
		text.delete(SEL_FIRST, SEL_LAST)
		return
	except:
		pass
	text.insert(INSERT, text.clipboard_get())
	
def quitFullScreen():
	"Quit Full Screen"
	lde.attributes("-fullscreen",False)

def refresh(give = ""):
	"Update GUI"
	lde.update()
	
def redo():
	"Redo"
	text["undo"] = True
	try:
		text.edit_redo()
	except:
		pass	

def runpythonfile():
	"Run python files"
	filename = lde.title()
	if filename == "CodeNoteBook":
		initpath(firstpath)
		showinfo("CodeNoteBook",output("savemsg"))
		save_file()
		runpythonfile()
	else:
		Run(filename,"None") # wait for arg update

def save_file(give = ""):
	"""
	"Save file"
	if lde.title() != "CodeNoteBook" and lde.title() != output("newfile") == False:
		try:
			filename = lde.title()
			if filename.endwith()
			
			with open(lde.title() + ".py","w",encoding = "utf-8") as savefile:
				savefile.write(text.get("0.0","end"))
				lde.title(lde.title())
		except:
			if Foldername == "" or " " or None:
				pass
			else:
				showerror("CodeNoteBook",output("saveerror") + " " + lde.title())
	else:
		Foldername = filedialog.asksaveasfilename(title=output("savetitle"), filetypes=[(output("filetype"), "*.py"),("Python Files (no console)", "*.pyw"),("All Files", "*")])
		try:
			with open(Foldername + ".py","w",encoding = "utf-8") as savefile:
				savefile.write(text.get("0.0","end"))
				lde.title(Foldername)
		except:
			if Foldername == "" or " " or None:
				pass
			else:
				showerror("CodeNoteBook",output("saveerror") + " " + lde.title())
	"""
	if lde.title() == "CodeNoteBook" or lde.title() == output("newfile"):
		save_as_file()
	elif textchanged:
		titles = lde.title()
		filename = titles
		if titles.endswith(".py"):
			pass
		else:
			filename = filename + ".py"	
		
		with open(filename,"w",encoding = "utf-8") as savefile:
				savefile.write(text.get("0.0","end").strip())
				lde.title(filename)
		
def KeyPress(event):
	global hasfile,titles
	"If keypressed"
	if hasfile:
		textchanged.set(1)
		titles = lde.title()
		lde.title("*" + lde.title())

def save_as_file(give = ""):
	"Save file as a new path"
	Foldername = filedialog.asksaveasfilename(title=output("saveas"), filetypes=[("Python Files", "*.py"),("Python Files (no console)", "*.pyw"),("All Files", "*")])
	try:
		with open(Foldername,"w",encoding = "utf-8") as saveasfile:
			saveasfile.write(text.get("0.0","end"))
			lde.title(Foldername)
	except:
		if Foldername == "" or " " or None:
			pass
		else:
			initpath(firstpath)
			showerror("CodeNoteBook",output("saveerror") + " " + lde.title())

def show_fast_bind(give = ""):
	"Show fast binds"
	binds = "SaveFile:Ctrl-S" + "\n" + "OpenFile:Ctrl-O" + "\n" + "NewFile:Ctrl-N" + "\n" + "Refresh:Ctrl-F" + "\n" + "Quit:Ctrl:Q" + "\n" + "RunFile:<F5>" + "\n" + "ShowHelp:<F1>" + "\n" + "Full/UnfullScreen:<F11>"  + "\n" + "ShowBinds:Ctrl-B" + "\n" + "ShowAboutlde:Ctrl-H" + "\n" + "ShowAboutLICENSE:Ctrl-l" + "\n" + "ChangeFont&Size:Ctrl-Shift-O" + "\n" + "Changelanguage:Ctrl-Shift-L" + "\n" + "FindString:Ctrl-Shift-C"
	initpath(firstpath)
	showinfo("Binds",binds)

def showpythonshell():
	"Run python if have"
	try:
		os.system("start python")
	except:
		showerror("CodeNoteBook","Didn't find Python on this computer")

def _thread_it(func, *args):
	"Create a function with thread"
	thread = threading.Thread(target=func, args=args)
	thread.setDaemon(True)
	thread.start()
	
def toggleFullScreen():
	"Use Full Screen"
	lde.attributes("-fullscreen",True)

def toolbar(give = ""):
	"Show Toolbar"
	toolbarwindow = Toplevel()
	toolbarwindow.iconbitmap(filepath + "Edit.ico")
	toolbarwindow.resizable(width = True, height = True)
	toolbar = Frame(toolbarwindow,relief="sunken",background="white")

	newimg = Imageopen.open(filepath + "New.png")
	enewimg = ImageTk.PhotoImage(newimg)
	newButton = Button(toolbar, image=enewimg,text = "New",width=50,height=50,command=new_file,relief="flat")
	newButton.image = enewimg
	newButton.pack(side=LEFT, padx=2, pady=2)

	openimg = Imageopen.open(filepath + "Open.png")
	eopenimg = ImageTk.PhotoImage(openimg)
	openButton = Button(toolbar, image=eopenimg,width=50,height=50,command=open_file,relief="flat")
	openButton.image = eopenimg
	openButton.pack(side=LEFT, padx=2, pady=2)

	saveimg = Imageopen.open(filepath + "Save.png")
	esaveimg = ImageTk.PhotoImage(saveimg)
	saveButton = Button(toolbar, image=esaveimg,width=50,height=50,command=save_file,relief="flat")
	saveButton.image = esaveimg
	saveButton.pack(side=LEFT, padx=2, pady=2)

	saveasimg = Imageopen.open(filepath + "Saveas.png")
	esaveasimg = ImageTk.PhotoImage(saveasimg)
	saveasButton = Button(toolbar, image=esaveasimg,width=50,height=50,command=save_as_file,relief="flat")
	saveasButton.image = esaveasimg
	saveasButton.pack(side=LEFT, padx=2, pady=2)

	complieimg = Imageopen.open(filepath + "Complie.png")
	ecomplieimg = ImageTk.PhotoImage(complieimg)
	complieButton = Button(toolbar, image=ecomplieimg,width=50,height=50,command=tocompilefile,relief="flat")
	complieButton.image = ecomplieimg
	complieButton.pack(side=LEFT, padx=2, pady=2)

	runimg = Imageopen.open(filepath + "Run.png")
	erunimg = ImageTk.PhotoImage(runimg)
	runButton = Button(toolbar, image=erunimg,width=50,height=50,command=runpythonfile,relief="flat")
	runButton.image = erunimg
	runButton.pack(side=LEFT, padx=2, pady=2)

	exitimg = Imageopen.open(filepath + "Exit.png")
	eexitimg = ImageTk.PhotoImage(exitimg)
	exitButton = Button(toolbar, image=eexitimg,width=50,height=50,command=ldequit,relief="flat")
	exitButton.image = eexitimg
	
	exitButton.pack(side=LEFT, padx=2, pady=2)

	toolbar.pack(side=TOP, fill=X)
	"""
	textbar = Frame(toolbarwindow,relief="sunken",background="white")
	newLabel = Label(textbar, text = "New",bg = "white")
	newLabel.pack(side=LEFT, padx=2, pady=2)

	openLabel = Label(textbar, text = "Open",bg = "white")
	openLabel.pack(side=LEFT, padx=2, pady=2)

	saveLabel = Label(textbar, text = "Save",bg = "white")
	saveLabel.pack(side=LEFT, padx=2, pady=2)

	saveasnewLabel = Label(textbar, text = "Save as",bg = "white")
	saveasnewLabel.pack(side=LEFT, padx=2, pady=2)

	complieLabel = Label(textbar, text = "Complie",bg = "white")
	complieLabel.pack(side=LEFT, padx=2, pady=2)

	runLabel = Label(textbar, text = "Run",bg = "white")
	runLabel.pack(side=LEFT, padx=2, pady=2)

	exitLabel = Label(textbar, text = "Exit",bg = "white")
	exitLabel.pack(side=LEFT, padx=2, pady=2)
	
	textbar.pack(side=TOP, fill=X)
	"""
	toolbarwindow.mainloop()
	
def tocompilefile():
	"Call the complie file function"
	filepath = lde.title()
	if filepath == "CodeNoteBook":
		initpath(firstpath)
		showinfo("CodeNoteBook",output("savemsg"))
		save_file()
	else:
		createcompilefile(filepath)

def usingrun(give = ""):
	"Run file with thread"
	_thread_it(runpythonfile)

def usingpythonhelp(give = ""):
	"Call openpythonhelp function"
	_thread_it(openpythonhelp)

def usingldehelp():
	"Call openldehelp function"
	_thread_it(openldehelp)
	
from winsound import *
def nicewavsound(event = ""):
	filename = filepath + 'type.wav'
	PlaySound(filename, SND_FILENAME)
	
#logger.info("Finished load function") # debug
# }

# Window {
#logger.info("Start creating window") # debug
import config
import ntkutils
cfg = config.get()

lde = Tk()
lde.title("CodeNoteBook")
lde.iconbitmap(filepath + "Edit.ico")
lde.resizable(width = True, height = True)
windnd.hook_dropfiles(lde,func = dragged_files)

# make the window beautifully
# using theme
lde.tk.call('source', 'resource\\themes\\themes.tcl')
lde.tk.call('set_theme', cfg["theme"].lower())

#lde.tk.call('set_theme', 'light')

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
lde.tk.call("tk", "scaling", ScaleFactor/75)
lde.attributes('-alpha',0.9875)

if cfg["theme"] == "Dark": 
	ntkutils.dark_title_bar(lde)

if cfg["mica"] == "ture": 
	if cfg["theme"] == "Dark":
		flag = True
	ntkutils.blur_window_background(lde, dark=flag)

width = 1074
height = 580
screenwidth = lde.winfo_screenwidth()
screenheight = lde.winfo_screenheight()
lde.geometry("%dx%d+%d+%d" % (width, height, (screenwidth-width)/2, (screenheight-height)/2))
myappid = "CodeNoteBook"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
"""
winname = "CodeNoteBook"
hwnd = windll.user32.FindWindowW(c_char_p(None),winname)
GWL_STYLE = -16
GWL_EXSTYLE = -20
old1=windll.user32.GetWindowLongA(hwnd,GWL_STYLE)
old2=windll.user32.GetWindowLongA(hwnd,GWL_EXSTYLE)
WS_BORDER = 0x800000
WS_OVERLAPPEDWINDOW = 0xcf0000 #不显示图标
WS_THICKFRAME = 0x40000
WS_VISIBLE = 0x10000000
WS_EX_ACCEPTFILES = 0x10
# ctypes
windll.user32.SetWindowLongA(hwnd,GWL_STYLE,WS_VISIBLE + WS_THICKFRAME + WS_EX_ACCEPTFILES + WS_BORDER)
"""


#logger.info("Adding window settings") # debug


# menu {
# to set language use ouput(id)
#logger.info("Loading menu & functions") # debug
"""
iconimg = Imageopen.open(filepath + "Show.png")
eiconimg = ImageTk.PhotoImage(iconimg)
iconmenu = Menu(menubar,image = eiconimg,tearoff = 0)
menubar.add_cascade(label=output("filemenu"), menu=iconmenu)

namemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "CodeNoteBook", menu =  namemenu)
"""
menubar = Menu(lde)
filemenu = Menu(menubar, tearoff=0)
viewfilemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label=output("newfile"), command=new_file)
filemenu.add_command(label=output("open"), command=open_file)
filemenu.add_command(label=output("save"), command=save_file)
filemenu.add_command(label=output("saveas"), command=save_as_file)
filemenu.add_cascade(label=output("viewfile"),menu=viewfilemenu)
viewfilemenu.add_command(label=output("clear"),command=Clear_menu)
filemenu.add_separator()
filemenu.add_command(label=output("quit"), command=ldequit)
menubar.add_cascade(label=output("filemenu"), menu=filemenu,underline = 0)

editmenu = Menu(menubar, tearoff=0)
editmenu_edit = Menu(editmenu, tearoff=0)
editmenu.add_command(label=output("refresh"), command=refresh)
editmenu.add_command(label=output("find"), command=find)
editmenu_edit.add_command(label=output("undo"),command=undo)
editmenu_edit.add_command(label="redo",command=redo)
editmenu_edit.add_command(label=output("cut"),command=cut)
editmenu_edit.add_command(label=output("copy"),command=copy)
editmenu_edit.add_command(label=output("paste"),command=paste)
editmenu.add_cascade(label=output("edit"),menu=editmenu_edit)
menubar.add_cascade(label=output("editmenu"), menu=editmenu,underline = 0)

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label=output("run"),command=runpythonfile)
runmenu.add_command(label=output("compliefile"),command=tocompilefile)
shellmenu = Menu(menubar, tearoff=0)
shellmenu.add_command(label=output("pythonshellconsole"),command=showpythonshell)
#shellmenu.add_command(label=output("pythonshellgui"),command=pass)
runmenu.add_cascade(label=output("shell"),menu=shellmenu)
menubar.add_cascade(label=output("runmenu"), menu=runmenu,underline = 0)

optionmenu = Menu(menubar, tearoff=0)
optionmenu.add_command(label=output("font"),command=changefontandsize)
optionmenu.add_command(label=output("language"),command=changelanguages)
menubar.add_cascade(label=output("option"),menu=optionmenu,underline = 0)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label=output("pythonhelp"),command=usingpythonhelp)
helpmenu.add_command(label=output("ldehelp"),command=usingldehelp)
helpmenu.add_command(label=output("help"),command=aboutgui)
helpmenu.add_command(label=output("bind"),command=show_fast_bind)
menubar.add_cascade(label=output("helpmenu"), menu=helpmenu,underline = 0)

windowmenu = Menu(menubar, tearoff=0)
windowmenu.add_command(label="*CodeNoteBook" + str(output("Version")) + "*",command=refresh)
menubar.add_cascade(label="Window", menu=windowmenu,underline = 0)

lde.config(menu = menubar)

#logger.info("Created frame,text,menu,label,statusbar,scrollbar") # debug
# }

# text & scrollbar
#logger.info("Creating frame & tools") # debug

if cfg["theme"] == "Dark":
	bg = "black"
else:
	bg = "white"
	
textframe = Frame(lde)
scrollbarx = Scrollbar(textframe,)
scrollbary = Scrollbar(textframe, orient = HORIZONTAL)
#text = _linenumbers_drag_scrolling(lde)

text = Text(textframe,yscrollcommand = scrollbarx.set,xscrollcommand = scrollbary.set,wrap = "none",highlightthickness = 0,highlightbackground = bg,insertborderwidth = 0,relief = "flat",selectbackground = "grey",undo = True)
text.focus_set()
textchanged = IntVar(value = 0)
text.config(tabs=("1c","2c"))
text.configure(font=("Consolas", 10, "normal"))

color_config(text)
Percolator = Percolator(text)
ColorDelegator = ColorDelegator()
Percolator.insertfilter(ColorDelegator)

scrollbarx.config(command = text.yview)
scrollbary.config(command = text.xview)
scrollbarx.pack(side = RIGHT, fill = Y)
scrollbary.pack(side = BOTTOM, fill = X)
textframe.pack(fill = BOTH, expand = True)

text.bind("<Key>",KeyPress)
#text.bind("<Key>",nicewavsound)

# }

lde.protocol("WM_DELETE_WINDOW",exitsave)
lde.protocol("WM_SAVE_YOURSELF",refresh)

# statusbar {

#logger.info("Load statusbar") # debug

class StatusBar(Frame):
	def __init__(self, master, **kw):
		Frame.__init__(self, master, **kw)
		self.labels = {}

	def set_label(self, name, text="", side="right", width=0):
		if name not in self.labels:
			label = Label(self, borderwidth=0, anchor="w")
			label.pack(side=side, pady=0, padx=4)
			self.labels[name] = label
		else:
			label = self.labels[name]
		if width != 0:
			label.config(width=width)
		label.config(text=text)

statusframe = Frame(lde)
Sizegrip(statusframe).pack(side = RIGHT)
statusbar = StatusBar(statusframe)

statusbar.set_label("type", "None",side = "left")
statusbar.set_label("column", "Col: ")
statusbar.set_label("line", "Ln: ")
statusbar.set_label("Split","|")
statusbar.set_label("import","Imp:")
statusbar.set_label("func","Func: ")
statusbar.set_label("class","Cls: ")

statusbar.pack(fill = X)
statusframe.pack(fill = X)

text.bind(":", checkindent)
text.bind("<Return>",autoindent)	

bindtags = list(text.bindtags())
bindtags.insert(2,"get")
text.bindtags(tuple(bindtags))
text.bind_class("get","<Key>",getmouselines)

bindtags = list(text.bindtags())
bindtags.insert(3,"counts")
text.bindtags(tuple(bindtags))
text.bind_class("counts","<Key>",countfuncandclassandimport)

def show(sleeptime = 0):
	# Just maked how to show it
	# Will add really program !
	lde.attributes("-disabled",True)
	progressbar["maximum"] = 100
	progressbar["value"] = 0
	for i in range(100):
		if progressbar["value"] == 20:
			statustext["text"] = "Loading tools & plugins"
		elif progressbar["value"] == 35:
			statustext["text"] = "Loading tools"
		elif progressbar["value"] == 50:
			statustext["text"] = "Loading settings"
		elif progressbar["value"] == 75:
			statustext["text"] = "Loading languages"
		elif progressbar["value"] == 85:
			statustext["text"] = "Using loaded packages"
		elif progressbar["value"] == 90:
			statustext["text"] = "Writing Log"
		elif progressbar["value"] == 99:
			statustext["text"] = "Ready"

		time.sleep(sleeptime)
		progressbar["value"] += 1
		lde.update()
	
	lde.attributes("-disabled",False)
	progressbar["value"] = 0

progressbar = Progressbar(statusbar)
separators = Label(statusbar,text = "|")
statustext = Label(statusbar,text = "Loading")
separators.pack(side = LEFT,padx = 10)
progressbar.pack(side = LEFT)
statustext.pack(side = LEFT,padx = 5)

# }

# bind {
#logger.info("Add keys") # debug

lde.bind("<Button-1>",getmouselines)
lde.bind("<Control-KeyPress-s>",save_file)
lde.bind("<Control-Shift-KeyPress-S>",save_as_file)
lde.bind("<Control-KeyPress-o>",open_file)
lde.bind("<Control-KeyPress-n>",new_file)
lde.bind("<Control-KeyPress-f>",refresh)
lde.bind("<Control-Shift-KeyPress-C>",find)
lde.bind("<Control-Shift-KeyPress-L>",changelanguages)
lde.bind("<Control-Shift-KeyPress-O>",changefontandsize)
lde.bind("<Control-KeyPress-q>",ldequit)
lde.bind("<Control-KeyPress-l>",aboutlicense)
lde.bind("<Control-KeyPress-h>",aboutlde)
lde.bind("<Control-C>",copy)
lde.bind("<Control-V>",paste)
lde.bind("<Control-X>",cut)
lde.bind("<Control-Z>",undo)
lde.bind("<Control-Y>",redo)
lde.bind("<Button-3>",click)
lde.bind("<F5>",usingrun)
lde.bind("<F1>",usingpythonhelp)
lde.bind("<Control-KeyPress-b>",show_fast_bind)
lde.bind("<F11>",
        lambda event: lde.attributes("-fullscreen",
				not lde.attributes("-fullscreen")))

# }

# Tooltip {
#create_tooltip()

# }

#logger.info("Set drop & settings") # debug
# }
"""
logger.info("Back to the first path") # debug
logger.info("Save settings & functions") # debug
logger.info("All things saved")  # debug
logger.info("Finish loading") # debug
"""
"""
_list = "ATTRS", "ArithmeticError", "AssertionError", "AttributeError", "AutoComplete", "BaseException", "BlockingIOError", "BrokenPipeError", "BufferError", "BytesWarning", "ChildProcessError","ConnectionAbortedError", "ConnectionError", "ConnectionRefusedError", "ConnectionResetError", "DeprecationWarning", "EOFError", "Ellipsis", "EnvironmentError", "Exception", "FILES", "FORCE", "False", "FileExistsError", "FileNotFoundError", "FloatingPointError", "FutureWarning", "GeneratorExit", "HyperParser", "ID_CHARS", "IOError", "ImportError", "ImportWarning", "IndentationError", "IndexError", "InterruptedError", "IsADirectoryError", "KeyError", "KeyboardInterrupt", "LookupError", "MemoryError", "ModuleNotFoundError", "NameError", "None", "NotADirectoryError", "NotImplemented", "NotImplementedError", "OSError", "OverflowError", "PendingDeprecationWarning", "PermissionError", "ProcessLookupError", "RecursionError", "ReferenceError", "ResourceWarning", "RuntimeError", "RuntimeWarning", "SEPS", "StopAsyncIteration", "StopIteration", "SyntaxError", "SyntaxWarning", "SystemError", "SystemExit", "TAB", "TRIGGERS", "TRY_A", "TRY_F", "TabError", "TimeoutError", "True", "TypeError", "UnboundLocalError", "UnicodeDecodeError", "UnicodeEncodeError", "UnicodeError", "UnicodeTranslateError", "UnicodeWarning", "UserWarning", "ValueError", "Warning", "WindowsError", "ZeroDivisionError", "abs", "all", "and", "any", "as", "ascii", "assert", "async", "autocomplete_w", "await", "bin", "bool", "break", "breakpoint", "bytearray", "bytes", "callable", "chr", "class", "classmethod", "compile", "complex", "continue", "copyright", "credits", "def", "del", "delattr", "dict", "dir", "divmod", "elif", "else", "enumerate", "eval", "except", "exec", "exit", "filter", "finally", "float", "for", "format", "from", "frozenset", "getattr", "global", "globals", "hasattr", "hash", "help", "hex", "id", "idleConf", "if", "import", "in", "input", "int", "is", "isinstance", "issubclass", "iter", "keyword","lambda", "len", "license", "list", "locals", "main", "map", "max", "memoryview", "min", "next", "nonlocal", "not", "object", "oct", "open", "or", "ord", "os", "pass", "pow", "", "property", "quit", "raise", "range", "repr", "return","reversed", "round", "set", "setattr", "slice", "sorted", "staticmethod", "str", "string", "sum", "super", "sys", "try", "tuple", "type", "vars", "while", "with", "yield", "zip"
sets(_list,False)
"""

show(0)
#lde.state("iconic")
os.chdir(firstpath)
lde.mainloop()
