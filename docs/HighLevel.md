# High Level Classes  
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## ConfigFactory  

It is typical for a build script to start by creating
a high-level *ConfigFactory* object and setting its attributes.

The major functions within the distbuilder library rely
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
    		
    setupName        = "setup"
    ifwDefDirPath    = None
    ifwPackages      = None
    
    ifwPkgId         = None
    ifwPkgName       = None
    ifwPkgNamePrefix = "com" 
    pkgSrcDirPath    = None
       
    ifwScriptName    = "installscript.qs"
    ifwScript        = None
    ifwScriptPath    = None   

Object creation functions:
     
    pyInstallerConfig()    
    opyConfig()
    qtIfwConfig( packages=None )
    qtIfwPackage( pyInstConfig=None, isTempSrc=False )
    qtIfwConfigXml()
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

This process class converts a program written as standard Python
scripts int to a stand-alone executable binary.  It additionally
has built-ing options for employing obfustication, for testing the 
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

"Virtual" configuration functions to optionally override:  

    onInitialize()    
	onOpyConfig( cfg )                    
    onPyInstConfig( cfg )
    onMakeSpec( spec )
    onFinalize()

Use:

Simply invoke the `run()` function to execute the process. 
        
### PyToBinInstallerProcess

This process contains a [PyToBinPackageProcess](#PyToBinPackageProcess)
within it, and thus provides the full functionality of that.    
In addition, however, this also rolls the product of that process within
a fullfleded installer.  Like the other process classes, this uses a
[ConfigFactory](#configfactory) to automatically produce the config 
objects it requires, but allows a client to modify those objects before 
they are implemented by defining a derived class and overriding certain 
functions as needed for this purpose.       

This process is basically a simplflied version of a
[RobustInstallerProcess](#RobustInstallerProcess).  Use that instead
if you need to build an installable distrubtion which does NOT involve
a Python to binary conversion process (e.g. packaging binaries
produced in another langauge with some other compiler), or if
you need to produce multiple binaries or installable "packages" bundled 
together. 
  
Constructor:

    PyToBinInstallerProcess( configFactory, 
	     name="Python To Binary Installer Process",
	     isDesktopTarget=False,
	     isHomeDirTarget=False )
                                 
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

### RobustInstallerProcess

This process is intended for use you need to produce multiple binaries 
from Python scripts and/or multiple installable "packages" bundled together.  
It is also usueful building an installable distrubtion which does NOT involve
a Python to binary conversion process (e.g. packaging binaries
produced in another langauge with some other compiler).
  
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
    onOpyConfig( key, cfg )                    
    onPyInstConfig( key, cfg )
    onMakeSpec( key, spec )   
    onPyToBinPkgsBuilt( pkgs )
    onQtIfwConfig( cfg )            
    onFinalize()
    
Use:

Simply invoke the `run()` function to execute the process. 

