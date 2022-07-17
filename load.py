# -*- coding:gbk -*-
# /usr/bin/env python 3.9
"""
This is CodeNoteBook load program
"""
from tkinter import *
from os import getcwd
from PIL import Image, ImageTk
import time
		
window = Tk()
width = 450
heigh = 250
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
window['background'] = '#FAFAD2'
window.tk.call('source', 'themes\\themes.tcl')
window.tk.call('set_theme', 'light')

def ExitWindow():
	window.destroy()

path = getcwd() + "\\resource\\"
icoimage = Image.open(path + 'Ico.png')
tkicoimage = ImageTk.PhotoImage(icoimage)
splashimage = Image.open(path + 'Splash.png')
tksplashimage = ImageTk.PhotoImage(splashimage)

closeimage = Image.open(path + 'Close.png')
tkcloseimage = ImageTk.PhotoImage(closeimage)

Top = Frame(window,bg = '#FAFAD2')

Icon = Label(window,image = tkicoimage,bg = '#FAFAD2')
Icon.pack(anchor = 'nw',side = LEFT,expand = True,pady = 5,padx = 5)

ExitButton = Button(window,image = tkcloseimage,bg = '#FAFAD2',relief = FLAT,activebackground = "red",command = ExitWindow)
ExitButton.pack(anchor = 'nw',side = RIGHT,expand = True,pady = 10,padx = 10)

Splash = Label(window,image = tksplashimage,bg = '#FAFAD2')
Splash.pack(anchor = 'center',expand = True)

Load = Label(window,text = 'Executing Main Program',bg = '#FAFAD2')
Load.pack(anchor = 'sw',expand = True)



def ExecuteMain():
	window.destroy()
	try:
		import function	
	except ModuleNotFoundError:
		warning = Tk()
		warning.resizable(width = False, height = False)
		warning.title("warning")
		Warningmessagebox = Label(warning,text = "Couldn't open CodeNoteBook!").pack()
		warning.mainloop()

window.attributes('-alpha',0.875)
window.overrideredirect(True)
window.after(100,ExecuteMain)
window.mainloop()
