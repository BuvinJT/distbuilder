import six
from distbuilder import util
from distbuilder.util import *  # @UnusedWildImport
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import date
from abc import ABCMeta, abstractmethod

BUILD_SETUP_DIR_PATH = absPath( "build_setup" )
INSTALLER_DIR_PATH = "installer"
DEFAULT_SETUP_NAME = util.normBinaryName( "setup" )
DEFAULT_QT_IFW_SCRIPT_NAME = "installscript.qs"

QT_IFW_VERBOSE_SWITCH = '-v'

QT_IFW_DIR_ENV_VAR = "QT_IFW_DIR"
QT_BIN_DIR_ENV_VAR = "QT_BIN_DIR"

__BIN_SUB_DIR = "bin"
__QT_INSTALL_CREATOR_EXE_NAME = util.normBinaryName( "binarycreator" )

__QT_WINDOWS_DEPLOY_EXE_NAME   = "windeployqt.exe"
__QT_WINDOWS_DEPLOY_QML_SWITCH = "--qmldir"
__MINGW_DLL_LIST = [
      "libgcc_s_dw2-1.dll"
    , "libstdc++-6.dll"
    , "libwinpthread-1.dll"
]

STARTMENU_WIN_SHORTCUT         = 0
DESKTOP_WIN_SHORTCUT           = 1
THIS_USER_STARTUP_WIN_SHORTCUT = 2
ALL_USERS_STARTUP_WIN_SHORTCUT = 3

APPS_MAC_SHORTCUT    = 0              
DESKTOP_MAC_SHORTCUT = 1             
                
APPS_X11_SHORTCUT    = 0
DESKTOP_X11_SHORTCUT = 1

# -----------------------------------------------------------------------------
class QtIfwConfig:
    """
    Refer to the Qt Installer Framework docs for command line usage details.
    """    
    
    def __init__( self, 
                  installerDefDirPath=None,
                  packages=None,
                  configXml=None, 
                  setupExeName=DEFAULT_SETUP_NAME ) :       
        self.installerDefDirPath = installerDefDirPath
        self.packages            = packages # list of QtIfwPackages or directory paths
        self.configXml           = configXml        
        self.setupExeName        = setupExeName
        # Qt paths (attempt to use environmental variables if not defined)
        self.qtIfwDirPath = None
        self.qtBinDirPath = None          
        # other IFW command line options
        self.isDebugMode    = True
        self.otherQtIfwArgs = ""
                
    def __str__( self ) :
        configSpec   = '-c "%s"' % (self.configXml.path() if self.configXml 
                                    else QtIfwConfigXml().path(),)
        packagesSpec = ""
        try:             
            for p in self.packages: packagesSpec += ' -p "%s"' % (str(p),)
        except: pass       
        verboseSpec  = '-v' if self.isDebugMode else ''                
        tokens = (configSpec, packagesSpec, verboseSpec, self.otherQtIfwArgs)
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

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
    __RUN_ARGS_TAG = "RunProgramArguments"
    __ARG_TAG      = "Argument"
        
    def __init__( self, name, exeName, version, publisher,
                  iconFilePath=None, isGui=True,
                  companyTradeName=None ) :
        _QtIfwXml.__init__( self, QtIfwConfigXml.__ROOT_TAG, 
                            QtIfwConfigXml.__TAGS )
       
        self.exeName = util.normBinaryName( exeName, isGui=isGui )
        if IS_LINUX :
            # qt installer does not support icon embedding in Linux
            iconBaseName = self.iconFilePath = None
        else :    
            self.iconFilePath = util._normIconName( iconFilePath, 
                                                    isPathPreserved=True )        
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
        if( self.companyTradeName is not None and 
            self.Name is not None ):
            # On macOS, self-contained "app bundles" are typically dropped 
            # into "Applications", but "traditional" directories e.g.
            # what QtIFW installs (with the .app contained within it)
            # are NOT placed there.  Instead, the user's home directory
            # seems more typical, with a link perhaps also appearing 
            # in Applications.  On Linux and Windows, @ApplicationsDir@
            # resolves to a typical (cross user) apps location.       
            dirVar = "@HomeDir@" if IS_MACOS else "@ApplicationsDir@"
            subDir = "%s/%s" % (self.companyTradeName, self.Name) 
            self.TargetDir = "%s/%s" % (dirVar, subDir)
        if IS_WINDOWS:
            if self.companyTradeName is not None :
                self.StartMenuDir = self.companyTradeName
        if self.exeName is not None: 
            # NOTE: THE WORKING DIRECTORY IS NOT SET FOR RUN PROGRAM!
            # THERE DOES NOT SEEM TO BE AN OPTION YET FOR THIS IN QT IFW   
            programPath = "@TargetDir@/%s" % (self.exeName,)    
            if util._isMacApp( self.exeName ):   
                self.RunProgram = util._LAUNCH_MACOS_APP_CMD 
                if not isinstance( self.runProgramArgList, list ) :
                    self.runProgramArgList = []
                self.runProgramArgList.insert(0, programPath)
            else : self.RunProgram = programPath                    
                                     
    def addCustomTags( self, root ) :
        if( self.RunProgram is not None and 
            self.runProgramArgList is not None ):            
            runArgs = _QtIfwXmlElement( QtIfwConfigXml.__RUN_ARGS_TAG, 
                                        None, root )
            for arg in self.runProgramArgList:
                _QtIfwXmlElement( QtIfwConfigXml.__ARG_TAG, arg, runArgs )                
        
    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwConfigXml.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwConfigXml.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )     
    
# -----------------------------------------------------------------------------
class QtIfwPackage:
    
    __PACKAGES_PATH_TMPLT = "%s/packages"
    __CONTENT_PATH_TMPLT = "%s/packages/%s/data" 
    
    def __init__( self, name=None, 
                  srcDirPath=None, srcExePath=None,    
                  isTempSrc=False,
                  pkgXml=None, pkgScript=None ) :       
        # definition
        self.name            = name
        self.pkgXml          = pkgXml
        self.pkgScript       = pkgScript        
        # content        
        self.srcDirPath      = srcDirPath
        self.srcExePath      = srcExePath
        self.othContentPaths = None
        self.isTempSrc       = isTempSrc                     
        # extended content detail
        self.exeName      = None   
        self.isQtCppExe     = False
        self.isMingwExe     = False
        self.qmlScrDirPath  = None  # for QML projects only   

    def dirPath( self ) :  
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwPackage.__PACKAGES_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )
            
    def contentDirPath( self ) :
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwPackage.__CONTENT_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.name,) ) )
    
    def __str__(self): return self.dirPath()
    
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

    # an example for use down the line...
    __LINUX_GET_DISTRIBUTION = ( 
"""
        var IS_UBUNTU   = (systemInfo.productType === "ubuntu");
        var IS_OPENSUSE = (systemInfo.productType === "opensuse");             
""" )

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

    __MAC_ADD_SYMLINK_TMPLT = ( 
"""
        component.addOperation( "CreateLink",  
            "[SHORTCUT_PATH]",
            "[EXE_PATH]"
        );    
""" )

    __X11_ADD_DESKTOP_ENTRY_TMPLT = ( 
"""
        component.addOperation( "CreateDesktopEntry", 
            "[SHORTCUT_PATH]",
            "Type=Application\\n" 
          + "Terminal=[IS_TERMINAL]\\n" 
          + "Exec=bash -c 'cd \\\"[WORKING_DIR]\\\" && \\\"[EXE_PATH]\\\"'\\n"
          + "Name=[LABEL]\\n" 
          + "Name[en_US]=[LABEL]\\n" 
          + "Version=[VERSION]\\n" 
          + "Icon=[PNG_PATH]\\n"                     
        );    
""" )
     
    __WIN_SHORTCUT_LOCATIONS = {
          DESKTOP_WIN_SHORTCUT          : "@DesktopDir@"
        , STARTMENU_WIN_SHORTCUT        : "@StartMenuDir@"
        , THIS_USER_STARTUP_WIN_SHORTCUT: "@UserStartMenuProgramsPath@/Startup"
        , ALL_USERS_STARTUP_WIN_SHORTCUT: "@AllUsersMenuProgramsPath@/Startup"    
    }

    __MAC_SHORTCUT_LOCATIONS = {
          DESKTOP_MAC_SHORTCUT : "@HomeDir@/Desktop"
        , APPS_MAC_SHORTCUT    : "@HomeDir@/Applications" 
    }

    # these may not be correct on all distros?
    __X11_SHORTCUT_LOCATIONS = {
          DESKTOP_X11_SHORTCUT : "@HomeDir@/Desktop"
        , APPS_X11_SHORTCUT    : "/usr/share/applications" 
    }

    @staticmethod
    def __winAddShortcut( location, exeName, 
                          label="@ProductName@", 
                          directory="@TargetDir@", 
                          iconId=0 ):        
        exePath = "%s/%s" % (directory, util.normBinaryName( exeName ))
        locDir = QtIfwPackageScript.__WIN_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s.lnk" % (locDir, label)        
        s = QtIfwPackageScript.__WIN_ADD_SHORTCUT_TMPLT
        s = s.replace( "[EXE_PATH]", exePath )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        s = s.replace( "[WORKING_DIR]", directory )
        s = s.replace( "[ICON_PATH]", exePath )
        s = s.replace( "[ICON_ID]", str(iconId) )
        return s 

    @staticmethod
    def __macAddShortcut( location, exeName, isGui,
                          label="@ProductName@", 
                          directory="@TargetDir@" ):        
        exePath = "%s/%s" % (directory, util.normBinaryName( exeName, 
                                                             isGui=isGui ))
        locDir = QtIfwPackageScript.__MAC_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s" % (locDir, label)        
        s = QtIfwPackageScript.__MAC_ADD_SYMLINK_TMPLT
        s = s.replace( "[EXE_PATH]", exePath )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        return s 

    @staticmethod
    def __linuxAddDesktopEntry( location, exeName, version, 
                                label="@ProductName@", 
                                directory="@TargetDir@", 
                                pngPath=None,
                                isGui=True ):        
        exePath = "%s/%s" % (directory, util.normBinaryName( exeName ))
        locDir = QtIfwPackageScript.__X11_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s.desktop" % (locDir, label.replace(" ","_"))        
        s = QtIfwPackageScript.__X11_ADD_DESKTOP_ENTRY_TMPLT
        s = s.replace( "[EXE_PATH]", exePath )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        s = s.replace( "[LABEL]", label )
        s = s.replace( "[VERSION]", version )
        s = s.replace( "[PNG_PATH]", "" if pngPath is None else 
                                     joinPath( "@TargetDir@", pngPath ) )
        s = s.replace( "[IS_TERMINAL]", "false" if isGui else "true" )
        s = s.replace( "[WORKING_DIR]", directory )        
        return s 
    
    def __init__( self, pkgName, fileName=DEFAULT_QT_IFW_SCRIPT_NAME, 
                  exeName=None, isGui=True, 
                  script=None, scriptPath=None ) :
        self.pkgName  = pkgName
        self.fileName = fileName
        if scriptPath :
            with open( scriptPath, 'rb' ) as f: self.script = f.read()
        else : self.script = script  

        self.exeName = exeName   
        self.isGui   = isGui
        
        self.exeVersion = "0.0.0.0"        
        self.pngIconResPath = None
        
        self.isAppShortcut     = True
        self.isDesktopShortcut = False

        self.componentConstructorBody = None
        self.isAutoComponentConstructor = True
        
        self.componentCreateOperationsBody = None
        self.isAutoComponentCreateOperations = True
                                            
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
            if self.exeName and self.isAppShortcut :
                winOps += QtIfwPackageScript.__winAddShortcut(
                        STARTMENU_WIN_SHORTCUT, self.exeName )              
            if self.exeName and self.isDesktopShortcut:
                winOps += QtIfwPackageScript.__winAddShortcut(
                        DESKTOP_WIN_SHORTCUT, self.exeName ) 
            if winOps!="" :    
                self.componentCreateOperationsBody += (             
                    '    if( systemInfo.kernelType === "winnt" ){\n' +
                    '%s\n    }' % (winOps,) )
        elif IS_MACOS:
            macOps = ""
            if self.exeName and self.isAppShortcut :
                macOps += QtIfwPackageScript.__macAddShortcut(
                        APPS_MAC_SHORTCUT, self.exeName,
                        self.isGui )              
            if self.exeName and self.isDesktopShortcut:
                macOps += QtIfwPackageScript.__macAddShortcut(
                        DESKTOP_MAC_SHORTCUT, self.exeName,
                        self.isGui )             
            if macOps!="" :    
                self.componentCreateOperationsBody += (             
                    '    if( systemInfo.kernelType === "darwin" ){\n' +
                    '%s\n    }' % (macOps,) )                    
        elif IS_LINUX:
            x11Ops = ""
            if self.exeName and self.isAppShortcut :
                x11Ops += QtIfwPackageScript.__linuxAddDesktopEntry(
                        APPS_X11_SHORTCUT, self.exeName, self.exeVersion,
                        pngPath=self.pngIconResPath,
                        isGui=self.isGui )                
            if self.exeName and self.isDesktopShortcut:
                x11Ops += QtIfwPackageScript.__linuxAddDesktopEntry(
                        DESKTOP_X11_SHORTCUT, self.exeName, self.exeVersion,
                        pngPath=self.pngIconResPath,
                        isGui=self.isGui )                               
            if x11Ops!="" :    
                self.componentCreateOperationsBody += (             
                    '    if( systemInfo.kernelType === "linux" ){\n' +
                    '%s\n    }' % (x11Ops,) )                                
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
def buildInstaller( qtIfwConfig ):
    ''' returns setupExePath '''
    __validateConfig( qtIfwConfig )        
    __initBuild( qtIfwConfig )    
    __addInstallerResources( qtIfwConfig )     
    setupExePath = __build( qtIfwConfig )    
    __postBuild( qtIfwConfig )
    return setupExePath

# -----------------------------------------------------------------------------
def __validateConfig( qtIfwConfig ):
    ''' Very superficial validation... '''
    # installer definition requirements
    if( qtIfwConfig.installerDefDirPath is not None and
        not isDir(qtIfwConfig.installerDefDirPath) ):        
        raise Exception( "Installer definition directory path is not valid" )
    if qtIfwConfig.packages is None :
        raise Exception( "Package specification(s)/definition(s) required" )
    for p in qtIfwConfig.packages :
        if p.srcDirPath is None:
            if p.srcExePath is None:
                raise Exception( "Package Source directory OR exe path required" )
            elif not isFile(p.srcExePath) :        
                raise Exception( "Package Source exe path is not valid" )    
        elif not isDir(p.srcDirPath) :        
            raise Exception( "Package Source directory path is not valid" )
    # required Qt utility paths 
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = getenv( QT_IFW_DIR_ENV_VAR )    
    if( qtIfwConfig.qtIfwDirPath is None or
        not isDir(qtIfwConfig.qtIfwDirPath) ):        
        raise Exception( "Valid Qt IFW directory path required" )
    for p in qtIfwConfig.packages :
        if not isinstance( p, QtIfwPackage ) : continue
        if p.isQtCppExe : 
            if qtIfwConfig.qtBinDirPath is None:
                qtIfwConfig.qtBinDirPath = getenv( QT_BIN_DIR_ENV_VAR )    
            if( qtIfwConfig.qtBinDirPath is None or
                not isDir(qtIfwConfig.qtBinDirPath) ):        
                raise Exception( "Valid Qt Bin directory path required" )

def __initBuild( qtIfwConfig ) :
    print( "Initializing installer build..." )
    # remove any prior setup file
    setupExePath = joinPath( THIS_DIR, 
                             util.normBinaryName( qtIfwConfig.setupExeName ) )
    if exists( setupExePath ) : removeFile( setupExePath )
    # create a "clean" build directory
    if exists( BUILD_SETUP_DIR_PATH ) : removeDir( BUILD_SETUP_DIR_PATH )
    makeDir( BUILD_SETUP_DIR_PATH )    
    # copy the installer definition to the build directory
    if qtIfwConfig.installerDefDirPath :   
        copyDir( qtIfwConfig.installerDefDirPath, 
                 joinPath( BUILD_SETUP_DIR_PATH, INSTALLER_DIR_PATH ) )
    # copy the source content into the build directory
    for p in qtIfwConfig.packages :
        if not isinstance( p, QtIfwPackage ) : continue
        destDir = p.contentDirPath()                
        if p.srcDirPath : 
            p.srcDirPath = normpath( p.srcDirPath )
            copyDir( p.srcDirPath, destDir )    
        if p.srcExePath :
            srcExeDir, srcExeName = splitPath( p.srcExePath )
            if srcExeDir != p.srcDirPath :                    
                copyFile( p.srcExePath, destDir )                
            if p.exeName is None: p.exeName = srcExeName 
            elif p.exeName != srcExeName :             
                rename( joinPath( destDir, srcExeName ),
                        joinPath( destDir, p.exeName ) )            
    print( "Build directory created: %s" % (BUILD_SETUP_DIR_PATH,) )

def __addInstallerResources( qtIfwConfig ) :    
    configXml = qtIfwConfig.configXml
    if configXml : 
        print( "Adding installer configuration resources..." )
        configXml.debug()
        configXml.write()        
        if( configXml.iconFilePath and 
            isFile( configXml.iconFilePath ) ):
            copyFile( configXml.iconFilePath,                       
                      joinPath( configXml.dirPath(), 
                        basename( configXml.iconFilePath ) ) )              
    for p in qtIfwConfig.packages :
        if not isinstance( p, QtIfwPackage ) : continue
        pkgXml = p.pkgXml              
        pkgScript = p.pkgScript                   
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
        if p.othContentPaths is not None : __addOtherFiles( p )     
        if p.isQtCppExe : __addQtCppDependencies( qtIfwConfig, p )        
            

def __addOtherFiles( package ) :    
    print( "Adding additional files..." )
    destPath = package.contentDirPath()            
    for srcPath in package.othContentPaths:
        if isDir( srcPath ) : copyDir( srcPath, destPath )
        else : copyFile( srcPath, joinPath( destPath, basename( srcPath ) ) )

def __addQtCppDependencies( qtIfwConfig, package ) :
    # TODO: Add the counterparts here for other platforms
    if IS_WINDOWS :
        print( "Adding Qt C++ dependencies...\n" )
        qtUtilityPath =  normpath( joinPath(
            qtIfwConfig.qtBinDirPath, __QT_WINDOWS_DEPLOY_EXE_NAME ) )                    
        destDirPath = package.contentDirPath()
        exePath = joinPath( destDirPath, package.exeName )
        cmdList = [qtUtilityPath, exePath]
        if package.qmlScrDirPath is not None:
            cmdList.append( __QT_WINDOWS_DEPLOY_QML_SWITCH )
            cmdList.append( normpath( package.qmlScrDirPath ) )
        cmd = list2cmdline( cmdList )
        system( cmd )
        if package.isMingwExe :
            print( "Adding additional Qt dependencies..." )
            for fileName in __MINGW_DLL_LIST:
                copyFile( normpath( package.qtBinDirPath ), 
                          joinPath( destDirPath, fileName ) )

def __build( qtIfwConfig ) :
    print( "Building installer using Qt IFW...\n" )
    qtUtilityPath = joinPath( qtIfwConfig.qtIfwDirPath, 
        joinPath( __BIN_SUB_DIR, __QT_INSTALL_CREATOR_EXE_NAME ) )
    setupExePath = joinPath( THIS_DIR, 
                             util.normBinaryName( qtIfwConfig.setupExeName ) )
    cmd = '%s %s "%s"' % ( qtUtilityPath, str(qtIfwConfig), setupExePath )
    util._system( cmd )  
    setupExePath = normBinaryName( setupExePath, 
                                   isPathPreserved=True, isGui=True )
    if not exists( setupExePath ) : 
        raise Exception( 'FAILED to create "%s"' % (setupExePath,) )
    print( 'Installer built successfully!\n"%s"!' % (setupExePath,) )
    return setupExePath

def __postBuild( qtIfwConfig ):  # @UnusedVariable
    removeDir( BUILD_SETUP_DIR_PATH )
    for p in qtIfwConfig.packages :
        if not isinstance( p, QtIfwPackage ) : continue        
        if not p.isTempSrc : continue
        if   p.srcDirPath and isDir(  p.srcDirPath): removeDir(  p.srcDirPath )
        elif p.srcExePath and isFile( p.srcExePath): removeFile( p.srcExePath )                    
