" This is a test for read file's speed test"

# Import lib
from timeit import timeit

def bufferreadfilelines(filename):
	file = open(filename, "r", 1024, encoding = "utf-8")
	for line in file.readlines():
		print(line)
	file.close()

def nobufferreadfilelines(filename):
	file = open(filename, "r", encoding = "utf-8")
	for line in file.readlines():
		print(line)
	file.close()

def bufferreadfileline(filename):
	file = open(filename, "r", 1024, encoding = "utf-8")
	for line in file:
		file.readline()
		print(line)
	file.close()

def nobufferreadfileline(filename):
	file = open(filename, "r", encoding = "utf-8")
	for line in file:
		file.readline()
		print(line)
	file.close()

def bufferonebyteonebytereadfile(filename):
	file = open(filename, "r", 1024, encoding = "utf-8")
	for byte in file:
		file.read(0)
		print(byte)
	file.close()

def onebyteonebytereadfile(filename):
	file = open(filename, "r", encoding = "utf-8")
	for byte in file:
		file.read(0)
		print(byte)
	file.close()

bufferreadfilelines = timeit('bufferreadfilelines("readfiletest.py")', 'from __main__ import bufferreadfilelines', number = 1)
nobufferreadfilelines = timeit('nobufferreadfilelines("readfiletest.py")', 'from __main__ import nobufferreadfilelines', number = 1)
bufferreadfileline = timeit('bufferreadfileline("readfiletest.py")', 'from __main__ import bufferreadfileline', number = 1)
nobufferreadfileline = timeit('nobufferreadfileline("readfiletest.py")', 'from __main__ import nobufferreadfileline', number = 1)
onebyteonebytereadfile = timeit('onebyteonebytereadfile("readfiletest.py")', 'from __main__ import onebyteonebytereadfile', number = 1)
bufferonebyteonebytereadfile = timeit('bufferonebyteonebytereadfile("readfiletest.py")', 'from __main__ import bufferonebyteonebytereadfile', number = 1)

print("Readlines {")
print("bufferreadfilelines : %f" % bufferreadfilelines)
print("nobufferreadfileslines : %f" % nobufferreadfilelines)
print("}")

print("Readline {")
print("bufferreadfileline : %f" % bufferreadfileline)
print("nobufferreadfileline : %f" % nobufferreadfileline)
print("}")

print("OneByte {")
print("bufferonebyteonebytereadfile : %f" % bufferonebyteonebytereadfile)
print("onebyteonebytereadfile : %f" % onebyteonebytereadfile)
print("}")

list = [bufferreadfilelines,nobufferreadfilelines,bufferreadfileline,nobufferreadfileline,bufferonebyteonebytereadfile,onebyteonebytereadfile]

print("Max time is :")
print(max(list))

print("Min time is :")
print(min(list))
