# High Level Classes  
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## ConfigFactory  

It is typical for a build script to start by creating
a high-level *ConfigFactory* object and set its attributes.

The major functions within the library rely
upon a collection of "configuration" objects which supply
extended sets of parameters to drive various processes.  Many of these 
classes have overlapping attributes, and scripts employing 
a series of these tend to have a great deal of redundant
parameter assignment.  With this in mind, the ConfigFactory class 
was created.

See [Configuration Classes](ConfigClasses.md#configuration-classes) for more 
information on the types of objects created by this factory class.  

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
    iconFilePath  = None
    distResources = []       
	specFilePath  = None

	isSilentSetup    = False    		
    setupName        = "setup"
    ifwDefDirPath    = None
    ifwPackages      = None
    
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
    
    pkgSrcDirPath    = None

Object creation functions:
     
    pyInstallerConfig()    
    opyConfig()
    qtIfwConfig( packages=None )
    qtIfwConfigXml()
    qtIfwControlScript()
    qtIfwPackage( pyInstConfig=None, isTempSrc=False )
    qtIfwPackageXml()    
    qtIfwPackageScript( pyInstConfig=None )

Cloning:

    newFactory = ConfigFactory.copy( instance )
    
#### cfgId                                              

Useful to distinguish between multiple ConfigFactory objects, as
are often employed by a [RobustInstallerProcess](#RobustInstallerProcess). 

#### productName, description

The name and description for the product on the whole, or a sub component
withit (based upon the context of the factory object is used).  Such
will appear as "brandings" upon a executable and/or as labels/details within 
installer menus.  

#### companyTradeName, companyLegalName       

Akin to `productName` and `description` attributes.  

Note the `companyTradeName` will be used in standard labels, directory names, shortcuts, etc.
as produced by the process employing the ConfigFactory.  In contrast, `companyLegalName`
will appear within copy rights, EULAs, and the like where this alternate value is 
called for.  

#### isObfuscating, opyBundleLibs, opyPatches

#### binaryName, version, isGui           

#### sourceDir, entryPointPy

#### specFilePath, iconFilePath

#### distResources        

#### setupName, isSilentSetup

#### ifwDefDirPath, ifwPackages

#### ifwCntrlScript, ifwCntrlScriptText, ifwCntrlScriptPath, ifwCntrlScriptName

#### ifwPkgId, ifwPkgName, ifwPkgNamePrefix         
   
#### ifwPkgScript, ifwPkgScriptText, ifwPkgScriptPath, ifwPkgScriptName

#### pkgSrcDirPath

    
## Process Classes

Many build scripts will follow the same essential
logic flow, to produce analogous distributions. 
As such, using high-level "process classes" can prevent 
having multiple implementation scripts be virtual 
duplicates of one another, each containing a fair volume 
of code which employs the "low level" functions in the
library.  

Distbuilder currently provides three high-level "process classes",
each more powerful (and complex) then the prior:
 
- [PyToBinPackageProcess](#PyToBinPackageProcess)
- [PyToBinInstallerProcess](#PyToBinInstallerProcess)
- [RobustInstallerProcess](#RobustInstallerProcess)

### PyToBinPackageProcess

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
	
[Hello World Example](QuickStart.md#hello-world-example)        

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
will be generated and passed here.  You may then config the details of such.       

#### onPyInstConfig( cfg )

Prior to running PyInstaller, a [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig) object
will be generated and passed here.  You may then config the details of such.       

#### onMakeSpec( spec )

This class employs the more advanced option of running PyInstaller against
a "spec" file.  After initial processing of the [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig)
object, a [PyInstSpec](ConfigClasses.md#pyinstspec) object (with a corresponding temp
spec file) will be generated.  The `onMakeSpec` function allows a final manipulation
of that prior to running the PyInstaller process.    

#### onFinalize()

After every other task has been performed by this process class, this function
will be called.  This allows you to perform any custom clean up tasks, or other
maniplations of the results.

These notable object attributes will now be set for you to potentially use at this 
stage: `binDir`, `binPath`.         
        
### PyToBinInstallerProcess

A PyToBinInstallerProcess process *contains* a 
[PyToBinPackageProcess](#PyToBinPackageProcess)
within it, and thus provides the full functionality of that to begin with.    
In addition, however, it rolls the product of that lower level process within
a full fledged installer.  Like the other process classes, this uses a
[ConfigFactory](#configfactory) to automatically produce the config 
objects it requires, but allows a client to modify those objects before 
they are implemented by defining a derived class and overriding certain 
functions as needed for this purpose.       

This process is basically a simplified version of a
[RobustInstallerProcess](#RobustInstallerProcess).  Use *that* class instead
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
	
[Hello World Tk Example](QuickStart.md#hello-world-tk-example)        
[Hello Silent Example](QuickStart.md#hello-silent-example)
                                               
#### configFactory, name 

See the documentation for these attributes as provided for the 
[PyToBinPackageProcess](#PyToBinPackageProcess) class.  
    
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

The `isTestingInstall` simply launches the installer. in contrast, `isAutoTestInstall`
runs it in "auto pilot" mode.  Note that there is not an "elevated privileges" option
as such is to built-in requirement for silent installers (i.e. the auto elevate 
themselves), and "loud"/gui installers have their own internal controls for this. 

#### onInitialize(), onFinalize()   

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#PyToBinPackageProcess) class.  

#### onOpyConfig( cfg ), onPyInstConfig( cfg ), onMakeSpec( spec ), 

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#PyToBinPackageProcess) class.  

#### onPyPackageProcess( prc )

As stated in the overview, this class generates and employs its own 
[PyToBinPackageProcess](#PyToBinPackageProcess) object. Upon doing so, it
passes that object through this function, where you can manipulate it as
needed for your implementation.  

#### onQtIfwConfig( cfg )              

After building a "package" from the Python source, QtIFW is employed to build
installer for deploying that content.  Those tasks are driven by a master   
[QtIfwConfig](ConfigClasses.md#qtifwconfig) object.  A collection of related
sub components are nested inside of that (e.g. [QtIfwPackage](ConfigClasses.md#qtifwpackage)).

Before running the process to build the installer, that master config object
is passed through this function, where you can manipulate it as needed for your 
implementation.  
	
### RobustInstallerProcess

A RobustInstallerProcess is the most advanced and intricate of these processes.  
It exposes details of the build process that [PyToBinInstallerProcess](#PyToBinInstallerProcess) 
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
separate instances of a [PyToBinPackageProcess](#PyToBinPackageProcess).

If a value in the "Py Package Config Factories" dictionary is set to `None`, one will 
be generated for it, by *cloning* the master config.  That cloned ConfigFactory will 
then be passed to the overridable function `onConfigFactory( key, factory )`.  Within
that, your implementation my modify the object, but it will not have to start from
"scratch" because whatever common attributes might be shared between the master and 
the sub components will already be defined.  

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
    onFinalize()
               
Use:

Simply invoke the `run()` function to execute the process. 

Examples:
	
[Hello Packages Example](QuickStart.md#hello-packages-example)        
[Hello Merge Example](QuickStart.md#hello-merge-example)

#### configFactory, name 

See the documentation for these attributes as provided for the 
[PyToBinPackageProcess](#PyToBinPackageProcess) class.  

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
[PyToBinInstallerProcess](#PyToBinInstallerProcess) class.  

#### isTestingInstall, isAutoTestInstall, isVerboseTestInstall  

See the documentation for these attributes as provided for the 
[PyToBinInstallerProcess](#PyToBinInstallerProcess) class.  

#### onInitialize(), onFinalize()   

See the documentation for these functions as provided for the 
[PyToBinPackageProcess](#PyToBinPackageProcess) class.  

Note these are to be used in relation to the *master* process.  

#### onPyPackageInitialize( key ), onPyPackageFinalize( key )

These functions are anlaougs to `onInitialize()` and `onFinalize()`.
They are, however, invoked around each [PyToBinPackageProcess](#PyToBinPackageProcess) 
this *master* process runs.

A `key` argument is provided to supply a means by which to identifiy the package being built
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
[PyToBinPackageProcess](#PyToBinPackageProcess) class.  

In addition to the standard object passed through these functions, a `key`
is provided to supply a means by which to identify the package being built
upon on the given invocation of these functions.  The keys passed here align with
those defined in the `pyPkgConfigFactoryDict` argument passed to the constructor.

#### onPyPackageProcess( key, prc )

See the documentation for this function as provided for the 
[PyToBinInstallerProcess](#PyToBinInstallerProcess) class.  

In addition to the standard object passed through this function, a `key`
is provided to supply a means by which to identify the package being built
upon on the given invocation of this function.  The keys passed here align with 
those defined in the `pyPkgConfigFactoryDict` argument passed to the constructor.

#### onPyPackagesBuilt( pkgs )

After ALL of the Python packages have been built, this function is invoked
prior to running the installer building process.  The `pkgs` parameter this 
recieves is the list of corresponding [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
objects which have been generated.

This function maybe used to manipulate the packages before the final send off
to QtIFW.  See [QtIfwPackage list manipulation](QuickStart.md#qtifwpackage-list-manipulation) 
for details, utility functions, and ideas surrounding how this can be applied. 
