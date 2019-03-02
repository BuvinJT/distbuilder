# To-Do List 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)
 
## High Priority

* Test QtIFW use on terminals / non-gui Linux distros like CentOS 
(silent installs / noninteractive). Look into options for producing such 
explictly (maybe a PyInstaller wrapper?) so the user does not have to pass a 
switch. 

* Continue to expand upon the documentation, especially with
regard to the various configuration options.

## Moderate Priority

* Test (and develop as needed) QtIFW packges which: 
	* do not install shortcuts
	* are not enabled for install by default
	* contain only "data" (no exe)

* Test (and develop as needed) QtIFW packges for Qt C++ exes, 
to confirm auto dependency collection (include QML based projects).

* Test on more Linux distros

* Further develop external library bundling (for Opy), making such 
more automated and less work for the user (e.g. finding external library 
sources locally and/or downloading them with pip...)
			
* Continue to improve and stablize the Opy library and its beta features.

## Low Priority

* Add additional examples.

* Add documentation/examples on sys._MEIPASS and resource bundling 
with PyInstaller. 

* Add option for appending platform suffix onto installer file names. 

* Add all yet to be provided parameters for PyInstaller.  

* Add all yet to be provided elements for the various Qt IFW 
XML config classes.  

* Add Qt IFW silent install and uninstall functions. 
(For repetitive testing and debugging.)  

* Further develop the Qt IFW script generation features. 

* Add QtIFW "online" installer features.

* Add tarball alternative to zip packaging.

* Add the option to build projects outside of the build script directory.  

## Wish List		

* Add a Py2Exe wrapper as alternative to PyInstaller.

* Add Py2Exe driven functions for Windows specific features 
which PyInstaller simply lacks (e.g. COM server dll creation).

* Add an NSIS wrapper as alternative to Qt IFW.

* Add setuptools / distutil wrappers an as alternative to pip.  

* Add git integration to commit and push versions.

* Add PyPi integration to publish releases.

* Add automated version tracking / stamping / git tagging...
  
* Add (configurable) interactive ui feature, to select various 
operations at runtime (cli or gui).  Use the selected options
to define the attributes of a process class, which is subsequently
executed.  The purpose of such is to allow the developer to
select the options needed at the moment e.g. build exe, run exe, 
build installer, include obfuscation...
