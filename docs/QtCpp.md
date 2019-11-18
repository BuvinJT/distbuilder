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

	qmakeInit()
	
    qmakeArgParser()
    qmakeArgs()

	installDeployTools( askPassPath=None )
	renameExe( args )
	             
	qmakeMasterConfigFactory( args=None ) 
	qmakePackageConfigFactory( args=None ) 
	
	QtCppConfig( qtBinDirPath, exeCompiler, qmlScrDirPath=None )
	
	<Linux Only>
	QtCppConfig.CQtDeployerConfig
	
Under most circumstances, you will only need to call `qmakeInit`.  If you wish to 
customize that process or recieve additional specifications from an external source 
(e.g. QMake), you may use the other functions to emulate and custom define what the 
vanilla `qmakeInit` does for you.   

### qmakeInit     

This function provides the standard way to set up an integration which allows QMake to
drive the build process in distbuilder. The function receives parameters passed to the  
script externally (normally via a system call from QMake), and returns a tuple of 
[ConfigFactory](HighLevel.md#configfactory) objects. The first factory in the tuple is 
intended for use as a "master" from which to build robust multi-package distributions.  
The other, is to build the C++ program package.  

Since you may wish to roll your own equivalent of this, here is the entire source for 
this function:         
            
	def qmakeInit():     
	    args = qmakeArgs()
	    installDeployTools( args.askPass )
	    if args.exeName: renameExe( args )    
	    return qmakeMasterConfigFactory( args ), qmakePackageConfigFactory( args )
            
**Note:** to modify a "product" of the library, it is strongly advised that you modify the 
factory used to produce it, when possible, rather than creating an object with it first 
and then altering that.  Changing the factory attributes can prevent the need to also 
regenerate *nested* components, which may not align as desired otherwise and could lead to 
subtle problems.  While this practice is applicable to distbuilder in general, it is 
pointed out here because this standard Qt integration pattern directly involves the 
creation of factories for the client to implement, as opposed to Qt C++ 
"configuration objects" or "process objects".    

### qmakeArgParser, qmakeArgs      

If overwriting the standard `qmakeInit` function, you may call either of these 
functions directly, in order to subsequently call `qmakeMasterConfigFactory` and/or 
`qmakePackageConfigFactory`. `qmakeArgs()` directly collects the required parameters
from the script arguments. In contrast, `qmakeArgParser` returns a raw 
[ArgParse](https://docs.python.org/3/library/argparse.html) object, which may be 
*customized* to collect additional / alternate script arguments.   

### installDeployTools

Normally, you would not have to call this directly, as `qmakeInit` will for you.
This function will install any tools required to produce distributions for 
Qt C++ based programs.  

On Linux, you may wish to pass a value for the `askPassPath` argument.  That is 
needed to invoke the function from a non-tty gui context.  The value should 
define the path to an "ask password" utility e.g. "OpenSSH Askpass"   

### renameExe

In some contexts, it is desirable to rename the exe which was built by QMake, when it
comes time to package and distribute it. This is a primitive convenience function for that 
purpose.  Using the `args` object, i.e. [qmakeArgs](#qmakeArgs), passed to it to determine 
the old and new path, the orginal executable will simply be renamed (i.e. literally - on 
the file system) and the `exePath` attribute of `args` will be revised to reflect the change. 
This takes place within `qmakeInit`, allowing the rest of the subsequent configurations 
and processes to remain oblivious to this initialization task.  
            
### qmakeMasterConfigFactory, qmakePackageConfigFactory

You may bypass the `qmakeInit` function, and call either of these functions directly
to generate the corresponding ConfigFactory.  Both of the functions take an optional 
argument called `args`, which is the product of a call to `parse_args()` from an 
[ArgParse](https://docs.python.org/3/library/argparse.html) object.  If that 
is not provided, those values will be collected via the default command line mechanism.  
   
### QtCppConfig

This class is used for low level Qt C++ packaging configurations. You will NOT likely 
need to maniuplate this type of class directly, but it is included in this documentation 
for the sake of completeness.

This type of object is owned by a [ConfigFactory](HighLevel.md#configfactory), and 
(as a product of that) by a [QtIfwPackage](ConfigClasses.md#qtifwpackage) object. 
It is ultimately employed by the [buildInstaller](LowLevel.md#buildinstaller) function, 
normally invoked via a [Process Class](HighLevel.md#process-classes).  

Constructor:

    QtCppConfig( qtBinDirPath, exeCompiler, qmlScrDirPath=None )
    
Attributes:                    

    qtBinDirPath             
    exeCompiler    
    qmlScrDirPath
      
    cQtDeployerConfig   

Object Functions:
    
    qtDirPath()
    validate()
    addDependencies( package )

Static Functions:

    srcCompilerOptions() 
    exeWrapper( exePath, isGui )    
    
### QtCppConfig.CQtDeployerConfig

On Linux, distbuilder uses a tool called
[CQtDeployer](https://github.com/QuasarApp/CQtDeployer/wiki)
to assist with the build process for Qt C++ deployments.  This class
allows you to customize how that utility is employed.  Please refer
to that documentation for help.

Constructor:

    CQtDeployerConfig()
    
Attributes:      

    libDirs = []
    plugins = []
    
    <custom addition, use package names>           
    hiddenQml = []
            
    ignoreLibs = [] 
    ignoreEnv  = [] 
            
    recurseDepth = 0
    deploySystem = False            
    deployLibc   = False
    allQml       = False

    strip        = True 
    translations = True

    <open ended string to append>
    otherArgs = None

## QMake Integration

To produce an executable binary from Qt C++ source, a developer normally defines (scripted)
build configurations in the form of a "project file" (`.pro`). That `.pro` file is 
processed by [QMake](https://doc.qt.io/qt-5/qmake-manual.html) to produce the program. 
Typically, the `.pro` file initially originates from some basic template, and QMake is simply 
run automatically from Qt Creator upon selecting a "build" action from the menu.  

QMake is a very powerful mechanism, and these `.pro` files can be customized extensively to 
setup complex build processes. In addition to `.pro` files, Qt uses more dynamic, user 
specific `.pro.user` files. These are normally managed via Qt Creator tools, and not directly
edited. For extended information about such, you may wish to refer to any/all of the 
following links:

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

* Name the new configuration "Package" (or a similiar name of your choice).

* For this configuration, find the **Build steps... qmake... Additional arguments**
input field and add `CONFIG+=package`.

To then use the new build option, choose the configuration (found along with Debug, 
Release, etc.) from the menu in the bottom left corner of Creator (above the big green
"play" button). Then, select **Build... REBUILD Project** from the menu.
Do NOT chose "deploy" or "run" for this configuration, as they are not applicable.

Upon selecting this build option, a key portion of the custom QMake logic should 
be executed.  When it is, you will find important debugging information in the "General 
Messages" output pane of Creator.  If this library can't be reached, you will see critical 
error messages there, indicating what has gone wrong. If everything is in 
order, however, you should see your Python version displayed, the version of distbuilder 
being used, and the **command which will be executed to run the build script**. Note that
you may wish to copy that command and execute it directly from the command prompt / terminal
in the event you want to run the build script again without having to recompile the C++
project.

When you run the **REBUILD** operation, you will find important debugging information in 
the "Compile Output" pane of Creator.  All messages produced by the Python script will 
appear at the end of that build log.  

For more details regarding the QMake script involved, and for ways to modify (or fix)
your integration, please continue on to the [Hello World Qt Example](#hello-world-qt-example).

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
[hello.pro](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/hello/hello.pro) 
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
[package.pri](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/hello/package/package.pri).  At the top of that, you'll find:

	# Get the python interpreter path from an environmental variable, if possible.
	# Note, that may be assigned in a .pro.user. If that is not defined, fallback to
	# a hardcoded value which assumes you want to use "python" from the system path.
	PY_PATH=$$getenv( PYTHON_PATH )
	isEmpty(PY_PATH){ PY_PATH=python }
   
As denoted by the comment, this is how Python is integrated in the most elementary 
aspect of the mechanism.  If an environmental variable called `PYTHON_PATH` is defined, that
is how the interpreter will be called upon. Note that may be either universally set on your 
system, or added to your "Package" build configuration's "run settings" (i.e. in `pro.user`).  
Alternatively, a hardcoded fall back to `python` on the system path is used.  
If desired, you might change that to another fallback e.g. `python3`.   
Note that finding the interpreter will also dictate the availability of the  
library.  If you have multiple instances of Python installed, make sure you use the 
same one where you ran the pip installation for this library.

The next portion of `package.pri` is comprised of assorted support functions.  
Scroll down a bit, and you'll find the following:

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
passed around the QMake build process and finally onto distbuilder.  This provides the means
to define such info in a single "master" location.  If you check out the
[mainwindow.cpp](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/hello/mainwindow.cpp) C++ implementation file, you will see this in action on 
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

Now, onto the Python script 
[package.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qt/hello/package/package.py).  It simply contains: 

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
In [package.pri](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qml/hello/package/package.pri), 
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

## Additional Options

In addition to the options for the QMake integration demoed and discussed, there are 
a handful more worth noting. These are all optional command line switches provided by
the default `qmakeInit` mechanism.

### srcDir
  
While this parameter is optional, it's generally a good idea to specify it.  The 
`packageConfigFactory` object returned by `qmakeInit()` will have the `sourceDir`
attribute set to this. That attibute is used to resolve relative paths to resources.  
If ommited, the "source directory" will become the parent directory to the requisite 
`exePath` value (i.e. the dynamic *build directory*) where QMake produced the C++ binary.  

In the exmples provided, as is more then likely desirable, the root directory to the 
project's source has been explictly passed.  If you wish to point this base path for 
resources to some other location (e.g. a sub directory within your project), you may 
do so with this option.

### resource 

The `--resource` switch (or `-r` for short) maybe passed repeatedly.  Use this
to bundle additional files or directories into the package.  Note that relative paths 
will be resolved against the `--srcDir` switch.

If you need to place the resource within a **nested** subdirectory in the target package
(or simply rename the resource in the product), you may pass a semicolon `;` delimited
pair of paths.  The first value in the pair is the source, and the second is the target
path relative to the target package root.  

Example:

	-r "readme.txt;docs/help.txt"
	
This would bundle the `readme.txt` (on the `--srcDir` root) into the package within a
sub directory called "docs" and would rename the file "help.txt". 	   

You may, of course, add resources to the package from within the Python build script,
rather than passing that in from an external source in this manner.    

### exeName

In some contexts, it is desirable to rename the exe which was built by QMake, when it
comes time to package and distribute it.  This switch is employed by the simple 
[renameExe](#renameExe) function via the the default `qmakeInit` mechanism.

### askPass
	
This option is only pertinent for Linux users.

In the examples, you'll find this near the end of the package QMake script:  
  
    # On Linux, you may optionally provide a custom "AskPass" program to handle
    # password input for root/sudo privileges if required
    #linux: packageCmd += --askPass $$quot( $$clean_path( /usr/share/git-cola/bin/ssh-askpass ) )

In order to run the integration from a non-tty gui context (e.g. Qt Creator),
you will need to lean on an "ask password" utility.  When you attempt to use the 
package script for the first time, it may fail because no such tool is found on the
system. It will suggest you install "OpenSSH Askpass".  If you prefer something else,
or have that installed in a path the script can't locate, uncomment this QMake
directive and provide that detail (e.g. the git-cola path demoed).
    