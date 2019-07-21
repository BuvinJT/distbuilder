# To-Do List 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)
 
## High Priority

* Provide backwards compatible PyInstaller builds for old OS versions
  to address known complications e.g. GCC .so dynamic linkage problems 
  (or at least document issue / suggested solutions).  

* Further develop the Qt IFW script generation features.
	* Directory creation on target (e.g. user data directories)		
	* Windows Registry functions     

* TEST on more Linux distros

* TEST (and develop as needed) QtIFW packages which: 
	* do not install shortcuts
	* are not enabled for install by default
	* contain only "data" (no exe)

## Moderate Priority

* TEST (and develop as needed) QtIFW packages for Qt C++ exes, 
to confirm auto dependency collection (include QML based projects).

* Further develop external library bundling (for Opy), making such 
more automated and less work for the user (e.g. finding external library 
sources locally and/or downloading them with pip...)
			
* Continue to improve and stabilize the Opy library and its beta features.

* Continue to expand upon the documentation, especially with
regard to the high level classes and the various configuration options.

## Low Priority

* Add option for appending platform suffix onto installer file names. 

* Add all yet to be provided parameters for PyInstaller.  

* Add all yet to be provided elements for the various Qt IFW 
XML config classes.  

* Add tarball alternative to zip packaging.

* Add QtIFW "online" installer features.

* Add additional examples.

## Wish List		

* Add a Py2Exe wrapper as alternative to PyInstaller.

* Add Py2Exe driven functions for Windows specific features 
which PyInstaller simply lacks (e.g. COM server dll creation).

* Add an NSIS wrapper as alternative to Qt IFW.

* Add setuptools / distutil wrappers an as alternative to pip.  

* Add git integration to commit and push versions.

* Add the option to build projects outside of the build script directory 
e.g. in temp.  

* Add PyPi integration to publish releases.

* Add automated version tracking / stamping / git tagging...
  
* Add (configurable) interactive ui feature, to select various 
operations at runtime (cli or gui).  Use the selected options
to define the attributes of a process class, which is subsequently
executed.  The purpose of such is to allow the developer to
select the options needed at the moment e.g. build exe, run exe, 
build installer, include obfuscation...
