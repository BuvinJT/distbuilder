# High Level Classes  
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## ConfigFactory  

It is typical for a build script to start by creating
a high-level *ConfigFactory* object and set its attributes.

The major functions within the library rely
upon a collection of "configuration" objects which supply
extended sets of parameters to drive various processes.  Many of these 
classes have overlapping attributes, and scripts employing 
a series of those (on a low level) tend to have a great deal of redundant
parameter assignment.  With this in mind, the ConfigFactory class 
was created.

See [Configuration Classes](ConfigClasses.md#configuration-classes) for more 
information on the types of objects generated by this factory class.  

Note that this class is NOT intended to have a one-to-one correspondence 
for **every** attribute within all of the configuration objects it can generate.
If that were provided, this class would become an overwhelmingly bloated monster! 
Only the more commonly needed (and/or shared) attributes are provided on this level.  You 
must manipulate those config objects generated by the factory *directly* if you need to 
access their more extended features.  Typically, you will want to access those
objects from a "callback" function within a derived "Process" class implementation.    

Constructor:

    ConfigFactory( cfgId=None )
    
Attributes & default values:  

	cfgId = None                                             

    productName = None
    description = None
    
    companyTradeName = None
    companyLegalName = None      

	isObfuscating = False             
    opyBundleLibs = None
    opyPatches    = None
    
    binaryName = None  
    version    = (0,0,0,0)
    isGui      = False           
    
    sourceDir     = None
    entryPointPy  = None
    specFilePath  = None
    iconFilePath  = None
    distResources = []       

    isSilentSetup    = False    		
    setupName        = "setup"
    ifwDefDirPath    = None
    ifwPackages      = None
    
    replaceTarget = False

    ifwUiPages	= None
       
    ifwCntrlScript     = None # None=Default False=Exclude                
    ifwCntrlScriptText = None
    ifwCntrlScriptPath = None
    ifwCntrlScriptName = "installscript.qs"

    ifwPkgId         = None
    ifwPkgName       = None
    ifwPkgNamePrefix = "com"        
	       
    ifwPkgScript     = None           
    ifwPkgScriptText = None
    ifwPkgScriptPath = None        
    ifwPkgScriptName = "installscript.qs"

    pkgType       = None    
    pkgSubDirName = None
    pkgSrcDirPath = None
    pkgSrcExePath = None
    pkgExeWrapper = None

    qtCppConfig      = None
 
Object creation functions:
     
    pyInstallerConfig()    
    opyConfig()
    qtIfwConfig( packages=None )
    qtIfwConfigXml()
    qtIfwControlScript()
    qtIfwPackage( pyInstConfig=None, isTempSrc=False )
    qtIfwPackageXml()    
    qtIfwPackageScript( pyInstConfig=None )
    qtIfwExeWrapper( wrapperScript=None,
                     workingDir=None, isElevated=False, 
                     envVars=None, args=None )
Cloning:

    newFactory = ConfigFactory.copy( instance )
    
#### cfgId                                              

Useful to distinguish between multiple ConfigFactory objects, as
are often employed by a [RobustInstallerProcess](#robustinstallerprocess). 

#### productName, description

The name and description for the product on the whole, or a sub component
within it (based upon the context of how the factory object is used).  Such
will appear as "brandings" upon a [Stand Alone Executable](LowLevel.md#stand-alone-executables) 
and/or as labels/details within [Installer](LowLevel.md#installers) menus.  

#### companyTradeName, companyLegalName       

Akin to `productName` and `description` attributes.  

Note the `companyTradeName` will be used in standard labels, directory names, shortcuts, etc.
produced by the process employing the ConfigFactory.  In contrast, `companyLegalName`
will appear within copyrights, EULAs, and the like where an "official" / legal name is 
called for.  

#### isObfuscating, opyBundleLibs, opyPatches

The `isObfuscating` switch toggles whether code obfuscation is employed by a process
using the config factory (based upon context).  

The `opyBundleLibs` and `opyPatches` are details used for generating an 
[OpyConfig](ConfigClasses.md#opyconfig) object when invoking the `opyConfig()`
function for this class.
 
For more information, refer to the following:

- [Executable Obfuscation](LowLevel.md#executable-obfuscation)  
- [Obfuscation Features](LowLevel.md#obfuscation-features)  
- [Hello World Tk Example](Examples.md#hello-world-tk-example)    
- [Opy for Distribution Builder](https://pypi.org/project/opy-distbuilder/)

#### version

Akin to `productName` and `description` attributes, this can be applied to
either a [Stand Alone Executable](LowLevel.md#stand-alone-executables) 
or an [Installer](LowLevel.md#installers) based on the context of what uses
the config factory.

A version should be defined as a 4 part tuple of unsigned integers, in the form:

    ( MAJOR, MINOR, PATCH, BUILD )

Alternatively, a string representation may be supplied.
See [versionTuple, versionStr](LowLevel.md#versiontuple,-versionstr).

Note that each part maybe any number of digits long.  i.e. this is a perfectly 
valid version stamp: `2.11.6.139`.  That example would be denoted in tuple form 
as: `(2,11,6,139)` 	

#### binaryName, isGui           

These are attribute used for a variety of purposes, which would be difficult to 
list here. Most notably, they are applied directly to the production of  
[Stand Alone Executables](LowLevel.md#stand-alone-executables). In that specific 
process these details are set on a [PyInstallerConfig](ConfigClasses.md#pyinstconfig) 
object when invoking the `pyInstallerConfig()` function for this class.
  
#### sourceDir

This attribute is used to resolve relative paths to absolute paths in various 
contexts. When omitted, such paths are normally resolved relative to the directory 
containing the build script (NOT the current working directory!).

#### entryPointPy 

This attribute is most notably used when producing a 
[Stand Alone Executable](LowLevel.md#stand-alone-executables).
In that context, it points PyInstaller to the starting point for the source from which 
to build a binary.

This is also used during an [Executable Obfuscation](LowLevel.md#executable-obfuscation)
process.  The entry point module **name** is **not** obfuscated (though its contents are). 

#### specFilePath

This attribute is a relatively sophisticated component used for   
producing a given [Stand Alone Executable](LowLevel.md#stand-alone-executables).
Most users of this library will never need to use this, though some may
wish to if they are migrating from a legacy build script which employed
a PyInstaller "spec file" they maintained.

This attribute is a means to specify a relative file path to an existing 
"spec" file. 

Note that distbuilder provides a [PyInstSpec](ConfigClasses.md#pyinstspec)
class which allows for programmatic generation and manipulation of such
files and configurations.  Also, many of the process classes which employ a 
config factory provide an `onMakeSpec( spec )` function.  And, if writing your 
own low level equivalents of the process class operations, the library provides
an [makePyInstSpec](LowLevel.md#makePyInstSpec) function.

#### iconFilePath

Based upon context, this attribute is used to embedded (or bundle) an icon for
a [Stand Alone Executable](LowLevel.md#stand-alone-executables) or an
[Installer](LowLevel.md#installers). 

As demoed in the [Hello World Example](Examples.md#hello-world-example),
on Windows you must use a ".ico" file, on macOS a ".icns", or on Linux a ".png".
You do NOT have to specify the extension, however, when setting this attribute.
Such will be automatically determined per the platform at runtime. 

#### distResources        

The `distResources` attribute is an optional list of external resources to bundle 
into the distribution package.  You may use a simple list of strings containing 
file/directory names or paths *relative* to the build script directory. Else, you 
may provide a list of two element tuples, with a specific source and destination. 
See **distResources** within [buildExecutable](LowLevel.md#buildExecutable) for
more details on this.
    
Notably, this attribute is used when generating a 
[PyInstallerConfig](ConfigClasses.md#pyinstconfig)
object when invoking the `pyInstallerConfig()` function for this class, 
and then utlimately invoking the low level 
[buildExecutable](LowLevel.md#buildExecutable) operation with that.
Note this may be done for you via various high level process classes.

This attribute is also used for producing a
[QtIfwPackage](ConfigClasses.md#qtifwpackage) object when invoking the
`qtIfwPackage()` function for this class.
This too may be done for you via various high level process classes.

#### setupName

This is the file name given to a QtIFW installer when the config factory is used in a 
context to produce one. This attribute is specifically applied when generating a 
[QtIfwConfig](ConfigClasses.md#qtifwconfig) object upon invoking the `qtIfwConfig()`
function for this class.

#### isSilentSetup

When `isSilentSetup` is enabled, the QtIFW installer produced will not display a GUI or 
provide any interactive prompts for the user.  All options are dictated by command line 
arguments. While this may certainly be desirable on any platform, it is  
*necessary* to create an installer for a target OS with no GUI (e.g. many Linux distros).

For more information refer to: 

- [buildInstaller](LowLevel.md#buildInstaller)
- [Silent Installers](LowLevel.md#silent-installers)
- [Hello Silent Example](Examples.md#hello-silent-example)        

#### ifwDefDirPath

When producing a QtIFW installer this attribute may *optionally* be used to specify 
an external, hard coded definition for the installer.  This is useful when either 
integrating the distbuilder library with an existing QtIFW installer, or when a 
developer would prefer to use the traditional QtIFW approach (perhaps due to extensive 
customizations).    

Note: This hard coded definition may include target installation content, and it 
may be used as a **partial** definition or **hybrid** with distbuilder manipulations 
and additions applied to it.    
   
This attribute is specifically applied when generating a 
[QtIfwConfig](ConfigClasses.md#qtifwconfig) object upon invoking the `qtIfwConfig()`
function for this class.

#### ifwPackages

When producing a QtIFW installer, this attribute maybe used to list of "Qt IFW Packages".
Items in this list may be dynamic [QtIfwPackage](ConfigClasses.md#qtifwpackage) objects,
or be simple strings defining relative paths to QtIFW packages which are defined
as external resources, in the traditional (hard coded, content containing) IFW manner.

When building Python only derived installers, this attribute will be set automatically 
by a process class, and *NOT* have to be manually defined or manipulated unless 
there is a need to merge or modify packages pro grammatically.      

This attribute is specifically applied when upon invoking the `qtIfwPackage()`
function for this class.

For more information refer to: 

- [RobustInstallerProcess](#robustinstallerprocess)
- [QtIfwPackage list manipulation](LowLevel.md#qtifwpackage-list-manipulation) 

#### replaceTarget

When producing a QtIFW installer, switch this attribute to `True` if you wish for the
installer to automatically replace a prior installation.  On Windows, this will referrence
the applications registered in the OS, and run the uninstallation for the prior install
via that mechanism.  On other platforms, this uses the QtIFW Maintenance Tool directly to 
"silently" uninstall a prior install found at the target location.

#### ifwUiPages

Use this to specify a list of [QtIfwUiPage](ConfigClasses.md#qtifwuipage) 
objects.  With that, you may fully customize the installer's UI using the
[Qt Designer WYSIWYG](https://doc.qt.io/qt-5/designer-quick-start.html) tool!

[Installer Scripting](LowLevel.md#installer-scripting), or the higher level
script abstraction classes [QtIfwControlScript](ConfigClasses.md#qtifwcontrolscript) and
[QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript) can be used to provide
dynamic features for the page. 

#### ifwCntrlScript, ifwCntrlScriptText, ifwCntrlScriptPath, ifwCntrlScriptName

QtIFW installers may have a "Control Script" and/or a collection of "Package Scripts".
The "Control Script" is intended to dictate how the installer *interface*  behaves, and
other high level logic pertaining to the installer itself. In contrast, "Package Scripts"
are intended for applying custom logic to manipulate a target environment when installing 
a given package.

These "Control Script" attributes are specifically applied when invoking the 
`qtIfwControlScript()` function for this class.

The attributes `ifwCntrlScript`, `ifwCntrlScriptText`, `ifwCntrlScriptPath` are mutually
exclusive.  Only one will be applied (the others such be set to `None`), with the 
priority being in that order. 

The `ifwCntrlScript` attribute is a [QtIfwControlScript](ConfigClasses.md#qtifwcontrolscript)     
object.

The `ifwCntrlScriptText` attribute is a means to supply the script as a raw string.

The `ifwCntrlScriptPath` is a file path (relative to the build script) to an externally 
defined script.

`ifwCntrlScriptName` provides a means to define the name of the file generated, in case 
there is need or desire to override the default. 
      
#### ifwPkgScript, ifwPkgScriptText, ifwPkgScriptPath, ifwPkgScriptName

QtIFW installers may have a "Control Script" and/or a collection of "Package Scripts".
The "Control Script" is intended to dictate how the installer *interface*  behaves, and
other high level logic pertaining to the installer itself. In contrast, "Package Scripts"
are intended for applying custom logic to manipulate a target environment when installing 
a given package.

These "Package Script" attributes are specifically applied when invoking the 
`qtIfwPackageScript()` function for this class.

The attributes `ifwPkgScript`, `ifwPkgScriptText`, `ifwPkgScriptPath` are mutually
exclusive.  Only one will be applied (the others such be set to `None`), with the 
priority being in that order. 

The `ifwPkgScript` attribute is a [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript)     
object.

The `ifwPkgScriptText` attribute is a means to supply the script as a raw string.

The `ifwPkgScriptPath` is a file path (relative to the build script) to an externally 
defined script.

`ifwPkgScriptName` provides a means to define the name of the file generated, in case 
there is need or desire to override the default. 

#### ifwPkgId, ifwPkgName, ifwPkgNamePrefix         

These attributes are utilized to differentiate [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
objects, and the packages which are produced for an installer.

`ifwPkgId` is employed for distbuilder operations where multiple packages are
involved. For more information refer to: 

[RobustInstallerProcess](#robustinstallerprocess). 

[QtIfwPackage list manipulation](LowLevel.md#qtifwpackage-list-manipulation) 

`ifwPkgName` and `ifwPkgNamePrefix` are provided to override the name used by the
QtInstaller for deployment on a target environment.  Normally, you may allow
distbuilder to set the name for you automatically.

#### pkgType    
	
The type (`QtIfwPackage.Type`) of package being built.  If this is omitted and a 
`binaryName` attribute is specified, `PY_INSTALLER` is assumed.  If there is no type 
provided, and no `binaryName`, the `DATA` type is assumed.  Other options are also possible. This list is expected to grow over time:

	QtIfwPackage.Type.DATA
	QtIfwPackage.Type.PY_INSTALLER
	QtIfwPackage.Type.QT_CPP

#### pkgSubDirName

If a `pkgSubDirName` is specified, this places the package inside of sub directory, 
rather than having the contents there of installed directly to the top level directory
of the target.

By default, this attribute is `None`, which is ideal for single package products. 
When multiple packages are present, however, the content of each will be merged into 
one directory during installation (if the end user selects more than one package).  
In the event "collisions" could occur (at installation or run time) due to this, 
the suggested resolution is to employ this option, thereby encapsulating the package(s). 

#### pkgSrcDirPath, pkgSrcExePath

When building installers that have external resources which are not part of
automatically generated products/packages, these attributes may be used to define the paths
to that package's content.  

When the `pkgSrcDirPath` is not supplied, this is path defined 
by either a [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig) object definition,
or assumed to simply be a sub directory adjacent to the build script
*with the same name* as the `binaryName` attribute.

The attribute `pkgSrcExePath` must only be supplied when the package contains a
"primary" executable which was not produced by a process with the library (i.e. 
it was complied previously by some other build system).  Note, that if `binaryName`
is also defined, the `pkgSrcExePath` file will be renamed to that name upon building
the package. 

See: [RobustInstallerProcess](#robustinstallerprocess). 

#### pkgExeWrapper 

A [QtIfwExeWrapper](ConfigClasses.md#qtifwexewrapper) object used to "wrap"
the primary executable in a [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
being built using the factory provided configurations.

Such a wrapper can super impose environmental conditions on the context
within which the binary is run.  Notably, this may include an 
[ExecutableScript](LowLevel.md#executablescript) for maximum flexibility.
Follow the links to learn to more.

#### qtCppConfig

A [QtCppConfig](ConfigClasses.md#qtcppconfig) object.  Used to define how to
package programs developed within the Qt C++ libraries / framework. 

See the [Qt C++ Integration](QtCpp.md) document for more information.  
    
## Process Classes Overview

Many build scripts will follow the same essential
logic flow, to produce analogous distributions. 
As such, using high-level "process classes" can prevent 
having multiple implementation scripts be virtual 
duplicates of one another, each containing a fair volume 
of code which employs the "low level" functions in the
library.  

Distbuilder currently provides three high-level "process classes",
each more powerful (and complex) then the prior:
 
- [PyToBinPackageProcess](#pytobinpackageprocess)
- [PyToBinInstallerProcess](#pytobininstallerprocess)
- [RobustInstallerProcess](#robustinstallerprocess)

## PyToBinPackageProcess

This "simple" process class converts a program written in Python
scripts into a stand-alone executable binary.  It additionally
has built-in options for employing code obfuscation, for testing the 
resulting product, for "resource bundling", and for packaging into 
an archive file.
 
The process uses a [ConfigFactory](#configfactory) to automatically 
produce the config objects it requires, but allows a client to modify
those objects before they are implemented by defining a derived class 
and overriding certain functions as needed for this purpose.       

Constructor:

    PyToBinPackageProcess( configFactory,                  
	   name="Python to Binary Package Process",
	   isZipped=False )
                                 
Attributes & default values:

    configFactory          = <required>                              
    name                   = "Python to Binary Package Process"
	isZipped               = False	                
	isPyInstDupDataPatched = None
	isTestingObfuscation   = False
	isTestingExe           = False
	exeTestArgs            = []        
	isElevatedTest         = False      
        
    # Results 
    binDir  = None
    binPath = None
        
"Virtual" configuration functions to optionally override:  
(Note the order shown is that in which these functions are invoked)

    onInitialize()    
	onOpyConfig( cfg )                    
    onPyInstConfig( cfg )
    onMakeSpec( spec )
    onFinalize()

Use:

Simply invoke the `run()` function to execute the process. 

Examples:
	
[Hello World Example](Examples.md#hello-world-example)        

#### configFactory                                        

The required [ConfigFactory](#configfactory) attribute contains
many of the details used to drive this process.

#### name                   

Used simply for logging or custom implementations where it
may be useful to distinguish between multiple processes. 

#### isZipped               	                

Setting this to `True` bundles the results into a zip file.

#### isPyInstDupDataPatched 

If this is set to `None` (the default) or `True`, the results are the same.
You must set this to `False` explicitly to disable this built-in feature. 

When enabled, this patches a known bug in PyInstaller when it is on Windows. 
PyInstaller analysis can build a set of data file names
which contain "duplicates" due to the Windows 
file system case insensitivity.  This patch eliminates
such duplicates, thus preventing runtime errors in the 
binary produced.

You will nearly always when to leave this alone.  It is only
made optional because it is not a "standard" part of a PyInstaller  
process.
        
#### isTestingObfuscation   

This option is intended to be toggled manually during a testing and 
debugging phase of the build process definition.

This is only applicable when when code obfuscation is enabled.
When this is also enabled, this will interrupt the normal build process.

Upon creating an obfuscated version of the scripts, the revised entry point
module will be launched, thereby allowing you to confirm the program
is still functional in this new state.  Upon exiting the program,
the build process is also exited.  

This option LEAVES the obfuscated code in place for further testing and 
inspection.  This is in opposition to the normal
deletion of such after having embedded the code in the binary.   	

#### isTestingExe, exeTestArgs, isElevatedTest               

The `isTestingExe` attribute is similar in nature to is `isTestingObfuscation`.  
This launches the resulting binary after building it.  
Unlike `isTestingObfuscation`, this does NOT exit build process.  Upon exiting 
the program, any remaining steps in the build process are continued.   	  
The `exeTestArgs` and `isElevatedTest` attributes are additionally provided
to vet the result in an automated fashion in the event such options are useful.

#### onInitialize()    

This function is intended for adding any custom setup procedures
to be run before any other operations are begun.  That involve
shuffling around files, downloading resources, etc.  

Notably, this is the ideal place to gather and install Python dependencies. 
By installing all of your dependencies here, you make your project and build 
script far more portable across machines / environments. Refer to the 
documentation on these useful utility functions for this purpose:
   
- [installLibrary](LowLevel.md#installlibrary)
- [installLibraries](LowLevel.md#installlibraries)
	
#### onOpyConfig( cfg )                  

When code obfuscation is enabled, an [OpyConfig](ConfigClasses.md#opyconfig) object
will be generated and passed here.  You may then configure the details of such.       

#### onPyInstConfig( cfg )

Prior to running PyInstaller, a [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig) object
will be generated and passed here.  You may then configure the details of such.       

#### onMakeSpec( spec )

This class employs the more advanced option of running PyInstaller against
a "spec" file.  After initial processing of the [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig)
object, a [PyInstSpec](ConfigClasses.md#pyinstspec) object (with a corresponding temp
spec file) will be generated.  The `onMakeSpec` function allows a final manipulation
of that prior to running the PyInstaller process.    

#### onFinalize()

After every other task has been performed by this process class, this function
will be called.  This allows you to perform any custom clean up tasks, or other
manipulations of the results.

These notable object attributes will now be set for you to potentially use at this 
stage: `binDir`, `binPath`.         
        
## PyToBinInstallerProcess

A PyToBinInstallerProcess process *contains* a 
[PyToBinPackageProcess](#pytobinpackageprocess)
within it, and thus provides the full functionality of that to begin with.
In addition, however, it rolls the product of that lower level process within
a full fledged installer.  Like the other process classes, this uses a
[ConfigFactory](#configfactory) to automatically produce the config 
objects it requires, but allows a client to modify those objects before 
they are implemented by defining a derived class and overriding certain 
functions as needed for this purpose.       

This process is basically a simplified version of a
[RobustInstallerProcess](#robustinstallerprocess).  Use *that* class instead
if you need to build an installable distribution which does NOT involve
a Python to binary conversion process (e.g. packaging binaries
produced in another language with some other compiler), or if
you have more comprehensive needs such as producing multiple Python derived 
binaries or installable "packages" bundled together. 
  
Constructor:

    PyToBinInstallerProcess( configFactory, 
	     name="Python To Binary Installer Process",
	     isDesktopTarget=False, isHomeDirTarget=False )
                                 
Attributes & default values:
                                               
    configFactory = <required>  
    
    name = "Python To Binary Installer Process"
            
    isDesktopTarget = False
    isHomeDirTarget = False
            
    isTestingInstall     = False
    isAutoTestInstall    = False
    isVerboseTestInstall = True
        
"Virtual" configuration functions to override:  
(Note the order shown is that in which these functions are invoked)

	onInitialize()   
	onPyPackageProcess( prc )
    onOpyConfig( cfg )                    
    onPyInstConfig( cfg )
    onMakeSpec( spec )
    onQtIfwConfig( cfg )              
	onFinalize()
    
Use:

Simply invoke the `run()` function to execute the process. 

Examples:
	
[Hello World Tk Example](Examples.md#hello-world-tk-example)        
[Hello Silent Example](Examples.md#hello-silent-example)
                                               
#### configFactory, name 

See the documentation for these attributes as provided for the 
[PyToBinPackageProcess](#pytobinpackageprocess) class.  
    
#### isDesktopTarget, isHomeDirTarget 

Set either of these to `True`, to have the final installer that is produced 
moved to either of these respective locations in the end.  
If neither are `True`, the installer is simply left in the build directory.
If both are `True`, priority is given to `isDesktopTarget`.  
         
#### isTestingInstall, isAutoTestInstall, isVerboseTestInstall  

Upon building the installer (and moving it to a target directory if so
directed), the installer will be launched when either `isTestingInstall`,
or `isAutoTestInstall` is enabled. The `isVerboseTestInstall` option controls
the level of debugging output logged to the console during the installation.

The `isTestingInstall` simply launches the installer. In contrast, `isAutoTestInstall`
runs it in "auto pilot" mode (i.e. performs the installation as well).  Note that an 
"elevated privileges" option was NOT provided as such is to built into all silent 
installers (i.e. they auto elevate themselves), and "loud"/gui installers have their 
own internal controls for this. 

#### onInitialize(), onFinalize()   

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#pytobinpackageprocess) class.  

#### onOpyConfig( cfg ), onPyInstConfig( cfg ), onMakeSpec( spec ), 

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#pytobinpackageprocess) class.  

#### onPyPackageProcess( prc )

As stated in the overview, this class generates and employs its own 
[PyToBinPackageProcess](#pytobinpackageprocess) object. Upon doing so, it
passes that object through this function, where you can manipulate it as
needed for your implementation.  

#### onQtIfwConfig( cfg )              

After building a "package" from the Python source, QtIFW is employed to build
an installer for deploying that content.  Those tasks are driven by a master   
[QtIfwConfig](ConfigClasses.md#qtifwconfig) object.  A collection of related
sub components are nested inside of that (e.g. [QtIfwPackage](ConfigClasses.md#qtifwpackage)).

Before running the process to build the installer, that master config object
is passed through this function, where you can manipulate it as needed for your 
implementation.  
	
## RobustInstallerProcess

A RobustInstallerProcess is the most advanced and intricate of these processes.  
It exposes details of the build process that [PyToBinInstallerProcess](#pytobininstallerprocess) 
insulates from the user.  In addition to providing access to more nitty gritty details,
this class is primarily intended for use when you need to produce multiple binaries
from Python scripts and/or multiple installable "packages" bundled together.
This class is also useful for building an installer which does NOT involve
a Python to binary conversion process (e.g. packaging binaries
produced in another language, using some other compiler).

What is most notable about this process class, compared to others, is that
uses a "Master Config Factory", plus a dictionary containing multiple 
"Py Package Config Factories".  Further, it can additionally use a list of 
independent (non-Python related) "Qt IFW Packages".
  
The "Master Config Factory" is used to define the top level "wrapper" installer.
For each element in the "Py Package Config Factories" dictionary, a "package" is created
from a Python script.  Those entries are sub components within the whole, built using
separate instances of a [PyToBinPackageProcess](#pytobinpackageprocess).

If a value in the "Py Package Config Factories" dictionary is set to `None`, one will 
be generated for it, by *cloning* the master config.  That cloned ConfigFactory will 
then be passed to the overridable function `onConfigFactory( key, factory )`.  Within
that, your implementation may modify the object, but it will not have to start from
"scratch" because whatever common attributes might be shared between the master and 
the sub components will already be defined (hence the purpose of the cloning option).  

The other notable attribute of this class is the list of "Qt IFW Packages".
Items in this list may be dynamic [QtIfwPackage](ConfigClasses.md#qtifwpackage) objects,
or be simple strings defining relative paths to QtIFW packages which are defined
as external resources, in the traditional (hard coded, content containing) IFW manner.
Using this class attribute, you may build installers with packages containing 
other programs that are not Python related, or may be comprised of optional 
resources that the end user might wish to selectively install.  
    
Constructor:

    RobustInstallerProcess( masterConfigFactory, 
      name="Multi-Package Python to Binary Installer Process",
      pyPkgConfigFactoryDict={}, ifwPackages=[],                                     
      isDesktopTarget=False, isHomeDirTarget=False  )
                                 
Attributes & default values:
                                               
    configFactory = <required>  
    
    name = "Multi-Package Python to Binary Installer Process"
    
    pyToBinPkgProcesses = []        
    ifwPackages         = []    
            
    isDesktopTarget = False
    isHomeDirTarget = False
            
    isTestingInstall     = False
    isAutoTestInstall    = False
    isVerboseTestInstall = True
        
"Virtual" configuration functions to override:  
(Note the order shown is that in which these functions are invoked)

	onInitialize()   
    onConfigFactory( key, factory )
    onPyPackageProcess( key, prc )
    onPyPackageInitialize( key )
    onOpyConfig( key, cfg )                    
    onPyInstConfig( key, cfg )
    onMakeSpec( key, spec )   
    onPyPackageFinalize( key )
    onPyPackagesBuilt( pkgs )
    onQtIfwConfig( cfg )
    onPackagesStaged( cfg, pkgs )            
    onFinalize()
               
Use:

Simply invoke the `run()` function to execute the process. 

Examples:
	
[Hello Packages Example](Examples.md#hello-packages-example)        
[Hello Merge Example](Examples.md#hello-merge-example)

#### configFactory, name 

See the documentation for these attributes as provided for the 
[PyToBinPackageProcess](#pytobinpackageprocess) class.  

Note `configFactory` == "Master Config Factory" for this class. 
See the class overview for an explanation of what that means.

#### pyToBinPkgProcesses, ifwPackages          

While technically exposed for access by an implementation,
**it is not generally advised that you directly modify these attributes**.

The `pyToBinPkgProcesses` list will be generated for you.  If you 
need to manipulate a given sub process definition before its use, 
it is recommended that you do so via `onPyPackageProcess( key, prc )`.
If you wish to manipulate the packages after they have all been 
built, that should normally be done via `onPyPackagesBuilt( pkgs )`.   

The `ifwPackages` attribute should normally be defined prior to
creating this class, and simply be passed to its constructor. 
See the class overview for an explanation of how this attribute
is used.
        
#### isDesktopTarget, isHomeDirTarget 

See the documentation for these attributes as provided for the 
[PyToBinInstallerProcess](#pytobininstallerprocess) class.  

#### isTestingInstall, isAutoTestInstall, isVerboseTestInstall  

See the documentation for these attributes as provided for the 
[PyToBinInstallerProcess](#pytobininstallerprocess) class.  

#### onInitialize(), onFinalize()   

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#pytobinpackageprocess) class.  

Note these are to be used in relation to the *master* process.  

#### onPyPackageInitialize( key ), onPyPackageFinalize( key )

These functions are analogous to `onInitialize()` and `onFinalize()`.
They are, however, invoked around each [PyToBinPackageProcess](#pytobinpackageprocess) 
this *master* process runs.

A `key` argument is provided to supply a means by which to identify the package being built
upon on the given invocation of these functions.  The keys passed here align with
those defined in the `pyPkgConfigFactoryDict` argument passed to the constructor.

#### onConfigFactory( key, factory )

This function receives a clone of the "Master Config Factory" for each entry in
the "Py Package Config Factories" dictionary that has a value set to `None`.

A `key` argument is provided to supply a means by which to identify the Factory 
being configured upon on the given invocation of this function.  The keys passed 
here align with those defined in the `pyPkgConfigFactoryDict` argument passed to 
the constructor.

See the class overview for an explanation of how this is used.

#### onOpyConfig( key, cfg ), onPyInstConfig( key, cfg ), onMakeSpec( key, spec ) 

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#pytobinpackageprocess) class.  

In addition to the standard object passed through these functions, a `key`
is provided to supply a means by which to identify the package being built
upon on the given invocation of these functions.  The keys passed here align with
those defined in the `pyPkgConfigFactoryDict` argument passed to the constructor.

#### onPyPackageProcess( key, prc )

See the documentation for this function as provided for the 
[PyToBinInstallerProcess](#pytobininstallerprocess) class.  

In addition to the standard object passed through this function, a `key`
is provided to supply a means by which to identify the package being built
upon on the given invocation of this function.  The keys passed here align with 
those defined in the `pyPkgConfigFactoryDict` argument passed to the constructor.

#### onPyPackagesBuilt( pkgs )

After all of the Python packages have been built (if applicable), this function is invoked
prior to running the installer building process.  The `pkgs` parameter this 
receives is the list of corresponding [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
objects, including those which have been generated from Python source.

#### onPackagesStaged( cfg, pkgs )

After ALL of the packages have been fully staged, just prior to running the QtIFW process,
this function is invoked. The `cfg` parameter this receives is the master   
[QtIfwConfig](ConfigClasses.md#qtifwconfig) object used to drive the installer build.   
The `pkgs` parameter this receives is the list of  
[QtIfwPackage](ConfigClasses.md#qtifwpackage) objects. Note, you could also access those
via `cfg.packages`.  The `pkgs` parameter is provided for convenience . 

This function maybe used to manipulate the packages before the final send off
to QtIFW.  See [QtIfwPackage list manipulation](LowLevel.md#qtifwpackage-list-manipulation) 
for details, utility functions, and ideas surrounding how this can be applied. 
