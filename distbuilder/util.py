from six import PY2, PY3, string_types  # @UnusedImport
from six.moves import urllib
from sys import argv, stdout, stderr, exit, \
    executable as PYTHON_PATH
from os import system, sep as PATH_DELIM, pardir as PARENT_DIR, \
    remove as removeFile, \
    fdopen, getcwd, chdir, walk, environ, devnull, \
    chmod, getenv, listdir, makedirs as makeDir, rename # @UnusedImport   
from os.path import exists, isfile, islink, \
    dirname as dirPath, normpath, realpath, isabs, \
    join as joinPath, split as splitPath, splitext as splitExt, \
    expanduser, basename as fileBaseName, \
    relpath, pathsep      # @UnusedImport
from shutil import rmtree as removeDir, move, make_archive, \
    copytree as copyDir, copyfile as copyFile   # @UnusedImport
import platform
from tempfile import gettempdir, mkstemp, mktemp
from subprocess import Popen, list2cmdline, check_output, \
    PIPE, STDOUT, \
    check_call  # @UnusedImport
try: from subprocess import DEVNULL 
except ImportError: DEVNULL = open(devnull, 'wb')    
import traceback
from distutils.sysconfig import get_python_lib
import inspect  # @UnusedImport
from time import sleep

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

__SCRUB_CMD_TMPL = "{0}{1}"
__DBL_QUOTE      = '"'
__SPACE          = ' '
__ESC_SPACE      = '\\ '
__NEWLINE        = '\n'
if IS_WINDOWS :
    import ctypes        
    from ctypes import wintypes
    from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW
    __CSIDL_DESKTOP_DIRECTORY = 16    
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
def run( binPath, args=[], 
         wrkDir=None, isElevated=False, isDebug=False ):
    _run( binPath, args, wrkDir, isElevated, isDebug )
         
def _run( binPath, args=[], 
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
            
    binDir, fileName = splitPath( binPath )   
    if wrkDir is None : wrkDir = binDir
    isMacApp = _isMacApp( binPath )
    
    # Handle elevated sub processes in Windows
    if IS_WINDOWS and isElevated and not __windowsIsElevated():        
        __printCmd( "", binPath, args, wrkDir )
        retCode = __windowsElevated( binPath, args, wrkDir )
        if isDebug and retCode is not None : __printRetCode( retCode )  
        return
    
    # "Debug" mode    
    if isDebug :
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
                   stdout=PIPE, stderr=STDOUT, bufsize=1 )
        while p.poll() is None:
            line = p.stdout.readline() if PY2 else p.stdout.readline().decode()
            if sharedFile: sharedFile.write( line )
            else:
                stdout.write( line )
                stdout.flush()
        if sharedFile :
            sharedFile.write( __SHARED_RET_CODE_TMPLT % (p.returncode,) )
            sharedFile.close()
        else : __printRetCode( p.returncode )
        return 
    
    # All other run conditions...    
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
    if IS_WINDOWS or isMacApp : pwdCmd = ""
    else : pwdCmd = "./" if wrkDir==binDir else ""
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
        chdir( wrkDir )
    cmd = __scrubSystemCmd( cmd )        
    print( cmd )
    system( cmd ) 
    print('')
    if wrkDir is not None: chdir( initWrkDir )

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
    return ctypes.windll.shell32.IsUserAnAdmin()

# returns  (isRun, retCode, output)            
def __windowsElevated( exePath, args=[], wrkDir=None ):

    def __runElevated( exePath, args, wrkDir, sharedFilePath ):
        verb = "runas"
        pyPath = PYTHON_PATH
        binPathArg = "'%s'" % (_normEscapePath(exePath),)
        argsArg= '[ %s ]' % (','.join(
            ["'%s'" % (_normEscapePath(a),) for a in args]),)
        wrkDirArg="'%s'" % (wrkDir,) if wrkDir else "None" 
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

    sharedFilePath = _reserveTempFile()
    isRun = __runElevated( exePath, args, wrkDir, sharedFilePath )
    retCode = __getResults( sharedFilePath ) if isRun else None
    removeFile( sharedFilePath )
    return retCode

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
    srcTail = fileBaseName( normpath(srcPath) )
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
    srcTail = fileBaseName( normpath(srcPath) )
    destPath = joinPath( destDirPath, srcTail )
    if srcPath == destPath: return
    __removeFromDir( srcTail, destDirPath )
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
            dirPath( sourceDir ), fileBaseName( sourceDir ) )
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
    if not isPathPreserved : path = fileBaseName( path )
    base, ext = splitExt( path )
    if IS_MACOS and isGui :
        return "%s%s" % (base, _MACOS_APP_EXT)      
    if IS_WINDOWS: return base + (".exe" if ext=="" else ext)
    return base 
                            
def normIconName( path, isPathPreserved=False ):
    if path is None : return None    
    if not isPathPreserved : path = fileBaseName( path )
    base, _ = splitExt( path )
    if IS_WINDOWS: return "%s%s" % (base, _WINDOWS_ICON_EXT) 
    elif IS_MACOS: return "%s%s" % (base, _MACOS_ICON_EXT) 
    elif IS_LINUX: return "%s%s" % (base, _LINUX_ICON_EXT) 
    raise Exception( __NOT_SUPPORTED_MSG )
    return base 
                        
def _isMacApp( path ):
    if path is None : return False 
    return IS_MACOS and splitExt(path)[1]==".app"

# ----------------------------------------------------------------------------- 
def rootFileName( path ): 
    if path is None : return None
    return splitExt(fileBaseName(path))[0]

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

def tempDirPath(): return gettempdir()

# mktemp returns a temp file path, but doesn't create it.
# Thus, it is possible in theory for second process
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
            
def __getFolderPathByCSIDL( csidl ):
    SHGFP_TYPE_CURRENT = 0   # Get current, not default value
    buf = ctypes.create_unicode_buffer( wintypes.MAX_PATH )
    ctypes.windll.shell32.SHGetFolderPathW( 
        None, csidl, None, SHGFP_TYPE_CURRENT, buf )
    return buf.value 

# -----------------------------------------------------------------------------
def versionTuple( ver, parts=4 ): return tuple( __versionList( ver, parts ) )
                
def versionStr( ver, parts=4 ): 
    verList = __versionList( ver, parts )
    verList = [str(p) for p in verList]
    return ".".join( verList )

def __versionList( ver, parts=4 ):        
    try:
        if isinstance(ver, string_types ):                 
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
        downloadName = fileBaseName( urllib.parse.urlsplit( url )[2] )
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
class ExecutableScript:
    
    __WIN_DEFAULT_EXT = "bat" 
    __NIX_DEFAULT_EXT = "sh"
    
    __NIX_DEFAULT_SHEBANG = "#!/bin/sh"
    __SHEBANG_TEMPLATE = "%s\n%s"
        
    def __init__( self, rootName, 
                  extension=True, # True==auto assign, str==what to use, or None
                  shebang=True, # True==auto assign, str==what to use, or None                  
                  script=None, scriptPath=None ) :
        self.rootName = rootName
        if extension==True:
            self.extension = ( ExecutableScript.__WIN_DEFAULT_EXT 
                if IS_WINDOWS else ExecutableScript.__NIX_DEFAULT_EXT )
        else: self.extension = extension    
        if shebang==True and scriptPath is None :
            self.shebang =( None if IS_WINDOWS else 
                            ExecutableScript.__NIX_DEFAULT_SHEBANG ) 
        else: self.shebang = shebang            
        if scriptPath:
            with open( scriptPath, 'rb' ) as f: self.script = f.read()
        else: self.script = script  
                                                    
    def __str__( self ) :
        if self.script is None : ""
        if self.shebang:
            return( ExecutableScript.__SHEBANG_TEMPLATE % 
                    (self.shebang, self.script) )
        else: return self.script 
        
    def debug( self ): 
        if self.script: print( str(self) )
        
    def fileName( self ):
        return joinExt( self.rootName,self.extension )
                        
    def write( self, dirPath ):
        if self.script is None : return
        if not isDir( dirPath ): makeDir( dirPath )
        filePath = joinPath( dirPath, self.fileName() )
        print("Writing script: %s\n\n%s\n" % (filePath,str(self)) )                               
        with open( filePath, 'w' ) as f: f.write( str(self) ) 
        if IS_LINUX : chmod( filePath, 0o755 )
    
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
        dmgBaseName = splitExt( fileBaseName( dmgPath ) )[0]
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
        