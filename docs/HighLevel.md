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
   
    self.__pkgPyInstConfig = None
    
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
    
## Process Classes

Many build scripts will follow the same essential
logic flow, to produce analogous distributions. 
As such, using high-level "process classes" can prevent 
having multiple implementation scripts be virtual 
duplicates of one another, each containing a fair volume 
of code.  

### PyToBinPackageProcess

This process class converts a program written with Python
scripts into a stand-alone executable binary.  It additionally
has built-in options for employing obfuscation, for testing the 
resulting product, and for primitive "bundling" into an archive.  
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
   
[installLibrary](LowLevel.md#installlibrary)
[installLibraries](LowLevel.md#installlibraries)
	
#### onOpyConfig( cfg )                  

When code obfuscation is enabled, an [OpyConfig](ConfigClasses.md#opyconfig) object
will be generated and passed here.  You may then config the details of such.       

#### onPyInstConfig( cfg )

Prior to running PyInstaller, a [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig) object
will be generated and passed here.  You may then config the details of such.       

#### onMakeSpec( spec )

This class employs the more advanced option of running PyInstaller against
a "spec" file.  After initial processing of the [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig)
object, a [PyInstSpec](ConfigClasses.md#pyinstspec) object (with a corrspdong temp
spec file) will be generated.  The `onMakeSpec` function allows a final manipulation
of that prior to running the PyInstaller process.    

#### onFinalize()

After every other task has been performed by this process class, this function
will be called.  This allows you to perform any custom clean up tasks, or other
maniplations of the results.

These notable object attributes will now be set for you to potentially use at this 
stage: `binDir`, `binPath`.         
        
### PyToBinInstallerProcess

A PyToBinInstallerProcess process contains a 
[PyToBinPackageProcess](#PyToBinPackageProcess)
within it, and thus provides the full functionality of that to begin with.    
In addition, however, rolls the product of that lower level process within
a full fledged installer.  Like the other process classes, this uses a
[ConfigFactory](#configfactory) to automatically produce the config 
objects it requires, but allows a client to modify those objects before 
they are implemented by defining a derived class and overriding certain 
functions as needed for this purpose.       

This process is basically a simplified version of a
[RobustInstallerProcess](#RobustInstallerProcess).  Use that class instead
if you need to build an installable distribution which does NOT involve
a Python to binary conversion process (e.g. packaging binaries
produced in another language with some other compiler), or if
you have more comprehensive needs such as producing multiple Python dervived 
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
            
    isTestingInstall = False
    isVerboseInstall = False
	isElevatedTest   = False       
        
"Virtual" configuration functions to override:  

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

### RobustInstallerProcess

A RobustInstallerProcess is the most advanced and intricate of these processes.  
It exposes details of the build process that [PyToBinInstallerProcess](#PyToBinInstallerProcess) 
insultates from the user.  In addition to providing access to more nitty gritty details,   
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
For each element in "Py Package Config Factories" dictionary, a "package" is created
from a Python script.  Those entries are sub components within the whole, built using
separate instances of a [PyToBinInstallerProcess](#PyToBinInstallerProcess).

If a value in the "Py Package Config Factories" dictionary is set to `None`, one will 
be generated for it, by *cloning* the master config.  That cloned Config Factory will 
then be passed to the overridable function `onConfigFactory( key, factory )`.  Within
that, your implementation my modify the object, but it will not have to start from
"scratch" because whatever common attributes might be shared between the master and 
the sub components will already be defined.  

The other notable attribute of this class is the a list of "Qt IFW Packages".
Item in this list may be dynamic [QtIfwPackage](ConfigClasses.md#qtifwpackage) objects,
or be simple strings defining relative paths to QtIFW packages that are defined
as external resources, in the traditional (hard coded, contented containing) IFW manner.
Using this class attribute, you may build installers with packages containing 
other programs that are not Python related, or may be comprised perhaps of optional 
resources that the end user might selectively install.  
    
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
            
    isTestingInstall = False
    isVerboseInstall = False
	isElevatedTest   = False       
        
"Virtual" configuration functions to override:  

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

