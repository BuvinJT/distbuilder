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

    PyInstHook( name, script=None ) 

Attributes & default values:
        
    name         = *required     
    script       = None
    hooksDirPath = None 

Object Methods:
	
    fileName()

	read()
	write()

    debug()

    toLines()
    fromLines( lines )
	injectLine( injection, lineNo )
    
Details:

The `name` attribute should simply specify the name of import which invokes the `script`. 
The `name` should **not** contain the *literal* "hook-" *file name* prefix, or a 
.py *file extension*.     

hooksDirPath = This may be override, as needed.  If left as the default `None`, 
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
    content 	 = None

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
          
    exists()            
    path()   
    dirPath() 
       
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
    
    virtualArgs = virtualArgs
    
    uiPages = []
    
    controllerGlobals = None
    isAutoGlobals = True
        
    controllerConstructorBody = None
    isAutoControllerConstructor = True
                                    
	isIntroductionPageVisible = True                                                                                                                                
    introductionPageCallbackBody = None
    isAutoIntroductionPageCallback = True

	isTargetDirectoryPageVisible = True
    targetDirectoryPageCallbackBody = None
    isAutoTargetDirectoryPageCallback = True

    isComponentSelectionPageVisible = True
    componentSelectionPageCallbackBody = None
    isAutoComponentSelectionPageCallback = True

	isLicenseAgreementPageVisible = True
    licenseAgreementPageCallbackBody = None
    isAutoLicenseAgreementPageCallback = True

	isStartMenuDirectoryPageVisible = True
    startMenuDirectoryPageCallbackBody = None
    isAutoStartMenuDirectoryPageCallback = True

	isReadyForInstallationPageVisible = True
    readyForInstallationPageCallbackBody = None
    isAutoReadyForInstallationPageCallback = True

	isPerformInstallationPageVisible = True
    performInstallationPageCallbackBody = None
    isAutoPerformInstallationPageCallback = True
        
	isFinishedPageVisible = True        
    finishedPageCallbackBody = None
    isAutoFinishedPageCallback = True        

    onPageChangeCallbackBody = None

	isRunProgVisible = True
	isRunProgInteractive = True
	
Object Methods:
    
    write()
    debug()

    exists()       	 
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
                  pkgXml=None, pkgScript=None,
                  uiPages=[] ) 

Attributes:    

	<internal id / type>
	pkgId           = None       
	pkgType	        = None
	
	<QtIFW definition>
	name            = None
	pkgXml          = None
	pkgScript       = None
	uiPages         = []
	        
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
				   scriptName=None, isDefault=True )
                  
Attributes & default values:      

	pkgName = <required>
               
	DisplayName    = <required>
	Description    = <required>
	Version        = <required>            
	Script         = None 
	Default        = True
	ReleaseDate    = date.today()
	UserInterfaces = []

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

    QtIfwPackageScript( pkgName, 
                        shortcuts=[], externalOps=[], uiPages=[],
                        fileName="installscript.qs", 
                        script=None, scriptPath=None )
                  
Attributes & default values:      

    pkgName  = <required>
    fileName = "installscript.qs"
    
    script = None <or loaded via scriptPath>
    
    shortcuts   = []
    uiPages     = []

    externalOps = []
    killOps     = []
    customOperations = None
    
    embeddedResources = None    
    packageGlobals = None
    isAutoGlobals = True
            
    componentConstructorBody = None
    isAutoComponentConstructor = True
    
    componentLoadedCallbackBody = None
    isAutoComponentLoadedCallback = True
        
    componentCreateOperationsBody = None
    isAutoComponentCreateOperations = True        
    
    <Linux Only>
    isAskPassProgRequired = False
                                                   
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
    args           	  = None  

    isGui             = True <used in Mac / Linux>       
    
    windowStyle       = None <used in Windows>        

    exeVersion        = "0.0.0.0" <used in Linux>        
    pngIconResPath    = None <used in Linux>   
    
    isAppShortcut     = True
    isDesktopShortcut = False

## QtIfwExternalOp

This class is used to represent shell command / external utility invocations.    
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
QScript `execute` function can be dropped into installation scripts anywhere, 
in an unrestricted manner.   

Constructor:
       
	QtIfwExternalOp( 
              script=None,       exePath=None,       args=[], successRetCodes=[0],  
        uninstScript=None, uninstExePath=None, uninstArgs=[],  uninstRetCodes=[0],
        isElevated=False, workingDir=QT_IFW_TARGET_DIR, onErrorMessage=None ):

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
then downloading and installing them as needed.  Or, doing something similar for updates
to your software. Using a wrapper, you could launch a "companion application" along side the 
primary target. You could start a background service, or open help documentation... The
possibilities are really boundless.  

Note: On Windows and Linux desktops (e.g. Ubuntu) for a gui application with shortcuts,  
the "built-in wrapper" features (`workingDir`, `isElevated`, `envVars`, `args`) maybe 
used in combination with a custom `wrapperScript`, as those options are applied via the shortcut
launching the script OR the executable.  On **macOS**, however, if using a custom script, you will have 
to **manually** include these other features in that script, as the way they are applied 
automatically by distibuilder is through the generation of one. If doing this, the easiest approach
maybe to first use the built-ins without the custom script, and then duplicate the pertinent parts
in your own.  Alternately, you could programmatically manipulate the `wrapperScript` attribute referencing an
[ExecutableScript](LowLevel.md#executablescript) generated for you by this class upon it's construction
or upon a call to `refresh()`. 

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
             
## QtIfwUiPage

A great deal can be done to customize the way an installer's interface works by
simply adding custom scripts.  There are limitations, however, to that approach.

This class is used to completely overwrite, or add, custom pages to an installer.
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

    name           = <required>
    pageOrder      = None  
 
    content        = None
    replacements   = {}        	
 
    onLoad         = None
    onEnter        = None       
    eventHandlers  = {}
    supportFuncs   = None  

    _isOnLoadBase  = True    
    _isOnEnterBase = True
        
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
[Silent Installer](LowLevel.md#silent-installers) context).  
Having this in place will additionally create a `var page`, which refers to
this page. The `onEnter` script may then make use of that variant to access the page widget or the child widgets on it.
See [Installer Scripting](LowLevel.md#installer-scripting)

**eventHandlers**: Qt Script "event handler" dictionary containing entries in the form: name:body.
The typical use case for this attribute involves the `onLoad` script connecting events (e.g. button clicks) to handlers. The `eventHandlers` then provide the handler definitions. 
These are defined within a **package** script, but are **controller.prototypes**.

**supportFuncs**: Open ended Qt Script attribute, for injecting whatever additional
support/helper function definitions maybe handy.  Note that these will live in the global space of the **controller** script. Be careful to avoid name conflicts!
             
**replacements**: A dictionary containing entries in the form: placeholder:value.  Upon 
writing the `.ui` file for the installer definition the library the generates, all "replacements"
in the `content` will be resolved.

TODO: further explain the complicate logic for page order (for replacement pages, or multiple pages with the same order...).  Also elaborate on ui replacements, the "resolve" function, provide a base example .ui in the docs...

### QtIfwPerformOperationPage

This class is derived from `QtIfwUiPage`. It provides a "blank" page for performing
custom operations during the installation process.  Note that these operations take place
outside of the main, built-in "installer operations", and instead allow more dynamic 
actions to place "around" that process. 
Optionally, you may control the UI as your operation proceeds, and upon success / failure.  
To do so, call the QScript function:
`setCustomPageText( page, title, description )` or build that script via the Python helper:
`setCustomPageText( title, description, isAutoQuote=True, pageVar="page" )`.

Constructor:

    QtIfwPerformOperationPage( name, operation="",
                               order=QT_IFW_PRE_INSTALL, 
                               onSuccessDelayMillis=None )                

Details:

**operation**: The custom QScript to execute, driving the operation. At the end of this
script, you this **MUST RETURN A BOOLEAN (TRUE/FASLE) INDICATION OF SUCCESS**.  If success
is indicated, the `onSuccessDelayMillis` parameter will dictate what occurs next.  If
a failure is indicated (via a return of *false*), then nothing will occur post operation.
The page cannot be advanced in this failure state. The user may only click the 
"Cancel" button to quit the installer.  

**order**: You may NOT specify one the standard options for a `QtIfwUiPage` attribute
 `pageOrder`.  Instead, use either `QT_IFW_PRE_INSTALL` or `QT_IFW_POST_INSTALL`.

**onSuccessDelayMillis**: By default, this is set to `None`, which indicates that upon
success, the page should advanced instantly.  If a value greater than 0 is provided, the
page will automatically advance after a delay of that duration.  Alternatively, an integer value of 0 (or less than 0), will indicate a manual advancement will take place.  The
"Next" button will become enabled, and the user may click such when they choose. 

## QtIfwOnPriorInstallationPage

This class is derived from `QtIfwUiPage`. As one would assume, this provides a base
from which to start modifying the distbuilder addition to QtIFW "Prior Installation Detected" 
installer page.  If another page has not been supplied for this, distbuilder will use this class to apply it's own default customization to the natural QtIfw interface.  

Constructor:

    QtIfwOnPriorInstallationPage()  # 0 arguments!                

### QtIfwRemovePriorInstallationPage

This class is derived from `QtIfwPerformOperationPage`.  It works in concert with 
`QtIfwOnPriorInstallationPage`, performing the actual action of the removal.  If desired,
you may supply your own custom definition of this page, else the library will inject the
default version of this.

Constructor:

    QtIfwRemoveInstallationPage()  # 0 arguments!                

### QtIfwTargetDirPagege

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
