import opy  # Custom Library
from opy import OpyConfig, analyze, patch, \
    obfuscatedId  # @UnusedImport
from distbuilder.util import *  # @UnusedWildImport

OBFUS_DIR_PATH = absPath( "obfuscated" )
STAGE_DIR_PATH = absPath( "stage" )

LIBRARY_SETUP_FILE_NAME         = "setup.py"
PACKAGE_ENTRY_POINT_MODULE_NAME = "__init__"
PACKAGE_ENTRY_POINT_FILE_NAME   = PACKAGE_ENTRY_POINT_MODULE_NAME + PY_EXT

# -----------------------------------------------------------------------------    
class OpyConfigExt( OpyConfig ):
    """
    See Opy docs for details.
    """        
    def __init__( self, name, entryPointPy=None, isLibrary=False,
                  bundleLibs=None, sourceDir=None, patches=None ):
        # common attributes
        self.name = name
        self.entryPointPy = entryPointPy
        self.bundleLibs = bundleLibs
        self.sourceDir = THIS_DIR if sourceDir is None else absPath(sourceDir)        
        self.patches = patches
        
        # library attributes 
        self.isLibrary                = isLibrary
        self.isExposingPackageImports = True 
        self.isExposingPublic         = True 
                
        OpyConfig.__init__( self )

# -----------------------------------------------------------------------------   
class LibToBundle:
    def __init__( self, name, localDirPath=None, pipConfig=None, isObfuscated=False ):
        self.name         = name
        self.localDirPath = localDirPath
        self.pipConfig    = pipConfig
        self.isObfuscated = isObfuscated

# -----------------------------------------------------------------------------   
class OpyPatch:
    def __init__( self, relPath, patches, parentDir=OBFUS_DIR_PATH ):
        self.relPath = normpath(relPath).replace("\\","/")
        self.path    = normpath(joinPath( parentDir, relPath )).replace("\\","/")
        self.patches = patches

    def obfuscatePath( self, opyResults ):
        try: 
            self.path = opyResults.obfuscatedFiles[ self.relPath ]
            return True
        except: 
            printErr( "OpyPatch cannot map %s" % (self.relPath,) )
            return False
        
    def apply( self, opyResults ): patch( self.path, opyResults, self.patches )

# -----------------------------------------------------------------------------       
def obfuscatePy( opyConfig ):
    if opyConfig.isLibrary : return __obfuscateLib( opyConfig )
    else :                   return __runOpy(       opyConfig )

def opyAnalyze( opyConfig, filesSubset=[] ):
    if opyConfig.isLibrary : 
        return __obfuscateLib( opyConfig, 
                               isAnalysis=True, filesSubset=filesSubset )
    else :                   
        return __runOpy(       opyConfig, 
                               isAnalysis=True, filesSubset=filesSubset )

def __obfuscateLib( opyConfig, isAnalysis=False, filesSubset=[] ):
    ''' returns: (obDir, obPath) OR an OpyResults object when isAnalysis=True '''
    
    # Leave the setup script and all package entry points in plain text
    plainFiles = [LIBRARY_SETUP_FILE_NAME]
    for root, _, files in walk( THIS_DIR ):
        for f in [f for f in files if f==PACKAGE_ENTRY_POINT_FILE_NAME]:
            plainFiles.append( relpath( joinPath(root, f), THIS_DIR ) )         
    opyConfig.plain_files.extend( plainFiles )
    
    # Don't obfuscate package name
    opyConfig.plain_names.extend( [opyConfig.name] )
    
    # Optionally, don't obfuscate any of the imports 
    # defined in the package entry point modules by
    # automatically finding those names and adding  
    # them to the clear text list
    if opyConfig.isExposingPackageImports :
        opyResults = analyze( fileList=[PACKAGE_ENTRY_POINT_FILE_NAME], 
                              configSettings=opyConfig )
        opyConfig.external_modules.extend( opyResults.obfuscatedModImports )
    
    # Optionally, don't obfuscate anything with public access
    # (e.g. public module constants or class functions/attributes)
    opyConfig.skip_public = opyConfig.isExposingPublic
    
    # Create an obfuscated library, designating setup as the entry point
    opyConfig.entryPointPy = LIBRARY_SETUP_FILE_NAME    
    return __runOpy( opyConfig, isAnalysis, filesSubset ) 

def __runOpy( opyConfig, isAnalysis=False, filesSubset=[] ):
    ''' returns: (obDir, obPath) OR an OpyResults object when isAnalysis=True '''
         
    # Discard prior obfuscated source   
    if exists( OBFUS_DIR_PATH ) : removeDir( OBFUS_DIR_PATH )
    
    # Using a staging directory if a bundleLibs list was provided 
    if opyConfig.bundleLibs: sourceDir = createStageDir( 
        opyConfig.bundleLibs, opyConfig.sourceDir )
    elif opyConfig.sourceDir : sourceDir = opyConfig.sourceDir 
    
    # Leave the build script calling this library 
    # out of the obfuscation results / directory
    try : opyConfig.skip_path_fragments.append( splitPath(argv[0])[1] )
    except : pass
    
    # Don't obfuscate the name of the entry point module
    try : 
        opyConfig.plain_names.append( 
            rootFileName( opyConfig.entryPointPy ) )
    except : pass         
    
    # Suffix all obfuscated names with the project name
    # (to avoid theoretical collisions with plain names)
    opyConfig.obfuscated_name_tail = "_%s_" % (opyConfig.name,)
    
    # Run Opy process
    if isAnalysis:        
        opyResults = opy.analyze( sourceRootDirectory = sourceDir,
                                  fileList            = filesSubset,  
                                  configSettings      = opyConfig )        
    else :        
        opyResults = opy.obfuscate( sourceRootDirectory = sourceDir,
                                    targetRootDirectory = OBFUS_DIR_PATH,
                                    configSettings      = opyConfig )
    print
    
    # Discard staging directory   
    if exists( STAGE_DIR_PATH ) : removeDir( STAGE_DIR_PATH )
    
    # Return results, when run in analysis mode 
    if isAnalysis: return opyResults 
        
    # Optionally, apply patches
    if opyConfig.patches :
        for p in opyConfig.patches:
            if p.obfuscatePath( opyResults ): 
                p.apply( opyResults )
    
    # Return the paths generated 
    return _toObfuscatedPaths( opyConfig )
    
def createStageDir( bundleLibs=[], sourceDir=THIS_DIR ):
    ''' returns: stageDir '''
    
    from distbuilder.pip_installer import installLibrary
    if exists( STAGE_DIR_PATH ) : removeDir( STAGE_DIR_PATH )
    if isDir( sourceDir ): copyDir( sourceDir, STAGE_DIR_PATH )    
    for lib in bundleLibs :        
        destPath = joinPath( STAGE_DIR_PATH, lib.name )
        if lib.pipConfig is None :
            if lib.localDirPath is None:
                lib.localDirPath = modulePackagePath( lib.name )            
            copyDir( lib.localDirPath, destPath )         
        else:    
            lib.pipConfig.destPath = destPath
            installLibrary( lib.name, pipConfig=lib.pipConfig ) 
    return STAGE_DIR_PATH

def _toObfuscatedPaths( opyConfig ) :
    entryPoint = splitPath( opyConfig.entryPointPy )[1] 
    return OBFUS_DIR_PATH, joinPath( OBFUS_DIR_PATH, entryPoint )
            