# To-Do List 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)
 
 The following is a loose, ever evolving "road map" for planned releases of the library, 
 grouped / ordered by release number:
 
## v.0.7.6

* Develop formal Qt C++ integration (and documentation).

* Start "QtIfwExeWrapper" class, to provide extended features for launching 
distributions.

## v.0.7.7

* Finish "QtIfwExeWrapper" class.

* TEST (and develop as needed) QtIFW packages which: 
	* contain only "data" (no exe)
	* do not install shortcuts
	* are not enabled for install by default

* Test, and confirm / fix uninstallation mechanism for silent installers,
notably in non GUI environments. Can this be done via the Maintenance Tool
and / or the original installer?

## v.0.7.8

* Test and develop "update installer" features as needed.
   
## v.0.7.9

* Further develop the Qt IFW script generation features.
	* Directory creation on target (e.g. user data directories)		
	* Resource installation outside of the target directory
	* Windows Registry functions, analogous settings on other platforms
	(e.g. plist on Mac)     

## v.0.8.x
			
* Improve and stabilize Opy to the point it can handle *most* scripts without *any*
manual intervention. 
   
* "Perfect" Opy "library bundling" (for both private and PyPi libraries). 

* Add git integration: Clone/pull to build project from multiple remote sources

## v.0.9.x

* Add option for appending platform suffix onto installer file names. 

* Add tarball alternative to zip packaging.

* Add all yet to be provided parameters for PyInstaller.  

* Add all yet to be provided elements for the various Qt IFW XML config classes.  

## v.1.0

* Extended QA... TBD

* TEST on more Windows versions (7?, 8.1?)

* TEST on more Linux distros (Debian, Fedora, Arch...?)

* TEST on OSes with alternate language settings? (Hunting for path names or unicode glitches, etc.?) 

## v.1.1.x 

* Add QtIFW "online" installer features.

* Add additional examples.

* Continue to expand upon the documentation.

* Add more git integration: auto commit / push / tag...

## v.1.5.x

* Provide forward/backward across OS versions.

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

* Add auto conversion of alternate icon formats, so a project only needs one file for such.

## v.2.x+ Spitballs 		

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
