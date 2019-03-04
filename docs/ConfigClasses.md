# Configuration Classes
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

The following classes are used to create objects which
are employed as arguments to various functions within the library.
Many of these can be generated for you using the 
[Configuration Factory](HighLevel.md#configfactory).

## PyInstallerConfig    

Objects of this type define *optional* details for building 
binaries from .py scripts using the PyInstaller utility 
invoked via the buildExecutable function. 

Note that if a [PyInstSpec](#pyinstspec) attribute is provided for one of 
these objects, the  build settings contained within such will **override** 
any that conflict with those supplied via the other attributes set directly 
in the object.  PyInstSpec objects may be created by supplying 
a traditional (perhaps legacy) spec file definition, or you may wish to 
generate one with distbuilder via the makePyInstSpec() function.  
In either case, you may also opt to dynamically manipulate the spec via 
the implementation of that class. 

Constructor: 

    PyInstallerConfig()

Attributes & default values:        

    pyInstallerPath = <python scripts directory>/pyinstaller
      
    name            = None   
    entryPointPy    = None

    pyInstSpec      = None
	
    isGui           = False
    iconFilePath    = None
      
    versionInfo     = None
    versionFilePath = None
           
    distDirPath     = None    
    isOneFile       = True     (note this differs from PyInstaller default)
      
    importPaths     = []
    hiddenImports   = []
    dataFilePaths   = []
    binaryFilePaths = []
      
    isAutoElevated  = False        
    otherPyInstArgs = ""  (open ended argument string)    

    (Not directly fed into the utility. Employed by buildExecutable function.)
    _pngIconResPath = None
    distResources   = []
    distDirs        = [] 
	isSpecFileRemoved = False

## PyInstSpec:

Objects of this type are used for PyInstaller spec file
parsing, and programmatic manipulation.  This class provides
an easy mechanism for applying known PyInstaller patches, 
as well as convenient mechanisms for applying custom 
revisions for similar purposes.  

Constructor: 

    PyInstSpec( filePath=None, pyInstConfig=None, content=None ) 

Attributes & default values:
        
    filePath     = None
    pyInstConfig = None 
    content 	 = None

Static Method:
    
    cfgToPath( pyInstConfig )

Object Methods:

	path()
	read()
	write()
    debug()
    
    injectDuplicateDataPatch()
    
    _toLines()
    _fromLines( lines )
	_injectLine( injection, lineNo )
	_parseAssigments() 

## WindowsExeVersionInfo

Objects of this type define metadata branded into Windows 
executables. This is the object type intended for 
PyInstallerConfig.versionInfo attributes. 

Constructor: 

    WindowsExeVersionInfo()

Attributes & default values:        

	major = 0
    minor = 0
    micro = 0
    build = 0
    companyName = ""
    productName = ""
    description = ""
    exeName     = ""

## QtIfwConfig 

Objects of this type define the details for building 
an installer using the QtIFW utility invoked via the
buildInstaller function. 

Constructor: 

    QtIfwConfig( installerDefDirPath=None,
                 packages=None,
                 configXml=None, 
                 setupExeName="setup" ) 
                     
Attributes & default values:                                               

	packages            = None <list of QtIfwPackages OR directory paths>
	configXml           = None        
	setupExeName        = "setup"
	
	<Qt paths (attempt to use environmental variables if not defined)>
	qtIfwDirPath = None
	qtBinDirPath = None          
	
	<other IFW command line options>
	isDebugMode    = True
	otherQtIfwArgs = ""

## QtIfwConfigXml 

Objects of this type define the contents of a QtIFW 
config.xml which will be dynamically generated 
when invoking the buildInstaller function. This file 
represents the highest level definition of a QtIFW 
installer, containing information such as the product 
name and version. Most of the attributes in these 
objects correspond directly to the name of tags 
added to config.xml.  Attributes with None values
will not be written, otherwise they will be.

Constructor:                

    QtIfwConfigXml( name, exeName, version, publisher,
                    iconFilePath=None, isGui=True,
                    companyTradeName=None ) 

Attributes:    

    exeName (used indirectly w/ isGui)
    iconFilePath  (used indirectly)
    companyTradeName (used indirectly)
    Name                     
    Version                  
    Publisher                
    InstallerApplicationIcon  (icon base name, i.e. omit extension)
    Title                    
    TargetDir                
    StartMenuDir             
    RunProgram               
    RunProgramDescription    
    runProgramArgList  (used indirectly)
    otherElements (open end dictionary of key/value pairs to inject)

Convenience functions:

    setDefaultVersion()
    setDefaultTitle()    
    setDefaultPaths()

## QtIfwPackage

Objects of this type define the packages with an installer.
A [QtIfwConfig](#qtifwconfig) contains a list of these.
Notably, these package objects define the source content to be 
included in the installer via `srcDirPath` or
simply `srcExePath` attributes. They also contain
[QtIfwPackageXml](#qtifwpackageXml) and 
[QtIfwPackageScript](#qtifwpackageScript) objects,
for extended configuration details.

Constructor:  

    QtIfwPackage( pkgId=None, name=None, 
                  srcDirPath=None, srcExePath=None,    
                  isTempSrc=False,
                  pkgXml=None, pkgScript=None ) 

Attributes:    

	<internal id>
	pkgId           = None       
	
	<definition>
	name            = None
	pkgXml          = None
	pkgScript       = None
	        
	<content>        
	srcDirPath      = None
	srcExePath      = None
	othContentPaths = None
	isTempSrc       = False
	                     
	<extended content detail>
	exeName        = None   
	isGui          = False
	isQtCppExe     = False
	isMingwExe     = False
	qmlScrDirPath  = None  <for QML projects only>   
 
## QtIfwPackageXml

Objects of this type define the a QtIFW package.xml 
file which will be dynamically generated 
when invoking the buildInstaller function. This file
defines a component within the installer which maybe
selected by the user to install. Most of the attributes 
in these objects correspond directly to the name of tags 
added to package.xml. Attributes with None values
will not be written, otherwise they will be.

Constructor:       

	QtIfwPackageXml( pkgName, displayName, description, version, 
					 scriptName=None, isDefault=True )
                  
Attributes & default values:      

	pkgName = <required>
               
	DisplayName   = <required>
	Description   = <required>
	Version       = <required>            
	Script        = None 
	Default       = True
	ReleaseDate   = date.today()

## QtIfwPackageScript

Objects of this type are used to dynamically generate
a script used by a QtIFW package. Scripts are able
to perform the most sophisticated customizations
for an installer. 

For maximum flexibility, you may directly define the 
entire script, by setting the "script" attribute.  Or,
you specify a source to an external file instead.  Also,
you may always delegate scripts to a traditional QtIFW 
definition.

This class currently has very limited functionality,
but in the future more options will be provided for
automating the generation common script directives.  

Note that [QtIfwShortcut](#qtifwpackageshortcut) objects
are used for the `shortcuts` attribute of this class.

Constructor:       

	QtIfwPackageScript( pkgName, 
					    shortcuts=[], 
						fileName="installscript.qs", 
                        exeName=None, isGui=True, 
                        script=None, scriptPath=None )
                  
Attributes & default values:      

	pkgName  = <required>
    fileName = "installscript.qs"
    
    script = None <or loaded via scriptPath>
    
    shortcuts = shortcuts
    
    componentConstructorBody = None
    isAutoComponentConstructor = True
    
    componentCreateOperationsBody = None
    isAutoComponentCreateOperations = True        
                                                   
## QtIfwShortcut

These shortcut objects are use by
[QtIfwPackageScript](#qtifwpackageScript) objects,
to create shortcuts on the installation target 
environments.

Constructor:       

	QtIfwShortcut( productName="@ProductName@", 
                   exeName=None, exeVersion="0.0.0.0",        
                   pngIconResPath=None, isGui=True )
                  
Attributes & default values:
      
	productName       = "@ProductName@" <QtIfw Built-in Variable>
    exeName           = None  
    isGui             = True <used in Mac / Linux>
    exeVersion        = "0.0.0.0"        
    pngIconResPath    = None <used in Linux>        
    isAppShortcut     = True
    isDesktopShortcut = False

## PipConfig

Objects of this type define the details for downloading
and/or installing Python libraries via the pip utility.
These objects are used directly by the installLibrary 
function as well indirectly via the obfuscation functions
and support classes.
    
Constructor:

    PipConfig( source = None
             , version = None
             , verEquality = "==" 
             , destPath = None
             , asSource = False
             , incDependencies = True        
             , isForced= False
             , isCacheUsed = True                
             , isUpgrade = False
             , otherPipArgs = "" ) 

Attributes:                        

    pipCmdBase = "[PYTHON BINARY PATH]" -m pip
    source          
    version         
    verEquality     
    destPath        
    asSource        
    incDependencies       
    isForced 
    isCacheUsed                  
    isUpgrade      
    otherPipArgs  (open ended argument string)      
          
## OpyConfig
    
Objects of this type define obfuscation details for 
use by the Opy Library.
**Refer to the documentation for that library for details.**

This library **EXTENDS** the natural OpyConfig, however,
adding the attributes / features described below.
See [Obfuscation Features](#obfuscation-features) for a 
description of how objects of this type are used.

Constructor:        

    OpyConfig( name, entryPointPy=None,
               bundleLibs=None, sourceDir=None, patches=None )

Attributes:                

	name
	entryPointPy
    bundleLibs (list of LibToBundle objects)
    sourceDir (dynamically defined when ommited)
    patches (list of OpyPatch objects)

## OpyPatch

See [Obfuscation Features](#obfuscation-features) for a 
description of how objects of this type are used.
    
Constructor:

    OpyPatch( relPath, patches, parentDir=OBFUS_DIR_PATH )
        
Attributes:                    

    relPath 
    path    
    patches 
    
Convenience functions:

    obfuscatePath( obfuscatedFileDict )        
    apply()

## LibToBundle 

See [Obfuscation Features](#obfuscation-features) for a 
description of how objects of this type are used.

Constructor:

    LibToBundle( name, localDirPath=None, pipConfig=None, isObfuscated=False )
    
Attributes:                    

    name         
    localDirPath 
    pipConfig    
    isObfuscated 
