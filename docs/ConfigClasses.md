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
                  	isPrimaryExeGui=True,
                  	primaryExeWrapper=None,
                  	companyTradeName=None ) 

Attributes:    

    primaryContentExe (used indirectly w/ isGui)    
    iconFilePath  (used indirectly)
    companyTradeName (used indirectly)
    
    primaryExeWrapper
    
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

    setPrimaryContentExe( ifwPackage )
    setDefaultVersion()
    setDefaultTitle()    
    setDefaultPaths()
    
    addCustomTags( root ) 
               
    write()
    
    debug()
    toPrettyXml()
            
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

    QtIfwPackage( pkgId=None, pkgType=None, name=None, 
    			  subDirName=None,
                  srcDirPath=None, srcExePath=None,    
                  resBasePath=None, isTempSrc=False,
                  pkgXml=None, pkgScript=None ) 

Attributes:    

	<internal id / type>
	pkgId           = None       
	pkgType	        = None
	
	<QtIFW definition>
	name            = None
	pkgXml          = None
	pkgScript       = None
	        
	<source content>        
	srcDirPath    = None <package ENTIRE source directory>
	srcExePath    = None
	resBasePath   = None
	distResources = None	
	isTempSrc     = False
	                     
	<destination content>
	subDirName  = None
	exeName     = None   
	exeWrapper  = None
	
	<other configuration details>
	isGui       = False
	qtCppConfig = None
 
Functions:      

	dirPath()
	contentTopDirPath()
    contentDirPath() 

Static Functions:   
 
    topDirPath()
 
## QtIfwPackageXml

Objects of this type define the a QtIFW `package.xml` 
file which will be dynamically generated 
when invoking the [buildInstaller](LowLevel.md#buildinstaller) function. This file
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

    addCustomTags( root ) 
               
    write()
    
    debug()
    toPrettyXml()
            
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
    
    shortcuts = []
    
    packageGlobals = None
    isAutoGlobals = True
            
    componentConstructorBody = None
    isAutoComponentConstructor = True
    
    componentCreateOperationsBody = None
    isAutoComponentCreateOperations = True        
    
    <Linux Only>
    isAskPassProgRequired = False
                                                   
## QtIfwShortcut

These shortcut objects are use by
[QtIfwPackageScript](#qtifwpackagescript) objects,
to create shortcuts on the installation target 
environments.

Constructor:       

	QtIfwShortcut( productName=QT_IFW_PRODUCT_NAME, 
                   command=None, args=[], 
                   exeDir=QT_IFW_TARGET_DIR, exeName=None, 
                   exeVersion="0.0.0.0",
                   isGui=True, pngIconResPath=None )
                  
Attributes & default values:
      
	productName       = "@ProductName@" <QtIfw Built-in Variable>
	command           = None	
    exeDir            = "@TargetDir@" <QtIfw Built-in Variable>
    exeName           = None
    args           	  = None  

    isGui             = True <used in Mac / Linux>       
    
    windowStyle       = None <used in Windows>        

    exeVersion        = "0.0.0.0" <used in Linux>        
    pngIconResPath    = None <used in Linux>   
    
    isAppShortcut     = True
    isDesktopShortcut = False

## QtIfwExeWrapper

This class provides a means to "wrap" your exe inside of additional external layers.
Such layers may take a series of forms, and be nested inside of one another.
The benefit of this is to impose a specific environment and or set of parameters 
onto the exe without having to modify it internally.  These options work cross
platform, and could be slapped over the top of a program written in any language.
You may, in fact, even wrap third-party (freeware) programs in these layers!

The easiest way to use this class is to set some of its basic attributes. For
example, `workingDir`, `isElevated`, `envVars`, or `args`.  The approach taken by the 
library is to use the "lightest touch" possible.  If you simply changed the 
default values for those example attributes, their shortcuts (on applicable plafforms) 
and the way QtIFW would run the program post installation, would be altered to provided 
the functionality.  

The most flexible attribute you may impose is a `wrapperScript` layer.
This is an [ExecutableScript](LowLevel.md#executablescript) object, used to produce
a persistent "companion" to your binary.  Executing the script rather then the 
binary itself would be the intended means for launching the program.  If this attribute 
is set, "shortcuts" which would normally point a user to the binary, will instead run this 
wrapper layer.  On Windows, this (normally) equates to having a batch file companion. 
On Linux, as shell script companion is created (with an explict `.sh` extension). On macOS, 
a shell script with no extension is embedded into the .app file when producing a gui application, 
else the same design used on Linux is employed for non-gui programs.  

The application of a wrapper script of this nature is not entirely uncommon - especailly on Linux. 
As an example, when deploying Qt C++ applications on Linux which are 
dynamically linked, the **standard procedure** (per Qt documentation) is to use this 
(slightly modifed) shell script to load the required libraries: 
 
    #!/bin/sh
	appname=`basename "$0" | sed s,\.sh$,,`
	dirname=`dirname "$0"`
	tmp="${dirname#?}"
	if [ "${dirname%$tmp}" != "/" ]; then
	dirname="$PWD/$dirname"
	fi
	LD_LIBRARY_PATH="$dirname"
	export LD_LIBRARY_PATH
	"$dirname/$appname" "$@"

Other ways for using a wrapper like this include automatically detecting dependencies, and
then downloading and installing them as needed.  Or, doing something simliar for updates
to your software. Using a wrapper, you could launch a "companion application" along side the 
primary target. You could start a background service, or open help documentation... The
possiblities are really boundless.  

Constructor:

    QtIfwExeWrapper( exeName, isGui=False, 
                     wrapperScript=None, 
                     exeDir=QT_IFW_TARGET_DIR, workingDir=None, 
                     args=None, envVars=None, isElevated=False )    

Attributes & default values:
        
        exeName = <required>        
        isGui   = False
        
        wrapperScript = None

        exeDir        = "@TargetDir@" <QtIfw Built-in Variable>
        workingDir    = None  <None=don't impose here, use QT_IFW_TARGET_DIR via other means>

        args          = None      
        envVars       = None         
        isElevated    = False

        _winPsStartArgs = None  <Windows only>

		<Auto defined via refresh>
        _runProgram       
        _runProgArgs      
        _shortcutCmd      
        _shortcutArgs     
        _shortcutWinStyle 
                            
Functions:
      
		refresh()
             
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
