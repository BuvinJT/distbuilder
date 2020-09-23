import string
from datetime import date
from abc import ABCMeta, abstractmethod
import xml.etree.ElementTree as ET
from xml.dom import minidom

import six

from distbuilder import util
from distbuilder.util import *  # @UnusedWildImport

QT_IFW_DEFAULT_VERSION = "3.2.2"
QT_IFW_DOWNLOAD_URL_BASE = "https://download.qt.io/official_releases/qt-installer-framework"
QT_IFW_DOWNLOAD_FILE_WINDOWS = "QtInstallerFramework-win-x86.exe"
QT_IFW_DOWNLOAD_FILE_MACOS   = "QtInstallerFramework-mac-x64.dmg"
QT_IFW_DOWNLOAD_FILE_LINUX   = "QtInstallerFramework-linux-x64.run"
__QT_IFW_DOWNLOAD_URL_TMPLT = "%s/%s/%s"

QT_IFW_DIR_ENV_VAR = "QT_IFW_DIR"

DEFAULT_SETUP_NAME = util.normBinaryName( "setup" )
DEFAULT_QT_IFW_SCRIPT_NAME = "installscript.qs"

BUILD_SETUP_DIR_PATH = absPath( "build_setup" )
INSTALLER_DIR_PATH = "installer"

QT_IFW_VERBOSE_SWITCH = '-v'
_KEEP_TEMP_SWITCH = "_keeptemp"
_SILENT_FORCED_ARGS = ["-f"]
_LOUD_FORCED_ARGS   = ["auto=true", "onexist=remove"]
_DEBUG_SCRIPTS_ARGS = ["_keeptemp=true"]

__BIN_SUB_DIR = "bin"
__QT_IFW_UNINSTALL_EXE_NAME = util.normBinaryName( "Uninstaller", isGui=True )
__QT_IFW_CREATOR_EXE_NAME = util.normBinaryName( "binarycreator" )

__QT_IFW_AUTO_INSTALL_PY_SCRIPT_NAME   = "__distb-install-qt-ifw.py"
__QT_IFW_AUTO_UNINSTALL_PY_SCRIPT_NAME = "__distb-uninstall-qt-ifw.py"
__QT_IFW_UNATTENDED_SCRIPT_NAME    = "__distb-unattended-qt-ifw.qs"

__WRAPPER_SCRIPT_NAME = "__installer.py"
__WRAPPER_INSTALLER_NAME = "wrapper-installer" 
__NESTED_INSTALLER_NAME  = "hidden-installer"

STARTMENU_WIN_SHORTCUT         = 0
DESKTOP_WIN_SHORTCUT           = 1
THIS_USER_STARTUP_WIN_SHORTCUT = 2
ALL_USERS_STARTUP_WIN_SHORTCUT = 3

APPS_MAC_SHORTCUT    = 0              
DESKTOP_MAC_SHORTCUT = 1             
                
APPS_X11_SHORTCUT    = 0
DESKTOP_X11_SHORTCUT = 1

SHORTCUT_WIN_MINIMIZED = 7

QT_IFW_ASKPASS_KEY = "askpass"
QT_IFW_ASKPASS_PLACEHOLDER = "[%s]" % (QT_IFW_ASKPASS_KEY,)
QT_IFW_ASKPASS_TEMP_FILE_PATH = "/tmp/{0}.path".format( QT_IFW_ASKPASS_KEY )

QT_IFW_DYNAMIC_SYMBOL = "@"

QT_IFW_ROOT_DIR      = "@RootDir@"
QT_IFW_TARGET_DIR    = "@TargetDir@"
QT_IFW_HOME_DIR      = "@HomeDir@" 
QT_IFW_DESKTOP_DIR   = ("@DesktopDir@" if IS_WINDOWS else
                        "%s/%s" % (QT_IFW_HOME_DIR,"Desktop") ) # Valid on macOS and Ubuntu at least (other Linux desktops?)
QT_IFW_APPS_DIR      = "@ApplicationsDir@"

QT_IFW_INSTALLER_DIR      = "@InstallerDirPath@"
QT_IFW_INTALLER_PATH      = "@InstallerFilePath@"   

_QT_IFW_INSTALLER_TEMP_DIR   = "InstallerTempDir"   # CUSTOM!
_QT_IFW_MAINTENANCE_TEMP_DIR = "MaintenanceTempDir" # CUSTOM!

QT_IFW_INSTALLER_TEMP_DIR   = "@%s@" % (_QT_IFW_INSTALLER_TEMP_DIR,)   # CUSTOM!
QT_IFW_MAINTENANCE_TEMP_DIR = "@%s@" % (_QT_IFW_MAINTENANCE_TEMP_DIR,) # CUSTOM!

QT_IFW_STARTMENU_DIR          = "@StartMenuDir@"
QT_IFW_USER_STARTMENU_DIR     = "@UserStartMenuProgramsPath@"  
QT_IFW_ALLUSERS_STARTMENU_DIR = "@AllUsersStartMenuProgramsPath@"

QT_IFW_PRODUCT_NAME    = "@ProductName@"
QT_IFW_PRODUCT_VERSION = "@ProductVersion@"
QT_IFW_TITLE           = "@Title@"
QT_IFW_PUBLISHER       = "@Publisher@"
QT_IFW_URL             = "@Url@"

QT_IFW_OS            = "@os@"

QT_IFW_APPS_X86_DIR  = "@ApplicationsDirX86@"
QT_IFW_APPS_X64_DIR  = "@ApplicationsDirX64@"

QT_IFW_INTRO_PAGE      = "Introduction"
QT_IFW_TARGET_DIR_PAGE = "TargetDirectory"
QT_IFW_COMPONENTS_PAGE = "ComponentSelection"
QT_IFW_LICENSE_PAGE    = "LicenseAgreement"
QT_IFW_START_MENU_PAGE = "StartMenuDirectory"
QT_IFW_READY_PAGE      = "ReadyForInstallation"
QT_IFW_INSTALL_PAGE    = "PerformInstallation"
QT_IFW_FINISHED_PAGE   = "Finished"

QT_IFW_REPLACE_PAGE_PREFIX="Replace"

_DEFAULT_PAGES = [
      QT_IFW_INTRO_PAGE      
    , QT_IFW_TARGET_DIR_PAGE 
    , QT_IFW_COMPONENTS_PAGE 
    , QT_IFW_LICENSE_PAGE    
    , QT_IFW_START_MENU_PAGE 
    , QT_IFW_READY_PAGE      
    , QT_IFW_INSTALL_PAGE    
    , QT_IFW_FINISHED_PAGE   
]

_PAGE_NAME_PLACHOLDER = "[PAGE_NAME]"

_ENV_TEMP_DIR     = "%temp%" if IS_WINDOWS else "/tmp"
_QT_IFW_TEMP_NAME = "__distbuilder-qtifw"

_QT_IFW_WATCH_DOG_SUFFIX = "-watchdog"
_QT_IFW_WATCH_DOG_EXT    = ".vbs" if IS_WINDOWS else ""

QT_IFW_DYNAMIC_PATH_VARS = [
      "RootDir" 
    , "HomeDir"  
    , "DesktopDir" 
    , "ApplicationsDir" 
    , "StartMenuDir" 
    , "UserStartMenuProgramsPath" 
    , "AllUsersStartMenuProgramsPath" 
    , "ApplicationsDirX86" 
    , "ApplicationsDirX64" 
    , "InstallerTempDir"
    , "MaintenanceTempDir"
    , "InstallerDirPath" 
    , "InstallerFilePath" 
]

# don't use back slash on Windows!
def joinPathQtIfw( head, tail ): return "%s/%s" % ( head, tail )

# -----------------------------------------------------------------------------
class QtIfwConfig:   
    def __init__( self, 
                  installerDefDirPath=None,
                  packages=None,                  
                  configXml=None,
                  controlScript=None, 
                  setupExeName=DEFAULT_SETUP_NAME ) :       
        self.installerDefDirPath = installerDefDirPath
        self.packages            = packages # list of QtIfwPackages or directory paths
        self.configXml           = configXml
        self.controlScript       = controlScript         
        
        self.setupExeName        = setupExeName
        # QtIFW path (attempt to use environmental variable if not defined)
        self.qtIfwDirPath = None
        # other IFW command line options
        self.isDebugMode    = True
        self.otherQtIfwArgs = ""
                
    def __str__( self ) :
        configSpec   = '-c "%s"' % (self.configXml.path() if self.configXml 
                                    else QtIfwConfigXml().path(),)
        packageDirSpec = ' -p "%s"' % (QtIfwPackage.topDirPath(),)        
        verboseSpec  = '-v' if self.isDebugMode else ''                
        tokens = (configSpec, packageDirSpec, verboseSpec, self.otherQtIfwArgs)
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
    
    def exists( self ): return isFile( self.path() )
            
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
                   , "ControlScript"                                 
                   ]
    __RUN_ARGS_TAG = "RunProgramArguments"
    __ARG_TAG      = "Argument"
        
    __RUN_PROG_DESCR_TMPLT = "Run %s now."    
    
    # QtIfwConfigXml
    def __init__( self, name, version, publisher,
                  iconFilePath=None, 
                  controlScriptName=None,
                  primaryContentExe=None,
                  isPrimaryExeGui=True,
                  primaryExeWrapper=None,
                  companyTradeName=None ) :
        _QtIfwXml.__init__( self, QtIfwConfigXml.__ROOT_TAG, 
                            QtIfwConfigXml.__TAGS )
       
        self.primaryContentExe = ( 
            util.normBinaryName( primaryContentExe, 
                                 isGui=isPrimaryExeGui )
            if primaryContentExe else None )
        self.primaryExeWrapper=primaryExeWrapper
        
        if IS_LINUX :
            # qt installer does not support icon embedding in Linux
            iconBaseName = self.iconFilePath = None
        else :    
            self.iconFilePath = ( None if iconFilePath is None else 
                                  normIconName( iconFilePath, 
                                                isPathPreserved=True ) )        
            try:    iconBaseName = splitExt( fileBaseName(iconFilePath) )[0]
            except: iconBaseName = None
        self.companyTradeName = ( companyTradeName if companyTradeName 
                                  else publisher.replace(".","") )
        self.runProgramArgList = None

        # TODO: expand on the built-in attributes here...        
        self.Name                     = name
        self.Version                  = version
        self.Publisher                = publisher
        self.InstallerApplicationIcon = iconBaseName
        self.ControlScript            = controlScriptName 
        self.Title                    = None        
        self.TargetDir                = None        
        self.StartMenuDir             = None
        self.RunProgram               = None
        self.RunProgramDescription    = None
                       
        self.setDefaultTitle()
        self.setDefaultPaths()

    def setPrimaryContentExe( self, ifwPackage ) :
        if ifwPackage:
            self.RunProgramDescription =( QtIfwConfigXml.__RUN_PROG_DESCR_TMPLT
                                          % (ifwPackage.pkgXml.DisplayName,) )
            self.primaryContentExe = util.normBinaryName( ifwPackage.exeName, 
                                                          isGui=ifwPackage.isGui )
            self.primaryExeWrapper = ifwPackage.exeWrapper            
            self.setDefaultPaths()

    def setDefaultVersion( self ) :
        # TODO: extract version info from primary exe?
        if self.Version is None: self.Version = "1.0.0" 

    def setDefaultTitle( self ) :
        if self.Title is None: self.Title = self.Name
            #self.Title = "%s Setup" % (self.Name) # New IFW seem to be adding "Setup" suffix?
    
    def setDefaultPaths( self ) :
        # NOTE: DON'T USE PATH FUNCTIONS HERE!
        # USE RAW STRINGS with FORWARD SLASHES (/) 
        # (QtIFW configs & scripts are happy with / cross platform)
                
        if self.companyTradeName and self.Name:
            # On macOS, self-contained "app bundles" are typically dropped 
            # into "Applications", but "traditional" directories e.g.
            # what QtIFW installs (with the .app contained within it)
            # are NOT placed there.  Instead, the user's home directory
            # is typical, with a link perhaps also appearing 
            # in Applications.  On Linux and Windows, @ApplicationsDir@
            # resolves to a typical (cross user) applications location.       
            dirVar = QT_IFW_HOME_DIR if IS_MACOS else QT_IFW_APPS_DIR
            subDir = joinPathQtIfw(self.companyTradeName, self.Name) 
            self.TargetDir = joinPathQtIfw(dirVar, subDir)
            
        if IS_WINDOWS:
            if self.companyTradeName:
                self.StartMenuDir = self.companyTradeName
                
        if self.primaryExeWrapper:
            self.RunProgram = self.primaryExeWrapper._runProgram 
            self.runProgramArgList = self.primaryExeWrapper._runProgArgs            
        elif self.primaryContentExe:        
            programPath = joinPathQtIfw( QT_IFW_TARGET_DIR, 
                                         self.primaryContentExe )    
            if util._isMacApp( self.primaryContentExe ):   
                self.RunProgram = util._LAUNCH_MACOS_APP_CMD 
                if not isinstance( self.runProgramArgList, list ) :
                    self.runProgramArgList = []
                else :
                    self.runProgramArgList.insert(0, util._LAUNCH_MACOS_APP_ARGS_SWITCH)     
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

    class Type: DATA, PY_INSTALLER, QT_CPP = range(3)  
    
    __PACKAGES_PATH_TMPLT       = "%s/packages"
    __DIR_PATH_TMPLT            = "%s/packages/%s"
    __META_PATH_TMPLT           = "%s/packages/%s/meta" 
    __CONTENT_PATH_TMPLT        = "%s/packages/%s/data" 
    __CONTENT_SUBDIR_PATH_TMPLT = "%s/packages/%s/data/%s"
    
    @staticmethod
    def topDirPath() :  
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwPackage.__PACKAGES_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )
    
    # QtIfwPackage
    def __init__( self, pkgId=None, pkgType=None, name=None,
                  subDirName=None,  
                  srcDirPath=None, srcExePath=None, 
                  resBasePath=None, isTempSrc=False, 
                  pkgXml=None, pkgScript=None,
                  uiPages=[] ) :
        # internal id / type
        self.pkgId     = pkgId
        self.pkgType   = pkgType       
        # QtIFW definition        
        self.name      = name
        self.pkgXml    = pkgXml
        self.pkgScript = pkgScript        
        self.uiPages   = uiPages
        # content        
        self.srcDirPath    = srcDirPath
        self.srcExePath    = srcExePath
        self.resBasePath   = resBasePath
        self.distResources = None        
        self.isTempSrc     = isTempSrc                     
        # extended content detail        
        self.subDirName  = subDirName 
        self.exeName     = None           
        self.isGui       = False
        self.exeWrapper  = None # class QtIfwExeWrapper
        self.qtCppConfig = None
    
    def dirPath( self ) :
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwPackage.__DIR_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.name,) ) )

    def metaDirPath( self ) :
        return joinPath( BUILD_SETUP_DIR_PATH, 
             normpath( QtIfwPackage.__META_PATH_TMPLT 
                       % (INSTALLER_DIR_PATH, self.name,) ) )

    def contentTopDirPath( self ) :
        return joinPath( BUILD_SETUP_DIR_PATH, 
             normpath( QtIfwPackage.__CONTENT_PATH_TMPLT 
                       % (INSTALLER_DIR_PATH, self.name,) ) )

    def contentDirPath( self ) :
        subDir = normpath(
            QtIfwPackage.__CONTENT_SUBDIR_PATH_TMPLT 
                % (INSTALLER_DIR_PATH, self.name, self.subDirName)
            if self.subDirName else
            QtIfwPackage.__CONTENT_PATH_TMPLT 
                % (INSTALLER_DIR_PATH, self.name,)
        ) 
        return joinPath( BUILD_SETUP_DIR_PATH, subDir )
    
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
    __UIS_TAG    = "UserInterfaces"
    __UI_TAG     = "UserInterface"
        
    # QtIfwPackageXml   
    def __init__( self, pkgName, displayName, description, 
                  version, scriptName=None, isDefault=True ) :
        _QtIfwXml.__init__( self, QtIfwPackageXml.__ROOT_TAG, 
                            QtIfwPackageXml.__TAGS )        
        self.pkgName       = pkgName
        
        # TODO: expand on the built-in attributes here...
        self.DisplayName    = displayName
        self.Description    = description
        self.Version        = version            
        self.Script         = scriptName 
        self.Default        = isDefault
        self.ReleaseDate    = date.today()
        self.UserInterfaces = []
                         
    def addCustomTags( self, root ) :
        if self.UserInterfaces is not None :            
            uis = _QtIfwXmlElement( QtIfwPackageXml.__UIS_TAG, 
                                    None, root )
            for ui in self.UserInterfaces:
                _QtIfwXmlElement( QtIfwPackageXml.__UI_TAG, ui, uis )                
                            
    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageXml.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageXml.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) )     


# -----------------------------------------------------------------------------
@six.add_metaclass(ABCMeta)
class _QtIfwScript:

    TAB         = "    "
    NEW_LINE    = "\n" 
    END_LINE    = ";\n"
    START_BLOCK = "{\n"
    END_BLOCK   = "}\n"
    
    TRUE  = "true"
    FALSE = "false"
    
    PATH_SEP = '"\\\\"' if IS_WINDOWS else '"/"'  
        
    MAINTENANCE_TOOL_NAME  = util.normBinaryName( 
        "maintenancetool", isGui=True )
    
    VERBOSE_CMD_SWITCH_ARG = "-v"    
    TARGET_DIR_KEY         = "TargetDir"
    STARTMENU_DIR_KEY      = "StartMenuDir"
    PRODUCT_NAME_KEY       = "ProductName"
    
    ERR_LOG_PATH_CMD_ARG      = "errlog"
    ERR_LOG_DEFAULT_PATH      = ( 
        "%temp%\\\\installer.err" if IS_WINDOWS else
        "/tmp/installer.err" ) # /tmp is supposedly guaranteed to exist, though it's not secure

    TARGET_DIR_CMD_ARG        = "target"
    START_MENU_DIR_CMD_ARG    = "startmenu"    
    ACCEPT_EULA_CMD_ARG       = "accept"
    INSTALL_LIST_CMD_ARG      = "install"
    INCLUDE_LIST_CMD_ARG      = "include"
    EXCLUDE_LIST_CMD_ARG      = "exclude"
    RUN_PROGRAM_CMD_ARG       = "run"
    AUTO_PILOT_CMD_ARG        = "auto"
    TARGET_EXISTS_OPT_CMD_ARG = "onexist"
    TARGET_EXISTS_OPT_FAIL    = "fail"
    TARGET_EXISTS_OPT_REMOVE  = "remove"
    TARGET_EXISTS_OPT_PROMPT  = "prompt"
    
    MAINTAIN_MODE_CMD_ARG        = "mode"
    MAINTAIN_MODE_OPT_ADD_REMOVE = "addremove"
    MAINTAIN_MODE_OPT_UPDATE     = "update"    
    MAINTAIN_MODE_OPT_REMOVE_ALL = "removeall"

    _GUI_OBJ       = "gui"
    _INSTALLER_OBJ = "installer"
    
    _TEMP_DIR = "Dir.temp()"
        
    __IS_INSTALLER   = "installer.isInstaller()"
    __IS_UNINSTALLER = "installer.isUninstaller()"

    __IS_MAINTENANCE_TOOL = 'isMaintenanceTool()'
        
    # an example for use down the line...
    __LINUX_GET_DISTRIBUTION = ( 
"""
        var IS_UBUNTU   = (systemInfo.productType === "ubuntu");
        var IS_OPENSUSE = (systemInfo.productType === "opensuse");             
""" )

    OK     = "QMessageBox.Yes"
    YES    = "QMessageBox.Yes" 
    NO     = "QMessageBox.No"
    CANCEL = "QMessageBox.Cancel"

    __LOG_TMPL = "console.log(%s);\n"
    __DEBUG_POPUP_TMPL = ( 
        'QMessageBox.information("debugbox", "Debug", ' +
            '%s, QMessageBox.Ok );\n' )
    
    __ERROR_POPUP_TMPL = ( 
        'QMessageBox. critical("errorbox", "Error", ' +
            '%s, QMessageBox.Ok );\n' )

    __YES_NO_POPUP_TMPL = ( 
        'var %s = QMessageBox.question("yesnobox", "%s", ' +
            '"%s", QMessageBox.Yes|QMessageBox.No );\n' )                                  
                                  
    __YES_NO_CANCEL_POPUP_TMPL = ( 
        'var %s = QMessageBox.question("yesnocancelbox", "%s", ' +
            '"%s", QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel );\n' )
    
    __VALUE_TMPL      = "installer.value( %s, %s )"
    __VALUE_LIST_TMPL = "installer.values( %s, %s )"
    __SET_VALUE_TMPL  = "installer.setValue( %s, %s )"

    __GET_ENV_VAR_TMPL = "installer.environmentVariable( %s )"

    __PATH_EXISTS_TMPL = "installer.fileExists( %s )"

    __MAKE_DIR_TMPL   = "makeDir( resolveQtIfwPath( %s ) );"
    __REMOVE_DIR_TMPL = "removeDir( resolveQtIfwPath( %s ) );"
    
    __WRITE_FILE_TMPL  = "writeFile( resolveQtIfwPath( %s ), %s );"
    __DELETE_FILE_TMPL = "deleteFile( resolveQtIfwPath( %s ), %s );"

    __EMBED_RES_TMPLT       = 'var %s = %s;\n\n'
    __EMBED_RES_CHUNK_SIZE  = 128
    __EXT_DELIM_PLACEHOLDER = "_dot_"
    __SCRIPT_FROM_B64_TMPL  = 'writeScriptFromBase64( "%s", %s, %s )%s'
    
    # Note, there is in fact an installer.killProcess(string absoluteFilePath)
    # this custom kill takes a process name, with no specific path
    # It also runs in parrellel with "install operation" kills
    __KILLALL_PROG_TMPL = "killAll( %s );\n"
    _KILLALL_PATH = "taskkill"   if IS_WINDOWS else "killall"
    _KILLALL_ARGS = ["/F","/IM"] if IS_WINDOWS else ["-9"] #TODO: CROSS SH? some might want -s9 ?
    _KILLALL_CMD_PREFIX = "%s %s" % (_KILLALL_PATH, " ".join( _KILLALL_ARGS ))

    @staticmethod        
    def _autoQuote( value, isAutoQuote ):                  
        return '"%s"' % (value,) if isAutoQuote else value 

    @staticmethod
    def embedResources( embeddedResources ):
        def chunks(s, n):
            """Produce `n`-character chunks from `s`."""
            for start in range(0, len(s), n):
                yield s[start:start+n]
        
        def embed( res ):
            if isinstance( res, ExecutableScript ):
                script = res
                varName = script.fileName().replace(".","_dot_")                
                b64 = script.toBase64( toString=True )
                b64Literals = ""
                for chunk in chunks(b64, _QtIfwScript.__EMBED_RES_CHUNK_SIZE):
                    concat = "  " if b64Literals=="" else "+ " 
                    b64Literals += '%s%s%s"%s"' % (
                        _QtIfwScript.NEW_LINE, _QtIfwScript.TAB, concat, chunk)                
                return _QtIfwScript.__EMBED_RES_TMPLT % (varName, b64Literals)                 
        raw = ""
        for res in embeddedResources: raw += embed( res )
        return raw
    
    @staticmethod
    def genResources( embeddedResources ):
        
        MAX_VAR_LENGTH = 64 # Not a true limit to the language, just a sanity check for this context
        VAR_NAME_CHARS = string.digits + string.ascii_letters + "_"
        
        def isValidVarName( name ):
            if name.strip()=="" or len(name) > MAX_VAR_LENGTH: return False
            for c in name: 
                if c not in VAR_NAME_CHARS: return False
            return True
        
        def gen( script ):
            if isinstance( script, ExecutableScript ):
                scriptName = script.fileName()
                scriptContent = str(script)
                resourceVarName = scriptName.replace(
                    ".", _QtIfwScript.__EXT_DELIM_PLACEHOLDER ) 
                dynamicVarNames = scriptContent.split( QT_IFW_DYNAMIC_SYMBOL )
                dynamicVarNames = [ v for v in dynamicVarNames 
                                    if isValidVarName( v ) ]
                dynamicVarNames = "[ %s ]" % (
                    ",".join( ['"%s"' % (v,) for v in dynamicVarNames] ), )
                return ( _QtIfwScript.log( "script: %s" % (scriptName,) ) +
                    _QtIfwScript.log( scriptContent ) +
                    _QtIfwScript.__SCRIPT_FROM_B64_TMPL % 
                    (scriptName, resourceVarName, dynamicVarNames, 
                    _QtIfwScript.END_LINE) )
            return ""        
        return "".join( [ gen( res ) for res in embeddedResources ] )

    @staticmethod        
    def log( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__LOG_TMPL % (
            _QtIfwScript._autoQuote( msg, isAutoQuote ),)

    @staticmethod        
    def debugPopup( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__DEBUG_POPUP_TMPL % (
             _QtIfwScript._autoQuote( msg, isAutoQuote ),) 
        
    @staticmethod        
    def errorPopup( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__ERROR_POPUP_TMPL % (
             _QtIfwScript._autoQuote( msg, isAutoQuote ),) 
        
    @staticmethod        
    def setValue( key, value, isAutoQuote=True ):                  
        return _QtIfwScript.__SET_VALUE_TMPL % (
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            _QtIfwScript._autoQuote( value, isAutoQuote ))

    @staticmethod        
    def lookupValue( key, default="", isAutoQuote=True ):                  
        return _QtIfwScript.__VALUE_TMPL % (
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            _QtIfwScript._autoQuote( default, isAutoQuote ))

    @staticmethod        
    def lookupValueList( key, defaultList=[], isAutoQuote=True, 
                          delimiter=None ):
        defList=""
        for v in defaultList: 
            defList += _QtIfwScript._autoQuote( str(v), isAutoQuote )
        defList = "[%s]" % defList            
        if delimiter:
            valScr = _QtIfwScript.lookupValue( key, isAutoQuote=True )
            return ( '( %s=="" ? %s : %s.split("%s") )' % 
                ( valScr, defList, valScr, delimiter ) )
        return _QtIfwScript.__VALUE_LIST_TMPL % (
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            defList )
        
    @staticmethod        
    def getEnv( varName, isAutoQuote=True ):                  
        return _QtIfwScript.__GET_ENV_VAR_TMPL % (
            _QtIfwScript._autoQuote( varName, isAutoQuote ) )

    @staticmethod        
    def killAll( exeName, isAutoQuote=True ):                  
        return _QtIfwScript.__KILLALL_PROG_TMPL % (
            _QtIfwScript._autoQuote( exeName, isAutoQuote ) )

    @staticmethod        
    def targetDir(): 
        return _QtIfwScript.lookupValue( _QtIfwScript.TARGET_DIR_KEY )

    @staticmethod        
    def startMenuDir(): 
        return _QtIfwScript.lookupValue( _QtIfwScript.STARTMENU_DIR_KEY )

    @staticmethod        
    def productName(): 
        return _QtIfwScript.lookupValue( _QtIfwScript.PRODUCT_NAME_KEY )
    
    @staticmethod        
    def ifCmdLineArg( arg, isNegated=False, isMultiLine=False, ):   
        return 'if( %s%s"" )%s\n%s' % (
            _QtIfwScript.lookupValue( arg ),            
            ("==" if isNegated else "!="),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def ifCmdLineSwitch( arg, isNegated=False, isMultiLine=False ):
        return 'if( %s%s"%s" )%s\n%s' % (
            _QtIfwScript.lookupValue( arg ),
            ("!=" if isNegated else "==") ,
            _QtIfwScript.TRUE,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def cmdLineArg( arg, default="" ):
        return _QtIfwScript.lookupValue( arg, default )

    @staticmethod        
    def cmdLineSwitchArg( arg ):
        return ( '(%s=="%s")' % 
            ( _QtIfwScript.lookupValue( arg ),
              _QtIfwScript.TRUE ) )

    @staticmethod        
    def cmdLineListArg( arg, default=[] ):                  
        return _QtIfwScript.lookupValueList( 
            arg, default, delimiter="," )

    @staticmethod
    def ifMaintenanceTool( isMultiLine=False ):
        return 'if( %s )%s\n%s' % (
            _QtIfwScript.__IS_MAINTENANCE_TOOL,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def ifInstalling( isMultiLine=False ):
        return 'if( %s )%s\n%s' % (
            _QtIfwScript.__IS_INSTALLER,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def yesNoPopup( msg, title="Question", resultVar="result" ):                  
        return _QtIfwScript.__YES_NO_POPUP_TMPL % ( resultVar, title, msg ) 

    # returns a full line, including the result var declaration
    @staticmethod        
    def yesNoCancelPopup( msg, title="Question", resultVar="result" ):                  
        return _QtIfwScript.__YES_NO_CANCEL_POPUP_TMPL % ( 
            resultVar, title, msg ) 

    @staticmethod        
    def ifYesNoPopup( msg, title="Question", resultVar="result", 
                      isMultiLine=False ):                  
        return ( 
            _QtIfwScript.TAB + _QtIfwScript.yesNoPopup( msg, title, resultVar ) +
            _QtIfwScript.TAB + 'if( %s == QMessageBox.Yes )%s\n%s' % (
            resultVar, ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) ) )

    @staticmethod        
    def switchYesNoCancelPopup( msg, title="Question", resultVar="result", 
                                onYes="", onNo="", onCancel="" ):
        TAB = _QtIfwScript.TAB                 
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        BREAK = 'break' + END      
        return ( 
            TAB + _QtIfwScript.yesNoCancelPopup( msg, title, resultVar ) +
            (TAB + 'switch( %s )' + _QtIfwScript.START_BLOCK + 
             TAB + 'case ' + _QtIfwScript.YES + ':' + NEW +
             (2*TAB) + '%s' + NEW +
             (2*TAB) + BREAK +
             TAB + 'case ' + _QtIfwScript.NO + ':' + NEW +
             (2*TAB) + '%s' + NEW + 
             (2*TAB) + BREAK +
             TAB + 'case ' + _QtIfwScript.CANCEL + ':' + NEW +
             (2*TAB) + '%s' + NEW +
             (2*TAB) + BREAK +             
             TAB + _QtIfwScript.END_BLOCK ) % 
            ( resultVar, onYes, onNo, onCancel ) )

    @staticmethod        
    def pathExists( path, isAutoQuote=True ):                  
        return _QtIfwScript.__PATH_EXISTS_TMPL % (
            _QtIfwScript._autoQuote( path, isAutoQuote ),) 

    @staticmethod        
    def ifPathExists( path, isAutoQuote=True, isMultiLine=False ):   
        return 'if( %s )%s\n%s' % (
            _QtIfwScript.pathExists( path, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod
    def ifNotPathExists( path, isAutoQuote=True, isMultiLine=False ):   
        return 'if( ! %s )%s\n%s' % (
            _QtIfwScript.pathExists( path, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def makeDir( path, isAutoQuote=True ):                  
        return _QtIfwScript.__MAKE_DIR_TMPL %  (
            _QtIfwScript._autoQuote( path, isAutoQuote ),) 

    @staticmethod        
    def removeDir( path, isAutoQuote=True ):                  
        return _QtIfwScript.__REMOVE_DIR_TMPL % (
            _QtIfwScript._autoQuote( path, isAutoQuote ),) 

    @staticmethod        
    def writeFile( path, content, isAutoQuote=True ):                  
        return _QtIfwScript.__WRITE_FILE_TMPL % (
            _QtIfwScript._autoQuote( path, isAutoQuote ),
            _QtIfwScript._autoQuote( content, isAutoQuote )) 

    @staticmethod        
    def deleteFile( path, isAutoQuote=True ):                  
        return _QtIfwScript.__DELETE_FILE_TMPL % (
            _QtIfwScript._autoQuote( path, isAutoQuote ),) 
            
    # _QtIfwScript            
    def __init__( self, fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None, 
                  virtualArgs={}, isAutoLib=True ) :
        self.fileName = fileName
        if scriptPath :
            with open( scriptPath, 'rb' ) as f: self.script = f.read()
        else : self.script = script  
        self.virtualArgs = virtualArgs
        self.isAutoLib   = isAutoLib
        self.qtScriptLib = None

    def _genLib( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK
        
        pathVarsList = ",".join([ '"%s"' % (v,) 
                                  for v in QT_IFW_DYNAMIC_PATH_VARS ])

        self.qtScriptLib = (              
            NEW +
            'var dynamicPathVars = [ ' + pathVarsList + ' ]' + END +
            NEW +                                                         
            'var Dir = new function () ' + SBLK +
            TAB + 'this.temp = function () ' + SBLK +
            (2*TAB) + 'return isMaintenanceTool() ? __maintenanceTempPath() : ' + 
                '__installerTempPath()' + END + 
            TAB + EBLK +
            TAB + 'this.toNativeSeparator = function (path) ' + SBLK +
            (2*TAB) + 'if( isWindows() )' + NEW +
                (3*TAB) + 'return path.replace(/\\//g, \'\\\\\')' + END +
            (2*TAB) + 'return path' + END + 
            TAB + EBLK +            
            TAB + 'this.fromNativeSeparator = function (path) ' + SBLK +
            (2*TAB) + 'if( isWindows() )' + NEW +
                (3*TAB) + 'return path.replace(/\\\\/g, \'/\')' + END +
            (2*TAB) + 'return path' + END + 
            TAB + EBLK +            
            '};' + NEW +
            'function isMaintenanceTool() ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var isTool = rootFileName( __lockFilePath() ).startsWith( ' + 
                  ('rootFileName( "%s" ) )' % (_QtIfwScript.MAINTENANCE_TOOL_NAME,)) + END +
            TAB + _QtIfwScript.log( '"isMaintenanceTool: " + isTool', isAutoQuote=False ) +                  
            TAB + 'return isTool' + END +                  
            EBLK + NEW +            
            # TODO: This logic could possibly fail when installers / uninstallers 
            # for *other* programs are running at the same time...          
            'function __lockFilePath() ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var path = installer.value( "__lockFilePath", "" )' + END +
            TAB + 'if( path === "" ) ' + SBLK +                        
            (2*TAB) + 'var lockFileName = ""' + END +
            (2*TAB) + 'var instPrefix = __installerPrefix()' + END +
            (2*TAB) + 'var toolPrefix = __maintenanceToolPrefix()' + END +
            (2*TAB) + 'var lockFileDir = getEnv("temp")' + END +
            (2*TAB) + 'var lockFileGlob = Dir.toNativeSeparator( lockFileDir + "/*.lock" )' + END +
            (2*TAB) + 'var sortByTime = true' + END +            
            (2*TAB) + 'var lockFiles = dirList( lockFileGlob, sortByTime )' + END +
            (2*TAB) + 'for( var i=0; i < lockFiles.length; i++ )' + SBLK +
                (3*TAB) + 'if( lockFiles[i].startsWith(instPrefix) ||' + NEW + 
                (3*TAB) + '    lockFiles[i].startsWith(toolPrefix) )' + END +
                (3*TAB) + '    lockFileName = lockFiles[i]' + END +                                         
            (2*TAB) + EBLK +                
            (2*TAB) + 'if( lockFileName === "" )' + NEW +
                (3*TAB) + 'silentAbort("Lock file path could not be resolved")' + END +                
            (2*TAB) + 'path = Dir.toNativeSeparator( lockFileDir + "/" + lockFileName )' + END +            
            (2*TAB) + _QtIfwScript.log( '"lockFilePath: " + path', isAutoQuote=False ) +
            (2*TAB) + 'installer.setValue( "__lockFilePath", path )'  + END +
            TAB + EBLK +                         
            TAB + 'return path' + END +
            EBLK + NEW +            
            'function __launchWatchDog() ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var watchDogPath = installer.value( "__watchDogPath", "" )' + END +
            TAB + 'if( watchDogPath === "" ) ' + SBLK +            
            (2*TAB) + ('watchDogPath = __tempPath( "%s%s" )' % 
                 (_QT_IFW_WATCH_DOG_SUFFIX,_QT_IFW_WATCH_DOG_EXT)) + END +
            (2*TAB) + 'installer.setValue( "__watchDogPath", watchDogPath )' + END +
            TAB + EBLK +   
            TAB + _QtIfwScript.log( '"__watchDogPath: " + watchDogPath', isAutoQuote=False ) +            
            (
            TAB + 'var vbs = ' + NEW +
            (2*TAB) + '"On Error Resume Next\\n" + ' + NEW + 
            (2*TAB) + '"Set oFSO = CreateObject(\\"Scripting.FileSystemObject\\")\\n" + ' + NEW +                        
            (2*TAB) + '"While oFSO.FileExists(\\"" + __lockFilePath() + "\\")\\n" + ' + NEW +            
            (2*TAB) + '"    WScript.Sleep(3000)\\n" + ' + NEW +
            (2*TAB) + '"Wend\\n" + ' + NEW +
            (2*TAB) + '"oFSO.DeleteFolder \\"" + Dir.temp() + "\\"\\n" + ' + NEW +
            (2*TAB) + '"oFSO.DeleteFile WScript.ScriptFullName\\n" ' + END +            
            TAB + 'executeVbScriptDetached( watchDogPath, vbs )' + END 
            if IS_WINDOWS else 
            TAB + '' + END) + # TODO: FILLIN!!
            EBLK + NEW +
            'function __tempPath( suffix ) ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'return (isMaintenanceTool() ? __maintenanceTempPath() : __installerTempPath()) + ' +
                      '(suffix ? suffix : "")' + END +                  
            EBLK + NEW +
            'function __installerTempPath( suffix ) ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var dirPath = installer.value( ' + 
                ('"%s"' % (_QT_IFW_INSTALLER_TEMP_DIR,)) + ', "" )' + END +
            TAB + 'if( dirPath === "" ) ' + SBLK +            
            (2*TAB) + 'dirPath = Dir.toNativeSeparator( ' +
                'getEnv("temp") + "/__" + __installerPrefix() + "-install" )' + END +
            (2*TAB) + 'installer.setValue( ' + 
            ('"%s"' % (_QT_IFW_INSTALLER_TEMP_DIR,)) + ', dirPath )' + END +
            (2*TAB) + _QtIfwScript.log( ('"%s' % (_QT_IFW_INSTALLER_TEMP_DIR,)) + 
                                        ': " + dirPath', isAutoQuote=False ) +                 
            TAB + EBLK + 
            TAB + 'return dirPath' + END + 
            EBLK + NEW +
            'function __maintenanceTempPath( suffix ) ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var dirPath = installer.value( ' + 
                ('"%s"' % (_QT_IFW_MAINTENANCE_TEMP_DIR,)) + ', "" )' + END +
            TAB + 'if( dirPath === "" ) ' + SBLK +            
            (2*TAB) + 'dirPath = Dir.toNativeSeparator( ' + # NOTE: __installerPrefix() is CORRECT HERE!
                'getEnv("temp") + "/__" + __installerPrefix() + "-maintenance" )' + END +
            (2*TAB) + 'installer.setValue( ' + 
            ('"%s"' % (_QT_IFW_MAINTENANCE_TEMP_DIR,)) + ', dirPath )' + END +
            (2*TAB) + _QtIfwScript.log( ('"%s' % (_QT_IFW_MAINTENANCE_TEMP_DIR,)) + 
                                        ': " + dirPath', isAutoQuote=False ) +                 
            TAB + EBLK + 
            TAB + 'return dirPath' + END +             
            EBLK + NEW +
            'function __installerPrefix() ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'return rootFileName( installer.value("InstallerFilePath") )' + END +                  
            EBLK + NEW +
            'function __maintenanceToolPrefix() ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + ('return rootFileName( "%s" )' % (_QtIfwScript.MAINTENANCE_TOOL_NAME,)) + END +                  
            EBLK + NEW +                                                                                     
            'function resolveQtIfwPath( path ) ' + SBLK +
            TAB + 'path = Dir.fromNativeSeparator( path )' + END +
            TAB + 'for( var i=0; i != dynamicPathVars.length; ++i ) ' + SBLK +                                    
            (2*TAB) + 'var varName = dynamicPathVars[i]' + END +
            (2*TAB) + 'var varVal = installer.value( varName )' + END +
            (2*TAB) + 'path = path.split( "@" + varName + "@" ).join( varVal )' + END +
            (2*TAB) + EBLK +             
            TAB + 'return path' + END +                                                                                                                          
            EBLK + NEW +                                   
            'function isWindows() ' + SBLK +
            TAB + 'return systemInfo.kernelType === "winnt"' + END +
            EBLK + NEW +
            'function isMacOs() ' + SBLK +
            TAB + 'return systemInfo.kernelType === "darwin"' + END +
            EBLK + NEW +
            'function isLinux() ' + SBLK +
            TAB + 'return systemInfo.kernelType === "linux"' + END +
            EBLK + NEW +
            'function getEnv( varName ) ' + SBLK +
            TAB + 'return installer.environmentVariable( varName )' + END +
            EBLK + NEW +
            'function fileName( filePath ) ' + SBLK +
            TAB + 'var pathParts = Dir.fromNativeSeparator( filePath ).split("/")' + END +
            TAB + 'return pathParts[pathParts.length-1]' + END +
            EBLK + NEW +
            'function rootFileName( filePath ) ' + SBLK +
            TAB + 'return fileName( filePath ).split(".")[0]' + END +
            EBLK + NEW +                                                            
            'function execute( binPath, args ) ' + SBLK +
            TAB + 'var cmd = "\\"" + binPath + "\\""' + END +
            TAB + 'for( i=0; i < args.length; i++ )' + NEW +
            (2*TAB) + 'cmd += (" " + args[i])' + END +
            TAB + _QtIfwScript.log( '"Executing: " + cmd', isAutoQuote=False ) +
            TAB + 'return installer.execute( binPath, args )' + END +
            EBLK + NEW +
            'function executeDetached( binPath, args ) ' + SBLK +
            TAB + 'var cmd = "\\"" + binPath + "\\""' + END +
            TAB + 'for( i=0; i < args.length; i++ )' + NEW +
            (2*TAB) + 'cmd += (" " + args[i])' + END +
            TAB + _QtIfwScript.log( '"Executing: " + cmd', isAutoQuote=False ) +
            TAB + 'return installer.executeDetached( binPath, args )' + END +
            EBLK + NEW +            
            'function resolveNativePath( path ) ' + SBLK +    # TODO: Test in NIX/MAC  
                TAB + 'path = Dir.toNativeSeparator( path )' + END +            
                TAB + 'var echoCmd = "' +
                    ('echo off\\n'                     
                     'echo " + path + "\\n' 
                     if IS_WINDOWS else
                     'echo \\"" + path + "\\"' ) + '"' + END +      
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], echoCmd' if IS_WINDOWS else
                     '"sh", ["-c", echoCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("resolveNativePath failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
                EBLK +
                TAB + 'catch(e){ path = "";' + EBLK +
                TAB + 'if( path=="" ) ' + NEW +
                (2*TAB) + 'throw new Error("resolveNativePath failed.")' + END +
                TAB + 'return path' + END +                                                                                                                          
            EBLK + NEW +                        
            'function dirList( path, isSortedByTime ) ' + SBLK +    # TODO: Test in NIX/MAC
                TAB + 'var retList=[]' + END +
                TAB + 'var sortByTime = isSortedByTime ? ' + 
                    ( '" /O:D"' if IS_WINDOWS else '' ) + 
                    ' : ""' + END +
                TAB + 'path = resolveNativePath( path )' + END +
                TAB + 'var dirLsCmd = "' +
                    ('echo off\\n'                     
                     'dir \\"" + path + "\\" /A /B" + sortByTime + "\\n'
                     if IS_WINDOWS else
                     'ls -a \\"" + path + "\\" ' ) + '"' + END +      
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], dirLsCmd' if IS_WINDOWS else
                     '"sh", ["-c", dirLsCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("dir list failed.")' + END +
                TAB + 'try' + SBLK +
                (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
                (2*TAB) + 'cmdOutLns.splice(0, 2)' + END +                                 
                (2*TAB) + 'for( var i=0; i < cmdOutLns.length; i++ )' + SBLK +
                    (3*TAB) + 'var entry = cmdOutLns[i].trim()' + END +
                    (3*TAB) + 'if( entry ) retList.push( entry );' + END +
                (2*TAB) + EBLK +
                EBLK +
                TAB + 'catch(e){}' + NEW +
                TAB + _QtIfwScript.log( '"dir list of: " + path', isAutoQuote=False ) +
                TAB + _QtIfwScript.log( '"entries: " + retList.length', isAutoQuote=False ) +
                TAB + 'for( var i=0; i < retList.length; i++ )' + NEW +
                (2*TAB) + _QtIfwScript.log( 'retList[i]', isAutoQuote=False ) +
                TAB + 'return retList' + END +                                                                                                               
            EBLK + NEW +                        
            'function makeDir( path ) ' + SBLK +      # TODO: Test in NIX/MAC
                TAB + 'path = resolveNativePath( path )' + END +
                TAB + _QtIfwScript.ifPathExists( 'path', isAutoQuote=False ) + 
                (2*TAB) + 'return path' + END +                    
                TAB + 'var mkDirCmd = "' +
                    ('echo off\\n'                     
                     'md \\"" + path + "\\"\\n'
                     'echo " + path + "\\n' 
                     if IS_WINDOWS else
                     'mkdir -p \\"" + path + "\\"; '
                     'echo \\"" + path + "\\"' ) + '"' + END +      
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], mkDirCmd' if IS_WINDOWS else
                     '"sh", ["-c", mkDirCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("makeDir failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
                EBLK +
                TAB + 'catch(e){ path = "";' + EBLK +
                TAB + 'if( path=="" || !' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("makeDir failed. (file does not exists)")' + END +
                TAB + _QtIfwScript.log( '"made dir: " + path', isAutoQuote=False ) + 
                TAB + 'return path' + END +                                                                                                               
            EBLK + NEW +                
            'function removeDir( path ) ' + SBLK +        # TODO: Test in NIX/MAC                  
                TAB + 'path = resolveNativePath( path )' + END +
                TAB + _QtIfwScript.ifNotPathExists( 'path', isAutoQuote=False ) + 
                (2*TAB) + 'return path' + END +                    
                TAB + 'var rmDirCmd = "' +
                    ('echo off\\n'                     
                     'rd /s /q \\"" + path + "\\"\\n'
                     'echo " + path + "\\n' 
                     if IS_WINDOWS else
                     'rm -R \\"" + path + "\\"; '
                     'echo \\"" + path + "\\"' ) + '"' + END +      
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], rmDirCmd' if IS_WINDOWS else
                     '"sh", ["-c", rmDirCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("removeDir failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
                EBLK +
                TAB + 'catch(e){ path = "";' + EBLK +
                TAB + 'if( path=="" || ' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("removeDir failed. (file does not exists)")' + END +
                TAB + _QtIfwScript.log( '"removed dir: " + path', isAutoQuote=False ) + 
                TAB + 'return path' + END +                                                                                                               
            EBLK + NEW +                            
            'function writeScriptFromBase64( fileName, b64, varNames ) ' + SBLK +  # TODO: Test in NIX/MAC                
            TAB + 'var path = writeFileFromBase64( fileName, b64 )' + END +
            TAB + 'replaceQtIfwVarsInFile( path, varNames )' +  END +            
            EBLK + NEW +                                                                         
            'function writeFileFromBase64( fileName, b64 ) ' + SBLK +      # TODO: Test in NIX/MAC
                TAB + 'var path = Dir.toNativeSeparator( Dir.temp() + "/" + fileName )' + END +            
                TAB + 'var tempPath = Dir.toNativeSeparator( Dir.temp() + "/" + fileName + ".b64" )' + END +
                (TAB + 'b64 = "-----BEGIN CERTIFICATE-----\\n" + '
                       'b64 + "\\n-----END CERTIFICATE-----\\n"' + END 
                if IS_WINDOWS else "" ) +
                TAB + 'writeFile( tempPath, b64 )' + END +                                 
                TAB + 'var decodeCmd = "' +
                    ('echo off\\n'                     
                     'certutil /decode \\"" + tempPath + "\\" '
                        '\\"" + path + "\\" >nul 2>nul\\n'
                        'echo " + path + "\\n' 
                     if IS_WINDOWS else
                     'echo $(cat \\"" + tempPath + "\\" | base64) > \\"" + path + "\\";'
                     'echo \\"" + path + "\\"' ) + '"' + END +      
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], decodeCmd' if IS_WINDOWS else
                     '"sh", ["-c", decodeCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("writeFileFromBase64 failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
                EBLK +
                TAB + 'catch(e){ path = "";' + EBLK +
                TAB + 'if( path=="" || !' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("writeFileFromBase64 failed. (file does not exists)")' + END +
                TAB + _QtIfwScript.log( '"Wrote file from base64: " + path', isAutoQuote=False ) + 
                #TAB + 'deleteFile( tempPath )' + END +
                TAB + 'return path' + END +                                                                                                               
            EBLK + NEW +                
            'function replaceQtIfwVarsInFile( path, varNames ) ' + SBLK +          # TODO: Test in NIX/MAC
            (
            TAB + 'var vbs = ' + NEW +
            (2*TAB) + '"Const ForReading = 1\\n" + ' + NEW +
            (2*TAB) + '"Const ForWriting = 2\\n" + ' + NEW +
            (2*TAB) + '"Const Amp = \\"@\\" \\n" + ' + NEW +
            (2*TAB) + '"Dim sFileName, sText\\n" + ' + NEW +
            (2*TAB) + '"\\n" + ' + NEW +
            (2*TAB) + '"sFileName = \\"" + path + "\\"\\n" + ' + NEW +
            (2*TAB) + '"Set oFSO = CreateObject(\\"Scripting.FileSystemObject\\")\\n" + ' + NEW +
            (2*TAB) + '"Set oFile = oFSO.OpenTextFile(sFileName, ForReading)\\n" + ' + NEW +
            (2*TAB) + '"sText = oFile.ReadAll\\n" + ' + NEW +
            (2*TAB) + '"oFile.Close\\n" ' + END +
            TAB + 'for( var i=0; i != varNames.length; ++i ) ' + SBLK +                                    
            (2*TAB) + 'var varName = varNames[i]' + END +
            (2*TAB) + 'var varVal = Dir.toNativeSeparator( installer.value( varName ) )' + END +
            (2*TAB) + 'vbs += "sText = Replace(sText, Amp + \\"" + varName + "\\" + Amp, \\"" + varVal + "\\")\\n"' + NEW +
            TAB + EBLK +
            TAB + 'vbs += ' + NEW +                
            (2*TAB) + '"Set oFile = oFSO.OpenTextFile(sFileName, ForWriting)\\n" + ' + NEW +
            (2*TAB) + '"oFile.Write sText\\n" + ' + NEW + #vbs WriteLine adds extra CR/LF
            (2*TAB) + '"oFile.Close\\n"' + END +            
            TAB + 'executeVbScript( vbs )' + END 
            if IS_WINDOWS else 
            TAB + '' + END) + # TODO: FILLIN!!
            EBLK + NEW +                                                             
            'function killAll( progName ) ' + SBLK + # TODO: Test in NIX/MAC
            TAB + 'var killCmd = "' + _QtIfwScript._KILLALL_CMD_PREFIX + 
                '\\"" + progName + "\\""' + END + 
            TAB + 'installer.execute( ' +
                ('"cmd.exe", ["/k"], killCmd' if IS_WINDOWS else
                 '"sh", ["-c", killCmd]' ) + ' )' + END +             
            EBLK + NEW +                  
            'function sleep( seconds ) ' + SBLK +
            TAB + 'var sleepCmd = "' +  # note Batch timeout doesn't work in a "non-interactive" shell, but this ping kludge does!                 
                ('ping 192.0.2.1 -n 1 -w " + seconds + "000\\n"' if IS_WINDOWS else
                 'sleep " + seconds' ) + END +                                                                                                
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], sleepCmd' if IS_WINDOWS else
                 '"sh", ["-c", sleepCmd]' ) + ' )' + END +             
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Sleep operation failed.")' + END +
            EBLK + NEW +      
            'function escapeEchoText( echo ) ' + SBLK +
                (TAB + 'if( echo.trim()=="" ) return "."' + END if IS_WINDOWS else '' ) +
                TAB + 'var escaped = echo' + END +                      
                TAB + 'return " " + escaped' + END +                                                                                          
            EBLK + NEW +      
            'function writeFile( path, content ) ' + SBLK +            
                TAB + 'path = Dir.toNativeSeparator( path )' + END +           
                TAB + 'var lines = content.split(\"\\n\")' + END +                                             
                TAB + 'var redirect = " >"' + END +      
                TAB + 'var writeCmd = ""' + END +
                (TAB + 'writeCmd += "echo off && "' + END if IS_WINDOWS else "" ) +
                TAB + 'for( i=0; i < lines.length; i++ )' + SBLK +                
                (2*TAB) + 'var echo = escapeEchoText( lines[i] )' + END +
                (2*TAB) + 'writeCmd += "echo" + echo + redirect + ' + NEW +
                    (3*TAB) + '" \\"" + path + "\\"' + ('\\n"' if IS_WINDOWS else ';"' ) + END +
                (2*TAB) + 'redirect = " >>"' + END +                                               
                TAB + EBLK + 
                TAB + 'writeCmd += "echo " + path' + 
                        ( '+ "\\n"' if IS_WINDOWS else '' ) + END +                                  
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], writeCmd' if IS_WINDOWS else
                     '"sh", ["-c", writeCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("Write file failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + EBLK + 
                TAB + 'catch(e){ path = "";' + EBLK +
                TAB + 'if( path=="" || !' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("Write file failed. (file does not exists)")' + END +
                TAB + _QtIfwScript.log( '"Wrote file to: " + path', isAutoQuote=False ) +
                TAB + 'return path' + END +
            EBLK + NEW +                   
            'function deleteFile( path ) ' + SBLK +
                TAB + 'path = Dir.toNativeSeparator( path )' + END +           
                TAB + 'var deleteCmd = "' +                    
                    ('echo off && del \\"" + path + "\\" /q\\necho " + path + "\\n"' 
                     if IS_WINDOWS else
                     'rm \\"" + path + "\\"; echo " + path' ) + END +                                                                                                
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], deleteCmd' if IS_WINDOWS else
                     '"sh", ["-c", deleteCmd]' ) + ' )' + END +             
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("Delete file failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + EBLK + 
                TAB + 'catch(e){ path = "";' + EBLK +                
                TAB + 'if( path=="" || ' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("Delete file failed. (file exists)")' + END +
                TAB + _QtIfwScript.log( '"Deleted file: " + path', isAutoQuote=False ) + 
                TAB + 'return path' + END +                                                                                                                                       
            EBLK + NEW +                                                                     
            'function clearErrorLog() ' + SBLK + # TODO: Call deleteFile()
                TAB + 'var path = ' + _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.ERR_LOG_PATH_CMD_ARG,
                    _QtIfwScript.ERR_LOG_DEFAULT_PATH ) + END + 
                TAB + 'var deleteCmd = "' +                    
                    ('echo off && del \\"" + path + "\\" /q\\necho " + path + "\\n"' 
                     if IS_WINDOWS else
                     'rm \\"" + path + "\\"; echo " + path' ) + END +                                                                                                
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], deleteCmd' if IS_WINDOWS else
                     '"sh", ["-c", deleteCmd]' ) + ' )' + END +             
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("Clear error log failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + EBLK + 
                TAB + 'catch(e){ path = "";' + EBLK +                
                TAB + 'if( path=="" || ' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("Clear error log failed. (file exists)")' + END +
                TAB + _QtIfwScript.log( '"Cleared error log: " + path', isAutoQuote=False ) +                                                                                                                                        
            EBLK + NEW +                           
            'function writeErrorLog( msg ) ' + SBLK +   # TODO: Call writeFile()
                TAB + 'var path = ' + _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.ERR_LOG_PATH_CMD_ARG,
                    _QtIfwScript.ERR_LOG_DEFAULT_PATH ) + END +                
                TAB + 'var writeCmd = "' +
                    ('echo off && '
                     'echo " + msg + " > \\"" + path + "\\"\n'
                     'echo " + path + "\\n"' 
                     if IS_WINDOWS else
                     'echo " + msg + " > \\"" + path + "\\";'
                     'echo " + path' ) + END +      
                TAB + 'var result = installer.execute( ' +
                    ('"cmd.exe", ["/k"], writeCmd' if IS_WINDOWS else
                     '"sh", ["-c", writeCmd]' ) + ' )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("Write error log failed.")' + END +
                TAB + 'try' + SBLK +
                TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
                TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + EBLK + 
                TAB + 'catch(e){ path = "";' + EBLK +
                TAB + 'if( path=="" || !' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("Write error log failed. (file does not exists)")' + END +
                TAB + _QtIfwScript.log( '"Wrote error log to: " + path', isAutoQuote=False ) +                                                                                                
            EBLK + NEW +                                                 
            'function silentAbort( msg ) ' + SBLK +
                TAB + 'writeErrorLog( msg )' + END +
                TAB + 'throw new Error( msg )' + END +                    
            EBLK + NEW +
            'function abort( msg ) ' + SBLK +
                TAB + 'msg = (msg==null || msg=="" ? "Installation aborted! Closing installer..." : msg)' + END +
                TAB + 'writeErrorLog( msg )' + END +
                TAB + 'QMessageBox.critical("errorbox", "Error", msg, QMessageBox.Ok)' + END +
                TAB + 'installer.autoAcceptMessageBoxes()' + END +
                TAB + 'gui.clickButton(buttons.CancelButton)' + END +
                TAB + 'gui.clickButton(buttons.FinishButton)' + END +                
                TAB + '' + END +                    
            EBLK + NEW +
            'function quit( msg ) ' + SBLK +
                TAB + 'msg = (msg==null || msg=="" ? "Click \\"OK\\" to quit..." : msg)' + END +
                TAB + 'writeErrorLog( msg )' + END +
                TAB + 'QMessageBox.warning("warnbox", "Installation canceled", msg, QMessageBox.Ok)' + END +
                TAB + 'installer.autoAcceptMessageBoxes()' + END +
                TAB + 'gui.clickButton(buttons.CancelButton)' + END +
                TAB + 'gui.clickButton(buttons.FinishButton)' + END +                
                TAB + '' + END +                    
            EBLK + NEW                                              
        )        
        if IS_WINDOWS : 
            # EMBEDDED VB SCRIPT
            self.qtScriptLib += (
            'function executeVbScript( vbs ) ' + SBLK +
                TAB + _QtIfwScript.log( "Executing VbScript:" ) +
                TAB + _QtIfwScript.log( "vbs", isAutoQuote=False ) +          
                TAB + 'var path = writeFile( Dir.temp() + "/__qtIfwInstaller.vbs", vbs )' + END +
                TAB + 'var result = installer.execute(' + 
                    '"cscript", ["//Nologo", path])' + END +
                TAB + _QtIfwScript.log( "Vbs execution Result:" ) +                
                TAB + _QtIfwScript.log( "result[0]", isAutoQuote=False ) + 
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("VbScript operation failed.")' + END +
                TAB + 'for( i=0; i < 3; i++ )' + SBLK +
                (2*TAB) + 'try{ deleteFile( path ); break; }' + NEW +                          
                (2*TAB) + 'catch(e){ sleep(1); }' + NEW +
                TAB + EBLK + NEW +
            EBLK + NEW +
            'function executeVbScriptDetached( scriptPath, vbs ) ' + SBLK +
                TAB + _QtIfwScript.log( "Executing Detached VbScript:" ) +
                TAB + _QtIfwScript.log( "scriptPath", isAutoQuote=False ) +                
                TAB + _QtIfwScript.log( "vbs", isAutoQuote=False ) +          
                TAB + 'var path = writeFile( scriptPath, vbs )' + END +
                TAB + 'var result = installer.executeDetached(' + 
                    '"cscript", ["//Nologo", path])' + END +
            EBLK + NEW                                                          
            )
        elif IS_LINUX:
            self.qtScriptLib += (    
            'function isPackageManagerInstalled( prog ) ' + SBLK +
                TAB + 'return installer.execute( prog, ["--help"] )[1] == 0' + END +
            EBLK + NEW +
            'function isAptInstalled() ' + SBLK +
                TAB + 'return isPackageManagerInstalled( "apt" )' + END +             
            EBLK + NEW +
            'function isDpkgInstalled() ' + SBLK +
                TAB + 'return isPackageManagerInstalled( "dpkg" )' + END +             
            EBLK + NEW +
            'function isYumInstalled() ' + SBLK +
                TAB + 'return isPackageManagerInstalled( "yum" )' + END +             
            EBLK + NEW +
            'function isRpmInstalled() ' + SBLK +
                TAB + 'return isPackageManagerInstalled( "rpm" )' + END +             
            EBLK + NEW +
            'function isPackageInstalled( pkg ) ' + SBLK +
                TAB + 'if( isDpkgInstalled() )' + NEW +             
                (2*TAB) + 'return installer.execute( "dpkg", ["-l", pkg] )[1] == 0' + END +
                TAB + 'else if( isRpmInstalled() )' + NEW +             
                (2*TAB) + 'return installer.execute( "rpm", ["-q", pkg] )[1] == 0' + END +
                TAB + 'throw new Error("No supported package manager found.")' + END +                                                     
            EBLK + NEW +
            'function installPackage( pkg ) ' + SBLK +
                TAB + 'if( isAptInstalled() )' + NEW +             
                (2*TAB) + 'return installer.execute( "apt-get", ["install", "-y", pkg] )[1] == 0' + END +
                TAB + 'else if( isYumInstalled() )' + NEW +             
                (2*TAB) + 'return installer.execute( "yum", ["install", "-y", pkg] )[1] == 0' + END +
                TAB + 'throw new Error("No supported package manager found.")' + END +                                                     
            EBLK + NEW +
            'function unInstallPackage( pkg ) ' + SBLK +
                TAB + 'if( isAptInstalled() )' + NEW +             
                (2*TAB) + 'return installer.execute( "apt-get", ["remove", "-y", pkg] )[1] == 0' + END +
                TAB + 'else if( isYumInstalled() )' + NEW +             
                (2*TAB) + 'return installer.execute( "yum", ["remove", "-y", pkg] )[1] == 0' + END +
                TAB + 'throw new Error("No supported package manager found.")' + END +                                                     
            EBLK + NEW 
            )
                                                    
    def __str__( self ) :
        if not self.script: self._generate()
        return self.script
        
    def write( self ):
        pkgDir = self.dirPath()
        if not isDir( pkgDir ): makeDir( pkgDir )
        with open( self.path(), 'w' ) as f: 
            f.write( str(self) ) 
    
    def debug( self ): print( str(self) )

    def exists( self ): return isFile( self.path() )
    
    @abstractmethod        
    def _generate( self ) : """PURE VIRTUAL"""        
        
    @abstractmethod
    def path( self )      : """PURE VIRTUAL""" 
        
    @abstractmethod
    def dirPath( self )   : """PURE VIRTUAL"""     

# -----------------------------------------------------------------------------
class QtIfwControlScript( _QtIfwScript ):
        
    __DIR_TMPLT  = "%s/config"
    __PATH_TMPLT = __DIR_TMPLT + "/%s"
    
    __PAGE_CALLBACK_FUNC_TMPLT = (
"""    
Controller.prototype.%sPageCallback = function() {
    %s
}\n
""" )

    __CONTROLER_CALLBACK_FUNC_TMPLT = (
"""
Controller.prototype.%s = function(){
    %s
}\n
""" )

    __CONTROLER_CONNECT_TMPLT = ( 
        "%s.connect(this, Controller.prototype.%s);\n" ) 
    __WIDGET_CONNECT_TMPLT = ( 
        "gui.currentPageWidget().%s.%s.connect(this, this.%s);\n" )

    __PAGE_WIDGET = 'gui.pageWidgetByObjectName("%s")'
    __PAGE_WIDGET_VAR_TMPLT = ( 
        '    var %s = gui.pageWidgetByObjectName("%s");\n' )

    __CUSTOM_PAGE_WIDGET = 'gui.pageWidgetByObjectName("Dynamic%s")'
    __CUSTOM_PAGE_WIDGET_VAR_TMPLT = ( 
        '    var %s = gui.pageWidgetByObjectName("Dynamic%s");\n' )
            
    __CURRENT_PAGE_WIDGET = "gui.currentPageWidget()"
    __CUR_PG_WIDGET_VAR_TMPLT = "    var %s = gui.currentPageWidget();\n"
                        
    __CLICK_BUTTON_TMPL       = "gui.clickButton(%s);\n"
    __CLICK_BUTTON_DELAY_TMPL = "gui.clickButton(%s, %d);\n"
    
    __SET_ENBALE_STATE_TMPL = (
        "gui.currentPageWidget().%s.setEnabled(%s);\n" )
    
    __SET_VISIBLE_STATE_TMPL = (
        "gui.currentPageWidget().%s.setVisible(%s);\n" )
    
    __SET_CHECKBOX_STATE_TMPL = (
        "gui.currentPageWidget().%s.setChecked(%s);\n" )

    __SET_TEXT_TMPL = (
        "gui.currentPageWidget().%s.setText(%s);\n" )
       
    __GET_TEXT_TMPL = ( "gui.currentPageWidget().%s.text" )

    __ASSIGN_TEXT_TMPL = ( "    var %s = gui.currentPageWidget().%s.text;\n" ) 

    __UI_PAGE_CALLBACK_FUNC_TMPLT = (
"""
    Controller.prototype.Dynamic%sCallback = function() {
        %s
    }
"""    )
                  
    NEXT_BUTTON   = "buttons.NextButton"
    BACK_BUTTON   = "buttons.BackButton"
    CANCEL_BUTTON = "buttons.CancelButton"
    FINISH_BUTTON = "buttons.FinishButton"
    
    TARGET_DIR_EDITBOX       = "TargetDirectoryLineEdit"
    START_MENU_DIR_EDITBOX   = "StartMenuPathLineEdit"
    ACCEPT_EULA_RADIO_BUTTON = "AcceptLicenseRadioButton"
    RUN_PROGRAM_CHECKBOX     = "RunItCheckBox"
                                    
    @staticmethod        
    def _purgeTempFiles():                  
        return( _QtIfwScript.ifCmdLineSwitch( _KEEP_TEMP_SWITCH, 
                                              isNegated=True ) +
                _QtIfwScript.removeDir( 
            _QtIfwScript._TEMP_DIR, isAutoQuote=False ) ) 
                                            
    @staticmethod        
    def currentPageWidget():                
        return QtIfwControlScript.__CURRENT_PAGE_WIDGET            

    @staticmethod        
    def pageWidget( name ): 
        return QtIfwControlScript._PAGE_WIDGET % (name,)     

    @staticmethod        
    def customPageWidget( name ): 
        return QtIfwControlScript.__CUSTOM_PAGE_WIDGET % (name,)     

    @staticmethod        
    def assignCurPageWidgetVar( varName="page" ):                
        return QtIfwControlScript.__CUR_PG_WIDGET_VAR_TMPLT % (varName,)            

    @staticmethod        
    def assignPageWidgetVar( pageName, varName="page" ):                
        return QtIfwControlScript.__PAGE_WIDGET_VAR_TMPLT % (varName,pageName)            

    @staticmethod        
    def assignCustomPageWidgetVar( pageName, varName="page" ):                
        return QtIfwControlScript.__CUSTOM_PAGE_WIDGET_VAR_TMPLT % (
                varName, pageName )                        
            
    @staticmethod        
    def connectWidgetEventHandler( controlName, eventName, slotName ):
        return QtIfwControlScript.__WIDGET_CONNECT_TMPLT % ( 
            controlName, eventName, slotName );

    @staticmethod        
    def connectButtonClickHandler( buttonName, slotName ):
        return QtIfwControlScript.connectWidgetEventHandler( 
            buttonName, QtIfwControlScript.__BUTTON_CLICKED_SIGNAL_NAME, slotName );

    @staticmethod        
    def clickButton( buttonName, delayMillis=None ):                
        return ( 
            QtIfwControlScript.__CLICK_BUTTON_DELAY_TMPL 
                % (buttonName, delayMillis)
            if delayMillis else
            QtIfwControlScript.__CLICK_BUTTON_TMPL 
                % (buttonName,) )

    @staticmethod        
    def enable( controlName, isEnable=True ):                
        return QtIfwControlScript.__SET_ENBALE_STATE_TMPL % ( 
            controlName, _QtIfwScript.TRUE if isEnable else _QtIfwScript.FALSE)

    @staticmethod        
    def setVisible( controlName, isVisible=True ):                
        return QtIfwControlScript.__SET_VISIBLE_STATE_TMPL % ( 
            controlName, _QtIfwScript.TRUE if isVisible else _QtIfwScript.FALSE)

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def setCheckBox( checkboxName, isCheck=True ):                
        return QtIfwControlScript.__SET_CHECKBOX_STATE_TMPL % ( 
            checkboxName, _QtIfwScript.TRUE if isCheck else _QtIfwScript.FALSE )

    @staticmethod        
    def setText( controlName, text, isAutoQuote=True ):                
        return QtIfwControlScript.__SET_TEXT_TMPL % ( 
                controlName, _QtIfwScript._autoQuote( text, isAutoQuote ) )

    @staticmethod        
    def getText( controlName ):                
        return QtIfwControlScript.__GET_TEXT_TMPL % (controlName,)   
    
    # QtIfwControlScript
    def __init__( self, 
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.virtualArgs = None

        self.uiPages = []

        self._installerResources = []
        self._maintenanceToolResources = []

        self.controllerGlobals = None
        self.isAutoGlobals = True
        
        self.controllerConstructorBody = None
        self.isAutoControllerConstructor = True
                                                   
        self.isIntroductionPageVisible = True                                                                    
        self.introductionPageCallbackBody = None
        self.isAutoIntroductionPageCallback = True

        self.isTargetDirectoryPageVisible = True
        self.targetDirectoryPageCallbackBody = None
        self.isAutoTargetDirectoryPageCallback = True

        self.isComponentSelectionPageVisible = True
        self.componentSelectionPageCallbackBody = None
        self.isAutoComponentSelectionPageCallback = True

        self.isLicenseAgreementPageVisible = True
        self.licenseAgreementPageCallbackBody = None
        self.isAutoLicenseAgreementPageCallback = True

        self.isStartMenuDirectoryPageVisible = True
        self.startMenuDirectoryPageCallbackBody = None
        self.isAutoStartMenuDirectoryPageCallback = True

        self.isReadyForInstallationPageVisible = True
        self.readyForInstallationPageCallbackBody = None
        self.isAutoReadyForInstallationPageCallback = True

        self.isPerformInstallationPageVisible = True
        self.performInstallationPageCallbackBody = None
        self.isAutoPerformInstallationPageCallback = True
        
        self.isFinishedPageVisible = True
        self.finishedPageCallbackBody = None
        self.isAutoFinishedPageCallback = True        

        self.isRunProgInteractive = True
        self.isRunProgVisible = True

        self.__widgetEventSlots = {}

        self.__standardEventSlots = {}        
        self.registerStandardEventHandler( 
            'installationFinished', 'onInstallFinished',
            QtIfwControlScript._purgeTempFiles() );                                                                 
        self.registerStandardEventHandler( 
            'uninstallationFinished', 'onUninstallFinished',
            QtIfwControlScript._purgeTempFiles() );                                                                 
        self.registerStandardEventHandler( 
            'updateFinished', 'onUpdateFinished',
            QtIfwControlScript._purgeTempFiles() );                                                                 
        self.registerStandardEventHandler( 
            'installationInterrupted', 'onInstallationInterrupted',
            QtIfwControlScript._purgeTempFiles() );                                                                 
        self.registerGuiEventHandler( 
            'interrupted', 'onGuiInterrupted',
            QtIfwControlScript._purgeTempFiles() );                                                                 
                
        self.__autoPilotEventSlots = {}
        self.registerAutoPilotEventHandler( 
            'installationFinished', 'onAutoInstallFinished',
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 
        self.registerAutoPilotEventHandler( 
            'uninstallationFinished', 'onAutoUninstallFinished',
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 
        self.registerAutoPilotEventHandler( 
            'updateFinished', 'onAutoUpdateFinished',
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 
        
    def registerStandardEventHandler( self, signalName, slotName, slotBody ) :
        signalKey = "%s.%s" % (_QtIfwScript._INSTALLER_OBJ, signalName)
        self.__standardEventSlots[ signalKey ] = ( slotName, slotBody )

    def registerGuiEventHandler( self, signalName, slotName, slotBody ) :
        signalKey = "%s.%s" % (_QtIfwScript._GUI_OBJ, signalName)
        self.__standardEventSlots[ signalKey ] = ( slotName, slotBody )

    def registerAutoPilotEventHandler( self, signalName, slotName, slotBody ) :
        signalKey = "%s.%s" % (_QtIfwScript._INSTALLER_OBJ, signalName)
        self.__autoPilotEventSlots[ signalKey ] = ( slotName, slotBody )
    
    def registerWidgetEventHandler( self, pageId, controlName, 
                                    signalName, slotName, slotBody ) :
        self.__widgetEventSlots[pageId][controlName][signalName] = (
            slotName, slotBody )
                                                             
    def _generate( self ) :        
        self.script = ""
                
        if self.isAutoLib: _QtIfwScript._genLib( self )        
        if self.qtScriptLib: self.script += self.qtScriptLib

        self.script += _QtIfwScript.embedResources( 
            self._maintenanceToolResources ) 

        if self.isAutoGlobals: self.__genGlobals()
        if self.controllerGlobals: self.script += self.controllerGlobals
        
        if self.isAutoControllerConstructor:
            self.__genControllerConstructorBody()
        self.script += ( "function Controller() {\n%s\n}\n" % 
                         (self.controllerConstructorBody,) )
                            
        if self.isAutoIntroductionPageCallback:
            self.__genIntroductionPageCallbackBody()
        if self.introductionPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_INTRO_PAGE, self.introductionPageCallbackBody) )
                        
        if self.isAutoTargetDirectoryPageCallback:
            self.__genTargetDirectoryPageCallbackBody()
        if self.targetDirectoryPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_TARGET_DIR_PAGE, self.targetDirectoryPageCallbackBody) )

        if self.isAutoComponentSelectionPageCallback:
            self.__genComponentSelectionPageCallbackBody()
        if self.componentSelectionPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_COMPONENTS_PAGE, self.componentSelectionPageCallbackBody) )

        if self.isAutoLicenseAgreementPageCallback:
            self.__genLicenseAgreementPageCallbackBody()
        if self.licenseAgreementPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_LICENSE_PAGE, self.licenseAgreementPageCallbackBody) )

        if self.isAutoStartMenuDirectoryPageCallback:
            self.__genStartMenuDirectoryPageCallbackBody()
        if self.startMenuDirectoryPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_START_MENU_PAGE, self.startMenuDirectoryPageCallbackBody) )

        if self.isAutoReadyForInstallationPageCallback:
            self.__genReadyForInstallationPageCallbackBody()
        if self.readyForInstallationPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_READY_PAGE, self.readyForInstallationPageCallbackBody) )

        if self.isAutoPerformInstallationPageCallback:
            self.__genPerformInstallationPageCallbackBody()
        if self.performInstallationPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_INSTALL_PAGE, self.performInstallationPageCallbackBody) )

        if self.isAutoFinishedPageCallback:
            self.__genFinishedPageCallbackBody()
        if self.finishedPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (QT_IFW_FINISHED_PAGE, self.finishedPageCallbackBody) )

        for _, (funcName, funcBody) in six.iteritems( self.__standardEventSlots ):    
            self.script += ( 
                QtIfwControlScript.__CONTROLER_CALLBACK_FUNC_TMPLT %
                (funcName, funcBody) )

        for _, (funcName, funcBody) in six.iteritems( self.__autoPilotEventSlots ):    
            self.script += ( 
                QtIfwControlScript.__CONTROLER_CALLBACK_FUNC_TMPLT %
                (funcName, funcBody) )
        
        self.__appendUiPageCallbacks()

    def __appendUiPageCallbacks( self ):    
        if self.uiPages: 
            for p in self.uiPages:
                # enter page event handler                
                if p.onAutoPilotClickNext:
                    clickNext=(
                        _QtIfwScript.TAB +
                        _QtIfwScript.ifCmdLineSwitch( 
                            _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                            QtIfwControlScript.clickButton( 
                                QtIfwControlScript.NEXT_BUTTON ) )
                    try: p.onEnter += clickNext
                    except: p.onEnter = clickNext
                                                    
                if p.onEnter:
                    self.script += (                         
                        QtIfwControlScript.__UI_PAGE_CALLBACK_FUNC_TMPLT % 
                        ( p.name, p.onEnter ) )

    def __genGlobals( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK
        self.controllerGlobals=""
        if self.virtualArgs :
            self.controllerGlobals += (
            'function initGlobals() ' + SBLK )
            for k,v in six.iteritems( self.virtualArgs ):            
                self.controllerGlobals += TAB + _QtIfwScript.setValue(k,v) +END 
            self.controllerGlobals += EBLK + NEW             
        self.controllerGlobals += (
            'function toMaintenanceToolPath( dir ) ' + SBLK +
                TAB + 'return dir + ' + _QtIfwScript.PATH_SEP + ' + ' +
                    ('"%s"' % (_QtIfwScript.MAINTENANCE_TOOL_NAME,)) + END + 
            EBLK + NEW +            
            'function maintenanceToolExists( dir ) ' + SBLK +
                TAB + 'return ' + _QtIfwScript.pathExists( 
                    'toMaintenanceToolPath( dir )', isAutoQuote=False ) + END + 
            EBLK + NEW +
            'function defaultTargetExists() ' + SBLK +
                TAB + 'return maintenanceToolExists( ' + 
                    _QtIfwScript.targetDir() + ' )' + END +  
            EBLK + NEW +
            'function cmdLineTargetExists() ' + SBLK +            
                TAB + 'return maintenanceToolExists( ' + 
                    _QtIfwScript.cmdLineArg( _QtIfwScript.TARGET_DIR_CMD_ARG ) +
                    ' )' + END +
            EBLK + NEW +
            'function targetExists( isAuto ) ' + SBLK +
                (TAB + 'if( isOsRegisteredProgram() ) ' + SBLK +
                 (2*TAB)  + _QtIfwScript.log('The program is OS registered.') +
                 (2*TAB) + 'return true' + END + 
                TAB + EBLK                  
                if IS_WINDOWS else '') +
                TAB + _QtIfwScript.ifCmdLineArg( 
                    _QtIfwScript.TARGET_DIR_CMD_ARG, isMultiLine=True ) +
                    'if( isAuto && cmdLineTargetExists() )'  + SBLK +
                        (3*TAB) + _QtIfwScript.log('The command line specified target exists.') +
                        (3*TAB) + 'return true' + END +
                    (2*TAB) + EBLK +
                TAB + EBLK +
                TAB + 'if( defaultTargetExists() )'  + SBLK +
                TAB + _QtIfwScript.log('The default target exists.') +
                (2*TAB) + 'return true' + END +                
                TAB + EBLK +                   
                TAB + 'return false' + END +                 
            EBLK + NEW +            
            'function removeTarget( isAuto ) ' + SBLK +
                TAB + _QtIfwScript.log('Removing existing installation...') +  
                TAB + 'var args=[ "-v", ' +                     
                    '"' + _QtIfwScript.AUTO_PILOT_CMD_ARG + '=' +
                    _QtIfwScript.TRUE + '" ' + 
                    ', "' + _QtIfwScript.MAINTAIN_MODE_CMD_ARG + '=' + 
                    _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL + '" ' 
                    "]" + END +
                TAB + _QtIfwScript.ifCmdLineSwitch( _KEEP_TEMP_SWITCH ) +
                    'args.push( "' + _KEEP_TEMP_SWITCH + '=true" )' + END +                     
                TAB + 'var exeResult' + END +
                (TAB + 'var regPaths = maintenanceToolPaths()' + END + 
                 TAB + 'if( regPaths != null )' + SBLK +
                (2*TAB) + 'for( i=0; i < regPaths.length; i++ )' + NEW +
                    (3*TAB) + 'exeResult = execute( regPaths[i], args )' + END + 
                TAB + EBLK +
                TAB + 'else '
                if IS_WINDOWS else TAB) +
                _QtIfwScript.ifCmdLineArg( 
                    _QtIfwScript.TARGET_DIR_CMD_ARG ) +
                    'exeResult = execute( toMaintenanceToolPath( ' +
                        _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.TARGET_DIR_CMD_ARG ) + ' ), args )' + END +
                TAB + 'else ' + NEW +                        
                (2*TAB) + 'exeResult = execute( toMaintenanceToolPath( ' +
                        _QtIfwScript.targetDir() + ' ), args )' + END +
                TAB + '// The MaintenanceTool is not removed until a moment\n' + 
                TAB + '// or two has elapsed after it was closed...' + NEW +
                TAB + _QtIfwScript.log('Verifying uninstall...') +    
                TAB + 'var MAX_CHECKS=3' + END  +
                TAB + 'for( var existCheck=0; existCheck < MAX_CHECKS; existCheck++ ) ' + SBLK +
                (2*TAB) + 'if( !targetExists( isAuto ) ) break' + END +
                (2*TAB) + _QtIfwScript.log('Waiting for uninstall to finish...') +                
                (2*TAB) + 'sleep( 1 )' + END +                
                TAB + EBLK +
                TAB + 'if( targetExists( isAuto ) ) ' + NEW +
                (2*TAB) + 'silentAbort("Failed to removed the program.")' + END +
                TAB + _QtIfwScript.log('Successfully removed the program.') +
            EBLK + NEW +
            'function autoManagePriorInstallation() ' + SBLK +
                TAB + "if( targetExists( true ) ) " + SBLK +
                (2*TAB) + 'switch (' + _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG ) + ')' + SBLK +
                (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_FAIL + '":' + NEW +
                    (3*TAB) + 'silentAbort("This program is already installed.")' + END + 
                (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_REMOVE + '":' + NEW + 
                    (3*TAB) + 'removeTarget( true )' + END +
                    (3*TAB) + 'break' + END +
                (2*TAB) + 'default:' + NEW +
                    (2*TAB) + _QtIfwScript.switchYesNoCancelPopup(  
                  'This program is already installed. ' +
                  'Would you like to uninstall it first?', 
                  title='Uninstall first?', 
                  resultVar="uninstallChoice", 
                  onYes='removeTarget( true );', 
                  onNo="// proceed without action...",
                  onCancel='silentAbort("This program is already installed.");'
                  ) +
                  (3*TAB) + 'break' + END +                  
                  EBLK +           
                EBLK +                         
            EBLK + NEW +
            'function managePriorInstallation() ' + SBLK +
                TAB + "if( targetExists( false ) ) " + SBLK +
                (2*TAB) + 'switch (' + _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG ) + ')' + SBLK +
                (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_REMOVE + '":' + NEW + 
                    (3*TAB) + 'removeTarget( false )' + END +
                    (3*TAB) + 'break' + END +
                (2*TAB) + 'default:' + NEW +
                    (2*TAB) + _QtIfwScript.ifYesNoPopup(  
                  'This program is already installed. ' +
                  'Do you wish to replace the prior installation? ' +
                  '(Select \\"No\\" to cancel and quit.)', 
                  title='Replace prior?', 
                  resultVar="uninstallChoice" ) + 
                        (2*TAB) + 'removeTarget( false )' + END +                  
                    TAB + 'else' + NEW +
                        (2*TAB) + 'quit()' + END +         
                    (3*TAB) + 'break' + END +                  
                  EBLK +         
                EBLK +                         
            EBLK + NEW                                                                          
            )

        if IS_WINDOWS : 
            # To query to the Windows registry for uninstall strings registered by
            # QtIFW for a program of a given name, this example command works when 
            # run directly on the command prompt. 
            #             
            # cmd.exe /k "@echo off & for /f delims^=^ eol^= %i in ('REG QUERY HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall\ /s /f "Hello Packages Example" /t REG_SZ /c /e ^| find "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\"') do ( for /f "tokens=2*" %a in ('REG QUERY %i /v "UninstallString" ^| find "UninstallString"') do echo %b )"
            #
            # Unfortunately, it only seemed to be 
            # possible to run this via an stdin pipe with the QtIFW execute function, 
            # rather than passing it as a direct cmd argument.
            #
            # Note the regQueryUninstallKeys string is defined below with 
            # multiple levels of escape. Reviewing the resulting QScript maybe easier
            # for initial debugging than doing so in this Python layer.                
            regQueryUninstallKeys = '@echo off & for /f delims^=^ eol^= %i in (\\\'REG QUERY HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Uninstall\\\\ /s /f \\"" + installer.value("ProductName") + "\\" /t REG_SZ /c /e ^| find \\"HKEY_CURRENT_USER\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Uninstall\\\\\\"\\\') do ( for /f \\"tokens=2*\\" %a in (\\\'REG QUERY %i /v \\"UninstallString\\" ^| find \\"UninstallString\\"\\\') do echo %b )\\n'          
            self.controllerGlobals += (
            '// returns null if no installation is registered OR an array,' + NEW +
            '// accounting for the fact that, while unlikely,' + NEW +
            '// it is possible to have multiple installations of the product' + NEW +
            '// (with different paths to them)' + NEW +
            'function maintenanceToolPaths() ' + SBLK +
                TAB + 'if( !installer.gainAdminRights() ) ' + NEW +
                (2*TAB) + 'throw new Error("Elevated privileges required.")' + END +
                TAB + ('var regQuery = "%s"' % (regQueryUninstallKeys,) ) + END +
                TAB + 'var result = installer.execute( "cmd.exe", ["/k"], regQuery )' + END +                
                TAB + 'if( result[1] != 0 ) ' + NEW +
                (2*TAB) + 'throw new Error("Registry query failed.")' + END +
                TAB + '// remove the first line (which is a command echo)' + NEW +
                TAB + '// remove blank lines & convert an empty array to null' + NEW +                
                TAB + 'var retArr = result[0].split(\"\\n\")' + END +
                TAB + 'try{ retArr.splice(0, 1)' + END + EBLK +
                TAB + 'catch(e){ throw new Error("Registry query failed.")' + END + EBLK +
                TAB + 'for( i=0; i < retArr.length; i++ )' + SBLK + 
                (2*TAB) + 'retArr[i] = retArr[i].trim()' + END + 
                (2*TAB) + 'if( retArr[i]==\"\" ) retArr.splice(i, 1)' + END + 
                EBLK +
                TAB + 'return retArr.length == 0 ? null : retArr' + END +                  
            EBLK + NEW +
            'function isOsRegisteredProgram() ' + SBLK +
                TAB + 'return maintenanceToolPaths() != null' + END + 
            EBLK + NEW           
            )

    def __genControllerConstructorBody( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK        
                              
        self.controllerConstructorBody = (
            TAB + 'installer.setValue( ' + 
                ('"%s"' % (_QT_IFW_INSTALLER_TEMP_DIR,)) + ', "" )' + END + 
            TAB + 'installer.setValue( ' + 
                ('"%s"' % (_QT_IFW_MAINTENANCE_TEMP_DIR,)) + ', "" )' + END + 
            TAB + 'installer.setValue( "__lockFilePath", "" )' + END +
            TAB + 'installer.setValue( "__watchDogPath", "" )' + END +
            TAB + 'clearErrorLog()' + END +
            TAB +  _QtIfwScript.log( ('"%s = " + ' % (_KEEP_TEMP_SWITCH,)) +
                _QtIfwScript.lookupValue(_KEEP_TEMP_SWITCH, "false" ), 
                isAutoQuote=False ) +
            TAB + '__installerTempPath()' + END +
            TAB + '__maintenanceTempPath()' + END +            
            TAB + 'makeDir( Dir.temp() )' + END +
            # currently the entire point of the watchdog is purge temp files,
            # so when _keeptemp is enabled, just drop that entire mechanism!
            TAB + _QtIfwScript.ifCmdLineSwitch( _KEEP_TEMP_SWITCH, 
                                                isNegated=True ) +
            TAB + '__launchWatchDog()' + END )        
        if self.virtualArgs :  
            self.controllerConstructorBody += TAB + 'initGlobals()' + END

        self.controllerConstructorBody += (
            _QtIfwScript.ifMaintenanceTool( isMultiLine=True ) +
                _QtIfwScript.genResources( self._maintenanceToolResources ) +
            EBLK )
        
        HIDE_PAGE_TMPLT = ( TAB + 
            'installer.setDefaultPageVisible(QInstaller.%s, false)' ) + END
        def hidePage( pageName ): 
            self.controllerConstructorBody += HIDE_PAGE_TMPLT % (pageName,)
        if not self.isIntroductionPageVisible:                                                                    
            hidePage( QT_IFW_INTRO_PAGE )
        if not self.isTargetDirectoryPageVisible:                                                                    
            hidePage( QT_IFW_TARGET_DIR_PAGE )
        if not self.isComponentSelectionPageVisible:
            hidePage( QT_IFW_COMPONENTS_PAGE )
        if not self.isLicenseAgreementPageVisible:                                                                    
            hidePage( QT_IFW_LICENSE_PAGE )
        if not self.isStartMenuDirectoryPageVisible:                                                                    
            hidePage( QT_IFW_START_MENU_PAGE )
        if not self.isReadyForInstallationPageVisible:                                                                    
            hidePage( QT_IFW_READY_PAGE )
        if not self.isPerformInstallationPageVisible:                                                                    
            hidePage( QT_IFW_INSTALL_PAGE )
        if not self.isFinishedPagePageVisible:                                                                    
            hidePage( QT_IFW_FINISHED_PAGE )
            
        for signalName, (slotName, _) in six.iteritems( self.__standardEventSlots ):    
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                (signalName, slotName) )            
        self.controllerConstructorBody += _QtIfwScript.ifCmdLineSwitch( 
                _QtIfwScript.AUTO_PILOT_CMD_ARG, isMultiLine=True )             
        for signalName, (slotName, _) in six.iteritems( self.__autoPilotEventSlots ):    
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                (signalName, slotName) )            
        self.controllerConstructorBody += (        
                _QtIfwScript.ifInstalling() + 
                    'autoManagePriorInstallation()' + END +
                'else ' + SBLK +
                    TAB + 'var mode = ' + _QtIfwScript.cmdLineArg( 
                        _QtIfwScript.MAINTAIN_MODE_CMD_ARG ) + END + 
                    TAB + 'switch( mode ) ' + SBLK +
                    (2*TAB) + 'case "' + 
                        _QtIfwScript.MAINTAIN_MODE_OPT_ADD_REMOVE + '":' + NEW +
                        (3*TAB) + 'installer.setPackageManager()' + END +
                        (3*TAB) + 'break' + END +
                    (2*TAB) + 'case "' + 
                        _QtIfwScript.MAINTAIN_MODE_OPT_UPDATE + '":' + NEW +
                        (3*TAB) + 'installer.setUpdater()' + END +
                        (3*TAB) + 'break' + END +
                    (2*TAB) + 'case "' +                         
                        _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL + '":' + NEW +
                        (3*TAB) + 'installer.setUninstaller()' + END +
                        (3*TAB) + 'break' + END +
                    (2*TAB) + EBLK +
                TAB + EBLK +    
            EBLK )        
                                 
    def __genIntroductionPageCallbackBody( self ):
        self.introductionPageCallbackBody = (
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        ) 

    def __genTargetDirectoryPageCallbackBody( self ):
        self.targetDirectoryPageCallbackBody = (
            _QtIfwScript.ifCmdLineArg( 
                _QtIfwScript.TARGET_DIR_CMD_ARG ) +
                _QtIfwScript.TAB + QtIfwControlScript.setText(
                    QtIfwControlScript.TARGET_DIR_EDITBOX, 
                    _QtIfwScript.cmdLineArg( 
                        _QtIfwScript.TARGET_DIR_CMD_ARG ), 
                    isAutoQuote=False ) +
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        ) 

    def __genComponentSelectionPageCallbackBody( self ):
        self.componentSelectionPageCallbackBody = (
            QtIfwControlScript.assignCurPageWidgetVar( "page" ) +            
            '    ' + _QtIfwScript.ifCmdLineArg( 
                _QtIfwScript.INSTALL_LIST_CMD_ARG ) + 
            '    {\n' +
            '        var comps = ' +
                    _QtIfwScript.cmdLineListArg( 
                        _QtIfwScript.INSTALL_LIST_CMD_ARG ) + ';\n' +
            '        if( comps[0]="all" )\n'
            '            page.selectAll();\n' +
            '        else {\n' +
            '            page.deselectAll();\n' +
            '            for( i=0; i < comps.length; i++ ) \n' +
            '                page.selectComponent( comps[i].trim() );\n' +
            '        }\n' +                         
            '    }\n' +
            '    else {\n' +            
            '        var includes = ' +
                        _QtIfwScript.cmdLineListArg( 
                            _QtIfwScript.INCLUDE_LIST_CMD_ARG ) + ';\n' +
            '        for( i=0; i < includes.length; i++ ) \n' +
            '            page.selectComponent( includes[i].trim() );\n' +
            '\n' +
            '        var excludes = ' +
                        _QtIfwScript.cmdLineListArg( 
                            _QtIfwScript.EXCLUDE_LIST_CMD_ARG ) + ';\n' +
            '        for( i=0; i < excludes.length; i++ ) \n' +
            '            page.deselectComponent( excludes[i].trim() );\n' +
            '    }\n' +
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        )

    def __genLicenseAgreementPageCallbackBody( self ):
        self.licenseAgreementPageCallbackBody = (
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
            '{\n' +                        
                QtIfwControlScript.setCheckBox( 
                    QtIfwControlScript.ACCEPT_EULA_RADIO_BUTTON ) +                 
                _QtIfwScript.TAB + QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) + 
            '    }\nelse{\n' +
                _QtIfwScript.ifCmdLineArg( 
                    _QtIfwScript.ACCEPT_EULA_CMD_ARG ) +  
                    _QtIfwScript.TAB +             
                    QtIfwControlScript.setCheckBox( 
                        QtIfwControlScript.ACCEPT_EULA_RADIO_BUTTON, 
                            _QtIfwScript.cmdLineSwitchArg(
                                _QtIfwScript.ACCEPT_EULA_CMD_ARG ) ) +
            '    }'                      
        )                         

    def __genStartMenuDirectoryPageCallbackBody( self ):
        self.startMenuDirectoryPageCallbackBody = (
            _QtIfwScript.ifCmdLineArg( 
                _QtIfwScript.START_MENU_DIR_CMD_ARG ) +
                _QtIfwScript.TAB + 
                QtIfwControlScript.setText(
                    QtIfwControlScript.START_MENU_DIR_EDITBOX, 
                    _QtIfwScript.cmdLineArg( 
                        _QtIfwScript.START_MENU_DIR_CMD_ARG ), 
                    isAutoQuote=False ) +
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +                 
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        )

    def __genReadyForInstallationPageCallbackBody( self ):
        self.readyForInstallationPageCallbackBody = (
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) + 
            '    else {\n' +                
            '        ' + _QtIfwScript.ifInstalling() +
                        ' managePriorInstallation();\n' +
            '    }\n'    
        )                

    def __genPerformInstallationPageCallbackBody( self ):
        self.performInstallationPageCallbackBody = (
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        )

    def __genFinishedPageCallbackBody( self ):
        TAB  = _QtIfwScript.TAB
        EBLK = _QtIfwScript.END_BLOCK
        self.finishedPageCallbackBody = (                
            _QtIfwScript.ifInstalling( isMultiLine=True ) +
            TAB + QtIfwControlScript.enable( 
                    QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                    self.isRunProgInteractive ) +                              
            TAB + QtIfwControlScript.setVisible( 
                    QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                    self.isRunProgVisible ) +                  
            TAB + _QtIfwScript.ifCmdLineArg( 
                    _QtIfwScript.RUN_PROGRAM_CMD_ARG ) +               
                    _QtIfwScript.TAB + QtIfwControlScript.setCheckBox( 
                        QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                            _QtIfwScript.cmdLineSwitchArg(
                                _QtIfwScript.RUN_PROGRAM_CMD_ARG ) ) +
            EBLK +         
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.FINISH_BUTTON ) 
        )            
            
    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwControlScript.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, 
                         self.fileName) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwControlScript.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )     

# -----------------------------------------------------------------------------
class QtIfwPackageScript( _QtIfwScript ):
    
    __DIR_TMPLT  = "%s/packages/%s/meta"
    __PATH_TMPLT = __DIR_TMPLT + "/%s"

    __CONTROLER_CALLBACK_FUNC_TMPLT = (
"""
Controller.prototype.%s = function(){
    %s
}\n
""" )

    __COMPONENT_CALLBACK_FUNC_TMPLT = (
"""
Component.prototype.%s = function(){
    %s
}\n
""" )
    
    __COMPONENT_LOADED_HNDLR_NAME = "componentLoaded"
            
    __WIN_ADD_SHORTCUT_TMPLT = ( 
"""
        component.addOperation( "CreateShortcut",
            "[CMD]",
            "[SHORTCUT_PATH]",
            [ARGS]
            "workingDirectory=[WORKING_DIR]",
            "iconPath=[ICON_PATH]",
            "iconId=[ICON_ID]"        
        );    
""" )
    
    __WIN_SET_SHORTCUT_STYLE_TMPLT = ( 
"""
        addVbsOperation( component, true, // Elevated             
            setShortcutWindowStyleVbs( "[SHORTCUT_PATH]", [STYLE_CODE] ) ); 
""" )

    __MAC_ADD_SYMLINK_TMPLT = ( 
"""
        component.addOperation( "CreateLink",  
            "[SHORTCUT_PATH]",
            "[LINK_TO_PATH]"
        );    
""" )

    #Refer to: https://specifications.freedesktop.org/desktop-entry-spec/latest/
    __X11_ADD_DESKTOP_ENTRY_TMPLT = ( 
"""
        component.addOperation( "CreateDesktopEntry", 
            "[SHORTCUT_PATH]",
            "Type=Application\\n" 
          + "Terminal=[IS_TERMINAL]\\n" 
          + "Exec=[CMD]\\n"
          + "Path=[WORKING_DIR]\\n"
          + "Name=[LABEL]\\n" 
          + "Name[en_US]=[LABEL]\\n" 
          + "Version=[VERSION]\\n" 
          + "Icon=[PNG_PATH]\\n"                     
        );    
""" )
     
    __WIN_SHORTCUT_LOCATIONS = {
          DESKTOP_WIN_SHORTCUT          : QT_IFW_DESKTOP_DIR
        , STARTMENU_WIN_SHORTCUT        : QT_IFW_STARTMENU_DIR
        , THIS_USER_STARTUP_WIN_SHORTCUT: "@UserStartMenuProgramsPath@/Startup"
        , ALL_USERS_STARTUP_WIN_SHORTCUT: "@AllUsersMenuProgramsPath@/Startup"    
    }

    __MAC_SHORTCUT_LOCATIONS = {
          DESKTOP_MAC_SHORTCUT : QT_IFW_DESKTOP_DIR
        , APPS_MAC_SHORTCUT    : "%s/%s" % (QT_IFW_HOME_DIR,"Applications") 
    }

    # these may not be correct on all distros?
    __X11_SHORTCUT_LOCATIONS = {
          DESKTOP_X11_SHORTCUT : QT_IFW_DESKTOP_DIR
        , APPS_X11_SHORTCUT    : "/usr/share/applications" 
    }   # ~/.local/share/applications - current user location?

    @staticmethod
    def __winAddShortcut( location, exeName, command=None, args=[], 
                          windowStyle=None,
                          label=QT_IFW_PRODUCT_NAME,
                          exeDir=QT_IFW_TARGET_DIR,                          
                          wrkDir=QT_IFW_TARGET_DIR,                     
                          iconId=0 ):
        if command is None :
            command = "%s/%s" % (exeDir, normBinaryName( exeName ))
        if args and len(args) > 0 :            
            args = [ a.replace('"','\\"').replace( 
                     '@TargetDir@', '" + ' + _QtIfwScript.targetDir() + ' + "') 
                    for a in args ]
            args = '\"%s\",' % (" ".join(args),)     
        else : args=""           
        iconPath = "%s/%s" % (exeDir, normBinaryName( exeName ) )   
        locDir = QtIfwPackageScript.__WIN_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s.lnk" % (locDir, label)        
        s = QtIfwPackageScript.__WIN_ADD_SHORTCUT_TMPLT
        s = s.replace( "[CMD]", command )
        s = s.replace( "[ARGS]", args )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        s = s.replace( "[WORKING_DIR]", wrkDir )
        s = s.replace( "[ICON_PATH]", iconPath )
        s = s.replace( "[ICON_ID]", str(iconId) )
        if windowStyle:            
            style = QtIfwPackageScript.__WIN_SET_SHORTCUT_STYLE_TMPLT
            style = style.replace( "[SHORTCUT_PATH]", shortcutPath )
            style = style.replace( "[STYLE_CODE]", 
                                   str(SHORTCUT_WIN_MINIMIZED) )
            s += style
        return s 

    @staticmethod
    def __macAddShortcut( location, exeName, isGui, command=None, 
                          label=QT_IFW_PRODUCT_NAME, 
                          exeDir=QT_IFW_TARGET_DIR ):    
        if command : linkToPath = command 
        else :
            linkToPath = "%s/%s" % (exeDir, 
                                    normBinaryName( exeName, isGui=isGui ))
        locDir = QtIfwPackageScript.__MAC_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s" % (locDir, label)        
        s = QtIfwPackageScript.__MAC_ADD_SYMLINK_TMPLT
        s = s.replace( "[LINK_TO_PATH]", linkToPath )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        return s 

    @staticmethod
    def __linuxAddDesktopEntry( location, exeName, version,
                                command=None, args=[], 
                                label=QT_IFW_PRODUCT_NAME, 
                                exeDir=QT_IFW_TARGET_DIR,                          
                                wrkDir=QT_IFW_TARGET_DIR, 
                                pngPath=None,
                                isGui=True ):        
        if command is None :
            command = '"{0}/{1}"'.format( exeDir, normBinaryName( exeName ))
        if args and len(args) > 0 : command += " " + ' '.join(args)            
        command = command.replace('"','\\"').replace( 
            QT_IFW_ASKPASS_PLACEHOLDER, 
            '" + ' + _QtIfwScript.lookupValue( QT_IFW_ASKPASS_KEY ) + ' + "' )                        
        locDir = QtIfwPackageScript.__X11_SHORTCUT_LOCATIONS[location]             
        shortcutPath = "%s/%s.desktop" % (locDir, label.replace(" ","_"))        
        s = QtIfwPackageScript.__X11_ADD_DESKTOP_ENTRY_TMPLT
        s = s.replace( "[CMD]", command )
        s = s.replace( "[SHORTCUT_PATH]", shortcutPath )
        s = s.replace( "[LABEL]", label )
        s = s.replace( "[VERSION]", version )
        s = s.replace( "[PNG_PATH]", "" if pngPath is None else 
                       joinPathQtIfw( QT_IFW_TARGET_DIR, pngPath ) )
        s = s.replace( "[IS_TERMINAL]", "false" if isGui else "true" )
        s = s.replace( "[WORKING_DIR]", wrkDir )        
        return s 
                
    # QtIfwPackageScript                              
    def __init__( self, pkgName, 
                  shortcuts=[], externalOps=[], uiPages=[],                    
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.pkgName          = pkgName
        self.shortcuts        = shortcuts
        self.uiPages          = uiPages
        
        self.externalOps      = externalOps
        self.killOps          = []
        self.customOperations = None
                
        # Linux Only
        self.isAskPassProgRequired = False

        self.packageGlobals = None
        self.isAutoGlobals = True

        self.componentConstructorBody = None
        self.isAutoComponentConstructor = True

        self.componentLoadedCallbackBody = None
        self.isAutoComponentLoadedCallback = True

        self.componentEnteredCallbackBody = None
        self.isAutoComponentEnteredCallback = True
                                                              
        self.componentCreateOperationsBody = None
        self.isAutoComponentCreateOperations = True
                                                        
    def _generate( self ) :        
        self.script = ""
        
        if self.isAutoLib: _QtIfwScript._genLib( self )        
        if self.qtScriptLib: self.script += self.qtScriptLib        
        if self.isAutoGlobals: self.__genGlobals()
        if self.packageGlobals: self.script += self.packageGlobals

        installScripts = [ op.script for op in self.externalOps 
                if isinstance( op.script, ExecutableScript ) ]
        self.script += _QtIfwScript.embedResources( installScripts ) 
        
        if self.isAutoComponentConstructor:
            self.__genComponentConstructorBody()
        self.script += ( "function Component() {\n%s\n}\n" % 
                         (self.componentConstructorBody,) )

        if self.isAutoComponentLoadedCallback:
            self.__genComponentLoadedCallbackBody()
        self.script += ( QtIfwPackageScript.__COMPONENT_CALLBACK_FUNC_TMPLT % 
                         (QtIfwPackageScript.__COMPONENT_LOADED_HNDLR_NAME,
                          self.componentLoadedCallbackBody,) )                            

        if self.uiPages: self.__appendUiPageCallbacks()
        
        if self.isAutoComponentCreateOperations:
            self.__genComponentCreateOperationsBody()
        if self.componentCreateOperationsBody:
            self.script += (
                "\nComponent.prototype.createOperations = function() {\n" +
                "    component.createOperations(); // call to super class\n" +
                "%s\n}\n" % (self.componentCreateOperationsBody,) )

    def __genGlobals( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK
        self.packageGlobals=""                    
        if IS_WINDOWS :
            self.packageGlobals += (
                'function setShortcutWindowStyleVbs( shortcutPath, styleCode ) ' + SBLK +
                    TAB + 'var vbs  = "Set WshShell = CreateObject(\\"Wscript.shell\\")\\n"' + END +
                    TAB + '    vbs += "Set oShortcut = WshShell.CreateShortcut(\\"" + shortcutPath + "\\")\\n"' + END +
                    TAB + '    vbs += "oShortcut.WindowStyle = " + styleCode + "\\n"' + END +
                    TAB + '    vbs += "oShortcut.Save\\n"' + END +
                    TAB + 'return vbs' + END +
                EBLK + NEW + #TODO: Add UNDO operation
                'function addVbsOperation( component, isElevated, vbs ) ' + SBLK +
                    TAB + 'var vbsPath = getEnv("temp")' + 
                            '+ "/__qtIfwInstaller.vbs"' + END +
                    TAB + 'var cmd = ["cscript", vbsPath]' + END +
                    TAB + 'component.addOperation( "Delete", vbsPath )' + END +
                    TAB + 'component.addOperation( "AppendFile", vbsPath , vbs )' + END +
                    TAB + 'if( isElevated )' + NEW +
                    (2*TAB) + 'component.addElevatedOperation( "Execute", cmd )' + END +    
                    TAB + 'else' + NEW +
                    (2*TAB) + 'component.addOperation( "Execute", cmd )' + END +                
                    TAB + 'component.addOperation( "Delete", vbsPath )' + END +            
                EBLK + NEW 
                )
        else :    
            self.packageGlobals += (               
                'function getAskPassProg() ' + SBLK +
                    TAB + 'var pkg' + END +
                    TAB + 'var progPath' + END +
                    TAB + 'switch( systemInfo.productType )' + SBLK +
                    TAB + '////TODO: Insert Distro specific paths/package names' + NEW +
                    TAB + 'default: ' + NEW +
                    (2*TAB) + 'pkg="ssh-askpass-gnome"' + END +
                    (2*TAB) + 'progPath="/usr/bin/ssh-askpass"' + END +
                    EBLK +
                    TAB + _QtIfwScript.ifFileExists( 'progPath', isAutoQuote=False ) + NEW +
                    (2*TAB) + 'return progPath' + END +                    
                    TAB + 'if( !isPackageInstalled( pkg ) )' + SBLK +
                    (2*TAB) + 'if( !installPackage( pkg ) )' + NEW +                    
                        (3*TAB) + 'throw new Error("Could not install package: " + pkg )' + END +
                    EBLK +                                                                    
                    TAB + _QtIfwScript.ifFileExists( 'progPath', isAutoQuote=False ) + NEW +
                    (2*TAB) + 'return progPath' + END +
                    TAB + 'else' + NEW +
                    (2*TAB) + 'throw new Error("Ask Pass program path is not valid: " + progPath )' + END +
                EBLK + NEW                  
            )
            
    def __genComponentConstructorBody( self ):
        END = _QtIfwScript.END_LINE
        self.componentConstructorBody = (            
            ('component.loaded.connect(this, this.%s)' % 
              (QtIfwPackageScript.__COMPONENT_LOADED_HNDLR_NAME,) ) + END             
        )

    def __genComponentLoadedCallbackBody( self ):
        TAB = _QtIfwScript.TAB
        END = _QtIfwScript.END_LINE
        NEW = _QtIfwScript.NEW_LINE        
        ADD_CUSTOM_PAGE_TMPLT = ( 
            'installer.addWizardPage(component, "%s", QInstaller.%s)' )
        HIDE_DEFAULT_PAGE_TMPLT = (
            'installer.setDefaultPageVisible(QInstaller.%s, false)' )                
        self.componentLoadedCallbackBody = ""
        replacePage = None
        for p in self.uiPages:
            # Replace default pages            
            if p.name.startswith( QT_IFW_REPLACE_PAGE_PREFIX ):
                replacePage = p.name[ len(QT_IFW_REPLACE_PAGE_PREFIX): ]
                if replacePage in _DEFAULT_PAGES : 
                    self.componentLoadedCallbackBody += ( NEW + 
                        TAB + (ADD_CUSTOM_PAGE_TMPLT % ( p.name, replacePage )) + END +
                            TAB + (HIDE_DEFAULT_PAGE_TMPLT % (replacePage,)) + END 
                    )         
            else :
                # Insert custom pages
                self.componentLoadedCallbackBody += ( NEW + TAB + 
                    (ADD_CUSTOM_PAGE_TMPLT % ( p.name, p.pageOrder )) + END )         

            if p._incOnLoadBase:
                self.componentLoadedCallbackBody += (
                    QtIfwUiPage.BASE_ON_LOAD_TMPT % (p.name,) )
                              
            if p.onLoad:
                self.componentLoadedCallbackBody += p.onLoad

    def __appendUiPageCallbacks( self ):    
        if self.uiPages: 
            for p in self.uiPages:
                # support functions                 
                for funcName, funcBody in six.iteritems( p.supportFuncs ):
                    self.script += (  
                        QtIfwPackageScript.__COMPONENT_CALLBACK_FUNC_TMPLT 
                        % (funcName, funcBody) )

    def __genComponentCreateOperationsBody( self ):
        self.componentCreateOperationsBody = ""
        if IS_LINUX and self.isAskPassProgRequired:
            self.__addAskPassProgResolution()        
        self.__addShortcuts()
        self.__addKillOperations()
        self.__addExecuteOperations() 
        if self.customOperations:
            self.componentCreateOperationsBody += (
                "\n%s\n" % (self.customOperations,) )            
        if self.componentCreateOperationsBody == "" :
            self.componentCreateOperationsBody = None
        
    # TODO: Clean up this lazy mess!    
    def __addShortcuts( self ):
        if not self.shortcuts: return         
        for shortcut in self.shortcuts :   
            if IS_WINDOWS:
                winOps=""
                if shortcut.exeName and shortcut.isAppShortcut :
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            STARTMENU_WIN_SHORTCUT, shortcut.exeName,
                            command=shortcut.command,
                            args=shortcut.args,
                            exeDir=shortcut.exeDir,
                            wrkDir=shortcut.exeDir, # forced via command                            
                            windowStyle=shortcut.windowStyle,
                            label=shortcut.productName )              
                if shortcut.exeName and shortcut.isDesktopShortcut:
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            DESKTOP_WIN_SHORTCUT, shortcut.exeName,
                            command=shortcut.command,
                            args=shortcut.args,
                            exeDir=shortcut.exeDir,
                            wrkDir=shortcut.exeDir, # forced via command                            
                            windowStyle=shortcut.windowStyle,
                            label=shortcut.productName ) 
                if shortcut.exeName and shortcut.isUserStartUpShortcut:
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            THIS_USER_STARTUP_WIN_SHORTCUT, shortcut.exeName,
                            command=shortcut.command,
                            args=shortcut.args,
                            exeDir=shortcut.exeDir,
                            wrkDir=shortcut.exeDir, # forced via command                            
                            windowStyle=shortcut.windowStyle,
                            label=shortcut.productName ) 
                if shortcut.exeName and shortcut.isAllUsersStartUpShortcut :
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            ALL_USERS_STARTUP_WIN_SHORTCUT, shortcut.exeName,
                            command=shortcut.command,
                            args=shortcut.args,
                            exeDir=shortcut.exeDir,
                            wrkDir=shortcut.exeDir, # forced via command                            
                            windowStyle=shortcut.windowStyle,
                            label=shortcut.productName )                     
                if winOps!="" :    
                    #TODO: get rid of these platform checks in the installer!
                    # The installer will only work on the target platform 
                    # for which it is built, and we're generating that on the 
                    # fly, so there is no need to ever "pivot" again at runtime.
                    self.componentCreateOperationsBody += (             
                        '    if( systemInfo.kernelType === "winnt" ){\n' +
                        '%s\n    }' % (winOps,) )
            elif IS_MACOS:
                macOps = ""
                if shortcut.exeName and shortcut.isAppShortcut :
                    macOps += QtIfwPackageScript.__macAddShortcut(
                            APPS_MAC_SHORTCUT, 
                            shortcut.exeName, shortcut.isGui, 
                            command=shortcut.command,
                            exeDir=shortcut.exeDir,
                            label=shortcut.productName )              
                if shortcut.exeName and shortcut.isDesktopShortcut:
                    macOps += QtIfwPackageScript.__macAddShortcut(
                            DESKTOP_MAC_SHORTCUT, 
                            shortcut.exeName, shortcut.isGui, 
                            command=shortcut.command,
                            exeDir=shortcut.exeDir,
                            label=shortcut.productName )             
                if macOps!="" :    
                    self.componentCreateOperationsBody += (             
                        '    if( systemInfo.kernelType === "darwin" ){\n' +
                        '%s\n    }' % (macOps,) )                    
            elif IS_LINUX:
                x11Ops = ""
                if shortcut.exeName and shortcut.isAppShortcut :
                    x11Ops += QtIfwPackageScript.__linuxAddDesktopEntry(
                            APPS_X11_SHORTCUT, 
                            shortcut.exeName, shortcut.exeVersion,
                            command=shortcut.command,
                            args=shortcut.args,
                            label=shortcut.productName,
                            exeDir=shortcut.exeDir,
                            wrkDir=shortcut.exeDir, # forced via command
                            pngPath=shortcut.pngIconResPath,
                            isGui=shortcut.isGui )                
                if shortcut.exeName and shortcut.isDesktopShortcut:
                    x11Ops += QtIfwPackageScript.__linuxAddDesktopEntry(
                            DESKTOP_X11_SHORTCUT, 
                            shortcut.exeName, shortcut.exeVersion,
                            command=shortcut.command,
                            args=shortcut.args,
                            label=shortcut.productName,
                            exeDir=shortcut.exeDir,
                            wrkDir=shortcut.exeDir, # forced via command                            
                            pngPath=shortcut.pngIconResPath,
                            isGui=shortcut.isGui )                               
                if x11Ops!="" :    
                    self.componentCreateOperationsBody += (             
                        '    if( systemInfo.kernelType === "linux" ){\n' +
                        '%s\n    }' % (x11Ops,) )

    def __addKillOperations( self ):
        if not self.killOps: return
        killPath = _QtIfwScript._KILLALL_PATH
        killArgs = _QtIfwScript._KILLALL_ARGS 
        # success=0, process not running=128 in WINDOWS
        retCodes = [0,128] if IS_WINDOWS else [0] # TODO: not running code in mac/linux 127 perhaps?       
        def toExOp( installExe, uninstallExe, isElevated ):
            return QtIfwExternalOp( isElevated=isElevated, 
                exePath=killPath                   if installExe else None,       
                args=killArgs+[installExe]         if installExe else None,
                successRetCodes=retCodes           if installExe else None,                    
                uninstExePath=killPath             if uninstallExe else None, 
                uninstArgs=killArgs+[uninstallExe] if uninstallExe else None,                                         
                uninstRetCodes=retCodes            if uninstallExe else None )                         
        firstOps=( [ toExOp( op.processName, None, op.isElevated ) 
                     for op in self.killOps if op.onInstall ] )
        # on uninstall, the operations occur in reverse, thus the last are first
        lastOps=( [ toExOp( None, op.processName, op.isElevated ) 
                     for op in self.killOps if op.onUninstall ] )
        if self.externalOps is None: self.externalOps=[]                         
        self.externalOps = firstOps + self.externalOps + lastOps

    # TODO: Clean up this ugly mess!            
    def __addExecuteOperations( self ):
        if not self.externalOps: return        
        
        TAB  = _QtIfwScript.TAB
        END  = _QtIfwScript.END_LINE
        NEW  = _QtIfwScript.NEW_LINE
        SBLK = _QtIfwScript.START_BLOCK  # @UnusedVariable
        EBLK = _QtIfwScript.END_BLOCK
        
        # generate the install scripts here and now, to apply dynamic
        # changes (e.g. path selection) made during the user interactions
        installScripts = [ op.script for op in self.externalOps 
                if isinstance( op.script, ExecutableScript ) ]
        self.componentCreateOperationsBody += (
            NEW +
            _QtIfwScript.ifInstalling( isMultiLine=True ) +
                _QtIfwScript.genResources( installScripts ) +
            EBLK )
                    
        shellPath   = "cmd.exe" if IS_WINDOWS else "sh"
        shellSwitch = "/c"      if IS_WINDOWS else "-c"                    
                
        self.componentCreateOperationsBody += (            
"""
    var shellPath      = "%s";
    var shellSwitch    = "%s";
    var execPath       = "";
    var retCodes       = "";
    var undoPath       = "";
    var undoRetCodes   = "";                   
    var execArgs       = [];     
""") % ( shellPath, shellSwitch )
        if IS_WINDOWS:
            self.componentCreateOperationsBody += (            
"""
    var vbsInterpreter = "cscript";
    var vbsNologo      = "/Nologo";    
    var psInterpreter  = "powershell";
    var psNologo       = "-NoLogo";
    var psExecPolicy   = "-ExecutionPolicy";
    var psBypassPolicy = "Bypass";
    var psExecScript   = "-File";
""")
        if IS_WINDOWS:
            self.componentCreateOperationsBody += (            
"""
    var osaInterpreter = "osascript";
""")            
        self.componentCreateOperationsBody += NEW            
        for task in self.externalOps :   
            setArgs = ""
            exePath = ( joinPathQtIfw( QT_IFW_INSTALLER_TEMP_DIR, 
                                       task.script.fileName() )
                if task.script 
                else task.exePath if task.exePath 
                else None )   
            scriptType=( task.script.extension if task.script else None )   
            if exePath:
                if not IS_WINDOWS: exePath = exePath.replace(" ", "\\\\ ")
                setArgs += '%sexecPath = "%s"%s' % (TAB,exePath,END)
            if task.successRetCodes:
                setArgs +=( '%sretCodes = "{%s}"%s' % 
                    (TAB,",".join([str(c) for c in task.successRetCodes]),END) )
            
            uninstExePath = ( joinPathQtIfw( QT_IFW_MAINTENANCE_TEMP_DIR, 
                                             task.uninstScript.fileName() )
                if task.uninstScript 
                else task.uninstExePath if task.uninstExePath 
                else None )      
            if uninstExePath:
                if not IS_WINDOWS: uninstExePath = uninstExePath.replace(" ", "\\\\ ")
                setArgs += '%sundoPath = "%s"%s' % (TAB,uninstExePath,END)
            if task.uninstRetCodes:
                setArgs +=( '%sundoRetCodes = "{%s}"%s' % 
                    (TAB,",".join([str(c) for c in task.uninstRetCodes]),END) )
            if len(setArgs) > 0: self.componentCreateOperationsBody += setArgs
             
            args=[]                        
            if exePath :                 
                if task.successRetCodes: args+=["retCodes"]       
                if scriptType=="vbs":                     
                    if not IS_WINDOWS: 
                        raise Exception( 
                            "VBScript is not supported by this platform!" )                                            
                    args+=["vbsInterpreter", "vbsNologo"]
                elif scriptType=="ps1":
                    if not IS_WINDOWS: 
                        raise Exception( 
                            "PowerShell scripts are not INHERTENTLY "
                            "supported by this platform!" )                                             
                    args+=["psInterpreter", "psNologo", 
                           "psExecPolicy", "psBypassPolicy", "psExecScript"]
                elif scriptType=="scpt":            
                    if not IS_MACOS:
                        raise Exception( 
                            "AppleScript is not supported by this platform!" )                                                     
                    args+=["osaInterpreter"]                                
                else: args+=["shellPath", "shellSwitch"]
                if IS_WINDOWS:
                    args+=["execPath"]
                    if task.args: args+=['"%s"' % (a,) for a in task.args]                    
                else: 
                    if task.args: 
                        subArgs=[ a.replace(" ", "\\\\ ") for a in task.args]
                        #args+=['"\\\"" + execPath + " ' + 
                        #       ' '.join(subArgs) + '" + "\\\""' ]
                        args+=['execPath + " ' + ' '.join(subArgs) + '"' ]                        
                    else:
                        args+=['"\\\"" + execPath + "\\\""']
                    
            if uninstExePath :
                if not exePath : args+=["shellPath", "shellSwitch"] # dummy install action
                args+=['"UNDOEXECUTE"']                
                if task.uninstRetCodes: args+=["undoRetCodes"]
                if scriptType=="vbs": 
                    args+=["vbsInterpreter", "vbsNologo"]
                elif scriptType=="ps1":
                    args+=["psInterpreter", "psNologo", 
                           "psExecPolicy", "psBypassPolicy", "psExecScript"]
                elif scriptType=="scpt":            
                    args+=["osaInterpreter"]                                              
                else: args+=["shellPath", "shellSwitch"]
                if IS_WINDOWS:
                    args+=["undoPath"]
                    if task.uninstArgs: 
                        args+=['"%s"' % (a,) for a in task.uninstArgs]                    
                else: 
                    if task.uninstArgs: 
                        subArgs=[ a.replace(" ", "\\\\ ")  
                                  for a in task.uninstArgs ]
                        #args+=['"\\\"" + undoPath + " ' + 
                        #       ' '.join(subArgs) + '" + "\\\""' ]
                        args+=['undoPath + " ' + ' '.join(subArgs) + '"' ]      
                    else:
                        args+=['"\\\"" + undoPath + "\\\""']
                                    
            self.componentCreateOperationsBody +=( "%sexecArgs = [%s]%s" % 
                (TAB,",".join(args),END) )
            
            # TODO: add workingdirectory= and errormessage=
            self.componentCreateOperationsBody +=(
                '%scomponent.add%sOperation( "Execute", execArgs )%s%s'                       
                ) % (TAB,"Elevated" if task.isElevated else "",END,NEW)
                                                                
    def __addAskPassProgResolution( self ):
        TAB = _QtIfwScript.TAB 
        END = _QtIfwScript.END_LINE
        self.componentCreateOperationsBody += ( 
            TAB + _QtIfwScript.setValue( 
                '"' + QT_IFW_ASKPASS_KEY + '"', 
                'getAskPassProg()', isAutoQuote=False ) + END +
            TAB + 'writeFile( "' + QT_IFW_ASKPASS_TEMP_FILE_PATH + '", ' +
            _QtIfwScript.lookupValue( QT_IFW_ASKPASS_KEY ) + ')' + END
        )

    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageScript.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName, 
                         self.fileName) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageScript.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) )     
    
# -----------------------------------------------------------------------------    
class QtIfwShortcut:
    def __init__( self, productName=QT_IFW_PRODUCT_NAME, 
                  command=None, args=[], 
                  exeDir=QT_IFW_TARGET_DIR, exeName=None, 
                  exeVersion="0.0.0.0",
                  isGui=True, pngIconResPath=None ) :
        self.productName    = productName
        self.command        = command   
        self.args           = args
        self.exeDir         = exeDir       
        self.exeName        = exeName           
        self.isGui          = isGui
        
        # Windows only
        self.windowStyle    = None        
        self.isUserStartUpShortcut = False      # TODO: make cross platform
        self.isAllUsersStartUpShortcut = False  # TODO: make cross platform ?

        # Linux only
        self.exeVersion     = exeVersion
        self.pngIconResPath = pngIconResPath        
 
        # Cross platform
        self.isAppShortcut     = True
        self.isDesktopShortcut = False
      
# -----------------------------------------------------------------------------
class QtIfwExternalOp:

    ON_INSTALL, ON_UNINSTALL, ON_BOTH, AUTO_UNDO = range(4) 

    __AUTO_SCRIPT_COUNT=0

    # TODO: Expand upon registry functions
    
    # TODO: Deal with 64 bit vs 32 bit registry contexts
    # Allow the use of either literal paths or implicit wow64 resolution
    # Some thoughts:     
    # https://stackoverflow.com/questions/630382/how-to-access-the-64-bit-registry-from-a-32-bit-powershell-instance
    
    @staticmethod
    def CreateRegistryEntry( event, key, valueName=None, value="", valueType="String" ):
        if not IS_WINDOWS: util._onPlatformErr()
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.CreateRegistryEntryScript( key, valueName, value, valueType ), 
            uninstScript=QtIfwExternalOp.RemoveRegistryEntryScript( key, valueName ), 
            isElevated=True )
    
    @staticmethod
    def RemoveRegistryEntry( event, key, valueName=None ):
        if not IS_WINDOWS: util._onPlatformErr()    
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.RemoveRegistryEntryScript( key, valueName ), 
            canAutoUndo=False, isElevated=True )
    
    @staticmethod
    def CreateStartupEntry( pkg=None, exePath=None, displayName=None, 
                            isAllUsers=False ):
        if pkg :
            if not displayName: displayName = pkg.pkgXml.DisplayName
            if not exePath:  
                try:    exeName = pkg.exeWrapper.wrapperScript.fileName()
                except: exeName = normBinaryName( pkg.exeName, pkg.isGui )
                exePath = joinPath( 
                    ( joinPath( QT_IFW_TARGET_DIR, pkg.subDirName ) 
                      if pkg.subDirName else QT_IFW_TARGET_DIR ), exeName )
        if exePath is None or displayName is None:
            raise Exception( "Missing required arguments" )    
        if IS_WINDOWS:
            # TODO: IS THIS SUPPORTED IN LEGACY WINDOWS VERSIONS?
            #     If not, just fall back to shortcuts in startup folders... 
            # See: https://devblogs.microsoft.com/powershell/how-to-access-or-modify-startup-items-in-the-window-registry/
            return QtIfwExternalOp.CreateRegistryEntry( QtIfwExternalOp.AUTO_UNDO, 
                key = "%s:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" % (
                    "HKLM" if isAllUsers else "HKCU" ),
                valueName=displayName, value=exePath )
        elif IS_LINUX: 
            # TODO: Fill in
            util._onPlatformErr()
        elif IS_MACOS: 
            # TODO: Fill in
            util._onPlatformErr()

    @staticmethod
    def __genScriptOp( event, script, uninstScript, canAutoUndo=True, isElevated=False ):    
        if   event==QtIfwExternalOp.ON_INSTALL:
            onInstall   = script
            onUninstall = None
        elif event==QtIfwExternalOp.ON_UNINSTALL:
            onInstall   = None 
            onUninstall = script if uninstScript is None else uninstScript
        elif event==QtIfwExternalOp.ON_BOTH:
            onInstall   = script 
            onUninstall = script        
        elif event==QtIfwExternalOp.AUTO_UNDO:
            if not canAutoUndo: 
                raise Exception( 
                    "Installer operation cannot be automatically undone." )
            onInstall   = script 
            onUninstall = uninstScript                  
        return QtIfwExternalOp( script=onInstall, uninstScript=onUninstall,
                                isElevated=isElevated ) 
    
    # See
    # https://blog.netwrix.com/2018/09/11/how-to-get-edit-create-and-delete-registry-keys-with-powershell/
    # https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-itemproperty?view=powershell-7
    @staticmethod
    def CreateRegistryEntryScript( key, valueName=None, value="", valueType="String" ):
        valueName = "-Name '%s' " % (valueName,) if valueName else ""
        if value is None: value=""
        QtIfwExternalOp.__AUTO_SCRIPT_COUNT+=1
        return ExecutableScript( 
            "createRegEntry_%d" % (QtIfwExternalOp.__AUTO_SCRIPT_COUNT,), 
            extension="ps1", script=(
            "New-ItemProperty -Path '%s' %s-Value '%s' -PropertyType '%s'" 
            % (key, valueName, value, valueType) ) )
    
    @staticmethod
    def RemoveRegistryEntryScript( key, valueName=None ):
        valueName = "-Name '%s' " % (valueName,) if valueName else ""
        QtIfwExternalOp.__AUTO_SCRIPT_COUNT+=1
        return ExecutableScript( "removeRegEntry_%d" % (
            QtIfwExternalOp.__AUTO_SCRIPT_COUNT,),
            extension="ps1", script=(
            "Remove-ItemProperty -Path '%s' %s" % (key, valueName) ) )
 
    # QtIfwExternalOp
    def __init__( self, 
              script=None,       exePath=None,       args=[], successRetCodes=[0],  
        uninstScript=None, uninstExePath=None, uninstArgs=[],  uninstRetCodes=[0],
        isElevated=False, workingDir=QT_IFW_TARGET_DIR, onErrorMessage=None ):
        
        self.script          = script #ExecutableScript        
        self.exePath         = exePath
        self.args            = args
        self.successRetCodes = successRetCodes

        self.uninstScript    = uninstScript #ExecutableScript
        self.uninstExePath   = uninstExePath
        self.uninstArgs      = uninstArgs
        self.uninstRetCodes  = uninstRetCodes
        
        self.isElevated      = isElevated 
        self.workingDir      = workingDir
                
        self.onErrorMessage  = onErrorMessage # TODO: TEST!

# -----------------------------------------------------------------------------
class QtIfwKillOp:
    def __init__( self, processName, onInstall=True, onUninstall=True ):        
        self.processName = ( normBinaryName( processName.exeName ) 
            if isinstance( processName, QtIfwPackage ) else processName )         
        self.onInstall   = onInstall
        self.onUninstall = onUninstall
        self.isElevated  = True  
            
# -----------------------------------------------------------------------------
class QtIfwUiPage():

    __FILE_EXTENSION  = "ui"
    __UI_RES_DIR_NAME = "qtifw_ui"
    

    BASE_ON_LOAD_TMPT = (    
"""
    var page = gui.pageWidgetByObjectName("Dynamic%s");
    switch( systemInfo.kernelType ){
    case "darwin": // macOS
        page.minimumSize.width=300;
        break;
    case "linux": 
        page.minimumSize.width=480;
        break;
    default: // "windows"
        // This is the hard coded width of "standard" QtIfw .ui's
        page.minimumSize.width=491;   
    }    
""")
    
    @staticmethod
    def __toFileName( name ): 
        return joinExt( name, QtIfwUiPage.__FILE_EXTENSION ).lower()  
    
    @staticmethod
    def _pageResPath( name ):    
        return util._toLibResPath( joinPath( 
                QtIfwUiPage.__UI_RES_DIR_NAME, 
                QtIfwUiPage.__toFileName( name ) ) )
    
    # QtIfwUiPage    
    def __init__( self, name, pageOrder=None, 
                  sourcePath=None, content=None,
                  onLoad=None, onEnter=None ) :
        self.name           = name
        self.pageOrder      = pageOrder if pageOrder in _DEFAULT_PAGES else None        
        self._incOnLoadBase = True
        self.onLoad         = onLoad
        self.onEnter        = onEnter
        self.supportFuncs   = {} 
        self.replacements   = {}
        self.onAutoPilotClickNext = True        
        if sourcePath:
            with open( sourcePath, 'r' ) as f: self.content = f.read()
        else: self.content = content  
               
    def fileName( self ): return QtIfwUiPage.__toFileName( self.name )  

    # resolve static substitutions
    def resolve( self, qtIfwConfig ):
        self.replacements.update({ 
             QT_IFW_TITLE           : qtIfwConfig.configXml.Title 
        ,    QT_IFW_PRODUCT_NAME    : qtIfwConfig.configXml.Name 
        ,    QT_IFW_PRODUCT_VERSION : qtIfwConfig.configXml.Version 
        ,    QT_IFW_PUBLISHER       : qtIfwConfig.configXml.Publisher 
        })
        
    def write( self, dirPath ):
        if self.content is None : return
        if not isDir( dirPath ): makeDir( dirPath )
        filePath = joinPath( dirPath, self.fileName() )
        content = self.__resolveContent()
        print( "Adding installer page definition: %s\n\n%s\n" % ( 
                filePath, content ) )                               
        with open( filePath, 'w' ) as f: f.write( content ) 

    def __resolveContent( self ):
        self.replacements[ _PAGE_NAME_PLACHOLDER ] = self.name
        ret = self.content
        for placeholder, value in six.iteritems( self.replacements ):
            ret = ret.replace( placeholder, value )
        return ret    

# -----------------------------------------------------------------------------    
class QtIfwSimpleTextPage( QtIfwUiPage ):
    
    __SRC  = QtIfwUiPage._pageResPath( "simpletext" )
    __TITLE_PLACEHOLDER = "[TITLE]"
    __TEXT_PLACEHOLDER = "[TEXT]"

    def __init__( self, name, pageOrder=None, title="", text="", 
                  onLoad=None, onEnter=None ) :
        QtIfwUiPage.__init__( self, name, pageOrder=pageOrder, 
                              onLoad=onLoad, onEnter=onEnter, 
                              sourcePath=QtIfwSimpleTextPage.__SRC  )
        self.replacements.update({ 
            QtIfwSimpleTextPage.__TITLE_PLACEHOLDER : title,
            QtIfwSimpleTextPage.__TEXT_PLACEHOLDER : text 
        })
                    
# -----------------------------------------------------------------------------    
class QtIfwTargetDirPage( QtIfwUiPage ):
    
    NAME = QT_IFW_REPLACE_PAGE_PREFIX + QT_IFW_TARGET_DIR_PAGE
    __SRC  = QtIfwUiPage._pageResPath( QT_IFW_TARGET_DIR_PAGE )

    def __init__( self ):
            
        ON_TARGET_CHANGED_NAME        = "targetDirectoryChanged"
        ON_TARGET_BROWSE_CLICKED_NAME = "targetChooserClicked"
    
        ON_LOAD = (    
"""
    // patch seems to be needed due to use of RichText?
    switch( systemInfo.kernelType ){
    case "darwin": // macOS
        page.warning.minimumSize.width=300;
        break;
    case "linux": 
        page.warning.minimumSize.width=480;
        break;
    }    
    page.targetDirectory.setText(
        Dir.toNativeSeparator(installer.value("TargetDir")));
    page.targetDirectory.textChanged.connect(this, this.%s);    
    page.targetChooser.released.connect(this, this.%s);
""") % ( ON_TARGET_CHANGED_NAME, ON_TARGET_BROWSE_CLICKED_NAME )
    
        ON_TARGET_CHANGED = (
"""
    var page = gui.pageWidgetByObjectName("Dynamic%s");
    var dir = page.targetDirectory.text;
    dir = Dir.toNativeSeparator(dir);
    page.warning.setText( !installer.fileExists(dir) ? "" :
        "<p style=\\"color: red\\">" +
            "WARNING: The path specified already exists. " +
            "All prior content will be erased!" + 
        "</p>" );        
    installer.setValue("TargetDir", dir);
""") % ( QtIfwTargetDirPage.NAME, )

        ON_TARGET_BROWSE_CLICKED = (
"""
    var page = gui.pageWidgetByObjectName("Dynamic%s");
    page.targetDirectory.setText( Dir.toNativeSeparator(
        QFileDialog.getExistingDirectory("", page.targetDirectory.text) ) );
""") % ( QtIfwTargetDirPage.NAME, )
        
        QtIfwUiPage.__init__( self, QtIfwTargetDirPage.NAME,
            sourcePath=QtIfwTargetDirPage.__SRC, onLoad=ON_LOAD )
        
        self.supportFuncs.update({ 
              ON_TARGET_CHANGED_NAME: ON_TARGET_CHANGED
            , ON_TARGET_BROWSE_CLICKED_NAME: ON_TARGET_BROWSE_CLICKED
        })
            
# -----------------------------------------------------------------------------    
class QtIfwExeWrapper:
    
    if IS_WINDOWS :
        __WIN_PS                    = "powershell"
        __WIN_PS_START_TMPLT        = "Start-Process -FilePath '%s'"
        __WIN_PS_START_ADMIN_SWITCH = " -Verb RunAs"
        __WIN_PS_START_PWD_TMPLT    = " -WorkingDirectory '%s'"                       
        __WIN_PS_START_ARGS_SWITCH  = " -ArgumentList "
        __WIN_PS_SET_ENV_VAR_TMPLT  = "$env:%s='%s';"

        #__WIN_CMD                   = "cmd"
        #__WIN_CMD_START_TMPLT       = '/c START "%s"'
        #__WIN_CMD_START_PWD_TMPLT   = ' /D "%s"'                           
        
        __SCRIPT_HDR = (
"""
@echo off
set appname=%~n0
set dirname=%~dp0
""")
        __TARGET_DIR = '%dirname%'
         
        __EXECUTE_PROG_TMPLT = (
"""
{0}"%dirname%\%appname%" {2}
""")        
        __GUI_EXECUTE_PROG_TMPLT = (
"""                
if "%{DEBUG_VAR}%"=="{DEBUG_VAL}" ( 
    {0}"%dirname%\%appname%" {2} 
) else ( 
    {0}start "" "%dirname%\%appname%" {2} 
)
""") 
        __GUI_EXECUTE_PROG_TMPLT = __GUI_EXECUTE_PROG_TMPLT.replace( 
            "{DEBUG_VAR}", DEBUG_ENV_VAR_NAME )
        __GUI_EXECUTE_PROG_TMPLT = __GUI_EXECUTE_PROG_TMPLT.replace( 
            "{DEBUG_VAL}", DEBUG_ENV_VAR_VALUE )

        __SET_ENV_VAR_TMPLT = 'set %s=%s'
        
    else:
        __SHELL            = "sh"
        __SHELL_CMD_SWITCH = "-c"
        __SHELL_CMD_TMPLT  = __SHELL_CMD_SWITCH + " '%s'"

        __CMD_DELIM = ";"

        __SUDO = 'sudo -E ' # -E preserves environment within the new context     
          
        __SCRIPT_HDR = (
"""
appname=`basename "$0" | sed s,\.sh$,,`
dirname=`dirname "$0"`
tmp="${dirname#?}"
if [ "${dirname%$tmp}" != "/" ]; then dirname="$PWD/$dirname"; fi
""") 
        __TARGET_DIR = '$dirname'            
        __SET_ENV_VAR_TMPLT = 'export %s="%s"'
        __EXECUTE_PROG_TMPLT = (
"""
{0}{1}"$dirname/$appname" {2} 
""")
                      
        if IS_LINUX : 
            __GUI_SUDO = ( 'export ' + util._ASKPASS_ENV_VAR + '="' +
                QT_IFW_ASKPASS_PLACEHOLDER + '"; sudo ' ) 
            __TMP_GUI_SUDO = ( 'export ' + util._ASKPASS_ENV_VAR + '=' +
                '$(cat "' + QT_IFW_ASKPASS_TEMP_FILE_PATH + '"); ' +
                'sudo ' )
                        
        elif IS_MACOS :
            __GUI_SCRIPT_HDR = (
"""
appname=_`basename "$0"`
dirname=`dirname "$0"`
tmp="${dirname#?}"
if [ "${dirname%$tmp}" != "/" ]; then dirname="$PWD/$dirname"; fi
""") 
            __GUI_TARGET_DIR = '$dirname/../../..'

            # must run in detached process to allow terminal app to close
            __GUI_EXECUTE_PROG_TMPLT = (
"""                
if [ "${%s}" == "%s" ]; then 
    {0}{1}"$dirname/$appname" {2} 
else 
    {0}{1}"$dirname/$appname" {2}&
fi 
""") % (DEBUG_ENV_VAR_NAME, DEBUG_ENV_VAR_VALUE) 
            # osascript must additionally be detached from stdout/err streams
            __GUI_SUDO_EXE_TMPLT = (
"""
{0}cd .
if [ "${%s}" == "%s" ]; then
    shscript="\\\\\\"$dirname/$appname\\\\\\" {2}" 
else
    shscript="\\\\\\"$dirname/$appname\\\\\\" {2} >/dev/null 2>&1 &"
fi   
osascript -e "do shell script \\\"${shscript}\\\" with administrator privileges"
""") % (DEBUG_ENV_VAR_NAME, DEBUG_ENV_VAR_VALUE)
 
    __PWD_PREFIX_CMD_TMPLT = 'cd "%s" && ' # cross platform!
    
    # QtIfwExeWrapper
    def __init__( self, exeName, isGui=False, 
                  wrapperScript=None,
                  exeDir=QT_IFW_TARGET_DIR, 
                  workingDir=None, # None=don't impose here, use QT_IFW_TARGET_DIR via other means
                  args=None, envVars=None, isElevated=False ) :
               
        self.exeName       = exeName
        self.isGui         = isGui
        
        self.wrapperScript = wrapperScript

        self.exeDir        = exeDir
        self.workingDir    = workingDir

        self.args          = args      
        self.envVars       = envVars 
        
        self.isElevated    = isElevated
        
        self._winPsStartArgs  = None
        #self._winCmdStartArgs = None
        
        self.refresh()
            
    def refresh( self ):
                
        self._runProgram       = None
        self._runProgArgs      = None
        self._shortcutCmd      = None
        self._shortcutArgs     = None
        self._shortcutWinStyle = None
        
        # wrapperScript string to ExecutableScript
        if isinstance( self.wrapperScript, string_types ):
            self.wrapperScript = ExecutableScript( 
                rootFileName( self.exeName ), script=self.wrapperScript )
        
        isScript = isinstance( self.wrapperScript, ExecutableScript )
        
        # In various contexts, some features, or combos there of, can only 
        # be provided by forcing the use of a wrapper script
        isAutoScript = False
        if not isScript:
            if IS_WINDOWS :
                # we must use a script to set envVars when auto elevating,
                # else they are lost when the non-admin to admin context is changed 
                isScript = isAutoScript = self.isElevated and self.envVars
            elif IS_LINUX :
                isScript = isAutoScript = (not self.isGui and
                    (self.isElevated or self.workingDir or
                     self.args or self.envVars) )
            elif IS_MACOS : 
                # there are no "light weight" shortcut wrappers employed on macOS, 
                # so force the use of a script to apply built-in wrapper features
                isScript = isAutoScript = (self.isElevated or self.workingDir
                                           or self.args or self.envVars)                
            if isAutoScript :
                self.wrapperScript = ExecutableScript( 
                    rootFileName( self.exeName ) )    

        # On macOS, strip the extension on a wrapper inside a .app 
        # (it will "masquerade" as the original exe)                  
        if IS_MACOS and isScript and self.isGui:                
            self.wrapperScript.extension=None
        
        # Set the "primary" launch commands to be executed. 
        # If applicable, point the run target at the script rather than the binary.        
        if isScript:
            self._runProgram = joinPathQtIfw( self.exeDir, 
                                              self.wrapperScript.fileName() )            
            self._shortcutCmd = self._runProgram
            if IS_MACOS and self.isGui :        
                appPath = normBinaryName( self._runProgram, 
                                          isPathPreserved=True, isGui=True )   
                self._shortcutCmd = appPath
                self._runProgram = util._macAppBinaryPath( appPath )
        else:
            self._runProgram = joinPathQtIfw( self.exeDir, self.exeName )            
            self._shortcutCmd = self._runProgram
            
        if self.args : 
            self._runProgArgs = self.args
            self._shortcutArgs = [ 
                ('"%s"' % (a,)) if " " in a else a for a in self.args ]

        targetPath =( self._runProgram if self._runProgram else
            joinPathQtIfw( self.exeDir, normBinaryName(self.exeName) ) )            
                  
        if IS_WINDOWS :
            if isAutoScript :
                script=QtIfwExeWrapper.__SCRIPT_HDR                
                if isinstance( self.envVars, dict ):
                    for k,v in six.iteritems( self.envVars ):
                        script += ( '\n' + 
                            (QtIfwExeWrapper.__SET_ENV_VAR_TMPLT % (k, v)) )
                    script += '\n'     
                launch =( QtIfwExeWrapper.__GUI_EXECUTE_PROG_TMPLT
                          if self.isGui 
                          else QtIfwExeWrapper.__EXECUTE_PROG_TMPLT )
                cdCmd = ""
                if self.workingDir :
                    if self.workingDir==QT_IFW_TARGET_DIR :
                        pwdPath = QtIfwExeWrapper.__TARGET_DIR  
                    else : pwdPath = self.workingDir  
                    cdCmd += QtIfwExeWrapper.__PWD_PREFIX_CMD_TMPLT % (pwdPath,)      
                args=""
                if self._runProgArgs :             
                    quot = '"'        
                    args += " ".join([ 
                        ('%s%s%s' % (quot,a,quot) if ' ' in a else '%s' % (a,))
                        for a in self._runProgArgs ])     
                    self._runProgArgs = None # don't need now, as they're being baked in                                                                       
                launch = launch.replace( "{0}", cdCmd )                
                launch = launch.replace( "{2}", args )
                script += launch                 
                self.wrapperScript.script=script
                                            
            if( self.isElevated or self.workingDir or self.envVars 
                or self._winPsStartArgs ):                                                
                self._runProgram  = QtIfwExeWrapper.__WIN_PS
                self._shortcutCmd = QtIfwExeWrapper.__WIN_PS
                psCmd = ""
                if not isAutoScript :
                    if isinstance( self.envVars, dict ):
                        for k,v in six.iteritems( self.envVars ):
                            psCmd += ( QtIfwExeWrapper.__WIN_PS_SET_ENV_VAR_TMPLT 
                                       % (k, v) )
                psCmd += QtIfwExeWrapper.__WIN_PS_START_TMPLT % (targetPath,)
                if self.isElevated: 
                    psCmd += QtIfwExeWrapper.__WIN_PS_START_ADMIN_SWITCH
                if not isAutoScript:    
                    if self.workingDir :
                        psCmd += QtIfwExeWrapper.__WIN_PS_START_PWD_TMPLT % (
                            self.workingDir,)
                    if self._runProgArgs :    
                        psCmd += QtIfwExeWrapper.__WIN_PS_START_ARGS_SWITCH
                        # don't mess with this multi-level escape hell!
                        psCmd += ",".join(
                            [ '\'\"%s\"\'' % (a,) for a in self._runProgArgs ])
                # Custom additions to Start-Process 
                if self._winPsStartArgs: 
                    psCmd += (" " + " ".join(self._winPsStartArgs)) 
                self._runProgArgs=[ psCmd ]                                                                        
                # the psCmd is one long argument for PS
                self._shortcutArgs = [ psCmd ] 
                self._shortcutWinStyle = SHORTCUT_WIN_MINIMIZED
            """
            # CMD Start    
            # START "title" [/D path] [options] "command" [parameters]
            elif self.workingDir or self._winCmdStartArgs:
                self._runProgram  = QtIfwExeWrapper.__WIN_CMD
                self._shortcutCmd = QtIfwExeWrapper.__WIN_CMD
                title = normBinaryName(self.exeName)
                cmd = QtIfwExeWrapper.__WIN_CMD_START_TMPLT % (title,)
                if self.workingDir :
                    cmd += QtIfwExeWrapper.__WIN_CMD_START_PWD_TMPLT % (
                        self.workingDir,)
                # Custom additions to Start                     
                if self._winCmdStartArgs: 
                    cmd += (" " + " ".join(self._winCmdStartArgs))
                cmd +=  ' "%s"' % (targetPath,)
                if self._shortcutArgs : # use in both context, these are already wrapped in quotes 
                    cmd += (" " + " ".join(self._shortcutArgs))
                self._runProgArgs = [ cmd ]
                self._shortcutArgs = [ cmd ]
            """    
        elif IS_LINUX :
            if isAutoScript:
                script=QtIfwExeWrapper.__SCRIPT_HDR                 
                if isinstance( self.envVars, dict ):
                    for k,v in six.iteritems( self.envVars ):
                        script += ( '\n' + 
                            (QtIfwExeWrapper.__SET_ENV_VAR_TMPLT % (k, v)) )
                    script += '\n'     
                launch = QtIfwExeWrapper.__EXECUTE_PROG_TMPLT    
                sudo =( QtIfwExeWrapper.__SUDO 
                        if self.isElevated and not self.isGui else "") 
                cdCmd = ""
                if self.workingDir :
                    if self.workingDir==QT_IFW_TARGET_DIR :
                        pwdPath = QtIfwExeWrapper.__TARGET_DIR  
                    else : pwdPath = self.workingDir  
                    cdCmd += QtIfwExeWrapper.__PWD_PREFIX_CMD_TMPLT % (pwdPath,)      
                args=""
                if self._runProgArgs :             
                    quot = '"'        
                    args += " ".join([ 
                        ('%s%s%s' % (quot,a,quot) if ' ' in a else '%s' % (a,))
                        for a in self._runProgArgs ])     
                    self._runProgArgs = None # don't need now, as they're being baked in 
                launch = launch.replace( "{0}", cdCmd )
                launch = launch.replace( "{1}", sudo )
                launch = launch.replace( "{2}", args )
                script += launch                 
                self.wrapperScript.script=script                   
            
            elif self.isElevated or self.workingDir or self.envVars or self.args:                
                self._runProgram  = QtIfwExeWrapper.__SHELL
                self._shortcutCmd = QtIfwExeWrapper.__SHELL      
                setVarsCmd = "" 
                if isinstance( self.envVars, dict ):
                    for k,v in six.iteritems( self.envVars ):
                        setVarsCmd += "%s%s" % (
                            (QtIfwExeWrapper.__SET_ENV_VAR_TMPLT % (k, v)),
                            QtIfwExeWrapper.__CMD_DELIM )                                                   
                cdCmd = ""
                if self.workingDir :
                    cdCmd += QtIfwExeWrapper.__PWD_PREFIX_CMD_TMPLT % (
                        self.workingDir,)                                
                runLaunch = ('"%s"' % (targetPath,))
                shortLaunch = runLaunch            
                if self.isElevated:
                    if self.isGui :                        
                        runLaunch = QtIfwExeWrapper.__TMP_GUI_SUDO + runLaunch
                        shortLaunch = QtIfwExeWrapper.__GUI_SUDO + runLaunch 
                    else:
                        runLaunch = QtIfwExeWrapper.__SUDO + runLaunch
                        shortLaunch = runLaunch                            
                args=""
                if self._runProgArgs :                        
                    args += " ".join([ 
                        ('"%s"' % (a,) if ' ' in a else '%s' % (a,))
                        for a in self._runProgArgs ])                
                cmdTmplt = "%s %s %s %s"
                runCmd   =( 
                    cmdTmplt % (setVarsCmd, cdCmd, runLaunch,   args) ).strip()
                shortCmd =( 
                    cmdTmplt % (setVarsCmd, cdCmd, shortLaunch, args) ).strip()
                self._runProgArgs = [ 
                    QtIfwExeWrapper.__SHELL_CMD_SWITCH, runCmd ]
                self._shortcutArgs = [ 
                    QtIfwExeWrapper.__SHELL_CMD_TMPLT % (shortCmd,) ]
        elif IS_MACOS:
            if isAutoScript:
                script=( QtIfwExeWrapper.__GUI_SCRIPT_HDR if self.isGui 
                         else QtIfwExeWrapper.__SCRIPT_HDR )                
                if isinstance( self.envVars, dict ):
                    for k,v in six.iteritems( self.envVars ):
                        script += ( '\n' + 
                            (QtIfwExeWrapper.__SET_ENV_VAR_TMPLT % (k, v)) )
                    script += '\n'     
                if self.isGui :    
                    launch =( QtIfwExeWrapper.__GUI_SUDO_EXE_TMPLT 
                              if self.isElevated 
                              else QtIfwExeWrapper.__GUI_EXECUTE_PROG_TMPLT )
                else : launch = QtIfwExeWrapper.__EXECUTE_PROG_TMPLT    
                sudo =( QtIfwExeWrapper.__SUDO 
                        if self.isElevated and not self.isGui else "") 
                cdCmd = ""
                if self.workingDir :
                    if self.workingDir==QT_IFW_TARGET_DIR :
                        pwdPath =( QtIfwExeWrapper.__GUI_TARGET_DIR if self.isGui
                                   else QtIfwExeWrapper.__TARGET_DIR ) 
                    else : pwdPath = self.workingDir  
                    cdCmd += QtIfwExeWrapper.__PWD_PREFIX_CMD_TMPLT % (pwdPath,)      
                args=""
                if self._runProgArgs :             
                    quot =( '\\\\\\"' 
                            if launch==QtIfwExeWrapper.__GUI_SUDO_EXE_TMPLT 
                            else '"' )       
                    args += " ".join([ 
                        ('%s%s%s' % (quot,a,quot) if ' ' in a else '%s' % (a,))
                        for a in self._runProgArgs ])     
                    self._runProgArgs = None # don't need now, as they're being baked in               
                launch = launch.replace( "{0}", cdCmd )
                launch = launch.replace( "{1}", sudo )
                launch = launch.replace( "{2}", args )
                script += launch                 
                self.wrapperScript.script=script                   
            if util._isMacApp( self.exeName ):
                self._args = [self._runProgram]
                self._runProgram = util._LAUNCH_MACOS_APP_CMD

# -----------------------------------------------------------------------------    
def installQtIfw( installerPath=None, version=None, targetPath=None ):    
    if installerPath is None :        
        if   IS_WINDOWS : fileName = QT_IFW_DOWNLOAD_FILE_WINDOWS
        elif IS_LINUX   : fileName = QT_IFW_DOWNLOAD_FILE_LINUX
        elif IS_MACOS   : fileName = QT_IFW_DOWNLOAD_FILE_MACOS
        if version is None: version = QT_IFW_DEFAULT_VERSION 
        installerPath = ( __QT_IFW_DOWNLOAD_URL_TMPLT % 
            (QT_IFW_DOWNLOAD_URL_BASE, version, fileName) )
    isLocal, path = util._isLocalPath( installerPath )    
    installerPath = path if isLocal else download( installerPath )
    if IS_LINUX and not isLocal: util.chmod( installerPath, 0o755 )
    if IS_MACOS and util._isDmg( installerPath ) :
        dmgPath = installerPath
        isDmgMount, mountPath, _, binPath = util._macMountDmg( dmgPath ) 
        if binPath is None:
            if isDmgMount: util._macUnMountDmg( mountPath ) 
            raise Exception( "Qt IWF installer binary not found." )
        installerPath = binPath  
    else : isDmgMount = False        
    if targetPath is None: 
        version = __QtIfwInstallerVersion( installerPath )
        targetPath = __defaultQtIfwPath( version ) 
        print( "targetPath: %s" % (targetPath,) )   
    if isFile( __qtIfwCreatorPath( targetPath ) ):
        if not isLocal: removeFile( installerPath )
        raise Exception( "A copy of QtIFW is already installed in: %s" 
                         % (targetPath,) )                             
    ifwQScriptPath = __generateQtIfwInstallerQScript()
    ifwPyScriptPath = __generateQtIfwInstallPyScript(                                    
        installerPath, ifwQScriptPath, targetPath )    
    runPy( ifwPyScriptPath )
    removeFile( ifwPyScriptPath )
    removeFile( ifwQScriptPath )
    if IS_MACOS: 
        if isDmgMount: 
            util._macUnMountDmg( mountPath ) 
            if not isLocal: removeFile( dmgPath )
    elif not isLocal: removeFile( installerPath )    
    isSuccess = isFile( __qtIfwCreatorPath( targetPath ) )
    print( "QtIFW successfully installed!" if isSuccess else
           "QtIFW FAILED to install!" )    
    return targetPath if isSuccess else None

def unInstallQtIfw( qtIfwDirPath=None, version=None ):
    if qtIfwDirPath is None: qtIfwDirPath = getenv( QT_IFW_DIR_ENV_VAR )    
    if qtIfwDirPath is None: qtIfwDirPath = __defaultQtIfwPath( version )
    uninstallerPath = joinPath( qtIfwDirPath, __QT_IFW_UNINSTALL_EXE_NAME )
    if not exists( uninstallerPath ): # maybe a file or a directory, i.e. .app is a dir
        raise  Exception( "The QtIFW uninstaller path cannot be resolved" )                             
    ifwQScriptPath = __generateQtIfwInstallerQScript()
    ifwPyScriptPath = __generateQtIfwInstallPyScript(        
        uninstallerPath, ifwQScriptPath, isInstaller=False )    
    runPy( ifwPyScriptPath )
    removeFile( ifwPyScriptPath )
    removeFile( ifwQScriptPath )
    isSuccess = not isFile( uninstallerPath )
    print( "QtIFW successfully uninstalled!" if isSuccess else
           "QtIFW FAILED to uninstall!" )    
    return isSuccess

def __defaultQtIfwPath( version=QT_IFW_DEFAULT_VERSION, isVerified=False ):
    if version is None: version=QT_IFW_DEFAULT_VERSION
    qtDefaultDir = joinPath( util._userHomeDirPath(), "Qt" )    
    subDirName = "QtIFW" if version is None else "QtIFW-%s" % (version,)
    qtIfwDir = joinPath( qtDefaultDir, subDirName )     
    if not isVerified : return qtIfwDir    
    return qtIfwDir if isFile( __qtIfwCreatorPath( qtIfwDir ) ) else None
    
def __defaultQtIfwCreatorPath( version=QT_IFW_DEFAULT_VERSION ):
    return __qtIfwCreatorPath( __defaultQtIfwPath( version ) )

def __qtIfwCreatorPath( qtIfwDir ):
    creatorPath = joinPath( qtIfwDir, 
        joinPath( __BIN_SUB_DIR, __QT_IFW_CREATOR_EXE_NAME ) )
    return creatorPath if isFile( creatorPath ) else None
    
# -----------------------------------------------------------------------------  
# adds any missing resources, required by the packages, to the configuration
def _addQtIfwResources( qtIfwConfig, packages ): 

    def isScriptFound( script, resources ):        
        if not script or not resources: return
        for res in resources:
            if isinstance( res, ExecutableScript ):
                if res.rootName == script.rootName: return True
        return False

    def addResource( res, resources ):        
        try: resources.append( res )
        except: resources = [res]

    def addMaintenanceToolResources( cfg, pkg ):
        try:
            for exOp in pkg.pkgScript.externalOps:
                # uninstall scripts must be added to Maintenance Tool resources
                if isinstance( exOp.uninstScript, ExecutableScript ):
                    if not isScriptFound( exOp.uninstScript, 
                        cfg.controlScript._maintenanceToolResources ):
                        addResource( exOp.uninstScript, 
                            cfg.controlScript._maintenanceToolResources )            
        except: pass

    for pkg in packages:
        if not isinstance( pkg, QtIfwPackage ) : continue
        addMaintenanceToolResources( qtIfwConfig, pkg )
        
# if the page is already present and overwrite is False, NOTHING will be modified                  
def _addQtIfwUiPages( qtIfwConfig, uiPages, isOverWrite=True ):

    def findPageOwner( packages, page ):    
        for pkg in packages :
            for pg in pkg.uiPages :
                if pg.name==page.name: return pkg
        return None            
    
    def add( ctrlScript, pkg, page ):        
        # if this is a replacement page for a built-in,
        # it must be the first page in the list with that page order
        # else the other pages with that order will end up appearing 
        # *after* this one rather than *before* it
        isInserted=False
        if page.name.startswith( QT_IFW_REPLACE_PAGE_PREFIX ):
            baseName = page.name[ len(QT_IFW_REPLACE_PAGE_PREFIX): ] 
            if baseName in _DEFAULT_PAGES:
                for i, pg in enumerate( pkg.uiPages ):
                    isInserted=pg.pageOrder==baseName
                    if isInserted: 
                        pkg.uiPages.insert( i,  page )
                        pkg.pkgScript.uiPages.insert( i, page )
                        ctrlScript.uiPages.insert( i, page )
                        break
        # if the page wasn't inserted into the middle of the list, append it                     
        if not isInserted:    
            pkg.uiPages.append( page )           
            pkg.pkgScript.uiPages.append( page )        
            ctrlScript.uiPages.append( page ) 
        # order doesn't matter for this list, but the items should be unique
        pkg.pkgXml.UserInterfaces.append( page.fileName() )
        pkg.pkgXml.UserInterfaces = list(set(pkg.pkgXml.UserInterfaces))

    def overwrite( ctrlScript, pkg, page ):        
        # order must be preserved here 
        pkg.uiPages = [ page if p.name==page.name else p 
                        for p in pkg.uiPages ]        
        pkg.pkgScript.uiPages = [ page if p.name==page.name else p 
                                  for p in pkg.pkgScript.uiPages ]
        ctrlScript.uiPages = [ page if p.name==page.name else p 
                               for p in  ctrlScript.uiPages ]
        # order doesn't matter for this list, but the items should be unique
        pkg.pkgXml.UserInterfaces.append( page.fileName() )
        pkg.pkgXml.UserInterfaces = list(set(pkg.pkgXml.UserInterfaces))
        
    if uiPages is None: return
    if isinstance( uiPages, QtIfwUiPage ): uiPages = [uiPages]  
    for page in uiPages:
        pkg = findPageOwner( qtIfwConfig.packages, page )
        if pkg:
            if isOverWrite: overwrite( qtIfwConfig.controlScript, pkg, page )
            continue            
        add( qtIfwConfig.controlScript, qtIfwConfig.packages[0], page )       
        
def findQtIfwPackage( pkgs, pkgId ):        
    for p in pkgs: 
        if p.pkgId==pkgId: return p
    return None 

def removeQtIfwPackage( pkgs, pkgId ):        
    pkgIndex=None
    for i, pkg in enumerate( pkgs ):
        if pkg.pkgId==pkgId: 
            pkgIndex=i
            break
    if pkgIndex is None: return     
    if isDir( pkg.dirPath() ): removeDir( pkg.dirPath() )
    if pkg.isTempSrc:
        if pkg.srcDirPath and isDir( pkg.srcDirPath ): 
            removeDir( pkg.srcDirPath )
        elif pkg.srcExePath and isFile( pkg.srcExePath ): 
            removeFile( pkg.srcExePath )                                    
    del pkgs[ pkgIndex ]               

def mergeQtIfwPackages( pkgs, srcId, destId ):            
    srcPkg  = findQtIfwPackage( pkgs, srcId )
    destPkg = findQtIfwPackage( pkgs, destId )
    if not srcPkg or not destPkg:
        raise Exception( "Cannot merge QtIfw packages. " +
                         "Invalid id(s) provided." )     
    mergeDirs( srcPkg.contentTopDirPath(), destPkg.contentDirPath() )    
    __mergePackageObjects( srcPkg, destPkg )    
    removeQtIfwPackage( pkgs, srcId )    
    return destPkg

def nestQtIfwPackage( pkgs, childId, parentId, subDirName=None ):                
    childPkg  = findQtIfwPackage( pkgs, childId )
    parentPkg = findQtIfwPackage( pkgs, parentId )
    if not childPkg or not parentPkg:
        raise Exception( "Cannot nest QtIfw package. " +
                         "Invalid id(s) provided." ) 
    if subDirName is None:        
        def prefix( name ): return ".".join( name.split(".")[:-1] ) + "." 
        def suffix( name ): return name.split(".")[-1]        
        subDirName = ( suffix( childPkg.name ) 
                   if prefix( childPkg.name ) == prefix( parentPkg.name )
                   else childPkg.name )     
    childHead, childTail = splitPath( childPkg.contentDirPath() )
    srcDir = renameInDir( (childTail, subDirName), childHead )
    destDir = parentPkg.contentDirPath()    
    copyToDir( srcDir, destDir )
    __mergePackageObjects( childPkg, parentPkg, subDirName )         
    removeQtIfwPackage( pkgs, childId )            
    return parentPkg

def __mergePackageObjects( srcPkg, destPkg, subDirName=None ):
    try: 
        srcShortcuts = srcPkg.pkgScript.shortcuts
        if subDirName:
            for i, _ in enumerate( srcShortcuts ): 
                srcShortcuts[i].exeDir = joinPathQtIfw( 
                    QT_IFW_TARGET_DIR, subDirName )                
    except: srcShortcuts = []            
    destScript = destPkg.pkgScript
    if destScript:    
        if srcShortcuts:
            try: destScript.shortcuts.extend( srcShortcuts )
            except: destScript.shortcuts = srcShortcuts
        if srcPkg.pkgScript.externalOps: 
            try: destScript.externalOps.extend( srcPkg.pkgScript.externalOps )
            except: destScript.externalOps = srcPkg.pkgScript.externalOps
        if srcPkg.pkgScript.customOperations:
            try: destScript.customOperations.extend( srcPkg.pkgScript.customOperations )
            except: destScript.customOperations = srcPkg.pkgScript.customOperations
        if srcPkg.pkgScript.killOps:
            try: destScript.killOps.extend( srcPkg.pkgScript.killOps )
            except: destScript.killOps = srcPkg.pkgScript.killOps
        print( "\nRegenerating installer package script: %s...\n" 
                % (destScript.path()) )
        destScript._generate()
        destScript.debug()
        destScript.write()    
        
# -----------------------------------------------------------------------------            
def buildInstaller( qtIfwConfig, isSilent ):
    ''' returns setupExePath '''
    _stageInstallerPackages( qtIfwConfig, isSilent )
    return _buildInstaller( qtIfwConfig, isSilent )

def _stageInstallerPackages( qtIfwConfig, isSilent ):
    __validateConfig( qtIfwConfig )        
    if isSilent: __toSilentConfig( qtIfwConfig )
    __initBuild( qtIfwConfig )    
    __addInstallerResources( qtIfwConfig )     

def _buildInstaller( qtIfwConfig, isSilent ):    
    setupExePath = __build( qtIfwConfig )    
    __postBuild( qtIfwConfig )
    if isSilent : setupExePath = __buildSilentWrapper( qtIfwConfig )
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
            elif not ( isFile(p.srcExePath) or 
                  (IS_MACOS and util._isMacApp(p.srcExePath)) ) :        
                raise Exception( "Package Source exe path is not valid" )    
        elif not isDir(p.srcDirPath) :        
            raise Exception( "Package Source directory path is not valid" )
    # resolve or install required utility paths 
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = getenv( QT_IFW_DIR_ENV_VAR )    
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = __defaultQtIfwPath( isVerified=True )
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = installQtIfw()                    
    if( qtIfwConfig.qtIfwDirPath is None or
        not isFile( __qtIfwCreatorPath( qtIfwConfig.qtIfwDirPath ) ) ):        
        raise Exception( "Valid Qt IFW directory path required" )
    for p in qtIfwConfig.packages :
        if not isinstance( p, QtIfwPackage ) : continue
        if p.pkgType == QtIfwPackage.Type.QT_CPP :
            p.qtCppConfig.validate() 

def __initBuild( qtIfwConfig ) :
    print( "Initializing installer build..." )
    # remove any prior setup file
    setupExePath = absPath( util.normBinaryName( qtIfwConfig.setupExeName ) )
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
            srcExeDir, srcExeName = splitPath( 
                normBinaryName( p.srcExePath, isPathPreserved=True, 
                                isGui=p.isGui ) )
            # if the source was was not in the source directory
            # and therefore already copied to the destDir, do so...
            if srcExeDir != p.srcDirPath :         
                if not isDir( destDir ): makeDir( destDir )
                copyToDir( p.srcExePath, destDirPath=destDir )
            # reconcile the exeName with the source exe                     
            if p.exeName is None: p.exeName = srcExeName 
            elif p.exeName != srcExeName :             
                rename( joinPath( destDir, srcExeName ),
                        joinPath( destDir, p.exeName ) )            
    print( "Build directory created: %s" % (BUILD_SETUP_DIR_PATH,) )

def __addInstallerResources( qtIfwConfig ) :
    
    _addQtIfwResources( qtIfwConfig, qtIfwConfig.packages )
    _addQtIfwUiPages( qtIfwConfig, QtIfwTargetDirPage(), isOverWrite=False )
    
    genQtIfwCntrlRes( qtIfwConfig ) 
                                      
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

        if p.uiPages: __addUiPages( qtIfwConfig, p ) 

        if p.pkgType == QtIfwPackage.Type.QT_CPP : 
            p.qtCppConfig.addDependencies( p )        

        if p.distResources: __addResources( p )     

        if isinstance( p.exeWrapper, QtIfwExeWrapper ): 
            __addExeWrapper( p )
                        
def genQtIfwCntrlRes( qtIfwConfig ) :
    
    configXml = qtIfwConfig.configXml
    ctrlScript = qtIfwConfig.controlScript
    
    if ctrlScript and configXml: 
        configXml.ControlScript = ctrlScript.fileName         
            
    if configXml :         
        print( "%s installer configuration resources..." 
               % ( "Regenerating" if configXml.exists() else "Adding" ) )
        configXml.debug()
        configXml.write()
        if configXml.iconFilePath :
            iconFilePath = absPath( configXml.iconFilePath )
            if isFile( iconFilePath ):
                copyFile( iconFilePath,                       
                          joinPath( configXml.dirPath(), 
                                    fileBaseName( configXml.iconFilePath ) ) )
    if ctrlScript :
        # Allow component selection to be explicitly disabled, but force that
        # when there are not multiple packages to begin with
        if len(qtIfwConfig.packages) < 2:
            ctrlScript.isComponentSelectionPageVisible=False 
        print( "%s installer control script..." 
               % ( "Regenerating" if ctrlScript.exists() else "Adding" ) )       
        if ctrlScript.script: ctrlScript._generate() 
        ctrlScript.debug()
        ctrlScript.write()        
                        
def __addUiPages( qtIfwConfig, package ) :
    for ui in package.uiPages:
        if isinstance( ui, QtIfwUiPage ): 
            ui.resolve( qtIfwConfig ) 
            ui.write( package.metaDirPath() )
                
def __addResources( package ) :    
    print( "Adding additional resources..." )
    destDir = package.contentDirPath()            
    basePath = package.resBasePath
    for res in package.distResources:
        src, dest = util._toSrcDestPair( res, destDir, basePath )
        print( 'Copying "%s" to "%s"...' % ( src, dest ) )
        if isFile( src ) :
            destParent = dirPath( dest )
            if not exists( destParent ): makeDir( destParent )
            try: copyFile( src, dest ) 
            except Exception as e: printExc( e )
        elif isDir( src ):
            try: copyDir( src, dest ) 
            except Exception as e: printExc( e )
        else:
            printErr( 'Invalid path: "%s"' % (src,) )                            

def __addExeWrapper( package ) :
    exeWrapperScript = package.exeWrapper.wrapperScript
    if isinstance( exeWrapperScript, ExecutableScript ):            
        dirPath = package.contentDirPath()
        fileName = exeWrapperScript.fileName()
        filePath = joinPath( dirPath, fileName )
        
        # For macOS apps, the wrapper will replace the orginal executable
        # binary and the original will be renamed with a leading underscore 
        # (which is indictive of being protected and/or hidden)
        if IS_MACOS and package.exeWrapper.isGui :
            appPath = normBinaryName( filePath, isPathPreserved=True, isGui=True )
            binPath = util._macAppBinaryPath( appPath )
            if isFile( binPath ):
                dirPath, binName = splitPath( binPath ) 
                renameInDir( (binName, "_%s" % (binName,)), dirPath )
        
        isFound = isFile( filePath )
        isCustom = exeWrapperScript.script is not None    
        if isFound:
            print( "%sExecutable wrapper script: %s content:\n" %
                   (("ORIGINAL " if isCustom else ""), fileName) )                   
            with open( filePath, 'r' ) as f: print( "\n\n%s\n\n" % (f.read(),) )
        if isCustom:
            if isFound: print( "REPLACING..." )                           
            exeWrapperScript.write( dirPath )           

def __build( qtIfwConfig ) :
    print( "Building installer using Qt IFW...\n" )
    creatorPath = __qtIfwCreatorPath( qtIfwConfig.qtIfwDirPath )
    setupExePath = joinPath( THIS_DIR, 
                             util.normBinaryName( qtIfwConfig.setupExeName ) )
    cmd = '%s %s "%s"' % ( creatorPath, str(qtIfwConfig), setupExePath )
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

def __toSilentConfig( qtIfwConfig ):
    qtIfwConfig.controlScript.isIntroductionPageVisible         = False                                                                   
    qtIfwConfig.controlScript.isTargetDirectoryPageVisible      = False
    qtIfwConfig.controlScript.isComponentSelectionPageVisible   = False
    qtIfwConfig.controlScript.isLicenseAgreementPageVisible     = False
    qtIfwConfig.controlScript.isStartMenuDirectoryPageVisible   = False
    qtIfwConfig.controlScript.isReadyForInstallationPageVisible = False
    qtIfwConfig.controlScript.isPerformInstallationPageVisible  = False
    qtIfwConfig.controlScript.isFinishedPagePageVisible         = False 
    
def __buildSilentWrapper( qtIfwConfig ) :
    print( "Building silent wrapper executable...\n" )
    from distbuilder.master import PyToBinPackageProcess, ConfigFactory
    
    # On macOS, a "gui" .app must be build because that provides a .plist
    # and an application we can best manipulate via AppleScript
    
    srcSetupExeName   = util.normBinaryName( qtIfwConfig.setupExeName, isGui=True )    
    destSetupExeName  = util.normBinaryName( qtIfwConfig.setupExeName, isGui=False ) 
    nestedExeName     = util.normBinaryName( __NESTED_INSTALLER_NAME,  isGui=True )
    wrapperExeName    = __WRAPPER_INSTALLER_NAME
    wrapperPyName     = __WRAPPER_SCRIPT_NAME    
    componentList     = [ (package.pkgXml.Default,
                           package.pkgXml.pkgName, 
                           package.pkgXml.DisplayName) 
                           for package in qtIfwConfig.packages ]            
    wrapperScript     = __silentQtIfwScript( nestedExeName, componentList )
        
    cfgXml            = qtIfwConfig.configXml
                                               
    f = configFactory  = ConfigFactory()
    f.productName      = cfgXml.Name
    f.description      = cfgXml.Name # don't have the exact description with this config
    f.companyLegalName = cfgXml.Publisher    
    f.binaryName       = wrapperExeName
    f.isGui            = False       
    f.entryPointPy     = wrapperPyName  
    f.iconFilePath     = cfgXml.iconFilePath  
    f.version          = cfgXml.Version 
    
    class BuildProcess( PyToBinPackageProcess ):            
        def onInitialize( self ):
            renameInDir( (srcSetupExeName, nestedExeName) )
            if IS_MACOS :               
                self.__injectHidePropertyIntoApp( nestedExeName )
                # a .app is a directory, so the "wrapper dir" must be preserved
                self.__nestedZipPath = toZipFile( nestedExeName, 
                                                  isWrapperDirIncluded=True ) 
            removeFromDir( wrapperPyName )
            with open( absPath( wrapperPyName ), 'w' ) as f:
                print( "Generating silent wrapper script:\n" ) 
                print( wrapperScript )
                f.write( wrapperScript )  
            
        def onPyInstConfig( self, cfg ):    
            if IS_MACOS: cfg.dataFilePaths   = [ self.__nestedZipPath ]
            else       : cfg.binaryFilePaths = [ absPath( nestedExeName ) ]
            cfg.isAutoElevated = True # Windows only feature
            
        def onFinalize( self ):
            removeFromDir( wrapperPyName )            
            removeFromDir( self.__nestedZipPath 
                           if IS_MACOS else nestedExeName )
            dirName = fileBaseName( self.binDir )
            binName = fileBaseName( self.binPath )       
            tmpDir = renameInDir( (dirName, "__" + dirName) )             
            moveToDir( joinPath( tmpDir, binName ) ) 
            removeFromDir( tmpDir )
            self.binPath = renameInDir( (binName, destSetupExeName) )
            self.binDir = dirPath( self.binPath )            
            #if IS_MACOS : self.__injectHidePropertyIntoApp( destSetupExeName )
                
        # On macOS enabling LSUIElement in the .plist will prevent 
        # showing the app icon in the dock when it is launched.  
        # Unfortunately, no analogous property seems to hide it from 
        # the screen! (or least not this app, on recent versions of the os...)
        def __injectHidePropertyIntoApp( self, appPath ):    
            util._system( ( "/usr/libexec/PlistBuddy -c " +
                "'Add :LSUIElement bool true' {0}/Contents/Info.plist" ).format(
                absPath( appPath ) ) )
                    
    BuildProcess( configFactory ).run()
    return absPath( destSetupExeName )
    
def __silentQtIfwScript( exeName, componentList=[],
                         isQtIfwInstaller=False,
                         isQtIfwUnInstaller=False,
                         scriptPath=None,
                         wrkDir=None, targetDir=None) :
    """
    Runs the IFW exe from inside the PyInstaller MEIPASS directory,
    with elevated privileges, hidden from view, gathering
    stdout, stderr, and other logged communications.  
    Note: On Windows, the wrapper is auto-elevated via PyInstaller.
    """
    
    componentsRepr     = "[]"
    componentsEpilogue = "" 
    componentsPrefix   = ""
    if len(componentList) > 1 :
        componentsRepr = ""
        idLen = 0 
        for (_, compId, _ ) in componentList :
            componentsRepr += ( ("" if componentsRepr=="" else ", ")  
                              + ("'%s'" % (compId,)) )            
            if len( compId ) > idLen : idLen = len( compId )
            prefix = ".".join( compId.split(".")[:-1] ) + "."
            if componentsPrefix=="" : componentsPrefix = prefix
            elif prefix != componentsPrefix: componentsPrefix=None
        componentsRepr = "[ " + componentsRepr + " ]"            
        componentsPrefixLen = (0 if componentsPrefix is None 
                               else len(componentsPrefix) )
        lineLen = 79
        defLen = 5
        idLen = idLen - componentsPrefixLen + 2        
        nameLen = lineLen - defLen - idLen   
        lnFormat = '{0:>%s}{1:<%s}{2:<%s}\n' % ( defLen, idLen, nameLen )
        componentsEpilogue = ( "Components:\n" + 
            lnFormat.format("Def ", "Id", "Name\n" ) ) 
        for (isDef, compId, name ) in componentList :
            default = "* " if isDef else ""
            if componentsPrefixLen : compId = compId[componentsPrefixLen:]
            componentsEpilogue += lnFormat.format( default, compId, name ) 

    if IS_WINDOWS: 
        imports = (
"""     
from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW
import glob
""" )
        
        helpers = ""
        preProcess = ""

        createInstallerProcess = (
"""    
    processStartupInfo = STARTUPINFO()
    processStartupInfo.dwFlags |= STARTF_USESHOWWINDOW 
    process = Popen( [EXE_PATH] + ARGS, cwd=WORK_DIR,
                     shell=False,
                     startupinfo=processStartupInfo,                                                                
                     universal_newlines=True,
                     stdout=PIPE, stderr=PIPE )
""" )

    if isQtIfwInstaller :
        cleanUp = (
"""     
    # Wait for IFW to release its lock       
    IFW_LOCK_FILE_PATTERN = "lockmyApp*.lock"    
    while glob.glob(  IFW_LOCK_FILE_PATTERN ): pass    
""" )
    elif isQtIfwUnInstaller:
        cleanUp = (
"""     
    pass
""" )
    else :                                                         
        cleanUp = (
"""     
    IFW_LOCK_FILE_PATTERN = "lockmyApp*.lock"
    PY_INST_FILE_RELEASE_DELAY_SECS = 2

    # Wait for IFW to release its lock       
    while glob.glob(  IFW_LOCK_FILE_PATTERN ): pass
    
    # For some reason, PyInstaller won't delete the IFW exe,
    # so that must be forced. It might still be OS locked at  
    # this point, and thus take a few attempts... 
    while os.path.exists( EXE_PATH ): 
        try: os.remove( EXE_PATH )
        except: pass
    
    removeIfwErrLog()
                                
    # this ugly pause causes the PyInstaller temp directory  
    # auto removal to work more reliably
    time.sleep( PY_INST_FILE_RELEASE_DELAY_SECS )        
""" )
    
    if IS_MACOS :  
        if isQtIfwInstaller:
            imports    = ""
            helpers = (
"""
BIN_PATH     = WORK_DIR + "/" + EXE_NAME    # os.path.join( WORK_DIR, EXE_NAME )
""") 
            preProcess = ""
        elif isQtIfwUnInstaller:
            imports    = ""
            helpers = (
"""
APP_PATH     = WORK_DIR + "/" + EXE_NAME    # os.path.join( WORK_DIR, EXE_NAME )
APP_BIN_DIR  = os.path.join( APP_PATH, "Contents/MacOS" )
BIN_PATH     = os.path.join( APP_BIN_DIR, os.listdir( APP_BIN_DIR )[0] )
""") 
            preProcess = ""            
        else :     
            imports = (
"""     
import zipfile, tempfile
""" )

            helpers = (
"""
APP_PATH     = WORK_DIR + "/" + EXE_NAME    # os.path.join( WORK_DIR, EXE_NAME )
ZIP_PATH     = APP_PATH + ".zip" 
APP_BIN_DIR  = os.path.join( APP_PATH, "Contents/MacOS" )
BIN_PATH     = ""

def extractBinFromZip():
    global BIN_PATH
    zipfile.ZipFile( ZIP_PATH, 'r' ).extractall( WORK_DIR )   
    BIN_PATH = os.path.join( APP_BIN_DIR, os.listdir( APP_BIN_DIR )[0] )
    os.chmod( BIN_PATH, 0o777 )    

# Failed experiment to hide the gui abandoned, but not 
# purged entirely from the code just yet...
# Note, this is for a .app, not the non-gui unix binary
# I went back to using once this did not work...
# This CAN hide the gui, but it only works by forcing 
#  the user into a manual 
#  System Preferences update, as damn Apple revoked the 
#  only means of programmatically granting such...
#  Plus, it's doesn't work "perfectly" anyway...
#    (i.e. a corner of the screen can still be glimpsed) 
PROCESS_NAME = os.path.splitext( EXE_NAME )[0]
RUN_APP_OFF_SCREEN_SCRIPT = (    
'''
do shell script "open %s %s"
set isMoved to false
set attempts to 0
repeat until isMoved or attempts = 25
    tell application "System Events" to tell process "%s"
        try
            set position of front window to {-9999999, 9999999}
            set isMoved to true
        end try
        set attempts to attempts + 1
    end tell
end repeat
''') % ( APP_PATH, " ".join(ARGS), PROCESS_NAME )
    
def runAppleScript( script ):
    scriptPath = tempfile.mktemp( suffix='.scpt' )
    with open( scriptPath, 'w' ) as f : f.write( script )
    ret = subprocess.call( ['osascript', scriptPath] ) 
    os.remove( scriptPath )
    if ret != 0 : raise RuntimeError( "AppleScript failed." )
""")

            preProcess = (
"""
    extractBinFromZip()
""")

            
        createInstallerProcess = (
"""    
    process = Popen( [ "sudo", BIN_PATH ] + ARGS, cwd=WORK_DIR,
                     shell=False,
                     universal_newlines=True,
                     stdout=PIPE, stderr=PIPE )
""")                                                     

        cleanUp = (
"""            
    removeIfwErrLog()
""" )

    if IS_LINUX : 
        imports = (
"""
import shlex
try: from subprocess import DEVNULL 
except ImportError: DEVNULL = open(os.devnull, 'wb')
""")

        helpers = (
"""
PKG_MGR_ERR_MSG = "No compatible package manager installed."

TEMP_PKG_DEPENDENCIES = { 
      "xvfb"       : [ "xvfb", "Xvfb" ]
    , "fontconfig" : [ "fontconfig", "libfontconfig1" ]
}

def packageAliases( pkg ):
    return TEMP_PKG_DEPENDENCIES.get( pkg, [pkg] ) 

def isPackageManagerInstalled( prog ):    
    try: 
        subprocess.check_call( [prog, "--help"], 
            stdout=DEVNULL, stderr=DEVNULL )
        return True                                                              
    except: return False     
def isAptInstalled():  return isPackageManagerInstalled( "apt" )   
def isDpkgInstalled(): return isPackageManagerInstalled( "dpkg" )
def isYumInstalled():  return isPackageManagerInstalled( "yum" )
def isRpmInstalled():  return isPackageManagerInstalled( "rpm" )

def isPackageInstalled( pkg ):
    if   isDpkgInstalled() : cmd = ["dpkg", "-l"]
    elif isRpmInstalled()  : cmd = ["rpm",  "-q"]
    else : raise RuntimeError( PKG_MGR_ERR_MSG )     
    aliases = packageAliases( pkg )
    for alias in aliases:    
        try:
            subprocess.check_call( cmd + [alias], 
                stdout=DEVNULL, stderr=DEVNULL )
            return True                                                              
        except: pass     
    return False

def installPackage( pkg ):
    if   isAptInstalled(): 
        inCmd = ["sudo", "apt-get", "install", "-y"]   
        rmCmd = ["sudo", "apt-get", "remove",  "-y"]
    elif isYumInstalled(): 
        inCmd = ["sudo", "yum", "install", "-y"]
        rmCmd = ["sudo", "yum", "remove",  "-y"]
    else : raise RuntimeError( PKG_MGR_ERR_MSG )     
    aliases = packageAliases( pkg )
    for alias in aliases:
        cmd = inCmd + [alias]            
        try:            
            subprocess.check_call( cmd, 
                stdout=DEVNULL, stderr=DEVNULL )
            if IS_VERBOSE:
                print( ' '.join( cmd ) ) 
                print( "Installed dependency: %s" % (alias,) )
            return rmCmd + [alias]                                                              
        except: pass     
    raise RuntimeError( 
        "Failed to install dependency: %s" % (pkg,) ) 

CLEANUP_CMDS=[]
def installTempDependencies():    
    global CLEANUP_CMDS
    for pkg in TEMP_PKG_DEPENDENCIES.keys() :
        if not isPackageInstalled( pkg ):
            CLEANUP_CMDS.append( installPackage( pkg ) )    
""")

        preProcess = (
"""
    installTempDependencies()
""")

        createInstallerProcess = (
"""
    process = Popen( [ "sudo", "xvfb-run", "./%s" % (EXE_NAME,) ] + ARGS, 
                     cwd=WORK_DIR,
                     shell=False,
                     universal_newlines=True,
                     stdout=PIPE, stderr=PIPE )
""")

        cleanUp = (
"""
    for cmd in CLEANUP_CMDS:
        if IS_VERBOSE: print( ' '.join( cmd ) ) 
        subprocess.check_call( cmd )         
    removeIfwErrLog()
""")       

    if isQtIfwInstaller or isQtIfwUnInstaller :
        return (
"""
import os, sys, time, argparse, subprocess
from subprocess import Popen, PIPE
{3}

SUCCESS=0
FAILURE=1

IS_WINDOWS = {4}

WORK_DIR         = "{1}"
EXE_NAME         = "{0}"
EXE_PATH         = os.path.join( WORK_DIR, EXE_NAME )

ARGS = ["-v","--script", "{2}" {9}]
IS_VERBOSE = True

{5}

def main():        
    {6}
    exitCode = runInstaller()
    cleanUp()        
    print( "Success!" if exitCode==SUCCESS else "Failure!" )    
    return exitCode

def runInstaller():
{7}
                                                     
    if IS_VERBOSE :
        POLL_DELAY_SECS = 0.1
        while process.poll() is None:
            sys.stdout.write( process.stdout.read() )
            sys.stderr.write( process.stderr.read() )
            time.sleep( POLL_DELAY_SECS )
        sys.stdout.write( process.stdout.read() )
        sys.stderr.write( process.stderr.read() )
    else : process.wait()    

    return process.returncode

def cleanUp():
{8}

def removeIfwErrLog(): pass

sys.exit( main() )
""").format( 
      exeName 
    , util._normEscapePath(wrkDir)
    , util._normEscapePath(scriptPath) 
    , imports             
    , IS_WINDOWS  
    , helpers
    , preProcess
    , createInstallerProcess
    , cleanUp
    , ( (', "target=%s"' % (util._normEscapePath(targetDir),)) 
        if isQtIfwInstaller else "" )
)
    else:
        return (
"""
import os, sys, time, argparse, subprocess
from subprocess import Popen, PIPE
{17}

SUCCESS=0
FAILURE=1

IS_WINDOWS = {10}

WORK_DIR         = sys._MEIPASS
EXE_NAME         = "{0}"
EXE_PATH         = os.path.join( WORK_DIR, EXE_NAME )
IFW_ERR_LOG_NAME = "installer.err"
IFW_ERR_LOG_PATH = os.path.join( WORK_DIR, IFW_ERR_LOG_NAME )

VERBOSE_SWITCH = "{4}"

components = {14}
componentsEpilogue = ( 
'''{15}'''
)
componentsPrefix = "{16}"

ARGS = []
IS_VERBOSE = False

{18}

def main():        
    global ARGS, IS_VERBOSE
    ARGS = toIwfArgs( wrapperArgs() )  
    IS_VERBOSE = VERBOSE_SWITCH in ARGS
    removeIfwErrLog() 
    {19}
    exitCode = runInstaller()
    cleanUp()        
    print( "Success!" if exitCode==SUCCESS else "Failure!" )    
    return exitCode

def wrapperArgs():
    parser = argparse.ArgumentParser( epilog=componentsEpilogue,
                formatter_class=argparse.RawTextHelpFormatter )
                
    parser.add_argument( '-v', '--verbose', default=False,
                         help='verbose mode', 
                         action='store_true' )
    parser.add_argument( '-f', '--force', default=False, 
                         help='force installation (uninstall existing installation)', 
                         action='store_true' )
    parser.add_argument( '-t', '--target', default=None,
                         help='target directory' )
                         
    if IS_WINDOWS :                          
        parser.add_argument( '-m', '--startmenu', default=None,  
                             help='start menu directory' )
                             
    if len(components) > 0 :                             
        parser.add_argument( '-c', '--components', nargs='*', default=[],
                             help='component ids to install (space delimited list)' )
        parser.add_argument( '-i', '--include', nargs='*', default=[],
                             help='component ids to include (space delimited list)' )
        parser.add_argument( '-e', '--exclude', nargs='*', default=[],
                             help='component ids to exclude (space delimited list)' )  
                                                        
    return parser.parse_args()

def toIwfArgs( wrapperArgs ):
    # silent install always uses:
    #     auto pilot mode
    #     client defined error log path
    #     run at end disabled
    args = ["{1}", ("{2}=%s" % IFW_ERR_LOG_NAME), "{3}"] 

    if wrapperArgs.verbose : args.append( VERBOSE_SWITCH )    
    args.append( "{5}={6}" if wrapperArgs.force else "{5}={7}" )
    if wrapperArgs.target is not None : 
        args.append( "{8}=%s" % (wrapperArgs.target.replace("\\\\","/"),) )
    
    if IS_WINDOWS :      
        if wrapperArgs.startmenu is not None : 
            args.append( "{9}=%s" % (wrapperArgs.startmenu.replace("\\\\","/"),) )
    
    if len(components) > 0 : 
        def appendComponentArg( wrapperArg, ifwArg ):     
            if len(wrapperArg) > 0:
                comps = ["%s%s" % (componentsPrefix,c) for c in wrapperArg]
                for id in comps:
                    if id not in components: 
                        sys.stderr.write( "Invalid component id: %s" % (id,) )
                        sys.exit( FAILURE )
                args.append( "%s=%s" % (ifwArg, ",".join(comps)) )
        appendComponentArg( wrapperArgs.components, "{11}" )
        appendComponentArg( wrapperArgs.include,    "{12}" )
        appendComponentArg( wrapperArgs.exclude,    "{13}" )

    return args

def runInstaller():
{20}
                                                     
    if IS_VERBOSE :
        POLL_DELAY_SECS = 0.1
        while process.poll() is None:
            sys.stdout.write( process.stdout.read() )
            sys.stderr.write( process.stderr.read() )
            time.sleep( POLL_DELAY_SECS )
        sys.stdout.write( process.stdout.read() )
        sys.stderr.write( process.stderr.read() )
    else : process.wait()    
    
    # use error log existence to set an exit code, 
    # since IFW doesn't support such currently  
    if os.path.exists( IFW_ERR_LOG_PATH ):
        with open( IFW_ERR_LOG_PATH ) as f:
            sys.stderr.write( f.read() )
        return FAILURE
    return process.returncode

def cleanUp():
{21}

def removeIfwErrLog(): 
    if os.path.exists( IFW_ERR_LOG_PATH ):
        os.remove( IFW_ERR_LOG_PATH )

sys.exit( main() )
""").format( exeName 
    , ("%s=true" % (_QtIfwScript.AUTO_PILOT_CMD_ARG,))
    , _QtIfwScript.ERR_LOG_PATH_CMD_ARG    
    , ("%s=false" % (_QtIfwScript.RUN_PROGRAM_CMD_ARG,))
    , _QtIfwScript.VERBOSE_CMD_SWITCH_ARG
    , _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG
    , _QtIfwScript.TARGET_EXISTS_OPT_REMOVE
    , _QtIfwScript.TARGET_EXISTS_OPT_FAIL       
    , _QtIfwScript.TARGET_DIR_CMD_ARG
    , _QtIfwScript.START_MENU_DIR_CMD_ARG 
    , IS_WINDOWS
    , _QtIfwScript.INSTALL_LIST_CMD_ARG 
    , _QtIfwScript.INCLUDE_LIST_CMD_ARG
    , _QtIfwScript.EXCLUDE_LIST_CMD_ARG
    , componentsRepr
    , componentsEpilogue
    , componentsPrefix
    , imports
    , helpers
    , preProcess
    , createInstallerProcess
    , cleanUp
)

def __generateQtIfwInstallPyScript( installerPath, ifwScriptPath, 
                                    targetPath=None,
                                    isInstaller=True ):
    installerDir, installerName = splitPath( installerPath ) 
    script = __silentQtIfwScript( 
        installerName, 
        isQtIfwInstaller=isInstaller, isQtIfwUnInstaller=(not isInstaller), 
        scriptPath=ifwScriptPath, wrkDir=installerDir,
        targetDir=targetPath )    
    filePath = joinPath( tempDirPath(), 
        __QT_IFW_AUTO_INSTALL_PY_SCRIPT_NAME if isInstaller else
        __QT_IFW_AUTO_UNINSTALL_PY_SCRIPT_NAME )
    #print( "Generating Python Script: %s" % (filePath,) )
    #print( "\n%s\n" % (script,) )
    with open( filePath, 'w' ) as f: f.write( script ) 
    return filePath 
            
def __generateQtIfwInstallerQScript() :
    script = (
"""
function Controller() {
    installer.installationFinished.connect(this, Controller.prototype.onInstallFinished);
    installer.uninstallationFinished.connect(this, Controller.prototype.onUninstallFinished);
}
    
Controller.prototype.IntroductionPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.TargetDirectoryPageCallback = function() {
    if( installer.value( "target", "" )!="" )
        gui.currentPageWidget().TargetDirectoryLineEdit.setText(installer.value( "target", "" ));
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.ComponentSelectionPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.LicenseAgreementPageCallback = function() {
    gui.currentPageWidget().AcceptLicenseRadioButton.setChecked(true);
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.StartMenuDirectoryPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.ReadyForInstallationPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.PerformInstallationPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}
    
Controller.prototype.FinishedPageCallback = function() {
    gui.clickButton(buttons.FinishButton);
}

Controller.prototype.onInstallFinished = function(){
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.onUninstallFinished = function(){
    gui.clickButton(buttons.NextButton);
}
""")
    filePath = joinPath( tempDirPath(), __QT_IFW_UNATTENDED_SCRIPT_NAME )
    #print( "Generating QScript: %s" % (filePath,) )
    #print( "\n%s\n" % (script,) )
    with open( filePath, 'w' ) as f: f.write( script ) 
    return filePath 

def __QtIfwInstallerVersion( installerPath ):
    version = util._subProcessStdOut( 
        [installerPath, "--framework-version"] )
    # TODO: validate expected format returned, return None if bad
    return version    
        