# Process Classes
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)
    
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
       isZipped=False, isDesktopTarget=False, isHomeDirTarget=False )
                                 
Attributes & default values:

    configFactory          = <required>                              
    name                   = "Python to Binary Package Process"

    isZipped               = False
    isDesktopTarget        = False
    isHomeDirTarget        = False
    
    isWarningSuppression   = True          
    isUnBufferedStdIo      = False          
    isPyInstDupDataPatched = None <auto>
    
    isObfuscationTest      = False
    isExeTest              = False
    isElevatedTest         = False      
    exeTestArgs            = []        
        
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

### isWarningSuppression  

By default, this is enabled by the library (thus differing from the standard in Python
or PyInstaller). Such will prevent Python **warning** messages from being output to the 
terminal (they will be "ignored" instead).

Note this neither suppresses nor exposes *exception* messages / stderr output.  That is
an entirely distinct matter.

Note that the inclusion of warning suppression which may be present in your Python source 
code will not actually be respected by PyInstaller binaries naturally!  This
mechanism (driven via a .spec file manipulation under the hood) is the means to control such.  

For more on Python warnings in general, refer to: 
https://docs.python.org/3/library/warnings.html

### isUnBufferedStdIo

By default, this is disabled.  Python stdin/out/err streams are naturally buffered, as that
is more efficient and thus preferable for most use cases.  Switching to "unbuffered" mode, 
will, however, produce more rapid responsiveness on these streams.  Such may be desirable    
if your program will communicate with other programs via these streams, or if you want to 
view "real-time debugging" messages, or have other uses for fast i/o on in a shell/terminal
context perhaps.   

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
        
#### isObfuscationTest   

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

#### isExeTest, exeTestArgs, isElevatedTest               

The `isExeTest` attribute is similar in nature to is `isObfuscationTest`.  
This launches the resulting binary after building it.  
Unlike `isObfuscationTest`, this does NOT exit the build process.  Upon exiting 
the program you are testing, any remaining steps in the build process are continued.         
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
                
## IExpressPackageProcess

**WINDOWS ONLY**

This "simple" process class converts a program written in a native Windows 
script (currently supporting Batch, PowerShell, VBScript, and JScript), into a 
stand-alone executable binary.  It additionally has built-in options for
testing the resulting product, for "resource bundling", and for packaging into 
an archive file.
 
The process uses a [ConfigFactory](#configfactory) to automatically 
produce the config objects it requires, but allows a client to modify
those objects before they are implemented by defining a derived class 
and overriding certain functions as needed for this purpose.       

Constructor:

    IExpressPackageProcess( configFactory,                  
       name="Windows Script to Binary Package Process",
       isZipped=False, isDesktopTarget=False, isHomeDirTarget=False )
                                 
Attributes & default values:

    configFactory          = <required>                              
    name                   = "Windows Script to Binary Package Process"

    isZipped               = False
    isDesktopTarget        = False
    isHomeDirTarget        = False
    
    isExeTest              = False
    isElevatedTest         = False      
    exeTestArgs            = []        
        
    # Results 
    binDir  = None
    binPath = None
        
"Virtual" configuration functions to optionally override:  
(Note the order shown is that in which these functions are invoked)

    onInitialize()    
    onIExpressConfig( cfg )
    onFinalize()

Use:

Simply invoke the `run()` function to execute the process. 
        
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
            
    isInstallTest            = False
    isAutoInstallTest        = False
    isVerboseInstallTest     = True
    isScriptDebugInstallTest = False
        
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
         
#### isInstallTest, isAutoInstallTest, isVerboseInstallTest  

Upon building the installer (and moving it to a target directory if so
directed), the installer will be launched when either `isInstallTest`,
or `isAutoInstallTest` is enabled. The `isVerboseInstallTest` option controls
the level of debugging output logged to the console during the installation.

The `isInstallTest` simply launches the installer. In contrast, `isAutoInstallTest`
runs it in "auto pilot" mode (i.e. performs the installation as well).  Note that an 
"elevated privileges" option was NOT provided as such is to built into all silent 
installers (i.e. they auto elevate themselves), and "loud"/gui installers have their 
own internal controls for this. 

#### isScriptDebugInstallTest

This flag may be useful in the event you are embedding scripts into an installer
via a [QtIfwExternalOp](ConfigClasses.md#qtifwexternalop) using an  
[ExecutableScript](LowLevel.md#executablescript).  When enabled, the dynamically
generated script (with installer driven value substitutions where applicable) 
will be left behind in a temp folder after running the installer,
rather than auto purging that upon completion.  If you have effectively built the 
script via Python "helpers" using a function e.g. 
`QtIfwExternalOp.CreateStartupEntry(...)`, this may be especially helpful to see
what was actually produced and executed, through a series of abstraction layers
that ultimately produce platform specific scripts, nested under the hood inside
an installer.   

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

## IExpressInstallerProcess

A IExpressInstallerProcess process *contains* an 
[IExpressPackageProcess](#iexpresspackageprocess)
within it, and thus provides the full functionality of that to begin with.
In addition, however, it rolls the product of that lower level process within
a full fledged installer.  Like the other process classes, this uses a
[ConfigFactory](#configfactory) to automatically produce the config 
objects it requires, but allows a client to modify those objects before 
they are implemented by defining a derived class and overriding certain 
functions as needed for this purpose.       

This process is basically a simplified version of a
[RobustInstallerProcess](#robustinstallerprocess).  Use *that* class instead
if you need to build an installable distribution if
you have more comprehensive needs such as producing multiple 
binaries or installable "packages" bundled together. 

Constructor:

    IExpressInstallerProcess( configFactory, 
         name="Windows Script to Binary Installer Process",
         isDesktopTarget=False, isHomeDirTarget=False )
                                 
Attributes & default values:
                                               
    configFactory = <required>  
    
    name = "Windows Script to Binary Installer Process"
            
    isDesktopTarget = False
    isHomeDirTarget = False
            
    isInstallTest            = False
    isAutoInstallTest        = False
    isVerboseInstallTest     = True
    isScriptDebugInstallTest = False
        
"Virtual" configuration functions to override:  
(Note the order shown is that in which these functions are invoked)

    onInitialize()   
    onIExpressPackageProcess( prc )
    onIExpressConfig( cfg )
    onQtIfwConfig( cfg )              
    onFinalize()
    
Use:

Simply invoke the `run()` function to execute the process. 
      
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
      pyPkgConfigFactoryDict={},
      iExpressPkgConfigFactoryDict={},  
      ifwPackages=[],                                     
      isDesktopTarget=False, isHomeDirTarget=False )
                                 
Attributes & default values:
                                               
    configFactory = <required>  
    
    name = "Multi-Package Python to Binary Installer Process"
    
    pyToBinPkgProcesses  = []        
    iexpressPkgProcesses = []
    ifwPackages          = []    
            
    isDesktopTarget = False
    isHomeDirTarget = False
            
    isInstallTest            = False
    isAutoInstallTest        = False
    isVerboseInstallTest     = True
    isScriptDebugInstallTest = False
        
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
    
    onIExpressPackageProcess( key, prc )
    onIExpressPackageInitialize( key )
    onIExpressConfig( key, cfg )
    onIExpressPackageFinalize( key )
    onIExpressPackagesBuilt( pkgs )
    
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

#### pyToBinPkgProcesses, iexpressPkgProcesses, ifwPackages          

While technically exposed for access by an implementation,
**it is not generally advised that you directly modify these attributes**.

The `pyToBinPkgProcesses` list will be generated for you.  If you 
need to manipulate a given sub process definition before its use, 
it is recommended that you do so via `onPyPackageProcess( key, prc )`.
If you wish to manipulate the packages after they have all been 
built, that should normally be done via `onPyPackagesBuilt( pkgs )`.   

`iexpressPkgProcesses` ...

The `ifwPackages` attribute should normally be defined prior to
creating this class, and simply be passed to its constructor. 
See the class overview for an explanation of how this attribute
is used.
        
#### isDesktopTarget, isHomeDirTarget 

See the documentation for these attributes as provided for the 
[PyToBinInstallerProcess](#pytobininstallerprocess) class.  

#### isInstallTest, isAutoInstallTest, isVerboseInstallTest  

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
