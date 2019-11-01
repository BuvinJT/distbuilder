# cross environment Tkinter import    
try:    from tkinter import Tk 
except: from Tkinter import Tk
try:    from tkinter.ttk import Label 
except: from ttk import Label

from os import curdir
from os.path import abspath

text="Directory: {0}".format( abspath(curdir) ) 

mainWindow = Tk()
Label( mainWindow, text=text, width=100 ).grid()
mainWindow.mainloop()