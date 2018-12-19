# Standard Libraries
from six import PY2, PY3  # @UnusedImport
from sys import argv, stdout, stderr, exit, \
    executable as PYTHON_PATH
from os import system, remove as removeFile, \
    getcwd, chdir, makedirs as makeDir, rename, getenv # @UnusedImport
from os.path import exists, isfile as isFile, \
    dirname as dirPath, normpath, realpath, relpath, \
    join as joinPath, split as splitPath, splitext as splitExt, \
    basename, pathsep      # @UnusedImport
from shutil import rmtree as removeDir, move, make_archive, \
    copytree as copyDir, copyfile as copyFile   # @UnusedImport
import platform
from tempfile import gettempdir
from subprocess import Popen, PIPE, STDOUT, list2cmdline
import traceback
from distutils.sysconfig import get_python_lib
import inspect  # @UnusedImport

THIS_DIR    = dirPath( realpath( argv[0] ) )
IS_WINDOWS  = platform.system() == "Windows"
PY_EXT      = ".py"
SITE_PACKAGES_PATH = get_python_lib()

__IMPORT_TMPLT       = "import %s"
__FROM_IMPORT_TMPLT  = "from %s import %s"
__GET_MOD_PATH_TMPLT = "inspect.getfile( %s )"
    
def isDir( path ): return exists(path) and not isFile(path)

# absolute path relative to the script directory NOT the working directory    
def absPath( relativePath ):    
    return normpath( joinPath( THIS_DIR, relativePath ) )

def tempDirPath(): return gettempdir()

# -----------------------------------------------------------------------------   
def run( binPath, args=[], isDebug=False ):
    wrkDir, fileName = splitPath( binPath )
    if isDebug :
        cmdList = [binPath]
        if isinstance(args,list): cmdList.extend( args )
        else: cmdList.append( args )    
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
        _system( '%s %s' % (fileName, args), wrkDir )
    
def runPy( pyPath, args=[] ):
    wrkDir, fileName = splitPath( pyPath )
    if isinstance(args,list): args = list2cmdline(args)
    _system( '%s %s %s' % (PYTHON_PATH, fileName, args), wrkDir )

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
    destPath = joinPath( _userDesktopDirPath(), 
                         basename( normpath(path) ) )
    if isFile( destPath ): removeFile( destPath )
    elif isDir( destPath ): removeDir( destPath )
    move( path, _userDesktopDirPath() )
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
__CSIDL_DESKTOP_DIRECTORY = 16
            
def _userDesktopDirPath():
    if not IS_WINDOWS : 
        raise Exception( 
            "Sorry this library does not yet support " +
            "this function on this platform!" )        
    return __getFolderPathByCSIDL( __CSIDL_DESKTOP_DIRECTORY )    
            
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
        if ext == "": ext = "exe"
        return base + "." + ext    
    return base 
            