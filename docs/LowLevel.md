# Low Level Classes And Functions 
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Stand-Alone Executables 

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

**opyConfig**: An (optional) [OpyConfig](#opyconfig) object, 
	providing supplemental details regarding the spec file
	creation.  Be sure to include this if you desire obfuscation
	and will be subsequently invoking the buildExecutable function.
      	                    
## Executable Obfuscation

PyInstaller is a truly amazing utility, but it has a significant
inherent weakness... it is possible reverse engineer the binaries 
it produces to extract the original source code! Distribution Builder 
has a core built-in feature to mitigate this risk for you: *code obfuscation*.

### obfuscatePy
 
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

### obfuscatePyLib

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
    see [PipConfig](#pipconfig) (and perhaps the pip documentation 
    for details).               
    
**opyConfig**: An (optional) [OpyConfig](#opyconfig) object, 
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

### OpyPatch

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

### LibToBundle

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

### createStageDir

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

### buildInstaller

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
     [QtIfwConfigXml](ConfigClasses.md#qtifwconfigxml), 
     [QtIfwPackage](ConfigClasses.md#qtifwpackage),
     [QtIfwPackageXml](ConfigClasses.md#qtifwpackagexml), 
     and [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript).                                  
     Other key attributes include the "pkgName", which is
     the sub directory where your content will be 
     dynamically copied to within the installer, and the 
     "pkgSrcDirPath" (most typically the "binDir" returned 
     by buildExecutable), which is source path of the 
     content. 
    
**isPkgSrcRemoved**: A "convenience" option denoting if the 
    package source content directory should be deleted 
    after successfully building the installer.   

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
*srcId* and *destId*.  "Merging" entails a recurvise 
directory merge of the source into the target via [mergeDirs](#mergeDirs)
as well as combining the [QtIfwShortcut](ConfigClasses.md#qtifwshortcut)    
list nested inside the [QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript)
objects.	
      
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
they are resolved via [absPath](#absPath).
      
    moveToDir( srcPaths, destDirPath )
        
Moves files OR directories to a given destination.
The argument srcPaths may be a singular path (i.e. a string)
or an iterable (i.e. a list or tuple).  (Note: it *moves* the 
path specified, it does not leave a copy of the source). This
*replaces* any existing copy found at the destination path.
When relative paths are specified, they are resolved via [absPath](#absPath).

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
they are resolved via [absPath](#absPath).

### renameInDir 

	renameInDir( namePairs, parentDirPath )

Renames files OR directories with a given directory.
The argument namePairs may be a singular tuple (oldName, newName)
or an iterable (i.e. a list or tuple) of such tuple pairs. 
When relative paths are specified for `parentDirPath`, 
they are resolved via [absPath](#absPath).

### collectDirs 

	collectDirs( srcDirPaths, destDirPath ) 
	
Moves a list of directories into a common parent directory.
That parent directory will be created is it does not exist.
When relative paths are specified or `parentDirPath`, 
they are resolved via [absPath](#absPath).

### mergeDirs

	mergeDirs( srcDirPaths, destDirPath, isRecursive=True )
	
Move the contents of a source directory into a target directory, 
over writing the target contents where applicable.
If performed recursively, the destination contents contained 
within a merged sub directory target are all preserved. Otherwise,
the source sub directories replace the target sub directories as
whole units. When relative paths are specified, 
they are resolved via [absPath](#absPath).
        
### normBinaryName
    
	normBinaryName( path, isPathPreserved=False, isGui=False )
	
The "normalized" name of a binary, resolving such for
cross platform contexts.  On Windows, binaries normally end 
in a ".exe" extension, but on other platforms they normally have
no extension.  On macOS, binaries to be launched with a GUI, 
normally have a ".app" extension (vs none when they do not have
a GUI).  That additional logic is applied when `isGui` is True. 
When `isPathPreserved` is True, the entire path is returned rather 
than only the file name.

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
        dirPath                os.path.dirname
        joinPath               os.path.join
        splitPath              os.path.split
        splitExt               os.path.splitext 
