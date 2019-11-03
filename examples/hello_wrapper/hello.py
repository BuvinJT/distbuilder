# cross environment Tkinter import    
try:    from tkinter import Tk 
except: from Tkinter import Tk
try:    from tkinter.ttk import Label 
except: from ttk import Label

from os import curdir
from os.path import abspath

def isElevated():
    try: 
        from os import geteuid
        return geteuid()==0  
    except:
        """TODO: Add Windows equivalent"""
        return False

text=(
    "Directory: {0}".format( abspath(curdir) ) + "\n" +
    "Elevated: {0}".format( str(isElevated()) ) 
)

mainWindow = Tk()
Label( mainWindow, text=text, width=100 ).grid()
mainWindow.mainloop()