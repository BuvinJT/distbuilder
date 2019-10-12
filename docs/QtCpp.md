# Qt C++ Integration
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Overview

The developers of Distribution Builder work in many languages and frameworks extending
beyond Python.  Ultimately, we hope to provide a collection of rapid integration modules
for this library into for other modes of software development.  

The first of these integrations we are rolling out is a ready means to allow your 
[Qt](https://www.qt.io/) C++ programs to flow directly into this tool.  The library can 
then be used as a middleman between the [Qt Creator](https://doc.qt.io/qtcreator/) IDE and the  
[Qt Installer Framework](http://doc.qt.io/qtinstallerframework).  

This mechanism provides far more flexibliy than simply connecting those tools, however.  
Other packages, notably Python based programs, can be built and bundled together simultaneously.
This design pattern gives you the full power of Distribution Builder (and Python on the whole) 
by which to extend your Qt build process.

## QMake Integration

Note: To modify the package, modify the factory, 
in order avoid missing nested components! 

For example, to override the wrapper script: 
 
	packageFactory.pkgExeWrapperScript = ExecutableScript("hello",script="notepad")
	helloQtPkg = configFactory.qtIfwPackage()

NOT

	helloQtPkg = configFactory.qtIfwPackage()
	helloQtPkg.exeWrapperScript = ExecutableScript("hello",script="notepad")
	
The later fails to modify the nested package script, which contains the qscript
to generates the program shortcut on the target, so while most of this
would appear to be functional, there would be a subtle glitch introduced to the product. 

## Qt Module

### QtCppConfig:

Used for Qt C++ integration.

Constructor:

    QtCppConfig( qtBinDirPath, exeCompiler, qmlScrDirPath=None  )
    
Attributes:                    

    qtBinDirPath             
    exeCompiler    
    qmlScrDirPath     

## Hello World Qt Example

## Hello World QML Example
