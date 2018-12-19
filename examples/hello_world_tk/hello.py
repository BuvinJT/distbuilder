from tkinter import Tk 
from tkinter.ttk import Button
from sys import stdout

def onClick(): 
    stdout.write( "Hello TKinkter\n" )
    stdout.flush()

mainWindow = Tk()
Button(mainWindow, text="Hello TKinkter", command=onClick).grid()
mainWindow.mainloop()