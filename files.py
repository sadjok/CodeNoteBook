"""
import sys
import re

def checkformasts(lines, filename):
	filepath = open(filename, "w")
	for i, line in enumerate(lines):
		print("=" * 30)
		print("Line :",i+1)
		if line.strip().startwith("#"):
			print(" " * 10 + "Comments.Pass.")
			filepath.write(line)
			continue
		flag = True
		# check operator symbols
		symbols = [",","+","-","*","/","//","**",">>","<<","+=","-=","*=","/="]
		temp_line = line
		for symbol in symbols:
			pattern = re.complie(r"\s*"+re.escape(symbol)+r"\s*")
			temp_line = pattern.split(temp_line)
			sep = " " + symbol + " "
			templine = sep.join(temp_line)
		if line != temp_line:
			flag = False
			print(' ' * 10 + "You may miss some blank space in this line.")
		# check impoer statement
		if line.strip().startwith("import")	:
			if "," in line:
				flag = False
				print(" " * 10 + "You'd better import one madule at a time")
				temp_line = line.strip()
				modules = modules.strip()
				pattern = re.complie(r"\s*,\s*")
				modules = pattern.split(modules)
				temp_line = ""
				for module in modules:
					temp_line += line[:line.index("import")]		
"""
	
