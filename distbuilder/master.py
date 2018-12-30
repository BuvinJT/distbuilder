from distbuilder.util import *  # @UnusedWildImport

from distbuilder.py_installer import \
      PyInstallerConfig \
    , WindowsExeVersionInfo
from wx.build import cfg_version
    
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
        
        self.verMajor     = 0
        self.verMinor     = 0
        self.verMicro     = 0
        self.verBuild     = 0 
                  
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
            cfg.versionInfo.major = self.verMajor
            cfg.versionInfo.minor = self.verMinor
            cfg.versionInfo.micro = self.verMicro
            cfg.versionInfo.build = self.verBuild
            cfg.versionInfo.companyName = self.companyLegalName
            cfg.versionInfo.productName = self.productName
            cfg.versionInfo.description = self.description
            cfg.versionInfo.exeName     = self.binaryName
        return cfg
    
    def __versionStr( self ):
        return "%d.%d.%d.%d" % (
            self.verMajor, self.verMinor, self.verMicro, self.verBuild )
                