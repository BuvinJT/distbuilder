import string  # @UnusedImport
from datetime import date
from six import PY2, PY3, string_types, iteritems  # @UnusedImport
from six.moves import urllib
from sys import argv, stdout, stderr, exit, \
    executable as PYTHON_PATH, path as sysPath
from os import system, sep as PATH_DELIM, \
    remove as removeFile, \
    fdopen, getcwd, chdir, walk, environ, devnull, \
    chmod, getenv, listdir, makedirs as makeDir, rename, pardir as PARENT_DIR # @UnusedImport   
from os.path import exists, isfile, islink, \
    dirname as dirPath, normpath, realpath, isabs, \
    join as joinPath, split as splitPath, splitext as splitExt, \
    expanduser, basename as baseFileName, \
    relpath, pathsep      # @UnusedImport
from shutil import rmtree as removeDir, move, make_archive, \
    copytree as copyDir, copyfile as copyFile   # @UnusedImport
import platform
from tempfile import gettempdir, mkstemp, mkdtemp, \
    mktemp  # @UnusedImport
from subprocess import Popen, list2cmdline, check_output, \
    PIPE, STDOUT, CalledProcessError, \
    check_call  # @UnusedImport
try: from subprocess import DEVNULL 
except ImportError: DEVNULL = open(devnull, 'wb')    
import traceback
from distutils.sysconfig import get_python_lib
import inspect  # @UnusedImport
from time import sleep
from struct import calcsize
import base64  # @UnusedImport
from operator import attrgetter, itemgetter # @UnusedImport 
from copy import deepcopy # @UnusedImport

# -----------------------------------------------------------------------------   
__plat = platform.system()
IS_WINDOWS = __plat == "Windows"
IS_LINUX   = __plat == "Linux"
IS_MACOS   = __plat == "Darwin"

__arch = platform.machine()
IS_ARM_CPU   = "arm" in __arch or "aarch" in __arch
IS_INTEL_CPU = not IS_ARM_CPU

BIT_CONTEXT = calcsize('P') * 8
IS_32_BIT_CONTEXT = BIT_CONTEXT==32
IS_64_BIT_CONTEXT = BIT_CONTEXT==64

_NO_USER, ALL_USERS, CURRENT_USER = range(3)

PY_EXT             = ".py"
PY_DIR             = dirPath( PYTHON_PATH )
SITE_PACKAGES_PATH = get_python_lib()

# (client script's dir)
THIS_DIR           = dirPath( realpath( argv[0] ) ) 

__THIS_LIB_DIR     = dirPath( realpath( __file__ ) ) 

PATH_PAIR_DELIMITER=";"
SYS_CMD_DELIM = "&" if IS_WINDOWS else ";"
SYS_CMD_COND_DELIM = "&&"

# Windows 
PY_SCRIPTS_DIR     = joinPath( PY_DIR, "Scripts" ) 

# *Nix
USER_BIN_DIR       = "/usr/bin"
USER_LOCAL_BIN_DIR = "/usr/local/bin"
OPT_LOCAL_BIN_DIR  = "/opt/local/bin"

# Shockingly platform independent 
# (though can vary by os language and configuration...)
DESKTOP_DIR_NAME   = "Desktop"

DEBUG_ENV_VAR_NAME  = "DEBUG_MODE"
DEBUG_ENV_VAR_VALUE = "1"

# strictly Apple
_MACOS_APP_EXT                     = ".app"
_LAUNCH_MACOS_APP_CMD              = "open"
_LAUNCH_MACOS_APP_ARGS_SWITCH      = "--args"
__LAUNCH_MACOS_APP_NEW_SWITCH      = "-n"
__LAUNCH_MACOS_APP_BLOCK_SWITCH    = "-W"
__INTERNAL_MACOS_APP_BINARY_TMPLT  = "%s/Contents/MacOS/%s"

# icons types across the platforms
_WINDOWS_ICON_EXT = ".ico"
_MACOS_ICON_EXT   = ".icns" 
_LINUX_ICON_EXT   = ".png" 

# library types across the platforms
_WINDOWS_LIB_EXT = ".dll" 
_MACOS_LIB_EXT   = ".so" 
_LINUX_LIB_EXT   = ".so" 

__NOT_SUPPORTED_MSG =( 
    "This operation/feature is not supported on the current platform!" )

__SCRUB_CMD_TMPL = "{0}{1}"
__DBL_QUOTE      = '"'
__SPACE          = ' '
__ESC_SPACE      = '\\ '
_NEWLINE         = '\n'
if IS_WINDOWS :
    import ctypes        
    from ctypes import wintypes
    from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW    
    __CSIDL_DESKTOP_DIRECTORY = 16    
    __CSIDL_PROGRAM_FILES     = 38
    __CSIDL_PROGRAM_FILESX86  = 42
    __BATCH_RUN_AND_RETURN_CMD = ["cmd","/K"] # simply assuming cmd is on the system path... 
    __BATCH_ONE_LINER_TMPLT    = "{0} 1>&2\n" # the newline triggers execution when piped in via stdin
    __BATCH_ESCAPE_PATH_TMPLT  = 'for %A in ("{0}") do @echo %~sA'     
    __BATCH_ONE_LINER_STARTUPINFO = STARTUPINFO()
    __BATCH_ONE_LINER_STARTUPINFO.dwFlags |= STARTF_USESHOWWINDOW 
    __SW_SHOWNORMAL=1
    __SW_HIDE=0        
    __SHARED_RET_CODE_PREFIX= "__SHARED_RET_CODE:"
    __SHARED_RET_CODE_TMPLT = __SHARED_RET_CODE_PREFIX + "%d" 

# -----------------------------------------------------------------------------  
def isDebug():
    try: return isDebug.__CACHE
    except:
        isDebug.__CACHE = getEnv( DEBUG_ENV_VAR_NAME ) == DEBUG_ENV_VAR_VALUE
        return isDebug.__CACHE

def run( binPath, args=None, 
         wrkDir=None, isElevated=False, isDebug=False ):
    _run( binPath, args, wrkDir, isElevated, isDebug )
         
def _run( binPath, args=None, 
         wrkDir=None, isElevated=False, 
         isDebug=False, sharedFilePath=None ):
    
    def __printCmd( elevate, binPath, args, wrkDir ):
        cmdList = [elevate, binPath]
        if isinstance(args,list): cmdList.extend( args )
        elif args is not None: cmdList.append( args )    
        print( 'cd "%s"' % (wrkDir,) )
        print( list2cmdline(cmdList) )

    def __printRetCode( retCode ):
        stdout.write( "\nReturn code: %d\n" % (retCode,) )
        stdout.flush()    
    
    if args is None: args=[]
            
    binDir, fileName = splitPath( binPath )   
    if wrkDir is None : wrkDir = binDir
    isMacApp = _isMacApp( binPath )
    
    # Handle elevated sub processes in Windows
    if IS_WINDOWS and isElevated and not __windowsIsElevated():        
        __printCmd( "", binPath, args, wrkDir )
        retCode = __windowsElevated( binPath, args, wrkDir ) # always in debug
        if isDebug and retCode is not None : __printRetCode( retCode )  
        return
    
    # "Debug" mode    
    if isDebug :
        setEnv( DEBUG_ENV_VAR_NAME, DEBUG_ENV_VAR_VALUE )
        if isMacApp:                
            binPath = __INTERNAL_MACOS_APP_BINARY_TMPLT % (
                  normBinaryName( fileName, isGui=True )
                , normBinaryName( fileName, isGui=False )  
            )                
        cmdList = [binPath]
        if isinstance(args,list): cmdList.extend( args )
        elif args is not None: cmdList.append( args )    
        if not IS_WINDOWS and isElevated:
            elevate = "sudo"
            cmdList = [elevate] + cmdList
        else: elevate = ""      
        __printCmd( elevate, binPath, args, wrkDir )        
        sharedFile = ( 
            _WindowsSharedFile( isProducer=True, filePath=sharedFilePath )
            if sharedFilePath else None )
        p = Popen( cmdList, cwd=wrkDir, shell=False, 
                   stdout=PIPE, stderr=STDOUT, bufsize=0,
                   universal_newlines=True )
        while p.poll() is None:
            line = p.stdout.readline()        
            # patch for some funky observed output from a python win service debug,
            # where nulls appeared between every cNULLhNULLaNULLrNULLaNULLcNULLtNULLeNULLrNULL!
            # I doubt anyone would miss nulls in some other context here?    
            line = line.replace( chr(0), '' ) 
            if sharedFile: sharedFile.write( line )
            else:
                stdout.write( line )
                stdout.flush()
        if sharedFile :
            sharedFile.write( __SHARED_RET_CODE_TMPLT % (p.returncode,) )
            sharedFile.close()
        else : __printRetCode( p.returncode )
        delEnv( DEBUG_ENV_VAR_NAME )
        return 
    
    # All other run conditions...    
    if isMacApp:     
        newArgs = [ __LAUNCH_MACOS_APP_NEW_SWITCH
                  , __LAUNCH_MACOS_APP_BLOCK_SWITCH 
                  , fileName
        ]
        if isinstance( args, list ): 
            newArgs.extend( [_LAUNCH_MACOS_APP_ARGS_SWITCH] + args ) 
        args=newArgs
        binPath = fileName = _LAUNCH_MACOS_APP_CMD
    if isinstance(args,list): args = list2cmdline(args)
    elif args is None: args=""
    elevate = "" if not isElevated or IS_WINDOWS else "sudo"  
    if IS_WINDOWS or isMacApp : pwdCmd = ""
    else : pwdCmd = "./" if wrkDir==binDir else ""
    cmd = ('%s %s%s %s' % (elevate, pwdCmd, fileName, args)).strip()
    _system( cmd, wrkDir )
    
def runPy( pyPath, args=None, isElevated=False ):
    wrkDir, fileName = splitPath( pyPath )
    pyArgs = [fileName]
    if isinstance(args,list): pyArgs.extend( args )
    run( PYTHON_PATH, pyArgs, wrkDir, isElevated, isDebug=False )
 
def _system( cmd, wrkDir=None ):
    if wrkDir is not None:
        initWrkDir = getcwd()
        print( 'cd "%s"' % (wrkDir,) )
        chdir( wrkDir )
    cmd = __scrubSystemCmd( cmd )        
    print( cmd )
    system( cmd ) 
    print('')
    if wrkDir is not None: chdir( initWrkDir )

def _isSystemSuccess( cmd, wrkDir=None ):
    if wrkDir is not None: print( 'cd "%s"' % (wrkDir,) )
    print( cmd )
    try:
        print( check_output( cmd, cwd=wrkDir,
                             shell=True, universal_newlines=True ) )
    except CalledProcessError as e:
        print( e.output )
        print( "Failed with exit code: %d" % (e.returncode,) )
        return False
    return True
    
def _subProcessStdOut( cmd, asCleanLines=False, isDebug=False ):
    if isDebug: print( cmd ) 
    stdOut = check_output( cmd )
    if isDebug: print( stdOut )    
    if PY3 : stdOut = stdOut.decode(encoding='windows-1252')
    if asCleanLines :
        lines = stdOut.split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        return lines      
    else : return stdOut.strip()

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

def _normEscapePath( path ): return normpath( path ).replace( "\\", "\\\\" ) 

def __batchOneLinerOutput( batch ):
    cmd = __BATCH_ONE_LINER_TMPLT.format( batch )
    p = Popen( __BATCH_RUN_AND_RETURN_CMD, shell=False, 
               startupinfo=__BATCH_ONE_LINER_STARTUPINFO,
               stdin=PIPE, stdout=PIPE, stderr=PIPE )    
    # pipe cmd to stdin, return stderr, minus a trailing newline
    return p.communicate( cmd )[1].rstrip()  

def __windowsIsElevated():
    return ctypes.windll.shell32.IsUserAnAdmin()==1

# returns  (isRun, retCode, output)            
def __windowsElevated( exePath, args=None, wrkDir=None ):

    def __runElevated( exePath, args, wrkDir, sharedFilePath ):
        verb = "runas"
        pyPath = PYTHON_PATH
        binPathArg = "'%s'" % (_normEscapePath(exePath),)
        argsArg= '[ %s ]' % (','.join(
            ["'%s'" % (_normEscapePath(a),) for a in args]),)
        wrkDirArg="'%s'" % (_normEscapePath(wrkDir),) if wrkDir else "None" 
        isElevatedArg="True"
        isDebugArg="True"        
        sharedFilePathArg = "'%s'" % (_normEscapePath(sharedFilePath),)
        args =( '-c "'
            'from distbuilder import _run;'
            '_run( %s, args=%s, wrkDir=%s, isElevated=%s, '
            'isDebug=%s, sharedFilePath=%s );'            
            '"'
            % ( binPathArg, argsArg, wrkDirArg, isElevatedArg, 
                isDebugArg, sharedFilePathArg ) )
        if PY2:
            verb = unicode(verb)      # @UndefinedVariable
            pyPath = unicode(pyPath)  # @UndefinedVariable
            args = unicode(args)      # @UndefinedVariable          
        hwd = ctypes.windll.shell32.ShellExecuteW( 
            None, verb, pyPath, args, None, __SW_HIDE )
        return int(hwd) > 32 # check if launched elevated    
    
    def __getResults( sharedFilePath ):
        POLL_FREQ_SECONDS = 0.25
        sharedFile = _WindowsSharedFile( isProducer=False, 
                                         filePath=sharedFilePath)        
        retCode = None
        while retCode is None :
            sleep( POLL_FREQ_SECONDS )
            chunk = sharedFile.read()
            if chunk is None: continue
            if __SHARED_RET_CODE_PREFIX in chunk:
                parts = chunk.split( __SHARED_RET_CODE_PREFIX )
                chunk = parts[0]
                try: retCode = int( parts[1] )
                except: retCode = -1                
            stdout.write( chunk ) 
            stdout.flush()                    
        sharedFile.close()    
        return retCode 

    if args is None: args=[]
    sharedFilePath = _reserveTempFile()
    isRun = __runElevated( exePath, args, wrkDir, sharedFilePath )
    retCode = __getResults( sharedFilePath ) if isRun else None
    removeFile( sharedFilePath )
    return retCode

# -----------------------------------------------------------------------------
__PS_OUTPUT_MAJOR_VERSION = [
      'Try{ Write-Host $PSVersionTable.PSVersion.Major }'
    , 'Catch{ Write-Host 1 }'
]

def _runPowerShell( script ): __runPowerShell( script )
def _powerShellOutput( script, asCleanLines=False ): 
    return __runPowerShell( script, isStdOut=True, asCleanLines=asCleanLines )
def __runPowerShell( script, isStdOut=False, asCleanLines=False ):
    if not IS_WINDOWS: _onPlatformErr()
    if isinstance( script, string_types ) or isinstance( script, list ): 
        script = ExecutableScript( "__tempDistbuilderScript", 
                                   extension="ps1", script=script )
    dirPath = tempDirPath()
    script.write( dirPath )    
    cmd =( 'powershell.exe -ExecutionPolicy Bypass -InputFormat None '
           '-File "%s"' % (joinPath( dirPath, script.fileName() ),) )
    if isStdOut: 
        try: sdtOut = _subProcessStdOut( cmd, asCleanLines=asCleanLines )
        finally: removeFromDir( script.fileName(), dirPath )
    else: 
        _system( cmd )        
        removeFromDir( script.fileName(), dirPath )
    if isStdOut: return sdtOut

def _powerShellMajorVersion():
    return int( _powerShellOutput( __PS_OUTPUT_MAJOR_VERSION ) )
    
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
    the source sub directories replace the target sub directories 
    in their entirety. 
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

def copyToDir( srcPaths, destDirPath=None ):
    """ 
    Copy files OR directories to a given destination.
    The argument srcPaths may be a singular path (i.e. a string)
    or an iterable (i.e. a list or tuple).  
    """
    if destDirPath is None : destDirPath=THIS_DIR
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
    srcTail = baseFileName( normpath(srcPath) )
    destPath = joinPath( destDirPath, srcTail )
    if srcPath == destPath: return
    __removeFromDir( srcTail, destDirPath )
    if isFile( srcPath ): copyFile( srcPath, destPath )
    elif isDir( srcPath ): copyDir( srcPath, destPath )        
    print( 'Copied "%s" to "%s"' % (srcPath, destPath) )
    return destPath

def moveToDir( srcPaths, destDirPath=None ):
    """ 
    Move files OR directories to a given destination.
    The argument srcPaths may be a singular path (i.e. a string)
    or an iterable (i.e. a list or tuple).  
    """
    if destDirPath is None : destDirPath=THIS_DIR
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
    srcTail = baseFileName( normpath(srcPath) )
    destPath = joinPath( destDirPath, srcTail )
    if srcPath == destPath: return
    __removeFromDir( srcTail, destDirPath )
    if not isDir( destDirPath ): makeDir( destDirPath )
    move( srcPath, destDirPath )    
    print( 'Moved "%s" to "%s"' % (srcPath, destPath) )
    return destPath

def removeFromDir( subPaths, parentDirPath=None ):
    """ 
    Removes files OR directories from a given directory.
    The argument subPaths may be a singular path (i.e. a string)
    or an iterable collection (i.e. a list or tuple).  
    """
    if parentDirPath is None : parentDirPath=THIS_DIR
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

def renameInDir( namePairs, parentDirPath=None ):
    """ 
    Renames files OR directories in a given destination.
    The argument namePairs may be a singular tuple (oldName, newName)
    or an iterable (i.e. a list or tuple) of such tuple pairs.  
    """
    if parentDirPath is None : parentDirPath=THIS_DIR
    if isinstance(namePairs,tuple) and isinstance(namePairs[0],tuple): 
        namePairs = list(namePairs)
    if isinstance(namePairs,list): 
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
__IMPORT_TMPLT               = "import %s"
__FROM_IMPORT_TMPLT          = "from %s import %s"

__GET_MOD_PATH_TMPLT = "inspect.getfile( %s )"

def _toLibResPath( relPath ): 
    path = joinPath( __THIS_LIB_DIR, relPath )
    return path if exists( path ) else None
   
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

def importFromPath( path, memberName=None ):
    scriptDir, scriptName = splitPath( path )
    moduleName = rootFileName( scriptName )
    sysPath.insert( 0, scriptDir ) 
    if memberName is None : exec( __IMPORT_TMPLT % (moduleName,) )
    else: exec( __FROM_IMPORT_TMPLT % (moduleName, memberName) )
    sysPath.remove( scriptDir )
    return locals()[memberName] if memberName else locals()[moduleName]  

def __importByStr( moduleName, memberName=None ):
    if memberName is None : exec( __IMPORT_TMPLT % (moduleName,) )
    else: exec( __FROM_IMPORT_TMPLT % (moduleName, memberName) )
    
# -----------------------------------------------------------------------------
def toZipFile( sourceDir, zipDest=None, removeScr=True, 
               isWrapperDirIncluded=False ):
    sourceDir = absPath( sourceDir )
    if zipDest is None :        
        zipDest = sourceDir # make_archive adds extension
    else:
        if isFile( zipDest ) : removeFile( zipDest )
        zipDest, _ = splitExt(zipDest)           
    if isWrapperDirIncluded:
        filePath = make_archive( zipDest, 'zip', 
            dirPath( sourceDir ), baseFileName( sourceDir ) )
    else :       
        filePath = make_archive( zipDest, 'zip', sourceDir )
    print( 'Created zip file: "%s"' % (filePath,) )    
    if removeScr :         
        removeDir( sourceDir )
        print( 'Removed directory: "%s"' % (sourceDir,) )        
    return filePath
 
# -----------------------------------------------------------------------------  
def normBinaryName( path, isPathPreserved=False, isGui=False ):
    if path is None : return None    
    if not isPathPreserved : path = baseFileName( path )
    base, ext = splitExt( path )
    if IS_MACOS and isGui :
        return "%s%s" % (base, _MACOS_APP_EXT)      
    if IS_WINDOWS: return base + (".exe" if ext=="" else ext)
    return base 
                            
def normIconName( path, isPathPreserved=False ):
    if path is None : return None    
    if not isPathPreserved : path = baseFileName( path )
    base, _ = splitExt( path )
    if IS_WINDOWS: return "%s%s" % (base, _WINDOWS_ICON_EXT) 
    elif IS_MACOS: return "%s%s" % (base, _MACOS_ICON_EXT) 
    elif IS_LINUX: return "%s%s" % (base, _LINUX_ICON_EXT) 
    raise Exception( __NOT_SUPPORTED_MSG )
    return base 

def normLibName( path, isPathPreserved=False ):
    if path is None : return None    
    if not isPathPreserved : path = baseFileName( path )
    base, _ = splitExt( path )
    if IS_WINDOWS: return "%s%s" % (base, _WINDOWS_LIB_EXT) 
    elif IS_MACOS: return "%s%s" % (base, _MACOS_LIB_EXT) 
    elif IS_LINUX: return "%s%s" % (base, _LINUX_LIB_EXT) 
    raise Exception( __NOT_SUPPORTED_MSG )
    return base 
                        
def _isMacApp( path ):
    if path is None : return False 
    return IS_MACOS and splitExt(path)[1]==".app"

def _macAppBinaryPath( appPath ):
    return __INTERNAL_MACOS_APP_BINARY_TMPLT % ( appPath, rootFileName( appPath ) )

# ----------------------------------------------------------------------------- 
def rootFileName( path ): 
    if path is None : return None
    return splitExt(baseFileName(path))[0]

def fileExt( path ): 
    if path is None : return None
    ext = splitExt(path)[1]
    return None if ext=="" else ext

def joinExt( rootName, extension=None ):
    if isinstance( rootName, tuple ): rootName, extension = rootName
    if rootName is None : return None
    if extension is None: return rootName 
    if rootName.endswith("."): rootName=rootName[:-1]
    if extension.startswith("."): extension=extension[1:]
    return "%s.%s" % ( rootName, extension )

def isFile( path ): # declaring any symbolic link to be a file! 
    return path is not None and (isfile( path ) or islink( path ))        

def isDir( path ): 
    return path is not None and exists( path ) and not isFile( path )

def isParentDir( parent, child, basePath=None ):
    if parent.endswith( PATH_DELIM ): parent=parent[:-1]
    if child.endswith(  PATH_DELIM ): child=child[:-1]
    child  = absPath( child,  basePath )
    parent = absPath( parent, basePath )
    return child.startswith( parent ) and child != parent  

def absPath( relativePath, basePath=None ):
    if relativePath is None : return None
    if isabs( relativePath ): return relativePath
    if basePath is None: basePath=THIS_DIR        
    return realpath( normpath( joinPath( basePath, relativePath ) ) )

def toNativePath( path ): 
    return path.replace("/","\\") if IS_WINDOWS else path.replace("\\","/")
    
def tempDirPath(): return gettempdir()

def _reserveTempDir( suffix="" ): return mkdtemp( suffix )

# mktemp returns a temp file path, but doesn't create it.
# Thus, it is possible in theory for a second process
# to create a file at that path before such can be done
# by the first.  This mitigates that possibility...   
def _reserveTempFile( suffix="" ):
    fd, path = mkstemp( suffix )
    with fdopen( fd, 'w' ) as _: pass
    return path

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
        home = _userHomeDirPath()
        desktop = normpath( joinPath( home, DESKTOP_DIR_NAME ) )
        return desktop if isDir(desktop) else home
    raise Exception( __NOT_SUPPORTED_MSG )        

def _winProgsDirPath(): 
    if not IS_WINDOWS : _onPlatformErr()
    return __getFolderPathByCSIDL( __CSIDL_PROGRAM_FILES )

def _winProgs86DirPath(): 
    if not IS_WINDOWS : _onPlatformErr()
    return( _winProgsDirPath() if IS_32_BIT_CONTEXT else 
            __getFolderPathByCSIDL( __CSIDL_PROGRAM_FILESX86 ) )
            
def __getFolderPathByCSIDL( csidl ):
    SHGFP_TYPE_CURRENT = 0   # Get current, not default value
    buf = ctypes.create_unicode_buffer( wintypes.MAX_PATH )
    ctypes.windll.shell32.SHGetFolderPathW( 
        None, csidl, None, SHGFP_TYPE_CURRENT, buf )
    return buf.value 

# -----------------------------------------------------------------------------
def _toSrcDestPair( pathPair, destDir=None, basePath=None ):
    #print( "_toSrcDestPair: pathPair=%s, destDir=%s, basePath=%s" % (pathPair, destDir, basePath) )
    
    src = dest = None             
    if isinstance( pathPair, string_types ):  
        # string pair representation
        if PATH_PAIR_DELIMITER in pathPair:
            pathPair = pathPair.split( PATH_PAIR_DELIMITER )
            try : src = pathPair[0].strip() 
            except: pass
            try : dest = pathPair[1].strip() 
            except: pass
        # shortcut syntax - only provide the source,
        # (the destination is relative)        
        else: src = pathPair
    elif isinstance( pathPair, dict ) :
        # if a dictionary is provided, use the first k/v pair  
        try : src, dest = iteritems( pathPair ).next() 
        except: pass
    else: 
        # a two element tuple (or list) is the expected src/dest format
        try : src = pathPair[0] 
        except: pass
        try : dest = pathPair[1] 
        except: pass
    
    if src is None: return None
    src = normpath( src )
    if dest==True : # True=="same"
        if not isabs(src): dest = src 
        else: 
            raise Exception( "A resource destination cannot be the same "
                             "as an ABSOLUTE source path" )
    elif dest is not None: dest = normpath( dest )
    
    relSrcDir = basePath if basePath else THIS_DIR  
    srcHead, srcTail = splitPath( src )

    # NOTE: for a relative source path to have a **nested** destination 
    # path, the destination MUST be explicitly provided                     
    if srcHead=="" or not isParentDir( relSrcDir, srcHead ):
        srcHead = relSrcDir                                
        src = absPath( src, basePath )

    if destDir is None: # (i.e. PyInstaller Argument)
        if dest is None: dest = relpath( srcHead, THIS_DIR )                    
    else :
        if dest is None: dest = srcTail         
        if dest.startswith( PATH_DELIM ) : 
            # must remove a leading slash from dest for joinPath to 
            # make the dest a child of destDir
            try: dest=dest[1:]
            except: pass
        dest = absPath( joinPath( destDir, dest ), relSrcDir )

    #print( "result: src=%s, dest=%s" % (src, dest) )
    return (src, dest) 

# -----------------------------------------------------------------------------    
def versionTuple( ver, parts=4 ): return tuple( __versionList( ver, parts ) )
                
def versionStr( ver, parts=4 ): 
    verList = __versionList( ver, parts )
    verList = [str(p) for p in verList]
    return ".".join( verList )

def versionNo( ver, parts=4, partLen=3 ):
    verList = __versionList( ver, parts )    
    ret = 0
    i = (parts-1) * partLen
    for part in verList:
        ret += (10**i) * part
        if i==0: break
        i-=partLen
    return ret

def assertMinVer( ver, minVer, parts=4, partLen=3, descr=None ):
    if versionNo( ver, parts, partLen ) < versionNo( minVer, parts, partLen ):
        raise RuntimeError( "%sversion %s is required, but %s is present" % 
            (descr + " " if descr else "", 
             versionStr( minVer, parts ), versionStr( ver, parts ) ) )   

def __versionList( ver, parts=4 ):        
    try:
        if isinstance( ver, string_types ):                 
            ver = ver.replace(",",".").replace(" ","").replace("(","").replace(")","")
            verList = ver.split(".")
        elif isinstance(ver, tuple): verList = list(ver)
        elif isinstance(ver, list): verList = ver
        else: verList = str(ver).split(".")
        verList = [int(p) for p in verList]        # convert all parts to ints or raise an exception
        verList.extend( [0]*(parts-len(verList)) ) # rpad with 0s as needed
        verList = verList[:parts]                  # truncate to size as needed
    except:
        printErr( "WARNING: version malformed or not defined!" ) 
        verList = [0]*parts
    return verList

# -----------------------------------------------------------------------------
def getEnv( varName, default=None ): return environ.get( varName, default )

def setEnv( varName, value ): environ[ varName ] = value
 
def delEnv( varName ):
    environ[ varName ] = "" 
    try: del environ[ varName ]
    except: pass        
    
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

def _onPlatformErr(): raise Exception( __NOT_SUPPORTED_MSG )
            
# -----------------------------------------------------------------------------           
def download( url, saveToPath=None, preserveName=True ):
    print( "Downloading: %s..." % (url,) )
    download._priorPct = 0
    def __ondownLoadProgress( blockCount, blockSize, fileSize ):
        if fileSize != -1: 
            pct = int(100 * ((blockCount*blockSize) / fileSize))
            if pct - download._priorPct >= 10 :
                download._priorPct = pct 
                stdout.write( "Done!\n" if pct==100 else 
                              "{0}%...".format( pct ) )
                stdout.flush() 
    if saveToPath is None and preserveName:
        downloadDir = tempDirPath()
        downloadName = baseFileName( urllib.parse.urlsplit( url )[2] )
        removeFromDir( downloadName, downloadDir )            
        saveToPath = joinPath( downloadDir, downloadName )
    localPath, _ = urllib.request.urlretrieve( url, saveToPath, 
                                               __ondownLoadProgress )
    print( "Saved to: %s" % (localPath,) )    
    return localPath

def _isLocalPath( path ):
    scheme,_,path,_,_ = urllib.parse.urlsplit( path )
    isLocal = scheme=="file" or scheme=="" 
    return isLocal, path 
# -----------------------------------------------------------------------------            

class PlasticFile:

    def __init__( self, filePath=None, content=None ) :
        self.filePath = filePath
        if content: self.content = content
        elif filePath and isFile(filePath): self.read()
        self.isInjected = False
    
    def __str__( self ): return self.content if self.content else ""  

    def debug( self ): print( str(self) )
    
    def path( self ): return self.filePath
    
    def read( self ):
        self.content = None        
        with open( self.path(), 'r' ) as f : self.content = f.read() 
            
    def write( self ):
        with open( self.path(), 'w' ) as f : f.write( str(self) )
                
    def toLines( self ):        
        return self.content.split( '\n' ) if self.content else []
    
    def fromLines( self, lines ): self.content = '\n'.join( lines )

    def injectLine( self, injection, lineNo ):               
        lines = self.toLines()            
        if lineNo : lines.insert( lineNo-1, injection )
        else : lines.append( injection )
        self.fromLines( lines )
        self.isInjected = True

# -----------------------------------------------------------------------------            
class WindowsExeVersionInfo( PlasticFile ):

    __TEMP_FILE_NAME = "win_exe_ver_info.tmp"
    
    __FILE_TEMPLT = ( 
"""
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(VER_MAJOR, VER_MINOR, VER_PATCH, VER_BUILD),
    prodvers=(VER_MAJOR, VER_MINOR, VER_PATCH, VER_BUILD),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'COMPANY_NAME'),
        StringStruct(u'FileDescription', u'PRODUCT_DESCR'),
        StringStruct(u'FileVersion', u'VER_MAJOR.VER_MINOR.VER_PATCH.VER_BUILD'),
        StringStruct(u'InternalName', u'PRODUCT_NAME_INTERNAL'),
        StringStruct(u'LegalCopyright', u'COPYRIGHT'),
        StringStruct(u'OriginalFilename', u'EXE_NAME'),
        StringStruct(u'ProductName', u'PRODUCT_NAME'),
        StringStruct(u'ProductVersion', u'VER_MAJOR, VER_MINOR, VER_PATCH, VER_BUILD')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
)
    
    @staticmethod
    def defaultPath(): return absPath( WindowsExeVersionInfo.__TEMP_FILE_NAME )

    def __init__( self ) :
        self.major = 0
        self.minor = 0
        self.micro = 0
        self.build = 0
        self.companyName = ""
        self.productName = ""
        self.description = ""
        self.exeName     = ""

    def __str__( self ):
        s = WindowsExeVersionInfo.__FILE_TEMPLT
        s = s.replace( "VER_MAJOR", str(self.major) )
        s = s.replace( "VER_MINOR", str(self.minor) )
        s = s.replace( "VER_PATCH", str(self.micro) )
        s = s.replace( "VER_BUILD", str(self.build) )                
        s = s.replace( "COPYRIGHT", self.copyright() )
        s = s.replace( "PRODUCT_NAME_INTERNAL", self.internalName() )                
        s = s.replace( "COMPANY_NAME",  self.companyName )        
        s = s.replace( "PRODUCT_NAME",  self.productName )
        s = s.replace( "PRODUCT_DESCR", self.description )
        s = s.replace( "EXE_NAME", normBinaryName( self.exeName ) )                
        return s 

    def path( self ): return WindowsExeVersionInfo.defaultPath()  
    
    # block these on this derivative of PlaticFile
    def read( self ): pass
    def toLines( self ): pass      
    def fromLines( self, lines ): pass
    def injectLine( self, injection, lineNo ): pass   

    def copyright( self ): 
        return "Copyright \\xa9 %d, %s. All rights reserved." % ( 
            date.today().year,
            (self.companyName[:-1] if self.companyName.endswith(".") else
             self.companyName) )
    
    def internalName( self ): 
        return self.productName.lower().replace( " ", "_" )                 

    def version( self, isCommaDelim=False ): 
        ver = versionStr(
            [self.major, self.minor, self.micro, self.build] )
        return ver.replace( ".", "," ) if isCommaDelim else ver
    
# -----------------------------------------------------------------------------            
class ExecutableScript(): # Roughly mirrors PlasticFile, but would override all of it   
    
    __WIN_DEFAULT_EXT = "bat" 
    __NIX_DEFAULT_EXT = "sh"
    
    __NIX_DEFAULT_SHEBANG = "#!/bin/sh"
    __SHEBANG_TEMPLATE = "%s\n%s"

    __PLACEHOLDER_TMPLT = "{%s}" 
    
    @staticmethod
    def strToLines( s ): return s.split( _NEWLINE  ) if s else []
    
    @staticmethod
    def linesToStr( lines ): return _NEWLINE.join( lines )    

    # ExecutableScript
    def __init__( self, rootName, 
                  extension=True, # True==auto assign, str==what to use, or None
                  shebang=True, # True==auto assign, str==what to use, or None                  
                  script=None, scriptPath=None,
                  replacements=None ) :
        self.rootName = rootName
        if extension==True:
            self.extension = ( ExecutableScript.__WIN_DEFAULT_EXT 
                if IS_WINDOWS else ExecutableScript.__NIX_DEFAULT_EXT )
        elif extension==False: self.extension = None
        else: self.extension = extension    
        if shebang==True and scriptPath is None :
            self.shebang =( None if IS_WINDOWS else 
                            ExecutableScript.__NIX_DEFAULT_SHEBANG ) 
        else: self.shebang = shebang            
        if scriptPath:
            with open( scriptPath, 'r' ) as f: self.script = f.read()
        elif isinstance( script, list ): self.fromLines( script )
        else: self.script = script
        self.replacements=replacements if replacements else {}  
        self.isIfwVarEscapeBackslash = False
                                                    
    def __str__( self ) :
        if self.script is None : ""
        if self.shebang:
            return( ExecutableScript.__SHEBANG_TEMPLATE % 
                    (self.shebang, self.__formated()) )
        else: return self.__formated() 
        
    def __formated( self ):
        script = self.script     
        for k,v in iteritems( self.replacements ):
            script = script.replace( self.__PLACEHOLDER_TMPLT % (k,), str(v) )
        return script    
                
    def debug( self ): 
        if self.script: print( str(self) )
        
    def fileName( self ):
        return joinExt( self.rootName, self.extension )
                        
    def write( self, dirPath ):
        if self.script is None : return
        if not isDir( dirPath ): makeDir( dirPath )
        filePath = joinPath( dirPath, self.fileName() )
        print("Writing script: %s\n\n%s\n" % (filePath,str(self)) )                               
        with open( filePath, 'w' ) as f: f.write( str(self) ) 
        if not IS_WINDOWS : chmod( filePath, 0o755 )
        
    def read( self, dirPath ):
        self.script = None        
        filePath = joinPath( dirPath, self.fileName() )
        with open( filePath, 'r' ) as f : self.script = f.read() 
                
    def toLines( self ): return ExecutableScript.strToLines( self.script )
    
    def fromLines( self, lines ): 
        self.script = ExecutableScript.linesToStr( lines )

    def injectLine( self, injection, lineNo ):               
        lines = self.toLines()            
        if lineNo : lines.insert( lineNo-1, injection )
        else : lines.append( injection )
        self.fromLines( lines )
        
    def toBase64( self, toString=False ):
        ret = base64.b64encode( str(self).encode('utf-8') )
        return ret.decode('utf-8') if toString else ret

    def fromBase64( self, data ):
        self.script = base64.b64decode( data ).decode('utf-8')
        self.shebang = None 
        # TODO: resolve shebang programmatically, and remove it from self.script        
        
# -----------------------------------------------------------------------------           
if IS_WINDOWS :
    class _WindowsSharedFile:
        
        __byref        = ctypes.byref
        __DWORD        = wintypes.DWORD
        __CreateFileW  = ctypes.windll.Kernel32.CreateFileW
        __CloseHandle  = ctypes.windll.Kernel32.CloseHandle
        __WriteFile    = ctypes.windll.Kernel32.WriteFile
        __ReadFile     = ctypes.windll.Kernel32.ReadFile
        __GetLastError = ctypes.windll.Kernel32.GetLastError       
        
        __GENERIC_READ         = 0x80000000 
        __GENERIC_WRITE        = 0x40000000 
        __FILE_SHARE_READ      = 0x00000001 
        __FILE_SHARE_WRITE     = 0x00000002 
        __CREATE_ALWAYS        = 2 
        __OPEN_EXISTING        = 3 
        __INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value
        __DEFAULT_CHUNK_SIZE   = 1024
             
        def __init__( self, isProducer=True, filePath=None ) :
            self.isProducer = isProducer 
            self.filePath = filePath # using "hidden" file stream to mitigate data visibility 
            self.chunkSize = _WindowsSharedFile.__DEFAULT_CHUNK_SIZE
            if isProducer :
                if self.filePath is None: self.filePath = mktemp()
                dwDesiredAccess = _WindowsSharedFile.__GENERIC_WRITE  
                dwCreationDisposition = _WindowsSharedFile.__CREATE_ALWAYS
            else :
                if not isFile( self.filePath ) :
                    raise Exception( "Shared file does not exist: %s" 
                                     % (self.filePath,) )
                dwDesiredAccess = _WindowsSharedFile.__GENERIC_READ
                dwCreationDisposition = _WindowsSharedFile.__OPEN_EXISTING            
            self.__handle = _WindowsSharedFile.__CreateFileW(
               unicode(self.filePath) if PY2 else self.filePath,    # @UndefinedVariable            
               dwDesiredAccess,   
               _WindowsSharedFile.__FILE_SHARE_READ | 
               _WindowsSharedFile.__FILE_SHARE_WRITE, # allow concurrent r/w by another process (it seems that both must be enabled for cross process concurrent access)
               None,            # security attributes
               dwCreationDisposition,
               0,               # additional flags
               None             # template file handle
            )
            if not self.isOpen():
                raise Exception( "Cannot open %s" % (self.filePath,) )        
    
        def isOpen( self ):
            return self.__handle != _WindowsSharedFile.__INVALID_HANDLE_VALUE
                   
        def close( self ):
            if not self.isOpen: return
            _WindowsSharedFile.__CloseHandle( self.__handle )
            self.__handle = _WindowsSharedFile.__INVALID_HANDLE_VALUE
    
        def remove( self ):
            self.close()
            if isFile( self.filePath ): removeFile( self.filePath )
                                            
        def write( self, data ):
            if not self.isProducer or not self.isOpen():
                raise Exception( "Cannot write to shared file" ) 
            if PY3: data=str(data).encode()
            bytesToWrite = _WindowsSharedFile.__DWORD( len(data) ) 
            bytesWritten = _WindowsSharedFile.__DWORD()
            _WindowsSharedFile.__WriteFile( 
                self.__handle, data, bytesToWrite,
                _WindowsSharedFile.__byref(bytesWritten), None )       
            if bytesToWrite.value != bytesWritten.value : 
                raise Exception( "Error writing to shared file" ) 
    
        def read( self ):
            if self.isProducer or not self.isOpen():
                raise Exception( "Cannot read from shared file" )         
            data = ""
            chunk = ctypes.create_string_buffer( self.chunkSize )
            bytesToRead = _WindowsSharedFile.__DWORD( self.chunkSize ) 
            bytesRead   = _WindowsSharedFile.__DWORD()            
            while True:
                _WindowsSharedFile.__ReadFile( self.__handle,  
                    _WindowsSharedFile.__byref(chunk), bytesToRead,
                    _WindowsSharedFile.__byref(bytesRead), None )  
                if bytesRead.value==0: break
                #data += ( eval("%s.decode()" % (chunk.value.decode(),)) 
                #          if PY3 else chunk.value )
                data += chunk.value.decode() if PY3 else chunk.value                            
            return None if data=="" else data
    
# ----------------------------------------------------------------------------- 
if IS_MACOS :
    
    def _isDmg( filePath ):    
        try: return splitExt( filePath )[1].lower() == ".dmg"
        except : return False
        
    # returns: isNewMount, mountPath, appPath (or None),  binPath (or None) 
    def _macMountDmg( dmgPath ):    
        def _toRet( isNew, mountPath, appPath, binPath ): 
            return ( isNew, mountPath,
                appPath if isFile( appPath ) else None, 
                binPath if isFile( binPath ) else None )
        #example mount path:
        #   /Volumes/QtInstallerFramework-mac-x64/QtInstallerFramework-mac-x64.app/Contents/MacOS/QtInstallerFramework-mac-x64              
        dmgBaseName = splitExt( baseFileName( dmgPath ) )[0]
        mountPath = joinPath( PATH_DELIM, joinPath( "Volumes", dmgBaseName ) )
        appPath = joinPath( mountPath, "%s.app" % (dmgBaseName,) )
        binPath = __INTERNAL_MACOS_APP_BINARY_TMPLT % (
                  normBinaryName( appPath, isPathPreserved=True, isGui=True )
                , normBinaryName( appPath, isPathPreserved=False, isGui=False )  
            )   
        if isDir( mountPath ) : 
            return _toRet( False, mountPath, appPath, binPath )
        _system( 'hdiutil mount "%s"' % (dmgPath,) )
        if isDir( mountPath ) : 
            return _toRet( True, mountPath, appPath, binPath )
        raise Exception( "Failed to mount %s to %s" % (dmgPath, mountPath) )
    
    # returns: t/f unmounted an existing path     
    def _macUnMountDmg( mountPath ):    
        if not exists( mountPath ) : return False
        _system( 'hdiutil unmount "%s"' % (mountPath,) )
        if not exists( mountPath ) : return True
        raise Exception( "Failed to unmount %s" % (mountPath) )
        
# ----------------------------------------------------------------------------- 
if IS_LINUX:

    from os import geteuid  # @UnresolvedImport (IMPORT DOES NOT EXIST ON WINDOWS)
    
    __commonAskpassPaths = [
         "/usr/X11R6/bin/ssh-askpass"
        ,"/usr/bin/ssh-askpass"
    ]
    _ASKPASS_ENV_VAR="SUDO_ASKPASS"
    __askpassSv=None
    def _assertAskPassAvailable( askpassPath=None ):
        # if running in a standard tty context, or if
        # the user has root access, there is no need to do this
        if stdout.isatty() or geteuid() == 0: return
             
        # if the askpass env var is already defined, just use that
        askpass = getEnv( _ASKPASS_ENV_VAR )
        if askpass: return 
        
        global __askpassSv
        __askpassSv = askpass
        if askpassPath: 
            if isFile( askpassPath ):
                setEnv( _ASKPASS_ENV_VAR, askpassPath )
                return 
        for path in __commonAskpassPaths:
            if isFile( path ):    
                setEnv( _ASKPASS_ENV_VAR, path )
                return
        
        # Invoke a fatal error if nothing succeeded    
        printErr( 
            'A GUI "askpass" program must be manually installed '
            'to run this script within this context (e.g. inside an IDE...?). ' 
            'Common paths were searched without success. '
            'Here is an example installation command to you might execute'
            'to solve this problem:\n\n'
            'sudo apt-get install ssh-askpass-gnome\n\n', 
            isFatal=True )
        
    def _restoreAskPass():
        global __askpassSv
        if __askpassSv: setEnv( _ASKPASS_ENV_VAR, __askpassSv )
        else          : delEnv( _ASKPASS_ENV_VAR )    
        __askpassSv = None                
        