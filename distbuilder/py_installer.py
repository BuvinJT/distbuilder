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
            
        iconSpec       = ( '--icon "%s"' % (self.iconFilePath,) 
                           if self.iconFilePath else "" )    
        # TODO : add version file generation
        versionSpec    = ( '--version-file "%s"' % (self.versionFilePath,) 
                           if self.versionFilePath else "" )
    
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
    
        adminSwitch    = "--uac-admin" if self.isAutoElevated else ""

        tokens = (nameSpec, distSpec, oneFileSwitch, 
                  windowedSwitch, adminSwitch, iconSpec, versionSpec,
                  pathsSpec, importsSpec, dataSpec, binarySpec,
                  self.otherPyInstArgs )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

# -----------------------------------------------------------------------------   
def buildExecutable( name, entryPointPy, 
        opyConfig=None, pyInstConfig=PyInstallerConfig(),
        distResources=[], distDirs=[] ):
    ''' returns: (binDir, binPath) '''   
       
    # Prepare to build (discard old build files)   
    distDirPath = joinPath( THIS_DIR, name )
    __clean( name, distDirPath )
    
    # Optionally, create obfuscated version of source
    if opyConfig is not None: 
        _, entryPointPy = obfuscatePy( name, entryPointPy, opyConfig ) 
    
    # Build the executable using PyInstaller        
    pyInstConfig.name = name
    pyInstConfig.distDirPath = distDirPath
    __runPyInstaller( entryPointPy, pyInstConfig )
    
    # Discard temp files
    __clean( name )
    
    # Confirm success
    exePath = joinPath( distDirPath, util._normExeName( name ) )
    if not exists(exePath) : 
        raise Exception( "Binary building failure!" )
    print( 'Binary built successfully!\n"%s"' % (exePath,) )
    print()

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
    print()
    
    # Return the paths generated    
    return distDirPath, exePath

# -----------------------------------------------------------------------------    
def __runPyInstaller( entryPointPy, config ) :          
    util._system( '%s %s "%s"' % 
        ( config.pyInstallerPath, str(config), 
          normpath(entryPointPy) ) )  

def __clean( name, distDirPath=None ) :     
    if distDirPath and exists( distDirPath ) :
        removeDir( distDirPath )
    if exists( OBFUS_DIR_PATH ) : removeDir( OBFUS_DIR_PATH )    
    if exists( BUILD_DIR_PATH ) : removeDir( BUILD_DIR_PATH )
    if exists( DIST_DIR_PATH )  : removeDir( DIST_DIR_PATH )
    specPath = joinPath( THIS_DIR, name + SPEC_EXT )    
    if isFile( specPath ): removeFile( specPath )    
            
