# Troubleshooting
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Tested Against

Python:  

* 2.7  
* 3.5  
* 3.7  
  
Windows:    

* 8.0  
* 10

macOS:    

* Sierra  
* Mojave

Linux:   

* Ubuntu 16.04  
* Ubuntu 18.04  

OS Language:  

* English  

PyInstaller:  

* Binary / Script
* 2.1
* 3.4

Qt Installer Framework:  

* 2.0.5
* 3.0.6  

Pip:  

* 8.x  
* 18.x  

Opy distbuilder:  

* 0.9+  

## Binary launching runtime issues

### Relative resources

If your application uses "relative resources" (e.g. images, etc. packaged
with it external to the binary), you may encounter problems with such
based on the context in which your application is launched.
Rather than depending upon the current working directory being set to
your's program's location before it is started, you would be better off
acquiring the directory path programmatically, and then resolving your 
relative paths to ones which are absolute.  

In Python, you could use a function such as this `absPath` example.  
Note, the `THIS_DIR` assignment shown here is valid in both a script and 
binary (i.e. "frozen") context.

    import os, sys
	
    THIS_DIR = os.path.dirname( os.path.realpath( sys.argv[0] ) )    
    
    def absPath( relativePath ):    
        return os.path.normpath( os.path.join( THIS_DIR, relativePath ) )

In some situations, that preferred approach would take a great deal of effort to apply unfortunately. In which case, a "shortcut" solution maybe to
just set the working directory when the program is launched, and then set it 
back to what it was upon exit.

Python example:

	import os, sys
	
	THIS_DIR = os.path.dirname( os.path.realpath( sys.argv[0] ) )    
	
	__INIT_DIR = None
	def normalizeWorkDir() :
	    global __INIT_DIR
	    __INIT_DIR = os.curdir
	    os.chdir( THIS_DIR )
	
	def restoreWorkDir() :
	    if __INIT_DIR : os.chdir( __INIT_DIR )
	
Example use of the above functions:
	
	if __name__ == "__main__":
	    normalizeWorkDir()
	    launchApp()
	    restoreWorkDir()

### Crash / failure with no debugging info

If a (gui) PyInstaller built application fails,
and you are seeking debugging info, refer to the 
[Testing](Reference.md#testing) section of the 
Reference Manual for more details on viewing such.    

## Qt Installer Framework issues

### Setting `QT_IFW_DIR` 

To use the Qt Installer Framework integration, it is 
recommended to you set the `QT_IFW_DIR` environmental 
variable on a *permanent* (non-volatile) basis (so it
doesn't have to set every time you want to use it). This 
method makes your build script portable across platforms and 
on all your project collaborator's machines.  If that proves
to be difficult, however, you may set that within the script.   
Refer to the [Installers](Reference.md#installers) section of 
the Reference Manual for details. 

Setting environmental variables is beyond the scope of this document,
but here some places to start looking for help.  

[Windows variables](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10)

[macOS variables](https://stackoverflow.com/questions/135688/setting-environment-variables-on-os-x)

[Ubuntu variables](https://askubuntu.com/questions/58814/how-do-i-add-environment-variables)

### Launch App at end of install failures

If the application appears runs in every other context, except
when launched at the end of the Qt installer, the most likely
reason is that working directory is incorrect when it is 
executed. This library attempts to set the working
directory for any program to the location where it resides
implictly.  QtIFW, however, does not currently support setting
the working directory as a "RunProgram" directive.
A feature request for this was filed with Qt (long ago):

https://bugreports.qt.io/browse/QTIFW-217

For now, while there are various potential solutions to this, 
the *best* one is arguably to resolve this directly within your program.  
See [Relative resources](Relative resources) for more help. 

If Qt does not finally resolve this themselves sometime in 
an upcoming IFW release, then distbuilder will provide a built-in
work around.  Note, this is also a known issue on macOS, when launching 
via symlinks added to Applications or the desktop.  That is NOT
a problem via Windows shortcuts or Linux desktops entries.

### Windows 8 (and earlier?): Crash at end of install

Recent versions of QtIFW have been observed to crash at the 
end of the installation on Windows 8.  This bug has been 
reported to Qt and they appear to be actively patching it.

https://bugreports.qt.io/browse/QTIFW-1248

The current work around is to directly launch the installer 
with elevated priviledges (i.e as an administrator) on this
version of Windows.

### Linux sudo password not accepted

It has been observed that sometimes the sudo password is
not accepted by the installer when it prompts for it. The
contexts and details have yet to be narrowed down.

The current work around is to directly launch the installer 
with elevated priviledges (i.e as root / sudo) if you encounter
this (inconsistent/odd) behavior.

## Get Help 

Refer to [Post An Issue](Contribute.md#post-an-issue).
