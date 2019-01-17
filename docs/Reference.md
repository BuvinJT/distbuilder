# Reference Manual 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Configuration Factory  

It is typical for a build script to start by creating
a high-level *ConfigFactory* object and setting its attributes.

The major functions within the distbuilder library rely
upon a collection of "configuration" objects which supply
parameters to drive various processes.  Many of these 
classes have overlapping attributes, and scripts employing 
a series of these tend to have a great deal of redundant
parameter passing.  With this in mind, the ConfigFactory class 
was created.

See [Configuration Classes](#configuration-classes) for more 
information on the type of objects created by this factory class.  

### ConfigFactory

Using this class, you can produce config objects without 
having to supply the same values repeatedly.  Then, you 
may customize the objects if needed after they have been 
roughly defined for you.    

Constructor:

    ConfigFactory()
    
Attributes & default values:                                               

    productName = None
    description = None
    
    companyTradeName = None
    companyLegalName = None      
            
    opyBundleLibs = None
    opyPatches    = None
    
    binaryName   = None  
    isGui        = False           
    entryPointPy = None
    iconFilePath = None       
    version      = (0,0,0,0)
		
    setupName        = "setup"
    ifwDefDirPath    = None
    pkgSrcDirPath    = None
    ifwPkgName       = None
    ifwPkgNamePrefix = "com"    
    ifwScriptName    = "installscript.qs"
    ifwScript        = None
    ifwScriptPath    = None   

Object creation functions:

    pyInstallerConfig()    
    opyConfig()
    qtIfwConfig()
    qtIfwConfigXml()
    qtIfwPackageXml()    
    qtIfwPackageScript()

## Process Classes

Many build scripts will follow the same essential
logic flow, to produce analogous distributions. 
As such, using high-level "process classes" can prevent 
having multiple implementation scripts be virtual 
duplicates of one another, each containing a fair volume 
of code.  

### PyToBinInstallerProcess 

This process class converts a program written in .py
scripts to a stand-alone binary, then packages it 
for deployment within an installer.  It uses a
[ConfigFactory](#configfactory)  to automatically produce the config 
objects it requires, but allows a client to modify
those objects before they are implemented by defining
a derived class and overriding certain functions as 
needed for this purpose.       

Constructor:

    PyToBinInstallerProcess( configFactory, 
                             name="Python To Binary Installer Process",
                             isObfuscating=False, isMovedToDesktop=False )
    
Attributes & default values:
                                               
    configFactory         = <required>  
    name                  = "Python To Binary Installer Process"
    isObfuscating         = False
    isDesktopTarget       = False
    isTestingObfuscation  = False
    isTestingExe          = False
    isTestingInstall      = False
    isVerboseInstall      = False
    
"Virtual" configuration functions to override:  

    onOpyConfig( cfg )                    
    onPyInstConfig( cfg )
    onQtIfwConfig( cfg )              

Use:

Simply invoke the `run()` function to execute the process. 

## Stand-Alone Executables 
        
To build a stand-alone binary distribution of a Python
program, invoke the buildExecutable function: 

    buildExecutable( name=None, entryPointPy=None,
        			 pyInstConfig=PyInstallerConfig(), 
        			 opyConfig=None, 
				     distResources=[], distDirs=[] )
    
**Returns (binDir, binPath)**: a tuple containing:
    the absolute path to the package created,
    the absolute path to the binary created 
    (within the package). 

**name**: The (optional) name given to both the resulting 
	executable and package distribution directory.
	This argument is only applied if pyInstConfig 
	is None. If omitted, the pyInstConfig attribute 
	for this is used.
    
**entryPointPy**: The (optional) path to the Python script 
	where execution begins. This argument is only 
	applied	if pyInstConfig is None. If omitted, the 
	pyInstConfig attribute for this is used.
        
**pyInstConfig**: An (optional) [PyInstallerConfig](#pyinstallerconfig) 
    object to dictate extended details for building 
    the binary using the PyInstaller Utility. If 
    omitted, the name and entryPointPy arguments, 
    plus other default settings will be used.

**opyConfig**: An (optional) [OpyConfig](#opyconfig) object, to 
	dictate code obfuscation details using the Opy 
	Library. If omitted (or explicitly specified as	None),
	no obfuscation will be performed.
	See [Executable Obfuscation](#executable-obfuscation).
     
**distResources**: An (optional) list of external 
    resources to bundle into the distribution package 
    containing the binary. You may use a simple 
    list of strings containing simply file/directory 
    names/paths relative to the original project 
    directory. Else, you may provide a list of two 
    element tuples, with a specific source and 
    destination.  The source may be an absolute path 
    from another location on your file system. The 
    destination maybe whatever name/path you want
    specified relative to the package being created.    
    
**distDirs**: An (optional) list of directories to 
    create within the package.  Note distResources
    implicitly does this for you when there is 
    a source to copy.  This additional option is
    for adding new empty directories.  
                    
## Executable Obfuscation

PyInstaller is a truly amazing utility, but it has a significant
inherent weakness... it is possible reverse engineer the binaries 
it produces to extract the original source code! Distribution Builder 
has a core built-in feature to mitigate this risk for you: *code obfuscation*.
 
To generate an obfuscated version of your project (without 
converting it to binary) invoke obfuscatePy:

    obfuscatePy( opyConfig )

**Returns (obDir, obPath)**: a tuple containing:
    the absolute path to the obfuscated package,
    the absolute path to the obfuscated entry point script
    (within the package). 
    
**opyConfig**: An [OpyConfig](#opyconfig) object, which dictates the 
    code obfuscation details using the Opy Library. 
    
Upon invoking this, you will be left with an "obfuscated"
directory adjacent to your build script.  This is a useful 
preliminary step to take, prior to running buildExecutable, 
so that you may inspect and test the obfuscation results 
before building the final distribution package.
               
## Library Obfuscation  

To generate an obfuscated version of your project, which 
you can then distribute as an importable library, invoke 
obfuscatePyLib:
 
    obfuscatePyLib( opyConfig, 
                    isExposingPackageImports=True, 
                    isExposingPublic=True )

**Returns (obDir, setupPath)**: a tuple containing:
    the absolute path to the obfuscated directory,
    the absolute path to the (non obfuscated) setup.py 
    script within the prepared package  

**opyConfig**: An [OpyConfig](#opyconfig) object, to 
	dictate code obfuscation details using the Opy Library. 
    
**isExposingPackageImports**: Option to NOT obfuscate 
    any of the imports defined in the package 
    entry point modules (i.e. __init__.py files).
    This is the default mode for a library.  
    
**isExposingPublic**: Option to NOT obfuscate anything 
    which it is naturally granting public access 
    (e.g. module constants, functions, classes, 
    and class members).  All locals and those 
    identifiers prefixed with a double underscore
    (denoting private) will be still be obfuscated.     
    This is the default mode for a library.

-------------------------------------------------------
To install a library (via pip), simply invoke installLibrary: 
    
    installLibrary( name, opyConfig=None, pipConfig=PipConfig() )
    
**Returns: None**

**name**: The name/source of the library.  If the
    library is your current project itself, supply
    the name you are giving it.  If you are NOT
    obfuscating it, specify "." instead.  Otherwise,
    you may specific a remote package name registered
    with pip (i.e. the typical way pip is used),
    or a local path, or a url (http/git). See
    pip documentation for details.               
    
**opyConfig**: An (optional) [OpyConfig](#opyconfig) object, 
    to dictate code obfuscation details using 
    the Opy Library. If omitted, no obfuscation 
    will be performed. If you are building
    an obfuscated version of your project 
    as a importable library, this function is useful 
    for testing the operations of your library 
    post-obfuscation/pre-distribution. This will  
    run obfuscatePyLib with default arguments, 
    install the library, and remove the temporary 
    obfuscation from the working directory.                             
    
**pipConfig**: An (optional) [PipConfig](#pipconfig) object, to dictate
    extended installation details.  If omitted,
    the library is simply installed in the standard
    manner to your (global) Python site packages.
    Notable attributes include "incDpndncsSwitch",
    "destPath" and "asSource".  These allow you to 
    skip dependency gathering if desired, install to 
    a specific path such as a temp build directory,
    and to request raw .py scripts be placed there.
    Note that remote raw pip packages will require an 
    alternate "vcs url" be supplied to "development" 
    repository in place of the simple package name.  
    See [editable-installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)
            
    uninstallLibrary( name )

**Returns: None**

Simply uninstalls a library from Python site packages
in the basic/traditional pip manner.    

    vcsUrl( name, baseUrl, vcs="git", subDir=None )  

Convenience function to build vcsUrls from their
component parts. This is to be used in conjunction
with the PipConfig attribute asSource.
See https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support

## Obfuscation Features 

The Opy Library contains an [OpyConfig](#opyconfig) class, which has been extended
by this library (and aliased with the same name).  The revised /
extended class contains attributes for patching the obfuscation and
for bundling the source of external libraries (so that they too maybe 
obfuscated). This new configuration type has the notable additions:
 
    patches
    bundleLibs 
    sourceDir

Patching:

Opy is not perfect.  It has known bugs, and can require a bit of 
effort in order to define a "perfect" configuration for it. In the 
event you are struggling to make it work exactly as desired, an
"easy out" has been provided by way of "patching" the results. If 
you have already determined exactly which files/lines/bugs
you are encountering, you may simply define a list of "OpyPatch"
objects for the configuration.  They will be applied at the end 
of the process to fix any problems. An [OpyPatch](#opypatch) is created via:

    OpyPatch( relPath, patches, parentDir=OBFUS_DIR_PATH )
    
relPath: The relative file path within the obfuscation 
results that you wish to change.  

patches: A list of tuples. 2 element tuples in the form 
(line number, line) will be utilized for complete line 
replacements. Alternatively, 3 element tuples in the form 
(line number, old, new) will perform a find/replace operation
on that line (to just swap out an identifier typically).  

parentDir: An (optional) path to use a directory other 
than the standard obfuscation results path. 

Library Bundling:
         
The sourceDir defaults to THIS_DIR.  If bundleLibs is defined, it is 
used in combination with sourceDir to create a "staging directory".
The bundleLibs attributes may be either None or a list of     
"LibToBundle" objects. [LibToBundle](#libtobundle) objects maybe created via: 

    LibToBundle( name, localDirPath=None, pipConfig=None, 
                 isObfuscated=False )

That class has attributes named likewise, which may be set after 
creating such an object as well.    

**name**: The name of the library, i.e. the name to be given to the 
    bundled package.  
    
**localDirPath**: If this library may be simply copied from a local 
    source, this is the path to that source.  Otherwise, leave 
    this as None.  
    
**pipConfig**: A [PipConfig](#pipconfig) object defining how to download and 
    install the library.  The destination will be automatically 
    set to the "staging    directory" for the obfuscation process.   
    
**isObfuscated**: A boolean indicating if the library is *already* 
    obfuscated, and therefore may be bundled as is.  

In the event that defining bundleLibs for an OpyConfig object will 
not suffice to setup your staging directory, you may instead call:      

    createStageDir( bundleLibs=[], sourceDir=THIS_DIR )

Returns: the path to the newly created staging directory.

After doing this, you may perform any extended operations that you 
require, and then set an OpyConfig object's sourceDir to that 
staging path while leaving bundleLibs as None in the configuration.

Note that the OpyConfig external_modules list attribute must still 
be set in such a manner to account for the libraries which were 
bundled, or which remain as "external" imports.
                
## Installers 
            
Upon creating a distribution (especially a stand-alone executable), 
the next logical progression is to bundle that into a full-scale 
installer. This library is designed to employ the open source,
cross platform utility: Qt IFW  (i.e. "Qt Installer Framework") 
for such purposes. While the prototypical implementation of this
tool is with a Qt C++ program, it is equally usable for a Python
program (especially if using "Qt for Python", and a QML driven 
interface...).  

    buildInstaller( qtIfwConfig, isPkgSrcRemoved=False )

**Returns**: the absolute path to the setup executable created.  

**qtIfwConfig**: A (required) [QtIfwConfig](#qtifwconfig) object which dictates 
     the details for building an installer.      
     Perhaps most critically, this object includes a "qtIfwDirPath"
     attribute. As this utility's path is not readily
     resolvable, such allows the user to define that.
     If omitted, the library will look for an 
     environmental variable instead, named "QT_IFW_DIR".
     Defining such is arguably the better option (since
     all your build scripts may then draw upon that)
     and your project collaborators may independently 
     define their own paths.
     The distbuilder library allows you either define a
     QtIFW installer in the full/natural manner, and then
     drawn upon that resource, or it can generate one from 
     entirely from scratch, or any combination thereof is 
     possible. Setting the attribute installerDefDirPath, 
     indicates that the installer definition (or at least part 
     of it) already exists and is to be used.  Dynamic components
     can be defined via attributes for the nested objects of type
     [QtIfwConfigXml](#qtifwconfigxml), [QtIfwPackageXml](#qtifwpackagexml), 
     and [QtIfwPackageScript](#qtifwpackagescript).                                  
     Other key attributes include the "pkgName", which is
     the sub directory where your content will be 
     dynamically copied to within the installer, and the 
     "pkgSrcDirPath" (most typically the "binDir" returned 
     by buildExecutable), which is source path of the 
     content. 
    
**isPkgSrcRemoved**: A "convenience" option denoting if the 
    package source content directory should be deleted 
    after successfully building the installer.   

## Testing

### Stand-alone Executables 

Upon creating a binary with PyInstaller, use the
following to test the success of the operation:  
    
    run( binPath, args=[], 
         wrkDir=None, isElevated=False, isDebug=False )      

**binPath**: The path to the binary to be executed. 
Note that the path is returned by `buildExecutable`, 
which allows the results of that to flow
directly into this function.  

**args**: An (optional) list of arguments, 
(or a flat string) to pass along to your program.  

**args**: An (optional) working directory specification.
If omitted (or None), the working directory will be 
automatically set to that of the binary path specified.  

**isElevated**: Boolean (option) to run the binary with 
elevated priviledges.

**isDebug**: Boolean (option) for explictly relaying 
standard output and standard error messages. Set this
to `True` to debug a PyInstaller binary which
was created with `pyInstConfig.isGui` set to `True`.
On some platforms, when that configuration is used, 
messages sent to the console (e.g. print statements 
or uncaught exceptions) are not visible even when launching
the application from a terminal. Enabling this option, 
however, will expose those messages to you. This can 
be invaluable for debugging problems that are unique 
to a stand-alone binary, and not present when run in 
the original raw script form.  (Note: some IDE's
may render this inoperable e.g. Eclipse/PyDev, in
which case be sure to use the terminal directly!)  

### Obfuscated scripts  

Upon creating a Python obfuscation, you may wish the 
to test the success of that operation. The following
was provided with that in mind:    

    runPy( pyPath, args=[], isElevated=False )

**pyPath**: The path to the script to be executed. 
Note that the path is returned by `obfuscatePy`, which allows 
the results of that to flow directly into this function.  

**args**: An (optional) list of arguments, 
(or a flat string) to pass along to your program.  

**isElevated**: Boolean (option) to run the binary with 
elevated priviledges.
   
The working directory will be automatically set to 
the directory of the python script.  

### Installers

The following two options are available for a QtIFW installer:
  
1) Manually run the installer with the "-v" switch 
   argument. Or, if running it via this library using the
   `run(...)` function, you can pass the `QT_IFW_VERBOSE_SWITCH` 
   constant as an argument.
       
2) If the build process is failing before you can run 
   the installer, try setting `qtIfwConfig.isDebugMode` 
   to `True` for verbose output.

## Archives and Distribution

Once you have a fully built distribution package, the 
following functions provide an easy means for further 
preparing the program for distribution:   

    toZipFile( sourceDir, zipDest=None, removeScr=True )

**Returns**: the path to the zip file created.         
    
**sourceDir**: the directory to convert to a zip
    (typically the binDir).   
    
**zipDest**: (optional) full path to the zip file to
    be created. If not specified, it will be
    named with same base as the source, and 
    created adjacent to it.          
    
**removeScr**: Option to delete the sourceDir after
    creating the zip of it. Note this is the 
    default behavior.

    moveToDesktop( path )            
    
**Returns**: the new path to the file or directory.        

Moves a file or directory to the desktop.
(Note: it *moves* the path specified, it does
not leave a copy of the source). This
*Replaces* any existing copy found at the 
destination path (i.e. on the desktop).
        
*TODO: Add git commit/push...*    
                                                                  
## Low-Level Utilities

The following low level "utilities" are also provided for 
convenience, as they maybe useful in defining the build 
parameters, further manipulating the package, or testing 
the results, etc.   

    THIS_DIR 
    
The path to the directory running the build script. 
(This should be the path to your project directory.) 

    absPath( relPath )
    
The absolute path relative to THIS_DIR (which is not 
necessarily the current working directory).  

    modulePath( moduleName )
    
The absolute path to an importable module's source.
(Note the moduleName argument should be a string, not 
an unquoted, direct module reference.)            
This is useful for dynamically resolving the path to 
external modules which you may wish to copy / "bundle" 
for obfuscation.  Returns None if the name is invalid 
and/or the path cannot be resolved.
Note that this often resolves the path to a library's
package entry point (i.e. an __init__.py) file where 
the module is initially imported, rather than literal 
module path. Normally modulePackagePath will be more 
useful...   

    modulePackagePath( moduleName )

Similar to modulePath, but this return the module's 
parent directory.  More often than not, a module 
will have dependencies within the package / library
where it resides. As such, resolving the package path
can be more useful than the specific module.  
   
    sitePackagePath( packageName )

Similar to modulePackagePath, but takes the package
name rather than a module within it AND is specific
to the site packages collection of libraries, rather
than a more universal path resolution.        

    isImportableModule( moduleName )
    isImportableFromModule( moduleName, memberName )            

Attempts the import, and returns a boolean indication
of success without raising an exception upon failure.  
Like the related functions here, the arguments are 
expected to be strings (not direct references).  
The purpose of this to test for library installation
success, or to preemptively confirm the presence
of dependencies.

    printErr( msg, isFatal=False )

Roughly emulates the print command, but writes to
stderr.  Optionally, exits the script with a return
code of 1 (i.e. general error).

    printExc( e, isDetailed=False, isFatal=False )

Analogous to printErr, but prints an exception's 
more detailed repr() information.  Optionally, 
prints a stack trace as well when isDetailed=True.
Note: use printErr( e ) to print just an exception 
"message". 

    Library Function       Alias For (Standard Function)
                
        exists                 os.path.exists 
        isFile                 os.path.isfile
        isDir                  os.path.exists and not os.path.isfile
        copyFile               shutil.copyFile 
        removeFile             os.remove
        makeDir                os.makedirs
        copyDir                shutil.copytree     
        removeDir              shutil.rmtree
        move                   shutil.move
        rename                 os.rename
        tempDirPath            tempfile.gettempdir()    
        dirPath                os.path.dirname
        joinPath               os.path.join
        splitPath              os.path.split
        splitExt               os.path.splitext 
 
## Configuration Classes

The following classes are used to create objects which
are employed as arguments to various functions within the library.
Many of these can be generated for you using the [Configuration Factory](#configuration-factory).

-------------------------------------------------------
### PyInstallerConfig    

Objects of this type define *optional* details for building 
binaries from .py scripts using the PyInstaller utility 
invoked via the buildExecutable function. 

Constructor: 

    PyInstallerConfig()

Attributes & default values:        

    pyInstallerPath = <python scripts directory>/pyinstaller
      
    name            = None   
    entryPointPy    = None
      
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

### WindowsExeVersionInfo

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

-------------------------------------------------------
### QtIfwConfig 

Objects of this type define the details for building 
an installer using the QtIFW utility invoked via the
buildInstaller function. 

Constructor: 

    QtIfwConfig( pkgSrcDirPath=None, pkgSrcExePath=None,                  
                 pkgName=None, installerDefDirPath=None,
                 configXml=None, pkgXml=None, pkgScript=None,
                 setupExeName=DEFAULT_SETUP_NAME  ) 
                     
Attributes & default values:                                               

    pkgName             = None
    installerDefDirPath = "installer"
	configXml           = None
	pkgXml              = None
	pkgScript           = None     
        
    pkgSrcDirPath   = None
    pkgSrcExePath   = None
    othContentPaths = None                     

    exeName      = None   
    setupExeName = "setup"

    qtIfwDirPath = None    (attempt to use environmental variable QT_IFW_DIR)

    isDebugMode    = False
    otherqtIfwArgs = ""

    isQtCppExe     = False
    isMingwExe     = False
    qtBinDirPath   = None  (attempt to use environmental variable QT_BIN_DIR)
    qmlScrDirPath  = None  (for QML projects only)                    

### QtIfwConfigXml 

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
                    companyTradeName=None, iconFilePath=None ) 
              
Attributes:    

    exeName (used indirectly)
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
 
### QtIfwPackageXml

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

### QtIfwPackageScript

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

Constructor:       

	QtIfwPackageScript( pkgName, fileName="installscript.qs", 
                        exeName=None, script=None, srcPath=None )
                  
Attributes & default values:      

	pkgName  = <required>
    fileName = "installscript.qs"
    
    script = None <or loaded via srcPath>
    
    exeName    = None   
    exeVersion = "0.0.0.0"
    
    pngIconResPath = None
    
    isAppShortcut     = True
    isDesktopShortcut = False

    componentConstructorBody = None
    isAutoComponentConstructor = True
    
    componentCreateOperationsBody = None
    isAutoComponentCreateOperations = True        
                                                                          
-------------------------------------------------------      
### PipConfig

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
             , isUpgrade = False
             , otherPipArgs = "" ) 

Attributes:                        

    pipPath = "pip"  (i.e. on the system path)
    source          
    version         
    verEquality     
    destPath        
    asSource        
    incDependencies       
    isForced                  
    isUpgrade      
    otherPipArgs  (open ended argument string)      
         
------------------------------------------------------- 
### OpyConfig
    
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

### OpyPatch

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

### LibToBundle 

See [Obfuscation Features](#obfuscation-features) for a 
description of how objects of this type are used.

Constructor:

    LibToBundle( name, localDirPath=None, pipConfig=None, isObfuscated=False )
    
Attributes:                    

    name         
    localDirPath 
    pipConfig    
    isObfuscated 

