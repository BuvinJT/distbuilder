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

## PyInstHook

Objects of this type are used for PyInstaller "hook" script
creation, and programmatic manipulation. 
Such hooks are executed during a PyInstaller analyis process 
when an import is encountered with a matching hook name. The purpose
of a hook is to help PyInstaller find and collect resources
it would otherwise not know to include in the bundle.  
  
Hooks are commonly installed by third party libraries for use across your 
Python environment whenever you employ PyInstaller.  It is 
also possible to use custom hooks during a given a build process via 
the PyInstaller option `--additional-hooks-dir` (though that parameter does **not** 
*override* a hook which is registered for the system on the whole...)   

If you are working in a context in which you can manipulate the build environment
freely, the use of hooks is arguably a better means by which to gather resources 
for a distribition rather than by adding them through  
[PyInstallerConfig](#pyinstallerconfig) attributes
`hiddenImports`, `dataFilePaths`, `binaryFilePaths`, etc.    

Use cases for this class include: **adding hooks** to patch a build process,
replacing **bad hooks** installed on your system, or to simply revisw them 
for some additional custom need.  

For more on hooks, see:
[Understanding PyInstaller Hooks](https://pyinstaller.readthedocs.io/en/stable/hooks.html) 

Constructor: 

    PyInstHook( name, script=None,
                isContribHook=True, isRunTimeHook=False ) 

Attributes & default values:
        
    name          = *required     
    script        = None

	isContribHook = True
	isRunTimeHook = False

    hooksDirPath  = None 

Object Methods:
    
    fileName()

    read()
    write()
    remove()

    debug()

    toLines()
    fromLines( lines )
    injectLine( injection, lineNo )
    
Details:

The `name` attribute should simply specify the name of import which invokes the `script`. 
The `name` should **not** contain the *literal* "hook-" *file name* prefix, or a 
.py *file extension*.     

**isContribHook**: Only respected for PyInstaller v4 or later, when it became available,
and the new standard practice for hook distribution.

**hooksDirPath** may be override, as needed.  If left as the default `None`, 
the path will be automatically resolved. 

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
    content      = None
    
    warningBehavior   = None 
    	<options: PyInstSpec.WARN_IGNORE, PyInstSpec.WARN_ONCE, PyInstSpec.WARN_ERROR>    
    isUnBufferedStdIo = False
    isModInitDebug    = False        
    
	isInjected   = False

Static Method:
    
    cfgToPath( pyInstConfig )

Object Methods:

    path()

    read()
    write()

    debug()

    toLines()
    fromLines( lines )
    injectLine( injection, lineNo )
    
    injectDuplicateDataPatch()
    
    _parseAssigments() 

## CodeSignConfig

This class defines the details used for code signing executables.

TODO: Make Cross Platform 

Constructor: 

    CodeSignConfig( keyFilePath=None, keyPassword=None )

Attributes & default values: 

	keyFilePath = None
    keyPassword = None
 
    signToolPath = None <None==auto resolved> 
       
    fileDigest         = CodeSignConfig.DEFAULT_DIGEST       
    timeStampDigest    = CodeSignConfig.DEFAULT_DIGEST 
    timeStampServerUrl = CodeSignConfig.DEFAULT_TIMESTAMP_SERVER
    otherSignToolArgs  = ""
        
    isDebugMode = True

Class Constants: 

    DEFAULT_DIGEST           = "sha256"
    DEFAULT_TIMESTAMP_SERVER = "http://timestamp.digicert.com"

**signToolPath**: Only applicable on WINDOWS.  If `None`, this defaults to the 
path the this library will auto install the tool as needed.  This attribute may 
also be set indirectly by running the script where an environmental variable 
call `SIGNTOOL_PATH` (defined the in constant `SIGNTOOL_PATH_ENV_VAR`) has been 
defined.  
    
## SelfSignedCertConfig

This class defines the details used for generating self-signed code signing 
certificates and keys.

TODO: Make Cross Platform 

Constructor: 

    CodeSignConfig( companyTradeName, destDirPath=None )

Attributes & default values: 

    commonName  = companyTradeName
    endDate     = SelfSignedCertConfig.DEFAULT_END_DATE

    destDirPath = destDirPath or THIS_DIR        
    
    caCertPath     = <auto, based on destDirPath> 
	privateKeyPath = <auto, based on destDirPath>
    
    makeCertPath = None <None, auto resolved >

    _maxCertChildren  = SelfSignedCertConfig.NO_MAX_CHILDREN       
    _enhancedKeyUsage = SelfSignedCertConfig.LIFETIME_SIGNING_EKU                
    
    otherArgs         = ""
    isDebugMode = True

Object Methods:
	
	_forceMakeCertMethod()
        
Class Constants: 

    DEFAULT_END_DATE     = '12/31/2050'
    NO_MAX_CHILDREN      = 0
    LIFETIME_SIGNING_EKU = '1.3.6.1.5.5.7.3.3,1.3.6.1.4.1.311.10.3.13'

**makeCertPath**: Only applicable on WINDOWS.  Normally used on legacy versions 
of Windows (v8.0 an earlier), where new standard means for creating such files - i.e. the PowerShell function `New-SelfSignedCertificate` is not available.  If 
`None`, this defaults to the path where this library will auto 
install the tool as needed.  This attribute may also be set indirectly by running 
the script where an environmental variable call `MAKECERT_PATH` (defined the in 
constant `MAKECERT_PATH_ENV_VAR`) has been defined.  

## Pvk2PfxConfig

Used in legacy Windows mechanisms for creating code signing certificates.
Specified defines the details for converting `.pvk` files (old style private keys) generated by the now defunct `makecert` utility, into `.pfx` files.

Constructor: 

    Pvk2PfxConfig( caCertPath, privateKeyPath, 
                   keyPassword=None, pfxFilePath=None )

Attributes & default values: 

    caCertPath     = <required>        
    privateKeyPath = <required>
    keyPassword    = None  
    keyFilePath    = <result - pfxFilePath or auto based on privateKeyPath>
    
    pvk2PfxPath = None <None, auto resolved> 
       
    otherArgs  = ""
    isDebugMode = True

**pvk2PfxPath**:  If `None`, this defaults to the 
path the this library will auto install the tool as needed.  This attribute may 
also be set indirectly by running the script where an environmental variable 
call `PVK2PFX_PATH` (defined the in constant `PVK2PFX_PATH_ENV_VAR`) has been 
defined.  
    
## WindowsExeVersionInfo

Objects of this type define meta data branded into Windows 
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

Static Methods:
    
    defaultPath()
    
Object Methods:

    version( isCommaDelim=False )    
    copyright() 
    internalName() 
    
    fileName()
    write()
    debug()
    
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

Functions:
	
    addUiElements( uiElements, isOverWrite=True ) 
    addLicense( licensePath, name="End User License Agreement" )

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
                    primaryContentExe=None, isPrimaryExeGui=True,
                    primaryExeWrapper=None,
                    companyTradeName=None,
                    wizardStyle=None, 
                    logoFilePath=None, bannerFilePath=None ) 

Attributes:    

    primaryContentExe (used indirectly w/ isGui)    
    companyTradeName  (used indirectly)
    iconFilePath      (used indirectly)    
    logoFilePath      (used indirectly)
    bannerFilePath    (used indirectly) 
    
    primaryExeWrapper
    
    Name                     
    Version                  
    Publisher                
    InstallerApplicationIcon  (icon base name, i.e. omit extension)
    Title                
    TitleColor                (HTML color code, such as "#88FF33")    
    
    ControlScript  
       
    TargetDir                
    StartMenuDir             
    
    RunProgram               
    RunProgramDescription
    
    WizardStyle              
    WizardDefaultWidth           
    WizardDefaultHeight      
    Logo                     
    Banner                          
        
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
          
    exists()            
    path()   
    dirPath() 

Static Constants:

    DEFAULT_WIZARD_STYLE
	WizardStyle.AERO     <Windows Default>	
    WizardStyle.MAC      <MacOS Default>
    WizardStyle.MODERN   <Linux Default>
	WizardStyle.CLASSIC  <Simliar to MODERN>  
       
## QtIfwControlScript

QtIfw installers may have a "Control Script" and/or a collection of "Package Scripts".
The "Control Script" is intended to dictate how the installer *interface*  behaves, and
other high level logic pertaining to the installer itself. In contrast, "Package Scripts"
are intended for applying custom logic to manipulate a target environment when installing 
a given package.  See [QtIfwPackageScript](#qtifwpackagescript) for more info. 

The QtIfwControlScript class provides an abstraction layer for QtIfw script
generation.  QtIfw scripts are written in [Qt Script](https://doc.qt.io/qt-5/qtscript-index.html) 
(which is conceptually a spin off from JavaScript), with additional custom objects and 
methods for this context. Using this abstraction, you can achieve a great many custom 
behaviors without having to learn much about the language yourself. Refer to the details on 
[Installer Scripting](LowLevel.md#installer-scripting) to learn more about 
the low level helpers provided by the library for this purpose. 

For maximum flexibility, rather than using the dynamic methods, you may directly define 
the entire script via a raw string, by setting the `script` attribute.  Or, you may 
specify an external file as the source instead via `script_path`. In addition, you may 
always delegate scripts to a traditional QtIfw  definition by using a higher level 
configuration [QtIfwConfig](#qtifwconfig) to specify such.

The way this class works, in summary, is that you may provide an optional script 
as a raw string, or a path to script you wish to load directly.  If specified, 
those resources act as a *base*, from which you may continue to add on to.

A QtIfw control script is "driven" by the builtin framework. When a given "event"
occurs a "handler" function is invoked (if it has been defined).
QtIfwControlScript object has a set of attributes related to each page and such 
event/handler pair in the framework. One is a boolean, controlling the "visibility"
of the page.  Setting that to `False` skips over that wizard page entirely. 
Another boolean is provided, dictating whether to auto generate the 
event handler using a set of fixed, built-in logic provided by distbuilder to add a 
notable amount of additional features to your installers "for free".  The final attribute 
in this pattern is the body of the event handler (normally auto generated), which allows
for an atomic replacement of that code.   
  
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
use to build your logic.  Otherwise, you may certainly just add Qt Script snippets
directly in the raw.  See [Installer Scripting](LowLeveel.md#installer-scripting).       

The `virtualArgs` attribute is a dictionary, containing key/values which
allows for hard coding [Standard Installer Arguments](LowLeveel.md#standard-installer-arguments)
into the installer, which are typically passed at runtime via the command line.

Constructor:                

    QtIfwControlScript( fileName="installscript.qs",                  
                        script=None, scriptPath=None,
                        virtualArgs={} ) :

Attributes & default values:                                               
    
    isLimitedMaintenance = True
    virtualArgs = virtualArgs
    
    uiPages = []
    widgets = []
    
    controllerGlobals = None
    isAutoGlobals = True
        
    controllerConstructorBody = None
    controllerConstructorInjection = None
    isAutoControllerConstructor = True

    onPageChangeCallbackBody      = None
    onPageChangeCallbackInjection = None
    isAutoPageChangeCallBack      = True

    onFinishedClickedCallbackBody      = None
    onFinishedClickedCallbackInjection = None
    isAutoFinishedClickedCallbackBody  = True

    onPageInsertRequestCallbackBody = None
    isAutoPageInsertRequestCallBack = True

    onPageRemoveRequestCallbackBody = None
    isAutoPageRemoveRequestCallBack = True

    onPageVisibilityRequestCallbackBody = None
    isAutoPageVisibilityRequestCallBack = True
      
    onValueChangeCallbackBody      = None
    onValueChangeCallbackInjection = None
    isAutoValueChangeCallBack      = True
                                        
    isIntroductionPageVisible = True                                                                                                                                
    introductionPageCallbackBody = None
    introductionPageOnInstall = None
    introductionPageOnMaintain = None    
    isAutoIntroductionPageCallback = True

    isTargetDirectoryPageVisible = True
    targetDirectoryPageCallbackBody = None
    isAutoTargetDirectoryPageCallback = True

    isComponentSelectionPageVisible = True
    componentSelectionPageCallbackBody = None
    componentSelectionPageInjection = None
    isAutoComponentSelectionPageCallback = True

    isLicenseAgreementPageVisible = True
    licenseAgreementPageCallbackBody = None
    isAutoLicenseAgreementPageCallback = True

    isStartMenuDirectoryPageVisible = True
    startMenuDirectoryPageCallbackBody = None
    isAutoStartMenuDirectoryPageCallback = True

    isReadyForInstallationPageVisible = True
    readyForInstallationPageCallbackBody = None
    readyForInstallationPageOnInstall = None
    readyForInstallationPageOnMaintain = None            
    isAutoReadyForInstallationPageCallback = True

    isPerformInstallationPageVisible = True
    performInstallationPageCallbackBody = None
    isAutoPerformInstallationPageCallback = True
        
    isFinishedPageVisible = True        
    finishedPageCallbackBody = None
    finishedPageOnInstall = None
    finishedPageOnMaintain = None
    isAutoFinishedPageCallback = True        

    isRunProgVisible = True
    isRunProgEnabled = True
    isRunProgChecked = True
    
Object Methods:
    
    registerAsyncFunc( func ) <takes QtIfwAsyncFunc>          
    registerStandardEventHandler( signalName, slotName, slotBody )
    registerAutoPilotEventHandler( signalName, slotName, slotBody )    
    registerGuiEventHandler( signalName, slotName, slotBody )
    registerWidgetEventHandler( pageId, controlName, 
                                signalName, slotName, slotBody ) 
                                    
    _generate()
    
    write()
    debug()

    exists()            
    path()
    dirPath()   
    
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
                  pkgXml=None, pkgScript=None,
                  licenses={}, uiPages=[], widgets=[] ) 

Attributes:    

    <internal id / type>
    pkgId           = None       
    pkgType         = None
    
    <QtIFW definition>
    name            = None
    pkgXml          = None
    pkgScript       = None
    uiPages         = []
    widgets         = []
    licenses        = {} <in the form name:filePath>
    isLicenseFormatPreserved = False
            
    <source content>            
    srcDirPath    = None <package ENTIRE source directory>
    srcExePath    = None
    resBasePath   = None
    distResources = None    
    isTempSrc     = False
                         
    <destination content>
    subDirName   = None
    exeName      = None   
    exeWrapper   = None
    
    <other configuration details>
    isGui           = False
    codeSignTargets = None <list of relative paths within package> 
    qtCppConfig     = None
 
Functions:      

    dirPath()
    metaDirPath() 
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
                     scriptName=None, 
                     isDefault=True, isRequired=False, 
                     isHidden=False, isCheckable=True )
                  
Attributes & default values:      

    pkgName = <required>

	SortingPriority    = None               
    DisplayName        = <required>
    Description        = <required>
    Version            = <required>            
    Script             = None     
    ReleaseDate        = date.today()
    Default            = True    
    ForcedInstallation = False <isRequired>
    Virtual            = False <isHidden>
    Checkable          = True
    Dependencies       = None
    AutoDependOn       = None
            
    UserInterfaces = []
    Licenses       = []
            
Functions:      

    addCustomTags( root ) 
               
    write()
    
    debug()
    toPrettyXml()
          
    exists()            
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
configuration [QtIfwConfig](#qtifwconfig) to specify such.

This class works in an analogous manner to [QtIfwControlScript](#qtifwcontrolscript).
Please refer to the that documentation for an explanation of how use these script
objects in general. 

Note that for this class [QtIfwShortcut](#qtifwshortcut) objects are used for the `shortcuts` 
attribute, [QtIfwExternalOp](#qtifwexternalop) objects are used for `externalOps`,
and [QtIfwKillOp](#qtifwexternalop) objects are used for `killOps`.

Constructor:       

    QtIfwPackageScript( pkgName, pkgVersion, pkgSubDirName=None,
                        shortcuts=[], bundledScripts=[], 
                        externalOps=[], installResources=[],
                        uiPages=[], widgets=[],
                        fileName="installscript.qs", 
                        script=None, scriptPath=None )
                  
Attributes & default values:      

    pkgName       = <required>
    pkgVersion    = <required>
    pkgSubDirName = None

    fileName = "installscript.qs"    
    script   = None <or loaded via scriptPath>
    
    shortcuts        = []    
    bundledScripts   = []    
    externalOps      = []
    installResources = []
    killOps          = []
    preOpSupport     = None
    customOperations = None
    
    uiPages = []
    widgets = []
           
    packageGlobals = None
    isAutoGlobals = True
            
    componentConstructorBody = None
    isAutoComponentConstructor = True
    
    componentLoadedCallbackBody = None
    isAutoComponentLoadedCallback = True
        
    componentCreateOperationsBody = None
    isAutoComponentCreateOperations = True        
    
    componentCreateOperationsForArchiveBody = None
    isAutoComponentCreateOperationsForArchive = True       
    
    <Linux Only>
        isAskPassProgRequired = False
                                                   
Methods
                                                   
	addSimpleOperation( name, parms=[], isElevated=False, isAutoQuote=True )
                                                                                                    
**addSimpleOperation**:  Appends a QScript snippet to be appended to the `customOperations`
attribute.  The available operations are documented on https://doc.qt.io/qtinstallerframework/operations.html.  Note that these operations 
implicitly occur during installation, have implicit "undo" operations (where possible), 
and **cannot** be made to occur specifically during an install vs update vs uninstall.  
They are, however, *cross platform* and relatively painless to implement. For more 
flexibility, use [QtIfwExternalOp](#qtifwexternalop) objects. (The draw back to such is you 
will need to call upon / include utilities or add 
[ExecutableScripts](LowLevel.md#executablescript) containing platform specific code. 
                                                   
## QtIfwShortcut

These shortcut objects are use by [QtIfwPackageScript](#qtifwpackagescript) objects,
to create shortcuts on the installation target environments.

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
    args              = None  

    isGui             = True <used in Mac / Linux>       
    
    windowStyle       = None <used in Windows>        

    exeVersion        = "0.0.0.0" <used in Linux>        
    pngIconResPath    = None <used in Linux>   
    
    isAppShortcut       = True
    isDesktopShortcut   = False
    isAdjancentShortcut = False

## QtIfwExternalOp

This class is used to represent and control the invocation of shell commands, 
external utilities, and embedded [ExecutableScripts](LowLevel.md#executablescript).    
It is employed by [QtIfwPackageScript](#qtifwpackagescript) to 
add operations to the installation, and/or uninstallation,
process of the *package* to which those operations are associated.     

This simple example (for *nix based systems), may serve well to clarify how 
this class is intended to be used:  

    filePath = joinPathQtIfw( QT_IFW_HOME_DIR, "test.txt" )     
    createFileOp = QtIfwExternalOp( exePath="touch",          args=[filePath],
                                    uninstExePath="rm", uninstArgs=[filePath] )         
    pkg.pkgScript.externalOps = [ createFileOp ]

This purpose of this class should not be confused with the 
[Installer Scripting](LowLevel.md#installer-scripting) function `execute( binPath, args )`.  
While that is also a means to invoke sub processes and shell commands from QtIWF, that
is more generally used in a "Controller scripting" context for on demand, 
often conditional and/or dynamic needs.  More to the point, `QtIfwExternalOp`
objects are bound directly to packages and to install/uninstall events, where the
QtScript `execute` function can be dropped into installation scripts anywhere, 
in an unrestricted manner.   

Note the intended design by Qt for creating sophisticated, cross platform, custom 
operations is to modify to the **installer engine** itself, writing in Qt C++, and 
recompile it yourself for a specific platform. See: https://doc.qt.io/qtinstallerframework/scripting.html#registering-custom-operations
If you *really* want to do that, here's the source you'll require:
https://github.com/qtproject/installer-framework
It is the opinion of the distbuilder developers that this typically going to be an 
absurdly complicated and time consuming endeavor for most use cases.  This "external
operation" mechanism, while having draw backs is likely a good deal more practical!

Constructor:
       
    QtIfwExternalOp( 
              script=None,       exePath=None,       args=[], successRetCodes=[0],  
        uninstScript=None, uninstExePath=None, uninstArgs=[],  uninstRetCodes=[0],
        isElevated=False, workingDir=QT_IFW_TARGET_DIR, onErrorMessage=None,
        resourceScripts=[], uninstResourceScripts=[], externalRes=[] )

Attributes & default values:
                  
    script          = None
    exePath         = None
    args            = []
    successRetCodes = [0]

    uninstScript    = None
    uninstExePath   = None
    uninstArgs      = []
    uninstRetCodes  = [0]
    
    isElevated      = False 
    workingDir      = QT_IFW_TARGET_DIR
            
    onErrorMessage  = None

    resourceScripts       = []
    uninstResourceScripts = []
	externalRes      = []

Notes:

QtIfw will execute these operations synchronously.  
By default, if the return code from the sub process is not 0, this is treated
as an installation error.  To expand the options for what is viewed as a "success",
or can at least be ignored, the attributes `successRetCodes`, and `uninstRetCodes`,
allow specifying lists of codes for either the installation or uninstallation processes,
respectively.

The [QtIfwPackageScript](#qtifwpackagescript) attribute `externalOps` is a list
to be executed in order.  Note that during uninstallation, that list is processed
in **reverse order**.  It is possible (and common), to define operations as only 
for installation or only for uninstallation.  Having direct counterparts is not 
required.  When defining an `externalOps` list with "pure uninstallation" actions, 
you should especially keep the reverse order of such operations in mind.    

**resourceScripts, uninstResourceScripts**: Lists of additional [ExecutableScripts](LowLevel.md#executablescript)
to make available on the target, for this operation to draw upon.  To reference the 
script, build a path using the python constant `QT_IFW_SCRIPTS_DIR` or from directly
within another script use `@ScriptsDir@`.   

**externalRes**: A list of [QtIfwExternalResource](#qtifwexternalresource) objects.
Tools defined this list will be rolled into the installer without explicitly
updating the [QtIfwPackageScript](#qtifwpackagescript) owner of this operation
object. 

### QtIfwExternalOp Builders

#### ON_INSTALL, ON_UNINSTALL, ON_BOTH, AUTO_UNDO

**Event** constants for convenience methods.

#### opDataPath

	opDataPath( rootFileName, isNative=True,
				quotes=None, isDoubleBackslash=False )

Dynamically resolve paths to temp data files used by the operations,
or to embed in custom scripts.  

**rootFileName**: A simple ("data key") identifier (with no file extension).

**isNative**: By default, paths are returned in a native format, i.e. 
with backslashes vs forward slashes as applicable.

**quotes**: Optionally, you may provide quote strings (e.g. `"` or `'`, or some 
escaped version of them) to wrap the returned path in such.  

**isDoubleBackslash**: Optionally, use this on Windows, to escape backslashes 
doubling them up.

#### QtIfwExternalOp.RunProgram

    RunProgram( event, path, arguments=None, isAutoQuote=True,  
                isHidden=False, isSynchronous=True, isElevated=True, 
                runConditionFileName=None, isRunConditionNegated=False,
                isAutoBitContext=True )

On Windows, set `isAutoBitContext=False` if you need to execute a 64 bit
program from the installer's 32 bit context.

#### QtIfwExternalOp.CreateOpFlagFile

    CreateOpFlagFile( event, fileName, dynamicVar=None, isElevated=True )
    
**dynamicVar**: Control the creation of this file via a dynamic installer 
variable. Note that a "false" condition will be met when a boolean variable is
explicitly set to `false`, or if the variable is undefined, or it contains no 
content, or if it is set to `0`. The opposing `true` condition, required to 
create the flag file, is simply the inverse of that. By default, this argument 
is set to `None`, and therefore the file will be created without any logical 
controls.       

#### QtIfwExternalOp.WriteOpDataFile

    WriteOpDataFile( event, fileName, data, isElevated=True )

#### QtIfwExternalOp.RemoveFile

    RemoveFile( event, filePath, isElevated=True )

#### QtIfwExternalOp.RemoveDir
    
    RemoveDir( event, dirPath, isElevated=True )

#### QtIfwExternalOp.CreateStartupEntry

    CreateStartupEntry( pkg=None, exePath=None, displayName=None, 
                        isAllUsers=False )

	TODO: Add Linux & macOS implementations

#### QtIfwExternalOp.CreateWindowsAppFoundFlagFile

**WINDOWS ONLY**

    CreateWindowsAppFoundFlagFile( event, appName, fileName, 
                                   isAutoBitContext=True )
                                           
#### QtIfwExternalOp.UninstallWindowsApp

**WINDOWS ONLY**
 	
    UninstallWindowsApp( appName, arguments=None,
                         isSynchronous=True, isHidden=True, 
                         isAutoBitContext=True,
                         isSuccessOnNotFound=True )

#### QtIfwExternalOp.CreateRegistryKey
	
**WINDOWS ONLY**

    CreateRegistryKey( event, key, isAutoBitContext=True )

Set `isAutoBitContext=False` if you need to access 64 bit entries
from the installer's 32 bit context, and/or wish to be explicit in the
use of SysWow64 nodes.

#### QtIfwExternalOp.RemoveRegistryKey
	
**WINDOWS ONLY**
 
    RemoveRegistryKey( event, key, isAutoBitContext=True )        

Set `isAutoBitContext=False` if you need to access 64 bit entries
from the installer's 32 bit context, and/or wish to be explicit in the
use of SysWow64 nodes.

#### QtIfwExternalOp.CreateRegistryEntry
	
**WINDOWS ONLY**

    CreateRegistryEntry( event, 
    	key, valueName=None, value="", valueType="String",
    	isAutoBitContext=True )

Set `isAutoBitContext=False` if you need to access 64 bit entries
from the installer's 32 bit context, and/or wish to be explicit in the
use of SysWow64 nodes.

#### QtIfwExternalOp.RemoveRegistryEntry
	
**WINDOWS ONLY**
 
    RemoveRegistryEntry( event, 
    	key, valueName=None, isAutoBitContext=True )        

Set `isAutoBitContext=False` if you need to access 64 bit entries
from the installer's 32 bit context, and/or wish to be explicit in the
use of SysWow64 nodes.

#### QtIfwExternalOp.CreateExeFromScript
	
**WINDOWS ONLY**

    CreateExeFromScript( script, brandingInfo, srcIconPath,
                         targetDir=QT_IFW_TARGET_DIR )

**script**: [ExecutableScripts](LowLevel.md#executablescript)
                                 
#### QtIfwExternalOp.WrapperScript2Exe
	
**WINDOWS ONLY**

    Script2Exe( scriptPath, exePath, brandingInfo,
                iconDirPath, iconName, 
                isScriptRemoved=False, isIconDirRemoved=False )
                        
#### QtIfwExternalOp.WrapperScript2Exe
	
**WINDOWS ONLY**

    WrapperScript2Exe( scriptPath, exePath, 
                       targetPath, brandingInfo, iconName="0.ico" )

### QtIfwExternalOp Convenience Scripts

#### Self-Destructing Script Snippets

In some circumstances, e.g. when using scripts with 
[QtIfwOnFinishedDetachedExec](#qtifwonfinisheddetachedexec) or 
[QtIfwOnFinishedCheckbox](#qtifwonfinishedcheckbox), you may wish for your
scripts to "self-destruct" (i.e. delete themselves).

The following functions return strings that you may append to / weave into
your custom scripts to serve this purpose. 

##### QtIfwExternalOp.batchSelfDestructSnippet 

##### QtIfwExternalOp.powerShellSelfDestructSnippet 

##### QtIfwExternalOp.vbScriptSelfDestructSnippet 

##### QtIfwExternalOp.shellScriptSelfDestructSnippet 

##### QtIfwExternalOp.appleScriptSelfDestructSnippet 
        
#### QtIfwExternalOp.RunProgramScript

    RunProgramScript( path, arguments=None, isAutoQuote=True, 
    				  isHidden=False, isSynchronous=True,
    				  runConditionFileName=None, isRunConditionNegated=False,
    				  isAutoBitContext=True, 
    				  replacements=None )

**Windows Type**: Batch or PowerShell (determined by options employed)
**Mac/Linux Type**: ShellScript 
    
On Windows, set `isAutoBitContext=False` if you need to execute a 64 bit
program from the installer's 32 bit context.

Note: Elevation is controlled via the operation executing the script 
rather embedded within it.

#### QtIfwExternalOp.CreateOpFlagFileScript

    CreateOpFlagFile( fileName, dynamicVar=None )
    
**dynamicVar**: Control the creation of the flag file via a dynamic installer 
variable. Note that a "false" condition will be met when a boolean variable is
explicitly set to `false`, or if the variable is **undefined**, or it contains **no content**, or if it is set to `0`. The opposing `true` condition, required 
to create the flag file, is simply the inverse of that.  So notably, the flag 
can be raised by having a value in the dynamic variable, to then just simply 
"true". By default, this argument is set to `None`, and therefore the file will be created without any logical 
controls.  

Note that the flag is either raised by this function or not. This function **does 
not remove** a file that already exists.        

#### QtIfwExternalOp.WriteOpDataFileScript

    WriteOpDataFileScript( fileName, data=None )

**Windows Type**: Batch 
**Mac/Linux Type**: ShellScript 

#### QtIfwExternalOp.RemoveFileScript

	RemoveFileScript( filePath )

**Windows Type**: Batch 
**Mac/Linux Type**: ShellScript 
 
#### QtIfwExternalOp.RemoveDirScript

	RemoveDirScript( dirPath )

**Windows Type**: Batch 
**Mac/Linux Type**: ShellScript 
                
#### QtIfwExternalOp.CreateRegistryKeyScript

**WINDOWS ONLY**
 
    CreateRegistryKeyScript( key, isAutoBitContext=True, 
                             replacements=None )

**Type**: PowerShell 
                               
#### QtIfwExternalOp.RemoveRegistryKeyScript

**WINDOWS ONLY**

    RemoveRegistryKeyScript( key, isAutoBitContext=True, 
                             replacements=None ) 

**Type**: PowerShell 

#### QtIfwExternalOp.CreateRegistryEntryScript

**WINDOWS ONLY**
 
    CreateRegistryEntryScript( key, valueName=None, 
                               value="", valueType="String",
                               isAutoBitContext=True,
                               replacements=None )

**Type**: PowerShell 
                               
#### QtIfwExternalOp.RemoveRegistryEntryScript

**WINDOWS ONLY**

    RemoveRegistryEntryScript( key, valueName=None, 
                               isAutoBitContext=True, 
                               replacements=None ) 

**Type**: PowerShell 

#### QtIfwExternalOp.CreateWindowsAppFoundFlagFileScript

**WINDOWS ONLY** 
	
    CreateWindowsAppFoundFlagFileScript( appName, fileName,
                                         isAutoBitContext=True,
                                         isSelfDestruct=False )

**Type**: PowerShell 
   
#### QtIfwExternalOp.UninstallWindowsAppScript
                  
**WINDOWS ONLY**
                                                                                        
    UninstallWindowsAppScript( appName, arguments=None,
                               isSynchronous=True,
                               isHidden=True,
                               isAutoBitContext=True,
                               isSelfDestruct=False )            
                                                                                        
**Type**: PowerShell 

## QtIfwKillOp

This class is used to drive process killing operations. Such actions are frequently 
useful prior to installing or uninstalling software, especially when it comes to
instances of the target programs themselves.  
     
This class is employed by [QtIfwPackageScript](#qtifwpackagescript), and is internally
used to actually generate and inject [QtIfwExternalOp](#qtifwexternalop) objects.     

Constructor:
       
    QtIfwKillOp( processName, onInstall=True, onUninstall=True ):

Attributes & default values:
                  
    processName = <required>
    onInstall   = True
    onUninstall = True
    isElevated  = True 

Notes:

Kill operations are performed prior to any others during either on install or uninstall process.
**ALL** processes with the given `processName` will be forcefully terminated.
For convenience, instead of passing the explicit name the of process, you may instead pass a 
[QtIfwPackage](#qtifwpackage).  In which case, the name of the "primary executable" will be 
automatically extracted from that.  

## QtIfwExternalResource

This class provides as a means to include "resources" (e.g. third party utility programs),
in the installer which are not part of the product or intended for direct use 
by an end user. Such resources may then be utilized by your package script operations.
These objects are typically added to in the `externalRes` attribute of 
[QtIfwExternalOp](#qtifwexternalop) objects, which in turn are utilized by  
[QtIfwPackageScript](#qtifwpackagescript) objects.
  
By default, such resources will be extracted into a temporary location on the target and 
removed at the end of installation. If you will require any for maintenance operations (i.e. 
during updates or uninstallation), enabling the `isMaintenanceNeed` attribute will cause the 
resource to be retained on the target, so it will be available later when needed. 

Constructor:
       
    QtIfwExternalResource( name, srcPath, srcBasePath=None, 
                           isMaintenanceNeed=False, contentKeys={} )

Object Attributes & default values:

    name              = <required>               
    srcPath           = <required> 
    srcBasePath       = None
    isMaintenanceNeed = False
    contentKeys       = {}
 
Object Methods:

    targetPath( key=None )
    targetDirPath()
 
    targetPathVar( key=None )
    targetDirPathVar()
 
Static Methods:
 
	BuiltIn( name, isMaintenanceNeed=False )

Built In Windows Resource Names:

	RESOURCE_HACKER
		http://www.angusj.com/resourcehacker/

**name**:  The base id by which to reference the resources and to name a target 
container directory.  

**srcPath**: The path to the resources **file** or **directory**.  This may be absolute or relative.
 
**srcBasePath**:  If using a relative `srcPath`, you may override the base path with this.

**isMaintenanceNeed**: Enabling this will cause the resource to be retained on the target, so it will be available for the maintenance tool / uninstaller. 

**contentKeys**: A dictionary of key/value pairs to be registered in the installer, allowing 
you to dynamically access the paths within scripts on your target.  If this detail is 
omitted during construction, and your QtIfwExternalResource contains only one file, 
a key will be automatically registered for you as the name of the object. 

**targetPath( key )**: Use this to reference the resource paths when generating 
QtScripts / operations which will utilize it.  Specify the key as registered via 
`contentKeys`. If you omit the key when calling this, and only one key exists 
(such as when bundling a single file), that default key will be implied.     
        
**targetDirPath()**: In the event you need to access the container directory for the tool,
e.g. to change your working directory to it, you may employ this method.
        
**targetPathVar( key=None ), targetDirPathVar()**: The place holders / variable names
to use inside an [ExecutableScript](LowLevel.md#executablescript) to refer to these paths.
Assuming a key is valid, you could also just hardcode it like `@key@` rather than call `targetPathVar( key=None )` to get that back! 
        
**QtIfwExternalResource.BuiltIn**: Convenience method to bundle tools into an installer 
which are included with the library. 
        
## QtIfwExeWrapper

This class provides a means to "wrap" your exe inside of additional external layers.
Such layers may take different forms, and be nested inside of one another.
The benefit of this is to impose a specific environment and or set of parameters 
onto the exe without having to modify it internally.  These options work cross
platform, and could be slapped over the top of a program written in any language.
You may, in fact, even wrap third-party (pre-compiled) programs in these layers!

The easiest way to use this class is to set some of its basic attributes. For
example, `workingDir`, `isElevated`, `envVars`, or `args`.  The approach taken by the 
library is to use the "lightest touch" possible.  If you simply changed the 
default values for those example attributes, their shortcuts (on applicable platforms) 
and the way QtIFW would run the program post installation, would be altered to provided 
the functionality.  

The most flexible attribute you may impose is a `wrapperScript` layer.
This is an [ExecutableScript](LowLevel.md#executablescript) object, used to produce
a persistent "companion" to your binary.  Executing the script rather then the 
binary itself would be the intended means for launching the program.  If this attribute 
is set, "shortcuts" which would normally point a user to the binary, will instead run this 
wrapper layer.  On Windows, this (normally) equates to having a batch file companion. 
On Linux, a shell script companion is created (with an explicit `.sh` extension). On macOS, 
a shell script with no extension is embedded into the .app file when producing a gui application, 
else the same design used on Linux is employed for non-gui programs.  

The application of a wrapper script of this nature is not entirely uncommon - especially on Linux. 
As an example, when deploying Qt C++ applications on Linux which are 
dynamically linked, the **standard procedure** (per Qt documentation) is to use this 
(slightly modified) shell script to load the required libraries: 
 
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
then downloading and installing them as needed.  Or, doing something similar for updates
to your software. Using a wrapper, you could launch a "companion application" along side the 
primary target. You could start a background service, or open help documentation... The
possibilities are really boundless.  

Note: On Windows and Linux desktops (e.g. Ubuntu) for a gui application with **shortcuts**,  
the "built-in wrapper" features (`workingDir`, `isElevated`, `envVars`, `args`) maybe 
used **in combination** with a custom `wrapperScript`. I.e. those options will be applied via 
the shortcut launching the script OR the executable.  If you need the wrapper to work without 
a shortcut involved, you will have to **manually** include these other features in the script.
On **macOS**, this will **always** be applicable because there is no "shortcut" involved.
To add these details yourself, you may wish to first use the built-in attributes without the 
custom script, then copy what is written to the auto generated script into your own.  
Alternately, you could programmatically manipulate the `wrapperScript` attribute referencing 
an [ExecutableScript](LowLevel.md#executablescript) generated for you by this class upon it's 
construction (or upon a call to `refresh()`). 

On **WINDOWS ONLY**: You may optionally enable the `isExe` flag. Rather than a batch file, 
this will produce a proxy exe, which will live adjacent to the target it wraps.  
The icon and version / branding info from the original will be injected into it.

Constructor:

    QtIfwExeWrapper( exeName, isGui=False, 
                     wrapperScript=None, 
                     exeDir=QT_IFW_TARGET_DIR, workingDir=None, 
                     args=None, envVars=None, isElevated=False,
                     isExe=False )    

Attributes & default values:
        
        exeName = <required>        
        isGui   = False
        
        wrapperScript = None

        exeDir        = "@TargetDir@" <QtIfw Built-in Variable>
        workingDir    = None  <None=don't impose here, use QT_IFW_TARGET_DIR via other means>

        args          = None      
        envVars       = None         
        isElevated    = False

		<Windows only>
			isExe           = False
			wrapperExeName  = "<exeName>Launcher" 
        	wrapperIconName = "0.ico"
        				
	        _winPsStartArgs = None  

        <Auto defined via refresh>
        _runProgram       
        _runProgArgs      
        _shortcutCmd      
        _shortcutArgs     
        _shortcutWinStyle 
                            
Functions:
      
        refresh()

## QtIfwOnFinishedDetachedExec

This class defines an action to be invoked upon completing the wizard.
It will launch a detached / asynchronous process when the user clicks 
the "Finished" button (which may occur virtually within a silent installer).
Such actions may be invoked on installation, uninstallation, or both. 

While working independently from it, this class is closely related to 
[QtIfwOnFinishedCheckbox](#qtifwonfinishedcheckbox).  This class provides the 
framework for the core functionally, while that one contributes UI dimensions.    

Constructor:

    QtIfwOnFinishedDetachedExec( name, event=None,   
                                 ifwPackage=None, 
                                 runProgram=None, argList=None,
                                 shellCmd=None, script=None,
                                 openViaOsPath=None,                 
                                 isReboot=False, rebootDelaySecs=2,
                                 ifCondition=None )
                                 onLoad=None, onEnter=None ) 
        
Attributes:   

	name  = name
    
    	<QtIfwOnFinishedDetachedExec.ON_INSTALL / ON_UNINSTALL / ON_BOTH>
    event = ON_INSTALL  
                
    runProgram  = None
    argList     = None
    script      = None 
    isReboot    = isReboot
        
    ifCondition = None <QtScript snippet>
    
    _action     = <auto defined>               

Details:

**ifCondition**: Controls whether to invoke this action via QtScript.
Note, this feature is not applied by the derived class QtIfwOnFinishedCheckbox.
That class invokes the corresponding action if the checkbox is selected.     
             
## QtIfwUiPage

This class closely resembles [QtIfwWidget](#qtifwwidget).  They internally derive
from a common (protected) base class.  In contrast, however, QtIfwWidgets are
**collections** of user interface elements to be injected *into* default wizard pages, 
where QtIfwUiPages are entirely new steps/pages injected *between* (or *over*) 
default wizard pages.   

A great deal can be done to customize the way an installer's interface works by
simply adding custom widgets.  There are limitations, however, to that approach.

This class is used to completely add or overwrite pages in the an installer.
The content of the pages are defined as Qt "forms", i.e. `.ui` (xml) files which 
adhere to the
[Qt UI file format](https://doc.qt.io/qt-5/designer-ui-file-format.html).
While it is possible to *manually* create such forms, typically such files    
are machine generated using a WYSIWYG tool from within
[Qt Creator](https://doc.qt.io/qtcreator/) or
[Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html).

Constructor:

    QtIfwUiPage( name, pageOrder=None, 
                 sourcePath=None, content=None,
                 onLoad=None, onEnter=None ) 
        
Attributes:   

    name             = <required>
    pageOrder        = None  
 
    content          = None
    replacements     = {}            
 
    onLoad           = None
    onEnter          = None       
    eventHandlers    = {}
    supportScript    = None  
    
    isIncInAutoPilot = False
    _isOnLoadBase    = True    
    _isOnEnterBase   = True
        
Functions:

    fileName()
    resolve( qtIfwConfig )
    write( dirPath )
    
Details:

**name**: This identifier will be used to name a .ui file containing the form, and to reference the page widget within any scripting.

If you wish to *replace* a default page, set the `name` for an object of this 
type to `QT_IFW_REPLACE_PAGE_PREFIX` *concatenated* with one of the following page name constants: 

    QT_IFW_INTRO_PAGE      
    QT_IFW_TARGET_DIR_PAGE 
    QT_IFW_COMPONENTS_PAGE 
    QT_IFW_LICENSE_PAGE    
    QT_IFW_START_MENU_PAGE 
    QT_IFW_READY_PAGE      
    QT_IFW_INSTALL_PAGE    
    QT_IFW_FINISHED_PAGE   

Conversely, to add a *new* page, give it some other name and specify the 
`pageOrder`using one the constants above. 

**pageOrder**: If **not** a replacement, the page will be added added BEFORE 
this specified page.

**onLoad**: Qt Script snippet invoked when loading the page into memory. This is executed within a **package** script, when then "component" is constructed.  It's scope therefore is limited to such, and it cannot call functions defined in the **controller script**.  UI page resources are contained within packages, which is why they are loaded and configured from there.

**onEnter**: Qt Script snippet invoked upon entering / displaying the page to the user.
This is executed within a **controller** script, it's scope is limited to such.  Therefore,
**package** script functions and globals are not available here.   

**isIncInAutoPilot**: This attribute is only applied when the page is **not** a replacement.  Note, this is `False` by default.  Set this to `True`, to load this "additional" page
when running in "auto pilot mode" (e.g. within a 
[Silent Installer](LowLevel.md#silent-installers) context.  It is then on you to ensure
that alternate installation mode functions as desired.  See `_isOnEnterBase`. 

**_isOnLoadBase**: *Protected* Note, this is enabled by default. When this is set to `True`,
an auto generated script will be added to the installer, which will execute prior to
`onLoad`.  This "base" script will dynamically resize the page, so it fits properly on each
alternate platform's version of the installer.
It is recommended you leave this in place, unless you are overwriting it. 
Having this in place will additionally create a `var page`, which refers to
this page. The `onLoad` script may then make use of that variant to access the page widget or the child widgets on it.
See [Installer Scripting](LowLevel.md#installer-scripting)

**_isOnEnterBase**: *Protected* Note, this is enabled by default. When this is set to `True`, 
an auto generated script will be added to the installer, which will execute prior to `onEnter`.  This "base" script will automatically "click" the "Next" button upon displaying the page, when running in "auto pilot mode" (e.g. within a 
[Silent Installer](LowLevel.md#silent-installers) context.  
Having this in place will additionally create a `var page`, which refers to
this page. The `onEnter` script may then make use of that variant to access the page widget or the child widgets on it.
See [Installer Scripting](LowLevel.md#installer-scripting)

**eventHandlers**: Qt Script simple "event handler" dictionary containing entries in the form: name:body.
The typical use case for this attribute involves the `onLoad` script connecting events (e.g. button clicks) to handlers. The `eventHandlers` then provide the definitions for what to do
upon event occurrences. (Note: These are defined within a **package** script, but are **controller.prototypes**.)
Note this uses the Qt signal/slot mechanism for **built-in** widget types.  You must add your
own "connections", via the Qt Script rules for such (again typically within your `onLoad`).  
An example of that would look like: `page.mybutton.released.connect(this, this.myhandler);`.

**supportScript**: A **completely open ended** Qt Script (string) attribute, for injecting 
any additional support/helper function definitions which maybe handy.  Note that these will live in the global space of the **controller** script. Be careful to avoid name conflicts!
             
**replacements**: A dictionary containing entries in the form: placeholder:value.  Upon 
writing the `.ui` file for the installer definition the library the generates, all "replacements"
in the `content` will be resolved.

TODO: further explain the complicate logic for page order (for replacement pages, or multiple pages with the same order...).  Also elaborate on ui replacements, the "resolve" function, provide a base example .ui in the docs...

### QtIfwDynamicOperationsPage

This class is derived from `QtIfwUiPage`. It provides a "blank" page for performing
custom operations during the installation process.  Note that these operations take place
outside of the main, built-in "installer operations", and instead allow more dynamic 
actions to place "around" that process. Optionally, you may also control the UI as your operation proceeds to indicate the status / result of the operations.  

Constructor:

    QtIfwDynamicOperationsPage( name, operation="", asyncFuncs=[],
                                order=QT_IFW_PRE_INSTALL, 
                                onCompletedDelayMillis=None )            
                               
Static Functions:

    onCompleted( name )                                           

Details:

**operation**: The custom QtScript to execute, kicking off the operation. At the end of this
script, you this should explicitly return a boolean indication of completion.  If completion is indicated (i.e. **true** is returned), the `onCompletedDelayMillis` parameter will dictate what occurs next (see the description for the constructor argument). If **false** is returned, then nothing will occur directly following the initial (synchronous) "kick off".

You may wish to return **false** from the **operation** script, so you that you may continue
the custom task by employing a [QtIfwDynamicOperationsPage.AsyncFunc](#qtifwdynamicoperationspage-asyncfunc) - or a series of them. At the end of such a 
function, you may inject what is returned from the static `onCompleted( name )` function 
of this class, in order to allow the advancement of the installer wizard.  

The `operation` function will have a reference to the UI page passed to it (called `page`).
During your operation, you may wish to call functions such as 
`setCustomPageText( page, title, description )`
(or build that script via the Python helper:
`setCustomPageText( title, description, isAutoQuote=True, pageVar="page" )`).  

**asyncFuncs**: List of [QtIfwDynamicOperationsPage.AsyncFunc](#qtifwdynamicoperationspage-asyncfunc) objects. See the description for `operation` above.

**order**: Specify either `QT_IFW_PRE_INSTALL` or `QT_IFW_POST_INSTALL`.
Note: You may NOT specify one of the standard options for a `QtIfwUiPage` attribute
 `pageOrder`.  

**onCompletedDelayMillis**: By default, this is set to `None`, which indicates that upon
completion, the page should advanced instantly.  If a value greater than 0 is provided, the
page will automatically advance after a delay of that duration.  Alternatively, an integer 
value of 0 (or less than 0), will indicate a manual advancement will take place.  The
"Next" button will become enabled, and the user may click such when they choose. 

**onCompleted( name )**:  Returns a string to do be injected into whatever QtScript you are 
dynamically generating.  (This not somehow literally "invoke" the function when called from 
the Python library! )

#### QtIfwDynamicOperationsPage.AsyncFunc

This class is used to define QtScript functions to be used by a [QtIfwDynamicOperationsPage](#qtifwdynamicoperationspage), which may be invoked
**asynchronously**.  The primary application for this mechanism is to allow UI modifications
to be redrawn on the screen, while performing long "blocking" operations.  To use it
in this manner, you should execute your UI modification code, and then invoke a
blocking operation which is defined within one of these async functions.  The UI will
thus be updated prior to the block.  At the end of the long running async function,
you may repeat the pattern, if desired, to again update the screen prior to initiating
another task which would prevent a screen refresh.  Such a design pattern simulates 
synchronous code, while getting the benefit of having the UI change through out it.

**Note: multiple overlapping AsyncFunc invocations are not currently supported.** The result
of attempting will yield undesired results!  Use these sequentially, one invoking another, 
in a chain is described previously. 

Constructor:

    AsyncFunc( name, parms=[], body="", delayMillis=1,
               standardPageId=None, customPageName=None )
        
Attributes:   

    name        = <required>
    args        = []
    body        = ""
    delayMillis = 1
    standardPageId = None
    customPageName = None

Functions:

    invoke( args=[], isAutoQuote=True ):        

Details:

**name**: The function name.  (Note this will not be the complete, *real* function name in the generated QtScript).

**args**: The names of the function arguments. 

**body**: The body of the function.

**delayMillis**: The number of milliseconds to wait before invoking the function.

***standardPageId**: Provide a standard page id constant to effectively bind the 
function to the page.  You will magically have a `page` var within the function 
to access the UI elements.

**customPageName**: Provide the name of a custom page effectively bind the 
function to the page.  You will magically have a `page` var within the function 
to access the UI elements.

**invoke()**: Returns a string to do be injected into whatever QtScript you are dynamically 
generating.  (This not somehow literally "invoke" the function when called from the Python
library! )

### QtIfwOnPriorInstallationPage

This class is derived from `QtIfwUiPage`. As one would assume, this provides a base
from which to start modifying the distbuilder addition to QtIFW "Prior Installation Detected" 
installer page.  If another page has not been supplied for this, distbuilder will use this class to apply it's own default customization to the natural QtIfw interface.  

Constructor:

    QtIfwOnPriorInstallationPage()  # 0 arguments!                

### QtIfwRemovePriorInstallationPage

This class is derived from `QtIfwDynamicOperationsPage`.  It works in concert with 
`QtIfwOnPriorInstallationPage`, performing the actual action of the removal.  If desired,
you may supply your own custom definition of this page, else the library will inject the
default version of this.

Constructor:

    QtIfwRemoveInstallationPage()  # 0 arguments!                

### QtIfwTargetDirPage

This class is derived from `QtIfwUiPage`. As one would assume, this provides a base
from which to start modifying the "Target Directory" installer page.  If another page 
has not been supplied for this, distbuilder will use this class to apply it's own 
default customization to the natural QtIfw interface.  

Constructor:

    QtIfwTargetDirPage()  # 0 arguments!                
                 
### QtIfwSimpleTextPage
      
This class is derived from `QtIfwUiPage`.  It does not require ANY form / .ui 
content passed to it. It provides a page layout with the only elements being
`title` and `description`, which can both be set easily via arguments to the constructor of this class.  That text may contain all valid QtIFW dynamic substitutions e.g. these [Installer Variables](LowLevel.md#installer-variables), or directly using the `@variable@` syntax. See https://doc.qt.io/qtinstallerframework/scripting.html#predefined-variables.  

By providing an `onLoad` or `onEnter` script, you may define more comprehensive 
manipulations of the pages elements. Alternatively, you wish to specify **no text** 
or content at all for the page, other than perhaps including a message such as "working..." and then use the page as a place holder to perform a given process.  
There are many imaginative ways for using this class as a convenient platform from which to start a custom, dynamic page.

Constructor:

    QtIfwSimpleTextPage( name, pageOrder=None, 
                         title="", text="", 
                         onLoad=None, onEnter=None ) 

## QtIfwWidget

This class closely resembles [QtIfwUiPage](#qtifwuipage).  They internally derive
from a common (protected) base class.  In contrast, however, QtIfwWidgets are
**collections** of user interface elements to be injected *into* default wizard pages, 
where QtIfwUiPages are entirely new steps/pages injected *between* (or *over*) 
default wizard pages.    

Note that a QtIfwWidget that you create and inject into a page will generally contain 
other widgets.  To access the nested widgets in a QtScript, you would use the notation `page.parent.child`.

The content of the widgets are defined as Qt "forms", i.e. `.ui` (xml) files which 
adhere to the
[Qt UI file format](https://doc.qt.io/qt-5/designer-ui-file-format.html).
While it is possible to *manually* create such forms, typically such files    
are machine generated using a WYSIWYG tool from within
[Qt Creator](https://doc.qt.io/qtcreator/) or
[Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html).

Constructor:
    
    QtIfwWidget( name, pageName, position=None, 
                 sourcePath=None, content=None,
                 onLoad=None, onEnter=None )

Attributes:   

    name     = <required>
    pageName = <required>
    position = None
     
    content          = None
    replacements     = {}            
         
    onLoad           = None
    onEnter          = None       
    eventHandlers    = {}
    supportScript    = None  
    
    _isOnLoadBase    = True    
    _isOnEnterBase   = True
            
Functions:

    fileName()
    resolve( qtIfwConfig )
    write( dirPath )

**pageName**: The wizard page where the widget will be added.

**position**: 0 based index where the widget will be injected onto the page.
Injections occur at the bottom of the default page, below the default elements.
(per Qt's design).

**onEnter**: Qt Script snippet invoked upon entering / displaying the page to the user.  This code will be invoked AFTER the initial "page call back" on which the widget was injected.  To modify those page call backs instead, see [QtIfwControlScript](#qtifwcontrolscript).     
    
### QtIfwOnFinishedCheckbox

A QtIfwWidget to be injected into the **Finished** QtIFW wizard page.
If one of these checkboxes is selected upon exiting a successfully completed wizard,
the action associated with that will be executed in a "detached" manner
(i.e. a process which is spawned by the installer, but not bound to it,
so that it may live on after the installer process no longer exists).   

In addition to inheriting from class QtIfwWidget, this class is also
a decedent of [QtIfwOnFinishedDetachedExec](#qtifwonfinisheddetachedexec).     
That class provides the framework for the core functionally, while this
one contributes UI dimensions.

Note: This class only adds checkboxes to the **installer** finished page.
It is not possible to add custom widgets to the **uninstaller** finished page,
because widgets are bundled and loaded via components (i.e. packages), and the 
QtIFW uninstaller does not load components!  For comparable functionality, you 
may employ QtIfwOnFinishedDetachedExec.      
    
Constructor:

    QtIfwOnFinishedCheckbox( name, text=None, position=None,  
                             ifwPackage=None, 
                             runProgram=None, argList=None,
                             shellCmd=None, script=None,
                             openViaOsPath=None,        
                             isReboot=False, rebootDelaySecs=2,                                
                             isVisible=True, isEnabled=True, isChecked=True )

Attributes & default values:    

    name         = <required>
    checkboxName = <automatic>    
    position     = None <automatic, per object instantiation order>     
    
    isReboot     = False
            
Functions:

	<These return QScript snippets>
    isChecked()
    setChecked()
    enable( isEnable=True )
    setVisible( isVisible=True )
                           
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
