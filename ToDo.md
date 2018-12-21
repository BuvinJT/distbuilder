# Distribution Builder (distbuild) 

### HIGH LEVEL DOTO LIST

* Test on platforms other than Windows! 
	(should work in theory, but confirmation required)
	
* Create a top level "shared info" class, for data that is used by
more than one process e.g. the product name, version, etc.

* Add version file generation to pyInstaller wrapper.

* Further develop the Qt IFW wrapper to the point that the entire installer 
definition can be generated on the fly (at least a primitive installer
with no custom scripting).  Include shortcut creation (done via qscript). 

* Add Qt IFW uninstall function.

* Add support for multiple Qt IFW packages.

* Add the options to build projects outside of the project directory.  
	(Both the source and the temp build directories.)
			
* Add tarball alternative to zip packaging.

### Wish List		

* Further develop external library bundling (for obfuscation), making such 
more automated and less work for the user (e.g. finding sources and
downloading them with pip...)

* Add an NSIS Wrapper as alternative to Qt IFW

* Add setuptools / distutil wrappers an as alternative to pip  

* Add git integration to commit and push build results

* Add (configurable) interactive ui option, to select various 
operations at runtime. (Command prompt and/or gui?)
Simple version would be an easy way to define a list of
check box options.  Then when run, the developer could
select the options he wants at the moment e.g.
build exe, run exe, build installer, include obfuscation...

* Add automated version tracking / stamping / tagging...
