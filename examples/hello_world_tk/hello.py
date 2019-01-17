from sys import stdout

# cross environment Tkinter import    
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