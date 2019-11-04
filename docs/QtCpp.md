# Qt C++ Integration
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Overview

The developers of Distribution Builder work in many languages and frameworks extending
beyond Python.  Ultimately, we hope to provide a collection of rapid integration modules
for this library into for other modes of software development.  

The first of these integrations we are rolling out is a ready means to allow your 
[Qt](https://www.qt.io/) C++ programs to flow directly into this tool.  The library can 
then be used as a middleman between [Qt Creator](https://doc.qt.io/qtcreator/) and the  
[Qt Installer Framework](http://doc.qt.io/qtinstallerframework). This mechanism provides 
far more flexibliy than simply connecting those tools, however. Other packages, notably 
Python based programs, can be built and bundled together simultaneously. This design 
pattern gives you the full power of Distribution Builder (and Python on the whole) 
by which to extend your Qt build process.

## QMake Integration

To produce an executable binary from Qt C++ source, a developer normally defines (static) 
build configurations in the form of a "project file" (`.pro`). Then, that `.pro` file is 
processed by [QMake](https://doc.qt.io/qt-5/qmake-manual.html). Typically, the `.pro` file 
initially originates from some basic template, and QMake is simply run automatically from 
Qt Creator upon selecting a "build" action.  

QMake is a very powerful mechanism, and these `.pro` files can be customized extensively to 
setup complex build processes. In addition to `.pro` files, Qt uses more dynamic, user 
specific `.pro.user` files. These are normally managed via Qt Creator tools. For extended
information about such, you may wish to refer to any/all of the following links:

* [Opening Projects](https://doc.qt.io/qtcreator/creator-project-opening.html)

* [Configuring Projects](https://doc.qt.io/qtcreator/creator-configuring-projects.html).

* [Editing Build Configurations](https://doc.qt.io/qtcreator/creator-build-settings.html#editing-build-configurations)

As illustrated in the Qt demos here, you can setup an easy workflow to allow use of this 
Python library from Qt Creator.  The demos include custom QMake scripting which you may 
copy into your own projects. Using these demo templates, the setup procedures are short 
and sweet, but they do span both `.pro` and `.pro.user` files.   

Since `.pro.user` files are specific to a user's environment, there is no way to 
distribute those in a manner which would work anything close to universally.  As such, to
run the demos, you must first *manually* perform the following tasks when 
you open one of these `.pro` files for the first time:

* From the "Projects" screen, **clone** a "Release" build configuration.

* Name the new configuration "Package".

* For this configuration, add "CONFIG+=package" to the **Build steps...Additional arguments** section.

To then use the new build option, choose the configuration (found along with Debug, 
Release, etc.) from the menu in the bottom left corner of Creator (above the big green
"play" button). Then, select **REBUILD** from the menu.  Do NOT chose "deploy" or "run" 
for this configuration.

Upon selecting this build option, a key portion of the custom QMake logic should 
be executed.  When it is, you will find important debugging information in the "General 
Messages" output pane of Creator.  If this library can't be reached, will you see critical 
error messages there, indicating why the configuration cannot be used. If everything is in 
order, however, you should see your Python version displayed, the version of distbuilder 
being used, and the command which will be executed to run the build script.

For more details regarding the QMake script involved, and for ways to modify (or fix)
your integration, please refer to the [Hello World Qt Example](#hello-world-qt-example) 
section.

## Qt Module

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
