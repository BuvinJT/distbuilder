# Qt C++ Integration
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Overview

The developers of Distribution Builder work in many languages and frameworks extending
beyond Python.  Ultimately, we hope to provide a collection of rapid integration modules
for this library for other modes of software development.  

The first of these integrations we are rolling out is a ready means to allow your 
[Qt](https://www.qt.io/) C++ programs to flow directly into this tool.  The library can 
then be used as a middleman between [Qt Creator](https://doc.qt.io/qtcreator/) and the  
[Qt Installer Framework](http://doc.qt.io/qtinstallerframework). This mechanism provides 
far more flexibility than simply bridging those tools, however. Other packages, notably 
Python based programs, can be built and bundled together simultaneously. This design 
pattern gives you the full power of Distribution Builder (and Python on the whole) 
by which to extend your Qt build process.

If you have not done so yet, it is strongly recommended that you you get your feet wet 
with this library by at least reviewing [Getting Started](QuickStart.md#getting-started) 
prior to diving into this extended feature set.  Also, you will need to be versed in using
Qt Creator and writing code with the Qt Library in order to make use of this, or follow 
the examples / documentation. 

## Qt C++ Module

A module has been provided in distbuilder which is specifically dedicated to Qt C++
integration, i.e. `distbuilder.qt_cpp`.  The following functions / classes can be imported 
from that: 

### qmakeInit     

This function provides the standard way to set up the mechanism to have QMake
drive the build process in distbuilder. The function receives parameters passed to the  
script externally (normally as arguments from a QMake invocation), and returns a tuple of 
[ConfigFactory](HighLevel.md#configfactory) objects. This first of these is intended for 
use as a "master" for building robust multi-package distributions.  The other, to build 
the C++ program package specifically.  

Example:         
            
	masterFactory, packageFactory = qmakeInit()
            
Note, to modify a Qt C++ package, it is strongly advised that you modify the factory
used to produce it, rather than creating the package and then altering that product.  
This prevents the need to also regenerate nested components, which may not align as 
desired otherwise and could lead to subtle problems.  While this practice is applicable
to distbuilder in general, it is pointed out here because this standard Qt integration
pattern directly involves the creation of factories for the client to then implement.    
            
### qmakeMasterConfigFactory, qmakePackageConfigFactory

You may bypass the `qmakeInit` function, and call either of these functions directly
to generate the corresponding ConfigFactory.  Both of the functions take an optional argument called `args`, which is the product of a call to `parse_args()` from an 
[ArgParse](https://docs.python.org/3/library/argparse.html) object.  If that 
is not provided, those values will be collected via the standard mechanism.  
  
### qmakeArgs, qmakeArgParser      

If overwriting the standard `qmakeInit` function, you may call either of these 
functions directly, in order to subsequently call `qmakeMasterConfigFactory` and/or 
`qmakePackageConfigFactory`. `qmakeArgs()` directly collects the required parameters
from the script arguments. In contrast, `qmakeArgParser` returns a raw 
[ArgParse](https://docs.python.org/3/library/argparse.html) object, which may be 
*customized* to collect additional / alternate script arguments.   

### installDeployTools

Normally, you should not have to call this directly, as the library will as needed.
It has been made public though, in the event you wish to explicitly, on demand.  
This function will install any tools required to produce distributions for 
Qt C++ based programs.  

On Linux, you may wish to pass a value for the `askPassPath` argument.  That is 
needed to invoke the function from a non-tty gui context.  The value should 
define the path to a "ask password" utility e.g. "OpenSSH Askpass"   
   
### QtCppConfig:

This class is used for Qt C++ integration.  It is employed by a 
[ConfigFactory](HighLevel.md#configfactory) when producing a package for
a Qt C++ program.  

Constructor:

    QtCppConfig( qtBinDirPath, exeCompiler, qmlScrDirPath=None  )
    
Attributes:                    

    qtBinDirPath             
    exeCompiler    
    qmlScrDirPath     

Object Functions:
    
    validate
    addDependencies( package )

Static Functions:

    srcCompilerOptions() 
    exeWrapper( exePath, isGui )    

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
run the demos, you must first **manually** perform the following tasks when 
you open one of these `.pro` files for the first time on a given machine:

* From the "Projects" screen, **clone** a "Release" build configuration.

* Name the new configuration "Package".

* For this configuration, add "CONFIG+=package" to the **Build steps...Additional arguments** section.

To then use the new build option, choose the configuration (found along with Debug, 
Release, etc.) from the menu in the bottom left corner of Creator (above the big green
"play" button). Then, select **REBUILD** from the menu.  Do NOT chose "deploy" or "run" 
for this configuration.

Upon selecting the build option, a key portion of the custom QMake logic should 
be executed.  When it is, you will find important debugging information in the "General 
Messages" output pane of Creator.  If this library can't be reached, will you see critical 
error messages there, indicating why the configuration cannot be used. If everything is in 
order, however, you should see your Python version displayed, the version of distbuilder 
being used, and the command which will be executed to run the build script.

For more details regarding the QMake script involved, and for ways to modify (or fix)
your integration, please refer to the [Hello World Qt Example](#hello-world-qt-example) 
section.

## Hello World Qt Example

This example Qt project was initially created from a simple built-in template, 
i.e. what is given to you upon selecting a new "Qt Widgets Application" project in 
Creator.  It was then modified slightly for this demo. This illustrates how you can 
rapidly package a Widgets based program for distribution via this Python library.

All of the examples discussed here are included in the "source distribution" of the 
library. The [PyPi downloads](https://pypi.org/project/distbuilder/#files) 
page for this project is arguably the fastest route to acquire the examples.  
Unlike many of the other examples stepped through in this documentation, not every file
will be explicitly listed and discussed here.  

Once you have the examples source, launch Qt Creator. Then select 
`File... Open File Or Project...`, browse to the examples sub directory named `hello_qt`,
and select `hello.pro`.   

Upon opening the project, follow the instructions in the above 
[QMake Integration](#qmake-integration) section.  Test your new "Package" build configuration.  If anything fails, you might well spot your incompatibility by stepping
through the QMake.  

The place to begin this code review is in the 
[hello.pro](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/hello.pro) 
file.  It starts with pure boiler plate QMake, and then ends with the following:


	# DISTRIBUTION BUILDER INTEGRATION
	#==============================================================================
	include(package/package.pri)
	message(Commands to execute upon rebuild:)
	message($${QMAKE_POST_LINK})

What this accomplishes is the inclusion of a "sub project" within the main one called 
"package".  That sub project has a corresponding sub directory, and `.pri` file of the same 
the name.  This sub project include the resources for packaging the application, and all
of that has been encapsulated rather then blending it with the rest of the work.  This
template gives you an easy means to copy and paste this feature into your own existing 
work.

If you expand the "package" sub project in the side bar, you'll find the `pri`, and "Other Files", which contains `package.py`.  The Python script is the distbuilder "build" script.  We elected the name that script "package" (along with rest of the sub project), so as to 
not conflate the meaning of "build" in C++ with this additional step.       

Next, let's look over 
[package.pri](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/package/package.pri).  At the top of that, you'll find:

	# Hardcode the path to your Python interpreter here.
	# Or, alternatively, use the (commented out) environmental variable method
	PY_PATH=python
	#PY_PATH=$$getenv( PYTHON_PATH )
   
As denoted by the comment, this is how Python is integrated in the most elementary 
aspect of the mechanism.  In the example, it is simply assumed you wish to use 
`python` on the system path.  If that is not correct for your environment, you may 
change that here.  Alternatively, define environmental variable called `PYTHON_PATH` 
and use that configuration method.  You may either do so universally on your system,
or add that to your "Package" build configuration "run settings" (i.e. via a `pro.user`
modification).  Note that interpreter path will also dictate the availability of the  
library.  If you have multiple instances of Python installed, make sure you use the 
same one where you ran the pip install.

The next portion of `package.pri` is comprised of assorted support functions.  Scroll down a bit, and you'll find the following:

	# Global application info shared across the C++ layer,
	# the binary branding, and the Python installation builder!
	DEFINES += $$globalStrDef( APP_VERSION, 1.0.0.0 )
	DEFINES += $$globalStrDef( COMPANY_TRADE_NAME, Some Company )
	DEFINES += $$globalStrDef( COMPANY_LEGAL_NAME, Some Company Inc. )
	DEFINES += $$globalStrDef( COPYRIGHT_YEAR, $${currentYear} )
	DEFINES += $$globalStrDef( PRODUCT_TITLE, Hello World QML Example )
	DEFINES += $$globalStrDef( PRODUCT_DESCRIPTION, A Distribution Builder Example )

In this section, the custom details are defined for the name of the product, and 
company, etc. Note, these values cascade down in the C++ in addition to being 
passed the QMake build process and finally onto distbuilder.  This provides the means
to define such info in a single "master" location.  If you check out the
[mainwindow.cpp](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/mainwindow.cpp) C++ implementation file, you will see this in action on 
that side of the equation.

Just below, the `.pri` contains:

	SETUP_NAME=HelloQtSetup
	
	win32: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.ico
	win64: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.ico
	macx:  ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.icns
	linux: ICON_PATH=$${_PRO_FILE_PWD_}/icons/demo.png

This section let's you define the name of setup file to be ultimately produced, along 
with relative paths to icons.

As you continue on, the script effectively builds a command to append onto 
`QMAKE_POST_LINK`.  That is way in which the Python script is executed upon rebuilding
the project using the "Package" build configuration.

Of note for Linux users, this is found near the end of the QMake:  
  
    # On Linux, you may optionally provide a custom "AskPass" program to handle
    # password input for root/sudo privileges if required
    #linux: packageCmd += --askPass $$quot( $$clean_path( /usr/share/git-cola/bin/ssh-askpass ) )

In order to run the integration from a non-tty gui context (e.g. Qt Creator!).
You will need to lean on an "ask password" utility.  When you attempt to use the 
package script for the first time, it may fail because it has no such tool found on the
system. It will suggest you install "OpenSSH Askpass".  If you prefer something else,
or have that installed in a path the script can't locate, uncomment this QMake
directive and provide that detail.

Now, onto the Python script 
[package.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/package/package.py).  It simply contains: 

	from distbuilder import RobustInstallerProcess   
	from distbuilder.qt_cpp import qmakeInit
	
	masterFactory, packageFactory = qmakeInit()
	helloQtPkg = packageFactory.qtIfwPackage()
	p = RobustInstallerProcess( masterFactory, ifwPackages=[helloQtPkg],
	                            isDesktopTarget=True )
	p.isTestingInstall = True
	p.run()

Most of this has been explained the [Qt C++ Module](#qt-c++-module) section and / or
the basic examples in [Getting Started](QuickStart.md#getting-started).  The key points
to point out are:

	masterFactory, packageFactory = qmakeInit()
  
Creates [ConfigFactory](HighLevel.md#configfactory) objects, 
using the QMake passed values. 

	helloQtPkg = packageFactory.qtIfwPackage()

Creates a [QtIfwPackage](ConfigClasses.md#qtifwpackage) object.

	p = RobustInstallerProcess( masterFactory, ifwPackages=[helloQtPkg],
	                            isDesktopTarget=True )

Creates a [RobustInstallerProcess](HighLevel.md#robustinstallerprocess),
which will employ the `masterFactory` and include the package containing
the C++ program.

## Hello World QML Example

This example was initially created from what is given to you upon selecting a new 
"Qt Quick Application - Canvas 3D" (including three.js) project in Creator.  
It was then modified for this demo.  Notably, some refactoring was done to shuffle
select components into a "ux" sub project.  This illustrates how you can rapidly 
package a QML based program, (with some dependencies and resources) for distribution
via this Python library.  

Assuming you already have the examples source, launch Qt Creator. Then select 
`File... Open File Or Project...`, browse to the examples sub directory named `hello_qml`,
and select `hello.pro`.   

Upon opening the project, follow the instructions in the above 
[QMake Integration](#qmake-integration) section.  Test your new "Package" build configuration.  

Other than the C++ side of this, this example is nearly identical to the more primitive
[Hello World Qt Example](#hello-world-qt-example). There is one key difference.
In [package.pri](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qml/package/package.pri), 
near the end you find this line:

    qmlSourcePath = $${_PRO_FILE_PWD_}/ux 

Then, as `packageCmd` is being built, you'll find `qmlSourcePath` used:

	-q $$quot( $$clean_path( $${qmlSourcePath} ) )    
	
This was the reason why the basic template was revised, to create a `ux` sub project
/ sub directory.  The tools used in distbuilder to find and collect the dependencies 
for QML components require a directory path to where the QML source resides for the 
project.  The process works ideally if it scans a directory (recursively) which is 
reserved primarily for these specific files.  It is a good practice to keep your C++ 
and QML split apart anyway, so this is a logical design either way. 


	
    