from sys import stdout

# OPY GLITCH! WANT TO USE:
# cross environment Tkinter import    
#try:    from tkinter import Tk 
#except: from Tkinter import Tk
#try:    from tkinter.ttk import Button 
#except: from ttk import Button

from tkinter import Tk
#from Tkinter import Tk
from tkinter.ttk import Button
#from ttk import Button


def onClick(): 
    stdout.write( "Hello!\n" )
    stdout.flush()

mainWindow = Tk()
Button( mainWindow, text="Hello TKinkter", command=onClick ).grid()
mainWindow.mainloop()