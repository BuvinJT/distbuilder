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

__QT_IFW_AUTO_INSTALL_PY_SCRIPT_NAME = "__distbuilder-qt-ifw.py"
__QT_IFW_AUTO_INSTALL_Q_SCRIPT_NAME = "__distbuilder-qt-ifw.qs"

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

    TAB         = "    "
    NEW_LINE    = "\n" 
    END_LINE    = ";\n"
    START_BLOCK = "{\n"
    END_BLOCK   = "}\n"
    
    TRUE  = "true"
    FALSE = "false"
    
    PATH_SEP = '"\\\\"' if IS_WINDOWS else '"/"'  
    
    MAINTENANCE_TOOL_NAME  = '"%s"' % ( 
        util.normBinaryName( "maintenancetool", isGui=True ) )
    
    VERBOSE_CMD_SWITCH_ARG = "-v"    
    TARGET_DIR_KEY         = "TargetDir"
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
        
    __IS_INSTALLER   = "installer.isInstaller()"
    __IS_UNINSTALLER = "installer.isUninstaller()"
        
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

    __YES_NO_POPUP_TMPL = ( 
        'var %s = QMessageBox.question("yesnobox", "%s", ' +
            '"%s", QMessageBox.Yes|QMessageBox.No );\n' )                                  
                                  
    __YES_NO_CANCEL_POPUP_TMPL = ( 
        'var %s = QMessageBox.question("yesnocancelbox", "%s", ' +
            '"%s", QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel );\n' )
    
    __VALUE_TMPL      = "installer.value( %s, %s )"
    __VALUE_LIST_TMPL = "installer.values( %s, %s )"
    __SET_VALUE_TMPL  = "installer.setValue( %s, %s )"

    __FILE_EXITS_TMPL = "installer.fileExists( %s )"

    @staticmethod        
    def _autoQuote( value, isAutoQuote ):                  
        return '"%s"' % (value,) if isAutoQuote else value 

    @staticmethod        
    def log( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__LOG_TMPL % (
            _QtIfwScript._autoQuote( msg, isAutoQuote ),)

    @staticmethod        
    def debugPopup( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__DEBUG_POPUP_TMPL % (
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
    def targetDir(): 
        return _QtIfwScript.lookupValue( _QtIfwScript.TARGET_DIR_KEY )

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
    def ifInstalling( isMultiLine=False ):
        return 'if( %s )%s\n%s' % (
            _QtIfwScript.__IS_INSTALLER,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod
    def ifMaintenanceTool( isMultiLine=False ):
        return 'if( %s )%s\n%s' % (
            _QtIfwScript.__IS_UNINSTALLER,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def yesNoPopup( msg, title="Question", resultVar="result" ):                  
        return _QtIfwScript.__YES_NO_POPUP_TMPL % ( title, msg, resultVar ) 

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
    def fileExists( path, isAutoQuote=True ):                  
        return _QtIfwScript.__FILE_EXITS_TMPL % (
            _QtIfwScript._autoQuote( path, isAutoQuote ),) 

    @staticmethod        
    def ifFileExists( path, isAutoQuote=True, isMultiLine=False ):   
        return 'if( %s )%s\n%s' % (
            _QtIfwScript.fileExists( path, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
        
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

    __CONTROLER_CALLBACK_FUNC_TMPLT = (
"""
Controller.prototype.%s = function(){
    %s
}\n
""" )

    __CONTROLER_CONNECT_TMPLT = ( 
        "%s.connect(this, Controller.prototype.%s);\n" ) 

    __CURRENT_PAGE_WIDGET = "gui.currentPageWidget()"
    __PAGE_WIDGET_VAR_TMPLT = "    var %s = gui.currentPageWidget();\n"
            
    __CLICK_BUTTON_TMPL       = "gui.clickButton(%s);\n"
    __CLICK_BUTTON_DELAY_TMPL = "gui.clickButton(%s, %d);\n"
    
    __SET_CHECKBOX_STATE_TMPL = (
        "gui.currentPageWidget().%s.setChecked(%s);\n" )

    __SET_TEXT_TMPL = (
        "gui.currentPageWidget().%s.setText(%s);\n" )
    
    NEXT_BUTTON   = "buttons.NextButton"
    BACK_BUTTON   = "buttons.BackButton"
    CANCEL_BUTTON = "buttons.CancelButton"
    FINISH_BUTTON = "buttons.FinishButton"
    
    TARGET_DIR_EDITBOX       = "TargetDirectoryLineEdit"
    START_MENU_DIR_EDITBOX   = "StartMenuPathLineEdit"
    ACCEPT_EULA_RADIO_BUTTON = "AcceptLicenseRadioButton"
    RUN_PROGRAM_CHECKBOX     = "RunItCheckBox"
                                    
    @staticmethod        
    def currentPageWidget():                
        return QtIfwControlScript.__CURRENT_PAGE_WIDGET            

    @staticmethod        
    def assignPageWidgetVar( varName="page" ):                
        return QtIfwControlScript.__PAGE_WIDGET_VAR_TMPLT % (varName,)            

    @staticmethod        
    def clickButton( buttonName, delayMillis=None ):                
        return ( 
            QtIfwControlScript.__CLICK_BUTTON_DELAY_TMPL 
                % (buttonName, delayMillis)
            if delayMillis else
            QtIfwControlScript.__CLICK_BUTTON_TMPL 
                % (buttonName,) )

    # Note: checkbox controls also work on radio buttons
    @staticmethod        
    def enableCheckBox( checkboxName ):                
        return QtIfwControlScript.__SET_CHECKBOX_STATE_TMPL % ( 
                checkboxName, _QtIfwScript.TRUE )

    @staticmethod        
    def disableCheckBox( checkboxName ):                
        return QtIfwControlScript.__SET_CHECKBOX_STATE_TMPL % ( 
                checkboxName, _QtIfwScript.FALSE )

    @staticmethod        
    def setCheckBox( checkboxName, boolean ):                
        return QtIfwControlScript.__SET_CHECKBOX_STATE_TMPL % ( 
                checkboxName, boolean )

    @staticmethod        
    def setText( controlName, text, isAutoQuote=True ):                
        return QtIfwControlScript.__SET_TEXT_TMPL % ( 
                controlName, _QtIfwScript._autoQuote( text, isAutoQuote ) )
    
    def __init__( self,
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.controllerGlobals = None
        self.isAutoGlobals = True
        
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

        self.__autoPilotSlots = {}
        self.registerAutoPilotSlot( 
            'installer.installationFinished', 'onInstallFinished', 
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 
        self.registerAutoPilotSlot( 
            'installer.uninstallationFinished', 'onUninstallFinished',
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 

    def registerAutoPilotSlot( self, signalName, slotName, slotBody ) :
        self.__autoPilotSlots[signalName] = (slotName, slotBody)
                                                                
    def _generate( self ) :        
        self.script = ""
        
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

        for _, (funcName, funcBody) in six.iteritems( self.__autoPilotSlots ):    
            self.script += ( 
                QtIfwControlScript.__CONTROLER_CALLBACK_FUNC_TMPLT %
                (funcName, funcBody) )

    def __genGlobals( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK
        self.controllerGlobals = (
            'function execute( binPath, args ) ' + SBLK +
            TAB + 'var cmd = "\\"" + binPath + "\\""' + END +
            TAB + 'for( i=0; i < args.length; i++ )' + NEW +
            (2*TAB) + 'cmd += (" " + args[i])' + END +
            TAB + _QtIfwScript.log( '"Executing: " + cmd', isAutoQuote=False ) +
            TAB + 'return installer.execute( binPath, args )' + END +
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
            'function clearErrorLog() ' + SBLK +
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
                TAB + 'if( path=="" || ' + _QtIfwScript.fileExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("Clear error log failed. (file exists)")' + END +
                TAB + _QtIfwScript.log( '"Cleared error log: " + path', isAutoQuote=False ) +                                                                                                                                        
            EBLK + NEW +                           
            'function writeErrorLog( msg ) ' + SBLK +
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
                TAB + 'if( path=="" || !' + _QtIfwScript.fileExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
                (2*TAB) + 'throw new Error("Write error log failed. (file does not exists)")' + END +
                TAB + _QtIfwScript.log( '"Wrote error log to: " + path', isAutoQuote=False ) +                                                                                                
            EBLK + NEW +                                                 
            'function silentAbort( msg ) ' + SBLK +
                TAB + 'writeErrorLog( msg )' + END +
                TAB + 'throw new Error( msg )' + END +                    
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
        self.controllerGlobals += (
            'function toMaintenanceToolPath( dir ) ' + SBLK +
                TAB + 'return dir + ' + _QtIfwScript.PATH_SEP + ' + ' +
                    _QtIfwScript.MAINTENANCE_TOOL_NAME + END + 
            EBLK + NEW +            
            'function maintenanceToolExists( dir ) ' + SBLK +
                TAB + 'return ' + _QtIfwScript.fileExists( 
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
            'function targetExists() ' + SBLK +
                (TAB + 'if( isOsRegisteredProgram() ) ' + SBLK +
                 (2*TAB)  + _QtIfwScript.log('The program is OS registered.') +
                 (2*TAB) + 'return true' + END + 
                TAB + EBLK                  
                if IS_WINDOWS else '') +
                TAB + _QtIfwScript.ifCmdLineArg( 
                    _QtIfwScript.TARGET_DIR_CMD_ARG, isMultiLine=True ) +
                    'if( cmdLineTargetExists() )'  + SBLK +
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
            'function removeTarget() ' + SBLK +
                TAB + _QtIfwScript.log('Removing existing installation...') +  
                TAB + 'var args=[ "-v", ' +                     
                    '"' + _QtIfwScript.AUTO_PILOT_CMD_ARG + '=' +
                    _QtIfwScript.TRUE + '" ' + 
                    ', "' + _QtIfwScript.MAINTAIN_MODE_CMD_ARG + '=' + 
                    _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL + '" ' 
                    "]" + END +
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
                (2*TAB) + 'if( !targetExists() ) break' + END +
                (2*TAB) + _QtIfwScript.log('Waiting for uninstall to finish...') +                
                (2*TAB) + 'sleep( 1 )' + END +                
                TAB + EBLK +
                TAB + 'if( targetExists() ) ' + NEW +
                (2*TAB) + 'silentAbort("Failed to removed the program.")' + END +
                TAB + _QtIfwScript.log('Successfully removed the program.') +
            EBLK + NEW +
            'function managePriorInstallation() ' + SBLK +
                TAB + "if( targetExists() ) " + SBLK +
                (2*TAB) + 'switch (' + _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG ) + ')' + SBLK +
                (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_FAIL + '":' + NEW +
                    (3*TAB) + 'silentAbort("This program is already installed.")' + END + 
                (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_REMOVE + '":' + NEW + 
                    (3*TAB) + 'removeTarget()' + END +
                    (3*TAB) + 'break' + END +
                (2*TAB) + 'default:' + NEW +
                    (2*TAB) + _QtIfwScript.switchYesNoCancelPopup(  
                  'This program is already installed. ' +
                  'Would you like to uninstall it first?', 
                  title='Uninstall first?', 
                  resultVar="uninstallChoice", 
                  onYes='removeTarget();', 
                  onNo="// proceed without action...",
                  onCancel='silentAbort("This program is already installed.");'
                  ) +
                  (3*TAB) + 'break' + END +                  
                  EBLK +           
                EBLK +                         
            EBLK + NEW                                                              
            )
        
    def __genControllerConstructorBody( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK        
        self.controllerConstructorBody = 'clearErrorLog()' + END  
        self.controllerConstructorBody += _QtIfwScript.ifCmdLineSwitch( 
                _QtIfwScript.AUTO_PILOT_CMD_ARG, isMultiLine=True )             
        for signalName, (slotName, _) in six.iteritems( self.__autoPilotSlots ):    
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                (signalName, slotName) )
        self.controllerConstructorBody += (        
                _QtIfwScript.ifInstalling() + 
                    'managePriorInstallation()' + END +
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
            QtIfwControlScript.assignPageWidgetVar( "page" ) +            
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
                QtIfwControlScript.enableCheckBox( 
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
                    QtIfwControlScript.NEXT_BUTTON ) 
            )                

    def __genPerformInstallationPageCallbackBody( self ):
        self.performInstallationPageCallbackBody = (
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
            )

    def __genFinishedPageCallbackBody( self ):
        self.finishedPageCallbackBody = (                
            _QtIfwScript.ifCmdLineArg( 
                _QtIfwScript.RUN_PROGRAM_CMD_ARG ) +               
                _QtIfwScript.TAB + QtIfwControlScript.setCheckBox( 
                    QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                        _QtIfwScript.cmdLineSwitchArg(
                            _QtIfwScript.RUN_PROGRAM_CMD_ARG ) ) + 
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
def installQtIfw( installerPath, targetPath=None ):
    if targetPath is None: 
        qtDefaultDir = joinPath( util._userHomeDirPath(), "Qt" )
        ifwVer = __QtIfwInstallerVersion( installerPath )
        dirName = "QtIFW" if ifwVer is None else "QtIFW-%s" % (ifwVer,)
        targetPath = joinPath( qtDefaultDir, dirName ) 
    ifwQScriptPath = __generateQtIfwInstallerQScript()
    ifwPyScriptPath = __generateQtIfwInstallPyScript( 
        installerPath, targetPath, ifwQScriptPath )    
    runPy( ifwPyScriptPath )
    removeFile( ifwPyScriptPath )
    removeFile( ifwQScriptPath )

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
    ctrlScript = qtIfwConfig.controlScript
    
    if ctrlScript and configXml: 
        configXml.ControlScript = ctrlScript.fileName         
            
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
                # a .app is a directory, so the "wrapper dir" must be peserved
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
            dirName = basename( self.binDir )
            binName = basename( self.binPath )       
            tmpDir = renameInDir( (dirName, "__" + dirName) )             
            moveToDir( joinPath( tmpDir, binName ) ) 
            removeFromDir( tmpDir )
            self.binPath = renameInDir( (binName, destSetupExeName) )
            self.binDir = dirPath( self.binPath )            
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
    
def __silentQtIfwScript( exeName, componentList=[],
                         isQtIfwInstaller=False, scriptPath=None,
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

    if isQtIfwInstaller :
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

ARGS = ["-v","--script", "{2}", "target={9}"]
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
    , wrkDir
    , scriptPath 
    , imports             
    , IS_WINDOWS  
    , helpers
    , preProcess
    , createInstallerProcess
    , cleanUp
    , targetDir
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
        args.append( "{8}=%s" % (wrapperArgs.target,) )
    
    if IS_WINDOWS :      
        if wrapperArgs.startmenu is not None : 
            args.append( "{9}=%s" % (wrapperArgs.startmenu,) )
    
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

def __generateQtIfwInstallPyScript( installerPath, targetPath, ifwScriptPath ):
    installerDir, installerName = splitPath( installerPath ) 
    script = __silentQtIfwScript( 
        installerName, isQtIfwInstaller=True, 
        scriptPath=ifwScriptPath, wrkDir=installerDir,
        targetDir=targetPath )    
    filePath = joinPath( tempDirPath(), __QT_IFW_AUTO_INSTALL_PY_SCRIPT_NAME )
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
    filePath = joinPath( tempDirPath(), __QT_IFW_AUTO_INSTALL_Q_SCRIPT_NAME )
    #print( "Generating QScript: %s" % (filePath,) )
    #print( "\n%s\n" % (script,) )
    with open( filePath, 'w' ) as f: f.write( script ) 
    return filePath 

def __QtIfwInstallerVersion( installerPath ):
    version = util._subProcessStdOut( 
        [installerPath, "--framework-version"] )
    # TODO: validate expected format returned, return None if bad
    return version    
    