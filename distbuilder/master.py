from distbuilder.util import *  # @UnusedWildImport

from distbuilder.py_installer import \
      PyInstallerConfig \
    , WindowsExeVersionInfo

from distbuilder.opy_library import \
    OpyConfigExt as OpyConfig
    
from distbuilder.qt_installer import \
      QtIfwConfig \
    , QtIfwConfigXml \
    , QtIfwPackageXml \
    , QtIfwPackageScript \
    , DEFAULT_SETUP_NAME \
    , DEFAULT_QT_IFW_SCRIPT_NAME
    
"""    
from distbuilder.pip_installer import \
    PipConfig 

from distbuilder.opy_library import \
      OpyConfigExt as OpyConfig \
    , OpyPatch \
    , LibToBundle 
"""    
    
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
    
    def qtIfwConfig( self ):
        return QtIfwConfig( pkgSrcDirPath=self.__pkgSrcDirPath(), 
                            pkgName=self.__ifwPkgName(),
                            installerDefDirPath=self.ifwDefDirPath,
                            configXml=self.qtIfwConfigXml(), 
                            pkgXml=self.qtIfwPackageXml(), 
                            pkgScript=self.qtIfwPackageScript(),
                            setupExeName=self.setupName )

    def qtIfwConfigXml( self ) :
        return QtIfwConfigXml( self.productName, self.binaryName, 
                               self.__versionStr(), self.companyLegalName, 
                               self.companyTradeName, self.iconFilePath ) 
    
    def qtIfwPackageXml( self ) :
        return QtIfwPackageXml( self.__ifwPkgName(), self.productName, self.description, 
                                self.__versionStr(), self.ifwScriptName )
    
    def qtIfwPackageScript( self ) :
        return QtIfwPackageScript( self.__ifwPkgName(), 
                                   fileName=self.ifwScriptName, 
                                   exeName=self.binaryName, 
                                   script=self.ifwScriptPath, 
                                   srcPath=self.ifwScriptPath )
            
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
                        