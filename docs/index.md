# Distribution Builder Python Library
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

"Distribution Builder" (distbuilder) is an open source Python library.
It is a "meta tool", which wraps and combines other related libraries and utilities 
including [PyInstaller](http://www.pyinstaller.org), 
the [Qt Installer Framework](http://doc.qt.io/qtinstallerframework), 
[Opy](https://pypi.org/project/opy-distbuilder/) (Obfuscator for Python), 
[pip](https://pypi.org/project/pip/), and more.  

This library works on both Python 2 and 3.  Its primary intention is for use 
with Python programs, but it can in fact be employed for bundling all sorts of 
software.  It has been tested on recent versions of Windows, macOS, and multiple Linux distros. 
It features the ability to to create standalone binaries from Python scripts (via PyInstaller)
which can be internally obfuscated (via Opy), so as to protect proprietary work.  In addition,   
it is capable of building installers in a cross platform manner (via QtIWF) 
which work in either gui or *non-gui* contexts (which QtIWF does NOT naturally provide).   

See the [Quick Start Guide](QuickStart.md) for instructions on installation 
and getting started with the tool.

For a more thorough explanation of how to use the library, proceed to 
[High Level Classes](HighLevel.md).  Then, as needed, move on to 
[Low Level Classes And Functions](LowLevel.md) and 
[Configuration Classes](ConfigClasses.md).
	
If you wish to contribute, please review to the [To-Do List](ToDo.md) 
for a collection of desired tasks to be completed and the priority 
they have been currently designated.
	
## Important Notes

*BEFORE USE, BACK UP YOUR ENTIRE PROJECT TO ENSURE THERE WILL 
NOT POSSIBLY BE ANY WORK LOST!!!* 

This library is actively under development. It is not 
yet officially released for production use. Function 
signatures, class definitions, etc. are NOT currently 
guaranteed to be stable / backwards compatible.  
Client implementations may require modification upon 
pulling the latest revisions to this.

Presently, the weakest components in the library are the 
obfuscation features.  There is a bit of a learning curve 
for utilizing such, and degree of effort likely required
to perfect it for your own project.  It is recommended that
you apply such security feature only after getting the 
rest of your build process defined.
