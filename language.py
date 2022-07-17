import os
'''
Folder Tree
\Program #Name Does not matter.
	\language
		\languagename
			\*files
'''
originpath = os.getcwd()

def getlanguage():
	"Get Language Pack Name"
	# .\local\lanuage\config
	languagepath = os.getcwd() + "\\resource\\" 
	configtext = ""
	config = open(languagepath + "config","r")
	for text in config:
		config.read(0) # bit and bit
		configtext += text
	config.close()
	return languagepath + configtext
	
def languageinformation():
	"Open language pack config"
	configtext = ""
	openfilelist = []
	languagepack = getlanguage()
	config = open(languagepack + "\\config","r")
	"""
	for text in config:
		config.read(0)
		configtext += text # bit and bit
	"""
	configtextlist = config.readlines()
	config.close()
	return configtextlist,languagepack
	

def readlanguage(encoding = 'utf-8'): # Set a argument to change encoding
	"Open file and read them all"
	filelist,filepath = languageinformation()
	textlist = []
	value = 0
	for readfile in filelist:
		filetext = ""
		readfile = filelist[value]
		openfile = open(filepath + "\\" + readfile,'r',encoding = encoding)
		for text in openfile:
			openfile.read(0)
			filetext += text
		
		openfile.close()
		textlist.append(filetext)
		value += 1
	return textlist
	
def configtext(encoding = 'utf-8'):
	"Return id & text"
	outputtext = readlanguage(encoding)
	allidtext = {}
	outputtext = outputtext[0].split('\n')
	for text in outputtext:
		if text != '' or ' ' or None:		
			text = text.split(':')
		else:
			pass
		try:
			allidtext[text[0]] = text[1]
		except:
			pass
	return allidtext

allidtext = configtext()

def output(id,encoding = 'utf-8'):
	# almost free %95 memory than 3.1.2 version
	os.chdir(originpath)
	return allidtext.get(id)

def changelanguage():
	os.chdir("resource")
	config = open("config","r")
	if config.readline().strip() == "chinese":
		name = "english"
	else:
		name = "chinese"
	config.close()
	config = open("config","w")
	config.write(name)
	os.chdir(originpath)
	
