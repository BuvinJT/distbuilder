# Low Level Classes And Functions 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Stand Alone Executables 

### buildExecutable
        
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

**opyConfig**: An (optional) [OpyConfig](ConfigClasses.md#opyconfig) object, to 
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

### makePyInstSpec

To generate a PyInstaller .spec file, using the secondary
utility "pyi-makespec" (bundled with PyInstaller), 
invoke the makePyInstSpec function:   

	makePyInstSpec( pyInstConfig, opyConfig=None )

**Returns: the absolute path to the spec file created.
    Also, updates the pyInstConfig argument, supplying 
	a [PyInstSpec](#pyinstspec) object and effectively
	returning it "by reference". 
        
**pyInstConfig**: An [PyInstallerConfig](#pyinstallerconfig) 
    object used to dictate the details for generating 
    the spec file using the makespec Utility.

**opyConfig**: An (optional) [OpyConfig](ConfigClasses.md#opyconfig) object, 
	providing supplemental details regarding the spec file
	creation.  Be sure to include this if you desire obfuscation
	and will be subsequently invoking the buildExecutable function.
      	                    
## Installers 
            
Upon creating a distribution (especially a stand-alone executable), 
the next logical progression is to bundle that into a full-scale 
installer. This library is designed to employ the open source,
cross platform utility: Qt IFW  (i.e. "Qt Installer Framework") 
for such purposes. While the prototypical implementation of that
tool is with a Qt C++ program, it is equally usable for a Python
program (especially if using "Qt for Python", and a QML driven 
interface...).  

### installQtIfw    
 
When the QtIFW utlity is required for use by the library 
(i.e. when [buildInstaller](#buildinstaller) is invoked), 
an attempt will be made to resolve the path to it via a collection 
of methods.  First, if a [QtIfwConfig](ConfigClasses.md#qtifwconfig) object is provided
which specifies a path via the `qtIfwDirPath` attribute, that will be 
employed.  Second, if there is an environmental variable defined named
`QT_IFW_DIR`, that path will be applied.  Next, a default directory 
where the utility would typically be installed will be checked to see if
that exists.  If none of these found, distbuilder will simply download 
the program an install it for you in that "default" location, 
using the [download](#download) function and this `installQtIfw` function. 

If you wish to take control of such yourself, or simply download QtIFW
directly for some other purpose, this function provides the means.   
 
    installQtIfw( installerPath=None, version=None, targetPath=None )

**Returns**: the absolute path to the directory where the utility was 
successfully installed.

**installerPath**: (Optional) The path to the QtIFW installer to be run. 
This may either be a **local** path or a **url** to a location on the web.
If omitted, the `version` argument will be used to dynamically resolve
the url.

**version**: (Optional) The version of QtIFW desired.  This should be provided
as a string e.g. "3.1.1".  If `installerPath` is omitted, this argument 
will be used to dynamically resolve the url.  If this argument is also omitted,
a default version will be selected automatically.

**targetPath**: (Optional) The target directory for installation.  If omitted,
a default path will be used. 
    
### unInstallQtIfw        

This is the counterpart to the `installQtIfw()` function.  It will uninstall
an existing installation of the QtIFW utility.

	unInstallQtIfw( qtIfwDirPath=None, version=None )
 
**Returns**: a boolean to indicate success or failure.

**qtIfwDirPath**: (Optional) The absolute path to the directory where the 
utlility was installed. (i.e. the return value of `installQtIfw()`).  If omitted,
the `version` argument will be looked to next.

**version**:  (Optional) The version of QtIFW to uninstall. If `qtIfwDirPath` is 
omitted, this argument will be used to dynamically resolve the default install path
to the utility for the version specified.  If this argument is also omitted,
a default version will be assumed.
 
### buildInstaller

	buildInstaller( qtIfwConfig, isSilent )

**Returns**: the absolute path to the setup executable created.  

**qtIfwConfig**: A (required) [QtIfwConfig](ConfigClasses.md#qtifwconfig) object which dictates 
     the details for building an installer.      
     The distbuilder library allows you either define a
     QtIFW installer in the full/natural manner, and then
     drawn upon that resource, or it can generate one from 
     entirely from scratch, or any combination thereof is 
     possible. Setting the attribute `installerDefDirPath`, 
     indicates that the installer definition (or at least part 
     of it) already exists and is to be used.  Dynamic components
     can be defined via attributes for the nested objects of type
     [QtIfwConfigXml](ConfigClasses.md#qtifwconfigxml), 
     [QtIfwControlScript](ConfigClasses.md#qtifwcontrolscript),
     [QtIfwPackage](ConfigClasses.md#qtifwpackage),
     [QtIfwPackageXml](ConfigClasses.md#qtifwpackagexml), 
     and [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript).                                  
     Other key attributes include the `pkgName`, which is
     the sub directory where your content will be 
     dynamically copied to within the installer, and the 
     `pkgSrcDirPath` (most typically the `binDir` returned 
     by [buildExecutable](#buildexecutable)), which is source path of the 
     content. 
    
**isSilent**: When `isSilent` is enabled, the QtIFW installer produced will not display 
a GUI or provide any interactive prompts for the user.  All options are dictated by 
command line arguments. While this may certainly be desirable on any platform, it is  
*necessary* to create an installer for a target OS with no GUI (e.g. many Linux distros).
 
See [Silent Installers](#silent-installers) for more information. 

### Standard Installer Arguments

The standard (non silent) QtIFW installer can accept a collection of command line arguments
out of the box.  To see the available options, simply pass the switch `-h` or `--help` 
when executing the binary from a terminal.

The distbuilder library, has added a series of additional options as well (assuming the
built-in default Control Script additions are preserved).  Unfortunately,
there does not appear to be a way to add these to the QtIFW help!  Note these differ from the 
[Silent Installer Arguments](#silent-installer-arguments).
**The following custom arguments must be passed in the format "Key=Value"**: 
    
**errlog=[path]**: The path where you would like (custom) error details written to for installation 
debugging.  The default is `<temp dir>/installer.err`.

**target=[path]**: The target directory for the installation.

**startmenu=[relative path]**: (Windows only) The target start menu directory for 
shortcuts.    

**install=[ids]**: The full set of components to include in the installation, 
represented as a space delimited list of package ids.  Those ids NOT listed, will not be installed 
(unless some custom logic added to the Control script forces them to be).  This list takes 
priority over any `include` or `exclude` arguments.

**include=[ids]**: The components to *additionally* include in the installation, 
represented as a space delimited list of package ids.  Default components do NOT need to be listed
here, as they are already "included" implicitly. 

**exclude=[ids]**: The components to exclude from in the installation, 
represented as a space delimited list of package ids.  Only default components need to be listed
here, those not automatically included they are already "excluded" implicitly.

**accept=[true/false]**: Enable the checkbox for accepting the end user license agreement.

**run=[true/false]**: Enable the checkbox for running the target program at the end of 
the installation.
       
**onexist=[fail/remove/prompt]**: Define the action taken when an existing (conflicting)
installation is present.  The default is to prompt, and allow for automatic removal if
the user so chooses explicitly.   
    
**mode=[addremove/update/removeall]**: This option is provided for controlling how the 
"Maintenance Tool" is to be run.   

**auto=[true/false]**: Enable "Auto pilot" mode.  This is very much akin to a running the 
installation like a [Silent Installer](#silent-installers), and is in fact at the heart
of how that works. Unlike a silent installer, GUI suppression is involved, however,
and some of the extended features are not available e.g. error return codes.                                                      
 
### Silent Installers

"Silent installation" is the process of running a installer without any interactive prompts 
for the user.  It simply runs without "talking" to you.  All options are dictated by 
command line arguments.  This allows for scripted installs of programs, which is useful for 
a great many purposes, e.g. programmatic integrations of external utilities, or running the 
same installation on a large number of workstations.  While such a feature can be desirable 
on any platform, not requiring a GUI interaction is, of course, outright *necessary* if 
one wishes to target an OS with no GUI support (e.g. many Linux distros).

"Silent installation" (and/or no GUI) is not a option provided naturally by 
the Qt Installer Framework. This feature has been made available, however, via this 
library!  As such, it is now easily possible to build installers for environments that
would not normally be able via the otherwise excellent installation system Qt has given us.     

Note that in addition to those major feature additions, a distbuilder silent installer
also returns an error code (1) upon failure.  A natural QtIFW installer does not, 
returning a "success code" (0) even when the installation fails. 

### Silent Installer Arguments

One of the core features of [Silent Installers](#silient-installers) is that they can
be driven by command line arguments.  The following switches have been provided for 
this type of distbuilder installer. Note these differ from the 
[Standard Installer Arguments](#standard-installer-arguments).
             
**-h / --help**: Display help for these arguments.
             
**-v / --verbose**: Enable verbose output. 

**-f / --force**: "Force" installation.  Uninstall an existing installation automatically,
in the event that there is a conflict.  Without this, the installer would abort under such
conditions by default (per the natural QtIFW design).

**-t / --target [path]**: The target directory for the installation.
                         
**-m / --startmenu [relative path]**: (Windows only) The target start menu directory for 
shortcuts.

**-c / --components [ids]**: The full set of components to include in the installation, 
represented as a space delimited list of package ids.  Those ids NOT listed, will not be installed 
(unless some custom logic added to the Control script forces them to be).  This list takes 
priority over any `include` or `exclude` arguments.

**-i / --include [ids]**: The components to *additionally* include in the installation, 
represented as a space delimited list of package ids.  Default components do NOT need to be listed
here, as they are already "included" implicitly. 

**-e / --exclude [ids]**: The components to exclude from in the installation, 
represented as a space delimited list of package ids.  Only default components need to be listed
here, those not automatically included they are already "excluded" implicitly.

The component selecting arguments are only made available when more than one
package is defined for the installer.  If there is only a single package, there is not
a needed to select/de-select it!  When these arguments can be used, the `--help` text
will list the package ids and indicate if they are included by default.  As package ids
are defined in the "Java package" format (e.g. "com.company.product"), and typically 
installers will all have the same long form prefix for all such ids, that prefix will be
truncated for the user's benefit.  So, rather than "com.company.product", the id will become
simply "product".  If any of the packages do not have the same prefix as the rest, they
will all be be listed in the long manner.

### Installer Scripting

While both QtIFW, and the distbuilder additions to it, provide many build-in features
for customizing installers, nothing can provide more open ended flexibility than writing
your own scripts.

QtIFW scripts are written in [Qt Script](https://doc.qt.io/qt-5/qtscript-index.html) 
(which is conceptually a spin off from JavaScript), with
additional custom objects and methods for this context.  To truly understand it and
learn about all of it's features in detail, you should refer to the official 
[QtIFW Manual](https://doc.qt.io/qtinstallerframework/index.html).

The classes [QtIfwControlScript](ConfigClasses.md#qtifwcontrolscript) and
[QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript) provide abstraction layers 
for QtIfw script generation. With these classes you can achieve a great many custom 
behaviors, driven by scripts, without having to learn much about the language yourself. 

Both of the distbuilder script classes provide the following **PYTHON** helpers:

Static Constants :

    TAB         
    NEW_LINE     
    END_LINE    
    START_BLOCK 
    END_BLOCK   
    
    TRUE  
    FALSE 
    
    PATH_SEP   
    
    MAINTENANCE_TOOL_NAME  
    
    VERBOSE_CMD_SWITCH_ARG     
    TARGET_DIR_KEY         
    PRODUCT_NAME_KEY       
    
    ERR_LOG_PATH_CMD_ARG   
    ERR_LOG_DEFAULT_PATH   

    TARGET_DIR_CMD_ARG        
    START_MENU_DIR_CMD_ARG        
    ACCEPT_EULA_CMD_ARG       
    INSTALL_LIST_CMD_ARG      
    INCLUDE_LIST_CMD_ARG      
    EXCLUDE_LIST_CMD_ARG      
    RUN_PROGRAM_CMD_ARG       
    AUTO_PILOT_CMD_ARG        
    
    TARGET_EXISTS_OPT_CMD_ARG 
    TARGET_EXISTS_OPT_FAIL    
    TARGET_EXISTS_OPT_REMOVE  
    TARGET_EXISTS_OPT_PROMPT  
    
    MAINTAIN_MODE_CMD_ARG        
    MAINTAIN_MODE_OPT_ADD_REMOVE 
    MAINTAIN_MODE_OPT_UPDATE         
    MAINTAIN_MODE_OPT_REMOVE_ALL 
        
    OK     
    YES     
    NO     
    CANCEL 

Static Functions:      
                                                   
    log( msg, isAutoQuote=True )            
	debugPopup( msg, isAutoQuote=True )
                      
    setValue( key, value, isAutoQuote=True )          
     
    lookupValue( key, default="", isAutoQuote=True )            
    lookupValueList( key, defaultList=[], isAutoQuote=True, 
                     delimiter=None )
                          
    targetDir()
    productName() 
    
    cmdLineArg( arg, default="" )
    cmdLineSwitchArg( arg )
    cmdLineListArg( arg, default=[] )
    ifCmdLineArg( arg, isNegated=False, isMultiLine=False, )  
    ifCmdLineSwitch( arg, isNegated=False, isMultiLine=False )
                      
    ifInstalling( isMultiLine=False )
    ifMaintenanceTool( isMultiLine=False )

    fileExists( path, isAutoQuote=True )
    ifFileExists( path, isAutoQuote=True, isMultiLine=False )   
    
    yesNoPopup( msg, title="Question", resultVar="result" )             
    yesNoCancelPopup( msg, title="Question", resultVar="result" )                  
    switchYesNoCancelPopup( msg, title="Question", resultVar="result", 
                            onYes="", onNo="", onCancel="" )
    ifYesNoPopup( msg, title="Question", resultVar="result", 
                 isMultiLine=False )
    
    _autoQuote( value, isAutoQuote )

In addition, QtIfwControlScript provides: 

Static Constants :

    NEXT_BUTTON 
    BACK_BUTTON 
    CANCEL_BUTTON
    FINISH_BUTTON
    
    TARGET_DIR_EDITBOX       
    START_MENU_DIR_EDITBOX   
    ACCEPT_EULA_RADIO_BUTTON 
    RUN_PROGRAM_CHECKBOX     

Static Functions:      
                   
    currentPageWidget()                
    assignPageWidgetVar( varName="page" )                
   
    setText( controlName, text, isAutoQuote=True )
    
    clickButton( buttonName, delayMillis=None )                

    	(Note: checkbox controls also work on radio buttons)
	enableCheckBox( checkboxName )                
    disableCheckBox( checkboxName )               
    setCheckBox( checkboxName, boolean )                  

If writing scripts directly for distbulder integration, you may also employ the 
following add-on **QT SCRIPT** functions:

	execute( binPath, args )
	
	sleep( seconds )
	
	clearErrorLog()
	writeErrorLog( msg )
	
	silentAbort( msg )

	targetExists()
	defaultTargetExists()
	cmdLineTargetExists()

	removeTarget()
	
	maintenanceToolExists( dir )
	toMaintenanceToolPath( dir )
	
	WINDOWS ONLY: (resolves via registry lookups)  
	maintenanceToolPaths()
	isOsRegisteredProgram()

### QtIfwPackage list manipulation

These functions are useful within an overridden version of
`onPyToBinPkgsBuilt` in a [RobustInstallerProcess](HighLevel.md#robustinstallerprocess), 
object
	
	findQtIfwPackage( pkgs, pkgId )
	
**Returns**: [QtIfwPackage](ConfigClasses.md#qtifwpackage) object 
within the *pkgs* argument with the id supplied by *pkgId*.   
	
	removeQtIfwPackage( pkgs, pkgId )

Removes the [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
within the *pkgs* argument with the id supplied by *pkgId*.   
	
	mergeQtIfwPackages( pkgs, srcId, destId )
	
Merges the [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
objects within the *pkgs* argument with the ids supplied by 
*srcId* and *destId*.  "Merging" entails a recursive 
directory merge of the source into the target via [mergeDirs](#mergedirs)
as well as combining the [QtIfwShortcut](ConfigClasses.md#qtifwshortcut)
list nested inside the [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript)
objects.	

## Code Obfuscation

Code [obfuscation](https://en.wikipedia.org/wiki/Obfuscation_(software)) 
is the process of **rewriting** normal, human readable code, into a form which
is very difficult (well, *ideally* impossible) to read, yet still executes 
in exactly the same manner when run through the target translator (or compiler).
The reason one would want to do this to is to protect proprietary work and/or
to eliminate security holes (based upon context) while sharing source code.  

[Opy for Distribution Builder](https://pypi.org/project/opy-distbuilder/)
is an obfuscation library for Python.  It can be used for protecting source 
that will be shared directly, or as an additional layer of protection behind 
binaries built with PyInstaller.  

While Opy does not protect your code as well as real compilation does, it's far better
than nothing!  The obfuscation process is "lossy", so while the end result still
functions as desired, Opy inherently destroys the clear text original names for 
functions, classes, objects, etc.  A hacker might still figure out some "secret"
after putting in a good deal of effort, but no one can't just walk away with 
your body of the work on the whole, or instantly spot your security secrets.    

### Executable Obfuscation

Why would you need to obfuscate when building executable binaries?  Aren't they implicitly 
protected by virtue to being compiled?

Well, the thing is you don't literally "compile" when using PyInstaller (or Py2Exe, etc.)!  
The mechanism for creating standalone Python executables works by creating `.pyc` files
and bundling them with a Python interpreter into a neat package.  Unfortunately `.pyc`
can be reverse engineered back into the original (or nearly original) `.py` source.  

As a quick starting point to learn about this hacking process, you can check out 
these Stack Overflow posts:

- [How do you reverse engineer an EXE compiled with PyInstaller?](https://reverseengineering.stackexchange.com/questions/160/how-do-you-reverse-engineer-an-exe-compiled-with-pyinstaller)
- [Is it possible to decompile a compiled .pyc file into a .py file?](https://stackoverflow.com/questions/5287253/is-it-possible-to-decompile-a-compiled-pyc-file-into-a-py-file)  

If you don't trust posts from "random" third parties, simply read this - straight from 
the horse's mouth: 
[PyInstaller Docs: Hiding The Source Code](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html#hiding-the-source-code)

One "solution" to this problem is to bundle `.pye` files instead of `.pyc`.  PyInstaller
provides built-in support for this, in fact.  The alternate `.pye` is an *encrypted* 
equilavent to a `.pyc`.  If your end user is in possession of the decryption key, they can run
the code, because it will be unlocked for them to begin the process of running it.
Unfortunately, that still ultimately exposes the code!  It merely restricts access.
If your goal is to distribute a program, for which you want to prevent access 
to the source, then you couldn't distribute the key!  So, this security measure is only
really pertinent when it is possible for someone to access the program independently from
the key, and the target user being given the key can be trusted with the raw source.
That's a fairly atypical use case...      

#### obfuscatePy
 
To generate an obfuscated version of your project (without 
converting it to binary) invoke obfuscatePy:

    obfuscatePy( opyConfig )

**Returns (obDir, obPath)**: a tuple containing:
    the absolute path to the obfuscated package,
    the absolute path to the obfuscated entry point script
    (within the package). 
    
**opyConfig**: An [OpyConfig](ConfigClasses.md#opyconfig) object, which dictates the 
    code obfuscation details using the Opy Library. 
    
Upon invoking this, you will be left with an "obfuscated"
directory adjacent to your build script.  This is a useful 
preliminary step to take, prior to running buildExecutable, 
so that you may inspect and test the obfuscation results 
before building the final distribution package.
               
### Library Obfuscation  

#### obfuscatePyLib

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

**opyConfig**: An [OpyConfig](ConfigClasses.md#opyconfig) object, to 
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

### Obfuscation Features 

The Opy Library contains an [OpyConfig](ConfigClasses.md#opyconfig) class, 
which has been extended by the distbuilder library (and aliased with the same name).  
The revised / extended class contains attributes for patching the obfuscation and
for bundling the source of external libraries (so that they too maybe 
obfuscated). This new configuration type has the notable additions:
 
    patches
    bundleLibs 
    sourceDir

#### OpyPatch

Opy is not perfect.  It has known bugs, and can require a bit of 
effort in order to define a "perfect" configuration for it. In the 
event you are struggling to make it work exactly as desired, an
"easy out" has been provided by way of "patching" the results. If 
you have already determined exactly which files/lines/bugs
you are encountering, you may simply define a list of "OpyPatch"
objects for the configuration.  They will be applied at the **end** 
of the process (i.e. to the **obfuscated** code) to fix any problems. 
An [OpyPatch](ConfigClasses.md#opypatch) is created via:

    OpyPatch( relPath, patches, parentDir=OBFUS_DIR_PATH )
    
**relPath**: The relative file path within the obfuscation 
results that you wish to change.  

**patches**: A list of tuples. 2 element tuples in the form 
(line number, line) will be utilized for complete line 
replacements. Alternatively, 3 element tuples in the form 
(line number, old, new) will perform a find/replace operation
on that line (to just swap out an identifier typically).  

**parentDir**: An (optional) path to use a directory other 
than the standard obfuscation results path. 

#### LibToBundle
        
When an [OpyConfig](ConfigClasses.md#opyconfig) object is created, the sourceDir 
defaults to `THIS_DIR`.  If the `bundleLibs` attribute is defined, it is 
used in combination with sourceDir to create a "staging directory".
The bundleLibs attributes may be either `None` or a list of     
"LibToBundle" objects, constructed via: 

    LibToBundle( name, localDirPath=None, pipConfig=None, 
                 isObfuscated=False )

That class has attributes named likewise, which may be set after 
creating such an object as well.    

**name**: The name of the library, i.e. the name to be given to the 
    bundled package.  
    
**localDirPath**: If this library may be simply copied from a local 
    source, this is the path to that source.  Otherwise, leave 
    this as None.  
    
**pipConfig**: A [PipConfig](ConfigClasses.md#pipconfig) object defining how to download and 
    install the library. The destination will be automatically 
    set to the "staging directory" for the obfuscation process.   
    
**isObfuscated**: A boolean indicating if the library is *already* 
    obfuscated, and therefore may be bundled as is.  

#### createStageDir

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
      
## Library Installation  
 
### installLibrary
 
To install a library (via pip), invoke installLibrary.
Note: that installLibraries (plural) may used to install
multiple libraries in a single call.  
    
    installLibrary( name, opyConfig=None, pipConfig=PipConfig() )
    
**Returns: None**

**name**: The name/source of the library.  If the
    library is your *current project itself* and you 
    are obfuscating it, be sure to supply the name you 
    are giving it.  If you are NOT obfuscating it, 
    specify "." instead.  If you wish to install a
    remote package registered with pip (i.e. the typical way pip 
    is used), simply supply the name.
    If you wish to use a local path, or a specific url (http/git), 
    see [PipConfig](ConfigClasses.md#pipconfig) (and perhaps the pip documentation 
    for details).               
    
**opyConfig**: An (optional) [OpyConfig](ConfigClasses.md#opyconfig) object, 
    to dictate code obfuscation details using 
    the Opy Library. If omitted, no obfuscation 
    will be performed. If you are building
    an obfuscated version of your project 
    as a importable library, this function is useful 
    for testing the operations of your library 
    post-obfuscation/pre-distribution. This will  
    run [obfuscatePyLib](#library-obfuscation) with default arguments, 
    install the library, and remove the temporary 
    obfuscation from the working directory.                             
    
**pipConfig**: An (optional) [PipConfig](ConfigClasses.md#pipconfig) object, to dictate
    extended installation details.  If omitted,
    the library is simply installed in the standard
    manner to your (global) Python site packages.
    Notable attributes include `incDpndncsSwitch`,
    `destPath` and `asSource`.  These allow you to 
    skip dependency gathering if desired, install to 
    a specific path such as a temp build directory,
    and to request raw .py scripts be placed there.
    Note that remote raw pip packages will require an 
    alternate "vcs url" be supplied to a "development" 
    repository in place of the simple package name.  
    See [editable installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)  

### installLibraries

	installLibraries( *libs )

This function is a convenience wrapper over installLibrary (singular) function.
One of the primary uses for this function is to ensure that the product to be
created by a build script is being run in an environment which has all of its
dependencies. 
	    
**Returns: None**

***libs**: This function is extremely flexible in terms of how 
   it may be invoked. The libs argument maybe a tuple, a list,
   or a series of arguments passed directly to the function 
   of arbitrary length.  The arguments or collection may consist of 
   simple strings (i.e. the library names), or be tuples / dictionaries
   themselves.  When passing tuples, or dictionaries, they will be
   treated as the argument list to installLibrary().
   
Simple example:
 	
	installLibraries( 'six', 'abc' )

Simple example with a version detail:

	installLibraries( 'six', 'abc', 'setuptools==40.6.3' )

Complex example:
 	
 	opyCfg = OpyConfig()
 	... 	
 	pipCfg = PipConfig()
 	... 	
 	myLib = {'name':'MyLib', 'opyConfig':opyCfg, 'pipConfig':pipCfg } 	
 	installLibraries( 'six', myLib )
            
### uninstallLibrary
	
	uninstallLibrary( name )

**Returns: None**

Simply uninstalls a library from Python site packages
in the basic/traditional pip manner.    

### vcsUrl

    vcsUrl( name, baseUrl, vcs="git", subDir=None )  

Convenience function to build vcsUrls from their
component parts. This is to be used in conjunction
with the PipConfig attribute asSource.
See https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support
      
## Testing

### run 

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

**wrkDir**: An (optional) working directory specification.
If omitted (or None), the working directory will be 
automatically set to that of the binary path specified.  

**isElevated**: Boolean (option) to run the binary with 
elevated privileges.

**isDebug**: Boolean (option) for explicitly displaying 
standard output and standard error messages. Set this
to `True` to debug a PyInstaller binary which
was created with `pyInstConfig.isGui` set to `True`.
On some platforms, when that configuration is used, 
messages sent to the console (e.g. *print* statements 
or *uncaught exceptions*) are not visible even when launching
the application from a terminal. Enabling this option, 
however, will expose those messages to you. This can 
be invaluable for debugging problems that are unique 
to a stand-alone binary, and not present when run in 
the original raw script form.  For instance, it is common
for PyInstaller binaries to be missing dependencies which must 
be accounted for (e.g. via "hidden imports").  In such situations,
exceptions maybe thrown when the app launches.  Without this
debugging feature, you may have no information regarding the 
fatal error.  

Note: some IDE / platform combinations may render this 
inoperable e.g. Eclipse/PyDev on Windows, in which case 
simply run the build script directly from the terminal
when employing isDebug.  

### runPy   

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
elevated privileges.
   
The working directory will be automatically set to 
the directory of the python script.  

### Testing installers

The following two options are available for a QtIFW installer:
  
1) Manually run the installer with the "-v" switch 
   argument. Or, if running it via this library using the
   `run(...)` function, you can pass the `QT_IFW_VERBOSE_SWITCH` 
   constant as an argument.
       
2) If the build process is failing before you can run 
   the installer, try setting `qtIfwConfig.isDebugMode` 
   to `True` for verbose output (note this should 
   currently be the be the default now).
      
## Archives and Distribution

Once you have a fully built distribution package, the 
following functions provide an easy means for further 
preparing the program for distribution:   

### toZipFile

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
                
*TODO: Add git commit/push...*    
                                                                        
## ExecutableScript

Executable scripts have wide ranging potential for use with this library.  
They may be employed as part of the build process, or deployed
with a distribution. 

The ExecutableScript class is used to generate / bundle such scripts. Normally,
this is a batch file on Windows, or a shell script on Linux or Mac.  Notably, 
this is most often used as a "wrapper" over a deployed executable, bundled
with a distribution.  In some contexts, that wrapper mechanism is implicitly
employed by deployment preparing tools the library leans on, and/or is added
directly by distbuilder code. Use of this class allows such to be overridden. 

Constructor:       

	ExecutableScript( rootName, 
					extension=True, shebang=True,                   
                  	script=None, scriptPath=None )
                  
Attributes & default values:    

    rootName <required> 
    extension=True
    shebang=True,                   
    script=None
    scriptPath=None
    
Functions:   

    debug()        
    fileName()
    write( dirPath )
    
Details:

**rootName**: The name of script without the extension.  If this is used
as an "exe/binary wrapper", this name should normally align with the root 
of that binary's name, which may be acquired with `rootFileName( path )`.  

**extension**: The file extension used when creating the file. If `True`,
the extension will be automatically assigned. This defaults to `bat` on 
Windows, `sh` on Mac and Linux.  If set to `None`, there will be no extension
on the file.  A user supplied string will be applied if custom provided.  

**shebang**: A "shebang" injected into the top of the script automatically. 
On Windows, this attribute is not used.  Else, if `True`, `#!/bin/sh` will be used. 
A user supplied string will be applied if custom provided.

**script**: The content for the for script, provided as a string.

**scriptPath**: The content for the for script, provided as a file path
to source for where it is to be extracted.

## Utilities

The following low level "utilities" are also provided for 
convenience, as they maybe useful in defining the build 
parameters, further manipulating the package, or testing 
the results, etc.   

### absPath

    THIS_DIR 
    
The path to the directory which contains the build script. 

    absPath( relativePath, basePath=None )
    
Covert a relative path to an absolute path. If a `basePath` 
is not specified, the path is re resolved relative to `THIS_DIR` 
(which may or **MAY NOT** be the *current working directory*).  

### Copy or Move To Dir

    copyToDir( srcPaths, destDirPath )
    
**Returns**: the destination path(s) to the file(s) / directory(ies).        

Copies files OR directories to a given destination.
The argument srcPaths may be a singular path (i.e. a string)
or an iterable (i.e. a list or tuple). This *replaces* any existing 
copy found at the destination path.  When relative paths are specified,
they are resolved via [absPath](#abspath).
      
    moveToDir( srcPaths, destDirPath )
        
Moves files OR directories to a given destination.
The argument srcPaths may be a singular path (i.e. a string)
or an iterable (i.e. a list or tuple).  (Note: it *moves* the 
path specified, it does not leave a copy of the source). This
*replaces* any existing copy found at the destination path.
When relative paths are specified, they are resolved via [absPath](#abspath).

    copyToDesktop( path )            
	moveToDesktop( path )
    copyToHomeDir( path )   
    moveToHomeDir( path )

Convenience wrapper functions which directly imply the destination.

### removeFromDir 
    
	removeFromDir( subPaths, parentDirPath )

Removes files OR directories from a given directory.
The argument subPaths may be a singular path (i.e. a string)
or an iterable (i.e. a list or tuple).  A `subPath` argument must be 
relative to the `parentDirPath`.
When relative paths are specified for `parentDirPath`, 
they are resolved via [absPath](#abspath).

### renameInDir 

	renameInDir( namePairs, parentDirPath )

Renames files OR directories with a given directory.
The argument namePairs may be a singular tuple (oldName, newName)
or an iterable (i.e. a list or tuple) of such tuple pairs. 
When relative paths are specified for `parentDirPath`, 
they are resolved via [absPath](#abspath).

### collectDirs 

	collectDirs( srcDirPaths, destDirPath ) 
	
Moves a list of directories into a common parent directory.
That parent directory will be created is it does not exist.
When relative paths are specified or `parentDirPath`, 
they are resolved via [absPath](#abspath).

### mergeDirs

	mergeDirs( srcDirPaths, destDirPath, isRecursive=True )
	
Move the contents of a source directory into a target directory, 
over writing the target contents where applicable.
If performed recursively, the destination contents contained 
within a merged sub directory target are all preserved. Otherwise,
the source sub directories replace the target sub directories as
whole units. When relative paths are specified, 
they are resolved via [absPath](#abspath).
        
### normBinaryName
    
	normBinaryName( path, isPathPreserved=False, isGui=False )
	
The "normalized" name of a binary, resolving such for
cross platform contexts.  On Windows, binaries normally end 
in a ".exe" extension, but on other platforms they normally have
no extension.  On macOS, binaries to be launched with a GUI, 
normally have a ".app" extension (vs none when they do not have
a GUI).  That additional logic is applied when `isGui` is `True`. 
When `isPathPreserved` is `True`, the entire path is returned rather 
than only the file name.  When `False` (the default) a full path 
is stripped down to the basename.

### normIconName
    
	normIconName( path, isPathPreserved=False )
	
The "normalized" name of an icon, resolving such for
cross platform contexts.  On Windows, icons end 
in a ".ico" extension, on macOS ".icns" files are used. In Linux, 
there is no fixed standard exactly on icons, since many distros 
are non-gui, and as such Linux binaries do not have icons embedded in them.
For Linux desktops, however, it is common place to use external ".png" files
to create icons which point to binaries. 
When `isPathPreserved` is `True`, the entire path is returned rather 
than only the file name. When `False` (the default) a full path 
is stripped down to the basename.

### getEnv, setEnv, delEnv

	getEnv( varName, default=None )
	setEnv( varName, value )
	delEnv( varName )

Use these functions to retrieve or manipulate environmental variables.

### versionTuple, versionStr

	versionTuple( ver, parts=4 )    
	versionStr( ver, parts=4 )
	
These functions return "version representations" as either tuples
of integers, or as strings delimited by periods respectively (e.g. "1.0.0.0").
Based upon context, either format is commonly used by this library, and
elsewhere.

The `ver` argument may take many forms: a string (Unicode or bytes), 
an integer, a float, a tuple, a list... It must simply use digits for 
each "part" of the version.  Alpha characters are not permitted.

The optional `parts` argument will truncate or pad the return value, so it
has that many elements present in the representation.  4 "parts" is the standard, 
i.e. "Major.Minor.Micro.Build". 
    
### Module import utilities 

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

### halt
	
	halt()
	
Immediately stops execution of the script.
This can be useful for debugging, since it is typical
to the use library for auto generating and purging files
which you might want to inspect along the way. 	 

### printErr, printExc

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

### download

	download( url, saveToPath=None, preserveName=True )
	
**Returns**: the local path to the completed download.

**url**: The url to the file that is to be downloaded.

**saveToPath**: (Optional) The full local path where the file should be downloaded to.
If omitted (or set to `None`), this path will be automatically assigned to one 
within a temp directory.

**preserveName**: (Optional) If `saveToPath` is `None`, this boolean dictates 
whether the original name of the file should be used when saving the file locally.
If set to `False`, the name will be auto assigned to one which does not conflict
with any that already exist. If set to `True`, and the path already exists, the
new download will overwrite the prior file.       	

### Aliased standard python functions
       
        exists                 os.path.exists 
        isFile                 os.path.isfile
        isDir                  exists AND not isFile
        copyFile               shutil.copyFile 
        removeFile             os.remove
        makeDir                os.makedirs
        copyDir                shutil.copytree     
        removeDir              shutil.rmtree
        move                   shutil.move
        rename                 os.rename
        tempDirPath            tempfile.gettempdir()    
        rootFileName			<custom> os.path.splitext of basename 
        baseFileName           os.path.basename         
        dirPath                os.path.dirname
        joinPath               os.path.join
        splitPath              os.path.split
        splitExt               os.path.splitext 
        joinExt 				<custom> inverse of splitExt   
        
### Constants
        
	IS_WINDOWS 
    IS_LINUX 
    IS_MACOS 
    
    PY2
    PY3
    
    THIS_DIR 
        