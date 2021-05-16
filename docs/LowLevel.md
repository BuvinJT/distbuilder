# Low Level Classes And Functions 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Stand Alone Executables 

### pyScriptToExe
        
To build a stand-alone binary distribution of a Python
program, invoke the pyScriptToExe function: 

    pyScriptToExe( name=None, entryPointPy=None,
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
        
**pyInstConfig**: An (optional) [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig) 
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
    list of strings containing file/directory 
    names or paths *relative* to the build script
    directory. Else, you may provide a list of two 
    element tuples, with a specific source and 
    destination.  The source path may be either a relative or 
    absolute path on your file system. The (optional) destination 
    path should be specified relative to the package being 
    created. In addition, source paths may be specified with globing *wildcards*
    if desired.  They may even include environmental variables or 
    path symbols e.g. `~` (as would be written 
    in a given platform specific shell).
    Several convenience functions have been provided for building 
    globing patterns. See [Globing pattern builders](#globing-pattern-builders).         
    Regarding the destination argument, note that its default path is
    the root directory of the package, using the same 
    file name as in the source. To package a resource within a *sub directory*, 
    or with an *alternate name*: you must either explicitly provide
    the relative destination path *or* **use the "shortcut value" `True` to 
    indicate the source and destination are the same relative paths**.      
    
**distDirs**: An (optional) list of directories to 
    create within the package.  Note distResources
    implicitly does this for you when there is 
    a source to copy.  This additional option is
    for adding new empty directories.  

### batchScriptToExe

** WINDOWS ONLY**

This function ultimately produces an executable via *IExpress*.

     batchScriptToExe( name=None, entryPointScript=None, 
                       iExpressConfig=None,                                     
                       distResources=None, distDirs=None )

TODO: Fill in

### powerShellScriptToExe  

** WINDOWS ONLY**

     powerShellScriptToExe( name=None, entryPointScript=None, 
                            iExpressConfig=None,                                     
                            distResources=None, distDirs=None )

TODO: Fill in

### vbScriptToExe  

** WINDOWS ONLY**

     vbScriptToExe( name=None, entryPointScript=None, 
                    iExpressConfig=None,                                     
                    distResources=None, distDirs=None )

TODO: Fill in

### jScriptToExe  

** WINDOWS ONLY**

     jScriptToExe( name=None, entryPointScript=None, 
                   iExpressConfig=None,                                     
                   distResources=None, distDirs=None )

TODO: Fill in

### installPyInstaller, uninstallPyInstaller

Distbuilder builds executables from Python source via PyInstaller.  For convenience,
these install/uninstall functions for the tool are provided.  Note, you may install  
a specific version if desired, in this (example) manner:  

	installPyInstaller( version="3.4" )

### PyInstallerVersion, PyInstallerMajorVer, PyInstallerMajorMinorVer

These functions have been provided to help you in circumstances where you need to 
pivot on the specific PyInstaller version installed. `PyInstallerVersion()` returns
the string representation, pulled directly from the library.
`PyInstallerMajorVer()`, just the major version explicitly cast as an integer.     
`PyInstallerMajorMinorVer()`, returns a 2 element tuple with major *and* minor versions
explicitly cast as integers.     

### makePyInstSpec

To generate a PyInstaller .spec file, using the secondary
utility "pyi-makespec" (bundled with PyInstaller), 
invoke the makePyInstSpec function:   

	makePyInstSpec( pyInstConfig, opyConfig=None )

**Returns: the absolute path to the spec file created.
    Also, updates the pyInstConfig argument, supplying 
	a [PyInstSpec](ConfigClasses.md#pyinstspec) object and effectively
	returning it "by reference". 
        
**pyInstConfig**: An [PyInstallerConfig](ConfigClasses.md#pyinstallerconfig) 
    object used to dictate the details for generating 
    the spec file using the makespec Utility.

**opyConfig**: An (optional) [OpyConfig](ConfigClasses.md#opyconfig) object, 
	providing supplemental details regarding the spec file
	creation.  Be sure to include this if you desire obfuscation
	and will be subsequently invoking the pyScriptToExe function.
      	                    
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
 
When the QtIFW utility is required for use by the library 
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
utility was installed. (i.e. the return value of `installQtIfw()`).  If omitted,
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
     by [pyScriptToExe](#pyscripttoexe)), which is source path of the 
     content. 
    
**isSilent**: When `isSilent` is enabled, the QtIFW installer produced will not display 
a GUI or provide any interactive prompts for the user.  All options are dictated by 
command line arguments. While this may certainly be desirable on any platform, it is  
*necessary* to create an installer for a target OS with no GUI (e.g. many Linux distros).
 
See [Silent Installers](#silent-installers) for more information. 

### Standard Installer Arguments

The standard (non silent) QtIFW installer can accept a collection of command line arguments
out of the box.  To see the available options, simply pass the switch `-h` or `--help` 
when executing the installer binary from a terminal.

The distbuilder library, has added a series of additional options as well (assuming the
built-in default Control Script additions are preserved).  Unfortunately,
there does not appear to be a way to add these to the QtIFW help!  Note these differ from the 
[Silent Installer Arguments](#silent-installer-arguments).
**The following custom arguments must be passed in the format "Key=Value"**: 

**outlog=[path]**: The path where you would like output messages written to.  The default is `<temp dir>/installer.out`.
    
**errlog=[path]**: The path where you would like error messages written to.  The default is `<temp dir>/installer.err`.

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

**accept=[true/false]**: Enable the check box for accepting the end user license agreement (if applicable).

**run=[true/false]**: Enable the check box for running the target program at the end of 
the installation (if applicable).

**reboot=[true/false]**: Enable the check box for rebooting the system at the 
end of the installation (if applicable).
       
**onexist=[fail/remove/prompt]**: Define the action taken when an existing (conflicting)
installation is present.  The default is to prompt, and allow for automatic removal if
the user so chooses explicitly.   
    
**mode=[addremove/update/removeall]**: This option is provided for controlling how the 
"Maintenance Tool" is to be run.   

**auto=[true/false]**: Enable "Auto pilot" mode.  This is very much akin to a running the 
installation like a [Silent Installer](#silent-installers), and is in fact at the heart
of how that works. Unlike a silent installer, GUI suppression is involved, however,
and some of the extended features are not available e.g. error return codes.                                                      

**dryrun=[true/false]**: This performs a "dry run" installation, where no
core installation or uninstallation operations are performed,
but Control Scripts are executed.  The wizard quits upon loading the ReadyForInstallation page. This allows for custom coding to 
detect and report error conditions to be fired off, returning their 
results to the client program / shell prior to attempting to use the \
installer. Note: This feature enables "Auto pilot" implicitly.  
Example use cases for this would include having logic embedded in 
the Introduction page to automatically abort the installer if a required 
reboot where detected.  Or, the TargetDirectory page could abort the
installer when in dry run mode if logic were embedded to validate the 
target path (vs displaying a non-fatal error dialog to the user when run 
in the normal interactive mode).  Many other examples could be cited. 
 
**_keeptemp=[true/false]**: DEBUGGING feature: Enable to leave scripts in a temp 
directory, post any dynamic modifications, allowing them to scrutinized / 
executed directly.  This may also be enabled by setting an environmental variable
as `_keeptemp=true`.
 
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

One of the core features of [Silent Installers](#silent-installers) is that they can
be driven by command line arguments.  The following switches have been provided for 
this type of distbuilder installer. Note these differ from the 
[Standard Installer Arguments](#standard-installer-arguments).
             
**-h / --help**: Display help for these arguments.

**-v / --version**: Display version information.

**-l / --license**: Display license agreement(s).

**-y / --dryrun**: Perform a "dry run" installation, where no
core installation or uninstallation operations are performed,
but Control Scripts are executed.  This allows for custom coding to 
detect and report error conditions to be fired off, returning their 
results to the client program / shell prior to attempting to use the \
installer.     
             
**-u / --uninstall**: Uninstall an existing installation (if found) and exit.

**-f / --force**: "Force" installation.  Uninstall an existing installation automatically,
in the event that there is a conflict.  Without this, the installer will abort under such
conditions by default (per the natural QtIFW design).

**-t / --target [path]**: The target directory for the installation.
                         
**-m / --startmenu [relative path]**: (Windows only) The target start menu directory for 
shortcuts.

**-c / --components [ids]**: The full set of components to include in the installation, 
represented as a space delimited list of package ids.  Those ids NOT listed, will not be installed 
(unless they are required or some custom logic added to the Control script forces them to be).  This list takes 
priority over any `include` or `exclude` arguments.

**-i / --include [ids]**: The components to *additionally* include in the installation, 
represented as a space delimited list of package ids.  Required/Default components do NOT need to be listed
here, as they are already included implicitly. 

**-x / --exclude [ids]**: The components to exclude from in the installation, 
represented as a space delimited list of package ids.  Only default components need to be listed
here, as those which not automatically included are implicitly excluded by default.  Attempts exclude a required package will produce an error .  

The component selecting arguments are only made available when more than one
package is defined for the installer.  If there is only a single package, there is not
a needed to select/de-select it!  When these arguments can be used, the `--help` text
will list the package ids and indicate if they are required or default inclusions.  As package ids
are defined in the "Java package" format (e.g. "com.company.product"), and typically 
installers will all have the same long form prefix for all such ids, that prefix will be
truncated for the user's benefit.  So, rather than "com.company.product", the id will become
simply "product".  If any of the packages do not have the same prefix as the rest, they
will all be be listed in the long manner.

**-r / --run**: Run the program automatically post installation.  This option is only made 
available when the installer naturally provides the option to choose this at runtime (i.e. in non-silent mode).  If the option is not exposed to the user normally, it is not exposed 
here.  When available, this is **disabled** by default.  You must explicitly opt to launch 
the program by including this switch.

**-b / --reboot**: Reboot the system automatically post installation, if the installer deems that necessary.  Otherwise, a message should appear on the terminal instructing the user to do this.  This option is only made 
available when the installer naturally provides the option to choose this at runtime (i.e. in non-silent mode).  If the option is not exposed to the user normally, it is not exposed 
here.  When available, this is **disabled** by default.  You must explicitly
opt to allow a reboot by including this switch.

**-o / --outfile**: Output messages from the installer are *always* 
returned to the client via the stdout stream.  When an outfile parameter is 
provided, such messages will *additionally* be written to that path.  If 
using this feature, it is up to the client to purge the file.  Note that an 
"output" file is only produced for "notable" messages.  It does not contain 
verbose debugging details, nor a simple success message.  
Most of the time, such a file will *not* be produced despite specifying 
this argument.  It is only created to pass back important information such 
as a need to reboot your machine.  
    
**-e / --errfile**: Error messages from the installer are *always* returned 
to the client via the stderr stream.  When an errfile parameter is 
provided, such messages will *additionally* be written to that path.  If 
using this feature, it is up to the client to purge the file.  Note that 
the creation of this file by the installer indicates an error occurred.  
Conversely, if the installer completed without creating this file, it 
was successful.  Such as also indicated via an exit code, where zero 
equals success, and any non-zero is an failure. 

**-p / --passthru**: Pass arguments through the silent installer wrapper to the 
QtIFW nested installer core.  To pass key/value pairs, 
use the following example format: 
`MySilentSetup -p "key1='some value' key2='/some/path'"`

**-a / --unpassthru**: Like `--passthru`, but for use with `--uninstall`.  
Pass direct QtIFW arguments to the nested uninstaller launched by the installer.  
Note, if used with `--passthru`, that set of arguments still applies to the 
*installer*, while `--unpassthru` independently applies to the *uninstaller*.   

**-d / --debug**: Enable debugging output. 

**_keeptemp=true**: DEBUGGING feature: Leave scripts in a temp 
directory, post any dynamic modifications, allowing them to scrutinized / 
executed directly.  Enabled by setting an **environmental variable**
as `_keeptemp=true`.

### Installer Variables

The following constants have been provided, which correspond to dynamic variables   
resolved at *runtime* by QtIFW.  Note these are applicable for **BOTH** direct 
[Installer Script](#installer-scripting) generation, and as parameters
and attributes for many higher level functions and objects in this library.   

    QT_IFW_DYNAMIC_VARS <LIST CONTAINING ALL OF THESE>

    QT_IFW_TARGET_DIR
    QT_IFW_DEFAULT_TARGET_DIR 

    QT_IFW_ROOT_DIR 
    
    QT_IFW_HOME_DIR 
    QT_IFW_DESKTOP_DIR

    QT_IFW_APPS_DIR 
    QT_IFW_APPS_X86_DIR
    QT_IFW_APPS_X64_DIR

    QT_IFW_STARTMENU_DIR
    QT_IFW_USER_STARTMENU_DIR
    QT_IFW_ALLUSERS_STARTMENU_DIR
    
    QT_IFW_SCRIPTS_DIR
    QT_IFW_INSTALLER_TEMP_DIR
    QT_IFW_MAINTENANCE_TEMP_DIR
    
    QT_IFW_INSTALLER_DIR 
    QT_IFW_INTALLER_PATH
     
    QT_IFW_PRODUCT_NAME 
    QT_IFW_PRODUCT_VERSION 
    QT_IFW_TITLE 
    QT_IFW_PUBLISHER 
    QT_IFW_URL

    QT_IFW_OS 

Note: use [joinPathQtIfw](#joinpathqtifw) to build paths with such constants. 

### Installer Scripting

While both QtIFW, and the distbuilder additions to it, provide many build-in features
for customizing installers, nothing can provide more open ended flexibility than writing
your own scripts.

QtIFW scripts are written in [Qt Script](https://doc.qt.io/qt-5/qtscript-index.html),
which is essentially [ECMAScript](https://www.ecma-international.org/memento/tc39.htm), 
which is also the base for JavaScript... QtIFW uses a custom 
[QScriptEngine](https://doc.qt.io/qt-5/qscriptengine.html) under the hood, which injects 
additional custom objects and methods for this special context.  To better understand it, and
learn about it's features in more detail, you should refer to the official 
[QtIFW Manual](https://doc.qt.io/qtinstallerframework/index.html).

The classes [QtIfwControlScript](ConfigClasses.md#qtifwcontrolscript) and
[QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript) provide abstraction layers 
for QtIfw script generation. With these classes you can achieve a great many custom 
behaviors, driven by scripts, without having to learn too much about Qt Script, and the
QtIFW specifics. 

#### Python Qt Script Builders

Both of the distbuilder script classes (QtIfwControlScript / QtIfwPackageScript) provide the following **PYTHON** helpers:

Static Constants :

    TAB         
    
    NEW_LINE     
    END_LINE    
    
    START_BLOCK 
    END_BLOCK   
        
    IF    
    ELSE  
    
    TRY   <Note: END_BLOCK required where called for>
    CATCH <Note: END_BLOCK required where called for, exception called "e">
    
    NULL    
    TRUE  
    FALSE 
    
    ASSIGN
      
    NOT 
    EQUAL_TO 
    NOT_EQUAL_TO 
      
    AND 
    OR  

    CONCAT 
    
    EXIT_FUNCTION <I.e.: return;>
        
    PATH_SEP   
    
    MAINTENANCE_TOOL_NAME  
    
    VERBOSE_CMD_SWITCH_ARG     
    TARGET_DIR_KEY
    DEFAULT_TARGET_DIR_KEY         
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
    DRYRUN_CMD_ARG                
    
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
                  
    ifCondition( condition, isNegated=False, isMultiLine=False )
    andList( conditions )
    orList( conditions )
                                                   
	quote( value )
    _autoQuote( value, isAutoQuote )
    _autoEscapeBackSlash( value, isAutoEscape )

	toNull( v )         <convert Python None to QtScript null, else pass through>
	
    toBool( b )         <pass Python bool or dynamic QtScript logic as Python string> 
    boolToString( b )	<pass Python bool or dynamic QtScript logic as Python string>
    stringToBool( value, isAutoQuote=True )
                      
    setValue( key, value, isAutoQuote=True )
    setBoolValue( key, b, isAutoQuote=True )
                   
    lookupValue( key, default="", isAutoQuote=True )
    lookupBoolValue( key, isNegated=False, isHardFalse=False, isAutoQuote=True )            
    lookupValueList( key, defaultList=[], isAutoQuote=True, 
                     delimiter=None )

    ifValueDefined( key, isNegated=False, isMultiLine=False )
    ifBoolValue( key, isNegated=False, isHardFalse=False, isMultiLine=False )
    
    cmdLineArg( arg, default="" )
    cmdLineSwitchArg( arg, isNegated=False, isHardFalse=False )
    cmdLineListArg( arg, default=[] )
    ifCmdLineArg( arg, isNegated=False, isMultiLine=False, )  
    ifCmdLineSwitch( arg, isNegated=False, isHardFalse=False, isMultiLine=False )

    isInstalling( isNegated=False, isMultiLine=False )
    ifInstalling( isMultiLine=False )                      
    isMaintenanceTool( isNegated=False )
    ifMaintenanceTool( isNegated=False, isMultiLine=False )
    
    isAutoPilot( isNegated=False )
    ifAutoPilot( isNegated=False, isMultiLine=False )

    isDryRun( isNegated=False )
    ifDryRun( isNegated=False, isMultiLine=False )

    isElevated()
    ifElevated( isNegated=False, isMultiLine=False )    
    elevate()
    dropElevation() 
                          
    getEnv( varName, isAutoQuote=True )
    
    pathExists( path, isNegated=False, isAutoQuote=True )
    ifPathExists( path, isNegated=False, sAutoQuote=True, isMultiLine=False )   
    
    makeDir( path )            <recursive, path can include native env vars> 
    removeDir( path ) 		   <path can include native env vars>
    	
    writeFile( path, content ) <path can include native env vars>
    deleteFile( path ) 	       <path can include native env vars>	

    assertInternetConnected( isRefresh=False, errMsg=None, isAutoQuote=True )
    isInternetConnected( isRefresh=False ) 
    ifInternetConnected( isRefresh=False, isNegated=False, isMultiLine=False )
       
    isPingable( uri, pings=3, totalMaxSecs=12, isAutoQuote=True )                  
    ifPingable( uri, pings=3, totalMaxSecs=12, isAutoQuote=True,
                isNegated=False, isMultiLine=False )
                        	        
	killAll( exeName, isAutoQuote=True )    
        
    targetDir()
    productName() 
                
    resolveDynamicVars( s, varNames=QT_IFW_DYNAMIC_VARS, <None==QT_IFW_DYNAMIC_VARS> 
                        isAutoQuote=True ) <returns string>
                
    getComponent( name, isAutoQuote=True )	   
    getPageOwner( pageName, isAutoQuote=True ) <returns Component>
		
		<the following are NOT functional in an uninstaller!
		package parameters here can be passed as QtIfwPackage, 
		or the name of such as a raw string ...>
	isComponentInstalled( package )
    ifComponentInstalled( package, isNegated=False, 
                          isAutoQuote=True, isMultiLine=False )   
    isComponentSelected( package )
    ifComponentSelected( package, isNegated=False, 
                         isAutoQuote=True, isMultiLine=False )           
    isComponentEnabled( package, isAutoQuote=True )
    ifComponentEnabled( package, isNegated=False, 
                        isAutoQuote=True, isMultiLine=False )
    enableComponent( package, enable=True, isAutoQuote=True )
        
    debugPopup( msg, isAutoQuote=True )
    warningPopup( msg, isAutoQuote=True )
    errorPopup( msg, isAutoQuote=True )    
    yesNoPopup( msg, title="Question", resultVar="result" )             
    yesNoCancelPopup( msg, title="Question", resultVar="result" )                  
    switchYesNoCancelPopup( msg, title="Question", resultVar="result", 
                            onYes="", onNo="", onCancel="" )
    ifYesNoPopup( msg, title="Question", resultVar="result", 
                 isMultiLine=False )

    quit( msg, isError=True, isSilent=False, isAutoQuote=True )
		<It is not possible to re-enable the user prompt after using these!>
    disableQuit()		<negate with disableQuitPrompt>         
    disableQuitPrompt()         
	
    log( msg, isAutoQuote=True )            

	<Windows Only>   
        
        registryEntryValue( key, valueName, isAutoBitContext=True,
                            isAutoQuote=True )                           
        assignRegistryEntryVar( key, valueName, isAutoBitContext=True,
                                varName="regValue", isAutoQuote=True ) 
        setValueFromRegistryEntry( key, 
                                   regKey, valueName, isAutoBitContext=True,                                    
                                   isAutoQuote=True )                              
                            
        registryEntryExists( key, valueName, isAutoBitContext=True,
                             isAutoQuote=True ) 
        ifRegistryEntryExists( key, valueName, isAutoBitContext=True,
                               isNegated=False, 
                               isAutoQuote=True, isMultiLine=False )       
        registryEntryExistsLike( key, valueNameContains, 
                                 isAutoBitContext=True, 
                                 isCaseSensitive=False, isRecursive=False,
                                 isAutoQuote=True )
        ifRegistryEntryExistsLike( key, valueNameContains, 
                                   isAutoBitContext=True, 
                                   isCaseSensitive=False, isRecursive=False,
                                   isNegated=False, 
                                   isAutoQuote=True, isMultiLine=False )

        registryKeyExists( key, isAutoBitContext=True,
                           isAutoQuote=True ): pass        
        ifRegistryKeyExists( key, isAutoBitContext=True, isNegated=False, 
                             isAutoQuote=True, isMultiLine=False )  
        registryKeyExistsLike( parentKey, childKeyNameContains, 
                               isAutoBitContext=True,
                               isCaseSensitive=False, isRecursive=False,
                               isAutoQuote=True )
        ifRegistryKeyExistsLike( parentKey, childKeyNameContains, 
                                 isAutoBitContext=True, 
                                 isCaseSensitive=False, isRecursive=False,
                                 isNegated=False, 
                                 isAutoQuote=True, isMultiLine=False )        

#### Python QtIfwControlScript Exclusive Builders 
        
In addition, **QtIfwControlScript** provides: 

Static Constants :

    NEXT_BUTTON 
    BACK_BUTTON 
    CANCEL_BUTTON
    FINISH_BUTTON
    
    TARGET_DIR_EDITBOX       
    START_MENU_DIR_EDITBOX   
    ACCEPT_EULA_RADIO_BUTTON 
    RUN_PROGRAM_CHECKBOX     
    FINISHED_MESSAGE_LABEL
    
    	< Applicable / functional on Component Selection Page ONLY!
    	  package parameters here can be passed as QtIfwPackage, 
		  or the name of such as a raw string ... >    	
    selectComponent( package, isSelect=True, isAutoQuote=True )
    selectAllComponents( isSelect=True )
    selectDefaultComponents()

Static Functions:      

    openViaOs( path, isAutoQuote=True )

    currentPageWidget()                
    assignCurrentPageWidgetVar( varName="page" )                              
                   
    pageWidget( pageId )     
    assignPageWidgetVar( pageId, varName="page" )                         

    customPageWidget( pageName )
    assignCustomPageWidgetVar( pageName, varName="page" )               
    
    toDefaultPageId( pageName )
    hideDefaultPage( pageName )
    
    clickButton( buttonName, delayMillis=None )                
    
    enable( controlName, isEnable=True )	
    isEnabled( controlName )
    ifEnabled( controlName, isNegated=False, isMultiLine=False )   

    setVisible( controlName, isVisible=True )
    isVisible( controlName )
    ifVisible( controlName, isNegated=False, isMultiLine=False )   
    
    getText( controlName )
    setText( controlName, text, varNames=None, isAutoQuote=True )
    	(Note: varNames=None==QT_IFW_DYNAMIC_VARS, 
    	       varNames=False==No variable resolution )
    
    	(Note: check box controls also work on radio buttons)    
    isChecked( checkboxName )
    ifChecked( checkboxName, isNegated=False, isMultiLine=False )   
    setChecked( checkboxName, isCheck=True ): <pass Python bool or dynamic QtScript logic>    

    insertCustomWidget( widgetName, pageName, position=None )
    removeCustomWidget( widgetName )
    
	<CUSTOM ("DYNAMIC") PAGES ONLY>	
	    enableNextButton( isEnable=True ) <can't do on standard wizard pages!>				
	    
	    insertCustomPage( pageName, position )
	    removeCustomPage( pageName )
	    
	    setCustomPageTitle( title, isAutoQuote=True, pageVar="page" )     	               
		setCustomPageText( title, description, isAutoQuote=True, pageVar="page" )

	    enableCustom( controlName, isEnable=True, pageVar="page" )
	    isCustomEnabled( controlName, pageVar="page" )
	    ifCustomEnabled( controlName, pageVar="page", isNegated=False, 
	    	             isMultiLine=False )   

	    setCustomVisible( controlName, isVisible=True, pageVar="page" )
	    isCustomVisible( controlName, pageVar="page" )
	    ifCustomVisible( controlName, pageVar="page", isNegated=False, 
	    	             isMultiLine=False )   

	    setCustomText( controlName, text, isAutoQuote=True, pageVar="page" )                
	    getCustomText( controlName, pageVar="page" )

        isCustomChecked( checkboxName, pageVar="page" )
	    setCustomCheckBox( checkboxName, isCheck=True, pageVar="page" )
	    ifCustomChecked( checkboxName, pageVar="page", isNegated=False, 
                         isMultiLine=False )

See [QtIfwUiPage](ConfigClasses.md#qtifwuipage)

#### Raw Qt Script Helpers

If writing scripts directly for distbulder integration, you may also employ the 
following add-on **QT SCRIPT** functions:

    isWindows()
    isMacOs()
    isLinux()

    isElevated()

    isMaintenanceTool()
	
	targetExists()
    removeTarget()
	
	maintenanceToolExists( dir )
	toMaintenanceToolPath( dir )	
    
    Dir.temp()
    Dir.toNativeSparator( path ) 
    Dir.fromNativeSparator( path )

    resolveQtIfwPath( path )		
    resolveNativePath( path )
    
    getEnv( varName )
    
    parentDir( path ) <null if no parent, e.g. path is root>    
    fileName( filePath )
    rootFileName( filePath )
	
	dirList( path, isSortedByTime ) <path can include native env vars, and wild cards>
		
    makeDir( path ) <recursive>
    removeDir( path )
    	
    writeFile( path, content ) <path can include native env vars>
    deleteFile( path ) 	       <path can include native env vars>	
	
	assertInternetConnected( isRefresh[=false], errMsg[=null] )
	isInternetConnected( isRefresh[=false] )
	isPingable( uri, pings[=3], totalMaxSecs[=12] )
	
	resolveDynamicVars( s, varNames )  <returns string>
    replaceDynamicVarsInFile( path, varNames, isDoubleBackslash )
	
	clearErrorLog()
	writeErrorLog( msg )

	sleep( seconds )

    killAll( progName )

	quit( msg, isError, isSilent )
	abort( msg )
	silentAbort( msg )
	
    execute( binPath, args )
    executeDetached( binPath, args ) 
    executeShellCmdDetached( cmd )
	executeHidden( binPath, args, isElevated )
	
	<Windows Only>   
		maintenanceToolPaths()	<resolves via registry lookups>
		isOsRegisteredProgram()	

		registryKeyExists( key, isAutoBitContext )
        registryKeyExistsLike( parentKey, childKeyNameContains, 
                               isAutoBitContext, isCaseSensitive, isRecursive )             

        registryEntryValue( key, valueName, isAutoBitContext )
        registryEntryExists( key, valueName, isAutoBitContext )				
		
		registryEntryExistsLike( key, valueNameContains, 
		                         isAutoBitContext, isCaseSensitive, isRecursive )
		
		executeBatchDetached( scriptPath, bat, args )
		executeVbScript( vbs )
		executeVbScriptDetached( scriptPath, vbs )
		executePowerShell( ps ) 
		executePowerShellDetached( scriptPath, ps ) 
			
		<Package Context Only>
			addVbsOperation( component, isElevated, vbs )
			setShortcutWindowStyleVbs( shortcutPath, styleCode )

    <Linux Only>        
	    isPackageInstalled( pkg )
	    installPackage( pkg ) 
	    unInstallPackage( pkg ) 

	    isPackageManagerInstalled( prog )
	    isAptInstalled() 
	    isDpkgInstalled()
	    isYumInstalled()
	    isRpmInstalled()
	    
		<the following are NOT functional in an uninstaller!>	    
    getComponent( name ) <throws on invalid name, or in any uninstall context>
	isComponentInstalled( name ) 
    isComponentSelected( name ) 
	isComponentEnabled( name )
    enableComponent( name, enable[=true] )

    getPageOwner( pageName ) <throws on invalid name>

	insertCustomWidget( widgetName, pageId, position )
    removeCustomWidget( widgetName )

    insertCustomPage( pageName, position ) 
    removeCustomPage( pageName )     
	setCustomPageText( page, title, description )

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
*srcId* and *destId*.  

"Merging" first of all entails a recursive *content* merge of the source 
into the target via [mergeDirs](#mergedirs).  In addition, a number of
other configuration details will be "merged" as well.  Examples of such
include combining the lists of
[QtIfwShortcut](ConfigClasses.md#qtifwshortcut) objects, 
[QtIfwExternalOp](ConfigClasses.md#qtifwexternalop) objects,  
[QtIfwExternalResource](ConfigClasses.md#qtifwexternalresource) objects,
etc., drilling down in to the [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript)
contained within the packages.  The package scripts are regenerated during a 
subsequent build process to reflect these changes. 
Note that any attributes of the source package, which aren't explicitly 
handled by the library in this operation, will likely be lost!  Some detailed inspection, 
and further customizations to the result, may need to be made post merge for a given 
use case, if the desired effect fails.

Note that if the source package has a `subDirName` attribute, that detail will be preserved.  I.e. the merge will retain the sub directory encapsulation.   

This function ultimately consolidates the package items in the list and returns
the destination object.	

    nestQtIfwPackage( pkgs, childId, parentId, subDirName=None )
    
"Nests" the "child" [QtIfwPackage](ConfigClasses.md#qtifwpackage) 
object within the "parent", modifying the *pkgs* collection supplied.  

"Nesting" entails moving the child *content* into a sub directory of the parent 
as well as combining the [QtIfwShortcut](ConfigClasses.md#qtifwshortcut)
list nested inside the [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript)
objects, followed by script regeneration to reflect that. Note that (most) other
attributes of the source package are lost! Exceptions to that would be dynamically
generated content, e.g. wrapper scripts, which were already added to the content.
Other customizations which need to be made must be applied post merge.

If a `subDirName` value is provided, that will be used to name the nested directory.
If omitted, the child's package name will be used (or a truncated version of that 
if the child and parent share a common package name "prefix"). If the source package 
has a  `subDirName` attribute, that detail will be overridden by this nesting.  I.e.
this will *NOT* nest the content two levels deep.   

This function ultimately consolidates the package items in the list and returns
the destination object.	

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
equivalent to a `.pyc`.  If your end user is in possession of the decryption key, they can run
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
preliminary step to take, prior to running pyScriptToExe, 
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
 
### updatePip

Distbuilder installs libraries via pip.  It is itself, also installed in via the
same means!  While no feature is provided to *fully* uninstall / re-install (since
doing so would break core features of the library), a convenience method to *update*
pip was provided.   
 
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
Note that the path is returned by `pyScriptToExe`, 
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

Note: When `run` employees the debugging feature, it will set
an environmental variable named `DEBUG_MODE` to `1`.  Some contexts
require this in order to allow this mode to work correctly.
You may wish to include your own custom logic within your
program to pivot on this environmental condition as well.

While distbuilder provides convenience constants/methods to determine if you 
running in this context, to avoid any "tight coupling" to the build system within 
your program's source (which may cause build failures in addition to being a 
questionable design choice), you may wish to employ the following code: 

    def isDebug(): 
        try: return isDebug.__CACHE
        except:
        	from os import environ
            isDebug.__CACHE = environ.get("DEBUG_MODE")=="1"
            return isDebug.__CACHE
            
Note: In some contexts, **you will NOT see the debugging output
until the executable has terminated.**
On Windows, this may occur when using debug mode in combination
with `isElevated` enabled, if you are NOT already running 
as an admin. On macOS, this will occur whenever using a "wrapper script" 
(see [QtIfwExeWrapper](ConfigClasses.md#qtifwexewrapper)) over the binary.

Note: some IDE / platform combinations may render this feature 
inoperable due to a conflict with output stream handling 
(e.g. Eclipse/PyDev on Windows), in which case 
simply execute the build script, or the `run` function, from a terminal
outside of the IDE when employing `isDebug`.  

### runPy   

Perhaps most notable, upon creating a Python obfuscation, you may wish the 
to test the success of that operation. The following
was provided with that in mind specifically:    

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

    toZipFile( sourceDir, zipDest=None, removeScr=True,
               isWrapperDirIncluded=False )

**Returns**: the path to the zip file created.         
    
**sourceDir**: the directory to convert to a zip
    (typically the binDir).   
    
**zipDest**: (optional) full path to the zip file to
    be created. If not specified, it will be
    named with same base as the source, and 
    created adjacent to it.          
    
**removeScr**: Option to delete the sourceDir after
    creating the archive. Note this is the 
    default behavior.
                
**isWrapperDirIncluded**: Option to include the outer
"wrapper" directory, or else put the contents on the root of the archive.

### toCabFile

** WINDOWS ONLY **

    toCabFile( sourceDir, zipDest=None, removeScr=True,
               isWrapperDirIncluded=False )

**Returns**: the path to the cabinet file created.         
    
**sourceDir**: the directory to convert to a cab
    (typically the binDir).   
    
**cabDest**: (optional) full path to the cab file to
    be created. If not specified, it will be
    named with same base as the source, and 
    created adjacent to it.          
    
**removeScr**: Option to delete the sourceDir after
    creating the archive. Note this is the 
    default behavior.
                
**isWrapperDirIncluded**: Option to include the outer
"wrapper" directory, or else put the contents on the root of the archive.
                
*TODO: Add git commit/push...*    
                                                                        
## ExecutableScript

Executable scripts have wide ranging potential for use with this library.  
They may be employed as part of the build process, deployed with a 
distribution, or run in an embedded process of some form. 

The ExecutableScript class is used to generate / bundle scripts. By default, 
the script is a batch file on Windows, or a shell script on Linux or Mac.

The class [QtIfwExternalOp](ConfigClasses.md#qtifwexternalop)) optionally 
employs this class to embedded custom installer scripts into it's processes.    

The class [QtIfwExeWrapper](ConfigClasses.md#qtifwexewrapper)) often contains 
a class of his type, used as a "wrapper" over a deployed executable.  In some 
contexts, that wrapper mechanism is implicitly employed by deployment preparing 
tools the library leans on, and/or is added directly by distbuilder.

Class [PyInstHook](ConfigClasses.md#pyinsthook)) is a derived class from 
ExecutableScript. Note that it is a Python script rather than the default type
for a given platform.  

Constructor:       

	ExecutableScript( rootName, 
				  	  extension=True, shebang=True,                   
                  	  script=None, 
                  	  scriptPath=None, scriptDirPath=None,
                  	  replacements={}, isDebug=True )
                  
Attributes & default values:    

    rootName <required> 
    extension=True  # i.e. True==automatic
    shebang=True    # i.e. True==automatic   
    script=None
    scriptDirPath=None
    replacements={}  
    isIfwVarEscapeBackslash=False
    isDebug=True
    
Functions:   
	
	filePath()
    fileName()

    exists( scriptDirPath=None )        
    read( scriptDirPath=None )
    write( scriptDirPath=None )
    remove( scriptDirPath=None )
    
    toLines()        
    fromLines( lines )
    injectLine( injection, lineNo )               
    
    toBase64( toString=False )
    fromBase64( data )
    
    debug()        

Static Functions:

	typeOf( path )
    strToLines( s )
    linesToStr( lines )    

Static Constants:

    SHELL_EXT       
    BATCH_EXT       
    VBSCRIPT_EXT    
    JSCRIPT_EXT     
    POWERSHELL_EXT  
    APPLESCRIPT_EXT 

    SUPPORTED_EXTS <list>
            
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

**script**: The content for the for script, provided as a string, or a list 
(representing lines).

**scriptPath**: The content for the for script, provided to the constructor 
as a file path to source for where it is to be extracted.  Use the 
filePath() function later if you need this apth again.

**scriptDirPath**: Optional. During construction, this may be explicitly defined, 
or left as `None` to imply `THIS_DIR`.  If a `scriptPath` is specified, 
a directory path extracted from that will be used.
On subsequent calls to `read( scriptDirPath )`, `write( scriptDirPath )`, or `remove( scriptDirPath )`, the `scriptDirPath` will be updated if supplied (i.e. `not None`).    

**replacements**: A dictionary of "placeholder" keys and "substitution" values in 
the script.  Place holders must defined in the script with the surrounding brackets,
i.e in the form "{placeholder}". The keys in replacements dictionary should not, however,
include the brackets.  This is similar to the built-in string format function, of course,
but works better in scripts which use brackets for other purposes. 

**isIfwVarEscapeBackslash**: If employing this class within a 
[QtIfwExternalOp](ConfigClasses.md#qtifwexternalop), enabling this
attribute with cause dynamically resolved installer driven paths
to be injected into the script with backslashes doubled up, thereby
escaping them in certain scripting languages / string literal contexts.  

## Code Signing

"Code signing" an executable file is a means to provide proof that a program was 
produced by a party who can be identified and trusted to not install viruses or 
malware on to your PC.  This mechanism may be thought of as a "first line of 
defense" for virus checkers and security tools.  

Explicitly installing a "Trusted Software Publisher Certificate" maybe necessary 
for the digital signature on a file to be validated, if the file was signed by an 
unknown "Certification Authority".  All major operating systems ship with a host 
of standard "CA certs" pre-installed, but will also allow the manual addition of 
such to supplement those included out-of-the-box.  

### signExe

    signExe( exePath, codeSignConfig )

**Returns**: exePath

**exePath**: The path to the executable to be code signed. 

**codeSignConfig**: [CodeSignConfig](ConfigClasses.md#codesignconfig) object

### generateTrustCerts

    generateTrustCerts( certConfig, keyPassword=None, isOverwrite=False )

Creates self-sign certificates and keys.

**Returns**: (CA Cert Path, Key Path)

**certConfig**: [SelfSignedCertConfig](ConfigClasses.md#selfsignedcertconfig)

**keyPassword**: Recommend using the function [getPassword](#getpassword) to 
set this.  
 
**isOverwrite**: Recommend keeping this as `False` in production context, 
and only making `True` is you are certain you want to regenerate existing files. 

### TrustInstallerBuilderProcess

A [PyToBinPackageProcess](HighLevel.md#pytobinpackageprocess) derivative.
Builds an installer based upon a [ConfigFactory](HighLevel.md#configFactory).
That ConfigFactory maybe most easily generated via the convenience function: 

#### trustCertInstallerConfigFactory

    trustCertInstallerConfigFactory( companyTradeName, 
        caCertPath, keyFilePath, keyPassword=None, 
        companyLegalName=None, version=(1,0,0,0), iconFilePath=None,    
        isSilent=False, script=None )  

    
## Module import utilities 

### modulePath

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

### modulePackagePath

    modulePackagePath( moduleName )

Similar to modulePath, but this return the module's 
parent directory.  More often than not, a module 
will have dependencies within the package / library
where it resides. As such, resolving the package path
can be more useful than the specific module.  

### sitePackagePath
   
    sitePackagePath( packageName )

Similar to modulePackagePath, but takes the package
name rather than a module within it AND is specific
to the site packages collection of libraries, rather
than a more universal path resolution.        

### isImportableModule, isImportableFromModule

    isImportableModule( moduleName )
    isImportableFromModule( moduleName, memberName )            
 
Attempts the import, and returns a boolean indication
of success without raising an exception upon failure.  
Like the related functions here, the arguments are 
expected to be strings (not direct references).  
The purpose of this to test for library installation
success, or to preemptively confirm the presence
of dependencies.

### importFromPath

	importFromPath( path, memberName=None )
	
Imports a module, or a select member from it, via the 
explicit path to that script, and returns the reference.
Example:
	
    myFunc = importFromPath( "/path/to/myscript.py", "myFunc" )
    myFunc( someArg )

This can be very useful for cross project integrations where
you want to import modules, or members of them, which are not
part of an installed system library or if they are located in 
a path where a standard import cannot be employed directly.

## Logging

Distbuilder often produces extensive debugging output when running assorted
processes.  It may prove cumbersome, if not impossible, to read through such
from a terminal, or from within an IDE.  In which case, the built in logging
mechanisms can be drawn upon to resolve this.

The easiest way to log the output of distbuilder processes, is to simply
call `startLogging()` at the top of your script.  This will redirect all print
statements, along with the stdout and stderr streams of sub processes, to 
a (default named) log file.  

When logging in the standard manner and an uncaught exception occurs, the 
stack trace for that will appear both in the log, and in the console where the 
script was launched.  

If desired, you may also explicitly create your own
[Logger](#logger) objects and call their functions e.g. 
`write( msg )` directly.  This maybe useful if you wish to split logs across 
multiple files for different parts of a build process.  
Note that only the primary/singleton instance will have implicit stream 
redirections applied though.  So, if there is no multi-threading / parallel processing dimension to your use case, you may alternatively wish use the pattern `stopLogging`...`startLogging( "MyAltLogName" )` to achieve a "split log" result.

### startLogging

    startLogging( name=None, isUniqueFile=False )

Start the primary/singleton logger. 

**name**: If omitted, the name is auto assigned,
based on the entry point script name (e.g. "build").  The Logger name will
dictate the name of the file produced.   

**isUniqueFile**: If this is enabled, the file produced will have a unique  
name, i.e. will have a time stamp suffix.  Else, a prior/existing log (of the
same name) will be overwritten.  

### stopLogging

    stopLogging()

Stop the primary/singleton logger.  Typically, you may omit invoking this 
explicitly.  When the script ends, all open Loggers will be gracefully closed
automatically.  Allowing that to occur "naturally" will also result in a 
message being sent to the console indicating when a script has completed
without an uncaught exception being encountered.       

### log

	log( msg )
	 
Log a message with the primary/singleton logger, **if it is in use**.

### isLogging

    isLogging()

Check if the primary/singleton logger is in use.    

### Logger

Class used for logging messages to files, e.g. debugging details and 
process results.

Constructor:

    Logger( name=None, isUniqueFile=False )
    
Attributes:
   
	name = <client supplied, or auto defined>
	isUniqueFile = False

Object Methods:

    open()
    close()
    
    pause()
    resume()
    
    write( msg )
    toStdout( msg )
    toStderr( msg )

    writeLn( msg )
    toStdoutLn( msg )
    toStderrLn( msg )

	isOpen()
	isPaused()
    filePath() 
	
Static Methods:

	singleton( name=None, isUniqueFile=False )
	isSingletonOpen()

## Utility Functions

The following low level "utilities" are also provided for 
convenience, as they maybe useful in defining the build 
parameters, further manipulating the package, or testing 
the results, etc.   

### absPath

    THIS_DIR 
    
The path to the directory which contains the build script. 

    absPath( relativePath, basePath=None )
    
Convert a relative path to an absolute path. If a `basePath` 
is not specified, the path is re resolved relative to `THIS_DIR` 
(which may or **MAY NOT** be the *current working directory*).  

### homePath, desktopPath

    homePath( relPath=None )
    desktopPath( relPath=None )
    
Convert a relative path to an absolute path, within the current user's
home directory or desktop directory.       

### joinPathQtIfw

Use this function to build paths within QtScript building contexts 
and to supply arguments for QtIFW operations.  
The paths will be joined in a *platform agnostic* manner.  

Note, use `joinPath` to build paths in a *platform specific* manner,
resolved at build time.    

### qtIfwDynamicValue

    qtIfwDynamicValue( name )

Use this function to produce the resolution of dynamic substitution variables 
at runtime, which are utilized by QtIFW operations and scripts in all contexts 
(directly or indirectly) on a target machine.

These values are *often* paths to files or directories on the target, or 
embedded resources in the installer, but may in fact be used for strings 
containing *any* content, which the installer knows how to resolve.  

### qtIfwOpDataPath

	qtIfwOpDataPath( rootFileName )

Use this function, within QtScript building contexts, to produce the resolution 
of dynamic temp paths at runtime, which are utilized by installer operations.
	
### isParentDir 

    isParentDir( parent, child, basePath=None ):

**Returns**: true/false, the parent / child paths specified, exist
and have such a relationship to one another.  The paths maybe
relative or absolute. `basePath` is optionally used for relative paths.
To actually get the parent directory, use `dirPath`.  

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
is stripped down to the base name.

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
is stripped down to the base name.

### normLibName

    normLibName( path, isPathPreserved=False )

The "normalized" name of a library file, resolving such for
cross platform contexts.  On Windows, "library" files end 
in a ".dll" extension, where on macOS and Linux ".so" is employed. 
When `isPathPreserved` is `True`, the entire path is returned rather 
than only the file name. When `False` (the default) a full path 
is stripped down to the base name.

### Globing pattern builders 

The following functions provide pattern strings, containing wild cards. 

	allPathPattern( basePath )
    extPathPattern( ext, basePath=None ) 
    startsWithPathPattern( match, basePath=None )
    endsWithPathPattern( match, basePath=None )
    containsPathPattern( match, basePath=None )	

Note: If the primary (first) argument supplied to any of these is a list, 
the return value is a corresponding list.  Otherwise, a single string 
is returned.   

### getEnv, setEnv, delEnv

	getEnv( varName, default=None )
	setEnv( varName, value )
	delEnv( varName )

Use these functions to retrieve or manipulate environmental variables.

### reserveTempFilePath

    reserveTempFilePath( suffix="", isSplitRet=False )

This is light wrapper over the standard tempfile.mkstemp function, which 
returns a temp file path, but doesn't create it. Thus, with that standard
function it is possible (in theory) for a second process
to create a file at that path before such can be done by the first.  
This customization mitigates that possibility by creating a
0 byte file on the spot, which you may then overwrite.

**Returns** : the file path, optionally split into (dirPath, fileName)
   
**suffix**: If specified, the file name will end with that suffix,
otherwise there will be no suffix.  Note, if the intended suffix is
a file extension, you must include the "." explicitly.

**isSplitRet**: Dictate the optional return value type / format.
    
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

### versionNo, assertMinVer, assertBuilderVer

	versionNo( ver, parts=4, partLen=3 )
	assertMinVer( ver, minVer, parts=4, partLen=3, descr=None )
    assertBuilderVer( ver )
    
Like `versionTuple` and `versionStr`, `versionNo` takes "any" representation 
of a version on under the sun and returns an integer. In addition to specifying 
the number of `parts` in the version, it will be very important to use a valid 
and persistent `partLen` spec.  That is the maximum number of digits to allow 
for use in each part.  This factor exponentially changes the numeric result 
from this function.  

The function `assertMinVer` is provided to raise an exception in the
event of a version (of whatever form and context), not meeting the requirements
for the build process to continue.

For convenience, `assertBuilderVer` is provided to confirm the minimum version 
of **this library**.  It may be useful to start some build scripts in a manner 
resembling the following: 

	from distbuilder assertBuilderVer
	assertBuilderVer( "0.7.8.0" )
  
### embedExeVerInfo

** WINDOWS ONLY**

    embedExeVerInfo( exePath, exeVerInfo )

Set the branding information (e.g. version, copyright, etc.) on an 
executable.
These details can be seen when inspecting the properties of the file.  
This meta info may also be used by other mechanisms in the OS.
    
**Returns**: None (Raising exception on failure)

**exePath**:  Absolute or relative path to the executable file.

**exeVerInfo**: A [WindowsExeVersionInfo](ConfigClasses.md#windowsexeversioninfo) object.   
  
### embedExeIcon

** WINDOWS ONLY**

    embedExeIcon( exePath, iconPath )
    
**Returns**: None (Raising exception on failure)

**exePath**:  Absolute or relative path to the executable file.

**iconPath**: Absolute or relative path to the `.ico` file.   
  
### extractExeIcons

** WINDOWS ONLY**

    extractExeIcons( exePath, targetDirPath )

Extract all the icons contained within an executable.
    
**Returns**: None (Raising exception on failure)

**srcExePath**:  Absolute or relative path to the executable file.

**destDirPath**: Absolute or relative directory path where the icons will be copied.    

### copyExeVerInfo
    
** WINDOWS ONLY**

    copyExeVerInfo( srcExePath, destExePath )

Copy the version / branding information from one exe to another.
    
**Returns**: None (Raising exception on failure)

**srcExePath**:  Absolute or relative path to the executable file 
which contains the information to be copied.

**destExePath**: Absolute or relative path to the executable file 
where the information is to be transferred.
Note, this file must already exist, to receive the branding info, i.e.
this function doesn't create a new exe.

### copyExeIcon

** WINDOWS ONLY**

    copyExeIcon( srcExePath, destExePath, iconName=None )

Copy an embedded icon from one exe to another.
    
**Returns**: None (Raising exception on failure)

**srcExePath**:  Absolute or relative path to the executable file 
which contains the icon to be copied.

**destExePath**: Absolute or relative path to the executable file 
where the icon is to be transferred.
Note, this file must already exist, to receive the icon, i.e.
this function doesn't create a new exe.

**iconName**: If the source exe contains multiple icons, this
argument allows the specification of which one of those is
to be copied.  This maybe figure out manually by first exacting 
the icons.  If none is specified, the "first" icon in an directory
listing will be automatically selected.     
    
### embedManifest

** WINDOWS ONLY**

    embedManifest( exePath, manifestPath )

**Returns**: None (Raising exception on failure)

**exePath**:  Absolute or relative path to the executable file.

**manifestPath**:  Absolute or relative path to a manifest file.

### embedAutoElevation        

** WINDOWS ONLY**

    embedAutoElevation( exePath )

Cause an executable to auto elevate (i.e. request admin priviledges) 
every time it is run, by embedding this requirement for the OS to 
enforce via a manifest.

**Returns**: None (Raising exception on failure)    

**exePath**:  Absolute or relative path to the executable file.

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

### getPassword

    getPassword( isGuiPrompt=True )
    
**Returns**: the password input by the user

**isGuiPrompt**: If enabled, uses the Tk library to drive a gui prompt. 
(Such requires a gui operating system / distro, of course.)
If not enabled, the password input prompt will work via a terminal interface.     

### Aliased standard python functions
       
        exists                 os.path.exists 
        isFile                 os.path.isfile or os.path.islink 
        isDir                  exists AND not isFile
        copyFile               shutil.copyFile 
        removeFile             os.remove
        makeDir                os.makedirs
        copyDir                shutil.copytree     
        removeDir              shutil.rmtree
        move                   shutil.move
        rename                 os.rename
        tempDirPath            tempfile.gettempdir()    
        rootFileName		   <custom> head of os.path.splitext of os.path.basename 
        baseFileName           os.path.basename         
        dirPath                os.path.dirname
        joinPath               os.path.join
        splitPath              os.path.split
        splitExt               os.path.splitext 
        joinExt 			   <custom> inverse of splitExt
        fileExt                <note returns None, rather than "", when there is no extension>  
        
## General Purpose Constants
        
    IS_WINDOWS 
    IS_LINUX 
    IS_MACOS 
    
    PY2
    PY3

    BIT_CONTEXT
    IS_32_BIT_CONTEXT
    IS_64_BIT_CONTEXT

    IS_ARM_CPU
    IS_INTEL_CPU 
    
    THIS_DIR 

    CURRENT_USER
    ALL_USERS
    
    DEBUG_ENV_VAR_NAME
    DEBUG_ENV_VAR_VALUE
            