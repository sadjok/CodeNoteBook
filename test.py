from tkinter import *
import keyword 

keywordlist = keyword.kwlist
keywords = keywordlist[:]

def returnsort(give = ""):
	return geted[0]

def getmouselines(give = ""):
	"Use mouse to get how many lines in text"
	line, column = map(str,str(text.index("insert")).split("."))
	return line

def gettext(event):
	global geted
	auto = []
	link = []
	lines = getmouselines()
	widget = event.widget
	geted = widget.get(str(lines) + ".0" ,"end")
	geted = geted.split("\n")[0]
	if geted:
		for i in range(len(keywords)):
			if len(geted) > 3:
				break
			elif geted in keywords[i]:
				auto.append(keywords[i])
				
		for i in range(len(keywords)):
			if len(geted) > 5:
				break
			if geted in keywords[i]:
				link.append(keywords[i])
				
		link.sort(key = returnsort)
		
		for i in range(len(link)):
			if link[i] not in auto:
				auto.append(link[i])
	return auto
	
root = Tk()
text = Text(root)
bindtags = list(text.bindtags())
bindtags.insert(3,"counts")
text.bindtags(tuple(bindtags))
text.bind_class("counts","<Key>",gettext)

text.pack()
root.mainloop()
