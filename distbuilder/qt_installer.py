import six
from distbuilder import util
from distbuilder.util import *  # @UnusedWildImport
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import date
from abc import ABCMeta, abstractmethod

BUILD_SETUP_DIR_PATH = absPath( "build_setup" )
INSTALLER_DIR_PATH = "installer"
DEFAULT_SETUP_NAME = util._normExeName( "setup" )
DEFAULT_QT_IFW_SCRIPT_NAME = "installscript.qs"

QT_IFW_VERBOSE_SWITCH = '-v'

QT_IFW_DIR_ENV_VAR = "QT_IFW_DIR"
QT_BIN_DIR_ENV_VAR = "QT_BIN_DIR"

__BIN_SUB_DIR = "bin"
__QT_INSTALL_CREATOR_EXE_NAME = util._normExeName( "binarycreator" )

__QT_WINDOWS_DEPLOY_EXE_NAME   = "windeployqt.exe"
__QT_WINDOWS_DEPLOY_QML_SWITCH = "--qmldir"
__MINGW_DLL_LIST = [
      "libgcc_s_dw2-1.dll"
    , "libstdc++-6.dll"
    , "libwinpthread-1.dll"
]

DESKTOP_WIN_SHORTCUT           = 0
STARTMENU_WIN_SHORTCUT         = 1
THIS_USER_STARTUP_WIN_SHORTCUT = 2
ALL_USERS_STARTUP_WIN_SHORTCUT = 3

# -----------------------------------------------------------------------------
class QtIfwConfig:
    """
    Refer to the Qt Installer Framework docs for command line usage details.
    """    
    
    __PACKAGES_PATH_TMPLT = "%s/packages"
    __CONTENT_PATH_TMPLT = "%s/packages/%s/data" 
    
    def __init__( self, 
                  pkgSrcDirPath=None, pkgSrcExePath=None,                  
                  pkgName=None, installerDefDirPath=None,
                  configXml=None, pkgXml=None, pkgScript=None,
                  setupExeName=DEFAULT_SETUP_NAME ) :       
        # definition
        self.pkgName             = pkgName
        self.installerDefDirPath = installerDefDirPath
        self.configXml           = configXml
        self.pkgXml              = pkgXml
        self.pkgScript           = pkgScript        
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
        configSpec   = '-c "%s"' % (self.configXml.path() if self.configXml 
                                    else QtIfwConfigXml().path(),)
        packagesSpec = '-p "%s"' % (self.pkgDirPath(),)
        verboseSpec  = '-v' if self.isDebugMode else ''                
        tokens = (configSpec, packagesSpec, verboseSpec, self.otherqtIfwArgs)
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

    def pkgDirPath( self ) :  
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwConfig.__PACKAGES_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )
            
    def pkgContentDirPath( self ) :
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwConfig.__CONTENT_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName,) ) )

# -----------------------------------------------------------------------------    
class _QtIfwXmlElement( ET.Element ):
    def __init__( self, tag, text=None, parent=None, attrib={}, **extra ):
        ET.Element.__init__( self, tag, attrib, **extra )
        if text:
            if   isinstance(text, bool): text = str(text)
            elif isinstance(text, date): text = text.isoformat() 
            self.text = text
        if parent is not None: parent.append( self )                                                        

# -----------------------------------------------------------------------------
@six.add_metaclass(ABCMeta)
class _QtIfwXml():

    __HEADER = '<?xml version="1.0" encoding="UTF-8"?>'

    def __init__( self, rootTag, tags ) :
        self.rootTag       = rootTag
        self.tags          = tags 
        self.otherElements = {}
        
    def __str__( self ) :        
        root = _QtIfwXmlElement( self.rootTag )
        for k, v in six.iteritems( self.__dict__ ) :
            if k in self.tags and v is not None : 
                _QtIfwXmlElement( k, v, root )                                        
        for k, v in six.iteritems( self.otherElements ) : 
            _QtIfwXmlElement( k, v, root )
        self.addCustomTags( root )    
        xml = ET.tostring( root )        
        return _QtIfwXml.__HEADER + (xml if six.PY2 else xml.decode()) 

    def toPrettyXml( self ):
        return minidom.parseString( str(self) ).toprettyxml()

    def addCustomTags( self, root ) : """VIRTUAL"""

    @abstractmethod
    def path( self ) : """PURE VIRTUAL"""

    @abstractmethod
    def dirPath( self ) : """PURE VIRTUAL"""    
        
    def write( self ):
        dirPath = self.dirPath()
        if not isDir( dirPath ): makeDir( dirPath )
        with open( self.path(), 'w' ) as f: 
            f.write( self.toPrettyXml() ) 

    def debug( self ): print( self.toPrettyXml() )
            
# -----------------------------------------------------------------------------    
class QtIfwConfigXml( _QtIfwXml ):
    
    __DIR_TMPLT  = "%s/config"
    __PATH_TMPLT = __DIR_TMPLT + "/config.xml"
    __ROOT_TAG   = "Installer"
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
        
    def __init__( self, name, exeName, version, publisher,
                  companyTradeName=None, iconFilePath=None ) :
        _QtIfwXml.__init__( self, QtIfwConfigXml.__ROOT_TAG, 
                            QtIfwConfigXml.__TAGS )
       
        self.exeName = util._normExeName( exeName )
        self.iconFilePath = iconFilePath        
        try:    iconBaseName = splitExt( basename(iconFilePath) )[0]
        except: iconBaseName = None
        self.companyTradeName = ( companyTradeName if companyTradeName 
                                  else publisher.replace(".","") )
        self.runProgramArgList = None

        # TODO: expand on the built-in attributes here...        
        self.Name                     = name
        self.Version                  = version
        self.Publisher                = publisher
        self.InstallerApplicationIcon = iconBaseName 
        self.Title                    = None        
        self.TargetDir                = None        
        self.StartMenuDir             = None
        self.RunProgram               = None
        self.RunProgramDescription    = None
                       
        self.setDefaultTitle()
        self.setDefaultPaths()

    def setDefaultVersion( self ) :
        # TODO: extract version info from primary exe?
        if self.Version is None: self.Version = "1.0.0" 

    def setDefaultTitle( self ) :
        if self.Title is None: self.Title = self.Name
            #self.Title = "%s Setup" % (self.Name) # New IFW seem to be adding "Setup" suffix?
    
    def setDefaultPaths( self ) :        
        if self.exeName is not None: 
            # NOTE: THE WORKING DIRECTORY IS NOT SET FOR RUN PROGRAM!
            # THERE DOES NOT SEEM TO BE AN OPTION YET FOR THIS IN QT IFW        
            self.RunProgram = "@TargetDir@/%s" % (self.exeName,)        
        if (self.companyTradeName is not None) and (self.Name is not None):    
            self.TargetDir = ( "@ApplicationsDir@/%s/%s" % 
                                (self.companyTradeName, self.Name) )
        if IS_WINDOWS:
            if self.companyTradeName is not None :
                self.StartMenuDir = self.companyTradeName
                                
    def addCustomTags( self, root ) :
        if self.runProgramArgList is not None and self.RunProgram is not None:            
            for arg in self.runProgramArgList:
                _QtIfwXmlElement( QtIfwConfigXml.__ARG_TAG, arg, root )                
        
    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwConfigXml.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwConfigXml.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )     
    
# -----------------------------------------------------------------------------    
class QtIfwPackageXml( _QtIfwXml ):
    
    __DIR_TMPLT  = "%s/packages/%s/meta"
    __PATH_TMPLT = __DIR_TMPLT + "/package.xml"
    __ROOT_TAG   = "Package"
    __TAGS       = [ "DisplayName"
                   , "Description"
                   , "Version"
                   , "ReleaseDate"    
                   , "Default"
                   , "Script"                                 
                   ]
        
    def __init__( self, pkgName, displayName, description, 
                  version, scriptName=None, isDefault=True ) :
        _QtIfwXml.__init__( self, QtIfwPackageXml.__ROOT_TAG, 
                            QtIfwPackageXml.__TAGS )        
        self.pkgName       = pkgName
        
        # TODO: expand on the built-in attributes here...
        self.DisplayName   = displayName
        self.Description   = description
        self.Version       = version            
        self.Script        = scriptName 
        self.Default       = isDefault
        self.ReleaseDate   = date.today()
                            
    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageXml.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageXml.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) )     

# -----------------------------------------------------------------------------    
class QtIfwPackageScript:
    
    __DIR_TMPLT  = "%s/packages/%s/meta"
    __PATH_TMPLT = __DIR_TMPLT + "/%s"

    __WIN_ADD_SHORTCUT_TMPLT = ( 
"""
        component.addOperation( "CreateShortcut",
            "[EXE_PATH]",
            "[SHORTCUT_PATH]",
            "workingDirectory=[WORKING_DIR]",
            "iconPath=[ICON_PATH]",
            "iconId=[ICON_ID]"        
        );    
""" )

    __X11_ADD_DESKTOP_ENTRY_TMPLT = ( 
"""
        component.addOperation( "CreateDesktopEntry", 
            "/usr/share/applications/[APP_NAME].desktop", 
            "Version=1.0\nType=Application\nTerminal=false\nExec=@TargetDir@/[EXE_NAME]\nName=[APP_NAME]\nIcon=@TargetDir@[APP_ICON_PNG]\nName[en_US]=[APP_NAME]"
        );    
""" )

    __X11_COPY_DESKTOP_ENTRY_TO_DESKTOP_TMPLT = ( 
"""
        component.addElevatedOperation( "Copy", 
            "/usr/share/applications/[APP_NAME].desktop", 
            "@HomeDir@/Desktop/[APP_NAME].desktop"
        );
""" )
     
    __WIN_SHORTCUT_LOCATIONS = {
          DESKTOP_WIN_SHORTCUT          : "@DesktopDir@"
        , STARTMENU_WIN_SHORTCUT        : "@StartMenuDir@"
        , THIS_USER_STARTUP_WIN_SHORTCUT: "@UserStartMenuProgramsPath@/Startup"
        , ALL_USERS_STARTUP_WIN_SHORTCUT: "@AllUsersMenuProgramsPath@/Startup"    
    }

    @staticmethod
    def __winAddShortcut( location, exeName, 
                          label="@ProductName@", 
                          directory="@TargetDir@", 
                          iconId=0 ):        
        exePath = "%s/%s" % (directory, util._normExeName( exeName ))
        locDir = QtIfwPackageScript.__WIN_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s.lnk" % (locDir, label)        
        s = QtIfwPackageScript.__WIN_ADD_SHORTCUT_TMPLT
        s = s.replace( "[EXE_PATH]", exePath )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        s = s.replace( "[WORKING_DIR]", directory )
        s = s.replace( "[ICON_PATH]", exePath )
        s = s.replace( "[ICON_ID]", str(iconId) )
        return s 
    
    def __init__( self, pkgName, fileName=DEFAULT_QT_IFW_SCRIPT_NAME, 
                  exeName=None, script=None, srcPath=None ) :
        self.pkgName  = pkgName
        self.fileName = fileName
        if srcPath :
            with open( srcPath, 'rb' ) as f: self.script = f.read()
        else : self.script = script  

        self.componentConstructorBody = None
        self.isAutoComponentConstructor = True
        
        self.componentCreateOperationsBody = None
        self.isAutoComponentCreateOperations = True        
        self.exeName = exeName   
        self.isWinStartMenuShortcut = True
        self.isWinDesktopShortcut   = False
                            
    def __str__( self ) : 
        if not self.script: self._generate()
        return self.script
            
    def _generate( self ) :        
        self.script = ""
        if self.isAutoComponentConstructor:
            self.__genComponentConstructorBody()
        self.script += ( "function Component() {\n%s\n}\n" % 
                         (self.componentConstructorBody,) )
        if self.isAutoComponentCreateOperations:
            self.__genComponentCreateOperationsBody()
        if self.componentCreateOperationsBody:
            self.script += (
                "\nComponent.prototype.createOperations = function() {\n" +
                "    component.createOperations(); // call to super class\n" +
                "%s\n}\n" % (self.componentCreateOperationsBody,) )

    def __genComponentConstructorBody( self ):
        """ No logic yet provided... """
        self.componentConstructorBody = ""   
            
    def __genComponentCreateOperationsBody( self ):
        self.componentCreateOperationsBody = ""        
        if IS_WINDOWS:
            winOps=""
            if self.exeName and self.isWinStartMenuShortcut :
                winOps += QtIfwPackageScript.__winAddShortcut(
                        STARTMENU_WIN_SHORTCUT, self.exeName )              
            if self.exeName and self.isWinDesktopShortcut:
                winOps += QtIfwPackageScript.__winAddShortcut(
                        DESKTOP_WIN_SHORTCUT, self.exeName ) 
            if winOps!="" :    
                self.componentCreateOperationsBody += (             
                    '    if( systemInfo.productType === "windows" ){\n' +
                    '%s\n    }' % (winOps,) )            
        if self.componentCreateOperationsBody == "" :
            self.componentCreateOperationsBody = None

    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageScript.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName, 
                         self.fileName) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageScript.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) )     
    
    def write( self ):
        pkgDir = self.dirPath()
        if not isDir( pkgDir ): makeDir( pkgDir )
        with open( self.path(), 'w' ) as f: 
            f.write( str(self) ) 
    
    def debug( self ): print( str(self) )
        
# -----------------------------------------------------------------------------            
def buildInstaller( qtIfwConfig, isPkgSrcRemoved=False ):
    ''' returns setupExePath '''
    __validateConfig( qtIfwConfig )        
    __initBuild( qtIfwConfig )    
    __addInstallerResources( qtIfwConfig )     
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
    if( qtIfwConfig.installerDefDirPath is not None and
        not isDir(qtIfwConfig.installerDefDirPath) ):        
        raise Exception( "Installer definition directory path is not valid" )
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
    setupExePath = joinPath( THIS_DIR, 
                             util._normExeName( qtIfwConfig.setupExeName ) )
    if exists( setupExePath ) : removeFile( setupExePath )
    # create a "clean" build directory
    if exists( BUILD_SETUP_DIR_PATH ) : removeDir( BUILD_SETUP_DIR_PATH )
    makeDir( BUILD_SETUP_DIR_PATH )    
    # copy the installer definition to the build directory
    if qtIfwConfig.installerDefDirPath :   
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

def __addInstallerResources( qtIfwConfig ) :    
    configXml = qtIfwConfig.configXml          
    pkgXml = qtIfwConfig.pkgXml              
    pkgScript = qtIfwConfig.pkgScript                   
    if configXml : 
        print( "Adding installer configuration resources..." )
        configXml.debug()
        configXml.write()        
        if( configXml.iconFilePath and 
            isFile( configXml.iconFilePath ) ):
            copyFile( configXml.iconFilePath,                       
                      joinPath( configXml.dirPath(), 
                        basename( configXml.iconFilePath ) ) )
    if pkgXml :            
        print( "Adding installer package definition: %s..." 
               % (pkgXml.pkgName) )
        pkgXml.debug()
        pkgXml.write()            
    if pkgScript :
        print( "Adding installer package script: %s..." 
               % (pkgScript.fileName) )
        pkgScript.debug()
        pkgScript.write()            

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
    setupExePath = joinPath( THIS_DIR, 
                             util._normExeName( qtIfwConfig.setupExeName ) )
    cmd = '%s %s "%s"' % ( qtUtilityPath, str(qtIfwConfig), setupExePath )
    util._system( cmd )  
    if exists( setupExePath ) : print( "Created %s!" % (setupExePath,) )
    else: raise Exception( "FAILED to create %s" % (setupExePath,) )
    return setupExePath

def __postBuild( qtIfwConfig, isPkgSrcRemoved ):  # @UnusedVariable
    removeDir( BUILD_SETUP_DIR_PATH )
    if isPkgSrcRemoved and isDir( qtIfwConfig.pkgSrcDirPath ): 
        removeDir( qtIfwConfig.pkgSrcDirPath )
