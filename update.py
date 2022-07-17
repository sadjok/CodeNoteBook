from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import zipfile
import threading
import os

"Update GUIS"
#To Do:
#	Check for update:
#		check the links...?
#	if flag:
#		Update()
#	else:
#		pass
#		mainloop()


filepath = os.getcwd() + "\\resource\\"
fixpackage = ".codenotebook.fix.package"
updatepackage = ".codenotebook.update.package" # original use update pakage
flag = False
# use endswich .codenotebook.update.package


class UpdatePackageNotFound(Exception):
	"Update Package Not Found Error"
	def __init__(self,name):
		Exception.__init__(self)

# Update from the disk
# Need : Update File.

def _start():
	checkprogressbar.start()

def _stop():
	checkprogressbar.stop()

def _thread_it(func, *args):
	"Create a function with thread"
	thread = threading.Thread(target=func, args=args)
	thread.setDaemon(True)
	thread.start()

def _list_files(path):
	_files = []
	list = os.listdir(path)
	for i in range(0, len(list)):
		path = os.path.join(path, list[i])
		if os.path.isdir(path):
			_files.extend(list_all_files(path))
		if os.path.isfile(path):
			_files.append(path)
	return _files

def _type_file():
	global firstseekpath
	firstseekpath = ["C:\\Users\\Administrator\\Downloads\\",os.getcwd() + "\\package\\"]
	for i in range(len(firstseekpath)):
		_files = _list_files(firstseekpath[i])
		for j in _files:
			if j.endswith(updatepackage) or j.endswith(fixpackage):
				return j
				break

def _update_package(package,encoding = "uft-8"):
	"Zip the package"
	global filecontent
	zip_path = os.path.dirname(os.path.realpath(__file__))
	zip_file = zipfile.ZipFile(package)
	for filecontent in zip_file.namelist():
		ZipFile.extract(filecontent,zip_path)
	zip_extract.close()

def _check_gui():
	global checkprogressbar
	Hide = Tk()
	Hide.withdraw()
	Update = Toplevel()
	Update.transient(Hide)
	Update.title("Update")
	Update.iconbitmap(filepath + "Update.ico")
	#Update.resizable(width = False, height = False)
	width = 575
	height = 275
	screenwidth = Update.winfo_screenwidth()
	screenheight = Update.winfo_screenheight()
	Update.geometry("%dx%d+%d+%d" % (width, height, (screenwidth-width)/2, (screenheight-height)/2))
	Update.tk.call('source', 'resource\\themes\\themes.tcl')
	Update.tk.call('set_theme', 'light')
	
	Up = Frame(Update)
	Mid = Frame(Update)
	Down = Frame(Update)
	
	icon = filepath + "edit96x96.png"
	load = Image.open(icon)   # open image
	image = ImageTk.PhotoImage(load)  # read opened image
	showimage = Label(Mid, image = image).pack(side = LEFT,fill = BOTH, expand = True,padx = 10)
	
	showtext = Label(Mid, text = "Checking for update").pack(side = TOP,fill = X,pady = 0,padx = 30)
	
	checkprogressbar = Progressbar(Up, length = 100, mode='indeterminate', orient = HORIZONTAL)
	_start()
	checkprogressbar.pack(fill = X,side = TOP)
	cancel = Button(Down, text = "Cancel", command = Update.destroy).pack(fill = X,side = RIGHT,pady = 1,padx = 1)
	
	Up.pack(side = TOP,fill = X)
	Mid.pack(side = LEFT,fill = X,padx = 30)
	Down.pack(side = BOTTOM, fill = X)
	
	Update.mainloop()
	
_check_gui()
