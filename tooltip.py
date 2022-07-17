from tkinter import *
 
class ToolTip(object):
	def __init__(self,widget):
		self.widget = widget
		self.tip_window = None
	 
	def show_tip(self,tip_text):
		"Display text in a tooltip window"
		if self.tip_window or not tip_text:
			return
		x, y, _cx, cy = self.widget.bbox("insert")      
		x = x + self.widget.winfo_rootx() + 75         
		y = y + cy + self.widget.winfo_rooty() - 25     
		self.tip_window = toolwindow = Toplevel(self.widget) 
		toolwindow.wm_overrideredirect(True)                    
		toolwindow.wm_geometry("+%d+%d" %(x, y))                
		toolwindow.wm_attributes("-alpha",0.75555)
		toolwindow.wm_attributes("-transparentcolor","#EAEAEA")
		toolwindow["background"] = "#EAEAEA"
		label = Label(toolwindow, text=tip_text, justify=LEFT,
						 background="#EAEAEA", relief=FLAT,
						 borderwidth=1,font=("Consolas", "10", "normal"))
		label.pack(ipadx=1)
	 
	def hide_tip(self):
		toolwindow = self.tip_window
		self.tip_window = None
		if toolwindow:
			toolwindow.destroy()
 
def create_tooltip(widget, text):
	tooltip = ToolTip(widget)
	def enter(event):
		tooltip.show_tip(text)
	def leave(event):
		tooltip.hide_tip()
	widget.bind('<Enter>', enter)
	widget.bind('<Leave>', leave)
