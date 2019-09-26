import ast 
from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport
from distbuilder.opy_library import obfuscatePy, \
    _toObfuscatedPaths, OBFUS_DIR_PATH

PYINST_BIN_NAME          = util.normBinaryName( "pyinstaller" )
PYINST_MAKESPEC_BIN_NAME = util.normBinaryName( "pyi-makespec" )

SPEC_EXT = ".spec"

BUILD_DIR_PATH = absPath( "build" )
DIST_DIR_PATH  = absPath( "dist" )
CACHE_DIR_PATH = absPath( "__pycache__" )

__TEMP_NEST_DIR_NAME = "__nested__"

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
                     
        self.isOneFile       = True # this differs from the PyInstaller default
        
        self.importPaths     = []
        self.hiddenImports   = []
        self.dataFilePaths   = []
        self.binaryFilePaths = []
        
        self.isAutoElevated  = False        
        
        self.distDirPath     = None
               
        self.otherPyInstArgs = "" # open ended
        
        # Not directly fed into the utility. Employed by buildExecutable function.       
        self._pngIconResPath   = None
        self.distResources     = []
        self.distDirs          = [] 
        self.isSpecFileRemoved = False
                
    def toArgs( self, isMakeSpec=False ) :

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
            src, dest = self._toSrcDestPair( paths ) 
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
    
    def _toSrcDestPair( self, pathPair, destDir=None ):
        ''' UGLY "Protected" function for internal library uses ONLY! '''
        
        # this is private implementation detail
        isPyInstallerArg = (destDir is None) 
        
        src = dest = None             
        if( isinstance(pathPair, str) or
            isinstance(pathPair, unicode) ):  # @UndefinedVariable
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
            srcHead = THIS_DIR if self.sourceDir is None else self.sourceDir
            src = self._absPath( srcTail )                    
        if isPyInstallerArg:
            if dest is None: dest = relpath( srcHead, THIS_DIR )                    
        else :
            if dest is None:
                relTo = THIS_DIR if self.sourceDir is None else self.sourceDir                                            
                dest = joinPath( relpath( srcHead, relTo ), srcTail )         
            dest = self._absPath( joinPath( destDir, dest ) )                             
        return (src, dest) 

class PyInstSpec:

    __DUPLICATE_DATA_FILE_PATCH = (
        "a.datas = list({tuple(map(str.upper, t)) for t in a.datas})" )

    @staticmethod
    def cfgToPath( pyInstConfig ): return absPath( pyInstConfig.name+SPEC_EXT )

    def __init__( self, filePath=None, pyInstConfig=None, content=None ) :
        self.filePath = filePath
        self.pyInstConfig = pyInstConfig 
        if content: self.content = content
        elif filePath and isFile(filePath): self.read()
    
    def __str__( self ): return self.content

    def path( self ):
        return ( PyInstSpec.cfgToPath( self.pyInstConfig )
                 if self.pyInstConfig else absPath(self.filePath) )
    
    def read( self ):
        self.content = None        
        with open( self.path(), 'r' ) as f : self.content = f.read() 
            
    def write( self ):
        with open( self.path(), 'w' ) as f : f.write( str(self) )
    
    def debug( self ): print( str(self) )
    
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
            self._injectLine( 
                PyInstSpec.__DUPLICATE_DATA_FILE_PATCH, injectLineNo )
            print("Duplicate data patch injected into .spec file...")
            
    def _toLines( self ):        
        return self.content.split('\n' ) if self.content else []
    
    def _fromLines( self, lines ): self.content = '\n'.join( lines )

    def _injectLine( self, injection, lineNo ):               
        lines = self._toLines()            
        if lineNo : lines.insert( lineNo-1, injection )
        else : lines.append( injection )
        self._fromLines( lines )
    
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
        
class WindowsExeVersionInfo:

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
        StringStruct(u'LegalCopyright', u'\\xa9 COMPANY_NAME_COPYRIGHT. All rights reserved.'),
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
    def path(): return absPath( WindowsExeVersionInfo.__TEMP_FILE_NAME )

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
        s = s.replace( "COMPANY_NAME_COPYRIGHT", 
            self.companyName[:-1] if self.companyName.endswith(".") 
            else self.companyName ) # (handle "Company Inc.")
        s = s.replace( "PRODUCT_NAME_INTERNAL", 
            self.productName.lower().replace( " ", "_" ) )                
        s = s.replace( "COMPANY_NAME",  self.companyName )        
        s = s.replace( "PRODUCT_NAME",  self.productName )
        s = s.replace( "PRODUCT_DESCR", self.description )
        s = s.replace( "EXE_NAME", util.normBinaryName( self.exeName ) )                
        return s 
    
    def write( self ):
        filePath = self.path() 
        with open( filePath,'w') as f : f.write( str(self) )
    
    def debug( self ): print( str(self) )
                            
# -----------------------------------------------------------------------------   
def buildExecutable( name=None, entryPointPy=None, 
                     pyInstConfig=PyInstallerConfig(), 
                     opyConfig=None,                    
                     distResources=[], distDirs=[] ):
    ''' returns: (binDir, binPath) '''   
    
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
        raise Exception( "Binary name is required" )
    if not pyInstConfig.entryPointPy : 
        raise Exception( "Binary entry point is required" )
    
    # auto assign some pyInstConfig values        
    distDirPath = joinPath( THIS_DIR, pyInstConfig.name ) 
    pyInstConfig.distDirPath = distDirPath
    if IS_WINDOWS and pyInstConfig.versionInfo is not None: 
        pyInstConfig.versionFilePath = WindowsExeVersionInfo.path()
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
        
    # Build the executable using PyInstaller        
    __runPyInstaller( pyInstConfig )

    # Discard all temp files
    __clean( pyInstConfig, False )

    # eliminate the directory nesting created when the 
    # binary is not bundled into one file 
    if not pyInstConfig.isOneFile :
        print( '"UN-nesting" the dist directory content...' )
        nestedInitDir = joinPath( distDirPath, name )
        nestedTempDir = joinPath( distDirPath, __TEMP_NEST_DIR_NAME )
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
        raise Exception( 'FAILED to create "%s"' % (exePath,) ) 
    print( 'Binary built successfully!\n"%s"' % (exePath,) )
    print('')

    # On Linux, automatically add a png icon to the 
    # external resources, if one exists and is not already included  
    if IS_LINUX :
        try:
            pngPath = pyInstConfig._pngIconResPath
            if exists( pngPath ):
                pngName = basename( pngPath )
                isRes = False
                for res in distResources :
                    isRes = res.endswith( pngName )
                    if isRes: break
                if not isRes: distResources.append( pngPath )
        except: pass
            
    # Add additional distribution resources        
    for res in distResources:
        src, dest = pyInstConfig._toSrcDestPair( res, destDir=distDirPath )
        print( 'Copying "%s" to "%s"...' % ( src, dest ) )
        if isFile( src ) :
            destDir = dirPath( dest )
            if not exists( destDir ): makeDir( destDir )
            try: copyFile( src, dest ) 
            except Exception as e: printExc( e )
        elif isDir( src ):
            try: copyDir( src, dest ) 
            except Exception as e: printExc( e )
        else:
            printErr( 'Invalid path: "%s"' % (src,) )                            
    for d in distDirs:
        dirToMk = joinPath( distDirPath, d )
        print( '"Making directory "%s"...' % ( dirToMk ) )
        try: makeDir( dirToMk ) # works recursively
        except Exception as e: printExc( e )   
    print('')
    
    # Return the paths generated    
    return distDirPath, exePath

def makePyInstSpec( pyInstConfig, opyConfig=None ):
    
    # Verify the required parameters are present    
    if not pyInstConfig.name :         
        raise Exception( "Binary name is required" )
    if not pyInstConfig.entryPointPy : 
        raise Exception( "Binary entry point is required" )
    
    # auto assign some pyInstConfig values        
    pyInstConfig.distDirPath = joinPath( THIS_DIR, pyInstConfig.name )
    if IS_WINDOWS and pyInstConfig.versionInfo is not None: 
        pyInstConfig.versionFilePath = WindowsExeVersionInfo.path()
    else : pyInstConfig.versionInfo = None
    
    # Optionally, get what will be the obfuscated paths
    if opyConfig is not None: 
        _, pyInstConfig.entryPointPy = _toObfuscatedPaths( opyConfig ) 
        
    # Generate the .spec file using the PyInstaller
    __runPyInstaller( pyInstConfig, isMakeSpec=True )

    # Confirm success
    specPath = PyInstSpec.cfgToPath( pyInstConfig )    
    if not exists(specPath) : 
        raise Exception( 'FAILED to create "%s"' % (specPath,) ) 
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
    util._system( '%s"%s" %s' % (runAsScriptPrefix, progPath, args) )   

def __clean( pyInstConfig, isBuildPrep ) :     
    if exists( OBFUS_DIR_PATH ) : removeDir( OBFUS_DIR_PATH )    
    if exists( BUILD_DIR_PATH ) : removeDir( BUILD_DIR_PATH )
    if exists( DIST_DIR_PATH )  : removeDir( DIST_DIR_PATH )
    if exists( CACHE_DIR_PATH ) : removeDir( CACHE_DIR_PATH )
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

    