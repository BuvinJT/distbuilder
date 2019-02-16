import sys
import six
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from datetime import datetime 
from time import time as curTime

from distbuilder.util import *  # @UnusedWildImport

from distbuilder.py_installer import \
      buildExecutable \
    , makePyInstSpec \
    , PyInstallerConfig \
    , PyInstSpec \
    , WindowsExeVersionInfo

from distbuilder.opy_library import \
      obfuscatePy \
    , OpyConfigExt as OpyConfig
    
from distbuilder.qt_installer import \
      buildInstaller \
    , QtIfwConfig \
    , QtIfwConfigXml \
    , QtIfwPackage \
    , QtIfwPackageXml \
    , QtIfwPackageScript \
    , DEFAULT_SETUP_NAME \
    , DEFAULT_QT_IFW_SCRIPT_NAME \
    , QT_IFW_VERBOSE_SWITCH

# -----------------------------------------------------------------------------       
class ConfigFactory:
    
    @classmethod
    def copy( cls, instance ): return cls( deepcopy( instance ) )

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
        self.specFilePath = None
        self.version      = (0,0,0,0)
        
        self.setupName     = DEFAULT_SETUP_NAME
        self.ifwDefDirPath = None        
        self.ifwPackages   = None

        self.ifwPkgName       = None
        self.ifwPkgNamePrefix = "com"
        self.pkgSrcDirPath    = None
        
        self.ifwScriptName = DEFAULT_QT_IFW_SCRIPT_NAME
        self.ifwScript     = None
        self.ifwScriptPath = None
                            
    def pyInstallerConfig( self ): 
        cfg = PyInstallerConfig()
        cfg.name         = self.binaryName
        cfg.entryPointPy = self.entryPointPy 
        cfg.isGui        = self.isGui
        cfg.iconFilePath = self.iconFilePath 
        if self.specFilePath :
            cfg.pyInstSpec = PyInstSpec( self.specFilePath )
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
    
    def qtIfwConfig( self, packages=None ):
        if packages is not None: self.ifwPackages = packages
        return QtIfwConfig( installerDefDirPath=self.ifwDefDirPath,
                            packages=self.ifwPackages,
                            configXml=self.qtIfwConfigXml(), 
                            setupExeName=self.setupName ) 

    def qtIfwConfigXml( self ) :
        return QtIfwConfigXml( self.productName, self.binaryName, 
                               self.__versionStr(), self.companyLegalName, 
                               iconFilePath=self.iconFilePath, 
                               isGui=self.isGui,                               
                               companyTradeName=self.companyTradeName ) 

    def qtIfwPackage( self, pyInstConfig=None, isTempSrc=False ):
        if pyInstConfig is not None: self.pyInstConfig = pyInstConfig
        return QtIfwPackage( name=self.__ifwPkgName(), 
                        srcDirPath=self.__pkgSrcDirPath(),                  
                        isTempSrc = isTempSrc,
                        pkgXml=self.qtIfwPackageXml(), 
                        pkgScript=self.qtIfwPackageScript( self.pyInstConfig ) )
    
    def qtIfwPackageXml( self ) :
        return QtIfwPackageXml( self.__ifwPkgName(), 
                                self.productName, self.description, 
                                self.__versionStr(), self.ifwScriptName )
    
    def qtIfwPackageScript( self, pyInstConfig=None ) :
        if pyInstConfig is not None: self.pyInstConfig = pyInstConfig
        script = QtIfwPackageScript( self.__ifwPkgName(), 
                                     fileName=self.ifwScriptName, 
                                     exeName=self.binaryName,    
                                     isGui=self.isGui,                                  
                                     script=self.ifwScript, 
                                     scriptPath=self.ifwScriptPath )
        if IS_LINUX:
            script.exeVersion = self.__versionStr()
            if self.pyInstConfig is not None:
                script.pngIconResPath = self.pyInstConfig._pngIconResPath             
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
@six.add_metaclass(ABCMeta)
class _DistBuildProcessBase:

    DIVIDER = "------------------------------------"

    def __init__( self, configFactory,
                  name="Distribution Builder Process" ) :
        self.configFactory = configFactory                              
        self.name          = name        
        self.__startTime   = None
        self.__endTime     = None
        self.__duration    = None
    
    def run( self ):        
        self.__startTime = curTime()
        self.__printHeader()        
        self._body()    
        self.__endTime   = curTime()
        self.__durationSecs  = self.__endTime - self.__startTime 
        self.__printFooter()
    
    def __printHeader( self ):
        try: 
            from distbuilder import __version__ as ver
            libPath = modulePackagePath( "distbuilder" )
        except: 
            ver = "?"
            libPath = "?"        
        print( _DistBuildProcessBase.DIVIDER )    
        print( "STARTING: %s" % (self.name,) )
        print( "Date/Time: %s" % (str(datetime.now()),) )        
        print( "Distrbution Builder Version: %s" % (ver,) )
        print( "Library Path:\n    %s" % (libPath,) )
        print( "Python Translator:\n    %s" % (sys.version,) )
        print( "System Info:\n    %s %s" % (platform.system(), platform.release()) )
        print( _DistBuildProcessBase.DIVIDER )
        print( "" )
    
    def __printFooter( self ):
        print( "" )        
        print( _DistBuildProcessBase.DIVIDER )
        print( "COMPLETED: %s" % (self.name,) )
        print( "Date/Time: %s" % (str(datetime.now()),) )
        print( "Total Seconds: %f" % (self.__durationSecs,) )
        print( _DistBuildProcessBase.DIVIDER )
        
    @abstractmethod
    def _body( self ): """PURE VIRTUAL"""           
   
# -----------------------------------------------------------------------------
class PyToBinPackageProcess( _DistBuildProcessBase ):

    def __init__( self, configFactory,                  
                  name="Python to Binary Package Process", 
                  isObfuscating=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )        
        self.isObfuscating = isObfuscating
                        
        self.isPyInstDupDataPatched = None
        self.isTestingObfuscation   = False
        self.isTestingExe           = False
        self.exeTestArgs            = []        
        self.isElevatedTest         = False
        
        self._pyInstConfig = None
        
    def _body( self ):        
        
        if self.isObfuscating :
            opyConfig = self.configFactory.opyConfig() 
            self. onOpyConfig( opyConfig )
            if self.isTestingObfuscation:
                _, obPath = obfuscatePy( opyConfig )
                runPy( obPath )
                sys.exit()
        else: opyConfig = None
        
        self._pyInstConfig = self.configFactory.pyInstallerConfig()        
        self.onPyInstConfig( self._pyInstConfig )                
        
        if self._pyInstConfig.pyInstSpec is None:
            self._pyInstConfig.isSpecFileRemoved = True
            makePyInstSpec( self._pyInstConfig, opyConfig=opyConfig )
            if self.isPyInstDupDataPatched is None: 
                self.isPyInstDupDataPatched = True  
        spec = self._pyInstConfig.pyInstSpec                
        if self.isPyInstDupDataPatched and self._pyInstConfig.isOneFile:        
            spec.injectDuplicateDataPatch()
            spec.write()            
        self.onMakeSpec( spec )
        spec.debug()
            
        _, binPath = buildExecutable( pyInstConfig=self._pyInstConfig, 
                                      opyConfig=opyConfig )
        if self.isTestingExe : 
            run( binPath, self.exeTestArgs,
                 isElevated=self.isElevatedTest, isDebug=True )
                    
    # Use these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onMakeSpec( self, spec ):    """VIRTUAL"""
                        
# -----------------------------------------------------------------------------                        
class BuildInstallerProcess( _DistBuildProcessBase ):

    def __init__( self, configFactory,
                  name="Build Installer Process",  
                  ifwPackages=[],
                  buildPackageProcesses=[],                                                                                  
                  isDesktopTarget=False,
                  isHomeDirTarget=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )
        self.ifwPackages           = ifwPackages
        self.buildPackageProcesses = buildPackageProcesses        
        self.isDesktopTarget       = isDesktopTarget
        self.isHomeDirTarget       = isHomeDirTarget
        
        self.isElevatedTest         = False       
        self.isTestingInstall       = False
        self.isVerboseInstall       = False
        
    def _body( self ):        

        for p in self.buildPackageProcesses :
            p.run()            
            self.ifwPackages.append( 
                self.configFactory.qtIfwPackage( p._pyInstConfig, 
                                                 isTempSrc=True )
            )
            
        ifwConfig = self.configFactory.qtIfwConfig( packages=self.ifwPackages )
        self.onQtIfwConfig( ifwConfig )                
        setupPath = buildInstaller( ifwConfig )
        
        if self.isDesktopTarget :
            setupPath = moveToDesktop( setupPath )
        elif self.isHomeDirTarget :
            setupPath = moveToHomeDir( setupPath )    
        if self.isTestingInstall : 
            run( setupPath, 
                 (QT_IFW_VERBOSE_SWITCH 
                 if self.isVerboseInstall else None),
                 isElevated=self.isElevatedTest )
            
    # Use these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onQtIfwConfig( self, cfg ):  """VIRTUAL"""                
                                                
# -----------------------------------------------------------------------------                        
class SimplePyToBinInstallerProcess( BuildInstallerProcess ):
    
    def __init__( self, configFactory,                  
                  name="Python to Binary Installer Process",
                  isObfuscating=False,
                  isDesktopTarget=False,
                  isHomeDirTarget=False ) :
        
        class CallbackPyToBinPackageProcess( PyToBinPackageProcess ):
            def __init__( self, parent, configFactory, isObfuscating ):
                PyToBinPackageProcess.__init__( self, configFactory, 
                                                isObfuscating=isObfuscating )
                self.__parent = parent
            def onOpyConfig( self, cfg ):    self.__parent.onOpyConfig( cfg )                    
            def onPyInstConfig( self, cfg ): self.__parent.onPyInstConfig( cfg )
            def onMakeSpec( self, spec ):    self.__parent.onMakeSpec( spec )       
                
        binPrcs = CallbackPyToBinPackageProcess( self, configFactory, 
                                                 isObfuscating=isObfuscating )    
        BuildInstallerProcess.__init__( self, 
            configFactory, name,
            buildPackageProcesses=[ binPrcs ],                                         
            isDesktopTarget=isDesktopTarget, isHomeDirTarget=isHomeDirTarget )

    # Use these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onMakeSpec( self, spec ):    """VIRTUAL"""   
    def onQtIfwConfig( self, cfg ):  """VIRTUAL"""                                                                
                                                