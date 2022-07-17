from time import perf_counter
from os import startfile,system
from threading import Thread

def Args():
	system("python -h")

def Run(pyfile,pyargs = "none",text = "Run time is %s"):
	if text != "" or " " or None:
		get = Threads(func = Timer(pyfile,pyargs,text))
	else:
		print("You can not set text None")
		return "You can not set text None"
		exit(0)
		
def Threads(func):
	Thread(target = func,args = ("Python File Runner"))

def Timer(pyfile,pyargs,text):
	start = perf_counter()
	system("cmd /c start /i ")
	startfile(r"%s" % pyfile)
	end = perf_counter()
	system("echo ------------------------------------")
	system("echo " + text % (end - start))
	system("pause")
	
	return text % (end - start)
	return get
