# To-Do List 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)
 
 The following is a loose, ever evolving "road map" for planned releases of the library, 
 grouped / ordered by release number:

## v.0.7.8.x **(WIP)**

* Code signing for Windows

* Provide a "natural" silent uninstall / wrapper to run the Maintenance Tool.  

* Directory creation on target (e.g. user data directories)		

* Resource installation outside of the target directory

* QtIFW graphic features

## v.0.7.9.x 

* RESTORE Linux / Mac QtIFW integration (broken during Windows development of 0.7.8.x)

* Dependency installation for QtIFW via Linux package managers (partially developed already), and Homebrew on Mac

* Add she bang respect / a Windows equivalent to ExecutableScript / QtIwfExternalOp 
embedded scripting mechanism, allowing interepter paths / options to be defined.  Thus
allowing options for embedding Python, Java, ect.

* Code signing for Mac / Linux 

* Direct Bat/Vbs/Ps to Exe high level process class
 
## v.0.8.0

* Add "version control" / "update control" for installers. 
Auto launch maintainencetool when trying to install the same version.
Have prompts questioning if the using wants to update or revert to a prior version.

* TEST (and develop as needed) QtIFW packages which: 
	* contain only "data" (no exe)
	* are not enabled for install by default
	* do not install shortcuts

* More Windows registry functions, and analogous settings on other platforms
	(e.g. plist on Mac)     

* Add "pure" QScript (custom operations) examples / features for QtIFW. 

* Determine if custom UI elements can be used in an uninstaller context? How about an update?
The ui forms are contained in packages, per QtIFW design.  But packages are not loaded
during uninstallation, so it seems an uninstaller couldn't support such ui customization...     

## v.0.8.1

* Revisit "QtIfwExeWrapper" details.  Specifically: NON gui on Windows? Used with QtIfwOnFinishedCheckbox?
  
* Add option for appending platform suffix onto installer file names. 

* Add tarball alternative to zip packaging.

## v.0.8.2

* Add all yet to be provided parameters for PyInstaller.  

* Add all yet to be provided elements for the various Qt IFW XML config classes.  

## v.0.8.3

* Large scale refactoring, to simplify the library and make it more user friendly. 
Rename high level process classes and functions.  Consider dialing back the volume
of published low level functions? 

## v.0.9.x
			
* Improve and stabilize Opy to the point it can handle *most* scripts without *any*
manual intervention. 
   
* "Perfect" Opy "library bundling" (for both private and PyPi libraries). 

## v.1.0

* Extended QA... TBD

* TEST on more Windows versions (Servers?, 8.1?)

* TEST on more Linux distros (Debian, Fedora, Arch...?)

* TEST on OSes with alternate language settings? (Hunting for path names or unicode glitches, etc.?) 

* Continue to expand upon / clean up the documentation.

## v.1.1.x 

* Add QtIFW "online" installer features.

## v.1.2.x 

* Add git integration: Clone/pull to build project from multiple remote sources

* Add Anaconda integration

## v.1.3.x 

* Add more git integration: auto commit / push / tag...

* Add auto conversion of alternate icon formats, so a project only needs one file for such.

* Further develop QtIfwUiPage derived classes and resources.

## v.2.x

* Provide PyInstaller forward/backward compatibility across OS versions.

Currently, (depending upon the platform) building with PyInstaller (and/or QtIFW?) 
on an older or newer version of an OS can result in the product NOT being forwards 
or backwards compatible!  

Notably, there are known complications e.g. GCC .so dynamic linkage:
   
   Refer to:    
   https://pythonhosted.org/PyInstaller/usage.html#making-linux-apps-forward-compatible

* Automate builds for multiple environments / platforms:
   Pyinstaller reference:
	* https://pythonhosted.org/PyInstaller/usage.html#supporting-multiple-python-environments 
	* https://pythonhosted.org/PyInstaller/usage.html#supporting-multiple-operating-systems

* QtIFW cross platform single run master script (several binaries produced of course)

## Spit balls... 		

* Add a Py2Exe wrapper as alternative to PyInstaller.

* Add Py2Exe driven functions for Windows specific features 
which PyInstaller simply lacks (e.g. COM server dll creation).

* Add an NSIS wrapper as alternative to Qt IFW.

* Add setuptools / distutil wrappers an as alternative to pip.  

* Add the option to build projects outside of the build script directory 
e.g. in temp.  

* Add PyPi integration to publish open source releases.
  
* Add (configurable) interactive ui feature, to select various 
operations at runtime (cli or gui).  Use the selected options
to define the attributes of a process class, which is subsequently
executed.  The purpose of such is to allow the developer to
select the options needed at the moment e.g. build exe, run exe, 
build installer, include obfuscation...
