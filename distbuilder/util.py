# Standard Libraries
from six import PY2, PY3  # @UnusedImport
from sys import argv, stdout, stderr, exit, \
    executable as PYTHON_PATH
from os import system, remove as removeFile, \
    getcwd, chdir, walk, \
    getenv, listdir, makedirs as makeDir, rename # @UnusedImport   
from os.path import exists, isfile as isFile, \
    dirname as dirPath, normpath, realpath, isabs, \
    join as joinPath, split as splitPath, splitext as splitExt, \
    expanduser, \
    basename, pathsep, relpath      # @UnusedImport
from shutil import rmtree as removeDir, move, make_archive, \
    copytree as copyDir, copyfile as copyFile   # @UnusedImport
import platform
from tempfile import gettempdir
from subprocess import Popen, list2cmdline, \
    PIPE, STDOUT
import traceback
from distutils.sysconfig import get_python_lib
import inspect  # @UnusedImport

# -----------------------------------------------------------------------------   
__plat = platform.system()
IS_WINDOWS         = __plat == "Windows"
IS_LINUX           = __plat == "Linux"
IS_MACOS           = __plat == "Darwin"

PY_EXT             = ".py"
PY_DIR             = dirPath( PYTHON_PATH )
SITE_PACKAGES_PATH = get_python_lib()

THIS_DIR           = dirPath( realpath( argv[0] ) )

# Windows 
PY_SCRIPTS_DIR     = joinPath( PY_DIR, "Scripts" ) 

# *Nix
USER_BIN_DIR       = "/usr/bin"
USER_LOCAL_BIN_DIR = "/usr/local/bin"
OPT_LOCAL_BIN_DIR  = "/opt/local/bin"

# Shockingly platform independent 
# (though can vary by os language and configuration...)
DESKTOP_DIR_NAME   = "Desktop"
# Windows Desktop actual resolution key
__CSIDL_DESKTOP_DIRECTORY = 16

# strictly Apple
_MACOS_APP_EXT                     = ".app"
_LAUNCH_MACOS_APP_CMD             = "open"
__LAUNCH_MACOS_APP_NEW_SWITCH      = "-n"
__LAUNCH_MACOS_APP_BLOCK_SWITCH    = "-W"
__INTERNAL_MACOS_APP_BINARY_TMPLT  = "%s/Contents/MacOS/%s"

# icons types across the platforms
_WINDOWS_ICON_EXT = ".ico"
_MACOS_ICON_EXT   = ".icns" 
_LINUX_ICON_EXT   = ".png" 

__NOT_SUPPORTED_MSG = ( "Sorry this operation is not supported " +
                        "this for this platform!" )

# -----------------------------------------------------------------------------  
def run( binPath, args=[], 
         wrkDir=None, isElevated=False, isDebug=False ):
    # TODO: finish isElevated logic (for windows, in debug mode...)    
    binDir, fileName = splitPath( binPath )   
    if wrkDir is None : wrkDir = binDir
    isMacApp = _isMacApp( binPath )
    if isDebug :
        if isMacApp:                
            binPath = __INTERNAL_MACOS_APP_BINARY_TMPLT % (
                  normBinaryName( fileName, isGui=True )
                , normBinaryName( fileName, isGui=False )  
            )                
        cmdList = [binPath]
        if isinstance(args,list): cmdList.extend( args )
        elif args is not None: cmdList.append( args )    
        print( 'cd "%s"' % (wrkDir,) )
        print( list2cmdline(cmdList) )
        p = Popen( cmdList, cwd=wrkDir, shell=False, 
                   stdout=PIPE, stderr=STDOUT, bufsize=1 )
        while p.poll() is None:
            stdout.write( p.stdout.readline() if PY2 else 
                          p.stdout.readline().decode() )
            stdout.flush()
        stdout.write( "\nReturn code: %d\n" % (p.returncode,) )
        stdout.flush()    
    else :     
        if isMacApp:     
            newArgs = [ __LAUNCH_MACOS_APP_NEW_SWITCH
                      , __LAUNCH_MACOS_APP_BLOCK_SWITCH 
                      , fileName
            ]
            if isinstance( args, list ): newArgs.extend( args ) 
            args=newArgs
            binPath = fileName = _LAUNCH_MACOS_APP_CMD
        if isinstance(args,list): args = list2cmdline(args)
        elif args is None: args=""
        elevate = "" if not isElevated or IS_WINDOWS else "sudo"  
        pwdCmd = "" if IS_WINDOWS or isMacApp else "./"
        cmd = ('%s %s%s %s' % (elevate, pwdCmd, fileName, args)).strip()
        _system( cmd, wrkDir )
    
def runPy( pyPath, args=[], isElevated=False ):
    wrkDir, fileName = splitPath( pyPath )
    pyArgs = [fileName]
    if isinstance(args,list): pyArgs.extend( args )
    run( PYTHON_PATH, pyArgs, wrkDir, isElevated, isDebug=False )

__SCRUB_CMD_TMPL = "{0}{1}"
__DBL_QUOTE      = '"'
__SPACE          = ' '
__ESC_SPACE      = '\\ '
if IS_WINDOWS :        
    __BATCH_RUN_AND_RETURN_CMD = ["cmd","/K"] # simply assuming cmd is on the system path... 
    __BATCH_ONE_LINER_TMPLT    = "{0} 1>&2\n" # the newline triggers execution when piped in via stdin
    __BATCH_ESCAPE_PATH_TMPLT  = 'for %A in ("{0}") do @echo %~sA' 
    from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW
    __BATCH_ONE_LINER_STARTUPINFO = STARTUPINFO()
    __BATCH_ONE_LINER_STARTUPINFO.dwFlags |= STARTF_USESHOWWINDOW 

def _system( cmd, wrkDir=None ):
    if wrkDir is not None:
        initWrkDir = getcwd()
        print( 'cd "%s"' % (wrkDir,) )
        chdir( wrkDir  )
    cmd = __scrubSystemCmd( cmd )        
    print( cmd )
    system( cmd ) 
    print('')
    if wrkDir is not None: chdir( initWrkDir )

def __scrubSystemCmd( cmd ):
    """
    os.system is more convenient than the newer subprocess functions
    when the intention is to act as very thin wrapper over the shell. 
    There is just one MAJOR problem with it: 
    If the first character in the command is a quote (to escape a long path
    to the binary you are executing), then the limited (undesirable) parsing 
    built into the function can all fall apart.  So, this scrub function
    solves that...  
    """    
    if not cmd.startswith( __DBL_QUOTE ): return cmd
    cmdParts    = cmd[1:].split( __DBL_QUOTE )
    safeBinPath = _escapePath( cmdParts[0] )
    args        = __DBL_QUOTE.join( cmdParts[1:] ) # (the leading space will remain)
    return __SCRUB_CMD_TMPL.format( safeBinPath, args ) 
                 
def _escapePath( path ):
    if not IS_WINDOWS: return path.replace(__SPACE, __ESC_SPACE)     
    return( path if __SPACE not in path else        
            __batchOneLinerOutput( __BATCH_ESCAPE_PATH_TMPLT.format(path) ) )    

def __batchOneLinerOutput( batch ):
    cmd = __BATCH_ONE_LINER_TMPLT.format( batch )
    p = Popen( __BATCH_RUN_AND_RETURN_CMD, shell=False, 
               startupinfo=__BATCH_ONE_LINER_STARTUPINFO,
               stdin=PIPE, stdout=PIPE, stderr=PIPE )    
    # pipe cmd to stdin, return stderr, minus a trailing newline
    return p.communicate( cmd )[1].rstrip()  
            
# -----------------------------------------------------------------------------
def collectDirs( srcDirPaths, destDirPath ):
    """ Move a list of directories into a common parent directory """
    destDirPath = absPath( destDirPath )    
    if not isDir( destDirPath ): makeDir( destDirPath )
    moveToDir( srcDirPaths, destDirPath )  

def mergeDirs( srcDirPaths, destDirPath, isRecursive=True ):
    if isinstance(srcDirPaths,list) or isinstance(srcDirPaths,tuple):
        for src in srcDirPaths : 
            __mergeDirs( src, destDirPath, isRecursive )
    else: __mergeDirs( srcDirPaths, destDirPath, isRecursive )          
        
def __mergeDirs( srcDirPath, destDirPath, isRecursive=True ):
    """ 
    Move the contents of a source directory into a target directory, 
    over writing the target contents where applicable.
    If performed recursively, the destination contents contained 
    within merged sub directory are all preserved. Otherwise,
    the source sub directories replace the target sub directories. 
    """    
    srcDirPath  = absPath( srcDirPath )
    destDirPath = absPath( destDirPath )    
    if not isDir( destDirPath ): makeDir( destDirPath )
    if not isDir( srcDirPath ): return
    if isRecursive:
        def moveItem( root, item, isSubDir=False ):
            srcPath = joinPath( root, item )                
            destDir = joinPath( destDirPath, 
                                relpath( root, srcDirPath ) )
            if isSubDir and isDir(destDir): return 
            __moveToDir( srcPath, destDir )            
        for root, dirs, files in walk( srcDirPath, topdown=False ):
            for f in files: moveItem( root, f )                
            for d in dirs:  moveItem( root, d, True )        
    else: 
        srcPaths = [ joinPath( srcDirPath, item ) 
                     for item in listdir( srcDirPath ) ]        
        moveToDir( srcPaths, destDirPath )
    removeDir( srcDirPath )

# -----------------------------------------------------------------------------
def copyToDesktop( path ): return __copyToDir( path, _userDesktopDirPath() )
def moveToDesktop( path ): return __moveToDir( path, _userDesktopDirPath() )

def copyToHomeDir( path ): return __copyToDir( path, _userHomeDirPath() )
def moveToHomeDir( path ): return __moveToDir( path, _userHomeDirPath() )

def copyToDir( srcPaths, destDirPath ):
    """ 
    Copy files OR directories to a given destination.
    The argument srcPaths may be a singular path (i.e. a string)
    or an iterable (i.e. list or tuple).  
    """
    if isinstance(srcPaths,list) or isinstance(srcPaths,tuple):
        destList=[]
        for src in srcPaths :
            destList.append( __copyToDir( src, destDirPath ) )
        return destList
    else: return __copyToDir( srcPaths, destDirPath )          

def __copyToDir( srcPath, destDirPath ):        
    """ Copies 1 item (recursively) """
    srcPath     = absPath( srcPath )
    destDirPath = absPath( destDirPath )
    srcTail = basename( normpath(srcPath) )
    destPath = joinPath( destDirPath, srcTail )
    if srcPath == destPath: return
    __removeFromDir( srcTail, destDirPath )
    if isFile( srcPath ): copyFile( srcPath )
    elif isDir( srcPath ): copyDir( srcPath )        
    print( 'Copied "%s" to "%s"' % (srcPath, destPath) )
    return destPath

def moveToDir( srcPaths, destDirPath ):
    """ 
    Move files OR directories to a given destination.
    The argument srcPaths may be a singular path (i.e. a string)
    or an iterable (i.e. list or tuple).  
    """
    if isinstance(srcPaths,list) or isinstance(srcPaths,tuple):
        destList=[]
        for src in srcPaths : 
            destList.append( __moveToDir( src, destDirPath ) )
        return destList
    else: return __moveToDir( srcPaths, destDirPath )          
    
def __moveToDir( srcPath, destDirPath ):        
    """ Moves 1 item (recursively) """
    srcPath     = absPath( srcPath )
    destDirPath = absPath( destDirPath )    
    srcTail = basename( normpath(srcPath) )
    destPath = joinPath( destDirPath, srcTail )
    if srcPath == destPath: return
    __removeFromDir( srcTail, destDirPath )
    move( srcPath, destDirPath )    
    print( 'Moved "%s" to "%s"' % (srcPath, destPath) )
    return destPath

def removeFromDir( subPaths, parentDirPath ):
    """ 
    Removes files OR directories from a given directory.
    The argument subPaths may be a singular path (i.e. a string)
    or an iterable collection (i.e. list or tuple).  
    """
    if isinstance(subPaths,list) or isinstance(subPaths,tuple):
        for subPath in subPaths : __moveToDir( subPath, parentDirPath )
    else: __removeFromDir( subPaths, parentDirPath )          
    
def __removeFromDir( subPath, parentDirPath ):        
    """ Removes 1 item (recursively) """
    parentDirPath = absPath( parentDirPath )   
    remPath = joinPath( parentDirPath, subPath )    
    if isFile( remPath ): 
        removeFile( remPath )
        print( 'Removed "%s"' % (remPath,) )
    elif isDir( remPath ): 
        removeDir( remPath )
        print( 'Removed "%s"' % (remPath,) )

def renameInDir( namePairs, parentDirPath ):
    """ 
    Renames files OR directories in a given destination.
    The argument namePairs may be a singular tuple (oldName, newName)
    or an iterable (i.e. list or tuple) of such tuple pairs.  
    """
    if isinstance(namePairs,list) or isinstance(namePairs,tuple): 
        destList=[]
        for pair in namePairs : 
            destList.append( __renameInDir( pair, parentDirPath ) )
        return destList
    else: return __renameInDir( namePairs, parentDirPath )          
    
def __renameInDir( namePair, parentDirPath ):
    parentDirPath = absPath( parentDirPath )    
    oldName, newName = namePair
    oldPath = joinPath( parentDirPath, oldName )        
    newPath = joinPath( parentDirPath, newName )
    rename( oldPath, newPath )
    print( 'Renamed "%s" to "%s"' % (oldPath, newPath) )
    return newPath

# -----------------------------------------------------------------------------
__IMPORT_TMPLT       = "import %s"
__FROM_IMPORT_TMPLT  = "from %s import %s"
__GET_MOD_PATH_TMPLT = "inspect.getfile( %s )"

def isImportableModule( moduleName ):
    try: __importByStr( moduleName )
    except : return False
    return True

def isImportableFromModule( moduleName, memberName ):
    try: __importByStr( moduleName, memberName )
    except : return False
    return True

def modulePath( moduleName ):
    try: 
        exec( __IMPORT_TMPLT % (moduleName,) ) # cannot use __importByStr as that is outside of the scope!
        return eval( __GET_MOD_PATH_TMPLT % (moduleName,) )
    except Exception as e: 
        printExc( e )
        return None

def modulePackagePath( moduleName ):
    modPath = modulePath( moduleName )
    return None if modPath is None else dirPath( modPath )
    
def sitePackagePath( packageName ):
    packagePath = joinPath( SITE_PACKAGES_PATH, packageName )
    return packagePath if exists( packagePath ) else None

def __importByStr( moduleName, memberName=None ):
    try: 
        if memberName is None : exec( __IMPORT_TMPLT % (moduleName,) )
        else: exec( __FROM_IMPORT_TMPLT % (moduleName, memberName) )
    except Exception as e: printExc( e )

# -----------------------------------------------------------------------------
def toZipFile( sourceDir, zipDest=None, removeScr=True ):
    if zipDest is None :        
        zipDest = sourceDir # make_archive add extension
    else:
        if isFile( zipDest ) : removeFile( zipDest )
        zipDest, _ = splitExt(zipDest)           
    filePath = make_archive( zipDest, 'zip', sourceDir )
    print( 'Created zip file: "%s"' % (filePath,) )    
    if removeScr :         
        removeDir( sourceDir )
        print( 'Removed directory: "%s"' % (sourceDir,) )        
    return filePath
 
# -----------------------------------------------------------------------------   
def normBinaryName( path, isPathPreserved=False, isGui=False ):    
    if not isPathPreserved : path = basename( path )
    base, ext = splitExt( path )
    if IS_MACOS and isGui :
        return "%s%s" % (base, _MACOS_APP_EXT)      
    if IS_WINDOWS: return base + (".exe" if ext=="" else ext)
    return base 
                        
def _normIconName( path, isPathPreserved=False ):    
    if not isPathPreserved : path = basename( path )
    base, _ = splitExt( path )
    if IS_WINDOWS: return "%s%s" % (base, _WINDOWS_ICON_EXT) 
    elif IS_MACOS: return "%s%s" % (base, _MACOS_ICON_EXT) 
    elif IS_LINUX: return "%s%s" % (base, _LINUX_ICON_EXT) 
    raise Exception( __NOT_SUPPORTED_MSG )
    return base 
                        
def _isMacApp( path ): return IS_MACOS and splitExt(path)[1]==".app"

# -----------------------------------------------------------------------------      
def isDir( path ): return exists(path) and not isFile(path)

def absPath( relativePath, basePath=None ):
    if isabs( relativePath ): return relativePath
    if basePath is None: basePath=THIS_DIR        
    return realpath( normpath( joinPath( basePath, relativePath ) ) )

def tempDirPath(): return gettempdir()

# -----------------------------------------------------------------------------                          
def _pythonPath( relativePath ):    
    return normpath( joinPath( PY_DIR, relativePath ) )

def _pythonScriptsPath( relativePath ):    
    return normpath( joinPath( PY_SCRIPTS_DIR, relativePath ) )

def _usrBinPath( relativePath ):    
    return normpath( joinPath( USER_BIN_DIR, relativePath ) )

def _usrLocalBinPath( relativePath ):    
    return normpath( joinPath( USER_LOCAL_BIN_DIR, relativePath ) )

def _optLocalBinPath( relativePath ):    
    return normpath( joinPath( OPT_LOCAL_BIN_DIR, relativePath ) )

def _userHiddenLocalBinDirPath( relativePath ) :
    return normpath( joinPath( "%s/.local/bin" % (_userHomeDirPath(),), 
                               relativePath ) )

def _userHomeDirPath(): return expanduser('~') # works in Windows too!
            
def _userDesktopDirPath():
    if IS_WINDOWS : 
        return __getFolderPathByCSIDL( __CSIDL_DESKTOP_DIRECTORY )
    elif IS_LINUX or IS_MACOS :
        return normpath( joinPath( _userHomeDirPath(), DESKTOP_DIR_NAME ) )
    raise Exception( __NOT_SUPPORTED_MSG )        
            
def __getFolderPathByCSIDL( csidl ):
    import ctypes.wintypes    
    SHGFP_TYPE_CURRENT = 0   # Get current, not default value
    buf = ctypes.create_unicode_buffer( ctypes.wintypes.MAX_PATH )
    ctypes.windll.shell32.SHGetFolderPathW( 
        None, csidl, None, SHGFP_TYPE_CURRENT, buf )
    return buf.value 
            
# -----------------------------------------------------------------------------
def halt(): printErr( "HALT!", isFatal=True )
               
def printErr( msg, isFatal=False ):
    try: stderr.write( str(msg) + "\n" )
    except: 
        try: stderr.write( unicode(msg) + "\n" )  # @UndefinedVariable
        except: stderr.write( "ERROR on: %s\n" % 
                (traceback.format_stack(limit=1)) )
    stderr.flush()        
    if isFatal: exit(1)   

def printExc( e, isDetailed=False, isFatal=False ):
    if isDetailed :
        printErr( repr(e) )
        printErr( "Stack Trace:" )
        printErr( traceback.format_exc() )
    else : printErr( e )
    if isFatal: exit(1)
            
# -----------------------------------------------------------------------------           
