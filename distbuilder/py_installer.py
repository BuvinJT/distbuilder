from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport
from distbuilder.opy_library import obfuscatePy, OBFUS_DIR_PATH

SPEC_EXT = ".spec"

BUILD_DIR_PATH = absPath( "build" )
DIST_DIR_PATH  = absPath( "dist" )

# -----------------------------------------------------------------------------
class PyInstallerConfig:
    """
    See PyInstaller docs for details on these settings.
    """       
    def __init__( self ) :
        self.pyInstallerPath = "pyinstaller" # i.e. on system path
        self.name            = None
        self.distDirPath     = None
        self.isOneFile       = True # overrides PyInstaller default
        self.isGui           = False
        self.versionInfo     = None 
        self.versionFilePath = None # TODO: offer programmatic version info
        self.iconFilePath    = None     
        self.importPaths     = []
        self.hiddenImports   = []
        self.dataFilePaths   = []
        self.binaryFilePaths = []
        self.isAutoElevated  = False        
        self.otherPyInstArgs = "" # open ended
        
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
            if( isinstance( self.iconFilePath, tuple ) or
                isinstance( self.iconFilePath, list ) ):
                if splitExt( self.iconFilePath[0] )[1]==".exe" :
                    self.iconFilePath = "%s,%d" % ( 
                        self.iconFilePath[0], self.iconFilePath[1] )
                else : raise    
            else :
                self.iconFilePath = ( splitExt( self.iconFilePath )[0] +
                                      ".ico" if IS_WINDOWS else ".icns" )                
        except: self.iconFilePath = None
        iconSpec = ( '--icon "%s"' % (self.iconFilePath,) 
                     if self.iconFilePath else "" )
    
        if IS_WINDOWS :        
            versionSpec    = ( '--version-file "%s"' % (self.versionFilePath,) 
                               if self.versionFilePath else "" )        
            adminSwitch    = "--uac-admin" if self.isAutoElevated else ""

        tokens = (nameSpec, distSpec, oneFileSwitch, 
                  windowedSwitch, adminSwitch, iconSpec, versionSpec,
                  pathsSpec, importsSpec, dataSpec, binarySpec,
                  self.otherPyInstArgs )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

class WindowsExeVersionInfo:

    TEMP_FILE_NAME = "win_exe_ver_info.tmp"
    
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
        
# -----------------------------------------------------------------------------   
def buildExecutable( name, entryPointPy, 
        opyConfig=None, pyInstConfig=PyInstallerConfig(),
        distResources=[], distDirs=[] ):
    ''' returns: (binDir, binPath) '''   
    
    # Ensure pyInstConfig is defined, then
    # override / auto assign some pyInstConfig values   
    if pyInstConfig is None: pyInstConfig=PyInstallerConfig()
    distDirPath = joinPath( THIS_DIR, name ) 
    pyInstConfig.name = name
    pyInstConfig.distDirPath = distDirPath
    if IS_WINDOWS and pyInstConfig.versionInfo is not None: 
        tempVerFilePath = absPath( WindowsExeVersionInfo.TEMP_FILE_NAME )                     
        pyInstConfig.versionFilePath = tempVerFilePath
    else : tempVerFilePath = None
    
    # Prepare to build (discard old build files)       
    __clean( pyInstConfig, distDirPath )
    
    # Optionally, create obfuscated version of source
    if opyConfig is not None: 
        _, entryPointPy = obfuscatePy( name, entryPointPy, opyConfig ) 

    # Create a temp version file    
    if tempVerFilePath:
        with open(tempVerFilePath,'wb') as f : 
            print( "Generating temp version file: %s" %
                   tempVerFilePath )
            f.write(str(pyInstConfig.versionInfo))
        
    # Build the executable using PyInstaller        
    __runPyInstaller( entryPointPy, pyInstConfig )
    
    # Discard all temp files (but not distDir!)
    __clean( pyInstConfig )
    
    # Confirm success
    exePath = joinPath( distDirPath, util._normExeName( name ) )
    if not exists(exePath) : 
        raise Exception( "Binary building failure!" )
    print( 'Binary built successfully!\n"%s"' % (exePath,) )
    print('')

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
def __runPyInstaller( entryPointPy, config ) :          
    util._system( '%s %s "%s"' % 
        ( config.pyInstallerPath, str(config), 
          normpath(entryPointPy) ) )  

def __clean( pyInstConfig, distDirPath=None ) :     
    if distDirPath and exists( distDirPath ) :
        removeDir( distDirPath )
    if exists( OBFUS_DIR_PATH ) : removeDir( OBFUS_DIR_PATH )    
    if exists( BUILD_DIR_PATH ) : removeDir( BUILD_DIR_PATH )
    if exists( DIST_DIR_PATH )  : removeDir( DIST_DIR_PATH )
    specPath = joinPath( THIS_DIR, pyInstConfig.name + SPEC_EXT )    
    if isFile( specPath ): removeFile( specPath )    
    if( pyInstConfig.versionInfo is not None and
        pyInstConfig.versionFilePath is not None and
        isFile( pyInstConfig.versionFilePath ) ) : 
        removeFile( pyInstConfig.versionFilePath )           
