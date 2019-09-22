# Configuration Classes
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

The following classes are used to create objects which
are employed as arguments to various functions within the library.
Many of these can be generated for you using the 
[Configuration Factory](HighLevel.md#configfactory).

## PyInstallerConfig    

Objects of this type define *optional* details for building 
binaries from .py scripts using the PyInstaller utility 
invoked via the [buildExecutable](LowLevel.md#buildexecutable) function 
(which maybe employed by higher level  
[Process Classes](HighLevel.md#process-classes) under the hood).

Note that if a [PyInstSpec](#pyinstspec) attribute is provided for one of 
these objects, the  build settings contained within that will **override** 
any which conflict with those specified via the attributes set directly 
on the PyInstallerConfig object.  PyInstSpec objects may be created by supplying 
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

## PyInstSpec

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

Objects of this type provide the highest level definition of 
a QtIFW installer configuration to use for building 
an installer via the 
[buildInstaller](LowLevel.md#buildinstaller) function
(which maybe employed by higher level  
[Process Classes](HighLevel.md#process-classes) under the hood).

Constructor: 

    QtIfwConfig( installerDefDirPath=None,
                 packages=None,
                 configXml=None,
                 controlScript=None, 
                 setupExeName="setup" ) 
                                                    
Attributes & default values:                                               

	installerDefDirPath = None

	packages            = None <list of QtIfwPackages OR directory paths>
	configXml           = None	
	controlScript       = None
	        
	setupExeName        = "setup"
	
	<Qt paths (attempt to use environmental variables if not defined)>
	qtIfwDirPath = None
	
	<other IFW command line options>
	isDebugMode    = True
	otherQtIfwArgs = ""

## QtIfwConfigXml 

Objects of this type define the contents of a QtIFW 
`config.xml` which will be dynamically generated 
when invoking the [buildInstaller](LowLevel.md#buildinstaller) function. 

The `config.xml` file represents the highest level definition 
of a QtIFW installer, containing information such as the product 
name and version. Most of the attributes in this 
class correspond directly to the name of the tags added to the xml file.  
Attributes set to `None` values will not be written, otherwise they will be.

Constructor:                

    QtIfwConfigXml( name, version, publisher,
                  	iconFilePath=None, 
                  	controlScriptName=None,
                  	primaryContentExe=None,
                  	isGuiPrimaryContentExe=True,
                  	companyTradeName=None ) 

Attributes:    

    primaryContentExe (used indirectly w/ isGui)
    iconFilePath  (used indirectly)
    companyTradeName (used indirectly)
    
    Name                     
    Version                  
    Publisher                
    InstallerApplicationIcon  (icon base name, i.e. omit extension)
    ControlScript  
    Title                    
    TargetDir                
    StartMenuDir             
    RunProgram               
    RunProgramDescription
        
    runProgramArgList  (used indirectly)
    
    otherElements (open ended dictionary of key/value pairs to inject)
    
Functions:

    setDefaultVersion()
    setDefaultTitle()    
    setDefaultPaths()
    
    addCustomTags( root ) 

    path()   
    dirPath() 
       
## QtIfwControlScript

QtIFW installers may have a "Control Script" and/or a collection of "Package Scripts".
The "Control Script" is intended to dictate how the installer *interface*  behaves, and
other high level logic pertaining to the installer itself. In contrast, "Package Scripts"
are intended for applying custom logic to manipulate a target environment when installing 
a given package.  See [QtIfwPackageScript](#qtifwpackagescript) for more info. 

The QtIfwControlScript class provides an abstraction layer for QtIfw script
generation.  QtIfw scripts are written in [Qt Script](https://doc.qt.io/qt-5/qtscript-index.html) 
(which is conceptually a spin off from JavaScript), with additional custom objects and 
methods for this context. Using this abstracion, you can achieve a great many custom 
behaviors without having to learn much about the language yourself. Refer to the details on 
[Installer Scripting](LowLevel.md#installer-scripting) to learn more about 
the low level helpers provided by the library for this purpose. 

For maximum flexibility, rather than using the dynamic methods, you may directly define 
the entire script via a raw string, by setting the `script` attribute.  Or, you may 
specify an external file as the source instead via `script_path`. In addition, you may 
always delegate scripts to a traditional QtIFW definition by using a higher level 
config [QtIfwConfig](#qtifwconfig) to specify such.

The way this class works, in summary, is that you may provide an optional script 
as a raw string, or a path to script you wish to load directly.  If specificied, 
those resources act as a *base*, from which you may continue to add on to.

Along with being able to add your own custom functions to use as "helpers"
a QtIFW Control script is driven by the framework which calls functions of
specific names, if they exist, in order to apply custom coding during a given
event.  A QtIfwControlScript object has a pair of attributes related to each such 
event in the framework.  One is a boolean, dictating whether to auto generate this 
event handler using a set of fixed, builtin logic provided by distbuilder to add a 
fair amount of additional features to your installers "for free".  The other attribute 
in ecah pair is the body of the function (which is normally auto generated).   
  
When the `write()` function is invoked, the actual script file to be embedded 
in the installer is generated from the attributes.  Prior to calling that, you
may switch off the various auto generate options, and supply your own function
definition from scratch.

If you wish to use the bulk of the "free" / standard add on logic, but then customize 
that the program flow should be to call `_generate()` first, which will define the 
function bodies using the auto generate options. Once that is done, you may disable 
select auto generates, and then directly add on to, or manipulate the event handling 
function bodies.  

A large number of abstract, static "helper" functions have been provided which you may
use to build your logic.  Otherwise, you may certainly just add QScript snippets
directly in the raw.       

Constructor:                

	QtIfwControlScript( fileName="installscript.qs",                  
                  		script=None, scriptPath=None ) :

Attributes & default values:                                               
    
	controllerGlobals = None
    isAutoGlobals = True
        
    controllerConstructorBody = None
    isAutoControllerConstructor = True
                                                            
    introductionPageCallbackBody = None
    isAutoIntroductionPageCallback = True

    targetDirectoryPageCallbackBody = None
    isAutoTargetDirectoryPageCallback = True

    componentSelectionPageCallbackBody = None
    isAutoComponentSelectionPageCallback = True

    licenseAgreementPageCallbackBody = None
    isAutoLicenseAgreementPageCallback = True

    startMenuDirectoryPageCallbackBody = None
    isAutoStartMenuDirectoryPageCallback = True

    readyForInstallationPageCallbackBody = None
    isAutoReadyForInstallationPageCallback = True

    performInstallationPageCallbackBody = None
    isAutoPerformInstallationPageCallback = True
        
    finishedPageCallbackBody = None
    isAutoFinishedPageCallback = True        

Object Methods:
    
    write()
    debug()
    	 
	path()
	dirPath()   

	registerAutoPilotSlot( signalName, slotName, slotBody )

    _generate()
    
## QtIfwPackage

Objects of this type define the packages with an installer.
A [QtIfwConfig](#qtifwconfig) contains a list of these.
Notably, these package objects define the source content to be 
included in the installer via `srcDirPath` or
simply `srcExePath` attributes. They also contain
[QtIfwPackageXml](#qtifwpackagexml) and 
[QtIfwPackageScript](#qtifwpackagescript) objects,
for extended configuration details.

Constructor:  

    QtIfwPackage( pkgId=None, name=None, 
                  srcDirPath=None, srcExePath=None,    
                  isTempSrc=False,
                  pkgXml=None, pkgScript=None ) 

Attributes:    

	<internal id / type>
	pkgId           = None       
	pkgType	        = None
	
	<QtIFW definition>
	name            = None
	pkgXml          = None
	pkgScript       = None
	        
	<content>        
	srcDirPath      = None
	srcExePath      = None
	distResources   = None
	isTempSrc       = False
	                     
	<extended content detail>
	exeName        = None   
	isGui          = False
	exeCompiler    = None
	qmlScrDirPath  = None  <for QML projects only>   
 
Functions:      

    contentDirPath() 
 
## QtIfwPackageXml

Objects of this type define the a QtIFW `package.xml` 
file which will be dynamically generated 
when invoking the buildInstaller function. This file
defines a component within the installer which maybe
selected by the user to install. Most of the attributes 
in these objects correspond directly to the name of tags 
added to the xml. Attributes set to `None` values
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

Functions:      

	path()
    dirPath() 
    
## QtIfwPackageScript

QtIFW installers may have a "Control Script" and/or a collection of "Package Scripts".
The "Control Script" is intended to dictate how the installer *interface*  behaves, and
other high level logic pertaining to the installer itself. In contrast, "Package Scripts"
are intended for applying custom logic to manipulate a target environment when installing 
a given package. See [QtIfwControlScript](#qtifwcontrolscript) for more info. 

Objects of the type `QtIfwPackageScript` are used to dynamically generate
a script used by a QtIFW package.  Refer to the details on 
[Installer Scripting](LowLevel.md#installer-scripting) to learn more about 
the low level helpers provided by the library for this purpose. 

For maximum flexibility, rather than using the dynamic methods, you may directly define 
the entire script via a raw string, by setting the `script` attribute.  Or, you may 
specify an external file as the source instead via `script_path`. In addition, you may 
always delegate scripts to a traditional QtIFW definition by using a higher level 
config [QtIfwConfig](#qtifwconfig) to specify such.

This class works in an analagous manner to [QtIfwControlScript](#qtifwcontrolscript).
Please refer to the that documentation for an explanation of how use these script
objects in general. 

Note that [QtIfwShortcut](#qtifwpackageshortcut) objects
are used for the `shortcuts` attribute of this class.

Constructor:       

	QtIfwPackageScript( pkgName, 
					    shortcuts=[], 
						fileName="installscript.qs", 
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
[QtIfwPackageScript](#qtifwpackagescript) objects,
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

TODO: Expand on this considerably... 

The `source` attribute is the the "heart" of this class.
It can take *many* different forms.  Including library
names registered at PyPi, local paths, and urls. 

Other Notable attributes include `incDpndncsSwitch`,
`destPath` and `asSource`.  These allow you to 
skip dependency gathering if desired, install to 
a specific path such as a temp build directory,
and to request raw .py scripts be placed there.

Note that remote raw pip packages will require an 
alternate [vcs url](LowLevel.md#vcsurl) be supplied to a "development" 
repository in place of the simple package name as the `source` attribute.  
See [editable installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)  
          
## OpyConfig
    
Objects of this type define obfuscation details for 
use by the Opy Library.
**Refer to the documentation for that library for details.**

This library **EXTENDS** the natural OpyConfig, however,
adding the attributes / features described below.
See [Obfuscation Features](LowLevel.md#obfuscation-features) for a 
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

See [Obfuscation Features](LowLevel.md#obfuscation-features) for a 
description of how objects of this type are used.
    
Constructor:

    OpyPatch( relPath, patches, parentDir=OBFUS_DIR_PATH )
        
Attributes:                    

    relPath 
    path    
    patches 
    
Functions:

    obfuscatePath( obfuscatedFileDict )        
    apply()

## LibToBundle 

See [Obfuscation Features](LowLevel.md#obfuscation-features) for a 
description of how objects of this type are used.

Constructor:

    LibToBundle( name, localDirPath=None, pipConfig=None, isObfuscated=False )
    
Attributes:                    

    name         
    localDirPath 
    pipConfig    
    isObfuscated 

## QtCppConfig:

Used for Qt C++ integration.

Constructor:

    QtCppConfig( qtBinDirPath, exeCompiler,  
                 qmlScrDirPath=None  )
    
Attributes:                    

	qtBinDirPath             
    exeCompiler    
    qmlScrDirPath     
    
    