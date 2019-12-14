# cross environment Tkinter import    
try:    from tkinter import Tk 
except: from Tkinter import Tk
try:    from tkinter.ttk import Label 
except: from ttk import Label

from os import curdir, environ
from os.path import abspath
from sys import argv, stdout

def isElevated():
    try:    # Nix  
        from os import geteuid
        return geteuid()==0  
    except: # Windows
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()==1

def isDebug(): 
    try: return isDebug.__CACHE
    except:
        isDebug.__CACHE = environ.get("DEBUG_MODE")=="1"
        return isDebug.__CACHE

text=(
             "Work Dir: {0}".format( abspath(curdir) ) 
    + "\n" + "Elevated: {0}".format( str(isElevated()) )
    + "\n" + "Debug mode: {0}".format( str(isDebug()) ) 
    + "\n" + "TEST_ENV_VAR: {0}".format( str(environ.get("TEST_ENV_VAR")) )
    + "\n" + "Args: {0}".format( ''.join([ '"%s" ' % a for a in argv[1:] ])  )
)

print( "App started" )
mainWindow = Tk()
Label( mainWindow, text=text, width=100 ).grid()
mainWindow.mainloop()
print( "Good bye!" )
