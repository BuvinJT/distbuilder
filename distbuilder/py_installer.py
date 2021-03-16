import ast 
from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport
from distbuilder.pip_installer import installLibrary, uninstallLibrary
from distbuilder.opy_library import( 
    obfuscatePy, _toObfuscatedPaths, OBFUS_DIR_PATH )

PYINST_BIN_NAME          = util.normBinaryName( "pyinstaller" )
PYINST_MAKESPEC_BIN_NAME = util.normBinaryName( "pyi-makespec" )

PYINST_ROOT_PKG_NAME   = "PyInstaller"
HOOKS_CONTRIB_PKG_NAME = "_pyinstaller_hooks_contrib"

SPEC_EXT = ".spec"

BUILD_DIR_PATH = absPath( "build" )
DIST_DIR_PATH  = absPath( "dist" )
CACHE_DIR_PATH = absPath( "__pycache__" )
TEMP_RES_DIR_PATH = absPath( "__res" )

HOOKS_DIR_NAME = "hooks"

_RUNTIME_HOOKS_DIR_NAME  = "rthooks"
_STANDARD_HOOKS_DIR_NAME = "stdhooks"

_TEMP_NEST_DIR_NAME = "__nested__"

# -----------------------------------------------------------------------------
class PyInstallerConfig:
    """
    See PyInstaller docs for details on these settings.
    """       
    def __init__( self ) :
        
        # Find the "default" installation of pyInstaller. 
        # Fall back to using the system path if an absolute path is not found.
        # Note, it is possible for a user to have multiple versions  
        # on their machine so the "first" one found in a blind search is 
        # not an advisable auto detection method.  The logic here is 
        # based primarily upon pyInstaller documentation, with little 
        # tweaks based on real world observations. 
        #
        # Windows, the "pyInstaller path" maybe a compiled .exe, 
        # or a .py script. On Mac and Linux, when it is not a .py,
        # the is still a py script  with no extension, but a shebang 
        # binding it to a hard coded interpreter path.  This detail 
        # is taken into acoount, to override that shebang, 
        # forcing pyInstaller to run within the same Python context
        # as distbuilder, resolving any cross ups on machines
        # with multiple versions of Python installed.   
        #
        # Note a user can assign a value to this attribute directly
        # when this default fails to meet their needs.
        #
        # -----------------------------------------------------------
        if IS_WINDOWS :            
            p = util._pythonScriptsPath( PYINST_BIN_NAME )
        elif IS_LINUX :
            p = util._usrBinPath( PYINST_BIN_NAME )
            if not exists( p ) :
                p = util._userHiddenLocalBinDirPath( PYINST_BIN_NAME )            
        elif IS_MACOS :
            p = util._usrBinPath( PYINST_BIN_NAME )
            if not exists( p ) :
                p = util._usrLocalBinPath( PYINST_BIN_NAME )
            if not exists( p ) :
                p = util._optLocalBinPath( PYINST_BIN_NAME )                
        else : p = None
        if p is None or not exists(p):
            self.pyInstallerPath = PYINST_BIN_NAME
            self.pyInstallerMakeSpecPath = PYINST_MAKESPEC_BIN_NAME
        else :
            self.pyInstallerPath = p
            self.pyInstallerMakeSpecPath = joinPath( 
                dirPath( p ), PYINST_MAKESPEC_BIN_NAME )
            
        self.name            = None
        
        self.sourceDir       = None
        self.entryPointPy    = None
        
        self.pyInstSpec      = None 
        
        self.isGui           = False
        self.iconFilePath    = None

        self.versionInfo     = None 
        self.versionFilePath = None 
 
        self.isAutoElevated  = False        
                            
        self.isOneFile       = True # this differs from the PyInstaller default
        
        self.importPaths     = []
        self.hiddenImports   = []
        
        self.dataFilePaths   = [] #Embedded
        self.binaryFilePaths = [] #Embedded

        self.distResources   = [] #External 
        self.distDirs        = [] #External (mkDir) 

        self.codeSignConfig  = []
        self.codeSignTargets = []
                
        self.distDirPath     = None
               
        self.otherPyInstArgs = "" # open ended
        
        self._pngIconResPath   = None
        self.isSpecFileRemoved = False
                
    def toArgs( self, isMakeSpec=False ) :

        # new feature not supported in OLD versions of PyInstaller!
        #workDirSpec = '--workpath="%s"' % ( 
        #    self.sourceDir if self.sourceDir else THIS_DIR,)      

        entryPointSpec = ""
        specFileSpec   = ""
        if isMakeSpec:       
            entryPointSpec = '"%s"' % (self._absPath(self.entryPointPy),)      
        else:     
            specPath = self.pyInstSpec.path() if self.pyInstSpec else None
            if specPath : 
                specFileSpec = '"%s"' % (self._absPath(specPath),)
            else :        
                entryPointSpec = '"%s"' % (self._absPath(self.entryPointPy),)
        
        nameSpec       = ( "--name %s" % (self.name,)
                           if self.name else "" )
        distSpec       = ('--distpath "%s"' % (self._absPath(self.distDirPath),)
                          if not isMakeSpec and self.distDirPath else "" )

        oneFileSwitch  = "--onefile" if self.isOneFile else ""
        windowedSwitch = "--windowed" if self.isGui else ""
                
        pathsSpec = ""
        for path in self.importPaths:
            pathsSpec += '--paths "%s"' % (self._absPath(path),)
        importsSpec = ""
        for importMod in self.hiddenImports:
            importsSpec += '--hidden-import "%s"' % (importMod,)
                
        def toPyInstallerSrcDestSpec( pyInstArg, paths ):
            src, dest = util._toSrcDestPair( paths, destDir=None, 
                                             basePath=self.sourceDir )            
            return '%s "%s%s%s" ' % (pyInstArg, src, pathsep, dest)
        
        dataSpec = ""
        for path in self.dataFilePaths:
            dataSpec += toPyInstallerSrcDestSpec( "--add-data", 
                                                  self._absPath(path) )
        binarySpec = ""
        for path in self.binaryFilePaths:
            binarySpec += toPyInstallerSrcDestSpec( "--add-binary", 
                                                    self._absPath(path) )
    
        try:
            if IS_LINUX : 
                # icon embedding is not supported by PyInstaller for Linux,
                # this is handled by the library wrapper independently
                if self._pngIconResPath is None: 
                    self._pngIconResPath = self._absPath( normIconName( 
                        self.iconFilePath, isPathPreserved=True ) )
                self.iconFilePath = None                                                         
            elif( IS_WINDOWS and
                  isinstance( self.iconFilePath, tuple ) or
                  isinstance( self.iconFilePath, list ) ):
                # if the iconFilePath is a tuple or list,
                # it represents a windows exe path and an 
                # icon index embedded within that                  
                if splitExt( self.iconFilePath[0] )[1]==".exe" :
                    self.iconFilePath = "%s,%d" % ( 
                        self._absPath(self.iconFilePath[0]), self.iconFilePath[1] )
                else : raise
            else :
                self.iconFilePath = self._absPath( normIconName( 
                    self.iconFilePath, isPathPreserved=True ) )               
        except: self.iconFilePath = None
        iconSpec = ( '--icon "%s"' % (self.iconFilePath,) 
                     if self.iconFilePath else "" )
    
        if IS_WINDOWS :        
            versionSpec = ( '--version-file "%s"' % (self._absPath(self.versionFilePath),) 
                            if self.versionFilePath else "" )        
            adminSwitch = "--uac-admin" if self.isAutoElevated else ""
        else : versionSpec = adminSwitch = ""

        tokens = (nameSpec, distSpec, oneFileSwitch, 
                  windowedSwitch, adminSwitch, iconSpec, versionSpec,
                  pathsSpec, importsSpec, dataSpec, binarySpec,
                  self.otherPyInstArgs, entryPointSpec, specFileSpec )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

    def _absPath( self, path ): return absPath( path, self.sourceDir )
    
class PyInstSpec( util.PlasticFile ):

    WARN_IGNORE, WARN_ONCE, WARN_ERROR = range(3) 
    
    __DUPLICATE_DATA_FILE_PATCH = (
        "a.datas = list({tuple(map(str.upper, t)) for t in a.datas})" )

    __EXE_SCRIPTS_PARM_LINE = "a.scripts,"

    @staticmethod
    def cfgToPath( pyInstConfig ): return absPath( pyInstConfig.name+SPEC_EXT )

    def __init__( self, filePath=None, pyInstConfig=None, content=None ) :
        self.filePath = filePath
        self.pyInstConfig = pyInstConfig 
        if content: self.content = content
        elif filePath and isFile(filePath): self.read()
        
        self.warningBehavior   = None
        self.isUnBufferedStdIo = False
        self.isModInitDebug    = False        
    
    def path( self ):
        return ( PyInstSpec.cfgToPath( self.pyInstConfig )
                 if self.pyInstConfig else absPath(self.filePath) )

    def injectInterpreterOptions( self ):       
        if not self.content: return 
        if( self.warningBehavior is None and
            not self.isUnBufferedStdIo and  
            not self.isModInitDebug ): return                    
        opt = [] 
        if self.warningBehavior==PyInstSpec.WARN_IGNORE: 
            opt.append( "('W ignore', None, 'OPTION')" )                      
        elif self.warningBehavior== PyInstSpec.WARN_ONCE:
            opt.append( "('W once', None, 'OPTION')" )
        elif self.warningBehavior== PyInstSpec.WARN_ERROR:
            opt.append( "('W error', None, 'OPTION')" )        
        if self.isUnBufferedStdIo:
            opt.append( "('u', None, 'OPTION')" )
        if self.isModInitDebug:
            opt.append( "('v', None, 'OPTION')" )
        opt = "[ %s ]" % (", ".join(opt),)                
        lines = self.toLines()
        for idx, ln in enumerate(lines):
            if ln.strip()==PyInstSpec.__EXE_SCRIPTS_PARM_LINE:
                self.injectLine( "          %s," % (opt,), idx+2 )
                print("Interpreter options injected into .spec file...")
                break
        
    def injectDuplicateDataPatch( self ):
        """
        This patches a known bug in PyInstaller on Windows. 
        PyInstaller analysis can build a set of data file names
        which contain "duplicates" due to the Windows 
        file system case insensitivity.  This patch eliminates
        such duplicates, thus preventing runtime errors in the 
        binary produced.
        """
        if not IS_WINDOWS or not self.content: return                 
        # inject the patch after "a=Analysis(..."
        aAssignFound=False
        injectLineNo=None
        assigns = self._parseAssigments()
        for item in assigns :
            name, lineno = item
            if name == "a": aAssignFound=True
            elif aAssignFound :
                injectLineNo = lineno
                break
        if aAssignFound:
            self.injectLine( 
                PyInstSpec.__DUPLICATE_DATA_FILE_PATCH, injectLineNo )
            print("Duplicate data patch injected into .spec file...")        
                            
    def _parseAssigments( self ):
        """
        Returns a list of tuples in the form of 
        (variable name, file line number (1 based) )
        """        
        assigments = []
        if self.content:
            root = ast.parse( self.content )    
            for child in ast.iter_child_nodes( root ):
                if isinstance( child, ast.Assign ):
                    for target in child.targets :
                        if isinstance( target, ast.Name ) :
                            assigments.append( ( target.id, child.lineno ) )
        return assigments
                                    
class PyInstHook( ExecutableScript ) :
    
    FILE_NAME_PREFIX = "hook-"
    
    def __init__( self, name, script=None,
                  isContribHook=True, isRunTimeHook=False ):
        ExecutableScript.__init__( self,
            name, extension=PY_EXT, shebang=None, script=script ) 
        self.isContribHook=isContribHook
        self.isRunTimeHook=isRunTimeHook
        self.hooksDirPath = None 

    def __str__( self ): return self.script if self.script else ""
    
    def read( self ):
        self.__resolveHooksPath()
        hookPath = joinPath( self.hooksDirPath, self.fileName() )
        if not isFile( hookPath ):
            raise DistBuilderError( 
                "PyInstaller hook does not exist: %s" % (hookPath,) )                      
        with open( hookPath, 'r' ) as f: self.script = f.read()
                                
    def write( self ):
        self.__resolveHooksPath()
        ExecutableScript.write( self, self.hooksDirPath )  

    def remove( self ):
        self.__resolveHooksPath()
        hookPath = joinPath( self.hooksDirPath, self.fileName() )
        if isFile( hookPath ): removeFile( hookPath )
        
    def fileName( self ):
        return "%s%s" % (PyInstHook.FILE_NAME_PREFIX, 
                         ExecutableScript.fileName( self ) )
    
    def __resolveHooksPath( self ):
        if self.hooksDirPath is None:        
            isV4orNewer = PyInstallerMajorVer() >= 4
            isContrib = self.isContribHook and isV4orNewer            
            try:
                pgkDir = modulePackagePath( HOOKS_CONTRIB_PKG_NAME if isContrib
                                            else PYINST_ROOT_PKG_NAME )                            
                if pgkDir is None: raise DistBuilderError()                
                hooksDir = joinPath( pgkDir, HOOKS_DIR_NAME )
                if isContrib:
                    hooksDir = joinPath( hooksDir, 
                        _RUNTIME_HOOKS_DIR_NAME if self.isRunTimeHook else
                        _STANDARD_HOOKS_DIR_NAME )
                elif self.isRunTimeHook:
                    hooksDir = joinPath( hooksDir, _RUNTIME_HOOKS_DIR_NAME )                         
                if isDir( hooksDir ): self.hooksDirPath = hooksDir
                else: raise DistBuilderError()
            except:    
                raise DistBuilderError( 
                    "PyInstaller hooks directory could not be resolved." )         
                                    
# -----------------------------------------------------------------------------   
def installPyInstaller( version=None ):
    installLibrary( PYINST_ROOT_PKG_NAME + ("=="+version if version else "") )

def uninstallPyInstaller(): uninstallLibrary( PYINST_ROOT_PKG_NAME )

def PyInstallerVersion():
    from PyInstaller import __version__ 
    return __version__

def PyInstallerMajorVer(): 
    return int(versionTuple( PyInstallerVersion(), parts=1 )[0])

def PyInstallerMajorMinorVer():
    major, minor = versionTuple( PyInstallerVersion(), parts=2 ) 
    return int(major), int(minor)

def pyScriptToExe( name=None, entryPointPy=None, 
                   pyInstConfig=PyInstallerConfig(), 
                   opyConfig=None,                    
                   distResources=None, distDirs=None ):
    ''' returns: (binDir, binPath) '''   
    
    if distResources is None: distResources=[]
    if distDirs is None: distDirs=[]
     
    # Resolve PyInstallerConfig and the overlapping parameters passed directly
    # (PyInstallerConfig values are given priority)    
    if pyInstConfig is None: 
        pyInstConfig = PyInstallerConfig()
        pyInstConfig.name          = name
        pyInstConfig.entryPointPy  = entryPointPy
        pyInstConfig.distResources = distResources
        pyInstConfig.distDirs      = distDirs
    else :
        name          = pyInstConfig.name   
        entryPointPy  = pyInstConfig.entryPointPy
        distResources = pyInstConfig.distResources
        distDirs      = pyInstConfig.distDirs             
    
    # Verify the required parameters are present    
    if not pyInstConfig.name :         
        raise DistBuilderError( "Binary name is required" )
    if not pyInstConfig.entryPointPy : 
        raise DistBuilderError( "Binary entry point is required" )
    
    # auto assign some pyInstConfig values        
    sourceDir = pyInstConfig.sourceDir 
    distDirPath = joinPath( THIS_DIR, pyInstConfig.name ) 
    pyInstConfig.distDirPath = distDirPath
    if IS_WINDOWS and pyInstConfig.versionInfo is not None: 
        pyInstConfig.versionFilePath = util.WindowsExeVersionInfo.defaultPath()
    else : pyInstConfig.versionInfo = None
        
    # Prepare to build (discard old build files)       
    __clean( pyInstConfig, True )
    
    # Optionally, create obfuscated version of source
    if opyConfig is not None: 
        _, pyInstConfig.entryPointPy = obfuscatePy( opyConfig )

    # Create a temp version file    
    if pyInstConfig.versionInfo is not None:
        print( "Generating version file: %s" % 
               (pyInstConfig.versionInfo.path(),) )
        pyInstConfig.versionInfo.debug() 
        pyInstConfig.versionInfo.write()
                     
    codeSignConfig  = pyInstConfig.codeSignConfig
    codeSignTargets = pyInstConfig.codeSignTargets 

    # Duplicate and sign any *embedded* code sign targets 
    if codeSignTargets:        
        revResources = []
        embeddedRes = pyInstConfig.dataFilePaths + pyInstConfig.binaryFilePaths      
        for res in embeddedRes:
            src, dest = util._toSrcDestPair( res, destDir=TEMP_RES_DIR_PATH,
                                             basePath=sourceDir )
            relDest = relpath( dest, TEMP_RES_DIR_PATH )        
            if relDest in codeSignTargets:
                tempSrcPath = copyToDir( src, TEMP_RES_DIR_PATH )    
                signExe( tempSrcPath, codeSignConfig )                        
                codeSignTargets.pop( relDest )
                revResources.append( (tempSrcPath, relDest) )
            else: revResources.append( res )    
        distResources = revResources
            
    # Build the executable using PyInstaller        
    __runPyInstaller( pyInstConfig )

    # Discard all temp files
    __clean( pyInstConfig, False )

    # eliminate the directory nesting created when the 
    # binary is not bundled into one file 
    if not pyInstConfig.isOneFile :
        print( '"UN-nesting" the dist directory content...' )
        nestedInitDir = joinPath( distDirPath, name )
        nestedTempDir = joinPath( distDirPath, _TEMP_NEST_DIR_NAME )
        if isDir( nestedInitDir ):           
            rename( nestedInitDir, nestedTempDir )
            dirEntries = listdir(nestedTempDir)
            for entry in dirEntries :
                move( joinPath( nestedTempDir, entry ),
                      joinPath( distDirPath,   entry ) )  
            removeDir( nestedTempDir )

    # Confirm success
    exePath = joinPath( distDirPath, util.normBinaryName( name ) )    
    if IS_MACOS and pyInstConfig.isGui :
        # Remove extraneous UNIX binary, and point result to the .app file
        if isFile( exePath ) : removeFile( exePath )
        exePath = normBinaryName( exePath, isPathPreserved=True, isGui=True )   
    if not exists(exePath) : 
        raise DistBuilderError( 'FAILED to create "%s"' % (exePath,) ) 
    print( 'Binary built successfully!\n"%s"' % (exePath,) )
    print('')

    # On Linux, automatically add a png icon to the 
    # external resources, if one exists and is not already included  
    if IS_LINUX :
        try:
            pngPath = pyInstConfig._pngIconResPath
            if exists( pngPath ):
                pngName = baseFileName( pngPath )
                isRes = False
                for res in distResources :
                    isRes = res.endswith( pngName )
                    if isRes: break
                if not isRes: distResources.append( pngPath )
        except: pass
            
    # Add additional distribution resources        
    __copyResources( distResources, distDirs, distDirPath, sourceDir )

    if pyInstConfig.codeSignConfig:
        # Code sign the exe
        signExe( exePath, pyInstConfig.codeSignConfig )
                
        # Code sign external resource targets
        if codeSignTargets:         
            for target in codeSignTargets:
                if target in distResources:            
                    targetPath = absPath( target, sourceDir )
                    signExe( targetPath, codeSignConfig )
                
    # Return the paths generated    
    return distDirPath, exePath


def __copyResources( resources, mkDirs, destDirPath, sourceDir ):
    for res in resources:
        src, dest = util._toSrcDestPair( res, destDir=destDirPath,
                                         basePath=sourceDir )
        print( 'Copying "%s" to "%s"...' % ( src, dest ) )
        if isFile( src ) :
            destDir = dirPath( dest )
            if not exists( destDir ): makeDir( destDir )
            try: copyFile( src, dest ) 
            except Exception as e: printExc( e )
        elif isDir( src ):
            try: copyDir( src, dest ) 
            except Exception as e: printExc( e )
        else: printErr( 'Invalid path: "%s"' % (src,) )         
    if mkDirs:
        for d in mkDirs:
            dirToMk = joinPath( destDirPath, d )
            print( '"Making directory "%s"...' % ( dirToMk ) )
            try: makeDir( dirToMk ) # works recursively
            except Exception as e: printExc( e )   
        print('')
    

def makePyInstSpec( pyInstConfig, opyConfig=None ):
    
    # Verify the required parameters are present    
    if not pyInstConfig.name :         
        raise DistBuilderError( "Binary name is required" )
    if not pyInstConfig.entryPointPy : 
        raise DistBuilderError( "Binary entry point is required" )
    
    # auto assign some pyInstConfig values        
    pyInstConfig.distDirPath = joinPath( THIS_DIR, pyInstConfig.name )
    if IS_WINDOWS and pyInstConfig.versionInfo is not None: 
        pyInstConfig.versionFilePath = WindowsExeVersionInfo.defaultPath()
    else : pyInstConfig.versionInfo = None
    
    # Optionally, get what will be the obfuscated paths
    if opyConfig is not None: 
        _, pyInstConfig.entryPointPy = _toObfuscatedPaths( opyConfig ) 
        
    # Generate the .spec file using the PyInstaller
    __runPyInstaller( pyInstConfig, isMakeSpec=True )

    # Confirm success
    specPath = PyInstSpec.cfgToPath( pyInstConfig )    
    if not exists(specPath) : 
        raise DistBuilderError( 'FAILED to create "%s"' % (specPath,) ) 
    print( 'Spec file generated successfully!\n"%s"' % (specPath,) )
    print('')

    # Create a PyInstSpec object and return it indirectly 
    # by updating the pyInstConfig
    pyInstConfig.pyInstSpec = PyInstSpec( specPath )
    
    # return the path to the .spec file
    return specPath
    
# -----------------------------------------------------------------------------    
def __runPyInstaller( pyInstConfig, isMakeSpec=False ) :   
    # See comments in PyInstallerConfig __init__ regarding
    # these paths and run contexts.   
    progPath = ( pyInstConfig.pyInstallerMakeSpecPath if isMakeSpec else
                 pyInstConfig.pyInstallerPath )    
    if IS_WINDOWS :
        _, ext = splitExt( progPath )    
        isPyScript = ext.lower()==PY_EXT
    else : isPyScript = True       
    runAsScriptPrefix = '"%s" ' % (PYTHON_PATH,) if isPyScript else ""           
    args = pyInstConfig.toArgs( isMakeSpec )
    # the cd is required to support legacy versions of PyInstaller, which lacked
    # the workpath switch
    util._system( 'cd "%s" %s %s"%s" %s' % 
                  (THIS_DIR, SYS_CMD_DELIM, runAsScriptPrefix, progPath, args) )   

def __clean( pyInstConfig, isBuildPrep ) :     
    if exists( OBFUS_DIR_PATH )    : removeDir( OBFUS_DIR_PATH )    
    if exists( TEMP_RES_DIR_PATH ) : removeDir( TEMP_RES_DIR_PATH )
    if exists( BUILD_DIR_PATH )    : removeDir( BUILD_DIR_PATH )
    if exists( DIST_DIR_PATH )     : removeDir( DIST_DIR_PATH )
    if exists( CACHE_DIR_PATH )    : removeDir( CACHE_DIR_PATH )
    
    if( pyInstConfig.versionInfo is not None and
        pyInstConfig.versionFilePath is not None and
        isFile( pyInstConfig.versionFilePath ) ) : 
        removeFile( pyInstConfig.versionFilePath )           
    
    if isBuildPrep:
        if isDir( pyInstConfig.distDirPath ) :
            removeDir( pyInstConfig.distDirPath )
    else :
        specPath = ( pyInstConfig.pyInstSpec.path() 
                     if pyInstConfig.pyInstSpec else None )
        if( specPath and pyInstConfig.isSpecFileRemoved and 
            isFile( specPath ) ): 
            removeFile( specPath )        

    