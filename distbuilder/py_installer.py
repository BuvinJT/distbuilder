from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport
from distbuilder.opy_library import obfuscatePy, OBFUS_DIR_PATH

PYINST_BIN_NAME = util.normBinaryName( "pyinstaller" )

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
        # not an advisable auto detection methed.  The logic here is 
        # based primarily upon pyInstaller documentation. 
        # Note a user can assign a value to this attribute directly
        # when this default fails to meet their needs.
        if IS_WINDOWS :
            # resolves multi-python version environments
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
        self.pyInstallerPath = (
            PYINST_BIN_NAME if p is None or not exists(p) else p)
        
        self.name            = None
        self.entryPointPy    = None
        
        self.isGui           = False
        self.iconFilePath    = None

        self.versionInfo     = None 
        self.versionFilePath = None # TODO: offer programmatic version info
                     
        self.distDirPath     = None
        self.isOneFile       = True # overrides PyInstaller default
        
        self.importPaths     = []
        self.hiddenImports   = []
        self.dataFilePaths   = []
        self.binaryFilePaths = []
        
        self.isAutoElevated  = False        
        self.otherPyInstArgs = "" # open ended

        # Not directly fed into the utility. Employed by buildExecutable function.       
        self._pngIconResPath = None
        self.distResources   = []
        self.distDirs        = [] 
                
    def __str__( self ):
        nameSpec       = ( "--name %s" % (self.name,)
                           if self.name else "" )
        distSpec       = ('--distpath "%s"' % (self.distDirPath,)
                          if self.distDirPath else "" )

        oneFileSwitch  = "--onefile" if self.isOneFile else ""
        windowedSwitch = "--windowed" if self.isGui else ""
                
        pathsSpec = ""
        for path in self.importPaths:
            pathsSpec += '--paths "%s"' % (path,)
        importsSpec = ""
        for importMod in self.hiddenImports:
            importsSpec += '--hidden-import "%s"' % (importMod,)
                
        def toPyInstallerSrcDestSpec( pyInstArg, paths ):
            src, dest = util._toSrcDestPair( paths ) 
            return '%s "%s%s%s" ' % (pyInstArg, src, pathsep, dest)
        
        dataSpec = ""
        for paths in self.dataFilePaths:
            dataSpec += toPyInstallerSrcDestSpec( "--add-data", paths )
        binarySpec = ""
        for paths in self.binaryFilePaths:
            binarySpec += toPyInstallerSrcDestSpec( "--add-binary", paths )
    
        try:
            if IS_LINUX : 
                # icon emmbedding is not supported by PyInstaller for Linux,
                # this is handled by the library wrapper independently 
                self._pngIconResPath = util._normIconName( 
                    self.iconFilePath, isPathPreserved=True )
                self.iconFilePath = None                                                         
            elif( IS_WINDOWS and
                  isinstance( self.iconFilePath, tuple ) or
                  isinstance( self.iconFilePath, list ) ):
                # if the iconFilePath is a tuple or list,
                # it represents a windows exe path and an 
                # icon index embedded within that                  
                if splitExt( self.iconFilePath[0] )[1]==".exe" :
                    self.iconFilePath = "%s,%d" % ( 
                        self.iconFilePath[0], self.iconFilePath[1] )
                else : raise
            else :
                self.iconFilePath = util._normIconName( 
                    self.iconFilePath, isPathPreserved=True )               
        except: self.iconFilePath = None
        iconSpec = ( '--icon "%s"' % (self.iconFilePath,) 
                     if self.iconFilePath else "" )
    
        if IS_WINDOWS :        
            versionSpec    = ( '--version-file "%s"' % (self.versionFilePath,) 
                               if self.versionFilePath else "" )        
            adminSwitch    = "--uac-admin" if self.isAutoElevated else ""
        else : versionSpec = adminSwitch = ""

        tokens = (nameSpec, distSpec, oneFileSwitch, 
                  windowedSwitch, adminSwitch, iconSpec, versionSpec,
                  pathsSpec, importsSpec, dataSpec, binarySpec,
                  self.otherPyInstArgs )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

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
            else self.companyName )
        s = s.replace( "PRODUCT_NAME_INTERNAL", 
            self.productName.lower().replace( " ", "_" ) )                
        s = s.replace( "COMPANY_NAME",  self.companyName )        
        s = s.replace( "PRODUCT_NAME",  self.productName )
        s = s.replace( "PRODUCT_DESCR", self.description )
        s = s.replace( "EXE_NAME",     
            self.exeName if self.companyName.endswith(".exe")
            else self.exeName + ".exe" )                
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
    if not name :         raise Exception( "Binary name is required" )
    if not entryPointPy : raise Exception( "Binary entry point is required" )
    
    # auto assign some pyInstConfig values        
    distDirPath = joinPath( THIS_DIR, name ) 
    pyInstConfig.distDirPath = distDirPath
    if IS_WINDOWS and pyInstConfig.versionInfo is not None: 
        pyInstConfig.versionFilePath = WindowsExeVersionInfo.path()
    else : pyInstConfig.versionInfo = None
    
    # Prepare to build (discard old build files)       
    __clean( pyInstConfig, distDirPath )
    
    # Optionally, create obfuscated version of source
    if opyConfig is not None: 
        _, entryPointPy = obfuscatePy( opyConfig ) 

    # Create a temp version file    
    if pyInstConfig.versionInfo is not None:
        print( "Generating version file: %s" % 
               (pyInstConfig.versionInfo.path(),) )
        pyInstConfig.versionInfo.debug() 
        pyInstConfig.versionInfo.write()
        
    # Build the executable using PyInstaller        
    __runPyInstaller( pyInstConfig )

    # Discard all temp files (but not distDir!)
    __clean( pyInstConfig ) 

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
        src, dest = util._toSrcDestPair( res, destDir=distDirPath )
        print( 'Copying "%s" to "%s"...' % ( src, dest ) )
        if isFile( src ) :
            destDir = dirPath( dest )
            if not exists( destDir ): makeDir( destDir )
            try: copyFile( src, dest ) 
            except Exception as e: printExc( e )
        elif exists:
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

# -----------------------------------------------------------------------------    
def __runPyInstaller( pyInstConfig ) :          
    util._system( '%s %s "%s"' % 
        ( pyInstConfig.pyInstallerPath, str(pyInstConfig), 
          normpath(pyInstConfig.entryPointPy) ) )  

def __clean( pyInstConfig, distDirPath=None ) :     
    if distDirPath and exists( distDirPath ) :
        removeDir( distDirPath )
    if exists( OBFUS_DIR_PATH ) : removeDir( OBFUS_DIR_PATH )    
    if exists( BUILD_DIR_PATH ) : removeDir( BUILD_DIR_PATH )
    if exists( DIST_DIR_PATH )  : removeDir( DIST_DIR_PATH )
    if exists( CACHE_DIR_PATH ) : removeDir( CACHE_DIR_PATH )
    specPath = joinPath( THIS_DIR, pyInstConfig.name + SPEC_EXT )    
    if isFile( specPath ): removeFile( specPath )    
    if( pyInstConfig.versionInfo is not None and
        pyInstConfig.versionFilePath is not None and
        isFile( pyInstConfig.versionFilePath ) ) : 
        removeFile( pyInstConfig.versionFilePath )           
    
    