import sys
import six
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from datetime import datetime 
from time import time as curTime

from distbuilder import util
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
    
    @staticmethod
    def copy( instance ): return deepcopy( instance )

    def __init__( self ) :        
        self.productName = None
        self.description = None
        
        self.companyTradeName = None
        self.companyLegalName = None      

        self.isObfuscating = False                
        self.opyBundleLibs = None
        self.opyPatches    = None
        
        self.binaryName    = None  
        self.version       = (0,0,0,0)
        self.isGui         = False
        
        self.sourceDir     = None      
        self.entryPointPy  = None
        self.iconFilePath  = None       
        self.distResources = []
        self.specFilePath  = None
        
        self.setupName     = DEFAULT_SETUP_NAME
        self.ifwDefDirPath = None        
        self.ifwPackages   = None

        self.ifwPkgName       = None
        self.ifwPkgNamePrefix = "com"
        self.pkgSrcDirPath    = None
        
        self.ifwScriptName = DEFAULT_QT_IFW_SCRIPT_NAME
        self.ifwScript     = None
        self.ifwScriptPath = None
        
        self.__pkgPyInstConfig = None
                            
    def pyInstallerConfig( self ): 
        cfg = PyInstallerConfig()        
        cfg.name          = self.binaryName
        cfg.sourceDir     = self.sourceDir
        cfg.entryPointPy  = self.entryPointPy 
        cfg.isGui         = self.isGui
        cfg.iconFilePath  = self.iconFilePath
        cfg.distResources = self.distResources 
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
                          sourceDir = self.sourceDir,
                          bundleLibs=self.opyBundleLibs,
                          patches=self.opyPatches )                 
    
    def qtIfwConfig( self, packages=None ):
        if packages is not None: self.ifwPackages = packages
        return QtIfwConfig( installerDefDirPath=self.ifwDefDirPath,
                            packages=self.ifwPackages,
                            configXml=self.qtIfwConfigXml(), 
                            setupExeName=self.setupName ) 

    def qtIfwConfigXml( self ) :
        xml = QtIfwConfigXml( self.productName, self.binaryName, 
                              self.__versionStr(), self.companyLegalName, 
                              iconFilePath=self.iconFilePath, 
                              isGui=self.isGui,                               
                              companyTradeName=self.companyTradeName )
        if xml.RunProgram is None and self.ifwPackages is not None:
            firstPkg = self.ifwPackages[0]
            xml.RunProgramDescription = firstPkg.pkgXml.DisplayName
            xml.exeName = util.normBinaryName( firstPkg.exeName, 
                                               isGui=firstPkg.isGui )            
            xml.setDefaultPaths()
        return xml

    def qtIfwPackage( self, pyInstConfig=None, isTempSrc=False ):
        self.__pkgPyInstConfig = pyInstConfig
        pkg = QtIfwPackage( name=self.__ifwPkgName(), 
                srcDirPath=self.__pkgSrcDirPath(),                  
                isTempSrc = isTempSrc,
                pkgXml=self.qtIfwPackageXml(), 
                pkgScript=self.qtIfwPackageScript( self.__pkgPyInstConfig ) )
        pkg.exeName = self.binaryName
        pkg.isGui = self.isGui
        return pkg

    def qtIfwPackageXml( self ) :
        return QtIfwPackageXml( self.__ifwPkgName(), 
                self.productName, self.description, 
                self.__versionStr(), self.ifwScriptName )
    
    def qtIfwPackageScript( self, pyInstConfig=None ) :
        self.__pkgPyInstConfig = pyInstConfig
        script = QtIfwPackageScript( self.__ifwPkgName(), 
                    fileName=self.ifwScriptName,
                    productName=self.productName,
                    exeName=self.binaryName,    
                    isGui=self.isGui,                                  
                    script=self.ifwScript, 
                    scriptPath=self.ifwScriptPath )
        if IS_LINUX:
            script.exeVersion = self.__versionStr()
            if self.__pkgPyInstConfig is not None:
                script.pngIconResPath = self.__pkgPyInstConfig._pngIconResPath             
        return script
            
    def __versionStr( self ):
        return "%d.%d.%d.%d" % self.version

    def __ifwPkgName( self ):
        if self.ifwPkgName : return self.ifwPkgName
        comp = ( self.companyTradeName if self.companyTradeName
                 else self.companyLegalName )
        prod = ( self.__pkgPyInstConfig.name if self.__pkgPyInstConfig 
                 else self.productName )        
        comp = comp.replace(" ", "").replace(".", "").lower()
        prod = prod.replace(" ", "").replace(".", "").lower()            
        return "%s.%s.%s" % (self.ifwPkgNamePrefix, comp, prod)

    def __pkgSrcDirPath( self ):
        if self.__pkgPyInstConfig :
            return joinPath( THIS_DIR, self.__pkgPyInstConfig.name )
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
                  isZipped=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )        
        self.isZipped = isZipped
                        
        self.isPyInstDupDataPatched = None
        self.isTestingObfuscation   = False
        self.isTestingExe           = False
        self.exeTestArgs            = []        
        self.isElevatedTest         = False
        
        self._pyInstConfig = None
        
    def _body( self ):        
        
        if self.configFactory.isObfuscating :
            opyConfig = self.configFactory.opyConfig() 
            self.onOpyConfig( opyConfig )
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
            
        binDir, binPath = buildExecutable( pyInstConfig=self._pyInstConfig, 
                                           opyConfig=opyConfig )
        if self.isTestingExe : 
            run( binPath, self.exeTestArgs,
                 isElevated=self.isElevatedTest, isDebug=True )
        
        if self.isZipped :
            toZipFile( binDir, zipDest=None, removeScr=True )
                    
    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onMakeSpec( self, spec ):    """VIRTUAL"""
                        
# -----------------------------------------------------------------------------                        
class _BuildInstallerProcess( _DistBuildProcessBase ):

    def __init__( self, configFactory,
                  name="Build Installer Process",  
                  pyToBinPkgProcesses=[], ifwPackages=[],                                                                                   
                  isDesktopTarget=False, isHomeDirTarget=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )
        self.pyToBinPkgProcesses = pyToBinPkgProcesses        
        self.ifwPackages         = ifwPackages
        self.isDesktopTarget     = isDesktopTarget
        self.isHomeDirTarget     = isHomeDirTarget
        
        self.isElevatedTest         = False       
        self.isTestingInstall       = False
        self.isVerboseInstall       = False
        
    def _body( self ):        

        for p in self.pyToBinPkgProcesses :
            p.run()
            self.ifwPackages.append(                
                p.configFactory.qtIfwPackage( p._pyInstConfig, 
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
            
    # Override this to further customize the build process once the 
    # ConfigFactory has produced the initial config object
    def onQtIfwConfig( self, cfg ):  """VIRTUAL"""                

# -----------------------------------------------------------------------------                        
class PyToBinInstallerProcess( _BuildInstallerProcess ):
    
    def __init__( self, configFactory,                  
                  name="Python to Binary Installer Process",
                  isDesktopTarget=False, isHomeDirTarget=False ) :
        
        class CallbackPyToBinPackageProcess( PyToBinPackageProcess ):
            def __init__( self, parent, configFactory ):
                PyToBinPackageProcess.__init__( self, configFactory )
                self.__parent = parent
            def onOpyConfig( self, cfg ):    self.__parent.onOpyConfig( cfg )                    
            def onPyInstConfig( self, cfg ): self.__parent.onPyInstConfig( cfg )
            def onMakeSpec( self, spec ):    self.__parent.onMakeSpec( spec )       
                
        binPrcs = CallbackPyToBinPackageProcess( self, configFactory )    
        _BuildInstallerProcess.__init__( self, 
            configFactory, name,
            pyToBinPkgProcesses=[ binPrcs ],                                         
            isDesktopTarget=isDesktopTarget, 
            isHomeDirTarget=isHomeDirTarget )

    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onMakeSpec( self, spec ):    """VIRTUAL"""   
    def onQtIfwConfig( self, cfg ):  """VIRTUAL"""                                                                
                                                                                                
# -----------------------------------------------------------------------------                        
class RobustInstallerProcess( _BuildInstallerProcess ):
    
    def __init__( self, masterConfigFactory, 
                  name="Multi-Package Python to Binary Installer Process",
                  pyPkgConfigFactoryDict={}, ifwPackages=[],                                     
                  isDesktopTarget=False, isHomeDirTarget=False ) :
        
        class CallbackPyToBinPackageProcess( PyToBinPackageProcess ):
            def __init__( self, parent, key, configFactory ):
                PyToBinPackageProcess.__init__( self, configFactory )
                self.__parent = parent
                self.__key    = key
            def onOpyConfig( self, cfg ):    
                self.__parent.onOpyConfig( self.__key, cfg )                    
            def onPyInstConfig( self, cfg ): 
                self.__parent.onPyInstConfig( self.__key, cfg )
            def onMakeSpec( self, spec ):    
                self.__parent.onMakeSpec( self.__key, spec )       

        binPrcs = []
        for key, factory in six.iteritems( pyPkgConfigFactoryDict ) :        
            if factory is None :
                factory = ConfigFactory.copy( masterConfigFactory )
                self.onConfigFactory( key, factory )
            prcs = CallbackPyToBinPackageProcess( self, key, factory )
            self.onPyPackageProcess( key, prcs )    
            binPrcs.append( prcs )
        
        _BuildInstallerProcess.__init__( self, 
            masterConfigFactory, name,
            ifwPackages=ifwPackages,
            pyToBinPkgProcesses=binPrcs,                                         
            isDesktopTarget=isDesktopTarget, 
            isHomeDirTarget=isHomeDirTarget )

    # Override these to further customize the build process  
    def onConfigFactory( self, key, factory ):    """VIRTUAL"""
    def onPyPackageProcess( self, key, binPrcs ): """VIRTUAL"""
    def onOpyConfig( self, key, cfg ):            """VIRTUAL"""                    
    def onPyInstConfig( self, key, cfg ):         """VIRTUAL"""
    def onMakeSpec( self, key, spec ):            """VIRTUAL"""   
    def onQtIfwConfig( self, cfg ):               """VIRTUAL"""                                                                
                                                