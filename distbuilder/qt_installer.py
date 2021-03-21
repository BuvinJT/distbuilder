from distbuilder import util
from distbuilder.util import * # @UnusedWildImport

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
QT_IFW_SILENT_DEBUG_SWITCH = '-d'
_KEEP_TEMP_SWITCH = "_keeptemp"
_SILENT_FORCED_ARGS = ["-f"]
_LOUD_FORCED_ARGS   = ["auto=true", "onexist=remove"]
_DEBUG_SCRIPTS_ARGS = ["_keeptemp=true"]

__BIN_SUB_DIR = "bin"
__QT_IFW_CREATOR_EXE_NAME    = util.normBinaryName( "binarycreator" )
__QT_IFW_CREATOR_OFFLINE_SWITCH = "--offline-only"

__QT_IFW_ARCHIVEGEN_EXE_NAME = util.normBinaryName( "archivegen" )
_QT_IFW_ARCHIVE_EXT = ".7z"

__QT_IFW_UNINSTALL_EXE_NAME = util.normBinaryName( "Uninstaller", isGui=True )
__QT_IFW_AUTO_INSTALL_PY_SCRIPT_NAME   = "__distb-install-qt-ifw.py"
__QT_IFW_AUTO_UNINSTALL_PY_SCRIPT_NAME = "__distb-uninstall-qt-ifw.py"
__QT_IFW_UNATTENDED_SCRIPT_NAME    = "__distb-unattended-qt-ifw.qs"

__WRAPPER_SCRIPT_NAME = "__installer.py"
__WRAPPER_INSTALLER_NAME = "wrapper-installer" 
__NESTED_INSTALLER_NAME  = "hidden-installer"

ADJANCENT_WIN_SHORTCUT         = 0
STARTMENU_WIN_SHORTCUT         = 1
DESKTOP_WIN_SHORTCUT           = 2
THIS_USER_STARTUP_WIN_SHORTCUT = 3
ALL_USERS_STARTUP_WIN_SHORTCUT = 4

ADJANCENT_MAC_SHORTCUT = 0
APPS_MAC_SHORTCUT      = 1
DESKTOP_MAC_SHORTCUT   = 2             

ADJANCENT_X11_SHORTCUT = 0                
APPS_X11_SHORTCUT      = 1
DESKTOP_X11_SHORTCUT   = 2

SHORTCUT_WIN_MINIMIZED = 7

QT_IFW_ASKPASS_KEY = "askpass"
QT_IFW_ASKPASS_PLACEHOLDER = "[%s]" % (QT_IFW_ASKPASS_KEY,)
QT_IFW_ASKPASS_TEMP_FILE_PATH = "/tmp/{0}.path".format( QT_IFW_ASKPASS_KEY )

QT_IFW_UNDEF_VAR_VALUE = "undef"

QT_IFW_DYNAMIC_SYMBOL = "@"

QT_IFW_ROOT_DIR      = "@RootDir@"
QT_IFW_TARGET_DIR    = "@TargetDir@"
QT_IFW_HOME_DIR      = "@HomeDir@" 
QT_IFW_DESKTOP_DIR   = ("@DesktopDir@" if IS_WINDOWS else
                        "%s/%s" % (QT_IFW_HOME_DIR,"Desktop") ) # Valid on macOS and Ubuntu at least (other Linux desktops?)
QT_IFW_APPS_DIR      = "@ApplicationsDir@"

QT_IFW_INSTALLER_DIR      = "@InstallerDirPath@"
QT_IFW_INTALLER_PATH      = "@InstallerFilePath@"   

_QT_IFW_DEFAULT_TARGET_DIR   = "DefaultTargetDir"   # CUSTOM!
_QT_IFW_SCRIPTS_DIR          = "ScriptsDir"         # CUSTOM!
_QT_IFW_INSTALLER_TEMP_DIR   = "InstallerTempDir"   # CUSTOM!
_QT_IFW_MAINTENANCE_TEMP_DIR = "MaintenanceTempDir" # CUSTOM!

_QT_IFW_VAR_TMPLT = "@%s@"

QT_IFW_DEFAULT_TARGET_DIR   = _QT_IFW_VAR_TMPLT % (_QT_IFW_DEFAULT_TARGET_DIR,)   # CUSTOM!
QT_IFW_SCRIPTS_DIR          = _QT_IFW_VAR_TMPLT % (_QT_IFW_SCRIPTS_DIR,)          # CUSTOM! 
QT_IFW_INSTALLER_TEMP_DIR   = _QT_IFW_VAR_TMPLT % (_QT_IFW_INSTALLER_TEMP_DIR,)   # CUSTOM!
QT_IFW_MAINTENANCE_TEMP_DIR = _QT_IFW_VAR_TMPLT % (_QT_IFW_MAINTENANCE_TEMP_DIR,) # CUSTOM!

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
QT_IFW_LICENSE_PAGE    = "LicenseCheck"
QT_IFW_START_MENU_PAGE = "StartMenuSelection"
QT_IFW_READY_PAGE      = "ReadyForInstallation"
QT_IFW_INSTALL_PAGE    = "PerformInstallation"
QT_IFW_FINISHED_PAGE   = "InstallationFinished"

_QT_IFW_INTRO_PAGE_CALLBACK_NAME      = "Introduction"
_QT_IFW_TARGET_DIR_PAGE_CALLBACK_NAME = "TargetDirectory"
_QT_IFW_COMPONENTS_PAGE_CALLBACK_NAME = "ComponentSelection"
_QT_IFW_LICENSE_PAGE_CALLBACK_NAME    = "LicenseAgreement"
_QT_IFW_START_MENU_PAGE_CALLBACK_NAME = "StartMenuDirectory"
_QT_IFW_READY_PAGE_CALLBACK_NAME      = "ReadyForInstallation"
_QT_IFW_INSTALL_PAGE_CALLBACK_NAME    = "PerformInstallation"
_QT_IFW_FINISHED_PAGE_CALLBACK_NAME   = "Finished"

QT_IFW_REPLACE_PAGE_PREFIX="Replace"

(QT_IFW_PRE_INSTALL, QT_IFW_POST_INSTALL) = range(2)

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

_PAGE_NAME_PLACHOLDER   = "[PAGE_NAME]"
_WIDGET_NAME_PLACHOLDER = "[WIDGET_NAME]"

_ENV_TEMP_DIR     = "%temp%" if IS_WINDOWS else "/tmp"
_QT_IFW_TEMP_NAME = "__distbuilder-qtifw"

_REMOVE_TARGET_KEY = "__removeTarget"

_QT_IFW_WATCH_DOG_SUFFIX = "-watchdog"
_QT_IFW_WATCH_DOG_EXT    = ".vbs" if IS_WINDOWS else ""

_QT_IFW_TEMP_DATA_EXT = ".dat"

QT_IFW_DYNAMIC_PATH_VARS = [
      "TargetDir"
    , "DefaultTargetDir"
    , "RootDir" 
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
    , "ScriptsDir"
    , "InstallerDirPath" 
    , "InstallerFilePath" 
]

QT_IFW_DYNAMIC_VARS = QT_IFW_DYNAMIC_PATH_VARS + [
      "ProductName"
    , "ProductVersion"
    , "Title"
    , "Publisher"
    , "Url"
    , "os"
]

_RETAINED_RESOURCE_SUBDIR = 'maintenanceResources'
_RETAINED_RESOURCE_DIR = '"%s/%s"' % (QT_IFW_TARGET_DIR,_RETAINED_RESOURCE_SUBDIR)
_TEMP_RESOURCE_SUBDIR = "resources"
_TEMP_RESOURCE_DIR = '__installerTempPath() + "/%s"' % (_TEMP_RESOURCE_SUBDIR,)

_WRAPPER_MSG_PREFIX = "__MSG__:"
_REBOOT_MSG = "Please reboot now to complete the installation."

_SCRIPT_LINE1_COMMENT = "// ------------ LINE 1 ------------ \n\n"

# don't use back slash on Windows!
def joinPathQtIfw( head, tail ): return "%s/%s" % ( head, tail )

def qtIfwDynamicValue( name ): return "@%s@" % (name,)
    
def qtIfwOpDataPath( rootFileName ): 
    return joinExt( joinPathQtIfw( QT_IFW_SCRIPTS_DIR, rootFileName ), 
                    _QT_IFW_TEMP_DATA_EXT )

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

    # if the element is already present and overwrite is False, NOTHING will be modified                  
    def addUiElements( self, uiElements, isOverWrite=True ):
    
        def findOwnerPackage( ui ):
            for pkg in self.packages :
                interfaces =( pkg.uiPages if isinstance( ui, QtIfwUiPage ) else 
                              pkg.widgets )               
                for interface in interfaces:
                    if interface==ui: return pkg
            return None            
        
        def add( pkg, ui ):            
            page   = ui if isinstance( ui, QtIfwUiPage ) else None
            widget = ui if isinstance( ui, QtIfwWidget ) else None    
            if page:                     
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
                                self.controlScript.uiPages.insert( i, page )
                                break
                # if the page wasn't inserted into the middle of the list, append it                     
                if not isInserted:    
                    pkg.uiPages.append( page )           
                    pkg.pkgScript.uiPages.append( page )        
                    self.controlScript.uiPages.append( page )
            elif widget:
                # items must unique and sorted
                sortAttr1 = "pageName"
                sortAttr2 = "position"                         
                sortAttr3 = "name"
                pkg.widgets.append( widget )
                pkg.widgets = sorted(list(set(pkg.widgets)),
                    key=attrgetter(sortAttr1, sortAttr2, sortAttr3) )
                # a copy here might be faster than another append + sort?
                pkg.pkgScript.widgets = deepcopy( pkg.widgets )
                # can't just copy this from the package, because it is a 
                # different (encompassing) collection
                self.controlScript.widgets.append( widget )
                self.controlScript.widgets = sorted(list(set(
                    self.controlScript.widgets)),
                    key=attrgetter(sortAttr1, sortAttr2, sortAttr3) )                            
            # order doesn't matter for this list, but the items should be unique
            pkg.pkgXml.UserInterfaces.append( ui.fileName() )
            pkg.pkgXml.UserInterfaces = list(set(pkg.pkgXml.UserInterfaces))
    
        def overwrite( pkg, ui ):                    
            page   = ui if isinstance( ui, QtIfwUiPage ) else None
            widget = ui if isinstance( ui, QtIfwWidget ) else None            
            if page:          
                # order must be preserved here 
                pkg.uiPages = [ page if p.name==page.name else p 
                                for p in pkg.uiPages ]        
                pkg.pkgScript.uiPages = [ page if p.name==page.name else p 
                                          for p in pkg.pkgScript.uiPages ]
                self.controlScript.uiPages = [ page if p.name==page.name else p 
                                               for p in self.controlScript.uiPages ]
                # order doesn't matter for this list, but the items should be unique
                pkg.pkgXml.UserInterfaces.append( ui.fileName() )
                pkg.pkgXml.UserInterfaces = list(set(pkg.pkgXml.UserInterfaces))                                             
            elif widget:
                # there is no difference in how to add vs overwrite a widget! 
                add( pkg, widget )                                                     
                            
        if uiElements is None: return
        if self.packages is None or len(self.packages)==0: return
        if self.controlScript is None: return        
        if not isinstance( uiElements, list ): uiElements = [uiElements]

        # For each ui element to add:
        # Search for a package which already "owns" (contains) the ui
        # and then overwrite that ui, if that option is enabled. Else,
        # simply do nothing - leaving the original definition in place. 
        # If the ui is not found, just arbitrarily inject it into the 
        # first package, as that owner has no functional significance!                  
        for ui in uiElements:
            pkg = findOwnerPackage( ui )
            if pkg:
                if isOverWrite: overwrite( pkg, ui )
            else: add( self.packages[0], ui )       

    def addLicense( self, licensePath, name="End User License Agreement" ): 
        try:
            if licensePath is not None:
                injectIndex=None 
                for i, p in enumerate( self.packages ):
                    if p.pkgXml.Virtual or p.pkgXml.ForcedInstallation:
                        injectIndex = i
                        break    
                    elif p.pkgXml.Default: 
                        if not injectIndex: injectIndex = i              
                if not injectIndex: injectIndex=0 
                self.packages[injectIndex].licenses[name] = licensePath                    
        except: pass
        try:        
            for p in self.packages:
                if len( p.licenses ) > 0:
                    self.controlScript._isLicenseRequired = True
                    break        
        except: pass
        
    # cleans up and shuffles around resources per some complicated design 
    # details a client should not have to know about and deal with
    def _scrubEmbeddedResources( self ): 
    
        def isScriptFound( script, resources ):        
            if not script or not resources: return
            for res in resources:
                if isinstance( res, ExecutableScript ):
                    if res.rootName == script.rootName: return True
            return False

        def addResource( res, resources ):        
            try: resources.append( res )
            except: resources = [res]
    
        def addMaintenanceToolResources( pkg ):
            try:
                for exOp in pkg.pkgScript.externalOps:
                    # uninstall scripts must be added to Maintenance Tool resources
                    if isinstance( exOp.uninstScript, ExecutableScript ):
                        if not isScriptFound( exOp.uninstScript, 
                            self.controlScript._maintenanceToolResources ):
                            addResource( exOp.uninstScript, 
                                self.controlScript._maintenanceToolResources )         
                    for resScript in exOp.uninstResourceScripts:
                        if isinstance( resScript, ExecutableScript ):
                            if not isScriptFound( resScript, 
                                self.controlScript._maintenanceToolResources ):
                                addResource( resScript, 
                                    self.controlScript._maintenanceToolResources )                    
            except: pass
    
        if self.packages is None or len(self.packages)==0: return
        if self.controlScript is None: return        
        for pkg in self.packages:
            if not isinstance( pkg, QtIfwPackage ) : continue
            addMaintenanceToolResources( pkg )

# -----------------------------------------------------------------------------    
class _QtIfwXmlElement( ET.Element ):                #attrib={}
    def __init__( self, tag, text=None, parent=None, attrib=None, **extra ):
        ET.Element.__init__( self, tag, attrib if attrib else {}, **extra )
        if text:
            if   isinstance(text, bool): text = str(text)
            elif isinstance(text, date): text = text.isoformat() 
            self.text = text
        if parent is not None: parent.append( self )                                                        

# -----------------------------------------------------------------------------
@add_metaclass( ABCMeta ) 
class _QtIfwXml:

    __HEADER = '<?xml version="1.0" encoding="UTF-8"?>'

    def __init__( self, rootTag, tags ) :
        self.rootTag       = rootTag
        self.tags          = tags 
        self.otherElements = {}
        
    def __str__( self ) :        
        root = _QtIfwXmlElement( self.rootTag )
        for k, v in iteritems( self.__dict__ ) :
            if k in self.tags and v is not None : 
                _QtIfwXmlElement( k, str(v), root )                                        
        for k, v in iteritems( self.otherElements ) : 
            _QtIfwXmlElement( k, str(v), root )
        self.addCustomTags( root )    
        xml = ET.tostring( root )        
        return _QtIfwXml.__HEADER + (xml if PY2 else xml.decode()) 

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

    class WizardStyle: AERO, MODERN, MAC, CLASSIC = range(4)
    DEFAULT_WIZARD_STYLE=( WizardStyle.MODERN  if IS_LINUX else
                           WizardStyle.MAC     if IS_MACOS else
                           WizardStyle.AERO ) #if IS_WINDOWS 
    _WizardStyles = { WizardStyle.AERO    : "Aero"
                    , WizardStyle.MODERN  : "Modern" 
                    , WizardStyle.MAC     : "Mac"
                    , WizardStyle.CLASSIC : "Classic"
                    }
    
    __DIR_TMPLT  = "%s/config"
    __PATH_TMPLT = __DIR_TMPLT + "/config.xml"
    __ROOT_TAG   = "Installer"
    __TAGS       = [ "Name"
                   , "Version"
                   , "Publisher"
                   , "InstallerApplicationIcon"
                   , "Title"
                   , "TitleColor"
                   , "TargetDir"
                   , "StartMenuDir"             
                   , "RunProgram" # RunProgramArguments added separately...
                   , "RunProgramDescription"
                   , "ControlScript"
                   , "WizardStyle"              
                   , "WizardDefaultWidth"    
                   , "WizardDefaultHeight"                      
                   , "Logo"
                   , "Banner"   # Questionable functionality...                              
                   , "ProductUrl"           
                   #, "DisableAuthorizationFallback" # Does not work?!         
                   ]
    __RUN_ARGS_TAG = "RunProgramArguments"
    __ARG_TAG      = "Argument"
        
    __RUN_PROG_DESCR_TMPLT = "Run %s now."    
                         
    # QtIfwConfigXml
    def __init__( self, name, version, publisher, 
                  iconFilePath=None,                   
                  controlScriptName=None,
                  primaryContentExe=None, isPrimaryExeGui=True,
                  primaryExeWrapper=None,
                  companyTradeName=None,
                  wizardStyle=None, 
                  logoFilePath=None, bannerFilePath=None ) :
        _QtIfwXml.__init__( self, QtIfwConfigXml.__ROOT_TAG, 
                            QtIfwConfigXml.__TAGS )
       
        self.primaryContentExe = ( 
            util.normBinaryName( primaryContentExe, 
                                 isGui=isPrimaryExeGui )
            if primaryContentExe else None )
        self.primaryExeWrapper=primaryExeWrapper
        self.runProgramArgList = None

        self.companyTradeName = ( companyTradeName if companyTradeName 
                                  else publisher.replace(".","") )        
        if IS_LINUX :
            # qt installer does not support icon embedding in Linux
            # TODO: use InstallerWindowIcon 
            iconRootName = self.iconFilePath = None
        else :    
            self.iconFilePath = ( None if iconFilePath is None else 
                                  normIconName( iconFilePath, 
                                                isPathPreserved=True ) )        
            try:    iconRootName = rootFileName( iconFilePath )
            except: iconRootName = None
       
        wizardStyleValue = QtIfwConfigXml._WizardStyles.get( 
                                wizardStyle, None )

        if( logoFilePath and 
            wizardStyle != QtIfwConfigXml.WizardStyle.CLASSIC and
            wizardStyle != QtIfwConfigXml.WizardStyle.MODERN ):
            printErr( "WARNING: Installer Logo is only applied in "
                      "CLASSIC or MODERN styles!" )        
        self.logoFilePath = logoFilePath
        try:    logoBaseName = baseFileName(logoFilePath)
        except: logoBaseName = None        
        
        if bannerFilePath and wizardStyle != QtIfwConfigXml.WizardStyle.MODERN:
            printErr( "WARNING: Installer Banner is only applied in "
                      "MODERN style!" )
        self.bannerFilePath = bannerFilePath
        try:    bannerBaseName = baseFileName(bannerFilePath)
        except: bannerBaseName = None

        self.Name                     = name
        self.Version                  = version
        self.Publisher                = publisher
        self.InstallerApplicationIcon = iconRootName
                 
        self.Title                    = None # defaults to name (+ "Setup")       
        self.TitleColor               = None # HTML color code, such as "#88FF33"
                        
        self.ControlScript            = controlScriptName
        
        self.TargetDir                = None        
        self.StartMenuDir             = None # Windows only of course
        
        self.RunProgram               = None
        self.RunProgramDescription    = None

        self.WizardStyle              = wizardStyleValue
        self.WizardDefaultWidth       = None    
        self.WizardDefaultHeight      = None
        self.Logo                     = logoBaseName
        self.Banner                   = bannerBaseName  # TODO: resolve size issues       
        self.ProductUrl               = None # Appears on Windows on the Control Panel Programs List, yet to see anywhere else...

        # This doesn't appear to work... so
        # custom scripting is also in place to enforce this!        
        #self.DisableAuthorizationFallback = True # Set to true if the installation should not ask users to run the authorization fallback in case of authorization errors. Instead abort the installation immediately.

        # TODO
        #self.InstallerWindowIcon   (vs InstallerApplicationIcon?) Filename for a custom window icon in PNG format for the Installer application.
        #self.StyleSheet    Set the stylesheet file.

        # TODO 
        #self.MaintenanceToolName    (will cause conflicts with existing custom code) Filename of the generated maintenance tool. Defaults to maintenancetool. The platform-specific executable file extension is appended.
        #self.MaintenanceToolIniFile    Filename for the configuration of the generated maintenance tool. Defaults to MaintenanceToolName.ini.

        # TODO
        #self.WizardShowPageList    Set to false if the widget listing installer pages on the left side of the wizard should not be shown. Defaults to true. If visible, this widget hides QWizard::WatermarkPixmap on QWizard::ClassicStyle and QWizard::ModernStyle, and QWizard::BackgroundPixmap on QWizard::MacStyle.
        #self.Watermark    Filename for a watermark used as QWizard::WatermarkPixmap. If <WizardShowPageList> is set to true, the watermark is hidden.
        #self.Background    Filename for an image used as QWizard::BackgroundPixmap (only used by MacStyle). If <WizardShowPageList> is set to true, the background is hidden.
        #self.PageListPixmap    Filename for an image shown on top of installer page list. The image is shown only if <WizardShowPageList> is also set to true.
        #self.ProductImages    A list of images to be shown on PerformInstallationPage. This element can have one or several <Image> child elements that contain a filename for an image.

        # TODO
        #self.RemoteRepositories    List of remote repositories. This element can contain several <Repository> child elements that each contain the <Url> child element that specifies the URL to access the repository. For more information, see Configuring Repositories.
        #self.RepositoryCategories    Name of a category that can contain a list of <RemoteRepositories> child elements. For more information, see Configuring Repository Categories.
        #self.RepositorySettingsPageVisible    Set to false to hide the repository settings page inside the settings dialog.
        #self.UrlQueryString    This string needs to be in the form "key=value" and will be appended to archive download requests. This can be used to transmit information to the webserver hosting the repository.

        # TODO 
        #self.Translations    List of language codes to be used for translating the user interface. To add several language variants, specify several <Translation> child elements that each specify the name of a language variant. Optional. For more information, see Translating Pages.
        
        # MAYBE Someday implement these...        
        #self.AdminTargetDir    Default target directory for installation with administrator rights. Only available on Linux, where you usually do not want to install in the administrator user's home directory.
        #self.RemoveTargetDir    (may cause conflicts with existing custom code!) Set to false if the target directory should not be deleted when uninstalling.
        #self.DisableCommandLineInterface    Set to true if command line interface features should be disabled. This prevents the user from passing any consumer command to installer, like install, update and remove. Other options can still be used normally. Defaults to false.        
        #self.DependsOnLocalInstallerBinary    Set to true if you want to prohibit installation from an external resource, such as a network drive. This might make sense for e.g. very big installers. The option is only used on Windows.
        #self.TargetConfigurationFile    Filename for the configuration file on the target. Default is components.xml.
        #self.AllowNonAsciiCharacters    Set to true if the installation path can contain non-ASCII characters.
        #self.AllowSpaceInPath    Set to false if the installation path cannot contain space characters.        
        #self.CreateLocalRepository    Set to true if you want to create a local repository inside the installation directory. This option has no effect on online installers. The repository will be automatically added to the list of default repositories.
        #self.InstallActionColumnVisible    Set to true if you want to add an extra column into component tree showing install actions. This extra column indicates whether a component is going to be installed or uninstalled, or just stay installed or uninstalled.
        #self.SupportsModify    Set to false if the product does not support modifying an existing installation.
        #self.SaveDefaultRepositories    Set to false if default repositories <RemoteRepositories> should not be saved to MaintenanceToolName.ini. By default default repositories are saved. Not saving the repositories means than when you run maintenancetool there are no default repositories in use.
        #self.AllowUnstableComponents    Set to true if other components are allowed to be installed although there are unstable components. A component is unstable if it is missing a dependency, has errors in scripts, and so on. Unstable components are grayed in the component tree, and therefore cannot be selected. By default, the value is false which means that the installation will be aborted if unstable components are found.        
        
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
        #self.Title = "%s Setup" % (self.Name,) # New versions of IFW add a "Setup" suffix 

    def _titleDisplayed( self ): return "%s Setup" % (self.Title,)
    
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
                _QtIfwXmlElement( QtIfwConfigXml.__ARG_TAG, str(arg), runArgs )                
        
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

    class Type: DATA, RESOURCE, PY_INSTALLER, IEXPRESS, QT_CPP = range(5)  
    
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
                  licenses=None, uiPages=None, widgets=None ) :
        # internal id / type
        self.pkgId     = pkgId
        self.pkgType   = pkgType       
        # QtIFW definition        
        self.name      = name
        self.pkgXml    = pkgXml
        self.pkgScript = pkgScript        
        self.uiPages   = uiPages if uiPages else []
        self.widgets   = widgets if widgets else []
        self.licenses  = licenses if licenses else {}
        self.isLicenseFormatPreserved = False        
        # content        
        self.srcDirPath    = srcDirPath
        self.srcExePath    = srcExePath
        self.resBasePath   = resBasePath
        self.distResources = None        
        self.isTempSrc     = isTempSrc                     
        # extended content detail        
        self.subDirName      = subDirName 
        self.exeName         = None           
        self.isGui           = False
        self.exeWrapper      = None # class QtIfwExeWrapper        
        self.codeSignTargets = None # list of relative paths within package 
        self.qtCppConfig     = None
        
        self._isMergeProduct = False
        
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
                   , "SortingPriority"
                   , "Default"
                   , "ForcedInstallation"
                   , "Essential"
                   , "Virtual"
                   , "Checkable"
                   , "Replaces"
                   , "Dependencies"
                   , "AutoDependOn"
                   , "Script"                       
                   ]
    __UIS_TAG      = "UserInterfaces"
    __UI_TAG       = "UserInterface"
    __LICENSES_TAG = "Licenses"
    __LICENSE_TAG  = "License"
    __NAME_ATTRIB  = "name"
    __FILE_ATTRIB  = "file"
        
    # QtIfwPackageXml   
    def __init__( self, pkgName, displayName, description, 
                  version, scriptName=None, 
                  isDefault=True, isRequired=False, 
                  isHidden=False, isCheckable=True ) :
        _QtIfwXml.__init__( self, QtIfwPackageXml.__ROOT_TAG, 
                            QtIfwPackageXml.__TAGS )        
        self.pkgName = pkgName
        
        # TODO: continue to expand on the natural IFW options here...
        self.SortingPriority    = None
        self.DisplayName        = displayName
        self.Description        = description
        self.Version            = version            
        self.Script             = scriptName 
        self.ReleaseDate        = date.today()
        self.Virtual            = True if isHidden else None
        self.Default            =( None if isHidden or isRequired
                                   or not isCheckable 
                                   else isDefault )
        self.ForcedInstallation = (True if isRequired and 
                                   not isHidden and 
                                   (isCheckable or isCheckable is None) 
                                   else None)
        self.Checkable          = (False if not isCheckable 
                                   and not isHidden and not isRequired 
                                   else None)         
        self.Dependencies       = None
        self.AutoDependOn       = None
        self.UserInterfaces     = []
        self.Licenses           = {} # name:filePath
                         
    def addCustomTags( self, root ) :
        if self.UserInterfaces is not None :            
            uis = _QtIfwXmlElement( QtIfwPackageXml.__UIS_TAG, 
                                    None, root )
            for ui in self.UserInterfaces:
                _QtIfwXmlElement( QtIfwPackageXml.__UI_TAG, ui, uis )                
        if self.Licenses is not None :            
            lics = _QtIfwXmlElement( QtIfwPackageXml.__LICENSES_TAG, 
                                    None, root )
            for name, filePath in iteritems( self.Licenses ):
                _QtIfwXmlElement( QtIfwPackageXml.__LICENSE_TAG, None, lics,
                    attrib={ QtIfwPackageXml.__NAME_ATTRIB:name, 
                             QtIfwPackageXml.__FILE_ATTRIB:filePath} )                
                            
    def path( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageXml.__PATH_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) ) 

    def dirPath( self ) :   
        return joinPath( BUILD_SETUP_DIR_PATH, 
            normpath( QtIfwPackageXml.__DIR_TMPLT 
                      % (INSTALLER_DIR_PATH, self.pkgName) ) )     


# -----------------------------------------------------------------------------
@add_metaclass( ABCMeta )
class _QtIfwScript:

    TAB         = "    "
    NEW_LINE    = "\n" 
    END_LINE    = ";\n"
    START_BLOCK = "{\n"
    END_BLOCK   = "}\n"

    IF    = "if "
    ELSE  = "else "
    
    TRY   = "try { "
    CATCH = "catch(e) { "
        
    NULL  = "null"    
    TRUE  = "true"
    FALSE = "false"

    ASSIGN = "=" # no spaces, to simplify use for argument building
    
    NOT = "! "
    EQUAL_TO = " == "
    NOT_EQUAL_TO = " != "
    
    AND = " && "
    OR  = " || "

    CONCAT = " + "
        
    EXIT_FUNCTION = "\n    return;\n"
    
    PATH_SEP = '"\\\\"' if IS_WINDOWS else '"/"'  
        
    MAINTENANCE_TOOL_NAME  = util.normBinaryName( 
        "maintenancetool", isGui=True )
    
    VERBOSE_CMD_SWITCH_ARG = "-v"    
    DEFAULT_TARGET_DIR_KEY = "DefaultTargetDir"
    TARGET_DIR_KEY         = "TargetDir"
    STARTMENU_DIR_KEY      = "StartMenuDir"
    PRODUCT_NAME_KEY       = "ProductName"
    
    ERR_LOG_PATH_CMD_ARG      = "errlog"
    ERR_LOG_DEFAULT_PATH      = ( 
        "%temp%\\\\installer.err" if IS_WINDOWS else
        "/tmp/installer.err" ) # /tmp is supposedly guaranteed to exist, though it's not secure

    OUT_LOG_PATH_CMD_ARG      = "outlog"
    OUT_LOG_DEFAULT_PATH      = ( 
        "%temp%\\\\installer.out" if IS_WINDOWS else
        "/tmp/installer.out" ) # /tmp is supposedly guaranteed to exist, though it's not secure

    TARGET_DIR_CMD_ARG        = "target"
    START_MENU_DIR_CMD_ARG    = "startmenu"    
    ACCEPT_EULA_CMD_ARG       = "accept"
    INSTALL_LIST_CMD_ARG      = "install"
    INCLUDE_LIST_CMD_ARG      = "include"
    EXCLUDE_LIST_CMD_ARG      = "exclude"
    RUN_PROGRAM_CMD_ARG       = "run"
    REBOOT_CMD_ARG            = "reboot"
    AUTO_PILOT_CMD_ARG        = "auto"
    DRYRUN_CMD_ARG            = "dryrun"
    _KEEP_ALIVE_PATH_CMD_ARG  = "__keepalive"
    TARGET_EXISTS_OPT_CMD_ARG = "onexist"
    TARGET_EXISTS_OPT_FAIL    = "fail"
    TARGET_EXISTS_OPT_REMOVE  = "remove"
    TARGET_EXISTS_OPT_PROMPT  = "prompt"
    
    MAINTAIN_MODE_CMD_ARG        = "mode"
    MAINTAIN_MODE_OPT_ADD_REMOVE = "addremove"
    MAINTAIN_MODE_OPT_UPDATE     = "update"    
    MAINTAIN_MODE_OPT_REMOVE_ALL = "removeall"
    MAINTAIN_PASSTHRU_CMD_ARG    = "maintpassthru"

    IS_NET_CONNECTED_KEY         = "isNetConnected"

    _WIZARD_STYLE_KEY     = "__wizardStyle"
    _IS_CMD_ARGS_TEMP_KEY = "__tmp_sv"
    _CMD_ARGS_TEMP_PREFIX = "__tmp_"
    _CMD_ARGS = { 
          ERR_LOG_PATH_CMD_ARG      : ERR_LOG_DEFAULT_PATH      
        , OUT_LOG_PATH_CMD_ARG      : OUT_LOG_DEFAULT_PATH     
        , TARGET_DIR_CMD_ARG        : ""       
        , START_MENU_DIR_CMD_ARG    : ""        
        , ACCEPT_EULA_CMD_ARG       : ""      
        , INSTALL_LIST_CMD_ARG      : ""     
        , INCLUDE_LIST_CMD_ARG      : ""     
        , EXCLUDE_LIST_CMD_ARG      : ""   
        , RUN_PROGRAM_CMD_ARG       : ""   
        , REBOOT_CMD_ARG            : ""   
        , AUTO_PILOT_CMD_ARG        : "" 
        , DRYRUN_CMD_ARG            : ""
        , TARGET_EXISTS_OPT_CMD_ARG : "" 
        , MAINTAIN_MODE_CMD_ARG     : ""
        , MAINTAIN_PASSTHRU_CMD_ARG : ""
        , _KEEP_ALIVE_PATH_CMD_ARG  : ""
        , _KEEP_TEMP_SWITCH         : ""           
    }

    _GUI_OBJ       = "gui"
    _INSTALLER_OBJ = "installer"
    
    _TEMP_DIR = "Dir.temp()"

    __QUIT = "quit(%s,%s,%s);\n"
                
    __IS_ELEVATED    = "isElevated();\n"        
    __GAIN_ELEVATION = "installer.gainAdminRights();\n"
    __DROP_ELEVATION = "installer.dropAdminRights();\n"
            
    __IS_INSTALLER   = "installer.isInstaller()"
    __IS_UNINSTALLER = "installer.isUninstaller()"

    __IS_MAINTENANCE_TOOL = 'isMaintenanceTool()'
            
    # an example for use down the line...
    __LINUX_GET_DISTRIBUTION = ( 
"""
        var IS_UBUNTU   = (systemInfo.productType === "ubuntu");
        var IS_OPENSUSE = (systemInfo.productType === "opensuse");             
""" )

    QUIT_MSGBOX_ID       = "cancelInstallation"
    AUTH_ERROR_MSGBOX_ID = "AuthorizationError"
    INTERUPTED_KEY       = "isInterupted"

    OK      = "QMessageBox.Yes"
    YES     = "QMessageBox.Yes" 
    NO      = "QMessageBox.No"
    CANCEL  = "QMessageBox.Cancel"
    ABORT   = "QMessageBox.Abort"
    
    RESTORE_MSGBOX_DEFAULT = "QMessageBox.RestoreDefaults"

    __STRING_TO_BOOL_TMPL = '(%s=="%s")'

    __LOG_TMPL = "console.log(%s);\n"
    __MSG_WRAPPER_TMPL = 'writeOutLog( %s );\n'
    
    __DEBUG_POPUP_TMPL = ( 
        'QMessageBox.information("debugbox", "Debug", ' +
            '%s, QMessageBox.Ok );\n' )    
    __WARN_POPUP_TMPL = ( 
        'QMessageBox.warning("warningbox", "Warning", ' +
            '%s, QMessageBox.Ok );\n' )
    __ERROR_POPUP_TMPL = ( 
        'QMessageBox.critical("errorbox", "Error", ' +
            '%s, QMessageBox.Ok );\n' )

    __YES_NO_POPUP_TMPL = ( 
        'var %s = QMessageBox.question("yesnobox", "%s", ' +
            '"%s", QMessageBox.Yes|QMessageBox.No );\n' )                                  
                                  
    __YES_NO_CANCEL_POPUP_TMPL = ( 
        'var %s = QMessageBox.question("yesnocancelbox", "%s", ' +
            '"%s", QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel );\n' )
    
    __SET_MSGBOX_AUTO_ANSWER_TMPL = (        
        'installer.setMessageBoxAutomaticAnswer( "%s", %s );\n' )
    
    __GET_COMPONENT_TMPL  = 'getComponent( %s )' 
    __GET_PAGE_OWNER_TMPL = 'getPageOwner( %s )'

    __IS_COMPONENT_INSTALLED = 'isComponentInstalled( %s )' 
    __IS_COMPONENT_SELECTED  = 'isComponentSelected( %s )'
    __IS_COMPONENT_ENABLED   = 'isComponentEnabled( %s )' 
        
    __ENABLE_COMPONENT       = 'enableComponent( %s, %s )'
        
    __VALUE_TMPL      = "installer.value( %s, %s )"
    __VALUE_LIST_TMPL = "installer.values( %s, %s )"
    __SET_VALUE_TMPL  = "installer.setValue( %s, %s );\n"

    __GET_ENV_VAR_TMPL = "installer.environmentVariable( %s )"

    __PATH_EXISTS_TMPL = "%sinstaller.fileExists( resolveQtIfwPath( %s ) )"
    
    __RESOLVE_DYNAMIC_VARS_TMPL = "resolveDynamicVars( %s, %s )"

    __MAKE_DIR_TMPL   = "makeDir( resolveQtIfwPath( %s ) );\n"
    __REMOVE_DIR_TMPL = "removeDir( resolveQtIfwPath( %s ) );\n"
    
    __WRITE_FILE_TMPL  = "writeFile( resolveQtIfwPath( %s ), %s );\n"
    __DELETE_FILE_TMPL = "deleteFile( resolveQtIfwPath( %s ) );\n"

    __EMBED_RES_TMPLT       = 'var %s = %s;\n\n'
    __EMBED_RES_CHUNK_SIZE  = 128
    __EXT_DELIM_PLACEHOLDER = "_dot_"
    __SCRIPT_FROM_B64_TMPL  = '__writeScriptFromBase64( "%s", %s, %s, %s, %s, %s );\n'
    __REPLACE_VARS_FILE_TMPL = 'replaceDynamicVarsInFile( %s, %s, %s );\n' 
    
    __ASSERT_INTERNET_TMPL  = "assertInternetConnected( %s, %s );"
    __IS_INTERNET_TMPL      = "isInternetConnected( %s )"
    __IS_PINGABLE_TMPL      = "isPingable( %s, %d, %d )"
        
    # Note, there is in fact an installer.killProcess(string absoluteFilePath)
    # this custom kill takes a process name, with no specific path
    # It also runs in parrellel with "install operation" kills
    __KILLALL_PROG_TMPL = "killAll( %s );\n"
    _KILLALL_PATH = "taskkill"   if IS_WINDOWS else "killall"
    _KILLALL_ARGS = ["/F","/IM"] if IS_WINDOWS else ["-9"] #TODO: CROSS SH? some might want -s9 ?
    _KILLALL_CMD_PREFIX = "%s %s" % (_KILLALL_PATH, " ".join( _KILLALL_ARGS ))

    if IS_WINDOWS:

        __REG_KEY_EXISTS_TMPL = "registryKeyExists( %s, %s )"        
        __REG_KEY_EXISTS_LIKE_TMPL = "registryKeyExistsLike( %s, %s, %s, %s, %s )"             

        __REG_ENTRY_VALUE_TMPL = "registryEntryValue( %s, %s, %s )"
        __ASSIGN_REG_ENTRY_VALUE_TMPL = "var %s = %s;\n"

        __REG_ENTRY_EXISTS_TMPL = "registryEntryExists( %s, %s, %s )"                        
        __REG_ENTRY_EXISTS_LIKE_TMPL =( 
            "registryEntryExistsLike( %s, %s, %s, %s, %s  )" )

    @staticmethod        
    def quote( value ):                  
        return '"%s"' % (value,)  

    @staticmethod        
    def ifCondition( condition, isNegated=False, isMultiLine=False ):
        return 'if( %s%s )%s\n%s' % (
            ("!" if isNegated else ""), condition, 
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def andList( conditions ):
        conditions = [ '(%s)' % (c,) if isinstance(c,string_types) 
                       else _QtIfwScript.toBool(c)
                       for c in conditions ]
        return '(%s)' % ( _QtIfwScript.AND.join( conditions ), )

    @staticmethod        
    def orList( conditions ):
        conditions = [ '(%s)' % (c,) if isinstance(c,string_types) 
                       else _QtIfwScript.toBool(c)
                       for c in conditions ]
        return '(%s)' % ( _QtIfwScript.OR.join( conditions ), )

    @staticmethod        
    def _autoQuote( value, isAutoQuote ):                  
        return '"%s"' % (value,) if isAutoQuote else value 

    @staticmethod        
    def _autoEscapeBackSlash( value, isAutoEscape ):                  
        return value.replace( "\\", "\\\\" ) if isAutoEscape else value 

    @staticmethod
    def embedResources( embeddedResources ):
        def chunks(s, n):
            """Produce `n`-character chunks from `s`."""
            for start in range(0, len(s), n):
                yield s[start:start+n]
        
        def embed( res ):
            if isinstance( res, ExecutableScript ):
                script = res
                print( "Embedding script: %s" % (script.rootName,) )
                if "-" in script.rootName: 
                    raise DistBuilderError( "Embedded script names may not contain dashes!"
                        " (Auto correcting this may produce hard to find bugs)" )
                varName = script.fileName().replace(".","_dot_")                                
                b64 = script.toBase64( toString=True )
                if len(b64)==0: b64Literals = '""'                    
                else:
                    b64Literals = ""
                    for chunk in chunks(b64, _QtIfwScript.__EMBED_RES_CHUNK_SIZE):
                        concat = "  " if b64Literals=="" else "+ " 
                        b64Literals += '%s%s%s"%s"' % (
                            _QtIfwScript.NEW_LINE, _QtIfwScript.TAB, concat, 
                            chunk )                                    
                return _QtIfwScript.__EMBED_RES_TMPLT % (varName, b64Literals)                 
        raw = ""
        for res in embeddedResources: raw += embed( res )
        return raw

    @staticmethod
    def genResources( embeddedResources, isTempRootTarget=False ):
        return _QtIfwScript.__writeScripts( embeddedResources, 
                                            isTempRootTarget=isTempRootTarget )
            
    @staticmethod
    def resolveScriptVars( scripts, subDir ):
        return _QtIfwScript.__writeScripts( scripts, True, False, subDir )

    @staticmethod
    def resolveScriptVarsOperations( scripts, subDir ):
        return _QtIfwScript.__writeScripts( scripts, True, True, subDir )

    @staticmethod
    def __writeScripts( scripts, isUpdate=False, isOp=False, 
                        subDir=None, isTempRootTarget=False ):
        
        MAX_VAR_LENGTH = 64 # Not a true limit to the language, just a sanity check for this context
        VAR_NAME_CHARS = string.digits + string.ascii_letters + "_"
        
        def isValidVarName( name ):
            if name.strip()=="" or len(name) > MAX_VAR_LENGTH: return False
            for c in name: 
                if c not in VAR_NAME_CHARS: return False
            return True
        
        def dynamicParms( script, subDir=None ):
            if isinstance( script, ExecutableScript ):
                scriptName = script.fileName()
                scriptPath = ( _QtIfwScript.targetDir() + ' + "/' +  
                    ( joinPathQtIfw( subDir, scriptName ) 
                      if subDir else scriptName ) + '"' )
                scriptContent = str(script)
                isDoubleBackslash = script.isIfwVarEscapeBackslash
                resourceVarName = scriptName.replace(
                    ".", _QtIfwScript.__EXT_DELIM_PLACEHOLDER ) 
                dynamicVarNames = set( scriptContent.split( QT_IFW_DYNAMIC_SYMBOL ) )
                dynamicVarNames = [ v for v in dynamicVarNames 
                                    if isValidVarName( v ) ]
                dynamicVarNames = "[ %s ]" % (
                    ",".join( ['"%s"' % (v,) for v in dynamicVarNames] ), )
                return ( scriptPath, scriptName, resourceVarName,
                         dynamicVarNames, isDoubleBackslash )
            return None
        
        def gen( script, isTempRootTarget ):
            parms = dynamicParms( script )  
            if parms:
                ( _, scriptName, resourceVarName, 
                  dynamicVarNames, isDoubleBackslash ) = parms
                isB64Removed =  isTempRootTarget
                return ( 
                    #_QtIfwScript.log( "script: %s" % (scriptName,) ) + 
                    #_QtIfwScript.log( scriptContent ) + # this introduces assorted escaping complications...
                    _QtIfwScript.__SCRIPT_FROM_B64_TMPL % 
                    (scriptName, resourceVarName, dynamicVarNames,
                     _QtIfwScript.toBool(isDoubleBackslash),
                     _QtIfwScript.toBool(isTempRootTarget),
                     _QtIfwScript.toBool(isB64Removed) ) )                
            return ""        
        
        def update( script, isOp, subDir ):
            parms = dynamicParms( script, subDir )  
            if parms:
                scriptPath, _, _, dynamicVarNames, isDoubleBackslash = parms
                if isOp:
                    return QtIfwPackageScript._addReplaceVarsInFileOperation( 
                        scriptPath, dynamicVarNames, 
                        _QtIfwScript.toBool(isDoubleBackslash), 
                        isElevated=True ) 
                else:
                    return _QtIfwScript.__REPLACE_VARS_FILE_TMPL % ( 
                        scriptPath, dynamicVarNames,
                        _QtIfwScript.toBool(isDoubleBackslash) ) 
            return ""
        
        return "".join( [ update( s, isOp, subDir ) if isUpdate else 
                          gen( s, isTempRootTarget )
                          for s in scripts ] )
        
    @staticmethod        
    def log( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__LOG_TMPL % (
            _QtIfwScript._autoQuote( msg, isAutoQuote ),)

    @staticmethod        
    def _msgToSilentWrapper( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__MSG_WRAPPER_TMPL % (
            _QtIfwScript._autoQuote( msg, isAutoQuote ),)

    @staticmethod        
    def logValue( key, defaultVal="" ):                  
        return _QtIfwScript.log( ('"%s = " + ' % (key,)) +
                _QtIfwScript.lookupValue(key, defaultVal ), 
                isAutoQuote=False ) 

    @staticmethod        
    def logSwitch( key ): 
        return  _QtIfwScript.logValue( key, defaultVal="false" ) 

    @staticmethod        
    def debugPopup( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__DEBUG_POPUP_TMPL % (
             _QtIfwScript._autoQuote( msg, isAutoQuote ),) 
        
    @staticmethod        
    def warningPopup( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__WARN_POPUP_TMPL % (
             _QtIfwScript._autoQuote( msg, isAutoQuote ),) 
        
    @staticmethod        
    def errorPopup( msg, isAutoQuote=True ):                  
        return _QtIfwScript.__ERROR_POPUP_TMPL % (
             _QtIfwScript._autoQuote( msg, isAutoQuote ),) 

    @staticmethod        
    def toNull( v ): return _QtIfwScript.NULL if v is None else v

    @staticmethod        
    def toBool( b ):
        if isinstance( b, string_types ): return b                          
        return _QtIfwScript.TRUE if b else _QtIfwScript.FALSE   

    @staticmethod        
    def boolToString( b ):
        if isinstance( b, string_types ):
            return '(%s ? "%s":"%s")' % ( 
                b, _QtIfwScript.TRUE, _QtIfwScript.FALSE )                          
        return '"%s"' % ( _QtIfwScript.TRUE if b else _QtIfwScript.FALSE )  

    @staticmethod        
    def stringToBool( value, isAutoQuote=True ):
        return _QtIfwScript.__STRING_TO_BOOL_TMPL % (
            _QtIfwScript._autoQuote( value, isAutoQuote ),
            _QtIfwScript.TRUE ) 
        
    @staticmethod        
    def setValue( key, value, isAutoQuote=True ):                  
        return _QtIfwScript.__SET_VALUE_TMPL % (
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            _QtIfwScript._autoQuote( value, isAutoQuote ))

    @staticmethod        
    def setBoolValue( key, b, isAutoQuote=True ):                  
        return _QtIfwScript.__SET_VALUE_TMPL % (            
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            _QtIfwScript.boolToString( b ) )

    @staticmethod        
    def lookupValue( key, default="", isAutoQuote=True ):                  
        return _QtIfwScript.__VALUE_TMPL % (
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            _QtIfwScript._autoQuote( default, isAutoQuote ))

    @staticmethod        
    def lookupBoolValue( key, isNegated=False, isHardFalse=False, isAutoQuote=True ):
        return '( %s%s"%s" )' % (
            _QtIfwScript.lookupValue( key, isAutoQuote=isAutoQuote ),
            ("!=" if isNegated and not isHardFalse else "==") ,
            (_QtIfwScript.FALSE if isHardFalse else _QtIfwScript.TRUE) )
        
    @staticmethod        
    def ifValueDefined( key, isNegated=False, isMultiLine=False ):
        return 'if( %s%s"" )%s\n%s' % (
            _QtIfwScript.lookupValue( key ),
            ("==" if isNegated else "!="), 
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def ifBoolValue( key, isNegated=False, isHardFalse=False, isMultiLine=False ):        
        return 'if( %s%s"%s" )%s\n%s' % (
            _QtIfwScript.lookupValue( key ),
            ("!=" if isNegated and not isHardFalse else "==") ,
            (_QtIfwScript.FALSE if isHardFalse else _QtIfwScript.TRUE),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def lookupValueList( key, defaultList=None, isAutoQuote=True, 
                          delimiter=None ):
        if defaultList is None: defaultList=[]
        defList=""
        for v in defaultList: 
            defList += _QtIfwScript._autoQuote( str(v), isAutoQuote )
        defList = "[%s]" % (",".join( defList ),)                    
        if delimiter:
            valScr = _QtIfwScript.lookupValue( key, isAutoQuote=True )
            return ( '( %s=="" ? %s : %s.split("%s") )' % 
                ( valScr, defList, valScr, delimiter ) )
        return _QtIfwScript.__VALUE_LIST_TMPL % (
            _QtIfwScript._autoQuote( key, isAutoQuote ),
            defList )
    
    @staticmethod
    def resolveDynamicVars( s, varNames=None, isAutoQuote=True ):
        if varNames is None:
            nameList = _QtIfwScript.toNull(varNames)
        else :    
            nameList=''
            for v in varNames: 
                nameList += _QtIfwScript._autoQuote( str(v), isAutoQuote )
            nameList = "[%s]" % (",".join( nameList ),)        
        return _QtIfwScript.__RESOLVE_DYNAMIC_VARS_TMPL % (
            _QtIfwScript._autoQuote( s, isAutoQuote ), nameList )
    
    @staticmethod        
    def quit( msg, isError=True, isSilent=False, isAutoQuote=True ): 
        return _QtIfwScript.__QUIT % (
            _QtIfwScript._autoQuote( msg, isAutoQuote ),
            _QtIfwScript.toBool( isError ), _QtIfwScript.toBool( isSilent ) )
        
    @staticmethod        
    def isElevated(): return _QtIfwScript.__IS_ELEVATED

    @staticmethod        
    def ifElevated( isNegated=False, isMultiLine=False ):
        return 'if( %sisElevated() )%s\n%s' % (
            ("!" if isNegated else ""), 
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def elevate():
        return( QtIfwControlScript._disableAuthErrorPrompt() +  
                _QtIfwScript.__GAIN_ELEVATION )
        
    @staticmethod        
    def dropElevation(): return _QtIfwScript.__DROP_ELEVATION 
        
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
    def ifCmdLineArg( arg, isNegated=False, isMultiLine=False ):   
        return _QtIfwScript.ifValueDefined( arg, isNegated, isMultiLine )

    @staticmethod        
    def ifCmdLineSwitch( arg, isNegated=False, isHardFalse=False, isMultiLine=False ):
        return _QtIfwScript.ifBoolValue( arg, isNegated, isHardFalse, isMultiLine )

    @staticmethod        
    def cmdLineArg( arg, default="" ):
        return _QtIfwScript.lookupValue( arg, default )

    @staticmethod        
    def cmdLineSwitchArg( arg, isNegated=False, isHardFalse=False ):
        return _QtIfwScript.lookupBoolValue( arg, 
            isNegated=isNegated, isHardFalse=isHardFalse ) 

    @staticmethod        
    def cmdLineListArg( arg, default=None ):
        if default is None: default=[]                  
        return _QtIfwScript.lookupValueList( 
            arg, default, delimiter="," )

    @staticmethod
    def isInstalling( isNegated=False ):
        return '( %s%s )' % ( "!" if isNegated else "", 
                              _QtIfwScript.__IS_INSTALLER )
    @staticmethod        
    def ifInstalling( isNegated=False, isMultiLine=False ):
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.__IS_INSTALLER,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod
    def isMaintenanceTool( isNegated=False ):
        return '( %s%s )' % ( "!" if isNegated else "", 
                              _QtIfwScript.__IS_MAINTENANCE_TOOL )

    @staticmethod
    def ifMaintenanceTool( isNegated=False, isMultiLine=False ):
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.__IS_MAINTENANCE_TOOL,
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod
    def isAutoPilot( isNegated=False ):
        return '( %s%s )' % ( "!" if isNegated else "", 
            _QtIfwScript.orList([
                _QtIfwScript.cmdLineSwitchArg( 
                    _QtIfwScript.AUTO_PILOT_CMD_ARG ),
                _QtIfwScript.andList([
                    _QtIfwScript.isInstalling(), 
                    _QtIfwScript.cmdLineSwitchArg(    
                        _QtIfwScript._CMD_ARGS_TEMP_PREFIX + 
                        _QtIfwScript.AUTO_PILOT_CMD_ARG )
                ])
            ])
        )
    
    @staticmethod
    def ifAutoPilot( isNegated=False, isMultiLine=False ):
        return _QtIfwScript.ifCondition( _QtIfwScript.isAutoPilot( 
            isNegated=isNegated ), isMultiLine=isMultiLine ) 

    @staticmethod
    def isDryRun( isNegated=False ):
        return '( %s%s )' % ( "!" if isNegated else "", 
                _QtIfwScript.cmdLineSwitchArg( 
                    _QtIfwScript.DRYRUN_CMD_ARG ), )
    
    @staticmethod
    def ifDryRun( isNegated=False, isMultiLine=False ):
        return _QtIfwScript.ifCondition( _QtIfwScript.isDryRun( 
            isNegated=isNegated ), isMultiLine=isMultiLine ) 

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
    def _disableAuthErrorPrompt():         
        return _QtIfwScript.__SET_MSGBOX_AUTO_ANSWER_TMPL % (
            _QtIfwScript.AUTH_ERROR_MSGBOX_ID, _QtIfwScript.ABORT )

    @staticmethod        
    def disableQuit():         
        return _QtIfwScript.__SET_MSGBOX_AUTO_ANSWER_TMPL % (
            _QtIfwScript.QUIT_MSGBOX_ID, _QtIfwScript.NO )

    @staticmethod        
    def disableQuitPrompt():         
        return _QtIfwScript.__SET_MSGBOX_AUTO_ANSWER_TMPL % (
            _QtIfwScript.QUIT_MSGBOX_ID, _QtIfwScript.YES )

    @staticmethod        
    def pathExists( path, isNegated=False, isAutoQuote=True ):                  
        return _QtIfwScript.__PATH_EXISTS_TMPL % (
            "!" if isNegated else "",
            _QtIfwScript._autoQuote( path, isAutoQuote ),) 

    @staticmethod        
    def ifPathExists( path, isNegated=False, 
                      isAutoQuote=True, isMultiLine=False ):   
        return 'if( %s )%s\n%s' % (            
            _QtIfwScript.pathExists( path, isNegated, isAutoQuote ),
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

    @staticmethod        
    def assertInternetConnected( isRefresh=False, errMsg=None, 
                                 isAutoQuote=True ): 
        return _QtIfwScript.__ASSERT_INTERNET_TMPL % (
            _QtIfwScript.toBool( isRefresh ),
            _QtIfwScript.toNull( errMsg ) if errMsg is None else
            _QtIfwScript._autoQuote( errMsg, isAutoQuote ) ) 

    @staticmethod        
    def isInternetConnected( isRefresh=False ): 
        return _QtIfwScript.__IS_INTERNET_TMPL % (
            _QtIfwScript.toBool( isRefresh ), ) 

    @staticmethod        
    def ifInternetConnected( isRefresh=False, isNegated=False, isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % ( "!" if isNegated else "",
            _QtIfwScript.isInternetConnected( isRefresh ),            
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
        
    @staticmethod        
    def isPingable( uri, pings=3, totalMaxSecs=12, isAutoQuote=True ):                  
        return _QtIfwScript.__IS_PINGABLE_TMPL % (
            _QtIfwScript._autoQuote( uri, isAutoQuote ),
            pings, totalMaxSecs ) 

    @staticmethod
    def ifPingable( uri, pings=3, totalMaxSecs=12, isAutoQuote=True,
                    isNegated=False, isMultiLine=False  ):
        return 'if( %s%s )%s\n%s' % ( "!" if isNegated else "", 
            _QtIfwScript.isPingable( uri, pings, totalMaxSecs, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def getComponent( name, isAutoQuote=True ):
        if isinstance( name, QtIfwPackage ): name = name.name                  
        return _QtIfwScript.__GET_COMPONENT_TMPL % (
            _QtIfwScript._autoQuote( name, isAutoQuote ),) 

    @staticmethod        
    def getPageOwner( pageName, isAutoQuote=True ):
        if isinstance( pageName, QtIfwUiPage ): pageName = pageName.name                  
        return _QtIfwScript.__GET_PAGE_OWNER_TMPL % (
            _QtIfwScript._autoQuote( pageName, isAutoQuote ),) 
            
    @staticmethod        
    def isComponentInstalled( package, isAutoQuote=True ):
        name = package.name if isinstance( package, QtIfwPackage ) else package              
        return _QtIfwScript.__IS_COMPONENT_INSTALLED % (
            _QtIfwScript._autoQuote( name, isAutoQuote ),) 

    @staticmethod
    def ifComponentInstalled( package, isNegated=False, 
                              isAutoQuote=True, isMultiLine=False ):
        name = package.name if isinstance( package, QtIfwPackage ) else package   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.isComponentInstalled( name, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
                       
    @staticmethod        
    def isComponentSelected( package, isAutoQuote=True ):
        name = package.name if isinstance( package, QtIfwPackage ) else package                  
        return _QtIfwScript.__IS_COMPONENT_SELECTED % (
            _QtIfwScript._autoQuote( name, isAutoQuote ),) 

    @staticmethod
    def ifComponentSelected( package, isNegated=False, 
                              isAutoQuote=True, isMultiLine=False ):
        name = package.name if isinstance( package, QtIfwPackage ) else package
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.isComponentSelected( name, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def isComponentEnabled( package, isAutoQuote=True ):
        name = package.name if isinstance( package, QtIfwPackage ) else package                  
        return _QtIfwScript.__IS_COMPONENT_ENABLED % (
            _QtIfwScript._autoQuote( name, isAutoQuote ),) 

    @staticmethod
    def ifComponentEnabled( package, isNegated=False, 
                              isAutoQuote=True, isMultiLine=False ):
        name = package.name if isinstance( package, QtIfwPackage ) else package
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.isComponentEnabled( name, isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def enableComponent( package, enable=True, isAutoQuote=True ):
        name = package.name if isinstance( package, QtIfwPackage ) else package                  
        return _QtIfwScript.__ENABLE_COMPONENT % (
            _QtIfwScript._autoQuote( name, isAutoQuote ),
            _QtIfwScript.toBool( enable ) ) 

    if IS_WINDOWS:
        
        @staticmethod
        def registryKeyExists( key, isAutoBitContext=True,
                               isAutoQuote=True ): 
            return _QtIfwScript.__REG_KEY_EXISTS_TMPL % (
                _QtIfwScript._autoEscapeBackSlash( 
                    _QtIfwScript._autoQuote( key, isAutoQuote ), 
                    isAutoQuote ).replace(":",""), 
                _QtIfwScript.toBool( isAutoBitContext ) )
        
        @staticmethod
        def ifRegistryKeyExists( key, isAutoBitContext=True, isNegated=False, 
                                isAutoQuote=True, isMultiLine=False ): 
            return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.registryKeyExists( key, 
                isAutoBitContext=isAutoBitContext, isAutoQuote=isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
        
        @staticmethod
        def registryKeyExistsLike( parentKey, childKeyNameContains, 
                                   isAutoBitContext=True, 
                                   isCaseSensitive=False, isRecursive=False,
                                   isAutoQuote=True ): 
            return _QtIfwScript.__REG_KEY_EXISTS_LIKE_TMPL % (
                _QtIfwScript._autoEscapeBackSlash( 
                    _QtIfwScript._autoQuote( parentKey, isAutoQuote ), 
                    isAutoQuote ).replace(":",""),
                _QtIfwScript._autoEscapeBackSlash( 
                    _QtIfwScript._autoQuote( childKeyNameContains, isAutoQuote ), 
                    isAutoQuote ).replace(":",""),                  
                _QtIfwScript.toBool( isAutoBitContext ), 
                _QtIfwScript.toBool( isCaseSensitive ),
                _QtIfwScript.toBool( isRecursive ) )
                
        @staticmethod
        def ifRegistryKeyExistsLike( parentKey, childKeyNameContains, 
                                     isAutoBitContext=True, 
                                     isCaseSensitive=False, isRecursive=False,
                                     isNegated=False, 
                                     isAutoQuote=True, isMultiLine=False ): 
            return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.registryKeyExistsLike( 
                parentKey, childKeyNameContains,                                                   
                isAutoBitContext=isAutoBitContext,
                isCaseSensitive=isCaseSensitive, isRecursive=isRecursive, 
                isAutoQuote=isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
        
        @staticmethod
        def registryEntryValue( key, valueName, isAutoBitContext=True,
                                isAutoQuote=True ): 
            valueName =( _QtIfwScript.toNull( valueName ) if valueName is None
                else _QtIfwScript._autoQuote( valueName, isAutoQuote ) )
            return _QtIfwScript.__REG_ENTRY_VALUE_TMPL % (
                _QtIfwScript._autoEscapeBackSlash( 
                    _QtIfwScript._autoQuote( key, isAutoQuote ), 
                    isAutoQuote ).replace(":",""), 
                valueName,
                _QtIfwScript.toBool( isAutoBitContext )  )                                

        @staticmethod            
        def assignRegistryEntryVar( key, valueName, isAutoBitContext=True,
                                    varName="regValue", isAutoQuote=True ): 
            return _QtIfwScript.__ASSIGN_REG_ENTRY_VALUE_TMPL % (
                varName, _QtIfwScript.registryEntryValue( 
                    key, valueName, isAutoBitContext=isAutoBitContext,
                    isAutoQuote=isAutoQuote ) ) 

        @staticmethod
        def setValueFromRegistryEntry( key, 
                                       regKey, valueName, isAutoBitContext=True,                                    
                                       isAutoQuote=True ):                                    
            return _QtIfwScript.setValue( 
                _QtIfwScript._autoQuote( key, isAutoQuote ), 
                _QtIfwScript.registryEntryValue( 
                    regKey, valueName, isAutoBitContext=isAutoBitContext,
                    isAutoQuote=isAutoQuote ), 
                isAutoQuote=False )
        
        @staticmethod
        def registryEntryExists( key, valueName, isAutoBitContext=True,
                                 isAutoQuote=True ):       
            valueName =( _QtIfwScript.toNull( valueName ) if valueName is None
                else _QtIfwScript._autoQuote( valueName, isAutoQuote ) )              
            return _QtIfwScript.__REG_ENTRY_EXISTS_TMPL % (                
                _QtIfwScript._autoEscapeBackSlash( 
                    _QtIfwScript._autoQuote( key, isAutoQuote ), 
                    isAutoQuote ).replace(":",""),                 
                valueName,
                _QtIfwScript.toBool( isAutoBitContext )  ) 
                                         
        @staticmethod
        def ifRegistryEntryExists( key, valueName, isAutoBitContext=True,
                                   isNegated=False, 
                                   isAutoQuote=True, isMultiLine=False ) : 
            return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.registryEntryExists( key, valueName,                                                   
                isAutoBitContext=isAutoBitContext,                
                isAutoQuote=isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
                            
        @staticmethod
        def registryEntryExistsLike( key, valueNameContains, 
                                     isAutoBitContext=True, 
                                     isCaseSensitive=False, isRecursive=False,
                                     isAutoQuote=True ): 
            return _QtIfwScript.__REG_ENTRY_EXISTS_LIKE_TMPL % ( 
                _QtIfwScript._autoEscapeBackSlash( 
                    _QtIfwScript._autoQuote( key, isAutoQuote ), 
                    isAutoQuote ).replace(":",""), 
                _QtIfwScript._autoQuote( valueNameContains, isAutoQuote ),
                _QtIfwScript.toBool( isAutoBitContext ), 
                _QtIfwScript.toBool( isCaseSensitive ),
                _QtIfwScript.toBool( isRecursive ) )                                 

        @staticmethod
        def ifRegistryEntryExistsLike( key, valueNameContains, 
                                       isAutoBitContext=True, 
                                       isCaseSensitive=False, isRecursive=False,
                                       isNegated=False, 
                                       isAutoQuote=True, isMultiLine=False ): 
            return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            _QtIfwScript.registryEntryExistsLike(  key, valueNameContains,                                                   
                isAutoBitContext=isAutoBitContext,
                isCaseSensitive=isCaseSensitive, isRecursive=isRecursive, 
                isAutoQuote=isAutoQuote ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
                        
    # _QtIfwScript            
    def __init__( self, fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None, 
                  virtualArgs=None, isAutoLib=True ) :
        self.fileName = fileName
        if scriptPath :
            with open( scriptPath, 'rb' ) as f: self.script = f.read()
        else : self.script = script  
        self.virtualArgs = virtualArgs if virtualArgs else {}
        self.isAutoLib   = isAutoLib
        self.qtScriptLib = None

    def _genLib( self ):
        NEW   = _QtIfwScript.NEW_LINE
        END   = _QtIfwScript.END_LINE
        TAB   = _QtIfwScript.TAB
        SBLK  = _QtIfwScript.START_BLOCK
        EBLK  = _QtIfwScript.END_BLOCK
        TRY   = _QtIfwScript.TRY
        CATCH = _QtIfwScript.CATCH
        #IF    = _QtIfwScript.IF
        ELSE  = _QtIfwScript.ELSE
        
        varsList = ",".join([ '"%s"' % (v,) 
                              for v in QT_IFW_DYNAMIC_VARS ])
        pathVarsList = ",".join([ '"%s"' % (v,) 
                                  for v in QT_IFW_DYNAMIC_PATH_VARS ])

        self.qtScriptLib = (              
            'function isWindows() ' + SBLK +
            TAB + 'return systemInfo.kernelType === "winnt"' + END +
            EBLK + NEW +
            'function isMacOs() ' + SBLK +
            TAB + 'return systemInfo.kernelType === "darwin"' + END +
            EBLK + NEW +
            'function isLinux() ' + SBLK +
            TAB + 'return systemInfo.kernelType === "linux"' + END +
            EBLK + NEW +
            'var dynamicVars = [ ' + varsList + ' ]' + END +
            'var dynamicPathVars = [ ' + pathVarsList + ' ]' + END +
            NEW +                              
            'function __realUserName()' + SBLK +
            TAB + 'if( isWindows() ) return ""; // not currently using this in Windows' + END +
            TAB + 'var realUserName = installer.value( "__realUserName", "" )' + END +
            TAB + 'if( realUserName === "" ) ' + SBLK +            
            (2*TAB) + 'realUserName = installer.environmentVariable("USER");' + END +
            (2*TAB) + 'installer.setValue( "__realUserName", realUserName )' + END +
            (2*TAB) + _QtIfwScript.log( '"__realUserName: " + realUserName', 
                                        isAutoQuote=False ) +                             
            EBLK + NEW +                                          
            TAB + 'return realUserName' + END +
            EBLK + NEW +                                                   
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
            TAB + 'var isMaintenance = false' + END + 
            TAB + 'var __isMaintenance = installer.value( "__isMaintenance", "" )' + END + 
            TAB + 'if( __isMaintenance === "" ) ' + SBLK +
            (2*TAB) + '__lockFilePath()' + END +
            (2*TAB) + '__isMaintenance = installer.value( "__isMaintenance", "false" )' + END +
            (2*TAB) + 'isMaintenance = ' + _QtIfwScript.stringToBool( 
                '__isMaintenance', isAutoQuote=False ) + END +             
            (2*TAB) + _QtIfwScript.log( '"isMaintenanceTool: " + isMaintenance', isAutoQuote=False ) +
            TAB + EBLK +
            TAB + 'else ' + SBLK +
                (2*TAB) + 'isMaintenance = ' + _QtIfwScript.stringToBool( 
                    '__isMaintenance', isAutoQuote=False ) + END +             
            TAB + EBLK +                  
            TAB + 'return isMaintenance' + END +                                   
            EBLK + NEW +            
            # TODO: This logic could possibly fail when installers / uninstallers 
            # for *other* programs are running at the same time...          
            'function __lockFilePath() ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var path = installer.value( "__lockFilePath", "" )' + END +
            TAB + 'if( path === "" ) ' + SBLK +                        
            (2*TAB) + 'var lockFileName = ""' + END +
            (2*TAB) + 'var instPrefix = __installerPrefix()' + END +
            (2*TAB) + 'var toolPrefix = __maintenanceToolPrefix()' + END +
            (2*TAB) + 'var lockFileDir = __envTempPath()' + END + 
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
            (2*TAB) + 'var isMaintenance = rootFileName( lockFileName ).startsWith( ' + 
                  ('rootFileName( "%s" ) )' % (_QtIfwScript.MAINTENANCE_TOOL_NAME,)) + END +
            (2*TAB) + 'installer.setValue( "__isMaintenance", ' + 
                _QtIfwScript.boolToString( 'isMaintenance' ) + ' )'  + END +              
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
            'function __envTempPath() ' + SBLK +              
            TAB + 'return isWindows() ? getEnv("temp") : "/tmp"' + END +                  
            EBLK + NEW +                                                                                                                  
            'function __tempPath( suffix ) ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'return (isMaintenanceTool() ? ' +
                    '__maintenanceTempPath() : __installerTempPath()) + ' +
                                                '(suffix ? suffix : "")' + END +                  
            EBLK + NEW +
            'function __tempRootFilePath( extension ) ' + SBLK +  # TODO: Test in NIX/MAC
            TAB + 'return __tempPath( "." + (extension ? extension : "tmp") ) ' + END +                                                                              
            EBLK + NEW +                        
            'function __installerTempPath( suffix ) ' + SBLK +  # TODO: Test in NIX/MAC            
            TAB + 'var dirPath = installer.value( ' + 
                ('"%s"' % (_QT_IFW_INSTALLER_TEMP_DIR,)) + ', "" )' + END +
            TAB + 'if( dirPath === "" ) ' + SBLK +            
            (2*TAB) + 'dirPath = Dir.toNativeSeparator( ' +
                '__envTempPath() + "/__" + __installerPrefix() + "-install" )' + END +
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
                '__envTempPath() + "/__" + __installerPrefix() + "-maintenance" )' + END +
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
            'function resolveDynamicVars( s, varNames ) ' + SBLK + 
            TAB + 'var ret = s' + END +
            TAB + 'if( !varNames ) varNames = dynamicVars' + END +                 
            TAB + 'for( var i=0; i != varNames.length; ++i ) ' + SBLK +                                    
            (2*TAB) + 'var varName = varNames[i]' + END +
            (2*TAB) + 'var varVal = installer.value( varName, "' + 
                                        QT_IFW_UNDEF_VAR_VALUE + '" )' + END +
            (2*TAB) + 'ret = ret.split( "@" + varName + "@" ).join( varVal )' + END +
            (2*TAB) + EBLK +             
            TAB + 'return ret' + END +                                                                                                                          
            EBLK + NEW +
            'function toMaintenanceToolPath( dir ) ' + SBLK +
                TAB + 'return dir + ' + _QtIfwScript.PATH_SEP + ' + ' +
                    ('"%s"' % (_QtIfwScript.MAINTENANCE_TOOL_NAME,)) + END + 
            EBLK + NEW +            
            'function maintenanceToolExists( dir ) ' + SBLK +
                TAB + 'return ' + _QtIfwScript.pathExists( 
                    'toMaintenanceToolPath( dir )', isAutoQuote=False ) + END + 
            EBLK + NEW +
            'function __defaultTargetExists() ' + SBLK +
                TAB + 'return maintenanceToolExists( ' + 
                    _QtIfwScript.targetDir() + ' )' + END +  
            EBLK + NEW +
            'function __cmdLineTargetExists() ' + SBLK +            
                TAB + 'return maintenanceToolExists( ' + 
                    _QtIfwScript.cmdLineArg( _QtIfwScript.TARGET_DIR_CMD_ARG ) +
                    ' )' + END +
            EBLK + NEW +
            'function targetExists() ' + SBLK +
            'var isAuto = ' + _QtIfwScript.cmdLineSwitchArg( 
                _QtIfwScript.AUTO_PILOT_CMD_ARG ) + END +                
            (TAB + 'if( isOsRegisteredProgram() ) ' + SBLK +
             (2*TAB)  + _QtIfwScript.log('The program is OS registered.') +
             (2*TAB) + 'return true' + END + 
            TAB + EBLK                  
            if IS_WINDOWS else '') +
            TAB + _QtIfwScript.ifCmdLineArg( 
                _QtIfwScript.TARGET_DIR_CMD_ARG, isMultiLine=True ) +
                'if( isAuto && __cmdLineTargetExists() )'  + SBLK +
                    (3*TAB) + _QtIfwScript.log('The command line specified target exists.') +
                    (3*TAB) + 'return true' + END +
                (2*TAB) + EBLK +
            TAB + EBLK +
            TAB + 'if( __defaultTargetExists() )'  + SBLK +
            TAB + _QtIfwScript.log('The default target exists.') +
            (2*TAB) + 'return true' + END +                
            TAB + EBLK +                   
            TAB + 'return false' + END +                 
            EBLK + NEW +            
            'function removeTarget() ' + SBLK +
           'var isAuto = ' + _QtIfwScript.cmdLineSwitchArg( 
                _QtIfwScript.AUTO_PILOT_CMD_ARG ) + END +                
            TAB + _QtIfwScript.log('Removing existing installation...') +
            TAB + 'var isElevated=true' + END +  
            TAB + 'var args=[ "-v", ' +                     
                '"' + _QtIfwScript.AUTO_PILOT_CMD_ARG + '=' +
                _QtIfwScript.TRUE + '" ' + 
                ', "' + _QtIfwScript.MAINTAIN_MODE_CMD_ARG + '=' + 
                _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL + '" ' 
                "]" + END +                
            TAB + _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.DRYRUN_CMD_ARG ) +
                'args.push( "' + _QtIfwScript.DRYRUN_CMD_ARG + '=true" )' + END +                     
            TAB + _QtIfwScript.ifCmdLineSwitch( _KEEP_TEMP_SWITCH ) +
                'args.push( "' + _KEEP_TEMP_SWITCH + '=true" )' + END +                
            TAB + 'var passthru=' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript.MAINTAIN_PASSTHRU_CMD_ARG ) + END +
            TAB + 'if( passthru == \"\" ) ' + NEW +
            (2*TAB) + 'passthru=' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript._CMD_ARGS_TEMP_PREFIX + 
                _QtIfwScript.MAINTAIN_PASSTHRU_CMD_ARG ) + END +            
            TAB + 'if( passthru != \"\" ) {' + NEW +
            (2*TAB) + 'passthru=Dir.fromNativeSeparator(passthru)' + END +
            (2*TAB) + 'passthru=passthru.replace(/`/g, \'\\"\')' + END +
            (2*TAB) + 'passthru=passthru.replace(/#/g, \'=\')' + END +
            (2*TAB) + 'passthru=passthru.split(\",\")' + END +            
            (2*TAB) + 'for( i=0; i < passthru.length; i++ )' + NEW +
                (3*TAB) + 'args.push( passthru[i] )' + END +            
            TAB + '}' + NEW +
            TAB + 'var exeResult' + END +
            (TAB + 'var regPaths = maintenanceToolPaths()' + END + 
             TAB + 'if( regPaths != null )' + SBLK +
            (2*TAB) + 'for( i=0; i < regPaths.length; i++ )' + SBLK +
                (3*TAB) + 'executeHidden( regPaths[i], args, isElevated )' + END +
            (2*TAB) + EBLK +                        
            TAB + EBLK +
            TAB + 'else '
            if IS_WINDOWS else TAB) +
            _QtIfwScript.ifCmdLineArg( 
                _QtIfwScript.TARGET_DIR_CMD_ARG ) +
                'executeHidden( toMaintenanceToolPath( ' +
                    _QtIfwScript.cmdLineArg( 
                _QtIfwScript.TARGET_DIR_CMD_ARG ) + ' ), args, isElevated )' + END +
            TAB + 'else ' + NEW +                        
            (2*TAB) + 'executeHidden( toMaintenanceToolPath( ' +
                    _QtIfwScript.targetDir() + ' ), args, isElevated )' + END +
            TAB + _QtIfwScript.ifDryRun() + 'return true' + END +            
            TAB + '// The MaintenanceTool is not removed until a moment\n' + 
            TAB + '// or two has elapsed after it was closed...' + NEW +
            TAB + _QtIfwScript.log('Verifying uninstall...') +    
            TAB + 'var MAX_CHECKS=3' + END  +
            TAB + 'for( var existCheck=0; existCheck < MAX_CHECKS; existCheck++ ) ' + SBLK +
            (2*TAB) + 'if( !targetExists() ) break' + END +
            (2*TAB) + _QtIfwScript.log('Waiting for uninstall to finish...') +                
            (2*TAB) + 'sleep( 1 )' + END +                
            TAB + EBLK +
            TAB + 'if( targetExists() ) ' + SBLK +
            (2*TAB) + 'if( isAuto ) ' + NEW +
                (3*TAB) + 'silentAbort("Failed to removed the program.")' + END +
            (2*TAB) + 'else ' + SBLK +
                (3*TAB) + _QtIfwScript.log('Failed to removed the program') +
                (3*TAB) + 'return false' + END +
            (2*TAB) + EBLK +
            TAB + EBLK +
            TAB + _QtIfwScript.log('Successfully removed the program.') +
            TAB + 'return true' + END +
            EBLK + NEW +
            'function __autoManagePriorInstallation() ' + SBLK +
            TAB + "if( targetExists() ) " + SBLK +            
            (2*TAB) + 'switch (' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG ) + ')' + SBLK +
            (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_FAIL + '":' + NEW +
                (3*TAB) + 'silentAbort("This program is already installed.")' + END + 
            (2*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_REMOVE + '":' + NEW + 
                (3*TAB) + 'removeTarget()' + END +
                (3*TAB) + 'break' + END +
            (2*TAB) + 'default:' + NEW +
                (3*TAB) + 'silentAbort("This program is already installed.")' + END +
              EBLK +           
            EBLK +                                         
            EBLK + NEW +          
            'function isElevated() ' + SBLK +      # TODO: Test on MAC
            TAB + 'var successEcho="success"' + END +
            TAB + 'var elevatedTestCmd = "' +
                ('echo off\\n' 
                 'fsutil dirty query %systemdrive% >nul'
                 ' && echo " + successEcho + "\\n"' 
                 if IS_WINDOWS else
                 '[ $(id -u) = 0 ] && echo " + successEcho' ) + END + #TODO: Test on MAC      
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], elevatedTestCmd' if IS_WINDOWS else
                 '"sh", ["-c", elevatedTestCmd]' ) + ' )' + END +
            TAB + 'var output=""' + END + 
            TAB + 'try' + SBLK +
            TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
            TAB + TAB + 'var output = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
            EBLK +
            TAB + 'catch(e){' + EBLK +                                        
            TAB + 'var isElev=output==successEcho' + END +
            #TAB + _QtIfwScript.log( '"isElevated: " + result[0] + ", " + result[1]', isAutoQuote=False )+
            TAB + _QtIfwScript.log( '"Has elevated privileges: " + isElev', isAutoQuote=False )+
            TAB + 'return isElev' + END +
            EBLK + NEW +                            
            'function getEnv( varName ) ' + SBLK +
            TAB + 'return installer.environmentVariable( varName )' + END +
            EBLK + NEW +
            'function parentDir( path ) ' + SBLK +
            TAB + 'var pathParts = Dir.fromNativeSeparator( path ).split("/")' + END +
            TAB + 'if( pathParts.length <= 1 ) return null' + END +
            TAB + 'return Dir.toNativeSeparator( ' +
                'pathParts.slice(0, pathParts.length-1).join("/") )' + END +
            EBLK + NEW +            
            'function fileName( filePath ) ' + SBLK +
            TAB + 'var pathParts = Dir.fromNativeSeparator( filePath ).split("/")' + END +
            TAB + 'return pathParts[pathParts.length-1]' + END +
            EBLK + NEW +
            'function rootFileName( filePath ) ' + SBLK +
            TAB + 'return fileName( filePath ).split(".")[0]' + END +
            EBLK + NEW +                                                            
            'function resolveNativePath( path, isSpaceEscaped ) ' + SBLK +    # TODO: Test in NIX/MAC  
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
            TAB + 'if( isSpaceEscaped && !isWindows() ) ' + NEW +
            (2*TAB) + 'path = path.replace(/ /g, \'\\\\ \')' + END +            
            TAB + 'return path' + END +                                                                                                                          
            EBLK + NEW +                        
            'function dirList( path, isSortByModTimeAsc ) ' + SBLK +    # TODO: Test in NIX/MAC
            TAB + 'var retList=[]' + END +
            TAB + 'var sortByTime = isSortByModTimeAsc ? ' + 
                ( '" /O:D"' if IS_WINDOWS else '"tr"' ) + 
                ' : ""' + END +
            TAB + 'path = resolveNativePath( path, true )' + END +
            TAB + 'var dirLsCmd = "' +
                ('echo off\\n'                     
                 'dir \\"" + path + "\\" /A /B" + sortByTime + "\\n'
                 if IS_WINDOWS else
                'ls -a" + sortByTime + " " + path + " | cat' ) + '"' + END +                
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], dirLsCmd' if IS_WINDOWS else
                 '"sh", ["-c", dirLsCmd]' ) + ' )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("dir list failed.")' + END +
            TAB + 'try' + SBLK +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            ((2*TAB) + 'cmdOutLns.splice(0, 2)' + END if IS_WINDOWS else '' ) +                                                                                    
            (2*TAB) + 'for( var i=0; i < cmdOutLns.length; i++ )' + SBLK +
                (3*TAB) + 'var entry = cmdOutLns[i].trim()' + END +                
                ((3*TAB) + 'entry = fileName( entry )' + END if not IS_WINDOWS else '' ) +                
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
            TAB + 'if( path==null ) return' + END +
            TAB + 'path = resolveNativePath( path )' + END +
            TAB + _QtIfwScript.ifPathExists( 'path', isAutoQuote=False ) + 
            (2*TAB) + 'return path' + END +                    
            TAB + 'var mkDirCmd = "' +
                ('echo off\\n'                     
                 'md \\"" + path + "\\"\\n' # implicitly recursive
                 'echo " + path + "\\n' 
                 if IS_WINDOWS else
                 'mkdir -p \\"" + path + "\\"; ' # -p = recursive
                 'echo \\"" + path + "\\"' ) + '"' + END +      
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], mkDirCmd' if IS_WINDOWS else
                 '"sh", ["-c", mkDirCmd]' ) + ' )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("makeDir failed. path: " + path )' + END +
            TAB + 'try' + SBLK +
            TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
            TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
            EBLK +
            TAB + 'catch(e){ path = "";' + EBLK +
            TAB + 'if( path=="" || !' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
            (2*TAB) + 'throw new Error("makeDir failed. path: " + path )' + END +
            TAB + _QtIfwScript.log( '"made dir: " + path', isAutoQuote=False ) + 
            TAB + 'return path' + END +                                                                                                               
            EBLK + NEW +                
            'function removeDir( path ) ' + SBLK +        # TODO: Test in NIX/MAC
            TAB + 'if( path==null ) return' + END +                  
            TAB + 'path = resolveNativePath( path )' + END +
            TAB + _QtIfwScript.ifPathExists( 'path', isNegated=True, isAutoQuote=False ) + 
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
            (2*TAB) + 'throw new Error("removeDir failed. path: " + path )' + END +
            TAB + 'try' + SBLK +
            TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
            TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + 
            EBLK +
            TAB + 'catch(e){ path = "";' + EBLK +
            TAB + 'if( path=="" || ' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
            (2*TAB) + 'throw new Error("removeDir failed. path: " + path )' + END +
            TAB + _QtIfwScript.log( '"removed dir: " + path', isAutoQuote=False ) + 
            TAB + 'return path' + END +                                                                                                               
            EBLK + NEW +                            
            'function __writeScriptFromBase64( fileName, b64, varNames, isDoubleBackslash, isTempRootTarget, isB64Removed ) ' + SBLK +  # TODO: Test in NIX/MAC                
            TAB + 'var path = __writeFileFromBase64( fileName, b64, isTempRootTarget, isB64Removed )' + END +
            TAB + 'replaceDynamicVarsInFile( path, varNames, isDoubleBackslash )' +  END +            
            EBLK + NEW +                                                                         
            'function __writeFileFromBase64( fileName, b64, isTempRootTarget, isB64Removed ) ' + SBLK +      # TODO: Test in NIX/MAC
            TAB + 'var dirPath = isTempRootTarget ? __envTempPath() : Dir.temp()' + END +            
            TAB + 'var tempPath = Dir.toNativeSeparator( dirPath + "/" + fileName + ".b64" )' + END +
            TAB + 'var path = Dir.toNativeSeparator( dirPath + "/" + fileName )' + END +            
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
            TAB + 'if( isB64Removed ) deleteFile( tempPath )' + END +
            TAB + 'return path' + END +                                                                                                               
            EBLK + NEW + # TODO: Test in NIX/MAC                
            'function __replaceDynamicVarsInFileScript( path, varNames, isDoubleBackslash ) ' + SBLK + 
            (
            TAB + 'var path = Dir.toNativeSeparator( path )' + END +                
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
            (2*TAB) + 'var varVal = Dir.toNativeSeparator( installer.value( varName, "' + 
                                        QT_IFW_UNDEF_VAR_VALUE + '" ) )' + END +
            (2*TAB) + 'if( isDoubleBackslash ) varVal = varVal.replace(/\\\\/g, \'\\\\\\\\\')' + END +
            (2*TAB) + 'vbs += "sText = Replace(sText, Amp + \\"" + varName + "\\" + Amp, \\"" + varVal + "\\")\\n"' + NEW +
            TAB + EBLK +
            TAB + 'vbs += ' + NEW +                
            (2*TAB) + '"Set oFile = oFSO.OpenTextFile(sFileName, ForWriting)\\n" + ' + NEW +
            (2*TAB) + '"oFile.Write sText\\n" + ' + NEW + #vbs WriteLine adds extra CR/LF
            (2*TAB) + '"oFile.Close\\n"' + END +
            TAB + 'return vbs' + END 
            if IS_WINDOWS else 
            TAB + '' + END) + # TODO: FILLIN in NIX/MAC
            EBLK + NEW +                                                                         
            'function replaceDynamicVarsInFile( path, varNames, isDoubleBackslash ) ' + SBLK + # TODO: Test in NIX/MAC
            TAB + 'var script = __replaceDynamicVarsInFileScript( path, varNames, isDoubleBackslash )' + END +
            (
            TAB + 'executeVbScript( script )' + END 
            if IS_WINDOWS else 
            TAB + '' + END) + # TODO: FILLIN in NIX/MAC
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
            'function __escapeEchoText( echo ) ' + SBLK +
            (TAB + 'if( echo.trim()=="" ) return "."' + END if IS_WINDOWS else '' ) +
            TAB + 'var escaped = echo' + END +                      
            TAB + 'return " " + escaped' + END +                                                                                          
            EBLK + NEW +      
            'function writeFile( path, content ) ' + SBLK +    
            TAB + 'if( path==null ) return' + END +        
            TAB + 'path = resolveNativePath( path )' + END +
            TAB + 'var dirPath = parentDir( path )' + END +
            TAB + _QtIfwScript.ifPathExists( 'dirPath', isNegated=True, isAutoQuote=False ) + 
                (2*TAB) + _QtIfwScript.makeDir( 'dirPath', isAutoQuote=False ) +                    
            TAB + 'var lines = content.split(\"\\n\")' + END +                                             
            TAB + 'var redirect = " >"' + END +      
            TAB + 'var writeCmd = ""' + END +
            (TAB + 'writeCmd += "echo off && "' + END if IS_WINDOWS else "" ) +
            TAB + 'for( i=0; i < lines.length; i++ )' + SBLK +                
            (2*TAB) + 'var echo = __escapeEchoText( lines[i] )' + END +
            (2*TAB) + 'writeCmd += "echo" + echo + redirect + ' + NEW +
                (3*TAB) + '" \\"" + path + "\\"' + ('\\n"' if IS_WINDOWS else ';"' ) + END +
            (2*TAB) + 'redirect = " >>"' + END +                                               
            TAB + EBLK + 
            ( TAB + 'var uname = __realUserName()' + END +
              TAB + 'writeCmd += "chown " + uname + ":" + uname + " \\"" + path + "\\";"' + END +
              TAB + 'writeCmd += "chmod 777 \\"" + path + "\\";"' + END 
              if not IS_WINDOWS else '' ) + 
            TAB + 'writeCmd += "echo " + path' + 
                    ( '+ "\\n"' if IS_WINDOWS else '' ) + END +                                  
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], writeCmd' if IS_WINDOWS else
                 '"sh", ["-c", writeCmd]' ) + ' )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Write file failed. path: " + path )' + END +
            TAB + 'try' + SBLK +
            TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +                
            TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + EBLK + 
            TAB + 'catch(e){ path = "";' + EBLK +
            TAB + 'if( path=="" || !' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
            (2*TAB) + 'throw new Error("Write file failed. path: " + path )' + END +
            TAB + _QtIfwScript.log( '"Wrote file to: " + path', isAutoQuote=False ) +
            TAB + 'return path' + END +
            EBLK + NEW +                   
            'function deleteFile( path ) ' + SBLK +
            TAB + 'if( path==null ) return' + END +
            TAB + 'path = resolveNativePath( path )' + END +      
            TAB + _QtIfwScript.ifPathExists( 'path', isNegated=True, isAutoQuote=False ) +
                'return' + END +                  
            TAB + 'var deleteCmd = "' +                    
                ('echo off && del \\"" + path + "\\" /q\\necho " + path + "\\n"' 
                 if IS_WINDOWS else
                 '[ -f \\"" + path + "\\" ] && rm -f \\"" + path + "\\"; echo " + path' ) + END +                                                                                                
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], deleteCmd' if IS_WINDOWS else
                 '"sh", ["-c", deleteCmd]' ) + ' )' + END +             
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Delete file failed. path: " + path )' + END +
            TAB + 'try' + SBLK +
            TAB + TAB + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            TAB + TAB + 'path = cmdOutLns[cmdOutLns.length-2].trim()' + END + EBLK + 
            TAB + 'catch(e){ path = "";' + EBLK +                
            TAB + 'if( path=="" || ' + _QtIfwScript.pathExists( 'path', isAutoQuote=False ) + ' ) ' + NEW +
            (2*TAB) + 'throw new Error("Delete file failed. path: " + path )' + END +
            TAB + _QtIfwScript.log( '"Deleted file: " + path', isAutoQuote=False ) + 
            TAB + 'return path' + END +                                                                                                                                       
            EBLK + NEW +                                                                     
            'function clearOutLog() ' + SBLK + 
            TAB + 'deleteFile( ' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript.OUT_LOG_PATH_CMD_ARG,
                _QtIfwScript.OUT_LOG_DEFAULT_PATH ) + ' )' + END + 
            EBLK + NEW +                           
            'function writeOutLog( msg ) ' + SBLK +
            TAB + 'writeFile( ' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript.OUT_LOG_PATH_CMD_ARG,
                _QtIfwScript.OUT_LOG_DEFAULT_PATH ) + ', msg )' + END +
            EBLK + NEW +
            'function clearErrorLog() ' + SBLK + 
            TAB + 'deleteFile( ' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript.ERR_LOG_PATH_CMD_ARG,
                _QtIfwScript.ERR_LOG_DEFAULT_PATH ) + ' )' + END + 
            EBLK + NEW +                           
            'function writeErrorLog( msg ) ' + SBLK +
            TAB + 'writeFile( ' + _QtIfwScript.cmdLineArg( 
                _QtIfwScript.ERR_LOG_PATH_CMD_ARG,
                _QtIfwScript.ERR_LOG_DEFAULT_PATH ) + ', msg )' + END +
            EBLK + NEW +
            'function silentAbort( msg ) ' + SBLK +
            TAB + 'console.log( msg )' + END +
            TAB + 'writeErrorLog( msg )' + END +
            TAB + 'throw new Error( msg )' + END +                    
            EBLK + NEW +                        
            'function abort( msg ) ' + SBLK +            
            TAB + 'msg = (msg==null || msg=="" ? "Installation aborted! Closing installer..." : msg)' + END +
            TAB + 'console.log( msg )' + END +
            TAB + 'writeErrorLog( msg )' + END +
            TAB + 'QMessageBox.critical("errorbox", "Error", msg, QMessageBox.Ok)' + END +
            TAB + 'installer.autoAcceptMessageBoxes()' + END +
            TAB + 'gui.clickButton(buttons.CancelButton)' + END +
            TAB + 'gui.clickButton(buttons.FinishButton)' + END +                
            TAB + '' + END +                    
            EBLK + NEW +
            'function quit( msg, isError, isSilent ) ' + SBLK +
            TAB + 'if( msg ) console.log( msg )' + END +
            TAB + 'if( msg && isError ) writeErrorLog( msg )' + END +
            TAB + _QtIfwScript.ifAutoPilot() + TAB + 'isSilent=true' + END +            
            TAB + 'if( !isSilent ) ' +  SBLK +
            (2*TAB) + 'msg = (msg==null || msg=="" ? "Click \\"OK\\" to quit..." : msg)' + END +
            (2*TAB) + 'QMessageBox.warning("warnbox", "Installation canceled", msg, QMessageBox.Ok)' + END +
            TAB + EBLK +
            TAB + 'installer.autoAcceptMessageBoxes()' + END +
            TAB + 'gui.clickButton(buttons.CancelButton)' + END +
            TAB + 'gui.clickButton(buttons.FinishButton)' + END +                
            TAB + '' + END +                    
            EBLK + NEW +
            'function getComponent( name ) ' + SBLK +
            TAB + 'var comps=installer.components()' + END +
            TAB + 'for( i=0; i< comps.length; i++ ) ' + SBLK +
            (2*TAB) + 'if( comps[i].name == name ) return comps[i]' + END +
            TAB + EBLK + 
            TAB + 'throw new Error("Component not found: " + name )' + END +
            EBLK + NEW +
            'function isComponentInstalled( name ) ' + SBLK +
            TAB + 'try{ return getComponent( name ).installed; }' + NEW +
            TAB + 'catch(e){ console.log("Component not found: " + name ); }' + NEW +
            TAB + 'return false' + END +
            EBLK + NEW +
            'function isComponentEnabled( name ) ' + SBLK +
            TAB + 'try{ return getComponent( name ).enabled; }' + NEW +
            TAB + 'catch(e){ console.log("Component not found: " + name ); }' + NEW +
            TAB + 'return false' + END +
            EBLK + NEW +                        
            'function enableComponent( name, isEnable ) ' + SBLK +
            TAB + 'try{ getComponent( name ).enabled =( isEnable==null ? false : isEnable ); }' + NEW +
            TAB + 'catch(e){ console.log("Component not found: " + name ); }' + NEW +
            EBLK + NEW +                                                
            'function isComponentSelected( name ) ' + SBLK +
            TAB + 'try{ return getComponent( name ).installationRequested(); }' + NEW +
            TAB + 'catch(e){ console.log("Component not found: " + name ); }' + NEW +
            TAB + 'return false' + END +
            EBLK + NEW +                                   
            'function getPageOwner( pageName ) ' + SBLK +
            TAB + 'var comps=installer.components()' + END +
            TAB + 'for( i=0; i < comps.length; i++ ) ' + SBLK +
            (2*TAB) + 'var owner = comps[i]' + END +
            (2*TAB) + 'for( j=0; j < comps[i].userInterfaces.length; j++ ) ' + SBLK +
                (3*TAB) + 'var page = comps[i].userInterfaces[j]' + END +
                (3*TAB) + 'if( page == pageName ) return owner' + END +
            (2*TAB) + EBLK +
            TAB + EBLK + 
            TAB + 'throw new Error("Owner not found for page: " + pageName )' + END +
            EBLK + NEW +
            'function insertCustomWidget( widgetName, pageId, position ) ' + SBLK +
            TAB + 'try{ installer.addWizardPageItem( ' +
                'getPageOwner( widgetName ), widgetName, pageId, position ); }' + NEW +
            TAB + 'catch(e){ console.log("Warning: Cannot insert widget: " + widgetName ); }' + NEW +                
            EBLK + NEW +
            'function removeCustomWidget( widgetName ) ' + SBLK +
            TAB + 'try{ installer.removeWizardPageItem( getPageOwner( widgetName ), widgetName ); }' + NEW +
            TAB + 'catch(e){ console.log("Warning: Cannot remove widget: " + widgetName ); }' + NEW +
            EBLK + NEW +                                                                                    
            'function insertCustomPage( pageName, position ) ' + SBLK +
            TAB + 'try{ installer.addWizardPage( ' +
                'getPageOwner( pageName ), pageName, position ); }' + NEW +
            TAB + 'catch(e){ console.log("Warning: Cannot insert page: " + pageName ); }' + NEW +                
            EBLK + NEW +
            'function removeCustomPage( pageName ) ' + SBLK +
            TAB + 'try{ installer.removeWizardPage( getPageOwner( pageName ), pageName ); }' + NEW +
            TAB + 'catch(e){ console.log("Warning: Cannot remove page: " + pageName ); }' + NEW +
            EBLK + NEW +                                                
            'function setCustomPageText( page, title, description ) {' + NEW +
            '    page.windowTitle = title;' + NEW +
            '    if( description ){' + NEW +
            '        page.description.setText( description );' + NEW +
            '        page.description.setVisible( true );' + NEW +
            '    }' + NEW +
            '    else{' + NEW +
            '        page.description.setVisible( false );' + NEW +
            '        page.description.setText( "" );' + NEW +
            '    }' + NEW +
            EBLK + NEW +
            'function execute( binPath, args ) ' + SBLK +
            TAB + 'var cmd = "\\"" + binPath + "\\""' + END +
            TAB + 'if( args ) ' + SBLK +  
            (2*TAB) + 'for( i=0; i < args.length; i++ )' + NEW +
                (3*TAB) + 'cmd += (" " + args[i])' + END +
            EBLK +    
            TAB + _QtIfwScript.log( '"Executing: " + cmd', isAutoQuote=False ) +
            TAB + 'return installer.execute( binPath, args )' + END +
            EBLK + NEW +
            'function executeDetached( binPath, args ) ' + SBLK +
            TAB + 'var cmd = "\\"" + binPath + "\\""' + END +
            TAB + 'if( args ) ' + SBLK +  
            (2*TAB) + 'for( i=0; i < args.length; i++ )' + NEW +
                (3*TAB) + 'cmd += (" " + args[i])' + END +
            EBLK +    
            TAB + _QtIfwScript.log( '"Executing: " + cmd', isAutoQuote=False ) +
            TAB + 'return installer.executeDetached( binPath, args )' + END +
            EBLK + NEW +              
            'function executeShellCmdDetached( cmd ) ' + SBLK +
            #TAB + 'cmd = "\\"" + cmd + "\\""' + END +
            TAB + _QtIfwScript.log( '"Executing Command Detached: " + cmd', isAutoQuote=False ) +
            TAB + 'return installer.executeDetached( ' +
                ('"cmd.exe", ["/c", cmd]' if IS_WINDOWS else
                 '"sh", ["-c", cmd]' ) + ' )' + END +                                  
            EBLK + NEW +              
            'function executeHidden( binPath, args, isElevated ) ' + SBLK + # TODO: Test in NIX/MAC 
            (                 
            (TAB+ 'var ps = "Start-Process -FilePath \'" + binPath + "\' ' +
                            '-Wait -WindowStyle Hidden"' + END +
            TAB + 'if( isElevated ) ps += " -Verb RunAs"' + END +
            TAB + 'if( args ) ' + NEW +  
            (2*TAB) + 'ps += " -ArgumentList " + "\'" + args.join("\',\'") + "\'"' + END +            
            TAB + 'executePowerShell( ps )' + END ) 
            if IS_WINDOWS else 
            (TAB + 'var shell = ""' + END +            
            TAB + 'var wasXvfbInstalled = isPackageInstalled( "Xvfb" ) ||'
                                     + ' isPackageInstalled( "xvfb" )' + END +
            TAB + 'if( !wasXvfbInstalled )' + SBLK +
            (2*TAB) + _QtIfwScript.log( 'Installing Xvfb utility (temporarily)...') +            
            (2*TAB) + 'var isXvfbInstalled = installPackage( "Xvfb" ) ||'
                                         + ' installPackage( "xvfb" )' + END +
            (2*TAB) + 'if( isXvfbInstalled ) ' + NEW +
                (3*TAB) + _QtIfwScript.log( '...Installed Xvfb.') +
            (2*TAB) + ELSE + NEW +
                (3*TAB) + 'quit( "Could not install required utility: Xvfb", true )' + END +                                         
            EBLK +
            NEW +                  
            TAB + '// Note: isElevated is already applied in the standard use case context. ' + NEW +
            TAB + '// *Dropping back to the real user* would be the thing to optionally enforce...' + NEW +
            TAB + 'var XVFB_RUN = "xvfb-run"' +  END +            
            TAB + 'var xvfbArgs = []' +  END +
            TAB + 'xvfbArgs.push( binPath )' +  END +
            TAB + 'for( i=0; i < args.length; i++ ) xvfbArgs.push( args[i] )' + END +
            TAB + 'var xvfbCmd = XVFB_RUN + " " + binPath' +  END +            
            TAB + 'for( i=0; i < xvfbArgs.length; i++ ) xvfbCmd += " " + xvfbArgs[i]' + END +
            _QtIfwScript.log( '"Invoking gui process on an offscreen frame buffer with: " '
                              '+ xvfbCmd', isAutoQuote=False ) +                                             
            TAB + 'var result = installer.execute( XVFB_RUN, xvfbArgs )' +  END +
            NEW +
            TAB + 'if( !wasXvfbInstalled )' + SBLK +
            (2*TAB) + _QtIfwScript.log( '(Politely) Uninstalling Xvfb...') +            
            (2*TAB) + 'var isXvfbUnInstall = unInstallPackage( "Xvfb" ) ||'
                   + ' unInstallPackage( "xvfb" )' + END +
            (2*TAB) + 'if( isXvfbUnInstall ) ' + NEW +
                (3*TAB) + _QtIfwScript.log( '...Uninstalled Xvfb.') +    
            (2*TAB) + ELSE + NEW +                   
                (3*TAB) + _QtIfwScript.log( 'Could NOT uninstall Xvfb!') +
            TAB + EBLK +                                  
            TAB + 'if( result[1] != 0 ) ' + NEW  +
                'quit( "Could not run xvfb sub process", true )' + END                                                                                                                      
            )
            if IS_LINUX else
            (TAB + '// The hidden feature is not yet supported on macOS!' + NEW +
            TAB + 'execute( binPath, args )' + END )
            ) +              
            EBLK + NEW +
            # TODO: Test in NIX/MAC                              
            'function assertInternetConnected( isRefresh, errMsg ) ' + SBLK +
            TAB + 'if( !isInternetConnected( isRefresh ) )' + NEW +
            (2*TAB) + 'quit( errMsg ? errMsg : ' +
                            '"An internet connection is required!", true )' + END +
            EBLK + NEW +           
            # TODO: Test in NIX/MAC                              
            'function isInternetConnected( isRefresh ) ' + SBLK +
            TAB + 'var isNet = installer.value( "' + 
                _QtIfwScript.IS_NET_CONNECTED_KEY + '", "" )' + END +
            TAB + 'if( isRefresh || isNet === "" ) ' + SBLK +                                    
            (2*TAB) + 'isNet = "" + isPingable( "www.google.com", 1, 5 )' + END +
            (2*TAB) + 'installer.setValue( "' + 
                _QtIfwScript.IS_NET_CONNECTED_KEY + '", isNet )' + END + 
            (2*TAB) + _QtIfwScript.log( 'isNet==="true" ? "connected to the internet" : ' +
                                        '"NOT connected to the internet"', 
                                        isAutoQuote=False ) +                             
            TAB + EBLK +                
            TAB + 'return isNet==="true";' + END +
            EBLK + NEW +           
            # TODO: Test in NIX/MAC                                                                   
            'function isPingable( uri, pings, totalMaxSecs ) ' + SBLK +
            TAB + 'if( uri==null ) return false' + END +
            TAB + 'if( pings==null ) pings=3' + END +
            TAB + 'if( totalMaxSecs==null ) totalMaxSecs=12' + END +
            TAB + _QtIfwScript.log( '"Pinging: " + uri + " ..."', isAutoQuote=False ) +
            TAB + 'var successOutput = "success"' + END +
            TAB + 'var pingCmd = "' +                    
                ('echo off && ping -n " + pings + " ' +
                 '-w " + ((1000 * totalMaxSecs)/pings) + " " +'
                 'uri + " | findstr /r /c:\\"[0-9] *ms\\" > nul && ' +  # see https://ss64.com/nt/ping.html 
                 'echo " + successOutput +"\\n"'         # regarding test for success
                 if IS_WINDOWS else 
                 'ping -n " + pings + " ' +              # TODO: check syntax in NIX/MAC
                 '-w " + totalMaxSecs + " " +'  +        # see https://linux.die.net/man/8/ping
                 'uri + " | grep \\"TTL\\" > nul && ' +  # align this grep with the Windows regex findstr above!
                 'echo " + successOutput'  ) + END +                                                                                                
            TAB + 'var result = installer.execute( ' +
                ('"cmd.exe", ["/k"], pingCmd' if IS_WINDOWS else
                 '"sh", ["-c", pingCmd]' ) + ' )' + END +             
            TAB + 'var output' + END +
            TAB + TRY +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            (2*TAB) + 'output = cmdOutLns[1].trim()' + END + EBLK + 
            TAB + CATCH + 'output = null;' + EBLK +
            TAB + 'var isSuccess = output==successOutput' + END +                            
            TAB + _QtIfwScript.log( 'isSuccess ? "...response received" : ' +
                                    '"... NO response received"', 
                                    isAutoQuote=False ) + 
            TAB + 'return isSuccess' + END +                  
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
            regQueryUninstallKeys =( 
                '@echo off & for /f delims^=^ eol^= %i in ('
                '\\\'REG QUERY HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Uninstall\\\\ '
                '/s /f \\"" + installer.value("ProductName") + "\\" /t REG_SZ /c /e '
                '^| find \\"HKEY_CURRENT_USER\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Uninstall\\\\\\"\\\')'
                ' do ( for /f \\"tokens=2*\\" %a in (\\\'REG QUERY %i /v \\"UninstallString\\" '
                '^| find \\"UninstallString\\"\\\') do echo %b )\\n' 
            )          
            self.qtScriptLib += (                
            'function registryEntryValue( key, valueName, isAutoBitContext ) ' + SBLK +
            TAB + _QtIfwScript.log( "Registry entry value query" ) + 
            TAB + _QtIfwScript.log( '"    key: " + key', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    valueName: " + valueName', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isAutoBitContext: " + isAutoBitContext', isAutoQuote=False ) +            
            TAB + 'if( !installer.gainAdminRights() ) ' + NEW +
            (2*TAB) + 'throw new Error("Elevated privileges required.")' + END +
            TAB + 'if( !registryEntryExists( key, valueName, isAutoBitContext ) )' + NEW +
            (2*TAB) + 'return null' + END +         
            TAB + 'var keySearch = " \\"" + key + "\\""' + END +       
            TAB + 'var valSearch = valueName==null ? " /VE " : '
                '" /V \\"" + valueName + "\\""' + END +        
            TAB + 'var bitContext = isAutoBitContext===false ? " /reg:64" : ""' + END +            
            TAB + 'var regQuery = "for /f \\"tokens=2*\\" %a in '
                '(\'REG QUERY" + keySearch + valSearch + bitContext + '
                    '" ^| FINDSTR \\"REG_\\"\') do @echo %b\\n"' + END +
            TAB + 'var result = installer.execute( "cmd.exe", ["/k"], regQuery )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Registry query failed.")' + END +
            TAB + TRY +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            (2*TAB) + 'value = cmdOutLns[1].trim()' + END + EBLK + 
            TAB + CATCH + 'value = null;' + EBLK +                
            TAB + _QtIfwScript.log( '"Registry value: " + value', isAutoQuote=False ) + 
            TAB + 'return value' + END +                  
            EBLK + NEW +
            'function registryEntryExists( key, valueName, isAutoBitContext ) ' + SBLK +            
            TAB + _QtIfwScript.log( "Registry entry exists query" ) + 
            TAB + _QtIfwScript.log( '"    key: " + key', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    valueName: " + valueName', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isAutoBitContext: " + isAutoBitContext', isAutoQuote=False ) +            
            TAB + 'if( !installer.gainAdminRights() ) ' + NEW +
            (2*TAB) + 'throw new Error("Elevated privileges required.")' + END +            
            TAB + 'var existsOutput = "exists"' + END +
            TAB + 'var keySearch = " \\"" + key + "\\""' + END +
            TAB + 'var valSearch = valueName==null ? " /VE " : '
                '" /V \\"" + valueName + "\\""' + END +        
            TAB + 'var bitContext = isAutoBitContext===false ? " /reg:64" : ""' + END +            
            TAB + 'var regQuery = "@echo off & REG QUERY" + keySearch + valSearch + '
                    'bitContext + '
                    '" 1>nul 2>&1 && echo " + existsOutput + "\\n"' + END + 
            TAB + 'var result = installer.execute( "cmd.exe", ["/k"], regQuery )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Registry query failed.")' + END +
            TAB + 'var output' + END +
            TAB + TRY +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            (2*TAB) + 'output = cmdOutLns[1].trim()' + END + EBLK + 
            TAB + CATCH + 'output = null;' + EBLK +
            TAB + 'var exists = output==existsOutput' + END +                            
            TAB + _QtIfwScript.log( '"Registry value exists: " + exists', isAutoQuote=False ) + 
            TAB + 'return exists' + END +                  
            EBLK + NEW +
            'function registryEntryExistsLike( key, valueNameContains, isAutoBitContext, '
                'isCaseSensitive, isRecursive ) ' + SBLK +            
            TAB + _QtIfwScript.log( "Registry entry exists query" ) + 
            TAB + _QtIfwScript.log( '"    key: " + key', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    valueNameContains: " + valueNameContains', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isAutoBitContext: " + isAutoBitContext', isAutoQuote=False ) +            
            TAB + _QtIfwScript.log( '"    isCaseSensitive: " + isCaseSensitive', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isRecursive: " + isRecursive', isAutoQuote=False ) +                                    
            TAB + 'if( !installer.gainAdminRights() ) ' + NEW +
            (2*TAB) + 'throw new Error("Elevated privileges required.")' + END +            
            TAB + 'var existsOutput = "exists"' + END +
            TAB + 'var keySearch = " \\"" + key + "\\""' + END +
            TAB + 'var valSearch = " /F \\"" + valueNameContains + "\\""' + END +        
            TAB + 'var bitContext = isAutoBitContext===false ? " /reg:64" : ""' + END +            
            TAB + 'var caseSens = isCaseSensitive ? " /C" : ""' + END +
            TAB + 'var subSearch = isRecursive ? " /S" : ""' + END +                        
            TAB + 'var regQuery = "@echo off & REG QUERY" + keySearch + valSearch + '
                    'bitContext + caseSens + subSearch + '
                    '" 1>nul 2>&1 && echo " + existsOutput + "\\n"' + END + 
            TAB + 'var result = installer.execute( "cmd.exe", ["/k"], regQuery )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Registry query failed.")' + END +
            TAB + 'var output' + END +
            TAB + TRY +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            (2*TAB) + 'output = cmdOutLns[1].trim()' + END + EBLK + 
            TAB + CATCH + 'output = null;' + EBLK +
            TAB + 'var exists = output==existsOutput' + END +                            
            TAB + _QtIfwScript.log( '"Registry value exists: " + exists', isAutoQuote=False ) + 
            TAB + 'return exists' + END +                  
            EBLK + NEW +
            'function registryKeyExists( key, isAutoBitContext ) ' + SBLK +            
            TAB + _QtIfwScript.log( "Registry key exists query" ) + 
            TAB + _QtIfwScript.log( '"    key: " + key', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isAutoBitContext: " + isAutoBitContext', isAutoQuote=False ) +            
            TAB + 'if( !installer.gainAdminRights() ) ' + NEW +
            (2*TAB) + 'throw new Error("Elevated privileges required.")' + END +            
            TAB + 'var existsOutput = "exists"' + END +
            TAB + 'var keySearch = " \\"" + key + "\\" /VE"' + END +        
            TAB + 'var bitContext = isAutoBitContext===false ? " /reg:64" : ""' + END +
             TAB + 'var regQuery = "@echo off & REG QUERY" + keySearch + bitContext + '                
                    '" 1>nul 2>&1 && echo " + existsOutput + "\\n"' + END + 
            TAB + 'var result = installer.execute( "cmd.exe", ["/k"], regQuery )' + END +
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Registry query failed.")' + END +
            TAB + 'var output' + END +
            TAB + TRY +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            (2*TAB) + 'output = cmdOutLns[1].trim()' + END + EBLK + 
            TAB + CATCH + 'output = null;' + EBLK +
            TAB + 'var exists = output==existsOutput' + END +                            
            TAB + _QtIfwScript.log( '"Registry key exists: " + exists', isAutoQuote=False ) + 
            TAB + 'return exists' + END +                  
            EBLK + NEW +
            'function registryKeyExistsLike( parentKey, childKeyNameContains, '
                'isAutoBitContext, isCaseSensitive, isRecursive ) ' + SBLK +            
            TAB + _QtIfwScript.log( "Registry entry exists query" ) + 
            TAB + _QtIfwScript.log( '"    parentKey: " + parentKey', isAutoQuote=False ) +            
            TAB + _QtIfwScript.log( '"    childKeyNameContains: " + childKeyNameContains', isAutoQuote=False ) +            
            TAB + _QtIfwScript.log( '"    isAutoBitContext: " + isAutoBitContext', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isCaseSensitive: " + isCaseSensitive', isAutoQuote=False ) +
            TAB + _QtIfwScript.log( '"    isRecursive: " + isRecursive', isAutoQuote=False ) +            
            TAB + 'if( !installer.gainAdminRights() ) ' + NEW +
            (2*TAB) + 'throw new Error("Elevated privileges required.")' + END +            
            TAB + 'var existsOutput = "exists"' + END +
            TAB + 'var keySearch = " \\"" + parentKey + "\\" /K /F \\"" + childKeyNameContains + "\\""' + END +        
            TAB + 'var bitContext = isAutoBitContext===false ? " /reg:64" : ""' + END +            
            TAB + 'var caseSens = isCaseSensitive ? " /C" : ""' + END +
            TAB + 'var subSearch = isRecursive ? " /S" : ""' + END +                        
            TAB + 'var regQuery = "@echo off & REG QUERY" + keySearch + bitContext + '
                    'caseSens + subSearch + '
                    '" 1>nul 2>&1 && echo " + existsOutput + "\\n"' + END + 
            TAB + 'var result = installer.execute( "cmd.exe", ["/k"], regQuery )' + END +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("Registry query failed.")' + END +
            TAB + 'var output' + END +
            TAB + TRY +
            (2*TAB) + 'var cmdOutLns = result[0].split(\"\\n\")' + END +
            (2*TAB) + 'output = cmdOutLns[1].trim()' + END + EBLK + 
            TAB + CATCH + 'output = null;' + EBLK +
            TAB + 'var exists = output==existsOutput' + END +                            
            TAB + _QtIfwScript.log( '"Registry key exists: " + exists', isAutoQuote=False ) + 
            TAB + 'return exists' + END +                  
            EBLK + NEW +
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
            EBLK + NEW +                           
            'function executeBatchDetached( scriptPath, bat, args ) ' + SBLK +
            TAB + _QtIfwScript.log( "Executing Detached Batch:" ) +
            TAB + _QtIfwScript.log( "scriptPath", isAutoQuote=False ) +                
            TAB + _QtIfwScript.log( "bat", isAutoQuote=False ) +          
            TAB + 'var path = bat ? writeFile( scriptPath, bat ) : '
                        'Dir.toNativeSeparator( scriptPath )' + END +                 
            TAB + 'if( !args ) args=[]' + END +
            TAB + 'args.unshift( path )' + END +
            TAB + 'args.unshift( "/c" )' + END +
            TAB + 'var result = installer.executeDetached( "cmd.exe", args )' + END +
            EBLK + NEW +                        
            'function executeVbScript( vbs ) ' + SBLK +
            TAB + _QtIfwScript.log( "Executing VbScript:" ) +
            TAB + _QtIfwScript.log( "vbs", isAutoQuote=False ) +          
            TAB + 'var path = writeFile( __tempRootFilePath( "vbs" ), vbs )' + END +
            TAB + 'var result = installer.execute(' + 
                '"cscript", ["//Nologo", path])' + END +
            TAB + _QtIfwScript.log( 
                '"> Script return code: " + (result.length==2 ? result[1] : "?" )', 
                isAutoQuote=False ) + 
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("VBScript operation failed.")' + END +
            TAB + 'for( i=0; i < 3; i++ )' + SBLK +
            (2*TAB) + 'try{ deleteFile( path ); break; }' + NEW +                          
            (2*TAB) + 'catch(e){ sleep(1); }' + NEW +
            TAB + EBLK + NEW +
            EBLK + NEW +
            'function executeVbScriptDetached( scriptPath, vbs, args ) ' + SBLK + 
            # TODO: add args implementation
            TAB + _QtIfwScript.log( "Executing Detached VbScript:" ) +
            TAB + _QtIfwScript.log( "scriptPath", isAutoQuote=False ) +                
            TAB + _QtIfwScript.log( "vbs", isAutoQuote=False ) +          
            TAB + 'var path = vbs ? writeFile( scriptPath, vbs ) : '
                        'Dir.toNativeSeparator( scriptPath )' + END +                             
            TAB + 'var result = installer.executeDetached(' + 
                '"cscript", ["//Nologo", path])' + END +
            EBLK + NEW +            
            'function executePowerShell( ps ) ' + SBLK +
            TAB + _QtIfwScript.log( "Executing PowerShell Script:" ) +
            TAB + _QtIfwScript.log( "ps", isAutoQuote=False ) +          
            TAB + 'var path = writeFile( __tempRootFilePath( "ps1" ), ps )' + END +
            TAB + 'var result = installer.execute(' + 
                '"powershell", ["-NoLogo", "-ExecutionPolicy", "Bypass", ' +
                                '"-InputFormat", "None", "-File", path])' + END +
            TAB + _QtIfwScript.log( 
                '"> Script return code: " + (result.length==2 ? result[1] : "?" )', 
                isAutoQuote=False ) +                
            TAB + 'if( result[1] != 0 ) ' + NEW +
            (2*TAB) + 'throw new Error("PowerShell operation failed.")' + END +
            TAB + 'for( i=0; i < 3; i++ )' + SBLK +
            (2*TAB) + 'try{ deleteFile( path ); break; }' + NEW +                          
            (2*TAB) + 'catch(e){ sleep(1); }' + NEW +
            TAB + EBLK + NEW +
            EBLK + NEW +
            'function executePowerShellDetached( scriptPath, ps, args ) ' + SBLK + 
            # TODO: add args implementation
            TAB + _QtIfwScript.log( "Executing Detached PowerShell Script:" ) +
            TAB + _QtIfwScript.log( "scriptPath", isAutoQuote=False ) +                
            TAB + _QtIfwScript.log( "ps", isAutoQuote=False ) +          
            TAB + 'var path = ps ? writeFile( scriptPath, ps ) : '
                        'Dir.toNativeSeparator( scriptPath )' + END +                             
            TAB + 'var result = installer.executeDetached(' + 
                '"powershell", ["-NoLogo", "-ExecutionPolicy", "Bypass", ' +
                                '"-InputFormat", "None", "-File", path])' + END +
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

    __CONTROLER_PAGE_CHANGED_CALLBACK_FUNC_TMPLT =(            
"""
Controller.prototype.onCurrentPageChanged = function(pageId){
    %s
}
""")

    __CONTROLER_VALUE_CHANGED_CALLBACK_FUNC_TMPLT =(            
"""
Controller.prototype.onValueChanged = function(key,value){
    %s
}
""")

    __CONTROLER_PAGE_INSERT_REQUESTED_CALLBACK_FUNC_TMPLT =(            
"""
Controller.prototype.onWizardPageInsertionRequested = function(page, pageId){
    %s
}
""")

    __CONTROLER_PAGE_REMOVE_REQUESTED_CALLBACK_FUNC_TMPLT =(            
"""
Controller.prototype.onWizardPageRemovalRequested = function(page){
    %s
}
""")

    __CONTROLER_PAGE_VISIBILITY_REQUESTED_CALLBACK_FUNC_TMPLT =(            
"""
Controller.prototype.onWizardPageVisibilityChangeRequested = function(isVisible, pageId){
    %s
}
""")

    __CONTROLER_FINISHED_CLICKED_CALLBACK_FUNC_TMPLT=(            
"""
Controller.prototype.onFinishButtonClicked = function(){
    %s
}
""")

    __CONTROLER_CONNECT_TMPLT = ( 
        "%s.connect(this, Controller.prototype.%s);\n" ) 
    __WIDGET_CONNECT_TMPLT = ( 
        "gui.currentPageWidget().%s.%s.connect(this, this.%s);\n" )

    __CURRENT_PAGE_WIDGET = "gui.currentPageWidget()"
    __CUR_PG_WIDGET_VAR_TMPLT = "    var %s = gui.currentPageWidget();\n"

    __PAGE_WIDGET_BY_ID = 'gui.pageById(QInstaller.%s)'
    __PAGE_WIDGET_BY_ID_VAR_TMPLT = ( 
        '    var %s = gui.pageById(QInstaller.%s);\n' )

    __PAGE_WIDGET = 'gui.pageWidgetByObjectName("%s")'
    __PAGE_WIDGET_VAR_TMPLT = ( 
        '    var %s = gui.pageWidgetByObjectName("%s");\n' )

    __CUSTOM_PAGE_WIDGET = 'gui.pageWidgetByObjectName("Dynamic%s")'
    __CUSTOM_PAGE_WIDGET_VAR_TMPLT = ( 
        '    var %s = gui.pageWidgetByObjectName("Dynamic%s");\n' )
                                    
    __CLICK_BUTTON_TMPL       = "gui.clickButton(%s);\n"
    __CLICK_BUTTON_DELAY_TMPL = "gui.clickButton(%s, %d);\n"

    __TO_PAGE_CONSTANT_TMPLT = 'QInstaller.%s' 

    __HIDE_PAGE_TMPLT = ( 
        'installer.setDefaultPageVisible(QInstaller.%s, false);\n' ) 
      
    __INSERT_PAGE_TMPLT = 'insertCustomPage("%s", QInstaller.%s);\n'
    __REMOVE_PAGE_TMPLT = 'removeCustomPage("%s");\n'
 
    __SET_ENABLE_STATE_TMPL = (
        "gui.currentPageWidget().%s.setEnabled(%s);\n" )    
    __GET_ENABLE_STATE_TMPL = (
        "gui.currentPageWidget().%s.enabled" )
    
    __SET_VISIBLE_STATE_TMPL = (
        "gui.currentPageWidget().%s.setVisible(%s);\n" )    
    __GET_VISIBLE_STATE_TMPL = (
        "gui.currentPageWidget().%s.visible" )
    
    __SET_CHECKBOX_STATE_TMPL = (
        "gui.currentPageWidget().%s.setChecked(%s);\n" )    
    __GET_CHECKBOX_STATE_TMPL = (
        "gui.currentPageWidget().%s.checked" )

    __SET_TEXT_TMPL = (
        "gui.currentPageWidget().%s.setText(%s);\n" )       
    __GET_TEXT_TMPL = "gui.currentPageWidget().%s.text"

    __ASSIGN_TEXT_TMPL = "    var %s = gui.currentPageWidget().%s.text;\n" 

    __INSERT_PAGE_ITEM_TMPLT = 'insertCustomWidget( "%s", QInstaller.%s, %s );\n' 
    __REMOVE_PAGE_ITEM_TMPLT = 'removeCustomWidget( "%s" );\n' 

    __ENABLE_NEXT_BUTTON_TMPL = "gui.currentPageWidget().complete=%s;\n" 
    
    __SET_CUSTPAGE_TITLE_TMPL = "%s.windowTitle = %s;\n" 

    __SET_CUSTPAGE_ENABLE_STATE_TMPL  = "%s.%s.setEnabled(%s);\n"     
    __GET_CUSTPAGE_ENABLE_STATE_TMPL = "%s.%s.enabled"
    
    __SET_CUSTPAGE_VISIBLE_STATE_TMPL = "%s.%s.setVisible(%s);\n" 
    __GET_CUSTPAGE_VISIBLE_STATE_TMPL = "%s.%s.visible"
    
    __SET_CUSTPAGE_CHECKBOX_STATE_TMPL = "%s.%s.setChecked(%s);\n" 
    __GET_CUSTPAGE_CHECKBOX_STATE_TMPL = "%s.%s.checked" 
    
    __SET_CUSTPAGE_TEXT_TMPL = "%s.%s.setText(%s);\n"        
    __GET_CUSTPAGE_TEXT_TMPL = "%s.%s.text"

    __SET_CUSTPAGE_CORE_TEXT_TMPL = "setCustomPageText( %s, %s, %s );\n" 

    __UI_PAGE_CALLBACK_FUNC_TMPLT = (
"""
Controller.prototype.Dynamic%sCallback = function() {
%s
}
"""    )

    __OPEN_VIA_OS_TMPL = "QDesktopServices.openUrl( resolveDynamicVars( %s ) );\n"
        
    __SELECT_ALL_COMPONENTS_TMPL     = "page.selectAll();\n"
    __DESELECT_ALL_COMPONENTS_TMPL   = "page.deselectAll();\n"    
    __SELECT_DEFAULT_COMPONENTS_TMPL = "page.selectDefault();\n"
    __SELECT_COMPONENT_TMPL          = "page.selectComponent( %s );\n"
    __DESELECT_COMPONENT_TMPL        = "page.deselectComponent( %s );\n"
                  
    BACK_BUTTON     = "buttons.BackButton"
    NEXT_BUTTON     = "buttons.NextButton"
    COMMIT_BUTTON   = "buttons.CommitButton"
    FINISH_BUTTON   = "buttons.FinishButton"
    CANCEL_BUTTON   = "buttons.CancelButton"
    HELP_BUTTON     = "buttons.HelpButton"
    CUSTOM_BUTTON_1 = "buttons.CustomButton1"
    CUSTOM_BUTTON_2 = "buttons.CustomButton2"
    CUSTOM_BUTTON_3 = "buttons.CustomButton3"
    
    # Don't seem to exist!?
    #ADD_REMOVE_RADIO_BUTTON = "PackageManagerRadioButton"
    #UPDATE_RADIO_BUTTON     = "UpdaterRadioButton"
    #UNINSTALL_RADIO_BUTTON  = "UninstallerRadioButton"

    TARGET_DIR_EDITBOX       = "TargetDirectoryLineEdit"
    START_MENU_DIR_EDITBOX   = "StartMenuPathLineEdit"
    ACCEPT_EULA_RADIO_BUTTON = "AcceptLicenseRadioButton"
    RUN_PROGRAM_CHECKBOX     = "RunItCheckBox"
    
    FINISHED_MESSAGE_LABEL   = "MessageLabel"
    DEFAULT_FINISHED_MESSAGE = "Click finish to exit the @ProductName@ Wizard."
                                    
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
    def pageWidget( pageId ): 
        return QtIfwControlScript.__PAGE_WIDGET_BY_ID % (pageId,)     

    @staticmethod        
    def customPageWidget( name ): 
        return QtIfwControlScript.__CUSTOM_PAGE_WIDGET % (name,)     

    @staticmethod        
    def assignCurrentPageWidgetVar( varName="page" ):                
        return QtIfwControlScript.__CUR_PG_WIDGET_VAR_TMPLT % (varName,)            

    @staticmethod        
    def assignPageWidgetVar( pageId, varName="page" ):                
        return QtIfwControlScript.__PAGE_WIDGET_BY_ID_VAR_TMPLT % (varName,pageId)            

    @staticmethod        
    def assignCustomPageWidgetVar( pageName, varName="page" ):                
        return QtIfwControlScript.__CUSTOM_PAGE_WIDGET_VAR_TMPLT % (
                varName, pageName )                        

    @staticmethod
    def toDefaultPageId( pageName ): 
        return QtIfwControlScript.__TO_PAGE_CONSTANT_TMPLT % (pageName,)

    @staticmethod
    def hideDefaultPage( pageName ): 
        return QtIfwControlScript.__HIDE_PAGE_TMPLT % (pageName,)

    @staticmethod        
    def insertCustomPage( pageName, position ):                
        return QtIfwControlScript.__INSERT_PAGE_TMPLT % (pageName, position)                        

    @staticmethod        
    def removeCustomPage( pageName ):                
        return QtIfwControlScript.__REMOVE_PAGE_TMPLT % (pageName,)                        

    @staticmethod        
    def insertCustomWidget( widgetName, pageName, position=None ):
        return  QtIfwControlScript.__INSERT_PAGE_ITEM_TMPLT % (
            widgetName, pageName, _QtIfwScript.toNull( position ) )

    @staticmethod        
    def removeCustomWidget( widgetName ):
        return  QtIfwControlScript.__REMOVE_PAGE_ITEM_TMPLT % (widgetName,)
            
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
        """ DOES NOT WORK FOR WIZARD BUTTONS!!! """                
        return QtIfwControlScript.__SET_ENABLE_STATE_TMPL % ( 
            controlName, _QtIfwScript.toBool( isEnable ) )

    @staticmethod        
    def isEnabled( controlName ):
        return QtIfwControlScript.__GET_ENABLE_STATE_TMPL % (controlName,)
        
    @staticmethod        
    def ifEnabled( controlName, isNegated=False, isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            QtIfwControlScript.isEnabled( controlName ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def setVisible( controlName, isVisible=True ):
        """ DOES NOT WORK FOR WIZARD BUTTONS!!! """                
        return QtIfwControlScript.__SET_VISIBLE_STATE_TMPL % ( 
            controlName, _QtIfwScript.toBool( isVisible ) )

    @staticmethod        
    def isVisible( controlName ):
        return QtIfwControlScript.__GET_VISIBLE_STATE_TMPL % (controlName,)
        
    @staticmethod        
    def ifVisible( controlName, isNegated=False, isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            QtIfwControlScript.isVisible( controlName ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
        
    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def setChecked( checkboxName, isCheck=True ):
        return QtIfwControlScript.__SET_CHECKBOX_STATE_TMPL % ( 
            checkboxName, _QtIfwScript.toBool( isCheck ) )

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def isChecked( checkboxName ):
        return QtIfwControlScript.__GET_CHECKBOX_STATE_TMPL % ( 
            checkboxName )
        
    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def ifChecked( checkboxName, isNegated=False, isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            QtIfwControlScript.isChecked( checkboxName ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def setText( controlName, text, varNames=None, 
                 isAutoQuote=True ):
        text =( _QtIfwScript._autoQuote( text, isAutoQuote ) 
                if varNames==False else
                _QtIfwScript.resolveDynamicVars( text, varNames, isAutoQuote ) )        
        return QtIfwControlScript.__SET_TEXT_TMPL % ( controlName, text )

    @staticmethod        
    def getText( controlName ):                
        return QtIfwControlScript.__GET_TEXT_TMPL % (controlName,)   

    @staticmethod        
    def enableNextButton( isEnable=True ):
        """ ONLY WORKS ON DYNAMIC / CUSTOM PAGES! """
        return QtIfwControlScript.__ENABLE_NEXT_BUTTON_TMPL % ( 
            _QtIfwScript.toBool( isEnable ) )

    @staticmethod        
    def setCustomPageTitle( title, isAutoQuote=True, pageVar="page" ):                
        return QtIfwControlScript.__SET_CUSTPAGE_TITLE_TMPL % ( pageVar, 
                _QtIfwScript._autoQuote( title, isAutoQuote ) )

    @staticmethod        
    def setCustomPageText( title, description, isAutoQuote=True, pageVar="page" ):
        if title is None: title=""
        if description is None: description="" 
        return QtIfwControlScript.__SET_CUSTPAGE_CORE_TEXT_TMPL % ( pageVar, 
                _QtIfwScript._autoQuote( title, isAutoQuote ), 
                _QtIfwScript._autoQuote( description, isAutoQuote ) )
    
    @staticmethod        
    def enableCustom( controlName, isEnable=True, pageVar="page" ):
        """ DOES NOT WORK FOR WIZARD BUTTONS!!! """                
        return QtIfwControlScript.__SET_CUSTPAGE_ENABLE_STATE_TMPL % ( pageVar, 
            controlName, _QtIfwScript.toBool( isEnable ) )

    @staticmethod        
    def isCustomEnabled( controlName, pageVar="page" ):
        return QtIfwControlScript.__GET_CUSTPAGE_ENABLE_STATE_TMPL % ( 
            pageVar, controlName )

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def ifCustomEnabled( controlName, pageVar="page", isNegated=False, 
                         isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            QtIfwControlScript.isCustomEnabled( controlName, pageVar ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )
        
    @staticmethod        
    def setCustomVisible( controlName, isVisible=True, pageVar="page" ):
        """ DOES NOT WORK FOR WIZARD BUTTONS!!! """                
        return QtIfwControlScript.__SET_CUSTPAGE_VISIBLE_STATE_TMPL % ( pageVar, 
            controlName, _QtIfwScript.toBool( isVisible ) )
        
    @staticmethod        
    def isCustomVisible( controlName, pageVar="page" ):
        return QtIfwControlScript.__GET_CUSTPAGE_VISIBLE_STATE_TMPL % ( 
            pageVar, controlName )

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def ifCustomVisible( controlName, pageVar="page", isNegated=False, 
                         isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            QtIfwControlScript.isCustomVisible( controlName, pageVar ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def setCustomCheckBox( checkboxName, isCheck=True, pageVar="page" ):
        return QtIfwControlScript.__SET_CUSTPAGE_CHECKBOX_STATE_TMPL % ( pageVar, 
            checkboxName, _QtIfwScript.toBool( isCheck ) )

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def isCustomChecked( checkboxName, pageVar="page" ):
        return QtIfwControlScript.__GET_CUSTPAGE_CHECKBOX_STATE_TMPL % ( 
            pageVar, checkboxName )

    # Note: checkbox controls also work on radio buttons!
    @staticmethod        
    def ifCustomChecked( checkboxName, pageVar="page", isNegated=False, 
                         isMultiLine=False ):   
        return 'if( %s%s )%s\n%s' % (
            "!" if isNegated else "", 
            QtIfwControlScript.isCustomChecked( checkboxName, pageVar ),
            ("{" if isMultiLine else ""), (2*_QtIfwScript.TAB) )

    @staticmethod        
    def setCustomText( controlName, text, isAutoQuote=True, pageVar="page" ):                
        return QtIfwControlScript.__SET_CUSTPAGE_TEXT_TMPL % ( pageVar, 
                controlName, _QtIfwScript._autoQuote( text, isAutoQuote ) )

    @staticmethod        
    def getCustomText( controlName, pageVar="page" ):                
        return QtIfwControlScript.__GET_CUSTPAGE_TEXT_TMPL % (pageVar, controlName)   

    # componentSelectionPage ONLY
    @staticmethod        
    def selectComponent( package, isSelect=True, isAutoQuote=True ):
        name = package.name if isinstance( package, QtIfwPackage ) else package                      
        return( (QtIfwControlScript.__SELECT_COMPONENT_TMPL % (
                 _QtIfwScript._autoQuote( name, isAutoQuote ),)) 
                 if isSelect else
                 (QtIfwControlScript.__DESELECT_COMPONENT_TMPL % (
                 _QtIfwScript._autoQuote( name, isAutoQuote ),))                  
        )

    # componentSelectionPage ONLY
    @staticmethod        
    def selectAllComponents( isSelect=True ):
        return( QtIfwControlScript.__SELECT_ALL_COMPONENTS_TMPL  
                if isSelect else
                QtIfwControlScript.__SELECT_ALL_COMPONENTS_TMPL )                  

    # componentSelectionPage ONLY
    @staticmethod        
    def selectDefaultComponents():
        return QtIfwControlScript.__SELECT_DEFAULT_COMPONENTS_TMPL  
            
    @staticmethod        
    def openViaOs( path, isAutoQuote=True ):                
        return QtIfwControlScript.__OPEN_VIA_OS_TMPL % ( 
                _QtIfwScript._autoQuote( path, isAutoQuote ) )

    # QtIfwControlScript
    def __init__( self, 
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.isLimitedMaintenance = True        
        self.virtualArgs = None

        self.uiPages = []
        self.widgets = []

        self._wizardStyle = None
        self._isLicenseRequired = False
        self._installerResources = []
        self._maintenanceToolResources = []

        self.controllerGlobals = None
        self.isAutoGlobals = True
        
        self.controllerConstructorBody = None
        self.controllerConstructorInjection = None
        self.isAutoControllerConstructor = True

        self.onValueChangeCallbackBody = None
        self.onValueChangeCallbackInjection = None
        self.isAutoValueChangeCallBack = True
        
        self.onPageChangeCallbackBody = None
        self.onPageChangeCallbackInjection = None
        self.isAutoPageChangeCallBack = True
                
        self.onPageInsertRequestCallbackBody = None
        self.isAutoPageInsertRequestCallBack = True

        self.onPageRemoveRequestCallbackBody = None
        self.isAutoPageRemoveRequestCallBack = True

        self.onPageVisibilityRequestCallbackBody = None
        self.isAutoPageVisibilityRequestCallBack = True
        
        self.onFinishedClickedCallbackBody     = None
        self.onFinishedClickedCallbackInjection = None
        self.onFinishedDetachedExecutions = []
        self.isAutoFinishedClickedCallbackBody = True
            
        self.isIntroductionPageVisible = True                                                                    
        self.introductionPageCallbackBody = None
        self.introductionPageOnInstall = None
        self.introductionPageOnMaintain = None
        self.isAutoIntroductionPageCallback = True

        self.isTargetDirectoryPageVisible = True
        self.targetDirectoryPageCallbackBody = None
        self.isAutoTargetDirectoryPageCallback = True

        self.isComponentSelectionPageVisible = True
        self.componentSelectionPageCallbackBody = None
        self.componentSelectionPageInjection = None
        self.isAutoComponentSelectionPageCallback = True

        self.isLicenseAgreementPageVisible = True
        self.licenseAgreementPageCallbackBody = None
        self.isAutoLicenseAgreementPageCallback = True

        self.isStartMenuDirectoryPageVisible = True
        self.startMenuDirectoryPageCallbackBody = None
        self.isAutoStartMenuDirectoryPageCallback = True

        self.isReadyForInstallationPageVisible = True
        self.readyForInstallationPageCallbackBody = None
        self.readyForInstallationPageOnInstall = None
        self.readyForInstallationPageOnMaintain = None        
        self.isAutoReadyForInstallationPageCallback = True

        self.isPerformInstallationPageVisible = True
        self.performInstallationPageCallbackBody = None
        self.isAutoPerformInstallationPageCallback = True
        
        self.isFinishedPageVisible = True
        self.finishedPageCallbackBody = None
        self.finishedPageOnInstall = None
        self.finishedPageOnMaintain = None
        self.isAutoFinishedPageCallback = True        

        self.isRunProgVisible = True
        self.isRunProgEnabled = True
        self.isRunProgChecked = True

        self.__standardEventSlots = {}            
        self.__autoPilotEventSlots = {}
        self.__widgetEventSlots = {}

        self.registerStandardEventHandler( 
            'installationStarted', 'onInstallationStarted',
            _QtIfwScript.log("installationStarted") )
        self.registerStandardEventHandler( 
            'installationFinished', 'onInstallFinished',
            _QtIfwScript.log("installationFinished") )         
        self.registerStandardEventHandler( 
            'uninstallationFinished', 'onUninstallFinished',
            _QtIfwScript.log("uninstallationFinished") );                                                                 
        self.registerStandardEventHandler( 
            'updateFinished', 'onUpdateFinished',
            _QtIfwScript.log("updateFinished") );                                                           
        self.registerStandardEventHandler( 
            'installationInterrupted', 'onInstallationInterrupted',
            _QtIfwScript.log("installationInterrupted") +
            _QtIfwScript.setBoolValue(_QtIfwScript.INTERUPTED_KEY, True) +
            QtIfwControlScript._purgeTempFiles() );                                                                 
        self.registerGuiEventHandler( 
            'interrupted', 'onGuiInterrupted',
            _QtIfwScript.log("interrupted") +
            _QtIfwScript.setBoolValue(_QtIfwScript.INTERUPTED_KEY, True) +
            QtIfwControlScript._purgeTempFiles() );          
                                                                                   
        self.registerAutoPilotEventHandler( 
            'installationFinished', 'onAutoInstallFinished',
            _QtIfwScript.log("onAutoInstallFinished") +
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 
        self.registerAutoPilotEventHandler( 
            'uninstallationFinished', 'onAutoUninstallFinished',
            _QtIfwScript.log("onAutoUninstallFinished") +
            QtIfwControlScript.clickButton( QtIfwControlScript.NEXT_BUTTON ) );                                                                 
        self.registerAutoPilotEventHandler( 
            'updateFinished', 'onAutoUpdateFinished',
            _QtIfwScript.log("onAutoUpdateFinished") +
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
        self.script = _SCRIPT_LINE1_COMMENT
                        
        if self.isAutoLib: _QtIfwScript._genLib( self )        
        if self.qtScriptLib: self.script += self.qtScriptLib

        controlScripts =( self._maintenanceToolResources 
                          if self._maintenanceToolResources else [] )
        for w in self.widgets: 
            if( isinstance( w, QtIfwOnFinishedCheckbox ) and 
                isinstance( w.script, ExecutableScript ) ):
                controlScripts.append( w.script )                                                    
        for ex in self.onFinishedDetachedExecutions:
            if( isinstance( ex, QtIfwOnFinishedDetachedExec ) and 
                isinstance( ex.script, ExecutableScript ) ):
                controlScripts.append( ex.script )                                                                
        self.script += _QtIfwScript.embedResources( controlScripts )

        if self.isAutoGlobals: self.__genGlobals()
        if self.controllerGlobals: self.script += self.controllerGlobals
                                 
        if self.isAutoPageChangeCallBack: self.__genPageChangeCallbackBody()
        if self.onPageChangeCallbackBody:
            self.script += (
                QtIfwControlScript.__CONTROLER_PAGE_CHANGED_CALLBACK_FUNC_TMPLT % (
                self.onPageChangeCallbackBody, ) )
                            
        if self.isAutoValueChangeCallBack: self.__genValueChangeCallbackBody()
        if self.onValueChangeCallbackBody:        
            self.script += (
                QtIfwControlScript.__CONTROLER_VALUE_CHANGED_CALLBACK_FUNC_TMPLT % (
                self.onValueChangeCallbackBody, ) )

        if self.isAutoPageInsertRequestCallBack: self.__genPageInsertRequestCallbackBody()
        if self.onPageInsertRequestCallbackBody:        
            self.script += (
                QtIfwControlScript.__CONTROLER_PAGE_INSERT_REQUESTED_CALLBACK_FUNC_TMPLT % (
                self.onPageInsertRequestCallbackBody, ) )

        if self.isAutoPageRemoveRequestCallBack: self.__genPageRemoveRequestCallbackBody()
        if self.onPageRemoveRequestCallbackBody:        
            self.script += (
                QtIfwControlScript.__CONTROLER_PAGE_REMOVE_REQUESTED_CALLBACK_FUNC_TMPLT % (
                self.onPageRemoveRequestCallbackBody, ) )
                     
        if self.isAutoPageVisibilityRequestCallBack: self.__genPageVisibilityRequestCallbackBody()
        if self.onPageVisibilityRequestCallbackBody:        
            self.script += (
                QtIfwControlScript.__CONTROLER_PAGE_VISIBILITY_REQUESTED_CALLBACK_FUNC_TMPLT % (
                self.onPageVisibilityRequestCallbackBody, ) )

        if self.isAutoFinishedClickedCallbackBody: self.__genFinishedClickedCallbackBody()
        if self.onFinishedClickedCallbackBody:        
            self.script += (
                QtIfwControlScript.__CONTROLER_FINISHED_CLICKED_CALLBACK_FUNC_TMPLT % (
                self.onFinishedClickedCallbackBody, ) )
                                 
        if self.isAutoControllerConstructor:
            self.__genControllerConstructorBody()
        self.script += ('function Controller() {\n%s'
                        '    console.log("Controller constructed");\n}\n' % 
                         (self.controllerConstructorBody,) )
                            
        if self.isAutoIntroductionPageCallback:
            self.__genIntroductionPageCallbackBody()
        if self.introductionPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_INTRO_PAGE_CALLBACK_NAME, self.introductionPageCallbackBody) )
                        
        if self.isAutoTargetDirectoryPageCallback:
            self.__genTargetDirectoryPageCallbackBody()
        if self.targetDirectoryPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_TARGET_DIR_PAGE_CALLBACK_NAME, 
                 self.targetDirectoryPageCallbackBody) )

        if self.isAutoComponentSelectionPageCallback:
            self.__genComponentSelectionPageCallbackBody()
        if self.componentSelectionPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_COMPONENTS_PAGE_CALLBACK_NAME, 
                 self.componentSelectionPageCallbackBody) )

        if self.isAutoLicenseAgreementPageCallback:
            self.__genLicenseAgreementPageCallbackBody()
        if self.licenseAgreementPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_LICENSE_PAGE_CALLBACK_NAME, 
                 self.licenseAgreementPageCallbackBody) )

        if self.isAutoStartMenuDirectoryPageCallback:
            self.__genStartMenuDirectoryPageCallbackBody()
        if self.startMenuDirectoryPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_START_MENU_PAGE_CALLBACK_NAME, 
                 self.startMenuDirectoryPageCallbackBody) )

        if self.isAutoReadyForInstallationPageCallback:
            self.__genReadyForInstallationPageCallbackBody()
        if self.readyForInstallationPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_READY_PAGE_CALLBACK_NAME, 
                 self.readyForInstallationPageCallbackBody) )

        if self.isAutoPerformInstallationPageCallback:
            self.__genPerformInstallationPageCallbackBody()
        if self.performInstallationPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_INSTALL_PAGE_CALLBACK_NAME, 
                 self.performInstallationPageCallbackBody) )

        if self.isAutoFinishedPageCallback:
            self.__genFinishedPageCallbackBody()
        if self.finishedPageCallbackBody:
            self.script += ( QtIfwControlScript.__PAGE_CALLBACK_FUNC_TMPLT %
                (_QT_IFW_FINISHED_PAGE_CALLBACK_NAME, 
                 self.finishedPageCallbackBody) )

        for (funcName, funcBody) in itervalues( self.__standardEventSlots ):    
            self.script += ( 
                QtIfwControlScript.__CONTROLER_CALLBACK_FUNC_TMPLT %
                (funcName, funcBody) )

        for (funcName, funcBody) in itervalues( self.__autoPilotEventSlots ):    
            self.script += ( 
                QtIfwControlScript.__CONTROLER_CALLBACK_FUNC_TMPLT %
                (funcName, funcBody) )
        
        self.__appendUiPageFunctions()
        self.__appendWidgetFunctions()
        
    def __genValueChangeCallbackBody( self ):         
        #prepend = _QtIfwScript.log( '"Value Changed: " + key + "=" + value', isAutoQuote=False )
        prepend = ""
        append  = ""
        self.onValueChangeCallbackBody =( 
            prepend + 
            (self.onValueChangeCallbackInjection 
             if self.onValueChangeCallbackInjection else "") 
            + append )

    def __genPageInsertRequestCallbackBody( self ):
        self.onPageInsertRequestCallbackBody = _QtIfwScript.log( 
            '"page insert request before id:" + pageId', isAutoQuote=False ) 
        
    def __genPageRemoveRequestCallbackBody( self ):
        self.onPageRemoveRequestCallbackBody = _QtIfwScript.log( 
            '"page remove request"', isAutoQuote=False )  
    
    def __genPageVisibilityRequestCallbackBody( self  ):
        self.onPageVisibilityRequestCallbackBody = _QtIfwScript.log( 
            '"page visibility request isVisible " + isVisible + " id: " + pageId', 
            isAutoQuote=False )  

    def __genFinishedClickedCallbackBody( self ):
        TAB  = _QtIfwScript.TAB
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK
   
        prepend = _QtIfwScript.log( "finish clicked" )
        
        # Execute ui bound (user controlled) finished actions
        finshedCheckboxes = [ w for w in self.widgets 
                              if isinstance( w, QtIfwOnFinishedCheckbox ) ]
        if len(finshedCheckboxes) > 0:   
            prepend +=( TAB + 
                _QtIfwScript.ifBoolValue( _QtIfwScript.INTERUPTED_KEY, 
                                          isNegated=True, isMultiLine=True ) +
                (2*TAB) + _QtIfwScript.ifInstalling( isMultiLine=True ) 
            )
            for checkbox in finshedCheckboxes:
                prepend += ( (3*TAB) + 
                    QtIfwControlScript.ifChecked( 
                        checkbox.checkboxName, isMultiLine=True ) +
                        checkbox._action + 
                    EBLK ) 
            prepend += EBLK + EBLK

        # Execute other finished actions                
        finshedDetachedExecs=[e for e in self.onFinishedDetachedExecutions 
                              if isinstance( e, QtIfwOnFinishedDetachedExec )]
        if len(finshedDetachedExecs) > 0:   
            prepend +=( TAB + 
                _QtIfwScript.ifBoolValue( _QtIfwScript.INTERUPTED_KEY, 
                                          isNegated=True, isMultiLine=True ) 
            )
            for ex in finshedDetachedExecs:
                prepend += ( 
                    (2*TAB) + 
                    (SBLK 
                     if ex.event == QtIfwOnFinishedDetachedExec.ON_BOTH 
                     else _QtIfwScript.ifInstalling( isNegated =
                        ex.event==QtIfwOnFinishedDetachedExec.ON_UNINSTALL,
                        isMultiLine=True ) ) + 
                        (3*TAB) +
                        (SBLK 
                         if ex.ifCondition is None 
                         else _QtIfwScript.ifCondition( ex.ifCondition,
                            isMultiLine=True ) ) + 
                            ex._action +    
                        (3*TAB) + EBLK +                     
                    (2*TAB) + EBLK ) 
            prepend += EBLK 
        
        # Remove keep alive file     
        append =( 
            _QtIfwScript.ifMaintenanceTool( isNegated=True, isMultiLine=True ) +            
                _QtIfwScript.ifCmdLineArg( _QtIfwScript._KEEP_ALIVE_PATH_CMD_ARG ) +
                        _QtIfwScript.deleteFile( 
                            _QtIfwScript.cmdLineArg( _QtIfwScript._KEEP_ALIVE_PATH_CMD_ARG ), 
                            isAutoQuote=False ) +
            EBLK                
        )        
        
        self.onFinishedClickedCallbackBody =( 
            prepend + 
            (self.onFinishedClickedCallbackInjection 
             if self.onFinishedClickedCallbackInjection else "") 
            + append )
           
    def __genPageChangeCallbackBody( self ):
        TAB  = _QtIfwScript.TAB
        NEW  = _QtIfwScript.NEW_LINE 
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK                                    
        ELSE = _QtIfwScript.ELSE
        
        prepend =(
            TAB + _QtIfwScript.log( '"page changed to id: " + pageId', isAutoQuote=False ) +
            TAB + _QtIfwScript.ifInstalling( isMultiLine=True ) +
            (2*TAB) + _QtIfwScript.ifCondition( _QtIfwScript.lookupValue( 
                _QtIfwScript.TARGET_DIR_KEY ) + '==""' ) +
            (3*TAB) + _QtIfwScript.setValue( '"%s"' % (_QtIfwScript.TARGET_DIR_KEY,),                     
                    _QtIfwScript.lookupValue( _QtIfwScript.DEFAULT_TARGET_DIR_KEY ), 
                    isAutoQuote=False ) +                                    
            (2*TAB) + ('if( pageId == %s )' % (
                QtIfwControlScript.toDefaultPageId( 
                    QT_IFW_INTRO_PAGE),)) + SBLK +              
                    TAB + _QtIfwScript.ifElevated( isNegated=True ) +
                        _QtIfwScript.quit( "Elevated privileges required!", 
                                           isError=True, isSilent=True ) +
                (2*TAB) + EBLK +
            (      
            (2*TAB) + ('else if( pageId == %s )' % (
                QtIfwControlScript.toDefaultPageId( 
                    QT_IFW_INSTALL_PAGE),)) + SBLK +
                    (3*TAB) + "// Kludge to fix license installation permissions error " + NEW +              
                    (3*TAB) + QtIfwControlScript.makeDir( QT_IFW_TARGET_DIR ) +
                (2*TAB) + EBLK
            if self._isLicenseRequired else ""      
            ) +                                   
            TAB + EBLK +         
            TAB + ELSE + SBLK + 
            (2*TAB) + ('if( pageId == %s )' % (
                QtIfwControlScript.toDefaultPageId( 
                    QT_IFW_READY_PAGE),)) + SBLK +              
                    TAB + _QtIfwScript.ifElevated( isNegated=True ) +
                        _QtIfwScript.quit( "Elevated privileges required!", 
                                           isError=True, isSilent=True ) +
                (2*TAB) + EBLK +            
                TAB + EBLK
            )                 
        append  = ""

        preInstallPageNames=[]
        postInstallPageNames=[]                        
        for ui in self.uiPages:
            if isinstance( ui, QtIfwDynamicOperationsPage ): 
                if ui.pageOrder==QT_IFW_INSTALL_PAGE:
                    preInstallPageNames.append( ui.name )                                                 
                elif ui.pageOrder==QT_IFW_FINISHED_PAGE:          
                    postInstallPageNames.append( ui.name )
                 
        if len(preInstallPageNames) > 0:
            prepend +=(
                TAB + ('if( pageId == %s )' % (
                    QtIfwControlScript.toDefaultPageId( 
                        QT_IFW_INSTALL_PAGE),)) + SBLK 
            )
            for name in preInstallPageNames:                                                      
                prepend += QtIfwControlScript.removeCustomPage( name )
            prepend += EBLK 
        
        prepend +=(
            TAB + ('if( pageId == %s )' % (
                QtIfwControlScript.toDefaultPageId( 
                    QT_IFW_FINISHED_PAGE),)) + SBLK +                                    
            ((2*TAB) + QtIfwControlScript.hideDefaultPage( 
                QT_IFW_INSTALL_PAGE ) 
                if len(postInstallPageNames) > 0 else "")  +
                QtIfwControlScript._purgeTempFiles() +
            EBLK )
                             
        # TODO: Test this                             
        if self.widgets:             
            for w in self.widgets:
                onEnter = w._onEnterSnippet()
                if len(onEnter) > 0:    
                    prepend +=(
                        TAB + ('if( pageId == %s )' % (
                            QtIfwControlScript.toDefaultPageId( 
                                w.pageName ),)) + SBLK +
                            (2*TAB) + _QtIfwScript.log( 
                                "%s widget on page enter invoked" % (w.name,) ) +                                    
                            onEnter +
                        EBLK )
                                                                    
        self.onPageChangeCallbackBody =( 
            prepend +
            (self.onPageChangeCallbackInjection 
             if self.onPageChangeCallbackInjection else "")  
            + append )

    def __appendUiPageFunctions( self ):    
        if self.uiPages: 
            for p in self.uiPages:
                if p.supportScript: self.script += p.supportScript                             
                self.script += (                         
                    QtIfwControlScript.__UI_PAGE_CALLBACK_FUNC_TMPLT % 
                    ( p.name, p._onEnterSnippet() ) )

    def __appendWidgetFunctions( self ):    
        if self.widgets: 
            for w in self.widgets:
                if w.supportScript: self.script += w.supportScript                             

    def __genGlobals( self ):
        NEW = _QtIfwScript.NEW_LINE
        #END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK
        self.controllerGlobals = 'function initGlobals() ' + SBLK 
        if self.virtualArgs :
            for k,v in iteritems( self.virtualArgs ):            
                self.controllerGlobals += TAB + _QtIfwScript.setValue(k,v)  
        self.controllerGlobals += EBLK + NEW             
        
    def __genControllerConstructorBody( self ):
        NEW = _QtIfwScript.NEW_LINE
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK     
        self.controllerConstructorBody=""   
        if self.isLimitedMaintenance:
            self.controllerConstructorBody += (
                _QtIfwScript.ifMaintenanceTool() +
                    _QtIfwScript.setValue( _QtIfwScript.MAINTAIN_MODE_CMD_ARG,
                        _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL ) 
            )
        self.controllerConstructorBody += (            
            TAB + 'installer.setValue( ' + 
                ('"%s"' % (_QT_IFW_SCRIPTS_DIR,)) + ', "" )' + END + 
            TAB + 'installer.setValue( ' + 
                ('"%s"' % (_QT_IFW_INSTALLER_TEMP_DIR,)) + ', "" )' + END + 
            TAB + 'installer.setValue( ' + 
                ('"%s"' % (_QT_IFW_MAINTENANCE_TEMP_DIR,)) + ', "" )' + END +
            TAB + 'installer.setValue( "__isMaintenance", "" )' + END +            
            TAB + 'installer.setValue( "__lockFilePath", "" )' + END +
            TAB + 'installer.setValue( "__watchDogPath", "" )' + END +
            TAB + 'installer.setValue( "__realUserName", "" )' + END +            
            TAB + 'installer.setValue( "' + 
                _QtIfwScript.IS_NET_CONNECTED_KEY + '", "" )' + END +
            TAB + 'installer.setValue( ' +
                ('"%s"' % (_REMOVE_TARGET_KEY,) ) + ', "" )' + END +        
            TAB + ('if( getEnv("%s")=="true" )' % (_KEEP_TEMP_SWITCH,)) + NEW +
            (2*TAB) + _QtIfwScript.setBoolValue( _KEEP_TEMP_SWITCH, True ) +
            TAB + _QtIfwScript.setValue( _QtIfwScript._WIZARD_STYLE_KEY, 
                self._wizardStyle if self._wizardStyle else 
                QtIfwConfigXml._WizardStyles[QtIfwConfigXml.DEFAULT_WIZARD_STYLE] ) +   
            TAB + 'clearOutLog()' + END +
            TAB + 'clearErrorLog()' + END +
            TAB + _QtIfwScript.ifDryRun() + _QtIfwScript.setBoolValue( 
                _QtIfwScript.AUTO_PILOT_CMD_ARG, True ) +            
            TAB + _QtIfwScript.logValue( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +                                                 
            TAB + _QtIfwScript.logValue( _QtIfwScript.DRYRUN_CMD_ARG ) +  
            TAB + _QtIfwScript.logValue( _QtIfwScript.MAINTAIN_MODE_CMD_ARG ) +                    
            TAB + _QtIfwScript.logValue( _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.MAINTAIN_PASSTHRU_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.TARGET_DIR_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.TARGET_DIR_KEY ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.START_MENU_DIR_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.ACCEPT_EULA_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.INSTALL_LIST_CMD_ARG ) +            
            TAB + _QtIfwScript.logValue( _QtIfwScript.INCLUDE_LIST_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.EXCLUDE_LIST_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.RUN_PROGRAM_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.REBOOT_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.ERR_LOG_PATH_CMD_ARG ) +
            TAB + _QtIfwScript.logValue( _QtIfwScript.OUT_LOG_PATH_CMD_ARG ) +            
            TAB + _QtIfwScript.logValue( _KEEP_TEMP_SWITCH ) + 
            TAB + _QtIfwScript.logValue( _QtIfwScript._KEEP_ALIVE_PATH_CMD_ARG ) +            
            TAB + '__realUserName()' + END +
            TAB + '__installerTempPath()' + END +
            TAB + '__maintenanceTempPath()' + END +            
            TAB + 'makeDir( Dir.temp() )' + END +
            TAB + 'installer.setValue( ' + 
                ('"%s"' % (_QT_IFW_SCRIPTS_DIR,)) + ', Dir.temp() )' + END + 
            _QtIfwScript.ifInstalling( isMultiLine=True ) +
                _QtIfwScript.setValue( '"%s"' % (_QT_IFW_DEFAULT_TARGET_DIR,),                     
                    _QtIfwScript.lookupValue( _QtIfwScript.TARGET_DIR_KEY ), 
                    isAutoQuote=False ) +                                    
                TAB + _QtIfwScript.ifCmdLineArg( 
                        _QtIfwScript.TARGET_DIR_CMD_ARG ) +
                    (2*TAB) + _QtIfwScript.setValue(
                        '"%s"' % (_QtIfwScript.TARGET_DIR_KEY,),                     
                        _QtIfwScript.cmdLineArg( _QtIfwScript.TARGET_DIR_CMD_ARG ), 
                        isAutoQuote=False ) +
            EBLK +                        
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
        
        def hidePage( pageName ): 
            self.controllerConstructorBody += (
                QtIfwControlScript.hideDefaultPage( pageName ) )
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
        if not self.isFinishedPageVisible:                                                                    
            hidePage( QT_IFW_FINISHED_PAGE )

        if self.onPageInsertRequestCallbackBody:                
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                    ("installer.wizardPageInsertionRequested", 
                     "onWizardPageInsertionRequested") 
                )        
        if self.onPageRemoveRequestCallbackBody:                
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                    ("installer.wizardPageRemovalRequested", 
                     "onWizardPageRemovalRequested") 
                )        
        if self.onPageVisibilityRequestCallbackBody:                
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                    ("installer.wizardPageVisibilityChangeRequested", 
                     "onWizardPageVisibilityChangeRequested") 
                )                        
        if self.onPageChangeCallbackBody:                
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                    ("installer.currentPageChanged", "onCurrentPageChanged") 
                )        
        if self.onValueChangeCallbackBody: 
            self.controllerConstructorBody += (               
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                    ("installer.valueChanged", "onValueChanged")                 
            )            
        if self.onFinishedClickedCallbackBody:                
            self.controllerConstructorBody += (               
                    QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                        ("installer.finishButtonClicked", "onFinishButtonClicked")                 
                )            
            
        for signalName, (slotName, _) in iteritems( self.__standardEventSlots ):    
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                (signalName, slotName) )            
            
        if self.controllerConstructorInjection: 
            self.controllerConstructorBody+=self.controllerConstructorInjection
            
        # auto pilot    
        self.controllerConstructorBody += _QtIfwScript.ifCmdLineSwitch( 
                _QtIfwScript.AUTO_PILOT_CMD_ARG, isMultiLine=True )             
        for signalName, (slotName, _) in iteritems( self.__autoPilotEventSlots ):    
            self.controllerConstructorBody += ( 
                QtIfwControlScript.__CONTROLER_CONNECT_TMPLT %
                (signalName, slotName) )                                                      
        self.controllerConstructorBody += (        
                TAB + 'var mode = ' + _QtIfwScript.cmdLineArg( 
                    _QtIfwScript.MAINTAIN_MODE_CMD_ARG ) + END + 
                TAB + _QtIfwScript.ifInstalling( isMultiLine=True ) + 
                    'switch( mode ) ' + SBLK +                            
                    (2*TAB) + 'case "' +                         
                        _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL + '":' + NEW +
                        (3*TAB) + 'if( targetExists() ) ' + SBLK +
                            (4*TAB) + 'removeTarget()' + END +                            
                            (4*TAB) + _QtIfwScript.quit( "",
                                           isError=False, isSilent=True ) +                          
                        (3*TAB) + EBLK +                                                                  
                        (3*TAB) + 'else ' + SBLK +
                            (4*TAB) + _QtIfwScript.quit( 
                                "The program is not installed.",
                                isError=True, isSilent=True ) +                          
                        (3*TAB) + EBLK +      
                        (3*TAB) + 'break' + END +
                    (2*TAB) + 'case "' + 
                        _QtIfwScript.MAINTAIN_MODE_OPT_ADD_REMOVE + '":' + NEW +
                    (2*TAB) + 'case "' + 
                        _QtIfwScript.MAINTAIN_MODE_OPT_UPDATE + '":' + NEW +
                        (3*TAB) + _QtIfwScript.quit( 
                            "The specified mode is not currently supported "
                            "with auto pilot enabled.",
                            isError=True, isSilent=True ) +
                        (3*TAB) + 'break' + END +                            
                    (2*TAB) + 'default:' + NEW +                         
                        (3*TAB) + '__autoManagePriorInstallation()' + END +
                    (2*TAB) + EBLK +
                TAB + EBLK +    
                TAB + 'else ' + SBLK +
                    (2*TAB) + 'switch( mode ) ' + SBLK +
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
            _QtIfwScript.log("IntroductionPageCallback") +            
            _QtIfwScript.ifInstalling( isMultiLine=True ) +
                _QtIfwScript.elevate() +
                (self.introductionPageOnInstall if
                 self.introductionPageOnInstall else "") +               
            _QtIfwScript.END_BLOCK +   
            _QtIfwScript.ELSE + _QtIfwScript.START_BLOCK +   
                (self.introductionPageOnMaintain if
                 self.introductionPageOnMaintain else "") +                
                ((QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) +
                    _QtIfwScript.EXIT_FUNCTION)
                if self.isLimitedMaintenance else "") +                     
            _QtIfwScript.END_BLOCK +               
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        ) 

    def __genTargetDirectoryPageCallbackBody( self ):
        self.targetDirectoryPageCallbackBody = (
            _QtIfwScript.log("TargetDirectoryPageCallback") +
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
            _QtIfwScript.log("ComponentSelectionPageCallback") +
            QtIfwControlScript.assignCurrentPageWidgetVar() +            
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
            _QtIfwScript.START_BLOCK +   
                (self.componentSelectionPageInjection if
                 self.componentSelectionPageInjection else "") +                
            _QtIfwScript.END_BLOCK +               
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        )

    def __genLicenseAgreementPageCallbackBody( self ):
        self.licenseAgreementPageCallbackBody = (
            _QtIfwScript.log("LicenseAgreementPageCallback") +
            _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
            '{\n' +                        
                QtIfwControlScript.setChecked( 
                    QtIfwControlScript.ACCEPT_EULA_RADIO_BUTTON ) +                 
                _QtIfwScript.TAB + QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) + 
            '    }\nelse{\n' +
                _QtIfwScript.ifCmdLineArg( 
                    _QtIfwScript.ACCEPT_EULA_CMD_ARG ) +  
                    _QtIfwScript.TAB +             
                    QtIfwControlScript.setChecked( 
                        QtIfwControlScript.ACCEPT_EULA_RADIO_BUTTON, 
                            _QtIfwScript.cmdLineSwitchArg(
                                _QtIfwScript.ACCEPT_EULA_CMD_ARG ) ) +
            '    }'                      
        )                         

    def __genStartMenuDirectoryPageCallbackBody( self ):
        self.startMenuDirectoryPageCallbackBody = (
            _QtIfwScript.log("StartMenuDirectoryPageCallback") +
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
        TAB = _QtIfwScript.TAB
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK             
        ELSE = _QtIfwScript.ELSE
        self.readyForInstallationPageCallbackBody = (
            _QtIfwScript.log("ReadyForInstallationPageCallback") +    
            _QtIfwScript.ifDryRun( isMultiLine=True ) + 
                _QtIfwScript.log( "Dry run completed." ) +
                (2*TAB) + 
                    _QtIfwScript.quit( "", isError=False, isSilent=True ) +
                (2*TAB) + " return;" +
            EBLK +
            _QtIfwScript.ifInstalling( isMultiLine=True ) +
                ("" if self.readyForInstallationPageOnInstall is None else
                 (2*TAB) + self.readyForInstallationPageOnInstall) +        
            EBLK +
            ELSE + SBLK +            
                _QtIfwScript.elevate() +            
                ("" if self.readyForInstallationPageOnMaintain is None else
                 (2*_QtIfwScript.TAB) + self.readyForInstallationPageOnMaintain) +       
            EBLK +            
            _QtIfwScript.ifInstalling( isMultiLine=True ) +              
                (2*TAB) + _QtIfwScript.ifBoolValue( 
                    _QtIfwScript._IS_CMD_ARGS_TEMP_KEY, isNegated=True,
                    isMultiLine=True ) 
        )
        # Ensure the volatile cmd args are not persisted during the install 
        # process, and thus carried forward into the maintenance tool context!
        for arg, defValue in iteritems( _QtIfwScript._CMD_ARGS ):
            self.readyForInstallationPageCallbackBody += (
                (2*TAB) + _QtIfwScript.setValue( '"%s"' % 
                    (_QtIfwScript._CMD_ARGS_TEMP_PREFIX + arg,), 
                    _QtIfwScript.lookupValue( arg, defValue ), isAutoQuote=False ) +
                (2*TAB) + _QtIfwScript.setValue( arg, defValue )                    
            )                
        self.readyForInstallationPageCallbackBody += (
                (2*TAB) + _QtIfwScript.setBoolValue( 
                    _QtIfwScript._IS_CMD_ARGS_TEMP_KEY, True ) +
            (2*TAB) + EBLK +
            EBLK +                                          
            _QtIfwScript.ifAutoPilot() +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON )  
        )                

    def __genPerformInstallationPageCallbackBody( self ):
        self.performInstallationPageCallbackBody = (
            _QtIfwScript.log("PerformInstallationPageCallback") +
            _QtIfwScript.ifAutoPilot() +
                QtIfwControlScript.clickButton( 
                    QtIfwControlScript.NEXT_BUTTON ) 
        )

    def __genFinishedPageCallbackBody( self ):
        TAB  = _QtIfwScript.TAB
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK
        ELSE = _QtIfwScript.ELSE        
        self.finishedPageCallbackBody = (                
            TAB + _QtIfwScript.log("FinishedPageCallback") + 
            TAB + _QtIfwScript.ifInstalling( isMultiLine=True )             
        )
        # restore args from temp 
        for arg, defValue in iteritems( _QtIfwScript._CMD_ARGS ):
            self.finishedPageCallbackBody += (
                _QtIfwScript.setValue( '"%s"' % (arg,), 
                    _QtIfwScript.lookupValue( 
                        _QtIfwScript._CMD_ARGS_TEMP_PREFIX + arg,
                        defValue ), 
                    isAutoQuote=False ) +
                _QtIfwScript.setValue(  
                   _QtIfwScript._CMD_ARGS_TEMP_PREFIX + arg, "" )                    
            )         
        self.finishedPageCallbackBody +=( 
                _QtIfwScript.setBoolValue( 
                    _QtIfwScript._IS_CMD_ARGS_TEMP_KEY, False ) +
            EBLK )
                    
        finshedCheckboxes = [ w for w in self.widgets 
                             if isinstance( w, QtIfwOnFinishedCheckbox ) ]        
        # on interrupt
        self.finishedPageCallbackBody += (
            TAB + _QtIfwScript.ifBoolValue( _QtIfwScript.INTERUPTED_KEY, isMultiLine=True ) +
                    QtIfwControlScript.setVisible( 
                        QtIfwControlScript.RUN_PROGRAM_CHECKBOX, False ) +
                (2*TAB) + QtIfwControlScript.setChecked( 
                        QtIfwControlScript.RUN_PROGRAM_CHECKBOX, False ) 
        )                        
        # TODO: Do something similar for all widgets, in some unified manner?
        # Perhaps an abstract onInterupted function?  
        for checkbox in finshedCheckboxes:
            self.finishedPageCallbackBody += ( checkbox.setVisible( False ) + 
                                               checkbox.setChecked( False ) )  
        self.finishedPageCallbackBody += EBLK 

        # else...                               
        self.finishedPageCallbackBody += (                                                                  
            TAB + ELSE + SBLK + 
                (2*TAB) + _QtIfwScript.ifInstalling( isMultiLine=True ) +
                    (3*TAB) + QtIfwControlScript.setVisible( 
                            QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                            self.isRunProgVisible ) +                  
                    (3*TAB) + QtIfwControlScript.enable( 
                            QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                            self.isRunProgEnabled ) +
                    ((3*TAB) + _QtIfwScript.ifCmdLineArg( 
                            _QtIfwScript.RUN_PROGRAM_CMD_ARG ) +               
                            _QtIfwScript.TAB + QtIfwControlScript.setChecked( 
                                QtIfwControlScript.RUN_PROGRAM_CHECKBOX, 
                                    _QtIfwScript.cmdLineSwitchArg(
                                        _QtIfwScript.RUN_PROGRAM_CMD_ARG ) )
                        if self.isRunProgChecked else                                  
                     (3*TAB) + QtIfwControlScript.setChecked( 
                                QtIfwControlScript.RUN_PROGRAM_CHECKBOX, False )                         
                    ) +
                    ("" if self.finishedPageOnInstall is None else
                    (2*TAB) + self.finishedPageOnInstall)         
                )
        for checkbox in finshedCheckboxes:
            if checkbox.isReboot: 
                self.finishedPageCallbackBody += ( 
                    (3*TAB) + QtIfwControlScript.ifVisible( 
                        checkbox.checkboxName ) +
                        (3*TAB) + _QtIfwScript._msgToSilentWrapper( 
                                                            _REBOOT_MSG )                      
            )             
        self.finishedPageCallbackBody += (                                                                
                (2*TAB) + EBLK +
                (2*TAB) + ELSE + SBLK +                 
                    ("" if self.finishedPageOnMaintain is None else
                    (2*TAB) + self.finishedPageOnMaintain) +                         
                (2*TAB) + EBLK +
            TAB + EBLK +                 
            TAB + _QtIfwScript.ifCmdLineSwitch( _QtIfwScript.AUTO_PILOT_CMD_ARG ) +
                TAB + QtIfwControlScript.clickButton( 
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

    __COMPONENT_CALLBACK_FUNC_TMPLT = (
"""
Component.prototype.%s = function(){
    %s
}
""" )
        
    __COMPONENT_LOADED_HNDLR_NAME = "componentLoaded"
            
    __ADD_OPERATION_TMPLT =( '    component.add%sOperation( "%s"%s%s );\n')            
    __ELEVATED = "Elevated"
            
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

    __ADD_VBS_OPERATION_TMPLT = "   addVbsOperation( component, %s, %s );\n"
    
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
          ADJANCENT_WIN_SHORTCUT         : QT_IFW_TARGET_DIR
        , DESKTOP_WIN_SHORTCUT           : QT_IFW_DESKTOP_DIR
        , STARTMENU_WIN_SHORTCUT         : QT_IFW_STARTMENU_DIR
        , THIS_USER_STARTUP_WIN_SHORTCUT : "@UserStartMenuProgramsPath@/Startup"
        , ALL_USERS_STARTUP_WIN_SHORTCUT : "@AllUsersMenuProgramsPath@/Startup"    
    }

    __MAC_SHORTCUT_LOCATIONS = {
          ADJANCENT_MAC_SHORTCUT : QT_IFW_TARGET_DIR
        , DESKTOP_MAC_SHORTCUT   : QT_IFW_DESKTOP_DIR
        , APPS_MAC_SHORTCUT      : "%s/%s" % (QT_IFW_HOME_DIR,"Applications") 
    }

    # these may not be correct on all distros?
    __X11_SHORTCUT_LOCATIONS = {
          ADJANCENT_X11_SHORTCUT : QT_IFW_TARGET_DIR
        , DESKTOP_X11_SHORTCUT   : QT_IFW_DESKTOP_DIR
        , APPS_X11_SHORTCUT      : "/usr/share/applications" 
    }   # ~/.local/share/applications - current user location?

    @staticmethod
    def _addVbsOperation( vbs, isElevated ): 
        return QtIfwPackageScript.__ADD_VBS_OPERATION_TMPLT % (
            _QtIfwScript.toBool( isElevated ), vbs )

    @staticmethod
    def _addReplaceVarsInFileOperation( path, varNames, isDoubleBackslash, 
                                        isElevated ):
        if IS_WINDOWS:
            vbs = '__replaceDynamicVarsInFileScript( %s, %s, %s )' % (
                path, varNames, _QtIfwScript.toBool( isDoubleBackslash ) )
            return QtIfwPackageScript._addVbsOperation( vbs, isElevated )                   
        else:
            return "" # TODO: FILLIN FOR NIX/MAc    
        
    @staticmethod                                         #args=[]
    def __winAddShortcut( location, exeName, command=None, args=None, 
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
                                command=None, args=None, 
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
    def __init__( self, pkgName, pkgVersion, pkgSubDirName=None,
                  shortcuts=None, bundledScripts=None,
                  externalOps=None, installResources=None,
                  uiPages=None, widgets=None,                    
                  fileName=DEFAULT_QT_IFW_SCRIPT_NAME,                  
                  script=None, scriptPath=None ) :
        _QtIfwScript.__init__( self, fileName, script, scriptPath )

        self.pkgName          = pkgName
        self.pkgVersion       = pkgVersion
        self.pkgSubDirName    = pkgSubDirName
        
        self.shortcuts        = shortcuts if shortcuts else [] 
        self.externalOps      = externalOps if externalOps else []
        self.killOps          = []
        self.preOpSupport     = None
        self.customOperations = None        
        self.bundledScripts   = bundledScripts if bundledScripts else []
        self.installResources = installResources if installResources else []

        self.uiPages          = uiPages if uiPages else []
        self.widgets          = widgets if widgets else []
                
        # Linux Only
        if IS_LINUX: self.isAskPassProgRequired = False

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

        self.componentCreateOperationsForArchiveBody = None
        self.isAutoComponentCreateOperationsForArchive=True       

    # TODO: Provide more control over the order - relative to external ops, etc.
    #        (search for current use)
    def addSimpleOperation( self, name, parms=None, isElevated=False, isAutoQuote=True ):
        if self.customOperations is None: self.customOperations= ""        
        if parms is not None:
            if len(parms)==0: parms=None        
            elif not isinstance(parms, list): parms = [parms]
        self.customOperations += QtIfwPackageScript.__ADD_OPERATION_TMPLT % (
            (QtIfwPackageScript.__ELEVATED if isElevated else ""), name, 
            "" if parms is None else ", ",
            "" if parms is None else
            "[%s]" % (", ".join( ['"%s"' % (p,) for p in parms] 
                                 if isAutoQuote else parms ) ) 
        ) 

    def _flatten( self ) :
        
        def flattenExOps():
            # merge grouped together lists of ops into one flat list
            listFound=False  
            ops=[]
            for op in self.externalOps:
                if isinstance(op, list): 
                    ops.extend( op )
                    listFound=True
                else: ops.append( op )
            self.externalOps = [op for op in ops if op]
            if listFound: flattenExOps()
        
        def collectDependencies():
            # add unique dependencies in ops to the higher level list in the pkg  
            for op in self.externalOps:
                for res in op.externalRes:
                    if res: self.installResources.append( res )
            if self.installResources:
                self.installResources = list(set( self.installResources ))
                
        flattenExOps()
        collectDependencies()
                                                        
    def _generate( self ) :        
        self.script = _SCRIPT_LINE1_COMMENT
        
        if self.isAutoLib: _QtIfwScript._genLib( self )        
        if self.qtScriptLib: self.script += self.qtScriptLib        
        if self.isAutoGlobals: self.__genGlobals()
        if self.packageGlobals: self.script += self.packageGlobals

        self._flatten()
         
        # embedded external op scripts (in base64) into the QtScript 
        installScripts = []
        for op in self.externalOps: 
            if isinstance( op.script, ExecutableScript ):
                installScripts.append( op.script )             
            for resScript in op.resourceScripts:
                if isinstance( resScript, ExecutableScript ):
                    installScripts.append( resScript )
        self.script += _QtIfwScript.embedResources( installScripts ) 

        if self.isAutoComponentConstructor:
            self.__genComponentConstructorBody()
        self.script += ( 'function Component() {\n%s\n'
                         '    console.log("Component %s constructed");\n}\n' % 
                         (self.componentConstructorBody,
                          self.pkgName) )

        if self.isAutoComponentLoadedCallback:
            self.__genComponentLoadedCallbackBody()
        self.script += ( QtIfwPackageScript.__COMPONENT_CALLBACK_FUNC_TMPLT % 
                         (QtIfwPackageScript.__COMPONENT_LOADED_HNDLR_NAME,
                          self.componentLoadedCallbackBody,) )                            

        if self.uiPages: self.__appendUiPageCallbacks()
        if self.widgets: self.__appendWidgetCallbacks()
        
        if self.isAutoComponentCreateOperations:
            self.__genComponentCreateOperationsBody()
        if self.componentCreateOperationsBody:
            self.script += (
                '\nComponent.prototype.createOperations = function() {\n' +
                ('%s\n' % (self.componentCreateOperationsBody,) ) +                            
                '}\n')

        if self.isAutoComponentCreateOperationsForArchive:
            self.__genComponentCreateOperationsForArchiveBody()
        if self.componentCreateOperationsForArchiveBody:
            self.script += (
            '\nComponent.prototype.createOperationsForArchive = function(archive) {\n' +
            ('%s\n' % (self.componentCreateOperationsForArchiveBody,) ) +                        
            '}\n' )

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
                NEW +
                'var __vbsOpCounter=0' + END +
                'function addVbsOperation( component, isElevated, vbs ) ' + SBLK +
                    TAB + '__vbsOpCounter++' + END +
                    TAB + 'var vbsPath = __installerTempPath()' + 
                            '+ "/__temp_" + __vbsOpCounter + ".vbs"' + END +
                    TAB + 'var cmd = ["cscript", "/Nologo", vbsPath]' + END +
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
                    TAB + _QtIfwScript.ifPathExists( 'progPath', isAutoQuote=False ) + NEW +
                    (2*TAB) + 'return progPath' + END +                    
                    TAB + 'if( !isPackageInstalled( pkg ) )' + SBLK +
                    (2*TAB) + 'if( !installPackage( pkg ) )' + NEW +                    
                        (3*TAB) + 'throw new Error("Could not install package: " + pkg )' + END +
                    EBLK +                                                                    
                    TAB + _QtIfwScript.ifPathExists( 'progPath', isAutoQuote=False ) + NEW +
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
            isReplacement = p.name.startswith( QT_IFW_REPLACE_PAGE_PREFIX )
            
            if isReplacement:
                replacePage = p.name[ len(QT_IFW_REPLACE_PAGE_PREFIX): ]
                if replacePage in _DEFAULT_PAGES : 
                    self.componentLoadedCallbackBody += ( NEW + 
                        TAB + (ADD_CUSTOM_PAGE_TMPLT % ( p.name, replacePage )) + END +
                            TAB + (HIDE_DEFAULT_PAGE_TMPLT % (replacePage,)) + END 
                    )         
            else :
                if p.isIncInAutoPilot:
                    self.componentLoadedCallbackBody +=(
                        _QtIfwScript.ifCmdLineSwitch( 
                            _QtIfwScript.AUTO_PILOT_CMD_ARG, isMultiLine=True))
                self.componentLoadedCallbackBody += ( NEW + TAB + 
                    (ADD_CUSTOM_PAGE_TMPLT % ( p.name, p.pageOrder )) + END )         

            self.componentLoadedCallbackBody += p._onLoadSnippet()

            if not isReplacement and p.isIncInAutoPilot: 
                self.componentLoadedCallbackBody += _QtIfwScript.END_BLOCK
        
        for w in self.widgets:                        
            self.componentLoadedCallbackBody += (
                _QtIfwScript.TAB + QtIfwControlScript.insertCustomWidget(
                    w.name, w.pageName, w.position ) +
                w._onLoadSnippet() )             
                
    def __appendUiPageCallbacks( self ):    
        if self.uiPages: 
            for p in self.uiPages:
                for funcName, funcBody in iteritems( p.eventHandlers ):
                    self.script += (  
                        QtIfwPackageScript.__COMPONENT_CALLBACK_FUNC_TMPLT 
                        % (funcName, funcBody) )
                if isinstance( p, QtIfwDynamicOperationsPage ):    
                    self.script += p._onCompletedFunc
                    for func in p._asyncFuncs:
                        if isinstance( func, QtIfwDynamicOperationsPage.AsyncFunc ): 
                            self.script += func._define()

    def __appendWidgetCallbacks( self ):    
        if self.widgets: 
            for w in self.widgets:
                for funcName, funcBody in iteritems( w.eventHandlers ):
                    self.script += (  
                        QtIfwPackageScript.__COMPONENT_CALLBACK_FUNC_TMPLT 
                        % (funcName, funcBody) )
        
    def __genComponentCreateOperationsBody( self ):
        END = _QtIfwScript.END_LINE
        TAB = _QtIfwScript.TAB
        NEW = _QtIfwScript.NEW_LINE        
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK
        
        self.componentCreateOperationsBody = "try " + SBLK
        
        if self.preOpSupport:
            self.componentCreateOperationsBody += (
                "\n%s\n" % (self.preOpSupport,) )            

        if self.customOperations:
            self.componentCreateOperationsBody += (
                "\n%s\n" % (self.customOperations,) )            
                
        # pre payload extractions
        for res in self.installResources:
            if isinstance( res, QtIfwExternalResource ):
                self.componentCreateOperationsBody +=(
                     res._setTargetPathValues() )                         
        if IS_LINUX and self.isAskPassProgRequired:
            self.__addAskPassProgResolution()
        
        # Call to super class - perform payload extractions 
        self.componentCreateOperationsBody += (
            TAB + 'component.createOperations(); // call to super class\n' )
        
        # post payload extractions
        self.__addScriptUpdates()
        self.__addShortcuts()
        self.__addKillOperations()
        self.__addExternalOperations()
                 
        self.componentCreateOperationsBody += (
            NEW + EBLK + 
            'catch(e)' + SBLK + 
                _QtIfwScript.setBoolValue( _QtIfwScript.INTERUPTED_KEY, True) +
                'throw e' + END +  
            EBLK + NEW )

    def __genComponentCreateOperationsForArchiveBody( self ):
        TAB = _QtIfwScript.TAB
        END = _QtIfwScript.END_LINE
        SBLK =_QtIfwScript.START_BLOCK
        EBLK =_QtIfwScript.END_BLOCK
        self.componentCreateOperationsForArchiveBody = ""
        
        # override tool archive extractions
        for tool in self.installResources:
            if isinstance( tool, QtIfwExternalResource ): 
                archiveName = joinExt( 
                    versionStr( self.pkgVersion ) + tool.name, 
                    _QT_IFW_ARCHIVE_EXT )
                self.componentCreateOperationsForArchiveBody +=(
                #TAB + _QtIfwScript.log( '"archive: " + archive', isAutoQuote=False ) +                     
                TAB + ('if(fileName(archive)=="%s")' % (archiveName,)) + SBLK +
                (2*TAB) + _QtIfwScript.log( 
                    "Handling installer tool archive: %s" % (archiveName,)  ) +
                (2*TAB) + ('component.addOperation("Extract", archive, %s)' % ( 
                            tool.targetDirPath() ) ) + END +
                (2*TAB) + 'return' + END +
                TAB + EBLK 
                )
                                
        # if not overridden, perform default pay load extraction         
        self.componentCreateOperationsForArchiveBody +=(        
            '    component.createOperationsForArchive(archive); // call to super class \n' )

    def __addScriptUpdates( self ):
        if self.bundledScripts and len(self.bundledScripts) > 0:
            self.componentCreateOperationsBody +=(
                _QtIfwScript.resolveScriptVarsOperations( 
                    self.bundledScripts, self.pkgSubDirName ) 
            )
        
    # TODO: Clean up this ever growing, hideous mess!    
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
                if shortcut.exeName and shortcut.isAdjancentShortcut:
                    winOps += QtIfwPackageScript.__winAddShortcut(
                            ADJANCENT_WIN_SHORTCUT, shortcut.exeName,
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
                if shortcut.exeName and shortcut.isAdjancentShortcut:
                    macOps += QtIfwPackageScript.__macAddShortcut(
                            ADJANCENT_MAC_SHORTCUT, 
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
                if shortcut.exeName and shortcut.isAdjancentShortcut:
                    x11Ops += QtIfwPackageScript.__linuxAddDesktopEntry(
                            ADJANCENT_X11_SHORTCUT, 
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
    def __addExternalOperations( self ):
        if not self.externalOps: return        
        
        TAB  = _QtIfwScript.TAB
        END  = _QtIfwScript.END_LINE
        NEW  = _QtIfwScript.NEW_LINE
        SBLK = _QtIfwScript.START_BLOCK  # @UnusedVariable
        EBLK = _QtIfwScript.END_BLOCK
        
        # generate the install scripts, applying dynamic changes (e.g. path selection) 
        # made via the user input in the installer
        installScripts = []
        for op in self.externalOps: 
            if isinstance( op.script, ExecutableScript ):
                installScripts.append( op.script )             
            for resScript in op.resourceScripts:
                if isinstance( resScript, ExecutableScript ):
                    installScripts.append( resScript )        
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
    var psInputFormat  = "-InputFormat";
    var psInputNone    = "None";     
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
            uninstScriptType=( task.uninstScript.extension if task.uninstScript else None )            
            if uninstExePath:
                if not IS_WINDOWS: uninstExePath = uninstExePath.replace(" ", "\\\\ ")
                setArgs += '%sundoPath = "%s"%s' % (TAB,uninstExePath,END)
            if task.uninstRetCodes:
                setArgs +=( '%sundoRetCodes = "{%s}"%s' % 
                    (TAB,",".join([str(c) for c in task.uninstRetCodes]),END) )
            if len(setArgs) > 0: self.componentCreateOperationsBody += setArgs
             
            # skip creating execute operations when none are really defined 
            # (e.g. with pure resource script "container" op objects)  
            if not exePath and not uninstExePath: continue
             
            args=[]                        
            if exePath :                 
                if task.successRetCodes: args+=["retCodes"]       
                if scriptType=="vbs":                     
                    if not IS_WINDOWS: 
                        raise DistBuilderError( 
                            "VBScript is not supported by this platform!" )                                            
                    args+=["vbsInterpreter", "vbsNologo"]
                elif scriptType=="ps1":
                    if not IS_WINDOWS: 
                        raise DistBuilderError( 
                            "PowerShell scripts are not INHERTENTLY "
                            "supported by this platform!" )                                             
                    args+=["psInterpreter", "psNologo", 
                           "psExecPolicy", "psBypassPolicy",                            
                           "psInputFormat", "psInputNone",                                
                           "psExecScript"]
                elif scriptType=="scpt":            
                    if not IS_MACOS:
                        raise DistBuilderError( 
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
                if uninstScriptType=="vbs": 
                    args+=["vbsInterpreter", "vbsNologo"]
                elif uninstScriptType=="ps1":
                    args+=["psInterpreter", "psNologo", 
                           "psExecPolicy", "psBypassPolicy",
                           "psInputFormat", "psInputNone", 
                           "psExecScript"]
                elif uninstScriptType=="scpt":            
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
                'getAskPassProg()', isAutoQuote=False ) +
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
                  command=None, args=None, 
                  exeDir=QT_IFW_TARGET_DIR, exeName=None, 
                  exeVersion="0.0.0.0",
                  isGui=True, pngIconResPath=None ) :
        self.productName    = productName
        self.command        = command   
        self.args           = args if args else []
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
        self.isAppShortcut       = True
        self.isDesktopShortcut   = False
        self.isAdjancentShortcut = False

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
        __EXE_SCRIPT_HDR = (
"""
@echo off
set "appname={0}"
set "dirname={1}"
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
    
    __WRAP_EXE_MIXED_SUFFIX = "%sLauncher"
    __WRAP_EXE_LCASE_SUFFIX = "%s_launcher"
    
    # QtIfwExeWrapper
    def __init__( self, exeName, isGui=False, 
                  wrapperScript=None,
                  exeDir=QT_IFW_TARGET_DIR, 
                  workingDir=None, # None=don't impose here, use QT_IFW_TARGET_DIR via other means
                  args=None, envVars=None, isElevated=False,
                  isExe=False ) : # Windows Only
               
        self.exeName       = exeName
        self.isGui         = isGui
        
        self.wrapperScript = wrapperScript

        self.exeDir        = exeDir
        self.workingDir    = workingDir

        self.args          = args      
        self.envVars       = envVars 
        
        self.isElevated    = isElevated
        
        self.isExe = isExe if IS_WINDOWS else False
        self.wrapperExeName =( normBinaryName( 
                (QtIfwExeWrapper.__WRAP_EXE_LCASE_SUFFIX 
                 if exeName.lower()==exeName else 
                 QtIfwExeWrapper.__WRAP_EXE_MIXED_SUFFIX) % (exeName,) ) 
            if IS_WINDOWS else None )
        self.wrapperIconName = None
        
        if IS_WINDOWS:
            self._winPsStartArgs  = None
                    
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
                isScript = isAutoScript =(
                    self.isExe or (self.isElevated and self.envVars) )
            elif IS_LINUX :
                # GUIs desktop entries can do all this, but without a gui a script
                # is required 
                isScript = isAutoScript = (not self.isGui and
                    (self.isElevated or self.workingDir or
                     self.args or self.envVars) )
            elif IS_MACOS : 
                # there are no "light weight" shortcut wrappers employed on macOS, 
                # so always use a script to apply wrapper features (but we hide it
                # inside the natural .app wrapper for gui programs)
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
                self.wrapperExeName if self.isExe else self.wrapperScript.fileName() )            
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
                script =( QtIfwExeWrapper.__EXE_SCRIPT_HDR.format( 
                            self.exeName, self.exeDir )  
                          if self.isExe else QtIfwExeWrapper.__SCRIPT_HDR )                
                if isinstance( self.envVars, dict ):
                    for k,v in iteritems( self.envVars ):
                        script += ( '\n' + 
                            (QtIfwExeWrapper.__SET_ENV_VAR_TMPLT % (k, v)) )
                    script += '\n'     
                launch =( QtIfwExeWrapper.__GUI_EXECUTE_PROG_TMPLT
                          if self.isGui 
                          else QtIfwExeWrapper.__EXECUTE_PROG_TMPLT )
                cdCmd = ""
                # for a hard exe wrapper, force the working directory, 
                # (as it will always be a funky temp path otherwise) 
                if self.workingDir or self.isExe:
                    if self.workingDir==QT_IFW_TARGET_DIR :
                        pwdPath = QtIfwExeWrapper.__TARGET_DIR                    
                    elif self.isExe and not self.workingDir: pwdPath = self.exeDir                               
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
                        for k,v in iteritems( self.envVars ):
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
        elif IS_LINUX :
            if isAutoScript:
                script=QtIfwExeWrapper.__SCRIPT_HDR                 
                if isinstance( self.envVars, dict ):
                    for k,v in iteritems( self.envVars ):
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
                    for k,v in iteritems( self.envVars ):
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
                    for k,v in iteritems( self.envVars ):
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
class QtIfwExternalOp:

    ON_INSTALL, ON_UNINSTALL, ON_BOTH, AUTO_UNDO = range(4) 

    __AUTO_SCRIPT_COUNT=0
    __SCRIPT_ROOT_NAME_TMPLT = "%s_%d"

    __NOT_FOUND_EXIT_CODE = 100

    __WIN_PATH_SEP = "\\"
    __NIX_PATH_SEP = "/"
    __NATIVE_PATH_SEP  = __WIN_PATH_SEP if IS_WINDOWS else __NIX_PATH_SEP
    __FOREIGN_PATH_SEP = __NIX_PATH_SEP if IS_WINDOWS else __WIN_PATH_SEP
    
    @staticmethod
    def opDataPath( rootFileName, isNative=True, 
                    quotes=None, isDoubleBackslash=False ): 
        path = joinExt( joinPath( QT_IFW_SCRIPTS_DIR, rootFileName ), 
                        _QT_IFW_TEMP_DATA_EXT )
        if isNative:
            path = path.replace( QtIfwExternalOp.__FOREIGN_PATH_SEP, 
                                 QtIfwExternalOp.__NATIVE_PATH_SEP )
            if IS_WINDOWS and isDoubleBackslash:
                path = path.replace( QtIfwExternalOp.__WIN_PATH_SEP,
                                     QtIfwExternalOp.__WIN_PATH_SEP+
                                     QtIfwExternalOp.__WIN_PATH_SEP )
        if quotes: path = "%s%s%s" % (quotes, path, quotes) 
        return path
        
    @staticmethod
    def CreateOpFlagFile( event, fileName, dynamicVar=None,
                          isElevated=True ):    
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.CreateOpFlagFileScript( 
                fileName, dynamicVar ), 
            isElevated=isElevated )
        
    @staticmethod
    def WriteOpDataFile( event, fileName, data, isElevated=True ):    
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.WriteOpDataFileScript( fileName, data ), 
            isElevated=isElevated )
        
    @staticmethod
    def RemoveFile( event, filePath, isElevated=True ): # TODO: Test in NIX/MAC            
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.RemoveFileScript( filePath ), 
            isElevated=isElevated )
    
    @staticmethod
    def RemoveDir( event, dirPath, isElevated=True ): # TODO: Test in NIX/MAC           
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.RemoveDirScript( dirPath ), 
            isElevated=isElevated )
     
    # TODO: Test in NIX/MAC 
    #
    # TODO: Fix a glitch on Windows with employing isHidden.  This is a problem
    # throughout the library - the PS -WindowStlye Hidden is not respected
    # by all applications - including our basic demos with PyInstaller / Tk!
    # (not sure which is to blame - but it's probably Tk?)
    #
    # TODO: Fix a glitch on Windows with setting isSynchronous to False. 
    # In the context of running one of our uninstallers as a sub process 
    # from one of our installers, an asynchronous program launch will still
    # produce a blocking condition because the installer launches using
    # a PowerShell StartProcess -Wait which sees the asynch program as a child
    # process it must wait for.   
    @staticmethod
    def RunProgram( event, path, arguments=None, isAutoQuote=True,  
                    isHidden=False, isSynchronous=True, isElevated=True,
                    runConditionFileName=None, isRunConditionNegated=False,  
                    isAutoBitContext=True ): # Windows Only           
        return QtIfwExternalOp.__genScriptOp( event, 
            script=QtIfwExternalOp.RunProgramScript( 
                path, arguments, isAutoQuote, 
                isHidden, isSynchronous,
                runConditionFileName, isRunConditionNegated, 
                isAutoBitContext ), 
            isElevated=isElevated )
    
    @staticmethod
    def CreateStartupEntry( pkg=None, 
                            exePath=None, displayName=None, 
                            isAllUsers=False ):
        if pkg:
            if not displayName: displayName = pkg.pkgXml.DisplayName                            
            if not exePath:
                if pkg.exeWrapper:                  
                    exeDir = pkg.exeWrapper.exeDir 
                    exeName = ( normBinaryName( pkg.exeWrapper.wrapperExeName ) 
                                if pkg.exeWrapper.isExe else
                                pkg.exeWrapper.wrapperScript.fileName() 
                                if pkg.exeWrapper.wrapperScript else 
                                normBinaryName( pkg.exeName, pkg.isGui ) )
                else :
                    exeDir = ( joinPath( QT_IFW_TARGET_DIR, pkg.subDirName ) 
                               if pkg.subDirName else QT_IFW_TARGET_DIR ) 
                    exeName = normBinaryName( pkg.exeName, pkg.isGui )                        
                exePath = joinPath( exeDir, exeName ) 
        if exePath is None or displayName is None:
            raise DistBuilderError( "Missing required arguments" )    
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

    if IS_WINDOWS:

        @staticmethod
        def CreateWindowsAppFoundFlagFile( event, appName, fileName, 
                                           isAutoBitContext=True ):
            return QtIfwExternalOp.__genScriptOp( event, 
                script=QtIfwExternalOp.CreateWindowsAppFoundFlagFileScript( 
                    appName, fileName, isAutoBitContext ), 
                isReversible=False, isElevated=True )
        
        @staticmethod
        def UninstallWindowsApp( event, appName, arguments=None,
                                 isSynchronous=True, isHidden=True, 
                                 isAutoBitContext=True, 
                                 isSuccessOnNotFound=True ):
            op = QtIfwExternalOp.__genScriptOp( event, 
                script=QtIfwExternalOp.UninstallWindowsAppScript( appName,
                    arguments, isSynchronous, isHidden, isAutoBitContext ),
                isReversible=False, isElevated=True )
            if isSuccessOnNotFound:
                op.successRetCodes=[ 0, QtIfwExternalOp.__NOT_FOUND_EXIT_CODE ]
                op.uninstRetCodes =[ 0, QtIfwExternalOp.__NOT_FOUND_EXIT_CODE ]
            return op
        
        # TODO: Expand upon registry functions (notably with cascading scripts)
        @staticmethod
        def CreateRegistryKey( event, key, isAutoBitContext=True ):
            return QtIfwExternalOp.__genScriptOp( event, 
                script=QtIfwExternalOp.CreateRegistryKeyScript( 
                    key, isAutoBitContext ), 
                uninstScript=QtIfwExternalOp.RemoveRegistryKeyScript( 
                    key, isAutoBitContext ), 
                isElevated=True )

        @staticmethod
        def RemoveRegistryKey( event, key, isAutoBitContext=True ):
            return QtIfwExternalOp.__genScriptOp( event, 
                script=QtIfwExternalOp.RemoveRegistryKeyScript( 
                    key, isAutoBitContext ), 
                isReversible=False, isElevated=True )

        @staticmethod
        def CreateRegistryEntry( event, key, valueName=None, 
                                 value="", valueType="String",
                                 isAutoBitContext=True ):
            return QtIfwExternalOp.__genScriptOp( event, 
                script=QtIfwExternalOp.CreateRegistryEntryScript( 
                    key, valueName, value, valueType, isAutoBitContext ), 
                uninstScript=QtIfwExternalOp.RemoveRegistryEntryScript( 
                    key, valueName, isAutoBitContext ), 
                isElevated=True )
        
        @staticmethod
        def RemoveRegistryEntry( event, key, valueName=None,
                                 isAutoBitContext=True ):
            return QtIfwExternalOp.__genScriptOp( event, 
                script=QtIfwExternalOp.RemoveRegistryEntryScript( 
                    key, valueName, isAutoBitContext ), 
                isReversible=False, isElevated=True )

        @staticmethod
        def CreateExeFromScript( script, exeVerInfo, srcIconPath,
                                 targetDir=QT_IFW_TARGET_DIR ):            
            iconRes = QtIfwExternalResource( "%sIcon" % (script.rootName,), 
                                             srcIconPath )            
            ops = [ QtIfwExternalOp( resourceScripts=[script], 
                                     externalRes=[iconRes] ) ]
            ops.extend( QtIfwExternalOp.Script2Exe( 
                scriptPath = joinPath( QT_IFW_SCRIPTS_DIR, script.fileName() )
                , exePath = joinPath( targetDir, 
                                      normBinaryName( script.rootName ) )
                , exeVerInfo = exeVerInfo
                , iconDirPath = iconRes.targetDirPathVar()
                , iconName = baseFileName( srcIconPath )
            ))
            return ops
        
        @staticmethod
        def Script2Exe( scriptPath, exePath, exeVerInfo,
                        iconDirPath, iconName, 
                        isScriptRemoved=False, isIconDirRemoved=False ):
            return [
                  QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.AUTO_UNDO, 
                    script=QtIfwExternalOp.Script2ExeScript( 
                        scriptPath, exePath, isScriptRemoved ),
                    uninstScript=QtIfwExternalOp.RemoveFileScript( exePath ),                     
                    isReversible=True, isElevated=True )
                , QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.ON_INSTALL, 
                    script=QtIfwExternalOp.EmbedExeVerInfoScript( 
                        exePath, exeVerInfo ), 
                    isReversible=False, isElevated=True,
                    externalRes=[ QtIfwExternalResource.BuiltIn(
                        QtIfwExternalResource.RESOURCE_HACKER ) ] )            
                , QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.ON_INSTALL, 
                    script=QtIfwExternalOp.ReplacePrimaryIconInExeScript( 
                        exePath, iconDirPath, iconName, 
                        isIconDirRemoved=isIconDirRemoved ), 
                    isReversible=False, isElevated=True,
                    externalRes=[ QtIfwExternalResource.BuiltIn(
                        QtIfwExternalResource.RESOURCE_HACKER ) ] )            
            ]

        #TODO: copy the branding directly rather than applying directly, in order to 
        # make this work with non PyInstaller binaries] 
        @staticmethod
        def WrapperScript2Exe( scriptPath, exePath, targetPath, 
                               iconName=None ):
            iconDirPath = joinPath( "%temp%", "extracted-icons" )            
            isScriptRemoved = isIconDirRemoved = True
            return [
                  QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.AUTO_UNDO, 
                    script=QtIfwExternalOp.Script2ExeScript( 
                        scriptPath, targetPath, isScriptRemoved ),
                    uninstScript=QtIfwExternalOp.RemoveFileScript( exePath ), 
                    isReversible=True, isElevated=True )
                , QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.ON_INSTALL, 
                    script=QtIfwExternalOp.CopyExeVerInfoScript( 
                        exePath, targetPath ),                         
                    isReversible=False, isElevated=True,
                    externalRes=[QtIfwExternalResource.BuiltIn(
                        QtIfwExternalResource.RESOURCE_HACKER ) ] )            
                , QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.ON_INSTALL, 
                    script=QtIfwExternalOp.ExtractIconsFromExeScript( 
                        exePath, iconDirPath ), 
                    isReversible=False, isElevated=True,
                    externalRes=[QtIfwExternalResource.BuiltIn(
                        QtIfwExternalResource.RESOURCE_HACKER ) ] )                  
                , QtIfwExternalOp.__genScriptOp( QtIfwExternalOp.ON_INSTALL, 
                    script=QtIfwExternalOp.ReplacePrimaryIconInExeScript( 
                        targetPath, iconDirPath, iconName, 
                        isIconDirRemoved=isIconDirRemoved ), 
                    isReversible=False, isElevated=True,
                    externalRes=[QtIfwExternalResource.BuiltIn(
                        QtIfwExternalResource.RESOURCE_HACKER ) ] )                            
            ]

    # Script Builders
    # -----------------
    @staticmethod
    def batchSelfDestructSnippet(): 
        return '(goto) 2>nul & del "%~f0"'

    @staticmethod
    def powerShellSelfDestructSnippet(): 
        return 'Remove-Item $script:MyInvocation.MyCommand.Path -Force'

    @staticmethod
    def vbScriptSelfDestructSnippet(): 
        return ExecutableScript.linesToStr([
             'Set oFSO = CreateObject("Scripting.FileSystemObject")'                        
            ,'oFSO.DeleteFile WScript.ScriptFullName'         
            ,'Set oFSO = Nothing'
        ])

    @staticmethod
    def shellScriptSelfDestructSnippet(): 
        return "" #TODO: Fill in NIX/MAC

    @staticmethod
    def appleScriptSelfDestructSnippet(): 
        return "" #TODO: Fill in NIX/MAC

    @staticmethod
    def __scriptRootName( prefix ):
        QtIfwExternalOp.__AUTO_SCRIPT_COUNT+=1
        return QtIfwExternalOp.__SCRIPT_ROOT_NAME_TMPLT % ( 
            prefix, QtIfwExternalOp.__AUTO_SCRIPT_COUNT )
    
    @staticmethod
    def __genScriptOp( event, script, uninstScript=None, 
                       isReversible=True, isElevated=False,
                       externalRes=None ):    
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
            # While seemingly redundant, this flag/check is in place
            # for building operations for clients that may pass AUTO_UNDO
            # events where such is not supported 
            if not isReversible: 
                raise DistBuilderError( 
                    "Installer operation cannot be automatically undone." )
            onInstall   = script 
            onUninstall = uninstScript                              
        return QtIfwExternalOp( script=onInstall, uninstScript=onUninstall,
                isElevated=isElevated, 
                externalRes=externalRes if externalRes else [] ) 


    @staticmethod
    def CreateOpFlagFileScript( fileName, dynamicVar=None ): # TODO: Test in NIX/MAC            
        return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "createOpFlagFile" ), script=(
                ("" if dynamicVar is None else
                 QtIfwExternalOp.__batExitIfFalseVar( dynamicVar )
                 if IS_WINDOWS else
                 QtIfwExternalOp.__shExitIfFalseVar( dynamicVar ) ) + 
                str( QtIfwExternalOp.WriteOpDataFileScript( 
                     fileName, data=None ) )         
        ))
        
    # TODO: Auto handle escape sequences?
    @staticmethod
    def WriteOpDataFileScript( fileName, data=None ): # TODO: Test in NIX/MAC            
        filePath = QtIfwExternalOp.opDataPath( fileName )
        if data is None:                    
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "touchOpDataFile" ), script=(
                'echo. > "%s"' % (filePath,) if IS_WINDOWS else
                'touch "%s"'  % (filePath,) ) )
        else:
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "writeOpDataFile" ), script=(
                'echo %s > "%s"' % (data, filePath,) if IS_WINDOWS else
                'echo "%s" > "%s"' % (data, filePath,) ) )
                    
    @staticmethod
    def RemoveFileScript( filePath ): # TODO: Test in NIX/MAC            
        return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
            "removeFile" ), script=(
            'del /q /f "{filePath}"' if IS_WINDOWS else 'rm "{filePath}"' ), 
            replacements={ "filePath": filePath } )
    
    @staticmethod
    def RemoveDirScript( dirPath ): # TODO: Test in NIX/MAC           
        return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
            "removeDir" ), script=(
            'rd /q /s "{dirPath}"' if IS_WINDOWS else 'rm -r "{dirPath}"'  ), 
            replacements={ "dirPath": dirPath } )

    # TODO: Test in NIX/MAC       
    @staticmethod
    def RunProgramScript( path, arguments=None, isAutoQuote=True, 
                          isHidden=False, isSynchronous=True,
                          runConditionFileName=None, isRunConditionNegated=False,
                          isAutoBitContext=True,
                          replacements=None  ):
        if arguments is None: arguments =[] 
        if isHidden: 
            if IS_WINDOWS :
                waitSwitch = " -Wait" if isSynchronous else ""
                hiddenStyle = " -WindowStyle Hidden"         
                argList = [('"%s"' % (a,) if (" " in a or "@" in a) else a) 
                           for a in arguments]            
                argList =( (" -ArgumentList " +
                    ",".join( ["'%s'" % (a,) for a in argList]) )         
                    if len(arguments) > 0 else "" )                
                return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                    "runHiddenProgram" ), extension="ps1", script=([
                    QtIfwExternalOp.__psExitIfFileMissing(
                        runConditionFileName, isRunConditionNegated ),    
                    QtIfwExternalOp.__psSetBitContext( isAutoBitContext ),   
                    'Start-Process -FilePath "%s" %s%s%s'
                         % (path, waitSwitch, hiddenStyle, argList), 
                    'exit $LastExitCode']), replacements=replacements )
            else: 
                # TODO: Fill-in on NIX/MAC
                util._onPlatformErr()
        else :
            tokens = [path] + arguments            
            if isAutoQuote:
                tokens = [('"%s"' % (t,) if (" " in t or "@" in t) else t) 
                          for t in tokens]            
            runCmd = " ".join( tokens )
            exitSnippet =(
                QtIfwExternalOp.__batExitIfFileMissing(
                    runConditionFileName, isRunConditionNegated )
                if IS_WINDOWS else
                QtIfwExternalOp.__shExitIfFileMissing(
                    runConditionFileName, isRunConditionNegated )                
            )                                     
            if not isSynchronous: 
                if IS_WINDOWS: runCmd = 'start "" ' + runCmd 
                else: runCmd += " &"                    
            if IS_WINDOWS and not isAutoBitContext:
                script=([
                    exitSnippet,
                    'set "RUN_CMD=%s"' % (runCmd,),
                    'if %PROCESSOR_ARCHITECTURE%==x86 ( "%windir%\sysnative\cmd" /c "%RUN_CMD%" ) else ( %RUN_CMD% )',
                    runCmd])  
            else: script=[exitSnippet, runCmd ]
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "runProgram" ), script=script, replacements=replacements )
                     
    if IS_WINDOWS:

        @staticmethod
        def __batExitIfFalseVar( varName, isNegated=False, errorCode=0 ):
            if varName is None: return ""
            return str( ExecutableScript( "", script=([               
                  'set "reqFlag={varName}"'               
                , 'if "%reqFlag%"=="{undef}" set "reqFlag=false"'
                , 'if "%reqFlag%"=="" set "reqFlag=false"'
                , 'if "%reqFlag%"=="0" set "reqFlag=false"'
                , 'if {negate}"%reqFlag%"=="false" exit /b {errorCode}'
            ]), replacements={
                  'negate' : ('' if isNegated else 'not ')  
                , 'varName' : qtIfwDynamicValue( varName )
                , 'errorCode': errorCode
                , 'undef' : QT_IFW_UNDEF_VAR_VALUE
            }) )

        @staticmethod
        def __batExitIfFileMissing( fileName, isNegated=False, errorCode=0 ):
            if fileName is None: return ""            
            return str( ExecutableScript( "", script=([                               
                'if {negate}exist "{filePath}" exit /b {errorCode}'   
            ]), replacements={
                  'negate' : ('' if isNegated else 'not ')  
                , 'filePath' : QtIfwExternalOp.opDataPath( fileName )
                , 'errorCode': errorCode
            }) )

        # TODO: TEST
        @staticmethod
        def __psExitIfFalseVar( varName, isNegated=False, errorCode=0 ):
            if varName is None: return ""
            return str( ExecutableScript( "", script=([    
                  '$reqFlag="{varName}"'
                , 'if( $reqFlag -eq "{undef}" ) { $reqFlag="false" }'
                , 'if( $reqFlag -eq "" ) { $reqFlag="false" }'
                , 'if( $reqFlag -eq "0" ) { $reqFlag="false" }'
                , 'if( {negate}($reqFlag -eq "false") ) {'
                , '    [Environment]::Exit( {errorCode} )'
                , '}'   
            ]), replacements={
                  'negate' : ('' if isNegated else '! ')  
                , 'varName' : qtIfwDynamicValue( varName )
                , 'errorCode': errorCode
                , 'undef' : QT_IFW_UNDEF_VAR_VALUE
            }) )

        @staticmethod
        def __psExitIfFileMissing( fileName, isNegated=False, errorCode=0 ):
            if fileName is None: return ""            
            return str( ExecutableScript( "", script=([               
                  'if( {negate}(Test-Path "{filePath}" -PathType Leaf) ) {'
                , '    [Environment]::Exit( {errorCode} )'
                , '}'   
            ]), replacements={
                  'negate' : ('' if isNegated else '! ')  
                , 'filePath' : QtIfwExternalOp.opDataPath( fileName )
                , 'errorCode': errorCode
            }) )
        
        __PS_32_TO_64_BIT_CONTEXT_HEADER=(
"""                
if( $env:PROCESSOR_ARCHITEW6432 -eq "AMD64" ) {
    $powershell=$PSHOME.tolower().replace("syswow64","sysnative").replace("system32","sysnative")
    if ($myInvocation.Line) {
        &"$powershell\powershell.exe" -NonInteractive -NoProfile $myInvocation.Line
    } else {
        &"$powershell\powershell.exe" -NonInteractive -NoProfile -file "$($myInvocation.InvocationName)" $args
    }
    exit $lastexitcode
}
""")
        @staticmethod
        def __psSetBitContext( isAutoBitContext ): 
            return( "" if isAutoBitContext else 
                    QtIfwExternalOp.__PS_32_TO_64_BIT_CONTEXT_HEADER )
                    
        @staticmethod
        def __psFindWindowsAppUninstallCmd( appName, isAutoBitContext,
                                            isExitOnNotFound=False,
                                            isSelfDestruct=False ):            
            psScriptTemplate=(
r"""
{setBitContext}

$APP_NAME = "{appName}"

# Search for the uninstall command within the registry Local Machine key (32 & 64 bit locations)
$RegPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" 
$app = Get-ChildItem -Path $RegPath | Get-ItemProperty | Where-Object {$_.DisplayName -match $APP_NAME }
if( $app.QuietUninstallString ){ $UninstallCmd = $app.QuietUninstallString }
elseif( $app.UninstallString ){ $UninstallCmd = $app.UninstallString }

if( !$UninstallCmd ){
    # Search within the Current User key (Wow6432Node never used here for this?)
    $RegPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    $app = Get-ChildItem -Path $RegPath | Get-ItemProperty | Where-Object {$_.DisplayName -match $APP_NAME }
    if( $app.QuietUninstallString ){ $UninstallCmd = $app.QuietUninstallString }
    elseif( $app.UninstallString ){ $UninstallCmd = $app.UninstallString }
}

if( !$UninstallCmd ){
    # Search in a final odd ball location, used by some old legacy programs
    $RegPath = "HKLM:\SOFTWARE\Classes\Installer\Products"
    $app = Get-ChildItem -Path $RegPath | Get-ItemProperty | Where-Object {$_.ProductName -match $APP_NAME }
    if( $app.UninstallString ){ $UninstallCmd = $app.UninstallString }    
}

# Log command found / optionally exit with error 
if( !$UninstallCmd ){ 
    Write-Error "Uninstall command not found for {appName}"
    {selfDestructOnNotFound}
    {exitOnNotFound}
}
else{
    Write-Host "OS registered uninstall command for {appName}: $UninstallCmd"
}
""") 
            exitOnNotFound =( "[Environment]::Exit( %d )" % 
                              (QtIfwExternalOp.__NOT_FOUND_EXIT_CODE,)
                              if isExitOnNotFound else "" ) 
            return str( ExecutableScript( "", script=psScriptTemplate,
                replacements={
                      "setBitContext": QtIfwExternalOp.__psSetBitContext( 
                                            isAutoBitContext )
                    , "appName" : appName
                    , "exitOnNotFound": exitOnNotFound     
                    , "selfDestructOnNotFound" : (
                        QtIfwExternalOp.powerShellSelfDestructSnippet()
                        if isSelfDestruct and exitOnNotFound else "" )                                                             
                } ) )

        @staticmethod
        def CreateWindowsAppFoundFlagFileScript( appName, fileName, 
                                                 isAutoBitContext=True,
                                                 isSelfDestruct=False ):            
            psScriptTemplate=(
                QtIfwExternalOp.__psFindWindowsAppUninstallCmd( 
                    appName, isAutoBitContext ) +                 
r"""
if( $UninstallCmd ){ Out-File -FilePath "{tempFilePath}" } 
              else { Remove-Item "{tempFilePath}" }
{selfDestruct}
[Environment]::Exit( 0 )
""")                                    
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "createAppFoundFile" ), extension="ps1", 
                script=psScriptTemplate, replacements={ 
                      "tempFilePath": QtIfwExternalOp.opDataPath( fileName )
                    , "selfDestruct" : (
                        QtIfwExternalOp.powerShellSelfDestructSnippet()
                        if isSelfDestruct else "" )       
                })

        @staticmethod
        def UninstallWindowsAppScript( appName, arguments=None,
                                       isSynchronous=True, isHidden=True, 
                                       isAutoBitContext=True,
                                       isSelfDestruct=False ):            
            psScriptTemplate=(
                QtIfwExternalOp.__psFindWindowsAppUninstallCmd( 
                    appName, isAutoBitContext, isExitOnNotFound=True,
                    isSelfDestruct=isSelfDestruct ) +                 
r"""
# Tweak QtIFW / Distbuilder commands
if( $UninstallCmd.tolower().Contains( "maintenancetool.exe" ) ){
    # Run in QtIFW verbose mode, in case distbuilder built - specify auto pilot / removeall
    $UninstallCmd="$UninstallCmd -v auto=true mode=removeall" 
}  

# Tweak MSI commands    
elseif( $UninstallCmd.tolower().Contains( "msiexec.exe" ) ){
    # Replace an install switch with an uninstall switch, if found
    # (not sure why some registered uninstall strings might have this issue, but apparently some do...?)
    # preserve the original case
    $UninstallCmd.Replace( "MsiExec.exe /I", "MsiExec.exe /X" )    
    $UninstallCmd.Replace( "msiexec.exe /I", "msiexec.exe /X" )    
    # Add silent switch if not present
    if( !$UninstallCmd.Contains( " /qn" ) ) { $UninstallCmd="$UninstallCmd /qn" } 
}  

# Split the command string into the program path and argument list
$tokens=$UninstallCmd.split(' ')
$lastProgTokenIdx=0
foreach( $token in $tokens ) {    
    if( $token.EndsWith('.exe') ){ break }    
    $lastProgTokenIdx++
}
$prog=$tokens[0..$lastProgTokenIdx]
$prog="$prog"
$lastIdx=$tokens.Count-1
if( $lastProgTokenIdx -lt $lastIdx ){ $args=$tokens[($lastProgTokenIdx+1)..$lastIdx] }
else{ $args=@{} }
{addArgs}

# Run the uninstaller with window hidden (if it respects that request!)
Write-Host "Running: $prog"
if( $args.Count -gt 0 ){ Write-Host "With arguments: $args" }
Start-Process $prog {wait}{hide}-ArgumentList $args
{selfDestruct}
[Environment]::Exit( 0 )
""")                                    
            if arguments:
                ADD_ARG_TMPL = '$args.Add("%s")\n'
                addArgs = [ ADD_ARG_TMPL % (a,) for a in arguments ]
            else: addArgs = ""
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "uninstallApp" ), extension="ps1", script=psScriptTemplate,
                replacements={                   
                      "addArgs": addArgs
                    , "wait": ("-Wait " if isSynchronous else "")
                    , "hide": ("-WindowStyle Hidden " if isHidden else "")
                    , "selfDestruct" : (
                        QtIfwExternalOp.powerShellSelfDestructSnippet()
                        if isSelfDestruct else "" )                      
                } )

        # Creates the key, if it does not exists.
        # Recursively creates the parent key, if that does not yet exist.
        @staticmethod
        def CreateRegistryKeyScript( key, isAutoBitContext=True,
                                     replacements=None ):
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "createRegKey" ), extension="ps1", script=([
                QtIfwExternalOp.__psSetBitContext( isAutoBitContext ),                
                "$key='%s'" % (key,),
                "Try{ Get-Item -Path $key -ErrorAction Stop | Out-Null }",
                "Catch{ New-Item -Force -Path $key }",
                ]), 
                replacements=replacements )

        # Removes the key, if it exists.
        @staticmethod
        def RemoveRegistryKeyScript( key, isAutoBitContext=True,
                                     replacements=None ):
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "removeRegKey" ), extension="ps1", script=([
                QtIfwExternalOp.__psSetBitContext( isAutoBitContext ),                
                "$key='%s'" % (key,),
                "Try{ ",
                "    Get-Item -Path $key -ErrorAction Stop | Out-Null }",
                "    Remove-Item -Path $key }",
                "Catch{}"
                ]),                 
                replacements=replacements )
        
        # Creates the entry, if it does not exists.
        # Overwrites any prior value, if it already exists.
        # Recursively creates the parent key, if that does not yet exist.
        # valueName=None = Default key value
        @staticmethod
        def CreateRegistryEntryScript( key, valueName=None, 
                                       value="", valueType="String",
                                       isAutoBitContext=True,
                                       replacements=None ):
            valueName = "-Name '%s'" % (valueName,) if valueName else ""
            if value is None: value=""
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "createRegEntry" ), extension="ps1", script=([
                QtIfwExternalOp.__psSetBitContext( isAutoBitContext ),                
                "$key='%s'" % (key,),
                "$value='%s'" % (value,),
                "$type='%s'" % (valueType,),
                "Try{",
                "    Get-ItemPropertyValue -Path $key %s -ErrorAction Stop | Out-Null"
                    % (valueName,), 
                "    Set-ItemProperty -Path $key %s -Value $value -Type $type"
                    % (valueName,), 
                "}",
                "Catch{",
                "    Try{ Get-Item -Path $key -ErrorAction Stop | Out-Null }",
                "    Catch{ New-Item -Force -Path $key }",
                "    New-ItemProperty -Path $key %s -Value $value -PropertyType $type"
                    % (valueName,), 
                "}"
                ]), 
                replacements=replacements )

        # Removes the entry, if it exists.
        # valueName=None = Default key value
        @staticmethod
        def RemoveRegistryEntryScript( key, valueName=None, 
                                       isAutoBitContext=True,
                                       replacements=None ):
            valueName = "-Name '%s'" % (valueName,) if valueName else ""            
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "removeRegEntry" ), extension="ps1", script=([
                QtIfwExternalOp.__psSetBitContext( isAutoBitContext ),                
                "$key='%s'" % (key,),
                "Try{",
                "    Get-ItemPropertyValue -Path $key %s -ErrorAction Stop | Out-Null"
                    % (valueName,), 
                "    Remove-ItemProperty -Path $key %s" % (valueName,), 
                "}",
                "Catch{}"
                ]),                 
                replacements=replacements )
 
        @staticmethod
        def Script2ExeScript( srcPath, destPath, isSrcRemoved=False ):   
            from distbuilder import iexpress
            return iexpress._IExpressScript(
                srcPath, destPath, isSrcRemoved=isSrcRemoved,
                name=QtIfwExternalOp.__scriptRootName( "script2exe" ) )

        @staticmethod
        def EmbedExeVerInfoScript( exePath, exeVerInfo ):
            script=(
"""
@echo off

set "EXE_PATH={exePath}"
for %%I in ("%EXE_PATH%") do set "ORIGINAL_NAME=%%~nxI"

set "TEMP_RC_PATH=%temp%\\versioninfo.rc"
set "TEMP_RES_PATH=%temp%\\versioninfo.res"

(
echo:VS_VERSION_INFO VERSIONINFO
echo:    FILEVERSION    {fileVerCommaDelim}
echo:    PRODUCTVERSION {productVerCommaDelim}
echo:{
echo:    BLOCK "StringFileInfo"
echo:    {
echo:        BLOCK "040904b0"
echo:        {
echo:            VALUE "CompanyName",        "{companyName}\\0"
echo:            VALUE "FileDescription",    "{fileDescr}\\0"
echo:            VALUE "FileVersion",        "{fileVer}\\0"
echo:            VALUE "LegalCopyright",     "{copyright}\\0"
echo:            VALUE "OriginalFilename",   "%ORIGINAL_NAME%\\0"
echo:            VALUE "ProductName",        "{productName}\\0"
echo:            VALUE "ProductVersion",     "{productVer}\\0"
echo:        }
echo:    }
echo:    BLOCK "VarFileInfo"
echo:    {
echo:        VALUE "Translation", 0x409, 1200
echo:    }
echo:}
) > "%TEMP_RC_PATH%" 

"@ResourceHacker@" -open "%TEMP_RC_PATH%" -save "%TEMP_RES_PATH%" -action compile 
"@ResourceHacker@" -open "%EXE_PATH%" -save "%EXE_PATH%" -action addoverwrite -resource "%TEMP_RES_PATH%" 

del /q /f "%TEMP_RC_PATH%"
del /q /f "%TEMP_RES_PATH%"

exit /b %errorlevel%
""")            
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "embedExeVerInfo" ), script=script, replacements={
                  "exePath": exePath            
                , "companyName": exeVerInfo.companyName
                , "copyright": exeVerInfo.copyright()
                , "productName": exeVerInfo.productName
                , "productVerCommaDelim": exeVerInfo.version( isCommaDelim=True )
                , "productVer": exeVerInfo.version()
                , "fileDescr": exeVerInfo.description
                , "fileVerCommaDelim": exeVerInfo.version( isCommaDelim=True )
                , "fileVer":exeVerInfo.version()
                })

        @staticmethod
        def CopyExeVerInfoScript( srcExePath, destExePath ):
            script=(
"""
@echo off

set "SRC_EXE_PATH={srcExePath}"
set "DEST_EXE_PATH={destExePath}"

set "TEMP_RES_PATH=%temp%\\versioninfo.res"

"@ResourceHacker@" -open "%SRC_EXE_PATH%" -save "%TEMP_RES_PATH%" -action extract -mask VERSIONINFO 
"@ResourceHacker@" -open "%DEST_EXE_PATH%" -save "%DEST_EXE_PATH%" -action addoverwrite -resource "%TEMP_RES_PATH%" 

del /q /f "%TEMP_RES_PATH%"
""")            
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "copyExeVerInfo" ), script=script, replacements={
                  "srcExePath": srcExePath, "destExePath": destExePath } )

        @staticmethod
        def ExtractIconsFromExeScript( exePath, targetDirPath ):
            script=(
"""
@echo off
"@ResourceHacker@" -open "{exePath}" -save "{targetDirPath}" -action extract -mask ICONGROUP
""")            
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "extractIconsFromExe" ), script=script, replacements={ 
                    "exePath": exePath, "targetDirPath": targetDirPath } )

        @staticmethod
        def ReplacePrimaryIconInExeScript( exePath, iconDirPath, 
                                           iconName=None, isIconDirRemoved=False ):            
            """
            Note the use of if %PROCESSOR_ARCHITECTURE%==x86 ( "%windir%\sysnative\cmd" ...
            That is **extremely important** here, as "ie4uinit" is a 64 bit program, 
            and the installer runs in 32 bit context. The use %windir%\sysnative\cmd 
            allows this 32 bit program to "see" and execute a 64 bit sub process.
            Without that, you get mind blowing errors thrown back at you saying the  
            the file does not even exist (including when you specify an absolute path 
            to the file you know for a fact is found there)!
            """            
            script=(
"""
@echo off
{setIconName}
"@ResourceHacker@" -open "{exePath}" -save "{exePath}" -action addoverwrite -res "{iconDir}\%iconName%" -mask ICONGROUP, MAINICON, 0
{removeIconDir}
set "REFRESH_ICONS=ie4uinit -ClearIconCache & ie4uinit -show"
if %PROCESSOR_ARCHITECTURE%==x86 ( "%windir%\sysnative\cmd" /c "%REFRESH_ICONS%" ) else ( %REFRESH_ICONS% )
""")
            if iconName is None:
                setIconName =( 'for /f "delims=" %%F in '
                    '(\'dir ' + iconDirPath + '\*.ico /b /o-n\') '
                    'do set iconName=%%F' )
            else:            
                setIconName = 'set "iconName=%s"' % ( iconName, )                  
            removeIconDir =( 'rd /q /s "%s"' % (iconDirPath,) 
                             if isIconDirRemoved else "" )  
            return ExecutableScript( QtIfwExternalOp.__scriptRootName( 
                "replacePrimaryIconInExe" ), script=script, replacements={
                "exePath":exePath, 
                "iconDir": iconDirPath, "setIconName": setIconName, 
                "removeIconDir": removeIconDir } )
 
    if IS_MACOS or IS_LINUX:
         
        # TODO: TEST
        @staticmethod
        def __shExitIfFalseVar( varName, isNegated=False, errorCode=0 ):
            if varName is None: return ""
            return str( ExecutableScript( "", script=([
                  'reqFlag="{varName}"'               
                , '[ "{reqFlag}"=="{undef}" ] && reqFlag="false"'
                , '[ "{reqFlag}"=="" ] && reqFlag="false"'
                , '[ "{reqFlag}"=="0" ] && reqFlag="false"'
                , '[ {negate}"{reqFlag}"=="false" ] && exit {errorCode}'   
            ]), replacements={
                  'negate' : ('' if isNegated else '! ')  
                , 'varName' : qtIfwDynamicValue( varName )
                , 'errorCode': errorCode
                , 'undef' : QT_IFW_UNDEF_VAR_VALUE
            }) )

        # TODO: TEST         
        @staticmethod
        def __shExitIfFileMissing( fileName, isNegated=False, errorCode=0 ):
            if not fileName: return ""            
            return str( ExecutableScript( "", script=([               
                '[ {negate}-f "{filePath}" ] && exit {errorCode}'   
            ]), replacements={
                  'negate' : ('' if isNegated else '! ')  
                , 'filePath' : QtIfwExternalOp.opDataPath( fileName )
                , 'errorCode': errorCode
            }) )

    # QtIfwExternalOp
    def __init__( self,                                                       # [0]
              script=None,       exePath=None,       args=None, successRetCodes=None,  
        uninstScript=None, uninstExePath=None, uninstArgs=None,  uninstRetCodes=None,
        isElevated=False, workingDir=QT_IFW_TARGET_DIR, onErrorMessage=None,
        resourceScripts=None, uninstResourceScripts=None, externalRes=None ):
        
        self.script          = script #ExecutableScript        
        self.exePath         = exePath
        self.args            = args if args else []
        self.successRetCodes = successRetCodes if successRetCodes else [0]

        self.uninstScript    = uninstScript #ExecutableScript
        self.uninstExePath   = uninstExePath
        self.uninstArgs      = uninstArgs if uninstArgs else []
        self.uninstRetCodes  = uninstRetCodes if uninstRetCodes else [0]
        
        self.isElevated      = isElevated 
        self.workingDir      = workingDir
                
        self.onErrorMessage  = onErrorMessage # TODO: TEST!

        self.resourceScripts       = resourceScripts if resourceScripts else []
        self.uninstResourceScripts = uninstResourceScripts if uninstResourceScripts else []
        self.externalRes           = externalRes if externalRes else []

# -----------------------------------------------------------------------------
class QtIfwExternalResource:
        
    __TOOLS_RES_DIR_NAME = "qtifw_res"
    
    __CONTENT_KEYS = {} # dict of dicts
    
    if IS_WINDOWS:
        RESOURCE_HACKER = "ResourceHacker"
        __CONTENT_KEYS[ RESOURCE_HACKER ] = {
            RESOURCE_HACKER: "ResourceHacker.exe" }

    @staticmethod
    def __toArchiveName( name ): return joinExt( name, _QT_IFW_ARCHIVE_EXT )

    @staticmethod
    def _builtInResPath( name ):    
        return util._toLibResPath( joinPath( 
            QtIfwExternalResource.__TOOLS_RES_DIR_NAME,
            ("linux" if IS_LINUX else "macos" if IS_MACOS else "windows" ),
            QtIfwExternalResource.__toArchiveName( name ) ) )

    @staticmethod
    def BuiltIn( name, isMaintenanceNeed=False ):            
        return QtIfwExternalResource( name, 
            QtIfwExternalResource._builtInResPath( name ), 
            isMaintenanceNeed=isMaintenanceNeed, 
            contentKeys=QtIfwExternalResource.__CONTENT_KEYS.get(name,{}) )

    def __init__( self, name, srcPath, srcBasePath=None, 
                  isMaintenanceNeed=False, contentKeys=None ):
        if "-" in name:
            raise DistBuilderError( "Resource names may not contain dashes!"
                " (Auto correcting this may produce hard to find bugs)" )
        self.name = name
        self.srcPath = absPath( srcPath, srcBasePath )        
        print("self.srcPath", self.srcPath)
        self.isMaintenanceNeed = isMaintenanceNeed        
        self.contentKeys = contentKeys if contentKeys else {}
        if( (contentKeys is None or len(contentKeys)==0) and 
            isFile( self.srcPath ) and 
            fileExt(self.srcPath) != _QT_IFW_ARCHIVE_EXT ):                
            self.contentKeys[ name ] = baseFileName( self.srcPath )         

    def __hash__( self ): return hash( self.name )
    
    def __eq__( self, other ):
        return self.__class__ == other.__class__ and self.name==other.name
           
    def targetPathVar( self, key=None ):
        return _QT_IFW_VAR_TMPLT % (self.__targetPathKey( key ),)

    def targetDirPathVar( self ):
        return _QT_IFW_VAR_TMPLT % self.__targetDirPathKey()

    def targetPath( self, key=None ):
        return _QtIfwScript.lookupValue( self.__targetPathKey( key ) )

    def targetDirPath( self ):
        return _QtIfwScript.lookupValue( self.__targetDirPathKey() )

    def _setTargetPathValues( self ):        
        snippet=""
        dirPath = self._targetDirPathRaw()
        snippet += _QtIfwScript.setValue( 
            '"%s"' % (self.__targetDirPathKey(),), dirPath, 
            isAutoQuote=False )
        for key, relPath in iteritems(self.contentKeys):        
            snippet += _QtIfwScript.setValue( 
                '"%s"' % (key,), '(%s + "/%s")' % ( dirPath, relPath ), 
                isAutoQuote=False )
        return snippet               

    def _targetDirPathRaw( self ):
        return( _QtIfwScript.targetDir() + ' + "/%s"' % (
                _RETAINED_RESOURCE_SUBDIR ) if self.isMaintenanceNeed else
                '__installerTempPath()' ) + ' + "/%s"' % (self.name,) 

    def __targetPathKey( self, key=None ):
        if( key is None and 
            self.contentKeys is not None and len(self.contentKeys)==1 ):
            key=list(self.contentKeys.keys())[0] 
        if self.contentKeys is None or key not in self.contentKeys:
            raise DistBuilderError("Invalid content key")
        return key
    
    def __targetDirPathKey( self ): return '%sDir' % (self.name,)

# -----------------------------------------------------------------------------
class QtIfwKillOp:
    def __init__( self, processName, onInstall=True, onUninstall=True ):        
        self.processName = ( normBinaryName( processName.exeName ) 
            if isinstance( processName, QtIfwPackage ) else processName )         
        self.onInstall   = onInstall
        self.onUninstall = onUninstall
        self.isElevated  = True  

# -----------------------------------------------------------------------------
@add_metaclass( ABCMeta )
class _QtIfwInterface:

    __FILE_EXTENSION  = "ui"
    __UI_RES_DIR_NAME = "qtifw_ui"
    
    @staticmethod
    def _toFileName( templateName ): 
        return joinExt( templateName, 
                        _QtIfwInterface.__FILE_EXTENSION ).lower()  
    
    @staticmethod
    def _toLibResPath( templateName ):    
        return util._toLibResPath( joinPath( 
                _QtIfwInterface.__UI_RES_DIR_NAME, 
                _QtIfwInterface._toFileName( templateName ) ) )
    
    # _QtIfwInterface
    def __init__( self, name, sourcePath=None, content=None,
                  onLoad=None, onEnter=None ) :
        self.name = name
        if sourcePath:
            with open( sourcePath, 'r' ) as f: self.content = f.read()
        else: self.content = content          
        
        self.onLoad = onLoad
        self.onEnter = onEnter
        self._isOnLoadBase = True
        self._isOnEnterBase = True

        self.eventHandlers    = {} 
        self.supportScript    = None

        self.replacements = {}        
        
    def __hash__( self ): return hash( self.name )
    
    def __eq__( self, other ):
        return self.__class__ == other.__class__ and self.name==other.name
               
    # resolve static substitutions
    def resolve( self, qtIfwConfig ):
        self.replacements.update({ 
             QT_IFW_TITLE           : qtIfwConfig.configXml.Title 
        ,    QT_IFW_PRODUCT_NAME    : qtIfwConfig.configXml.Name 
        ,    QT_IFW_PRODUCT_VERSION : qtIfwConfig.configXml.Version 
        ,    QT_IFW_PUBLISHER       : qtIfwConfig.configXml.Publisher 
        })
    
    def __resolveContent( self ):
        self.replacements[ _PAGE_NAME_PLACHOLDER ]   = self.name
        self.replacements[ _WIDGET_NAME_PLACHOLDER ] = self.name
        ret = self.content
        for placeholder, value in iteritems( self.replacements ):
            ret = ret.replace( placeholder, value )
        return ret    
        
    def write( self, dirPath ):
        if self.content is None : 
            raise DistBuilderError( "No content found for interface definition: %s" % 
                             (self.name,) )
        if not isDir( dirPath ): makeDir( dirPath )
        filePath = joinPath( dirPath, self.fileName() )
        content = self.__resolveContent()
        print( "Adding interface definition: %s\n\n%s\n" % ( 
                filePath, content ) )                               
        with open( filePath, 'w' ) as f: f.write( content ) 

    def fileName( self ): return _QtIfwInterface._toFileName( self.name )  

    def _onLoadSnippet( self ): return self.onLoad if self.onLoad else ""          

    def _onEnterSnippet( self ): return self.onEnter if self.onEnter else ""          
            
# -----------------------------------------------------------------------------
class QtIfwUiPage( _QtIfwInterface ):

    __FILE_EXTENSION  = "ui"
    __UI_RES_DIR_NAME = "qtifw_ui"

    BASE_ON_LOAD_TMPT = (        
"""    
    var page = gui.pageWidgetByObjectName( "%s" );
    var wizardStyle = installer.value( "%s", "%s" );
    switch( wizardStyle ){
    case "%s": 
        page.minimumSize.width=300;
        break;
    case "%s": 
        page.minimumSize.width=475;
        break;
    case "%s": 
        page.minimumSize.width=480;
        break;        
    default: // "Aero" - This is the hard coded width of QtIfw example .ui's
        page.minimumSize.width=491;   
    }    
""") %  ( "Dynamic%s" # setup subsequent template use
        , _QtIfwScript._WIZARD_STYLE_KEY
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.DEFAULT_WIZARD_STYLE]         
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.MAC]
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.CLASSIC]
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.MODERN]   
        #, QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.AERO]
        )

    BASE_ON_ENTER_TMPT = (    
"""
    var page = gui.pageWidgetByObjectName("Dynamic%s");
    if( installer.value( "auto", "" )=="true" )
        gui.clickButton(buttons.NextButton);
    else {
    %s                        
    }
""")
        
    # QtIfwUiPage    
    def __init__( self, name, pageOrder=None, 
                  sourcePath=None, content=None,
                  onLoad=None, onEnter=None ) :        
        _QtIfwInterface.__init__( self, 
            name, sourcePath, content, onLoad, onEnter )        
        self.pageOrder =( pageOrder if pageOrder in _DEFAULT_PAGES 
                          else None )        
        self.isIncInAutoPilot = False

    def _onLoadSnippet( self ):
        snippet = _QtIfwScript.TAB + _QtIfwScript.log( 
                    "(Custom) %sPageLoaded" % (self.name,) )           
        if self._isOnEnterBase:             
            snippet += QtIfwUiPage.BASE_ON_LOAD_TMPT % (self.name,)
        snippet += self.onLoad if self.onLoad else ""          
        return snippet

    def _onEnterSnippet( self ):        
        snippet = _QtIfwScript.TAB + _QtIfwScript.log( 
                    "(Custom) %sPageCallback" % (self.name,) )        
        if self._isOnEnterBase:             
            snippet +=( QtIfwUiPage.BASE_ON_ENTER_TMPT % 
                       (self.name, (self.onEnter if self.onEnter else "") ) ) 
        else :
            snippet += self.onEnter if self.onEnter else ""          
        return snippet             

# -----------------------------------------------------------------------------    
class QtIfwSimpleTextPage( QtIfwUiPage ):
    
    __SRC  = QtIfwUiPage._toLibResPath( "simpletext" )
    __TITLE_PLACEHOLDER = "[TITLE]"
    __TEXT_PLACEHOLDER = "[TEXT]"

    def __init__( self, name, pageOrder=None, title="", text="", 
                  onLoad=None, onEnter=None ) :
        QtIfwUiPage.__init__( self, name, pageOrder=pageOrder, 
                              onLoad=onLoad, onEnter=onEnter, 
                              sourcePath=QtIfwSimpleTextPage.__SRC )
        self.replacements.update({ 
            QtIfwSimpleTextPage.__TITLE_PLACEHOLDER : title,
            QtIfwSimpleTextPage.__TEXT_PLACEHOLDER : text 
        })
                    
# -----------------------------------------------------------------------------    
class QtIfwDynamicOperationsPage( QtIfwUiPage ):
    
    __SRC = QtIfwUiPage._toLibResPath( "performoperation" )
     
    _TIMER_BUTTON = "timerKludgeButton"
     
    @staticmethod
    def __performOpName( name ): return "_performOp%s" % (name,) 

    @staticmethod
    def __onCompletedName( name ): 
        return "%sCompleted" % ( 
            QtIfwDynamicOperationsPage.__performOpName( name ), )  

    @staticmethod
    def onCompleted( name ):
        return "%s();\n" % ( 
            QtIfwDynamicOperationsPage.__onCompletedName( name ), )  

    def __init__( self, name, operation="", asyncFuncs=None,
                  order=QT_IFW_PRE_INSTALL, 
                  onCompletedDelayMillis=None ) :

        TAB  = _QtIfwScript.TAB
        NEW  = _QtIfwScript.NEW_LINE
        END  = _QtIfwScript.END_LINE
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK

        isPreInstall = order != QT_IFW_POST_INSTALL
                        
        PERFORM_OP_DONE_VALUE = "_isPerformOp%sDone" % (name,)

        ON_TIMEOUT_NAME = "onPerformOp%sTimeOut" % (name,)

        ON_LOAD='page.%s.released.connect(this, this.%s);\n' % ( 
            self._TIMER_BUTTON, ON_TIMEOUT_NAME )                                
        ON_ENTER =( 
            (2*TAB) + _QtIfwScript.ifBoolValue( PERFORM_OP_DONE_VALUE ) +
                (2*TAB) + QtIfwControlScript.clickButton(
                                QtIfwControlScript.NEXT_BUTTON ) +
            (2*TAB) + 'else ' + SBLK +
                (2*TAB) + QtIfwControlScript.enableNextButton( False )  +     
                (2*TAB) + ('if( %s( page ) )' % self.__performOpName( name )) + NEW +
                    (3*TAB) + self.onCompleted( name ) +            
            (2*TAB) + EBLK                     
        )
        OP_FUNC =(
            'function ' + self.__performOpName( name ) + '( page )' + SBLK +
                operation +
            EBLK
        )
        ON_COMPLETED =(
            'function ' + self.__onCompletedName( name ) + '()' + SBLK +
            QtIfwControlScript.assignCustomPageWidgetVar( name ) +     
            _QtIfwScript.setBoolValue( PERFORM_OP_DONE_VALUE, True ) +
            (2*TAB) + QtIfwControlScript.enableNextButton()  +                         
            (QtIfwControlScript.clickButton(
                QtIfwControlScript.NEXT_BUTTON, onCompletedDelayMillis ) 
            if onCompletedDelayMillis is None or onCompletedDelayMillis > 0 
            else "") +             
            EBLK            
        )                
        ON_TIMEOUT =( 
            "var func = " + _QtIfwScript.lookupValue( 
            self.AsyncFunc._TIMEOUT_FUNC_KEY ) + END + 
            "var argsRaw = " + _QtIfwScript.lookupValue( 
                "func", default='""', isAutoQuote=False ) + END +            
            _QtIfwScript.log( '"Async func requested:" + func' , isAutoQuote=False )
        )
        if asyncFuncs is None: asyncFuncs=[]
        for func in asyncFuncs:
            if isinstance( func, self.AsyncFunc ):                 
                ON_TIMEOUT +=(
                    ('if( func==="%s" )' % (func._realName(),)) + SBLK +                    
                    func._execute() +
                    "return" + END +
                    EBLK )
                        
        QtIfwUiPage.__init__( self, name,   
            pageOrder=(QT_IFW_INSTALL_PAGE if isPreInstall else 
                       QT_IFW_FINISHED_PAGE),
            sourcePath=QtIfwDynamicOperationsPage.__SRC,
            onLoad=ON_LOAD, onEnter=ON_ENTER )
                
        self.supportScript = OP_FUNC + NEW + ON_COMPLETED + NEW  
        self.eventHandlers.update({ 
              ON_TIMEOUT_NAME: ON_TIMEOUT
        })        

        self._asyncFuncs      = asyncFuncs
        self._operationFunc   = OP_FUNC 
        self._onCompletedFunc = ON_COMPLETED

    class AsyncFunc:
        
        _TIMEOUT_FUNC_KEY  = "__timeoutFunc"       
        __KEY_PREFIX       = "__async"
        __ARG_DELIMITER    = '__delim__'    
        __DEFINITION_TMPLT =(
    """
    function %s( %s ){
    %s
    }    
    """)
        
        def __init__( self, name, args=None, body="", delayMillis=1,
                      standardPageId=None, customPageName=None ):
            self.name           = name
            self.args           = args if args else []
            self.body           = body
            self.delayMillis    = delayMillis
            self.standardPageId = standardPageId
            self.customPageName = customPageName
    
        def invoke( self, args=None, isAutoQuote=True ):
            if args is None: args=[]        
            if isAutoQuote:
                args = ['"%s"' % (a,) for a in args]        
            if self.standardPageId: 
                args = ['"%s"' % (self.standardPageId,)] + args
            elif self.customPageName: 
                args = ['"%s"' % (self.customPageName,)] + args            
            concat = ' + "%s" + ' % (self.__ARG_DELIMITER,)                    
            return (                                 
                ('installer.setValue( "%s", "%s" );\n' % ( 
                self._TIMEOUT_FUNC_KEY, self._realName() )) +                
                ('installer.setValue( "%s", %s );\n' % ( 
                self._realName(), concat.join( args ) )) +
                ('page.%s.animateClick( %d );\n' % ( 
                 QtIfwDynamicOperationsPage._TIMER_BUTTON, 
                 1 if self.delayMillis < 1 else self.delayMillis )) 
            )
    
        def _define( self ):
            args =( ["page"] + self.args
                if self.standardPageId or self.customPageName else self.args )
            return self.__DEFINITION_TMPLT % ( 
                self._realName(), ", ".join( args ), self.body )       
    
        def _execute( self ):
            snippet = ""
            argOffset=0
            if self.standardPageId: 
                snippet += QtIfwControlScript.assignPageWidgetVar(
                    self.standardPageId )                        
                argOffset+=1
            elif self.customPageName: 
                snippet +=QtIfwControlScript.assignCustomPageWidgetVar(
                    self.customPageName )
                argOffset+=1
            if len(self.args) > 0:
                snippet = 'var args = argsRaw.split( "%s" );\n' % (self.__ARG_DELIMITER,)                                
                for i, p in enumerate( self.args ):
                    snippet +=( "var {0} = args.length > {1} ? args[{1}] : null;\n"
                                .format(p, i+argOffset) )                    
            parms =( ["page"] + self.args
                if self.standardPageId or self.customPageName else self.args )    
            snippet += "%s( %s );\n" % (self._realName(), ", ".join( parms ))
            return snippet   
    
        def _realName( self ): return "%s%s" % (self.__KEY_PREFIX, self.name)    
            
            
# -----------------------------------------------------------------------------    
class QtIfwTargetDirPage( QtIfwUiPage ):
    
    NAME = QT_IFW_REPLACE_PAGE_PREFIX + QT_IFW_TARGET_DIR_PAGE
    __SRC = QtIfwUiPage._toLibResPath( QT_IFW_TARGET_DIR_PAGE )

    def __init__( self ):
            
        ON_TARGET_CHANGED_NAME = "targetDirectoryChanged"
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
        
        ON_TARGET_BROWSE_CLICKED_NAME = "targetChooserClicked"
        ON_TARGET_BROWSE_CLICKED = (
"""
    var page = gui.pageWidgetByObjectName("Dynamic%s");
    var curTarget = Dir.toNativeSeparator( page.targetDirectory.text );
    var newTarget = Dir.toNativeSeparator( 
        QFileDialog.getExistingDirectory( "", curTarget ) );
    if( newTarget ) page.targetDirectory.setText( newTarget );
""") % ( QtIfwTargetDirPage.NAME, )
    
        ON_LOAD = (    
"""
    // patch seems to be needed due to use of RichText?    
    var wizardStyle = installer.value( "%s", "%s" );
    switch( wizardStyle ){
    case "%s": 
        page.warning.minimumSize.width=300;
        break;
    case "%s": 
        page.warning.minimumSize.width=475;
        break;    
    case "%s": 
        page.warning.minimumSize.width=480;
        break;
    }            
    page.targetDirectory.setText(
        Dir.toNativeSeparator(installer.value("TargetDir")));
    page.targetDirectory.textChanged.connect(this, this.%s);    
    page.targetChooser.released.connect(this, this.%s);
""") %  ( _QtIfwScript._WIZARD_STYLE_KEY
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.DEFAULT_WIZARD_STYLE]
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.MAC]
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.CLASSIC]
        , QtIfwConfigXml._WizardStyles[QtIfwConfigXml.WizardStyle.MODERN]   
        , ON_TARGET_CHANGED_NAME
        , ON_TARGET_BROWSE_CLICKED_NAME 
        )
                
        ON_ENTER = (
"""            
    page.targetDirectory.setText(
        Dir.toNativeSeparator(installer.value("TargetDir")));
""")
                
        QtIfwUiPage.__init__( self, QtIfwTargetDirPage.NAME,
            sourcePath=QtIfwTargetDirPage.__SRC, 
            onLoad=ON_LOAD, onEnter=ON_ENTER  )
        
        self.eventHandlers.update({ 
              ON_TARGET_CHANGED_NAME: ON_TARGET_CHANGED
            , ON_TARGET_BROWSE_CLICKED_NAME: ON_TARGET_BROWSE_CLICKED
        })

# -----------------------------------------------------------------------------    
class QtIfwOnPriorInstallationPage( QtIfwUiPage ):
    
    NAME  = "PriorInstallation"

    __SRC = QtIfwUiPage._toLibResPath( "priorinstallation" )
    __PAGE_ORDER = QT_IFW_READY_PAGE

    __TITLE = "Prior Installation Detected"
    
    __TEXT_LABEL      = "description"
    __CONTINUE_BUTTON = "continueButton"
    __STOP_BUTTON     = "stopButton"
    __NOTE_LABEL      = "note"
                
    def __init__( self ) :
        TAB  = _QtIfwScript.TAB
        END  = _QtIfwScript.END_LINE
        NEW  = _QtIfwScript.NEW_LINE
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK

        # TODO: Test for, and resolve this problem: Add/remvoe page could screw up 
        # the page order if multiple custom pages are intended to live before the same  
        # default wizard pages.   
        IS_PAGE_SHOWN_NAME = "isPriorInstallationPageShown"
        IS_PAGE_SHOWN =(
            'function ' + IS_PAGE_SHOWN_NAME + '() ' + SBLK +
                TAB + _QtIfwScript.ifInstalling( isMultiLine=True ) +
                    (2*TAB) + "if( targetExists() ) " + SBLK +
                        # check for the "hard false" to know the page was removed
                        (3*TAB) + _QtIfwScript.ifBoolValue( _REMOVE_TARGET_KEY, 
                                    isHardFalse=True ) +                           
                            (4*TAB) + QtIfwControlScript.insertCustomPage( 
                                QtIfwRemovePriorInstallationPage.NAME,
                                QT_IFW_INSTALL_PAGE ) +
                        (3*TAB) + _QtIfwScript.setBoolValue( _REMOVE_TARGET_KEY, True ) +
                        (3*TAB) + 'switch (' + _QtIfwScript.cmdLineArg( 
                            _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG ) + ')' + SBLK +
                        (3*TAB) + 'case "' + _QtIfwScript.TARGET_EXISTS_OPT_REMOVE + '":' + NEW + 
                            (4*TAB) + 'return false' + END +
                        (3*TAB) + 'default:' + NEW +                
                            (4*TAB) + 'return true' + END +
                        (3*TAB) + EBLK +                                 
                    (2*TAB) + EBLK +      
                    (2*TAB) + "else " + SBLK +
                        # set a "hard false"  when the page is removed
                        (3*TAB) + _QtIfwScript.setBoolValue( _REMOVE_TARGET_KEY, False ) +
                        (3*TAB) + QtIfwControlScript.removeCustomPage( 
                            QtIfwRemovePriorInstallationPage.NAME ) +
                    (2*TAB) + EBLK +  
                TAB + EBLK +     
                TAB + 'return false' + END +                
            EBLK + NEW 
        )

        ON_CONTINUE_CLICKED_NAME = "onPriorInstallContinueClicked"
        ON_CONTINUE_CLICKED = QtIfwControlScript.enableNextButton() 

        ON_STOP_CLICKED_NAME = "onPriorInstallStopClicked"     
        ON_STOP_CLICKED = QtIfwControlScript.enableNextButton( False ) 

        ON_LOAD =( 
"""
    page.%s.released.connect(this, this.%s);
    page.%s.released.connect(this, this.%s);
""" ) % ( QtIfwOnPriorInstallationPage.__CONTINUE_BUTTON, 
            ON_CONTINUE_CLICKED_NAME,
          QtIfwOnPriorInstallationPage.__STOP_BUTTON,     
            ON_STOP_CLICKED_NAME )     
   
        ON_ENTER = ( 
            (2*TAB) + 'if( ' + IS_PAGE_SHOWN_NAME + '() )' + SBLK +            
                (3*TAB) + QtIfwControlScript.enableNextButton(                     
                    QtIfwControlScript.isCustomChecked( 
                        QtIfwOnPriorInstallationPage.__CONTINUE_BUTTON ) ) +                
                (3*TAB) + QtIfwControlScript.setCustomPageTitle( 
                     QtIfwOnPriorInstallationPage.__TITLE ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__TEXT_LABEL ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__CONTINUE_BUTTON ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__STOP_BUTTON ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__NOTE_LABEL ) +                            
            (2*TAB) + EBLK + 
            (2*TAB) +  'else '  + SBLK +
                (3*TAB) + QtIfwControlScript.enableNextButton() +
                (3*TAB) + QtIfwControlScript.setCustomPageTitle( "" ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__TEXT_LABEL, False ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__CONTINUE_BUTTON, False ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__STOP_BUTTON, False ) +
                (3*TAB) + QtIfwControlScript.setCustomVisible( 
                    QtIfwOnPriorInstallationPage.__NOTE_LABEL, False ) +                                             
                (3*TAB) + QtIfwControlScript.clickButton(
                    QtIfwControlScript.NEXT_BUTTON ) +                
            (2*TAB) + EBLK            
        )

        QtIfwUiPage.__init__( self, QtIfwOnPriorInstallationPage.NAME,
            pageOrder=QtIfwOnPriorInstallationPage.__PAGE_ORDER, 
            sourcePath=QtIfwOnPriorInstallationPage.__SRC,
            onLoad=ON_LOAD, onEnter=ON_ENTER  )
        
        self.supportScript = IS_PAGE_SHOWN
        self.eventHandlers.update({ 
              ON_CONTINUE_CLICKED_NAME: ON_CONTINUE_CLICKED
            , ON_STOP_CLICKED_NAME: ON_STOP_CLICKED
        })
                                                      
# -----------------------------------------------------------------------------    
class QtIfwRemovePriorInstallationPage( QtIfwDynamicOperationsPage ):
  
    NAME = "RemovePriorInstallation"
    
    __TITLE = "Removing Prior Installation"
    
    def __init__( self ):

        TAB  = _QtIfwScript.TAB
        END  = _QtIfwScript.END_LINE
        SBLK = _QtIfwScript.START_BLOCK
        EBLK = _QtIfwScript.END_BLOCK

        removeTargetFunc = self.AsyncFunc( "RemoveTarget", 
            customPageName=self.NAME, body=(
           TAB + _QtIfwScript.log( "Removing prior installation..." ) +       
           TAB + 'if( removeTarget() ) ' + SBLK +
               (2*TAB) + QtIfwControlScript.setCustomPageText(
                   self.__TITLE, "The program was successfully removed!" ) +
               (2*TAB) + _QtIfwScript.setBoolValue( _REMOVE_TARGET_KEY, False ) +
               (2*TAB) + self.onCompleted( self.NAME ) +
           TAB + EBLK +
           TAB + 'else ' + SBLK +
               (2*TAB) + QtIfwControlScript.setCustomPageText(
                   "ERROR", "Program removal failed!" ) +
           TAB + EBLK 
        ))
        
        OPERATION=(
            TAB + _QtIfwScript.ifBoolValue( _REMOVE_TARGET_KEY, isMultiLine=True ) +                         
                QtIfwControlScript.setCustomPageText(
                    self.__TITLE, "Removal in progress..." ) +
                removeTargetFunc.invoke() +
                TAB + 'return false' + END +
            TAB + EBLK +    
            TAB + 'return true' + END 
        )

        QtIfwDynamicOperationsPage.__init__( self, 
            QtIfwRemovePriorInstallationPage.NAME, 
            operation=OPERATION, asyncFuncs=[ removeTargetFunc ], 
            order=QT_IFW_PRE_INSTALL, 
            onCompletedDelayMillis=2500 )

# -----------------------------------------------------------------------------
class QtIfwWidget( _QtIfwInterface ):

    __FILE_ROOT_SUFFIX = "-widget"
    
    # QtIfwWidget    
    def __init__( self, name, pageName, position=None, 
                  sourcePath=None, content=None,
                  onLoad=None, onEnter=None ) :
        # TODO: Test onEnter        
        _QtIfwInterface.__init__( self, 
            name, sourcePath, content, onLoad, onEnter )        
        self.pageName =( pageName if pageName in _DEFAULT_PAGES 
                         else None )     
        self.position = position
    
    def _onLoadSnippet( self ):
        snippet = _QtIfwScript.TAB + _QtIfwScript.log( 
                    "%s Widget Loaded" % (self.name,) )              
        snippet += self.onLoad if self.onLoad else ""          
        return snippet
               
    def fileName( self ): 
        return _QtIfwInterface._toFileName( 
            self.name + QtIfwWidget.__FILE_ROOT_SUFFIX )  

# -----------------------------------------------------------------------------
class QtIfwOnFinishedDetachedExec:

    ON_INSTALL, ON_UNINSTALL, ON_BOTH = range(3) 

    __EXEC_DETACHED_TMPLT=(
        'executeDetached( resolveQtIfwPath( "%s" ), %s );\n' )
    __EXEC_CMD_DETACHED_TMPLT=(
        'executeShellCmdDetached( resolveDynamicVars( "%s" ) );\n' ) 
    __EXEC_BAT_DETACHED_TMPLT=(
        'executeBatchDetached( resolveNativePath( "%s" ), null, %s );\n' )
    __EXEC_VBS_DETACHED_TMPLT=(
        'executeVbScriptDetached( resolveNativePath( "%s" ), null, %s );\n' )
    __EXEC_PS_DETACHED_TMPLT=(
        'executePowerShellDetached( resolveNativePath( "%s" ), null, %s );\n' )
    
    __SCRIPT_TMPLTS = { 
          "bat" : __EXEC_BAT_DETACHED_TMPLT 
        , "vbs" : __EXEC_VBS_DETACHED_TMPLT
        , "ps1" : __EXEC_PS_DETACHED_TMPLT
    }
        
    # TODO: Test in NIX/MAC - handle elevation ?
    __REBOOT_CMD =( "shutdown /r -t %d" if IS_WINDOWS else 
                    "sleep %d; sudo reboot" )
    
    # QtIfwOnFinishedDetachedExec
    def __init__( self, name, event=None,   
                  ifwPackage=None, 
                  runProgram=None, argList=None,
                  shellCmd=None, script=None,
                  openViaOsPath=None,                 
                  isReboot=False, rebootDelaySecs=2,
                  ifCondition=None ):
        
        self.name  = name
        self.event =( QtIfwOnFinishedDetachedExec.ON_INSTALL if event is None
                      else event )
                
        self.runProgram  = None
        self.argList     = None
        self.script      = None 
        self.isReboot    = isReboot
        
        self.ifCondition = ifCondition
        self._action     = None                            
                
        if isReboot: self.__setAsReboot( rebootDelaySecs )
        elif isinstance( ifwPackage, QtIfwPackage ): 
            self.__setFromPackage( ifwPackage, argList )
        elif isinstance( script, ExecutableScript ):
            self.__setFromScript( script, argList )
        elif openViaOsPath:
            self._action = QtIfwControlScript.openViaOs( openViaOsPath )                    
        elif shellCmd:   
            # TODO: Figure out how to use quotes in the commands here!
            # It seems they never work - around paths in the command 
            # or around entire commands.
            # Escape quotes & backslashes for the QScript literal. 
            shellCmd = shellCmd.replace('\\','\\\\').replace('"','\\"')
            self._action =( QtIfwOnFinishedDetachedExec.__EXEC_CMD_DETACHED_TMPLT 
                            % (shellCmd,) )
        else :
            self.runProgram = runProgram
            self.argList    = argList                     
            self.__setSimpleExecDetachedAction()
        
    # TODO: Bind this logic with that in QtIfwConfigXml         
    # TODO: Test implementation of QtIfwExeWrapper
    def __setFromPackage( self, ifwPackage, argList ) :
        if ifwPackage.exeWrapper:
            self.runProgram = ifwPackage.exeWrapper._runProgram 
            self.argList    = ifwPackage.exeWrapper._runProgArgs                        
        elif ifwPackage.exeName:        
            exeName = util.normBinaryName( ifwPackage.exeName, 
                                           isGui=ifwPackage.isGui )            
            programPath = joinPathQtIfw( QT_IFW_TARGET_DIR, exeName )
            self.argList = argList    
            if util._isMacApp( exeName ):   
                self.runProgram = util._LAUNCH_MACOS_APP_CMD 
                if not isinstance( self.argList, list ): self.argList = []
                else: self.argList.insert( 0, util._LAUNCH_MACOS_APP_ARGS_SWITCH )     
                self.argList.insert( 0, programPath )
            else: self.runProgram = programPath                                    
        self.__setSimpleExecDetachedAction()

    # TODO: Finish testing and filling in the use of arguments in each script
    # type context
    def __setFromScript( self, script, argList ):         
        self.script = script
        self.runProgram = joinPathQtIfw( _ENV_TEMP_DIR, script.fileName() )
        self.argList = argList
        args =( '[%s]' % (",".join( ['"%s"' % (a,) for a in self.argList ] ),) 
                if self.argList else _QtIfwScript.NULL )        
        execTemplate = QtIfwOnFinishedDetachedExec.__SCRIPT_TMPLTS.get( 
            script.extension )
        if execTemplate is None: raise DistBuilderError("Script type not supported")
        self._action =( 
            _QtIfwScript.genResources( [script], isTempRootTarget=True ) +
            execTemplate % ( self.runProgram, args ) 
        )
                                                        
    def __setAsReboot( self, rebootDelaySecs ):
        self.isReboot = True
        cmd = QtIfwOnFinishedDetachedExec.__REBOOT_CMD % (rebootDelaySecs,)
        self._action =( 
            QtIfwOnFinishedDetachedExec.__EXEC_CMD_DETACHED_TMPLT % (cmd,) )

    def __setSimpleExecDetachedAction( self ):
        args = self.argList if self.argList else []        
        args = '[%s]' % (",".join( ['"%s"' % (a,) for a in args] ),)            
        self._action = QtIfwOnFinishedDetachedExec.__EXEC_DETACHED_TMPLT % (
            self.runProgram, args ) 

# -----------------------------------------------------------------------------    
class QtIfwOnFinishedCheckbox( QtIfwWidget, QtIfwOnFinishedDetachedExec ):

    __AUTO_POSITION = 0
    
    __CHECKBOX_SUFFIX = "CheckBox"
    __PAGE_ID = QT_IFW_FINISHED_PAGE
    __SRC     = QtIfwWidget._toLibResPath( "altrunitcheckbox-widget" )

    __CHECKBOX_NAME_PLACEHOLDER = "[CHECKBOX_NAME]"
    __TEXT_PLACEHOLDER          = "[TEXT]"    
    __IS_VISIBLE_PLACEHOLDER    = "[IS_VISIBLE]"
    __IS_ENABLED_PLACEHOLDER    = "[IS_ENABLED]"
    __IS_CHECKED_PLACEHOLDER    = "[IS_CHECKED]"

    # TODO: Test in NIX/MAC
    BASE_ON_LOAD_TMPT = (    
"""
    var widget = gui.pageById(QInstaller.%s).%s;
    switch( systemInfo.kernelType ){
    case "darwin": // macOS
        widget.minimumSize.width=221;
        break;
    case "linux": 
        widget.minimumSize.width=401;
        break;
    default: // "windows"
        // This is the hard coded width of "standard" QtIfw widgets
        widget.minimumSize.width=412;   
    }    
""")
    
    __RUN_PROG_DESCR_TMPLT = "Run %s now."
        
    __REBOOT_TEXT = "REBOOT NOW."
        
    # QtIfwOnFinishedCheckbox
    def __init__( self, name, text=None, position=None,  
                  ifwPackage=None, 
                  runProgram=None, argList=None,
                  shellCmd=None, script=None,
                  openViaOsPath=None,                 
                  isReboot=False, rebootDelaySecs=2,                    
                  isVisible=True, isEnabled=True, isChecked=True ) :
        QtIfwWidget.__init__( self, name, QtIfwOnFinishedCheckbox.__PAGE_ID, 
            position=( position if position else 
                       QtIfwOnFinishedCheckbox.__AUTO_POSITION ),             
            sourcePath=QtIfwOnFinishedCheckbox.__SRC )
        QtIfwOnFinishedDetachedExec.__init__( self, name,
            event=QtIfwOnFinishedDetachedExec.ON_INSTALL,   
            ifwPackage=ifwPackage, 
            runProgram=runProgram, argList=argList,
            shellCmd=shellCmd, script=script,
            openViaOsPath=openViaOsPath,                 
            isReboot=isReboot, rebootDelaySecs=rebootDelaySecs )                            
        
        QtIfwOnFinishedCheckbox.__AUTO_POSITION += 1                    
        checkboxName = name + self.__CHECKBOX_SUFFIX
        self.checkboxName = "%s.%s" % ( self.name, checkboxName )
        
        self.text = None                
        if isReboot: self.__setAsReboot()
        elif isinstance( ifwPackage, QtIfwPackage ): 
            self.__setFromPackage( ifwPackage )            
        if text: self.text = text # allows override from prior set defaults
            
        self.replacements.update({ 
              self.__CHECKBOX_NAME_PLACEHOLDER: checkboxName 
            , self.__TEXT_PLACEHOLDER : self.text
            , self.__IS_VISIBLE_PLACEHOLDER : _QtIfwScript.toBool( isVisible )
            , self.__IS_ENABLED_PLACEHOLDER : _QtIfwScript.toBool( isEnabled )
            , self.__IS_CHECKED_PLACEHOLDER : _QtIfwScript.toBool( isChecked )            
        })       
        
    # TODO: Bind this logic with that in QtIfwConfigXml         
    # TODO: Test implementation of QtIfwExeWrapper
    def __setFromPackage( self, ifwPackage ) :
        self.text =( QtIfwOnFinishedCheckbox.__RUN_PROG_DESCR_TMPLT
                       % (ifwPackage.pkgXml.DisplayName,) )
                                                        
    def __setAsReboot( self ):
        self.text =  QtIfwOnFinishedCheckbox.__REBOOT_TEXT   
        self.onEnter =(
            _QtIfwScript.ifInstalling( isMultiLine=True ) +
                _QtIfwScript.ifCmdLineArg( _QtIfwScript.REBOOT_CMD_ARG ) +               
                    _QtIfwScript.TAB + self.setChecked( 
                        _QtIfwScript.cmdLineSwitchArg(
                            _QtIfwScript.REBOOT_CMD_ARG ) ) +
            _QtIfwScript.END_BLOCK                                
            )                                                                 
                                                                                                            
    def _onLoadSnippet( self ):
        snippet = _QtIfwScript.TAB + _QtIfwScript.log( 
                    "%s Widget Loaded" % (self.name,) )              
        if self._isOnLoadBase:             
            snippet += QtIfwOnFinishedCheckbox.BASE_ON_LOAD_TMPT % (
                self.pageName, self.name )
        snippet += self.onLoad if self.onLoad else ""          
        return snippet
    
    # Dynamic script
    def isChecked( self ): 
        return QtIfwControlScript.isChecked( self.checkboxName )

    def setChecked( self, isChecked=True ):
        return QtIfwControlScript.setChecked( self.checkboxName, isChecked )

    def enable( self, isEnable=True ): 
        return QtIfwControlScript.enable( self.checkboxName, isEnable )

    def setVisible( self, isVisible=True ): 
        return QtIfwControlScript.setVisible( self.checkboxName, isVisible )
                            
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
            raise DistBuilderError( "Qt IWF installer binary not found." )
        installerPath = binPath  
    else : isDmgMount = False        
    if targetPath is None: 
        version = __QtIfwInstallerVersion( installerPath )
        targetPath = __defaultQtIfwPath( version ) 
        print( "targetPath: %s" % (targetPath,) )   
    if isFile( __qtIfwCreatorPath( targetPath ) ):
        if not isLocal: removeFile( installerPath )
        raise DistBuilderError( "A copy of QtIFW is already installed in: %s" 
                         % (targetPath,) )                             
    ifwQScriptPath = __generateQtIfwInstallerQScript()
    ifwPyScriptPath = __generateQtIfwInstallPyScript(                                    
        installerPath, ifwQScriptPath, targetPath )    
    runPy( ifwPyScriptPath, isElevated=True )
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

def __defaultQtIfwArchiveGenPath( version=QT_IFW_DEFAULT_VERSION ):
    return __qtIfwArchiveGenPath( __defaultQtIfwPath( version ) )

def __qtIfwArchiveGenPath( qtIfwDir ):
    generatorPath = joinPath( qtIfwDir, 
        joinPath( __BIN_SUB_DIR, __QT_IFW_ARCHIVEGEN_EXE_NAME ) )
    return generatorPath if isFile( generatorPath ) else None
    
# -----------------------------------------------------------------------------                
def findQtIfwPackage( pkgs, pkgId ):        
    for p in pkgs: 
        if p.pkgId==pkgId: return p
    return None 

def findQtIfwUiPage( pkgs, name ):
    for p in pkgs: 
        for p in p.uiPages: 
            if p.name==name: return p
    return None     

def findQtIfwWidget( pkgs, name ):
    for p in pkgs: 
        for w in p.widgets: 
            if w.name==name: return w
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
        raise DistBuilderError( "Cannot merge QtIfw packages. " 
                         "Invalid id(s) provided." )     
    mergeDirs( srcPkg.contentTopDirPath(), destPkg.contentDirPath() )    
    __mergePackageObjects( srcPkg, destPkg )    
    removeQtIfwPackage( pkgs, srcId )    
    return destPkg

def nestQtIfwPackage( pkgs, childId, parentId, subDirName=None ):                
    childPkg  = findQtIfwPackage( pkgs, childId )
    parentPkg = findQtIfwPackage( pkgs, parentId )
    if not childPkg or not parentPkg:
        raise DistBuilderError( "Cannot nest QtIfw package. " 
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
    if srcPkg.uiPages:
        try: destPkg.uiPages.extend( srcPkg.uiPages )
        except: destPkg.uiPages = srcPkg.uiPages
        destPkg.uiPages = list(set( destPkg.uiPages ))
    if srcPkg.licenses:       
        # (licenses is a dictionary, not a list)
        try: destPkg.licenses.extend( srcPkg.licenses )
        except: destPkg.licenses = srcPkg.licenses                
    if srcPkg.isLicenseFormatPreserved:
        destPkg.isLicenseFormatPreserved = True      
    try: 
        srcShortcuts = srcPkg.pkgScript.shortcuts
        if subDirName:
            for i, _ in enumerate( srcShortcuts ): 
                srcShortcuts[i].exeDir = joinPathQtIfw( 
                    QT_IFW_TARGET_DIR, subDirName )                
    except: srcShortcuts = []
    if srcPkg.codeSignTargets:
        try: destPkg.codeSignTargets.extend( srcPkg.codeSignTargets )
        except: destPkg.codeSignTargets = srcPkg.codeSignTargets
        destPkg.codeSignTargets = list(set( destPkg.codeSignTargets ))                    
    if destPkg.pkgScript:    
        if srcShortcuts:
            try: destPkg.pkgScript.shortcuts.extend( srcShortcuts )
            except: destPkg.pkgScript.shortcuts = srcShortcuts
        if srcPkg.pkgScript.externalOps: 
            try: destPkg.pkgScript.externalOps.extend( srcPkg.pkgScript.externalOps )
            except: destPkg.pkgScript.externalOps = srcPkg.pkgScript.externalOps
        if srcPkg.pkgScript.customOperations:
            try: destPkg.pkgScript.customOperations.extend( srcPkg.pkgScript.customOperations )
            except: destPkg.pkgScript.customOperations = srcPkg.pkgScript.customOperations
        if srcPkg.pkgScript.killOps:
            try: destPkg.pkgScript.killOps.extend( srcPkg.pkgScript.killOps )
            except: destPkg.pkgScript.killOps = srcPkg.pkgScript.killOps
        if srcPkg.pkgScript.bundledScripts:
            try: destPkg.pkgScript.bundledScripts.extend( srcPkg.pkgScript.bundledScripts )
            except: destPkg.pkgScript.bundledScripts = srcPkg.pkgScript.bundledScripts
        if srcPkg.pkgScript.installResources:
            try: destPkg.pkgScript.installResources.extend( srcPkg.pkgScript.installResources )
            except: destPkg.pkgScript.installResources = srcPkg.pkgScript.installResources
            destPkg.pkgScript.installResources = list(set( destPkg.pkgScript.installResources ))                        
        if IS_LINUX: 
            if srcPkg.pkgScript.isAskPassProgRequired:
                destPkg.pkgScript.pkgScript.isAskPassProgRequired=True                    
        print( "\nRegenerating installer package script: %s...\n" 
                % (destPkg.pkgScript.path()) )
        destPkg.pkgScript._generate()
        print( "script: \n" )
        destPkg.pkgScript.debug()
        destPkg.pkgScript.write()    
    destPkg._isMergeProduct = True
    
# -----------------------------------------------------------------------------            
def buildInstaller( qtIfwConfig, isSilent ):
    ''' returns setupExePath '''
    _stageInstallerPackages( qtIfwConfig, isSilent )
    return _buildInstaller( qtIfwConfig, isSilent )

def _stageInstallerPackages( qtIfwConfig, isSilent ):
    __validateConfig( qtIfwConfig )        
    __initBuild( qtIfwConfig )    
    __addInstallerResources( qtIfwConfig )     

def _buildInstaller( qtIfwConfig, isSilent ):    
    for pkg in qtIfwConfig.packages:
        if pkg._isMergeProduct:
            __genQtIfwCntrlRes( qtIfwConfig )
            break          
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
        raise DistBuilderError( "Installer definition directory path is not valid" )
    if qtIfwConfig.packages is None :
        raise DistBuilderError( "Package specification(s)/definition(s) required" )
    for p in qtIfwConfig.packages :
        if p.pkgType==QtIfwPackage.Type.RESOURCE: continue
        if p.srcDirPath is None:
            if p.srcExePath is None:
                raise DistBuilderError( "Package Source directory OR exe path required" )
            elif not ( isFile(p.srcExePath) or 
                  (IS_MACOS and util._isMacApp(p.srcExePath)) ) :        
                raise DistBuilderError( "Package Source exe path is not valid" )    
        elif not isDir(p.srcDirPath) :        
            raise DistBuilderError( "Package Source directory path is not valid" )
    # resolve or install required utility paths 
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = getenv( QT_IFW_DIR_ENV_VAR )    
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = __defaultQtIfwPath( isVerified=True )
    if qtIfwConfig.qtIfwDirPath is None:
        qtIfwConfig.qtIfwDirPath = installQtIfw()                    
    if( qtIfwConfig.qtIfwDirPath is None or
        not isFile( __qtIfwCreatorPath( qtIfwConfig.qtIfwDirPath ) ) ):        
        raise DistBuilderError( "Valid Qt IFW directory path required" )
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
        
        def stageContent( p ):
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

        def stageAdditionalResources( p ):        
            p.pkgScript._flatten()        
            for res in p.pkgScript.installResources:
                if isinstance( res, QtIfwExternalResource ) and res.srcPath: 
                    __addArchive( res.srcPath, p, qtIfwConfig, 
                                  archiveRootName=res.name )        
        
        if not p.pkgType==QtIfwPackage.Type.RESOURCE: stageContent( p )
        stageAdditionalResources( p )
                                        
    print( "Build directory created: %s" % (BUILD_SETUP_DIR_PATH,) )

def __addInstallerResources( qtIfwConfig ) :
        
    qtIfwConfig._scrubEmbeddedResources()
    qtIfwConfig.addUiElements( QtIfwTargetDirPage(), isOverWrite=False )
    qtIfwConfig.addUiElements( QtIfwOnPriorInstallationPage(), isOverWrite=False )
    qtIfwConfig.addUiElements( QtIfwRemovePriorInstallationPage(), isOverWrite=False )
    
    __genQtIfwCntrlRes( qtIfwConfig ) 
                                      
    for p in qtIfwConfig.packages :
        if not isinstance( p, QtIfwPackage ) : continue
        __addLicenses( p )
        pkgXml = p.pkgXml              
        pkgScript = p.pkgScript       
        if pkgXml :            
            print( "Adding installer package definition: %s\n..." 
                   % (pkgXml.pkgName,) )
            pkgXml.debug()
            pkgXml.write()            
        if pkgScript :
            print( "Adding installer package script: %s\n..." 
                   % (pkgScript.fileName,) )
            pkgScript.debug()
            pkgScript.write()

        if p.uiPages: __addUiPages( qtIfwConfig, p ) 
        if p.widgets: __addWidgets( qtIfwConfig, p ) 

        if p.pkgType == QtIfwPackage.Type.QT_CPP : 
            p.qtCppConfig.addDependencies( p )        

        if p.distResources: __addResources( p )     

        if isinstance( p.exeWrapper, QtIfwExeWrapper ): 
            __addExeWrapper( p )
                        
def __genQtIfwCntrlRes( qtIfwConfig ) :
    
    configXml = qtIfwConfig.configXml
    ctrlScript = qtIfwConfig.controlScript
    
    if ctrlScript and configXml: 
        configXml.ControlScript = ctrlScript.fileName         
            
    if configXml :         
        print( "%s installer configuration resources..." 
               % ( "Regenerating" if configXml.exists() else "Adding" ) )
        configXml.debug()
        configXml.write()
        def copyToConfigDir( scrPaths ):
            for scrPath in scrPaths:
                if scrPath :
                    scrPath = absPath( scrPath )
                    if isFile( scrPath ):
                        copyFile( scrPath,                       
                                  joinPath( configXml.dirPath(), 
                                            baseFileName( scrPath ) ) )                
        copyToConfigDir([ configXml.iconFilePath 
                        , configXml.logoFilePath 
                        , configXml.bannerFilePath 
                        ])
    if ctrlScript :
        # Allow component selection to be explicitly disabled, but force that
        # when there are not multiple packages to begin with
        if len(qtIfwConfig.packages) < 2:
            ctrlScript.isComponentSelectionPageVisible=False 
        # Allow start menu target to be explicitly disabled, but force that
        # when there are no shortcuts being installed there to begin with        # 
        if IS_WINDOWS:  
            isStartMenuUpdated = False  
            for p in qtIfwConfig.packages :
                try:                    
                    for shortcut in p.pkgScript.shortcuts:
                        isStartMenuUpdated = ( shortcut.exeName is not None 
                                               and shortcut.isAppShortcut )
                        if isStartMenuUpdated: break
                    if isStartMenuUpdated: break
                except: pass            
            if not isStartMenuUpdated:    
                ctrlScript.isStartMenuDirectoryPageVisible=False

        print( "%s installer control script...\n" 
               % ( "Regenerating" if ctrlScript.exists() else "Adding" ) )       
        if ctrlScript.script: ctrlScript._generate() 
        ctrlScript.debug()
        ctrlScript.write()        

__CHAR_SWAP = { u'\u201c': u'"'
            , u'\u201D': u'"' 
            , u'\u2018': u"'" 
            , u'\u2019': u"'" 
}

def __scrubLicenseText( text ):    
    try:
        for k,v in iteritems( __CHAR_SWAP ): 
            text = text.replace(k,v)
    except: pass     
    try: return str( text ) if PY2 else bytes( text, 'ascii' ).decode('ascii')
    except UnicodeEncodeError:
        return text.encode('ascii', 'replace').decode('ascii')
    except: return ""
    
def __addLicenses( package ) :
    if package.licenses is None or len(package.licenses)==0: return
    print( "Adding licenses..." )
    destDir = package.metaDirPath()
    fixFormat = not package.isLicenseFormatPreserved
    if not exists( destDir ): makeDir( destDir )
    for name, filePath in iteritems( package.licenses ):
        fileName = baseFileName( filePath )
        package.pkgXml.Licenses[name] = fileName
        srcPath = absPath( filePath, basePath=package.resBasePath )
        if fixFormat:
            # Change white space to resemble web browser rendering,
            # (e.g. left flushed), w/ natural word wrapping, but 
            # preserve hard blanks (as single instances of such).
            revLines=[]
            with open( srcPath, 'r' ) as f:
                lines = [ ln.strip() for ln in f.readlines() ]                
                curLn=""
                for ln in lines: 
                    ln = __scrubLicenseText( ln )
                    if len(curLn) > 0:
                        if len(ln)==0:
                            revLines += [ curLn, "" ]
                            curLn=""
                        else: curLn += " " + ln
                    else: curLn += ln                    
                if len(curLn) > 0: revLines.append( curLn )        
                revLines = [ ln + util._NEWLINE for ln in revLines ]
            destPath = joinPath( destDir, fileName )    
            with open( destPath, 'w' ) as f: f.writelines( revLines )                    
        else: copyToDir( srcPath, destDir )        
                            
def __addUiPages( qtIfwConfig, package ) :
    if package.uiPages is None or len(package.uiPages)==0: return
    print( "Adding custom installer pages..." )
    for ui in package.uiPages:
        if isinstance( ui, QtIfwUiPage ):
            ui.resolve( qtIfwConfig ) 
            ui.write( package.metaDirPath() )

def __addWidgets( qtIfwConfig, package ) :
    if package.widgets is None or len(package.widgets)==0: return
    print( "Adding custom installer widgets..." )
    for widget in package.widgets:
        if isinstance( widget, QtIfwWidget ):
            widget.resolve( qtIfwConfig ) 
            widget.write( package.metaDirPath() )
                
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
    
def __addArchive( srcPaths, package, qtIfwConfig, archiveRootName=None ):
    if archiveRootName is None:
        if isinstance( srcPaths, list ):            
            if len(srcPaths)==1: archiveRootName = rootFileName( srcPaths[0] ) 
            else: raise DistBuilderError( "An archive root name must be provided" )
        else: 
            archiveRootName = rootFileName( srcPaths )        
    if not isinstance( srcPaths, list ): srcPaths=[srcPaths]  
    archives=[ c for c in srcPaths 
               if fileExt( c ).lower()==_QT_IFW_ARCHIVE_EXT ]
    nonArchives=[ c for c in srcPaths if c not in archives ]
    destDir = package.contentTopDirPath()
    if not exists( destDir ): makeDir( destDir )
    if len( archives ) > 0:
        print( "Copying pre-compressed archives to QT IFW package...\n" ) 
        copyToDir( archives, destDir )    
    if len( nonArchives ) > 0:
        print( "Generating archive for QT IFW package...\n" )            
        generatorPath = __qtIfwArchiveGenPath( qtIfwConfig.qtIfwDirPath )
        destPath = joinPath( destDir, 
                    joinExt( archiveRootName, _QT_IFW_ARCHIVE_EXT ) )
        nonArchives = [ joinPath( p, "*" ) 
                        if isDir( p ) else p for p in nonArchives ]               
        scrList = " ".join( [ '"%s"' % (p,) for p in nonArchives ] )                     
        cmd = '%s "%s" %s' % ( generatorPath, destPath, scrList )
        util._system( cmd )  
        if not exists( destPath ) : 
            raise DistBuilderError( 'FAILED to create "%s"' % (destPath,) )

def __build( qtIfwConfig ) :
    print( "Building installer using Qt IFW...\n" )
    creatorPath = __qtIfwCreatorPath( qtIfwConfig.qtIfwDirPath )
    setupExePath = joinPath( THIS_DIR, 
                             util.normBinaryName( qtIfwConfig.setupExeName ) )
    cmd = '%s %s %s "%s"' % ( creatorPath, __QT_IFW_CREATOR_OFFLINE_SWITCH,
                              str(qtIfwConfig), setupExePath )
    util._system( cmd )  
    setupExePath = normBinaryName( setupExePath, 
                                   isPathPreserved=True, isGui=True )
    if not exists( setupExePath ) : 
        raise DistBuilderError( 'FAILED to create "%s"' % (setupExePath,) )
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
    print( "Building silent wrapper executable...\n" )
    from distbuilder.process import PyToBinPackageProcess, ConfigFactory
    
    cfgXml    = qtIfwConfig.configXml
    ctrlScrpt = qtIfwConfig.controlScript
    
    # On macOS, a "gui" .app must be build because that provides a .plist
    # and an application we can best manipulate via AppleScript    
    srcSetupExeName   = util.normBinaryName( qtIfwConfig.setupExeName, isGui=True )    
    destSetupExeName  = util.normBinaryName( qtIfwConfig.setupExeName, isGui=False ) 
    nestedExeName     = util.normBinaryName( __NESTED_INSTALLER_NAME,  isGui=True )
    wrapperExeName    = __WRAPPER_INSTALLER_NAME
    wrapperPyName     = __WRAPPER_SCRIPT_NAME    
    componentList     = [] 
    MIN_SORT_PRIORITY = 9999999999
    for p in qtIfwConfig.packages:
        if p.pkgXml.Virtual: continue  # package never shown to the user      
        isRequired = p.pkgXml.ForcedInstallation 
        isDefault = p.pkgXml.Default   
        sortPriority = p.pkgXml.SortingPriority
        if sortPriority is None: sortPriority = MIN_SORT_PRIORITY  
        componentList.append( (isRequired, isDefault, 
            p.pkgXml.pkgName, p.pkgXml.DisplayName, sortPriority) )
    componentList.sort( key=itemgetter(4), reverse=True ) 

    licenses={}
    for p in qtIfwConfig.packages:
        pkgLics={}
        for name, filePath in iteritems( p.licenses ):
            srcPath = absPath( filePath, basePath=p.resBasePath )            
            with open( srcPath, 'r' ) as f: 
                pkgLics[name] = __scrubLicenseText( f.read() )
        if len(pkgLics) > 0: licenses[p.pkgXml.pkgName] = pkgLics
    isRunSwitch=( False if cfgXml.RunProgram is None or 
                  not ctrlScrpt.isRunProgChecked else 
                  None if ctrlScrpt.isRunProgEnabled and 
                          ctrlScrpt.isRunProgVisible else True )
    isRebootSwitch = None
    for p in qtIfwConfig.packages:
        for w in p.widgets:
            if( isinstance(w, QtIfwOnFinishedCheckbox)
                and w.isReboot):
                isRebootSwitch = False # Show option, but disabled
                break            
        if isRebootSwitch is not None: break
            
    wrapperScript = __silentQtIfwScript( nestedExeName, componentList,
        isRunSwitch=isRunSwitch, isRebootSwitch=isRebootSwitch, 
        licenses=licenses, 
        isStartMenu=ctrlScrpt.isStartMenuDirectoryPageVisible,
        setupTitle=cfgXml._titleDisplayed(), version=cfgXml.Version,
        companyLegalName=cfgXml.Publisher )
                                               
    f = configFactory  = ConfigFactory()
    f.productName      = cfgXml.Name
    f.description      = cfgXml._titleDisplayed()
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
            if IS_WINDOWS:
                cfg.isAutoElevated = True # Windows only feature
                cfg.versionInfo.exeName = destSetupExeName
            
        def onFinalize( self ):
            removeFromDir( wrapperPyName )            
            removeFromDir( self.__nestedZipPath 
                           if IS_MACOS else nestedExeName )
            dirName = baseFileName( self.binDir )
            binName = baseFileName( self.binPath )       
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

# TODO: Break up this monolith!    
def __silentQtIfwScript( exeName, componentList=None,
                         isQtIfwInstaller=False,
                         isQtIfwUnInstaller=False,
                         scriptPath=None,
                         wrkDir=None, targetDir=None,
                         isRunSwitch=None, isRebootSwitch=None,
                         licenses=None, isStartMenu=True,
                         setupTitle=None, version=None, 
                         companyLegalName=None ) :
    """
    Runs the IFW exe from inside the PyInstaller MEIPASS directory,
    with elevated privileges, hidden from view, gathering
    stdout, stderr, and other logged communications.  
    Note: On Windows, the wrapper is auto-elevated via PyInstaller.
    """
    if componentList is None: componentList=[]
    if licenses is None: licenses={}
    
    versionInfo = setupTitle if setupTitle else ""
    if version:
        if len(versionInfo) > 0 : versionInfo += "\\n"
        versionInfo += "Version: %s" % (version,)
    if companyLegalName:
        if len(versionInfo) > 0 : versionInfo += "\\n"
        versionInfo += "Copyright (c) %d, %s. All rights reserved." % ( 
            date.today().year,
            (companyLegalName[:-1] if companyLegalName.endswith(".") else
             companyLegalName) )
    
    componentsRepr     = ""
    componentsReqRepr  = ""
    componentsEpilogue = "" 
    componentsPrefix   = ""    
    if len(componentList) > 1 :
        componentsRepr = ""
        idLen = 0 
        for (isReq, _, compId, _, _) in componentList :
            componentsRepr += ( ("" if componentsRepr=="" else ", ")  
                              + ("'%s'" % (compId,)) )
            if isReq:            
                componentsReqRepr += ( ("" if componentsReqRepr=="" else ", ")  
                                       + ("'%s'" % (compId,)) )                        
            if len( compId ) > idLen : idLen = len( compId )
            prefix = ".".join( compId.split(".")[:-1] ) + "."
            if componentsPrefix=="" : componentsPrefix = prefix
            elif prefix != componentsPrefix: componentsPrefix=None
        componentsRepr = "[ " + componentsRepr + " ]"            
        componentsReqRepr = "[ " + componentsReqRepr + " ]"
        componentsPrefixLen = (0 if componentsPrefix is None 
                               else len(componentsPrefix) )
        lineLen = 79
        flagLen = 3
        idLen = idLen - componentsPrefixLen + 2        
        nameLen = lineLen - flagLen - idLen   
        lnFormat = '{0:>%s}{1:<%s}{2:<%s}\n' % ( flagLen, idLen, nameLen )
        componentsEpilogue = ( "components:\n" + 
            lnFormat.format("  ", "id", "name\n" ) )
        REQ_SYM = "* "  
        DEF_SYM = "+ "
        for (isReq, isDef, compId, name, _) in componentList :
            req = REQ_SYM if isReq else DEF_SYM if isDef else ""
            if componentsPrefixLen : compId = compId[componentsPrefixLen:]
            componentsEpilogue += lnFormat.format( req, compId, name ) 
        componentsEpilogue+="\n%s= Required   %s= Default" % (REQ_SYM,DEF_SYM)        
    if componentsPrefix is None: componentsPrefix = ""
    if componentsRepr == "": componentsRepr = "[]" 
    if componentsReqRepr == "": componentsReqRepr = "[]"  
    licensesRepr = str(licenses)   
        
    if IS_WINDOWS: 
        imports = (
"""     
from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW
try: from subprocess import DEVNULL 
except ImportError: DEVNULL = open(os.devnull, 'wb')
import tempfile
import glob
""" )
        
        helpers = ""
        preProcess = ""

        runInstallerProcess = (
"""                     
    PS                  = "powershell"
    PS_START            = "Start-Process"
    PS_PATH_SWITCH      = "-FilePath"
    PS_WAIT_SWITCH      = "-Wait"
    PS_WIN_STYLE_SWITCH = "-WindowStyle"
    PS_WIN_STYLE_HIDDEN = "Hidden"
    PS_REDIRECT_STDOUT  = "-RedirectStandardOutput"
    PS_REDIRECT_STDERR  = "-RedirectStandardError"
    
    psArgs = [PS, PS_START, PS_PATH_SWITCH, EXE_PATH, 
              PS_WAIT_SWITCH, PS_WIN_STYLE_SWITCH, PS_WIN_STYLE_HIDDEN]              
    
    if REDIRECT_PATH:
        # PS Start-Process will not redirect both streams to the same file
        outPath = REDIRECT_PATH + ".out"
        errPath = REDIRECT_PATH + ".err"
        psArgs += [PS_REDIRECT_STDOUT, outPath, PS_REDIRECT_STDERR, errPath]
                                                            
    psArgs = list2cmdline( psArgs ) 

    keepAliveFilePath = tempfile.mktemp( suffix='.keep' ).replace( "\\\\","/" )
    with open( keepAliveFilePath, 'w' ) as f: pass
    
    keepAliveArg  = '{0}="%s"' % (keepAliveFilePath,)
    installerArgs = (ARGS if len(ARGS) > 0 else []) + [keepAliveArg]
    psArgs +=( " -ArgumentList " + 
        ",".join( [ "'%s'" % (a.replace('"','\\\\"'),) 
                    for a in installerArgs ] ) 
    )

    processStartupInfo = STARTUPINFO()
    processStartupInfo.dwFlags |= STARTF_USESHOWWINDOW
    # passing psArgs as a string vs list prevents more auto escape nonsense!
    # print( psArgs )
    process = Popen( psArgs, cwd=WORK_DIR, 
                     shell=False, universal_newlines=True,
                     stdin=DEVNULL, # Prevent PS blocking encountered in special contexts
                     startupinfo=processStartupInfo )

    # The PowerShell layer is used because it *actually* hides the installer.
    # The wait switch causes it to wait until not only the installer completes,  
    # but all of it's descendants (See https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-7#parameters). 
    # That even includes *detached* processes! It does not pipe back stdout/err,
    # despite putting it on the screen.  More complicated PS scripts can read
    # and pipe back stdout/err, but refused to hide the QtIFW window (like every 
    # other attempted mechanism). So, instead watch for the "keep alive file" 
    # to be deleted by the installer, and then kill it from here. 
    POLL_FREQ_SECS = 0.1
    RUN_PROG_DETACHED_DELAY_SECS = 2
    while process.poll() is None and os.path.exists( keepAliveFilePath ):
        time.sleep( POLL_FREQ_SECS )                                    
    if os.path.exists( keepAliveFilePath ):
        os.remove( keepAliveFilePath )
    else: 
        time.sleep( RUN_PROG_DETACHED_DELAY_SECS )
        process.kill()        
        retCode=0

    if REDIRECT_PATH:
        output = ""
        try: 
            with open( outPath, 'r' ) as f: output += f.read()
            os.remove( outPath )
        except: pass
        try: 
            with open( errPath, 'r' ) as f: output += f.read()
            os.remove( errPath )
        except: pass
        with open( REDIRECT_PATH, 'a+' ) as f: f.write( output )                                                                      
""" ).format( _QtIfwScript._KEEP_ALIVE_PATH_CMD_ARG )

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
    
    removeIfwLogs()
                                
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

            
        runInstallerProcess = (
"""    
    shArgs = [ "sudo", BIN_PATH ] + ARGS
    #print( list2cmdline( shArgs ) )
    process = Popen( shArgs, cwd=WORK_DIR,
                     shell=False, universal_newlines=True,
                     stdout=PIPE, stderr=PIPE )
                     
    if IS_VERBOSE :
        POLL_FREQ_SECS = 0.1        
        while process.poll() is None:
            sys.stdout.write( process.stdout.read() )
            sys.stderr.write( process.stderr.read() )
            time.sleep( POLL_FREQ_SECS )
        sys.stdout.write( process.stdout.read() )
        sys.stderr.write( process.stderr.read() )
    else : process.wait()                         
""")                                                     

        cleanUp = (
"""            
    removeIfwLogs()
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

        runInstallerProcess = (
"""
    shArgs = [ "sudo", "xvfb-run", "./%s" % (EXE_NAME,) ] + ARGS
    #print( list2cmdline( shArgs ) )
    process = Popen( shArgs, cwd=WORK_DIR,
                     shell=False, universal_newlines=True,
                     stdout=PIPE, stderr=PIPE )
                     
    if IS_VERBOSE :
        POLL_FREQ_SECS = 0.1        
        while process.poll() is None:
            sys.stdout.write( process.stdout.read() )
            sys.stderr.write( process.stderr.read() )
            time.sleep( POLL_FREQ_SECS )
        sys.stdout.write( process.stdout.read() )
        sys.stderr.write( process.stderr.read() )
    else : process.wait()                                              
""")

        cleanUp = (
"""
    for cmd in CLEANUP_CMDS:
        if IS_VERBOSE: print( ' '.join( cmd ) ) 
        subprocess.check_call( cmd )         
    removeIfwLogs()
""")       

    if isQtIfwInstaller or isQtIfwUnInstaller :
        return (
"""
import os, sys, time, argparse, subprocess
from subprocess import Popen, PIPE, list2cmdline
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
    retCode=None
{7}
    return process.returncode if retCode is None else retCode   

def cleanUp():
{8}

def removeIfwLogs(): pass

sys.exit( main() )
""").format( 
      exeName                               #{0} 
    , util._normEscapePath(wrkDir)          #{1}
    , util._normEscapePath(scriptPath)      #{2}
    , imports                               #{3}
    , IS_WINDOWS                            #{4}
    , helpers                               #{5}
    , preProcess                            #{6}
    , runInstallerProcess                   #{7}
    , cleanUp                               #{8}
    , ( (', "target=%s"' % (util._normEscapePath(targetDir),))  #{9} 
        if isQtIfwInstaller else "" )
)
    else:
        return (
"""
import os, sys, shlex, time, argparse, subprocess
from subprocess import Popen, PIPE, list2cmdline
{17}

SUCCESS=0
FAILURE=1

VERSION_INFO = "{26}"

IS_WINDOWS = {10}
IS_FROZEN = True

WORK_DIR = sys._MEIPASS
EXE_NAME = "{0}"
EXE_PATH = os.path.join( WORK_DIR, EXE_NAME )

IFW_OUT_LOG_NAME     = "installer.out"
IFW_OUT_LOG_PATH     = os.path.join( WORK_DIR, IFW_OUT_LOG_NAME )
IS_IFW_OUT_LOG_PURGE = True
IFW_ERR_LOG_NAME     = "installer.err"
IFW_ERR_LOG_PATH     = os.path.join( WORK_DIR, IFW_ERR_LOG_NAME )
IS_IFW_ERR_LOG_PURGE = True

VERBOSE_SWITCH = "{4}"
REDIRECT_PATH = os.getenv( "{34}" )
IS_RUN_SWITCH  = {22}
IS_REBOOT_SWITCH = {28}
IS_STARTMENU_SWITCH = {32}

components = {14}
componentsRequired = {27}
componentsEpilogue = ( 
'''{15}'''
)
componentsPrefix = "{16}"

licenses = {23}

ARGS = []
IS_VERBOSE = False

{18}

class CustomArgumentParser( argparse.ArgumentParser ):
    if IS_WINDOWS:
        # override
        def parse_args( self ):
            def rawCommandLine():
                from ctypes.wintypes import LPWSTR
                from ctypes import windll
                Kernel32 = windll.Kernel32
                GetCommandLineW = Kernel32.GetCommandLineW
                GetCommandLineW.argtypes = ()
                GetCommandLineW.restype  = LPWSTR
                return GetCommandLineW()                
            WINDOWS_PATH_DELIMITER = '\\\\'
            NIX_PATH_DELIMITER = '/'                
            commandLine = rawCommandLine().replace( 
                WINDOWS_PATH_DELIMITER, NIX_PATH_DELIMITER )
            skipArgCount = 1 if IS_FROZEN else 2
            args = shlex.split( commandLine )[skipArgCount:]        
            return argparse.ArgumentParser.parse_args( self, args )

def main():        
    global ARGS, IS_VERBOSE    
    ARGS = wrapperArgs() 
    try:
        if ARGS.version: return showVersion()
        if ARGS.license: return showLicenses()        
    except: pass    
    ARGS = toIwfArgs( wrapperArgs() )  
    IS_VERBOSE = VERBOSE_SWITCH in ARGS
    removeIfwLogs() 
    {19}
    exitCode = runInstaller()
    cleanUp()        
    print( "Success!" if exitCode==SUCCESS else "Failure!" )    
    return exitCode

def wrapperArgs():
    parser = CustomArgumentParser( epilog=componentsEpilogue,
        formatter_class=argparse.RawTextHelpFormatter )

    parser.add_argument( '-v', '--version', default=False,
                         help='show version information and exit',
                         action='store_true' )

    if len(licenses) > 0 : 
        parser.add_argument( '-l', '--license', default=False,
                             help='show license agreement(s) and exit', 
                             action='store_true' )                                        

    parser.add_argument( '-y', '--dryrun', default=False,
                         help='perform a dry run (to detect error conditions)',
                         action='store_true' )                        
    parser.add_argument( '-u', '--uninstall', default=False, 
                         help='uninstall existing installation', 
                         action='store_true' )                         
    parser.add_argument( '-f', '--force', default=False, 
                         help='force installation (replace existing installation)', 
                         action='store_true' )                         

    parser.add_argument( '-t', '--target', default=None,
                         help='target directory' )                         
    
    if IS_WINDOWS and IS_STARTMENU_SWITCH:                          
        parser.add_argument( '-m', '--startmenu', default=None,  
                             help='start menu directory' )
                             
    if len(components) > 0 :                             
        parser.add_argument( '-c', '--components', nargs='*', default=[],
                             help='component ids to install (space delimited list)' )
        parser.add_argument( '-i', '--include', nargs='*', default=[],
                             help='component ids to include (space delimited list)' )
        parser.add_argument( '-x', '--exclude', nargs='*', default=[],
                             help='component ids to exclude (space delimited list)' )  
                         
    if IS_RUN_SWITCH is None:                     
        parser.add_argument( '-r', '--run', default=False, 
                             help='run the program post installation', 
                             action='store_true' )

    if IS_REBOOT_SWITCH is not None:                     
        parser.add_argument( '-b', '--reboot', default=False, 
                             help='allow post installation reboot (if required)', 
                             action='store_true' )

    parser.add_argument( '-o', '--outfile', default=None,
                         help='output messages file path' )               
    parser.add_argument( '-e', '--errfile', default=None,
                         help='error messages file path' )               

    parser.add_argument( '-p', '--passthru', default=None,
                         help='QtIFW arguments (k/v ex: "a=\\'1\\' b=\\'2\\'")' )

    parser.add_argument( '-a', '--unpassthru', default=None,
                         help='uninstall arguments (k/v ex: "a=\\'1\\' b=\\'2\\'")' )
                                                  
    parser.add_argument( '-d', '--debug', default=False,
                         help='show debugging information', 
                         action='store_true' )
                                                        
    return parser.parse_args()

def toIwfArgs( wrapperArgs ):
    global IFW_OUT_LOG_PATH, IS_IFW_OUT_LOG_PURGE 
    global IFW_ERR_LOG_PATH, IS_IFW_ERR_LOG_PURGE                          

    # Note: if allowing these paths to be overridden, ensure they are passed to
    # QtIWF as absolutes, relative to the client's current working directory         
    if wrapperArgs.outfile:
        IFW_OUT_LOG_PATH = os.path.realpath( wrapperArgs.outfile )
        IS_IFW_OUT_LOG_PURGE = False             
    if wrapperArgs.errfile:               
        IFW_ERR_LOG_PATH = os.path.realpath( wrapperArgs.errfile )
        IS_IFW_ERR_LOG_PURGE = False                         
                         
    # silent install always uses:
    #     auto pilot mode
    #     client defined out/err log paths    
    args = ['{1}', 
            '{2}="%s"' % (IFW_ERR_LOG_PATH.replace("\\\\","/"),), 
            '{30}="%s"' % (IFW_OUT_LOG_PATH.replace("\\\\","/"),) ]
    
    if wrapperArgs.debug: args.append( VERBOSE_SWITCH )        
    
    if wrapperArgs.dryrun: args.append( "{31}" )
    
    if wrapperArgs.uninstall: args.append( "{24}={25}" )        
    else: args.append( "{5}={6}" if wrapperArgs.force else "{5}={7}" )

    if wrapperArgs.target is not None :
        args.append( '{8}="%s"' % (wrapperArgs.target.replace("\\\\","/"),) )
            
    if IS_WINDOWS and IS_STARTMENU_SWITCH and wrapperArgs.startmenu is not None: 
        args.append( '{9}="%s"' % (wrapperArgs.startmenu.replace("\\\\","/"),) )
    
    if len(components) > 0 : 
        def appendComponentArg( wrapperArg, ifwArg, isExclude=False ):                
            if len(wrapperArg) > 0:
                comps = ["%s%s" % (componentsPrefix,c) for c in wrapperArg]
                for id in comps:
                    if id not in components: 
                        sys.stderr.write( "Invalid component id: %s" % (id,) )
                        sys.exit( FAILURE )
                    if isExclude and id in componentsRequired:
                        sys.stderr.write( "Cannot exclude component id: %s" % (id,) )
                        sys.exit( FAILURE )    
                if not isExclude: wrapperArg += componentsRequired                            
                args.append( "%s=%s" % (ifwArg, ",".join(comps)) )
        appendComponentArg( wrapperArgs.components, "{11}" )
        appendComponentArg( wrapperArgs.include,    "{12}" )
        appendComponentArg( wrapperArgs.exclude,    "{13}" )

    args.append( "{3}=%s" % str( wrapperArgs.run 
            if IS_RUN_SWITCH is None else IS_RUN_SWITCH ).lower() )
    if IS_REBOOT_SWITCH is not None:         
        args.append( "{29}=%s" % str( wrapperArgs.reboot ).lower() )

    if wrapperArgs.passthru: 
        args.append( wrapperArgs.passthru.replace("\\\\","/").replace("'",'"') )

    if wrapperArgs.unpassthru:
        unpassthru = wrapperArgs.unpassthru.replace("\\\\","/")
        delimited = ""
        inQuotes=False
        for c in unpassthru:            
            if c==" ":
                if not inQuotes: 
                    delimited += ","
                    continue
            elif c=="'": inQuotes = not inQuotes            
            delimited += c                           
        unpassthru = delimited.replace("'","`").replace("=","#")            
        args.append( '{33}="%s"' % (unpassthru,) )
        
    return args

def runInstaller():
    retCode=None
{20}
    
    # Display (non-error) messages left by the installer
    if os.path.exists( IFW_OUT_LOG_PATH ):
        with open( IFW_OUT_LOG_PATH ) as f:
            sys.stdout.write( f.read() )

    # use error log existence to set an exit code, 
    # since IFW doesn't support such   
    if os.path.exists( IFW_ERR_LOG_PATH ):
        with open( IFW_ERR_LOG_PATH ) as f:
            sys.stderr.write( f.read() )
        return FAILURE        
    return process.returncode if retCode is None else retCode 

def cleanUp():
{21}

def removeIfwLogs(): 
    if IS_IFW_OUT_LOG_PURGE and os.path.exists( IFW_OUT_LOG_PATH ):
        os.remove( IFW_OUT_LOG_PATH )
    if IS_IFW_ERR_LOG_PURGE and os.path.exists( IFW_ERR_LOG_PATH ):
        os.remove( IFW_ERR_LOG_PATH )

def showVersion():        
    print( VERSION_INFO )
    return SUCCESS

def showLicenses():        
    for compId in licenses:
        compLics = licenses[ compId ]
        for name in compLics:            
            if len(licenses) > 1: 
                print( "Component id: %s" % (id,) )
                print( name )
            print( "\\n%s\\n" % ( compLics[ name ],) )
    return SUCCESS

sys.exit( main() )
""").format( 
       exeName                                              # {0}
    , ("%s=true" % (_QtIfwScript.AUTO_PILOT_CMD_ARG,))      # {1}
    , _QtIfwScript.ERR_LOG_PATH_CMD_ARG                     # {2}
    , _QtIfwScript.RUN_PROGRAM_CMD_ARG                      # {3}
    , _QtIfwScript.VERBOSE_CMD_SWITCH_ARG                   # {4}
    , _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG                # {5}
    , _QtIfwScript.TARGET_EXISTS_OPT_REMOVE                 # {6}
    , _QtIfwScript.TARGET_EXISTS_OPT_FAIL                   # {7}
    , _QtIfwScript.TARGET_DIR_CMD_ARG                       # {8}
    , _QtIfwScript.START_MENU_DIR_CMD_ARG                   # {9}
    , IS_WINDOWS                                            # {10}
    , _QtIfwScript.INSTALL_LIST_CMD_ARG                     # {11}
    , _QtIfwScript.INCLUDE_LIST_CMD_ARG                     # {12}
    , _QtIfwScript.EXCLUDE_LIST_CMD_ARG                     # {13}
    , componentsRepr                                        # {14}
    , componentsEpilogue                                    # {15}
    , componentsPrefix                                      # {16}
    , imports                                               # {17}
    , helpers                                               # {18}
    , preProcess                                            # {19}
    , runInstallerProcess                                   # {20}
    , cleanUp                                               # {21}
    , str(isRunSwitch)                                      # {22}
    , licensesRepr                                          # {23}
    , _QtIfwScript.MAINTAIN_MODE_CMD_ARG                    # {24}
    , _QtIfwScript.MAINTAIN_MODE_OPT_REMOVE_ALL             # {25}
    , versionInfo                                           # {26}
    , componentsReqRepr                                     # {27}
    , str(isRebootSwitch)                                   # {28}
    , _QtIfwScript.REBOOT_CMD_ARG                           # {29}
    , _QtIfwScript.OUT_LOG_PATH_CMD_ARG                     # {30}
    , ("%s=true" % (_QtIfwScript.DRYRUN_CMD_ARG,))          # {31}
    , str(isStartMenu)                                      # {32}
    , _QtIfwScript.MAINTAIN_PASSTHRU_CMD_ARG                # {33}
    , util._REDIRECT_PATH_ENV_VAR_NAME                      # {34}
)

def __generateQtIfwInstallPyScript( installerPath, ifwScriptPath, 
                                    targetPath=None,
                                    isInstaller=True ):
    installerDir, installerName = splitPath( installerPath ) 
    script = __silentQtIfwScript( 
        installerName, 
        isQtIfwInstaller=isInstaller, isQtIfwUnInstaller=(not isInstaller), 
        scriptPath=ifwScriptPath, wrkDir=installerDir,
        targetDir=targetPath, isRunSwitch=False )    
    filePath = joinPath( tempDirPath(), 
        __QT_IFW_AUTO_INSTALL_PY_SCRIPT_NAME if isInstaller else
        __QT_IFW_AUTO_UNINSTALL_PY_SCRIPT_NAME )
    #print( "Generating Python Script: %s" % (filePath,) )
    #print( "\n%s\n" % (script,) )
    with open( filePath, 'w' ) as f: f.write( script ) 
    return filePath 
        
"""
THIS IS INJECTED INTO THE QT IFW TOOL INSTALLATION ITSELF.
I.E. IT IS NOT FOR THE PRODUCTS OF DISTBUILDER 
"""            
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
        