from ctypes import windll,cdll
from os import path
from importlib import machinery
from messagebox import *


# Check the file is type = .dll file then use the ctypes windll to try it can be import and no less bite
# Check the file is type = .pyd file then use the import to try it can be import and no less bite
# main type .dll .pyd file (just support python & C/C++ out function lib) but only support python window appcation project
# it just help to try the lib is exsit or none
# Code:
# if extension == '.dll':
# --snip--
# elif extension == '.pyd':
# --snip--
# (--snip-- = look down code)
# You can get the error from the output_error
# Usage:
# 	ANYNAME = Check(FILENAME1,FILENAME2,FILENAME3..........).output_error()
#	if ANYNAME == None:
#		ALL FILES ARE EXSIT
#	else:
#		print(ANYNAME)

class Check():
	def __init__(self,*checkfiles):
		self.checkfile = checkfiles
		self.extension = []
		self.output = []
		self.value = int()
		
	def output_extension(self):
		for value in range(0,len(self.checkfile)):
			name = self.checkfile[value]
			name = name.split('.')
			name = name[-1]
			self.extension.append(name)
			del name
			
	def check_file(self):
		self.output_extension()
		filename = self.checkfile[self.value]
		extension = self.extension[self.value]
		if extension == 'dll': #type C/C++ lib
			try:
				try:
					Objdll = windll.LoadLibrary(filename + extension)
				except FileNotFoundError:
					return filename
			except:
				try:
					Objdll = cdll.LoadLibrary(filename + extension)
				except FileNotFoundError:
					return filename
		elif extension == 'pyd': # type python lib
			try:
				machinery("dml",filename)
			except FileNotFoundError:
				return filename
				
		else: # normal file
			flag = path.isfile(filename)
			if flag == False:
				return filename	
					
	def output_error(self):
		for value in range(0,len(self.checkfile)):
			self.value = value
			output = self.check_file()
			self.output.append(output)
			
			del output
			
		return self.output


class CHECK():			
	def self_check():
		return Check('shell.pyd','sets.pyd','settings.pyd','note.pyd','messagebox.pyd','load.pyd','function.pyd').output_error()

	def show_check():
		list = CHECK.self_check()
		for value in range(0,len(list)):
			tkinter.messagebox.showerror('Lost' + ' -' + list[value],'Lost Lib' + ' -' + list[value])
