import six
from distbuilder import util
from distbuilder.util import *  # @UnusedWildImport
import xml.etree.ElementTree as ET
from xml.dom import minidom

BUILD_SETUP_DIR_PATH = absPath( "build_setup" )
INSTALLER_DIR_PATH = "installer"
DEFAULT_SETUP_NAME = "setup.exe"

QT_IFW_VERBOSE_SWITCH = '-v'

QT_IFW_DIR_ENV_VAR = "QT_IFW_DIR"
QT_BIN_DIR_ENV_VAR = "QT_BIN_DIR"

__BIN_SUB_DIR = "bin"
__QT_INSTALL_CREATOR_EXE_NAME  = "binarycreator.exe"

__QT_WINDOWS_DEPLOY_EXE_NAME   = "windeployqt.exe"
__QT_WINDOWS_DEPLOY_QML_SWITCH = "--qmldir"
__MINGW_DLL_LIST = [
      "libgcc_s_dw2-1.dll"
    , "libstdc++-6.dll"
    , "libwinpthread-1.dll"
]

# -----------------------------------------------------------------------------
class QtIfwConfig:
    """
    Refer to the Qt Installer Framework docs for command line usage details.
    """    
    
    __PACKAGES_PATH_TMPLT = "%s/packages"
    __CONTENT_PATH_TMPLT = "%s/packages/%s/data" 
    
    @staticmethod
    def pkgDirPath() :  
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwConfig.__PACKAGES_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )
    
    def __init__( self, pkgSrcDirPath=None, pkgSrcExePath=None,                  
                  pkgName=None, installerDefDirPath=None,
                  setupExeName=DEFAULT_SETUP_NAME ) :       
        # basic definition
        self.pkgName             = pkgName
        self.installerDefDirPath = installerDefDirPath
        # content
        self.pkgSrcDirPath   = pkgSrcDirPath
        self.pkgSrcExePath   = pkgSrcExePath
        self.othContentPaths = None                     
        # exe names
        self.exeName      = None   
        self.setupExeName = setupExeName
        # IFW tool path (attempt to use environmental variable if None)
        self.qtIfwDirPath = None
        # other IFW command line options
        self.isDebugMode    = False
        self.otherqtIfwArgs = ""
        # Qt C++ Content extended details / requirements
        self.isQtCppExe     = False
        self.isMingwExe     = False
        self.qtBinDirPath   = None  # (attempt to use environmental variable if None)
        self.qmlScrDirPath  = None  # for QML projects only   
                
    def __str__( self ) :
        configSpec   = '-c "%s"' % (QtIfwConfigXml.path(),)
        packagesSpec = '-p "%s"' % (QtIfwConfig.pkgDirPath(),)
        verboseSpec  = '-v' if self.isDebugMode else ''                
        tokens = (configSpec, packagesSpec, verboseSpec, self.otherqtIfwArgs)
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         
        
    def pkgContentDirPath( self ) :
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwConfig.__CONTENT_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName,) ) )
            
# -----------------------------------------------------------------------------    
class QtIfwConfigXml:
    """
    Refer to the Qt Installer Framework docs for details on the qtIfwConfig.xml options.
    """    
    
    __DIR_TMPLT  = "%s/config"
    __PATH_TMPLT = __DIR_TMPLT + "/config.xml"
    __HEADER     = '<?xml version="1.0" encoding="UTF-8"?>'
    __ROOT       = "Installer"
    __TAGS       = [ "Name"
                   , "Version"
                   , "Title"
                   , "Publisher"
                   , "InstallerApplicationIcon"
                   , "TargetDir"
                   , "StartMenuDir"             
                   , "RunProgram" # RunProgramArguments added separately...
                   , "RunProgramDescription"                                 
                   ]
    __ARG_TAG    = "Argument"
    
    @staticmethod
    def path() :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwConfigXml.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) ) 

    @staticmethod
    def dirPath() :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwConfigXml.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )     
    
    def __init__( self, name, exeName, version, publisher, 
                  iconFilePath=None, 
                  isDefaultTitle=True, isDefaultPaths=True ) :
        # TODO: expand on the built-in attributes here...
        self.exeName = util._normExeName( exeName )
        self.iconFilePath = iconFilePath        
        try:    iconBaseName = splitExt( basename(iconFilePath) )[0]
        except: iconBaseName = None
        self.Name                     = name
        self.Version                  = version
        self.Publisher                = publisher
        self.InstallerApplicationIcon = iconBaseName 
        self.Title                    = None        
        self.TargetDir                = None        
        self.StartMenuDir             = None
        self.RunProgram               = None
        self.RunProgramDescription    = None
        self.runProgramArgList        = None                
        self.otherElements            = {}
        if isDefaultTitle: self.setDefaultTitle()
        if isDefaultPaths: self.setDefaultPaths()

    def setDefaultVersion( self ) :
        # TODO: extract version info from primary exe?
        if self.Version is None: self.Version = "1.0.0" 

    def setDefaultTitle( self ) :
        if self.Title is None: 
            self.Title = ("%s Setup" % (self.Name)).strip()
    
    def setDefaultPaths( self ) :        
        if self.exeName is not None: 
            # NOTE: THE WORKING DIRECTORY IS NOT SET FOR RUN PROGRAM!
            # THERE DOES NOT SEEM TO BE AN OPTION YET FOR THIS IN QT IFW        
            self.RunProgram = "@TargetDir@/%s" % (self.exeName,)        
        if (self.Publisher is not None) and (self.Name is not None):    
            self.TargetDir = ( "@ApplicationsDir@/%s/%s" % 
                                (self.Publisher, self.Name) )
        if IS_WINDOWS:
            if self.Publisher is not None :
                self.StartMenuDir = self.Publisher
                            
    def __str__( self ) :        
        class XmlElement(ET.Element):
            def __init__(self, tag, text=None, parent=None, attrib={}, **extra):
                ET.Element.__init__(self, tag, attrib, **extra)
                if text: self.text = text
                if parent is not None: parent.append( self )                            
        root = XmlElement( QtIfwConfigXml.__ROOT )
        for k, v in six.iteritems( self.__dict__ ) :
            if k in QtIfwConfigXml.__TAGS and v is not None : 
                XmlElement( k, v, root )                        
        if self.runProgramArgList is not None and self.RunProgram is not None:            
            for arg in self.runProgramArgList:
                XmlElement( QtIfwConfigXml.__ARG_TAG, arg, root )                
        for k, v in six.iteritems( self.otherElements ) : XmlElement( k, v, root )
        xml = ET.tostring( root )        
        return QtIfwConfigXml.__HEADER + (xml.decode() if six.PY3 else xml) 
        
    def write( self ):
        configDir = QtIfwConfigXml.dirPath()
        if not isDir( configDir ): makeDir( configDir )
        with open( QtIfwConfigXml.path(), 'w' ) as f: 
            print(str(self))
            f.write( minidom.parseString( str(self) ).toprettyxml() ) 
        
# -----------------------------------------------------------------------------            
def buildInstaller( qtIfwConfig, qtIfwConfigXml=None, 
                    isPkgSrcRemoved=False ):
    ''' returns setupExePath '''
        
    __validateConfig( qtIfwConfig )        
    __initBuild( qtIfwConfig )    
    __addInstallerResources( qtIfwConfigXml )     
    if qtIfwConfig.othContentPaths is not None : __addOtherFiles( qtIfwConfig )     
    if qtIfwConfig.isQtCppExe : __addQtCppDependencies( qtIfwConfig )        
    setupExePath = __build( qtIfwConfig )    
    __postBuild( qtIfwConfig, isPkgSrcRemoved )
    return setupExePath

# -----------------------------------------------------------------------------
def __validateConfig( qtIfwConfig ):
    ''' Very superficial validation... '''
    # installer definition requirements
    if qtIfwConfig.pkgName is None :
        raise Exception( "Package Name required" )
    if qtIfwConfig.installerDefDirPath is None:
        qtIfwConfig.installerDefDirPath = absPath( INSTALLER_DIR_PATH )         
    if not isDir(qtIfwConfig.installerDefDirPath):        
        raise Exception( "Valid Installer Definition directory path required" )
    if qtIfwConfig.pkgSrcDirPath is None:
        if qtIfwConfig.pkgSrcExePath is None:
            raise Exception( "Package Source directory OR exe path required" )
        elif not isFile(qtIfwConfig.pkgSrcExePath) :        
            raise Exception( "Package Source exe path is not valid" )    
    elif not isDir(qtIfwConfig.pkgSrcDirPath) :        
        raise Exception( "Package Source directory path is not valid" )
    # tool path requirements
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = getenv( QT_IFW_DIR_ENV_VAR )    
    if( qtIfwConfig.qtIfwDirPath is None or
        not isDir(qtIfwConfig.qtIfwDirPath) ):        
        raise Exception( "Valid Qt IFW directory path required" )
    if qtIfwConfig.isQtCppExe : 
        if qtIfwConfig.qtBinDirPath is None:
            qtIfwConfig.qtBinDirPath = getenv( QT_BIN_DIR_ENV_VAR )    
        if( qtIfwConfig.qtBinDirPath is None or
            not isDir(qtIfwConfig.qtBinDirPath) ):        
            raise Exception( "Valid Qt Bin directory path required" )

def __initBuild( qtIfwConfig ) :
    print( "Initializing installer build..." )
    # remove any prior setup file
    setupExePath = joinPath( THIS_DIR, qtIfwConfig.setupExeName )
    if exists( setupExePath ) : removeFile( setupExePath )
    # create a "clean" build directory
    if exists( BUILD_SETUP_DIR_PATH ) : removeDir( BUILD_SETUP_DIR_PATH )
    makeDir( BUILD_SETUP_DIR_PATH )    
    # copy the installer definition to the build directory   
    copyDir( qtIfwConfig.installerDefDirPath, 
             joinPath( BUILD_SETUP_DIR_PATH, INSTALLER_DIR_PATH ) )
    # copy the source content into the build directory
    destDir = qtIfwConfig.pkgContentDirPath()            
    if qtIfwConfig.pkgSrcDirPath : 
        qtIfwConfig.pkgSrcDirPath = normpath( qtIfwConfig.pkgSrcDirPath )
        copyDir( qtIfwConfig.pkgSrcDirPath, destDir )    
    if qtIfwConfig.pkgSrcExePath :
        srcExeDir, srcExeName = splitPath( qtIfwConfig.pkgSrcExePath )
        if srcExeDir != qtIfwConfig.pkgSrcDirPath :                    
            copyFile( qtIfwConfig.pkgSrcExePath, destDir )                
        if qtIfwConfig.exeName is None: qtIfwConfig.exeName = srcExeName 
        elif qtIfwConfig.exeName != srcExeName :             
            rename( joinPath( destDir, srcExeName ),
                    joinPath( destDir, qtIfwConfig.exeName ) )            
    print( "Build directory created: %s" % (BUILD_SETUP_DIR_PATH,) )

def __addInstallerResources( qtIfwConfigXml ) :    
    if qtIfwConfigXml : 
        print( "Adding installer resources..." )
        qtIfwConfigXml.write()
        if( qtIfwConfigXml.iconFilePath and 
            isFile( qtIfwConfigXml.iconFilePath ) ):
            copyFile( qtIfwConfigXml.iconFilePath,                       
                      joinPath( qtIfwConfigXml.dirPath(), 
                        basename( qtIfwConfigXml.iconFilePath ) ) )

def __addOtherFiles( qtIfwConfig ) :    
    print( "Adding additional files..." )
    destPath = qtIfwConfig.pkgContentDirPath()            
    for srcPath in qtIfwConfig.othContentPaths:
        if isDir( srcPath ) : copyDir( srcPath, destPath )
        else : copyFile( srcPath, joinPath( destPath, basename( srcPath ) ) )

def __addQtCppDependencies( qtIfwConfig ) :
    # TODO: Add the counterparts here for other platforms
    if IS_WINDOWS :
        print( "Adding Qt C++ dependencies...\n" )
        qtUtilityPath =  normpath( joinPath(
            qtIfwConfig.qtBinDirPath, __QT_WINDOWS_DEPLOY_EXE_NAME ) )
        destDirPath = qtIfwConfig.pkgContentDirPath()
        exePath = joinPath( destDirPath, qtIfwConfig.exeName )
        cmdList = [qtUtilityPath, exePath]
        if qtIfwConfig.qmlScrDirPath is not None:
            cmdList.append( __QT_WINDOWS_DEPLOY_QML_SWITCH )
            cmdList.append( normpath( qtIfwConfig.qmlScrDirPath ) )
        cmd = list2cmdline( cmdList )
        system( cmd )
        if qtIfwConfig.isMingwExe :
            print( "Adding additional Qt dependencies..." )
            for fileName in __MINGW_DLL_LIST:
                copyFile( normpath( qtIfwConfig.qtBinDirPath ), 
                          joinPath( destDirPath, fileName ) )

def __build( qtIfwConfig ) :
    print( "Building installer using Qt IFW...\n" )
    qtUtilityPath = joinPath( qtIfwConfig.qtIfwDirPath, 
        joinPath( __BIN_SUB_DIR, __QT_INSTALL_CREATOR_EXE_NAME ) )
    setupExePath = joinPath( THIS_DIR, qtIfwConfig.setupExeName )
    cmd = '%s %s "%s"' % ( qtUtilityPath, str(qtIfwConfig), setupExePath )
    util._system( cmd )  
    if exists( setupExePath ) : print( "Created %s!" % (setupExePath,) )
    else: raise Exception( "FAILED to create %s" % (setupExePath,) )
    return setupExePath

def __postBuild( qtIfwConfig, isPkgSrcRemoved ):  # @UnusedVariable
    removeDir( BUILD_SETUP_DIR_PATH )
    if isPkgSrcRemoved and isDir( qtIfwConfig.pkgSrcDirPath ): 
        removeDir( qtIfwConfig.pkgSrcDirPath )
