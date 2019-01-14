from sys import stdout
# import Tkinter in a cross Python version manner  
try:    from tkinter import Tk 
except: from Tkinter import Tk
try:    from tkinter.ttk import Button 
except: from ttk import Button

def onClick(): 
    stdout.write( "Hello!\n" )
    stdout.flush()

mainWindow = Tk()
Button( mainWindow, text="Hello TKinkter", command=onClick ).grid()
mainWindow.mainloop()