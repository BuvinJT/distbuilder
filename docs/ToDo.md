# To-Do List 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)
 
## High Priority

* Add additional examples.

* Continue to expand upon the documentation, especially with
regard to the various configuration options.

* Add support to high level "process" class for multiple PyInstaller 
builds / "package" (sub-component) creation via project sub directory 
divisions.

* Add support for multiple Qt IFW packages.

## Moderate Priority

* Test on more Linux distros

* Test QtIFW use on terminals / non-gui Linux distros like CentOS 
(silent installs / noninteractive). Look into options for producing such 
explictly (maybe a PyInstaller wrapper?) so the user does not have to pass a 
switch. 

* Further develop external library bundling (for Opy), making such 
more automated and less work for the user (e.g. finding external library 
sources locally and/or downloading them with pip...)
			
* Continue to improve and stablize the Opy library and its beta features.

* Add documentation/examples on sys._MEIPASS and resource bundling 
with PyInstaller. 

* Add option for appending platform suffix onto installer file names. 

## Low Priority

* Add the options to build projects outside of the project directory.  
(Both the source and the temp build directories.)  

* Add all yet to be provided parameters for PyInstaller.  

* Add all yet to be provided elements for the various Qt IFW 
XML config classes.  

* Add Qt IFW silent install and uninstall functions. 
(For repetitive testing and debugging.)  

* Further develop the Qt IFW script generation features. 

* Add tarball alternative to zip packaging.

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
