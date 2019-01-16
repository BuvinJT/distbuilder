import sys

from distbuilder.util import *  # @UnusedWildImport

from distbuilder.py_installer import \
      buildExecutable \
    , PyInstallerConfig \
    , WindowsExeVersionInfo

from distbuilder.opy_library import \
      obfuscatePy \
    , OpyConfigExt as OpyConfig
    
from distbuilder.qt_installer import \
      buildInstaller \
    , QtIfwConfig \
    , QtIfwConfigXml \
    , QtIfwPackageXml \
    , QtIfwPackageScript \
    , DEFAULT_SETUP_NAME \
    , DEFAULT_QT_IFW_SCRIPT_NAME \
    , QT_IFW_VERBOSE_SWITCH

# -----------------------------------------------------------------------------       
class ConfigFactory:
    
    def __init__( self ) :        
        self.productName = None
        self.description = None
        
        self.companyTradeName = None
        self.companyLegalName = None      
                
        self.opyBundleLibs = None
        self.opyPatches    = None
        
        self.binaryName   = None  
        self.isGui        = False           
        self.entryPointPy = None
        self.iconFilePath = None       
        self.version      = (0,0,0,0)

        self.setupName     = DEFAULT_SETUP_NAME
        self.ifwDefDirPath = None
        self.pkgSrcDirPath = None

        self.ifwPkgName       = None
        self.ifwPkgNamePrefix = "com"
        
        self.ifwScriptName = DEFAULT_QT_IFW_SCRIPT_NAME
        self.ifwScript     = None
        self.ifwScriptPath = None
                            
    def pyInstallerConfig( self ): 
        cfg = PyInstallerConfig()
        cfg.name         = self.binaryName
        cfg.entryPointPy = self.entryPointPy 
        cfg.isGui        = self.isGui
        cfg.iconFilePath = self.iconFilePath 
        if IS_WINDOWS :
            cfg.versionInfo = WindowsExeVersionInfo()
            ( verMajor, verMinor, verMicro, verBuild ) = self.version
            cfg.versionInfo.major = verMajor
            cfg.versionInfo.minor = verMinor
            cfg.versionInfo.micro = verMicro
            cfg.versionInfo.build = verBuild
            cfg.versionInfo.companyName = self.companyLegalName
            cfg.versionInfo.productName = self.productName
            cfg.versionInfo.description = self.description
            cfg.versionInfo.exeName     = self.binaryName
        return cfg
    
    def opyConfig( self ):
        return OpyConfig( self.binaryName, self.entryPointPy,
                          bundleLibs=self.opyBundleLibs,
                          patches=self.opyPatches )                 
    
    def qtIfwConfig( self, pyInstConfig=None ):
        return QtIfwConfig( pkgSrcDirPath=self.__pkgSrcDirPath(), 
                            pkgName=self.__ifwPkgName(),
                            installerDefDirPath=self.ifwDefDirPath,
                            configXml=self.qtIfwConfigXml(), 
                            pkgXml=self.qtIfwPackageXml(), 
                            pkgScript=self.qtIfwPackageScript( pyInstConfig ),
                            setupExeName=self.setupName )

    def qtIfwConfigXml( self ) :
        return QtIfwConfigXml( self.productName, self.binaryName, 
                               self.__versionStr(), self.companyLegalName, 
                               self.companyTradeName, self.iconFilePath ) 
    
    def qtIfwPackageXml( self ) :
        return QtIfwPackageXml( self.__ifwPkgName(), self.productName, self.description, 
                                self.__versionStr(), self.ifwScriptName )
    
    def qtIfwPackageScript( self, pyInstConfig=None ) :
        script = QtIfwPackageScript( self.__ifwPkgName(), 
                                     fileName=self.ifwScriptName, 
                                     exeName=self.binaryName,                                      
                                     script=self.ifwScriptPath, 
                                     srcPath=self.ifwScriptPath )
        if IS_LINUX:
            script.exeVersion = self.__versionStr()
            if pyInstConfig is not None:
                script.pngIconResPath = pyInstConfig._pngIconResPath             
        return script
            
    def __versionStr( self ):
        return "%d.%d.%d.%d" % self.version

    def __ifwPkgName( self ):
        if self.ifwPkgName : return self.ifwPkgName
        comp = self.companyTradeName.replace(" ", "").replace(".", "").lower()
        prod = self.productName.replace(" ", "").replace(".", "").lower()
        return "%s.%s.%s" % (self.ifwPkgNamePrefix, comp, prod)

    def __pkgSrcDirPath( self ):
        if self.pkgSrcDirPath : return self.pkgSrcDirPath
        return joinPath( THIS_DIR, self.binaryName )                 
   
# -----------------------------------------------------------------------------
class PyToBinInstallerProcess:

    def __init__( self, configFactory,
                  name="Python To Binary Installer Process", 
                  isObfuscating=False, 
                  isDesktopTarget=False ) :
        self.name              = name
        self.configFactory     = configFactory                      
        self.isObfuscating     = isObfuscating
        self.isDesktopTarget  = isDesktopTarget
        self.isTestingObfuscation  = False
        self.isTestingExe          = False
        self.exeTestArgs           = []
        self.isTestingInstall      = False
        self.isVerboseInstall      = False
        self.isElevatedTest        = False

    def __printHeader( self ):
        try: 
            from distbuilder import __version__ as ver
            libPath = modulePackagePath( "distbuilder" )
        except: 
            ver = "?"
            libPath = "?"
        DIVIDER = "------------------------------------"
        print( DIVIDER )    
        print( ">>> Distrbution Builder Process <<<" )
        print( "" )
        print( "Process Name: %s" % (self.name,) )
        print( "" )
        print( "Library Version: %s" % (ver,) )
        print( "Library Path:\n%s" % (libPath,) )
        print( "" )
        print( "Python Translator:\n%s" % (sys.version,) )
        print( "" )
        print( "System Info:\n%s\n%s" % (platform.system(), platform.release()) )
        print( DIVIDER )
        print( "" )
        
    def run( self ):        
        self.__printHeader()
        
        if self.isObfuscating :
            opyConfig = self.configFactory.opyConfig() 
            self. onOpyConfig( opyConfig )
            if self.isTestingObfuscation:
                _, obPath = obfuscatePy( opyConfig )
                runPy( obPath )
                sys.exit()
        else: opyConfig = None
        
        pyInstConfig = self.configFactory.pyInstallerConfig()
        self.onPyInstConfig( pyInstConfig )        
        _, binPath = buildExecutable( pyInstConfig=pyInstConfig, 
                                           opyConfig=opyConfig )
        if self.isTestingExe : 
            run( binPath, self.exeTestArgs,
                 isElevated=self.isElevatedTest, isDebug=True )
        
        ifwConfig = self.configFactory.qtIfwConfig( pyInstConfig )
        self.onQtIfwConfig( ifwConfig )
        setupPath = buildInstaller( ifwConfig, isPkgSrcRemoved=True )
        if self.isDesktopTarget :
            setupPath = moveToDesktop( setupPath )
        if self.isTestingInstall : 
            run( setupPath, 
                 (QT_IFW_VERBOSE_SWITCH 
                 if self.isVerboseInstall else None),
                 isElevated=self.isElevatedTest )
            
        self.__printFooter()

    def __printFooter( self ):        
        #TODO: add time elapsed...      
        print( "Done!" )

    # Use these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onQtIfwConfig( self, cfg ):  """VIRTUAL"""                
                        