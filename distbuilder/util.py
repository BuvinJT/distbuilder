# Standard Libraries
from six import PY2, PY3  # @UnusedImport
from sys import argv, stdout, stderr, exit, \
    executable as PYTHON_PATH
from os import system, remove as removeFile, \
    getcwd, chdir, makedirs as makeDir, rename, getenv # @UnusedImport
from os.path import exists, isfile as isFile, \
    dirname as dirPath, normpath, realpath, relpath, \
    join as joinPath, split as splitPath, splitext as splitExt, \
    expanduser, \
    basename, pathsep      # @UnusedImport
from shutil import rmtree as removeDir, move, make_archive, \
    copytree as copyDir, copyfile as copyFile   # @UnusedImport
import platform
from tempfile import gettempdir
from subprocess import Popen, PIPE, STDOUT, list2cmdline
import traceback
from distutils.sysconfig import get_python_lib
import inspect  # @UnusedImport

# -----------------------------------------------------------------------------   
IS_WINDOWS         = platform.system() == "Windows"
IS_LINUX           = platform.system() == "Linux"
IS_MACOS           = platform.system() == "Darwin"

PY_EXT             = ".py"
PY_DIR             = dirPath( PYTHON_PATH )
PY_SCRIPTS_DIR     = joinPath( PY_DIR, "Scripts" )
SITE_PACKAGES_PATH = get_python_lib()

USER_BIN_DIR       = "/usr/bin"
USER_LOCAL_BIN_DIR = "/usr/local/bin"
OPT_LOCAL_BIN_DIR  = "/opt/local/bin"

DESKTOP_DIR_NAME   = "Desktop"
THIS_DIR           = dirPath( realpath( argv[0] ) )

__IMPORT_TMPLT       = "import %s"
__FROM_IMPORT_TMPLT  = "from %s import %s"
__GET_MOD_PATH_TMPLT = "inspect.getfile( %s )"

__NOT_SUPPORTED_MSG = ( "Sorry this operation is not supported " +
                        "this for this platform!" )

__CSIDL_DESKTOP_DIRECTORY = 16

# -----------------------------------------------------------------------------      
def isDir( path ): return exists(path) and not isFile(path)

# absolute path relative to the script directory NOT the working directory    
def absPath( relativePath ):    
    return normpath( joinPath( THIS_DIR, relativePath ) )

def tempDirPath(): return gettempdir()

# -----------------------------------------------------------------------------  
def run( binPath, args=[], 
         wrkDir=None, isElevated=False, isDebug=False ):
    # TODO: finish isElevated logic (for windows, in debug mode...)
    binDir, fileName = splitPath( binPath )
    if wrkDir is None : wrkDir = binDir
    if isDebug :
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
        if isinstance(args,list): args = list2cmdline(args)
        elif args is None: args=""
        elevate = "" if not isElevated or IS_WINDOWS else "sudo"  
        pwdCmd = "" if IS_WINDOWS else "./"
        cmd = ('%s %s%s %s' % (elevate, pwdCmd, fileName, args)).strip()
        _system( cmd, wrkDir )
    
def runPy( pyPath, args=[], isElevated=False ):
    wrkDir, fileName = splitPath( pyPath )
    pyArgs = [fileName]
    if isinstance(args,list): pyArgs.extend( args )
    run( PYTHON_PATH, pyArgs, wrkDir, isElevated, isDebug=False )

def _system( cmd, wrkDir=None ):
    if wrkDir is not None:
        initWrkDir = getcwd()
        print( 'cd "%s"' % (wrkDir,) )
        chdir( wrkDir  )
    print( cmd )
    system( cmd ) # synchronous, streams results to the console implicitly
    print('')
    if wrkDir is not None: chdir( initWrkDir )

# -----------------------------------------------------------------------------
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
    
def moveToDesktop( path ):        
    desktopDir = _userDesktopDirPath()
    destPath = joinPath( desktopDir, 
                         basename( normpath(path) ) )
    if isFile( destPath ): removeFile( destPath )
    elif isDir( destPath ): removeDir( destPath )
    move( path, desktopDir )
    print( 'Moved "%s" to "%s"' % (path, destPath) )
    return destPath

# -----------------------------------------------------------------------------           
def printErr( msg, isFatal=False ):
    try: stderr.write( str(msg) + "\n" )
    except: 
        try: stderr.write( unicode(msg) + "\n" )
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
    return normpath( joinPath( "%s/.local/bin" % (_userDirPath(),), 
                               relativePath ) )
    
# -----------------------------------------------------------------------------    
def _toSrcDestPair( pathPair, destDir=None ):
    ''' "Protected" function for internal library uses only '''
    
    isPyInstallerArg = (destDir is None) # private implementation detail
    src = dest = None             
    if( isinstance(pathPair, str) or
        isinstance(pathPair, unicode) ):
        # shortcut syntax - only provide the source,
        # (the destination is relative)
        src = pathPair
    elif isinstance(pathPair, dict) :
        # if a dictionary is provided, use the first k/v pair  
        try : src, dest = pathPair.iteritems().next() 
        except: pass
    else: 
        # a two element tuple (or list) is the expected format
        try : src = pathPair[0] 
        except: pass
        try : dest = pathPair[1] 
        except: pass
    if src is None: return None
    src = normpath( src )
    srcHead, srcTail = splitPath( src )
    if srcHead=="" : 
        srcHead = THIS_DIR
        src = joinPath( srcHead, srcTail )
    if isPyInstallerArg:
        if dest is None: dest = relpath( srcHead )  # relative to cwd                   
    else :
        if dest is None:
            dest = joinPath( relpath( srcHead ), srcTail )         
        dest = normpath( joinPath( destDir, dest ) )                             
    return (src, dest) 
            
# -----------------------------------------------------------------------------           

def _userDirPath(): return expanduser('~')
            
def _userDesktopDirPath():
    if IS_WINDOWS : 
        return __getFolderPathByCSIDL( __CSIDL_DESKTOP_DIRECTORY )
    elif IS_LINUX :
        return normpath( joinPath( _userDirPath(), DESKTOP_DIR_NAME ) )
    raise Exception( __NOT_SUPPORTED_MSG )        
            
def __getFolderPathByCSIDL( csidl ):
    import ctypes.wintypes    
    SHGFP_TYPE_CURRENT = 0   # Get current, not default value
    buf = ctypes.create_unicode_buffer( ctypes.wintypes.MAX_PATH )
    ctypes.windll.shell32.SHGetFolderPathW( 
        None, csidl, None, SHGFP_TYPE_CURRENT, buf )
    return buf.value 
            
def __importByStr( moduleName, memberName=None ):
    try: 
        if memberName is None : exec( __IMPORT_TMPLT % (moduleName,) )
        else: exec( __FROM_IMPORT_TMPLT % (moduleName, memberName) )
    except Exception as e: printExc( e )

def _normExeName( exeName ):    
    base, ext = splitExt( basename( exeName ) )
    if IS_WINDOWS: 
        if ext=="": ext="exe"
        return base + "." + ext
    return base 
            