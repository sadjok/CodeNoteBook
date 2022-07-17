from messagebox import showalert

def _func(ls):
	for i in ls:
		print(i)

def hook_dropfiles(tkwindow_or_winfoid,func=_func,force_unicode=False):
	"""
	Using windnd out of package
	Change some script
	"""
	import platform
	import ctypes
	from ctypes.wintypes import DWORD

	hwnd = tkwindow_or_winfoid.winfo_id()\
		   if getattr(tkwindow_or_winfoid, "winfo_id", None)\
		   else tkwindow_or_winfoid

	if platform.architecture()[0] == "32bit":
		GetWindowLong = ctypes.windll.user32.GetWindowLongW
		SetWindowLong = ctypes.windll.user32.SetWindowLongW
		argtype = DWORD
	elif platform.architecture()[0] == "64bit":
		GetWindowLong = ctypes.windll.user32.GetWindowLongPtrA
		SetWindowLong = ctypes.windll.user32.SetWindowLongPtrA
		argtype = ctypes.c_uint64

	prototype = ctypes.WINFUNCTYPE(argtype,argtype,argtype,argtype,argtype)
	WM_DROPFILES = 0x233
	GWL_WNDPROC = -4
	create_buffer = ctypes.create_unicode_buffer if force_unicode else ctypes.c_buffer
	func_DragQueryFile = ctypes.windll.shell32.DragQueryFileW if force_unicode else ctypes.windll.shell32.DragQueryFile

	def py_drop_func(hwnd,msg,wp,lp):
		global files
		if msg == WM_DROPFILES:
			count = func_DragQueryFile(argtype(wp),-1,None,None)
			szFile = create_buffer(260)
			files = []
			for i in range(count):
				func_DragQueryFile(argtype(wp),i,szFile,ctypes.sizeof(szFile))
				dropname = szFile.value
				files.append(dropname)
			func(files)
			ctypes.windll.shell32.DragFinish(argtype(wp))
		return ctypes.windll.user32.CallWindowProcW(*map(argtype,(globals()[old],hwnd,msg,wp,lp)))
			
	limit_num = 200
	for i in range(limit_num):
		if i+1 == limit_num:
			showalert("Windnd Error : over hook limit number 200, for protect computer.")
		if "old_wndproc_%d" % i not in globals():
			old, new = "old_wndproc_%d"%i, "new_wndproc_%d"%i
			break

	globals()[old] = None
	globals()[new] = prototype(py_drop_func)

	ctypes.windll.shell32.DragAcceptFiles(hwnd,True)
	globals()[old] = GetWindowLong(hwnd,GWL_WNDPROC)
	SetWindowLong(hwnd,GWL_WNDPROC,globals()[new])
