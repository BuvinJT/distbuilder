from distbuilder.util import *  # @UnusedWildImport

from distbuilder.py_installer import \
      PyInstallerConfig \
    , WindowsExeVersionInfo

from distbuilder.opy_library import \
    OpyConfigExt as OpyConfig
    
"""    
from distbuilder.qt_installer import \
      QtIfwConfig \
    , QtIfwConfigXml \
    , QtIfwPackageXml \
    , QtIfwPackageScript \

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
        
        self.binaryName   = None  
        self.isGui        = False           
        self.entryPointPy = None
        self.iconFilePath = None       
        self.version      = (0,0,0,0)
                  
        self.setupName    = None
        self.ifwPkgName   = None

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
    
    def opyConfig( self, bundleLibs=None, sourceDir=None, patches=None ):
        return OpyConfig( self.binaryName, self.entryPointPy,
                          bundleLibs, sourceDir, patches )                 
    
    def __versionStr( self ):
        return "%d.%d.%d.%d" % self.version
                