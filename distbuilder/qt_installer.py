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

__WRAPPER_SCRIPT_NAME = "__installer.py"
__WRAPPER_INSTALLER_NAME = "wrapper-installer" 
__NESTED_INSTALLER_NAME  = "hidden-installer"

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
                  controlScript=None, 
                  setupExeName=DEFAULT_SETUP_NAME ) :       
        self.installerDefDirPath = installerDefDirPath
        self.packages            = packages # list of QtIfwPackages or directory paths
        self.configXml           = configXml
        self.controlScript       = controlScript         
        if self.controlScript and self.configXml: 
            self.configXml.ControlScript = self.controlScript.fileName  
        
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
        packageDirSpec = ' -p "%s"' % (QtIfwPackage.dirPath(),)        
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
        
    def __init__( self, name, version, publisher,
                  iconFilePath=None, 
                  controlScriptName=None,
                  primaryContentExe=None,
                  isGuiPrimaryContentExe=True,
                  companyTradeName=None ) :
        _QtIfwXml.__init__( self, QtIfwConfigXml.__ROOT_TAG, 
                            QtIfwConfigXml.__TAGS )
       
        self.primaryContentExe = ( 
            util.normBinaryName( primaryContentExe, 
                                 isGui=isGuiPrimaryContentExe )
            if primaryContentExe else None )
        
        if IS_LINUX :
            # qt installer does not support icon embedding in Linux
            iconBaseName = self.iconFilePath = None
        else :    
            self.iconFilePath = ( None if iconFilePath is None else 
                                  util._normIconName( iconFilePath, 
                                                      isPathPreserved=True ) )        
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
        self.ControlScript            = controlScriptName 
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
        if self.primaryContentExe is not None: 
            # NOTE: THE WORKING DIRECTORY IS NOT SET FOR RUN PROGRAM!
            # THERE DOES NOT SEEM TO BE AN OPTION YET FOR THIS IN QT IFW   
            programPath = "@TargetDir@/%s" % (self.primaryContentExe,)    
            if util._isMacApp( self.primaryContentExe ):   
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

    @staticmethod
    def dirPath() :  
        return joinPath( BUILD_SETUP_DIR_PATH,
            normpath( QtIfwPackage.__PACKAGES_PATH_TMPLT 
                      % (INSTALLER_DIR_PATH,) ) )
    
    def __init__( self, pkgId=None, name=None, 
                  srcDirPath=None, srcExePath=None,    
                  isTempSrc=False,
                  pkgXml=None, pkgScript=None ) :
        # internal id
        self.pkgId           = pkgId       
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
        self.exeName        = None   
        self.isGui          = False
        self.isQtCppExe     = False
        self.isMingwExe     = False
        self.qmlScrDirPath  = None  # for QML projects only   
            
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
@six.add_metaclass(ABCMeta)
class _QtIfwScript:
    
    # an example for use down the line...
    __LINUX_GET_DISTRIBUTION = ( 
"""
        var IS_UBUNTU   = (systemInfo.productType === "ubuntu");
        var IS_OPENSUSE = (systemInfo.productType === "opensuse");             
""" )

    def __init__( self, fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        self.fileName = fileName
        if scriptPath :
            with open( scriptPath, 'rb' ) as f: self.script = f.read()
        else : self.script = script  
                                                    
    def __str__( self ) : 
        if not self.script: self._generate()
        return self.script
        
    def write( self ):
        pkgDir = self.dirPath()
        if not isDir( pkgDir ): makeDir( pkgDir )
        with open( self.path(), 'w' ) as f: 
            f.write( str(self) ) 
    
    def debug( self ): print( str(self) )

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
                    
    __SILENT_CONSTRUCTOR_BODY = ( 
"""
    installer.autoRejectMessageBoxes();
    installer.setMessageBoxAutomaticAnswer("OverwriteTargetDirectory", QMessageBox.Yes);
    installer.setMessageBoxAutomaticAnswer("stopProcessesForUpdates", QMessageBox.Ignore);        
    installer.installationFinished.connect(function() {
        gui.clickButton(buttons.NextButton);
    });
""" )
    
    __CLICK_BUTTON_TMPL       = "gui.clickButton(%s);"
    __CLICK_BUTTON_DELAY_TMPL = "gui.clickButton(%s, %d);"

    _NEXT_BUTTON   = "buttons.NextButton"
    _BACK_BUTTON   = "buttons.BackButton"
    _CANCEL_BUTTON = "buttons.CancelButton"
    _FINISH_BUTTON = "buttons.FinishButton"
    
    @staticmethod        
    def _getClickButton( button, delayMillis=None ):                
        return ( 
            QtIfwControlScript.__CLICK_BUTTON_DELAY_TMPL % (button, delayMillis)
            if delayMillis else
            QtIfwControlScript.__CLICK_BUTTON_TMPL % (button,) )
            
    def __init__( self,
                  isAutoPilotMode=False,                    
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.isAutoPilotMode = isAutoPilotMode
        
        self.controllerConstructorBody = None
        self.isAutoControllerConstructor = True
                                                            
        self.introductionPageCallbackBody = None
        self.isAutoIntroductionPageCallback = True

        self.targetDirectoryPageCallbackBody = None
        self.isAutoTargetDirectoryPageCallback = True

        self.componentSelectionPageCallbackBody = None
        self.isAutoComponentSelectionPageCallback = True

        self.licenseAgreementPageCallbackBody = None
        self.isAutoLicenseAgreementPageCallback = True

        self.startMenuDirectoryPageCallbackBody = None
        self.isAutoStartMenuDirectoryPageCallback = True

        self.readyForInstallationPageCallbackBody = None
        self.isAutoReadyForInstallationPageCallback = True

        self.performInstallationPageCallbackBody = None
        self.isAutoPerformInstallationPageCallback = True
        
        self.finishedPageCallbackBody = None
        self.isAutoFinishedPageCallback = True        
                                                    
    def __str__( self ) : 
        if not self.script: self._generate()
        return self.script
            
    def _generate( self ) :        
        self.script = ""
        
        if self.isAutoControllerConstructor:
            self.__genControllerConstructorBody()
        self.script += ( "function Controller() {\n%s\n}\n" % 
                         (self.controllerConstructorBody,) )
        
        if self.isAutoIntroductionPageCallback:
            self.__genIntroductionPageCallbackBody()
        if self.introductionPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("Introduction", self.introductionPageCallbackBody) )
            
        if self.isAutoTargetDirectoryPageCallback:
            self.__genTargetDirectoryPageCallbackBody()
        if self.targetDirectoryPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("TargetDirectory", self.targetDirectoryPageCallbackBody) )

        if self.isAutoComponentSelectionPageCallback:
            self.__genComponentSelectionPageCallbackBody()
        if self.componentSelectionPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("ComponentSelection", self.componentSelectionPageCallbackBody) )

        if self.isAutoLicenseAgreementPageCallback:
            self.__genLicenseAgreementPageCallbackBody()
        if self.licenseAgreementPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("LicenseAgreement", self.licenseAgreementPageCallbackBody) )

        if self.isAutoStartMenuDirectoryPageCallback:
            self.__genStartMenuDirectoryPageCallbackBody()
        if self.startMenuDirectoryPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("StartMenuDirectory", self.startMenuDirectoryPageCallbackBody) )

        if self.isAutoReadyForInstallationPageCallback:
            self.__genReadyForInstallationPageCallbackBody()
        if self.readyForInstallationPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("ReadyForInstallation", self.readyForInstallationPageCallbackBody) )

        if self.isAutoPerformInstallationPageCallback:
            self.__genPerformInstallationPageCallbackBody()
        if self.performInstallationPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("PerformInstallation", self.performInstallationPageCallbackBody) )

        if self.isAutoFinishedPageCallback:
            self.__genFinishedPageCallbackBody()
        if self.finishedPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                ("Finished", self.finishedPageCallbackBody) )
        
    def __genControllerConstructorBody( self ):
        self.controllerConstructorBody = ""
        if self.isAutoPilotMode :   
            self.controllerConstructorBody += (
                QtIfwControlScript.__SILENT_CONSTRUCTOR_BODY
            )
                 
    def __genIntroductionPageCallbackBody( self ):
        self.introductionPageCallbackBody = ""
        if self.isAutoPilotMode :
            self.introductionPageCallbackBody += ( 
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            ) 
        if self.introductionPageCallbackBody == "" :
            self.introductionPageCallbackBody = None

    def __genTargetDirectoryPageCallbackBody( self ):
        self.targetDirectoryPageCallbackBody = ""
        if self.isAutoPilotMode :
            # TODO: auto target path logic (vs default)
            """
            gui.currentPageWidget().TargetDirectoryLineEdit.setText( "......" );
            """
            self.targetDirectoryPageCallbackBody += (
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            ) 
        if self.targetDirectoryPageCallbackBody == "" :
            self.targetDirectoryPageCallbackBody = None

    def __genComponentSelectionPageCallbackBody( self ):
        self.componentSelectionPageCallbackBody = ""        
        if self.isAutoPilotMode :
            # TODO: auto component selection logic (vs default)
            """
            var widget = gui.currentPageWidget();
            widget.deselectAll();
            widget.selectComponent("......");
            """
            self.componentSelectionPageCallbackBody += ( 
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            )
        if self.componentSelectionPageCallbackBody == "" :
            self.componentSelectionPageCallbackBody = None

    def __genLicenseAgreementPageCallbackBody( self ):
        self.licenseAgreementPageCallbackBody = ""
        if self.isAutoPilotMode :            
            self.licenseAgreementPageCallbackBody += (
                "gui.currentPageWidget().AcceptLicenseRadioButton.setChecked(true);\n" + 
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            ) 
        if self.licenseAgreementPageCallbackBody == "" :
            self.licenseAgreementPageCallbackBody = None

    def __genStartMenuDirectoryPageCallbackBody( self ):
        self.startMenuDirectoryPageCallbackBody = ""
        if self.isAutoPilotMode :
            self.startMenuDirectoryPageCallbackBody += ( 
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            )
        if self.startMenuDirectoryPageCallbackBody == "" :
            self.startMenuDirectoryPageCallbackBody = None

    def __genReadyForInstallationPageCallbackBody( self ):
        self.readyForInstallationPageCallbackBody = ""
        if self.isAutoPilotMode :
            self.readyForInstallationPageCallbackBody += (
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            )                
        if self.readyForInstallationPageCallbackBody == "" :
            self.readyForInstallationPageCallbackBody = None

    def __genPerformInstallationPageCallbackBody( self ):
        self.performInstallationPageCallbackBody = ""
        if self.isAutoPilotMode :
            self.performInstallationPageCallbackBody += (
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._NEXT_BUTTON ) 
            )
        if self.performInstallationPageCallbackBody == "" :
            self.performInstallationPageCallbackBody = None

    def __genFinishedPageCallbackBody( self ):
        self.finishedPageCallbackBody = ""
        if self.isAutoPilotMode :
            self.finishedPageCallbackBody += (                   
                QtIfwControlScript._getClickButton( 
                    QtIfwControlScript._FINISH_BUTTON ) 
            )
        if self.finishedPageCallbackBody == "" :
            self.finishedPageCallbackBody = None
            
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
    
    def __init__( self, pkgName,
                  shortcuts=[],                   
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.pkgName  = pkgName
        self.shortcuts = shortcuts

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
        self.__addShortcuts()
        if self.componentCreateOperationsBody == "" :
            self.componentCreateOperationsBody = None
        
    def __addShortcuts( self ):
        for shortcut in self.shortcuts :                
            if IS_WINDOWS:
                winOps=""
                if shortcut.exeName and shortcut.isAppShortcut :
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            STARTMENU_WIN_SHORTCUT, shortcut.exeName,
                            label=shortcut.productName )              
                if shortcut.exeName and shortcut.isDesktopShortcut:
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            DESKTOP_WIN_SHORTCUT, shortcut.exeName,
                            label=shortcut.productName ) 
                if winOps!="" :    
                    self.componentCreateOperationsBody += (             
                        '    if( systemInfo.kernelType === "winnt" ){\n' +
                        '%s\n    }' % (winOps,) )
            elif IS_MACOS:
                macOps = ""
                if shortcut.exeName and shortcut.isAppShortcut :
                    macOps += QtIfwPackageScript.__macAddShortcut(
                            APPS_MAC_SHORTCUT, shortcut.exeName,
                            shortcut.isGui, label=shortcut.productName )              
                if shortcut.exeName and shortcut.isDesktopShortcut:
                    macOps += QtIfwPackageScript.__macAddShortcut(
                            DESKTOP_MAC_SHORTCUT, shortcut.exeName,
                            shortcut.isGui, label=shortcut.productName )             
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
                            label=shortcut.productName,
                            pngPath=shortcut.pngIconResPath,
                            isGui=shortcut.isGui )                
                if shortcut.exeName and shortcut.isDesktopShortcut:
                    x11Ops += QtIfwPackageScript.__linuxAddDesktopEntry(
                            DESKTOP_X11_SHORTCUT, 
                            shortcut.exeName, shortcut.exeVersion,
                            label=shortcut.productName,
                            pngPath=shortcut.pngIconResPath,
                            isGui=shortcut.isGui )                               
                if x11Ops!="" :    
                    self.componentCreateOperationsBody += (             
                        '    if( systemInfo.kernelType === "linux" ){\n' +
                        '%s\n    }' % (x11Ops,) )                                

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
    def __init__( self, productName="@ProductName@", 
                  exeName=None, exeVersion="0.0.0.0",        
                  pngIconResPath=None, isGui=True ) :
        self.productName    = productName
        self.exeName        = exeName   
        self.isGui          = isGui
        self.exeVersion     = exeVersion        
        self.pngIconResPath = pngIconResPath        
        self.isAppShortcut     = True
        self.isDesktopShortcut = False

# -----------------------------------------------------------------------------                   
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
    if pkgIndex : del pkgs[ pkgIndex ]               

def mergeQtIfwPackages( pkgs, srcId, destId ):                
    srcPkg  = findQtIfwPackage( pkgs, srcId )
    destPkg = findQtIfwPackage( pkgs, destId )
    if not srcPkg or not destPkg:
        raise Exception( "Cannot merge QtIfw packages. " +
                         "Invalid id(s) provided." ) 
    mergeDirs( srcPkg.srcDirPath, destPkg.srcDirPath )
    destPkg.pkgScript.shortcuts.extend( 
        srcPkg.pkgScript.shortcuts )
    removeQtIfwPackage( pkgs, srcId )        
    return destPkg
    
# -----------------------------------------------------------------------------            
def buildInstaller( qtIfwConfig, isSilent ):
    ''' returns setupExePath '''
    __validateConfig( qtIfwConfig )        
    __initBuild( qtIfwConfig )    
    __addInstallerResources( qtIfwConfig )     
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
        if configXml.iconFilePath :
            iconFilePath = absPath( configXml.iconFilePath )
            if isFile( iconFilePath ):
                copyFile( iconFilePath,                       
                          joinPath( configXml.dirPath(), 
                                    basename( configXml.iconFilePath ) ) )
    ctrlScript = qtIfwConfig.controlScript
    if ctrlScript :
        print( "Adding installer control script..." )
        ctrlScript.debug()
        ctrlScript.write()                                      
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

def __buildSilentWrapper( qtIfwConfig ) :
    print( "Building silient wrapper executable...\n" )
    from distbuilder.master import PyToBinPackageProcess, ConfigFactory
    
    # On macOS, a "gui" .app must be build because that provides a .plist
    # and an application we can best manipulate via AppleScript
    
    srcSetupExeName   = util.normBinaryName( qtIfwConfig.setupExeName, isGui=True )    
    destSetupExeName  = util.normBinaryName( qtIfwConfig.setupExeName, isGui=False ) 
    nestedExeName     = util.normBinaryName( __NESTED_INSTALLER_NAME,  isGui=True )
    wrapperExeName    = __WRAPPER_INSTALLER_NAME
    wrapperPyName     = __WRAPPER_SCRIPT_NAME
    wrapperScript     = __silentWrapperScript( nestedExeName )
        
    cfgXml         = qtIfwConfig.configXml
                                               
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
                # a .app is a directory, so the "wrapper dir" must be peserved
                self.__nestedZipPath = toZipFile( nestedExeName, 
                                                  isWrapperDirIncluded=True ) 
            removeFromDir( wrapperPyName )
            with open( absPath( wrapperPyName ), 'w' ) as f: 
                f.write( wrapperScript )  
            
        def onPyInstConfig( self, cfg ):    
            if IS_MACOS: cfg.dataFilePaths   = [ self.__nestedZipPath ]
            else       : cfg.binaryFilePaths = [ absPath( nestedExeName ) ]
            
        def onFinalize( self ):
            removeFromDir( wrapperPyName )
            removeFromDir( nestedExeName ) 
            removeFromDir( self.__nestedZipPath )
            # TODO : add a standard option to avoid needing this mess
            # of moving the binary out of the sub directory here           
            tmpDir = renameInDir( (wrapperExeName, "__" + wrapperExeName) )
            normWrapperName = util.normBinaryName( wrapperExeName, isGui=False ) 
            moveToDir( joinPath( tmpDir, normWrapperName ) ) 
            removeFromDir( tmpDir )
            renameInDir( (normWrapperName, destSetupExeName) )
            #if IS_MACOS : self.__injectHidePropertyIntoApp( destSetupExeName )
                
        # On macOS enabling LSUIElement in the .plist will prevent 
        # showing the app icon in the dock when it is launched.  
        # Unfornately, no analogous property seems to hide it from 
        # the screen! (or least not this app, on recent versions of the os...)
        def __injectHidePropertyIntoApp( self, appPath ):    
            util._system( ( "/usr/libexec/PlistBuddy -c " +
                "'Add :LSUIElement bool true' {0}/Contents/Info.plist" ).format(
                absPath( appPath ) ) )
                    
    BuildProcess( configFactory ).run()
    return absPath( destSetupExeName )
    
def __silentWrapperScript( exeName ) :
    """
    Runs the exe from inside the PyInstaller MEIPASS directory,
    with elevated privileges, and hidden from view.  
    """
    
    COMMON_INIT = (
"""
WORK_DIR = sys._MEIPASS
EXE_NAME = "{0}"
ARGS     = ""
""").format( exeName )
        
    if IS_WINDOWS: return (
"""     
import os, sys, glob, time, ctypes

{0}

def runInstaller():
    shell32 = ctypes.windll.shell32        
    VERB    = "open" if shell32.IsUserAnAdmin() else "runas"
    SW_HIDE = 0 
    if sys.version_info[0]==2:
        VERB     = unicode(VERB)
        EXE_NAME = unicode(EXE_NAME)
        WORK_DIR = unicode(WORK_DIR)
        ARGS     = unicode(ARGS)    
    shell32.ShellExecuteW( None, VERB, EXE_NAME, ARGS, WORK_DIR, SW_HIDE )

def cleanUp():
    LOCK_FILE_PATTERN = "lockmyApp*.lock"
    while glob.glob( LOCK_FILE_PATTERN ): pass
    EXE_PATH = os.path.join( WORK_DIR, EXE_NAME )
    while os.path.exists( EXE_PATH ): 
        try: os.remove( EXE_PATH )
        except: pass
    time.sleep(2)    

runInstaller()
cleanUp()    

""").format( COMMON_INIT )

    if IS_LINUX : return ( 
"""
import os, subprocess, shlex
try: from subprocess import DEVNULL 
except ImportError: DEVNULL = open(os.devnull, 'wb')

{0}

def runInstaller():
    subprocess.check_call( shlex.split("sudo xvfb-run ./%s" % (EXE_NAME,)), 
                           cwd=WORK_DIR, stdout=DEVNULL, stderr=DEVNULL ) 

def installTempDependencies():    
    cleanUpCmds=[]
    try: 
        subprocess.check_call( shlex.split("xvfb-run -h"),
                               stdout=DEVNULL, stderr=DEVNULL )                                       
    except:     
        try: 
            subprocess.check_call( shlex.split("sudo apt-get install xvfb -y") )
            cleanUpCmds.append( "sudo apt-get remove xvfb -y" )
        except: 
            subprocess.check_call( shlex.split("sudo yum install Xvfb -y") )
            cleanUpCmds.append( "sudo yum remove xvfb -y" )
    return cleanUpCmds

def cleanUp( cmds ):
    for cmd in cmds: subprocess.check_call( shlex.split(cmd) )

cleanUpCmds = installTempDependencies()
runInstaller()
cleanUp( cleanUpCmds )

""").format( COMMON_INIT )

    if IS_MACOS : return ( 
"""
import os, sys, subprocess, shlex, zipfile, tempfile
try: from subprocess import DEVNULL 
except ImportError: DEVNULL = open(os.devnull, 'wb')

"""
+ COMMON_INIT +
"""
APP_PATH     = WORK_DIR + "/" + EXE_NAME    # os.path.join( WORK_DIR, EXE_NAME )
ZIP_PATH     = APP_PATH + ".zip" 
APP_BIN_DIR  = os.path.join( APP_PATH, "Contents/MacOS" )

# failed experiment abandoned, but not purged yet...
# (this only works by forcing the user into a manual 
#  System Perferrences update, as Apple revoked the 
#  only means of programmatically granting such...
#  Plus, it's doesn't work "perfectly" anyway...) 
PROCESS_NAME = os.path.splitext( EXE_NAME )[0]
RUN_APP_OFF_SCREEN_SCRIPT = (    
'''
do shell script "open %s"
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
''') % ( APP_PATH, PROCESS_NAME )

def extractAppFromZip():
    zipfile.ZipFile( ZIP_PATH, 'r' ).extractall( WORK_DIR )   
    BIN_PATH = os.path.join( APP_BIN_DIR, os.listdir( APP_BIN_DIR )[0] )
    os.chmod( BIN_PATH, 0o777 )

def runAppleScript( script ):
    scriptPath = tempfile.mktemp( suffix='.scpt' )
    with open( scriptPath, 'w' ) as f : f.write( script )
    ret = subprocess.call( ['osascript', scriptPath] ) 
    os.remove( scriptPath )
    if ret != 0 : raise RuntimeError( "AppleScript failed." )

def runInstaller():
    # failed experiment abandoned 
    #runAppleScript( RUN_APP_OFF_SCREEN_SCRIPT )
    subprocess.check_call( shlex.split("sudo open -W %s" % (EXE_NAME,)), 
                           cwd=WORK_DIR, stdout=DEVNULL, stderr=DEVNULL ) 

extractAppFromZip()
runInstaller()

""") 