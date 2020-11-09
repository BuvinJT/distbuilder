import sys
import six
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from datetime import datetime 
from time import time as curTime

from distbuilder import util    # @UnusedImport
from distbuilder.util import *  # @UnusedWildImport

from distbuilder.py_installer import \
      buildExecutable \
    , makePyInstSpec \
    , PyInstallerConfig \
    , PyInstSpec 

from distbuilder.opy_library import \
      obfuscatePy \
    , OpyConfigExt as OpyConfig
    
from distbuilder.qt_installer import \
      _stageInstallerPackages \
    , _buildInstaller \
    , _addQtIfwLicense \
    , _addQtIfwEmbeddedResources \
    , _addQtIfwUiElements \
    , joinPathQtIfw \
    , QtIfwConfig \
    , QtIfwConfigXml \
    , QtIfwControlScript \
    , QtIfwPackage \
    , QtIfwPackageXml \
    , QtIfwPackageScript \
    , QtIfwShortcut \
    , QtIfwExeWrapper \
    , QtIfwExternalOp \
    , _QtIfwScript \
    , DEFAULT_SETUP_NAME \
    , DEFAULT_QT_IFW_SCRIPT_NAME \
    , QT_IFW_VERBOSE_SWITCH \
    , QT_IFW_SILENT_DEBUG_SWITCH \
    , _DEBUG_SCRIPTS_ARGS \
    , QT_IFW_TARGET_DIR \
    , _SILENT_FORCED_ARGS \
    , _LOUD_FORCED_ARGS 
    
# -----------------------------------------------------------------------------       
class ConfigFactory:
    
    @staticmethod
    def copy( instance ): return deepcopy( instance )

    def __init__( self, cfgId=None ) :
        self.cfgId = cfgId
        
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
        
        self.isSilentSetup = False
        self.licensePath   = None
        self.setupName     = DEFAULT_SETUP_NAME
        self.ifwDefDirPath = None        
        self.ifwPackages   = None

        self.startOnBoot   = False
        self.replaceTarget = False # TODO: Fix this, or drop it!
        
        self.ifwUiPages     = None
        self.ifwWidgets     = None
                    
        self.ifwCntrlScript     = None # None=Default False=Exclude                
        self.ifwCntrlScriptText = None
        self.ifwCntrlScriptPath = None
        self.ifwCntrlScriptName = DEFAULT_QT_IFW_SCRIPT_NAME

        # These are used for direct package generation via the factory,
        # to then be added to a process.  Most typically, this is for non
        # Python packages.
        self.ifwPkgId         = None
        self.ifwPkgName       = None
        self.ifwPkgNamePrefix = "com"        

        self.ifwPkgIsDefault  = True
        self.ifwPkgIsRequired = False 
        self.ifwPkgIsHidden   = False
                                     
        self.ifwPkgScript     = None           
        self.ifwPkgScriptText = None
        self.ifwPkgScriptPath = None        
        self.ifwPkgScriptName = DEFAULT_QT_IFW_SCRIPT_NAME
        
        self.pkgType         = None
        self.pkgSubDirName   = None
        self.pkgSrcDirPath   = None
        self.pkgSrcExePath   = None
        self.pkgExeWrapper   = None 
               
        self.qtCppConfig = None
       
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
        if IS_WINDOWS: cfg.versionInfo = self .exeVersionInfo()
        return cfg

    if IS_WINDOWS :
        def exeVersionInfo( self ):
            verInfo = WindowsExeVersionInfo()
            ( verInfo.major,
              verInfo.minor,
              verInfo.micro,
              verInfo.build
            ) = self.__versionTuple()
            verInfo.companyName = self.companyLegalName
            verInfo.productName = self.productName
            verInfo.description = self.description
            verInfo.exeName     = self.binaryName
            return verInfo 
    
    def opyConfig( self ):
        return OpyConfig( self.binaryName, self.entryPointPy,
                          sourceDir=self.sourceDir,
                          bundleLibs=self.opyBundleLibs,
                          patches=self.opyPatches )                 
    
    def qtIfwConfig( self, packages=None ):
        if packages is not None: self.ifwPackages = packages        
        
        cfg = QtIfwConfig( installerDefDirPath=self.ifwDefDirPath,
                            packages=self.ifwPackages,
                            configXml=self.qtIfwConfigXml(), 
                            controlScript=self.qtIfwControlScript(),
                            setupExeName=self.setupName ) 
        _addQtIfwLicense( self.licensePath, self.ifwPackages, cfg )
        _addQtIfwEmbeddedResources( cfg, self.ifwPackages )        
        _addQtIfwUiElements( cfg, self.ifwUiPages )
        _addQtIfwUiElements( cfg, self.ifwWidgets )
        return cfg 

    def qtIfwConfigXml( self ) :
        xml = QtIfwConfigXml( self.productName,  
                              self.__versionStr(), self.companyLegalName, 
                              iconFilePath=self.iconFilePath, 
                              primaryContentExe=self.binaryName,
                              isPrimaryExeGui=self.isGui,
                              primaryExeWrapper=self.pkgExeWrapper,                               
                              companyTradeName=self.companyTradeName )
        if xml.RunProgram is None and self.ifwPackages is not None:
            xml.setPrimaryContentExe( self.ifwPackages[0] )
        return xml

    def qtIfwControlScript( self ) :
        if self.ifwCntrlScript : return self.ifwCntrlScript 
        if( self.ifwCntrlScript == False and
            self.ifwCntrlScriptText is None and 
            self.ifwCntrlScriptPath is None ):
            return None     
        script = QtIfwControlScript(
                fileName=self.ifwCntrlScriptName,
                script=self.ifwCntrlScriptText, 
                scriptPath=self.ifwCntrlScriptPath )
        
        # TODO: Fix this, as it is no longer respected!
        if self.replaceTarget:
            script.virtualArgs={ _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG:
                                 _QtIfwScript.TARGET_EXISTS_OPT_REMOVE } 
        return script
    
    def qtIfwPackage( self, pyInstConfig=None, isTempSrc=False ):
        self.__pkgPyInstConfig = pyInstConfig
        pkgType=self.__ifwPkgType()

        if IS_WINDOWS and self.startOnBoot in [True, CURRENT_USER, ALL_USERS]:
            if self.pkgExeWrapper and not self.pkgExeWrapper.isExe:
                self.pkgExeWrapper.isExe = True
                self.pkgExeWrapper.refresh()
            else: self.pkgExeWrapper = self.qtIfwExeWrapper( isExe=True )        
                
        pkg = QtIfwPackage(
                pkgId=self.__ifwPkgId(),
                pkgType=pkgType, 
                name=self.__ifwPkgName(), 
                subDirName=self.pkgSubDirName,
                srcDirPath=self.__pkgSrcDirPath(),
                srcExePath=self.pkgSrcExePath,            
                resBasePath=self.sourceDir,      
                isTempSrc = isTempSrc,
                pkgXml=self.qtIfwPackageXml(), 
                pkgScript=self.qtIfwPackageScript( self.__pkgPyInstConfig ) )
        
        pkg.exeName    = self.__pkgExeName()
        pkg.isGui      = self.isGui
        
        pkg.exeWrapper = self.pkgExeWrapper        
        if( IS_WINDOWS and 
            isinstance( pkg.exeWrapper, QtIfwExeWrapper ) and 
            pkg.exeWrapper.isExe ):
            w = pkg.exeWrapper
            pkg.pkgScript.externalOps += [
                QtIfwExternalOp.WrapperScript2Exe(
                    scriptPath = joinPath( w.exeDir, 
                        w.wrapperScript.fileName() ), 
                    exePath = joinPath( w.exeDir, normBinaryName( w.exeName ) ),
                    targetPath = joinPath( w.exeDir, normBinaryName( w.wrapperExeName ) ), 
                    iconName=normIconName( w.wrapperIconName ) ) ]       
            if self.startOnBoot in [True, CURRENT_USER, ALL_USERS]:
                pkg.pkgScript.externalOps += [
                    QtIfwExternalOp.CreateStartupEntry( pkg, 
                        isAllUsers=self.startOnBoot==ALL_USERS ) ]
         
        # Add additional distribution resources 
        # (note PyInst process adds these resource itself)
        if pkgType != QtIfwPackage.Type.PY_INSTALLER:            
            # Add the external icon resource as needed for Linux 
            if IS_LINUX and self.iconFilePath :  
                pngPath = normIconName( self.iconFilePath, isPathPreserved=True )
                if isFile( pngPath ):
                    if pkg.distResources is None: pkg.distResources=[] 
                    pkg.distResources.append( pngPath )
            # Merge the factory resources into the existing list for the package 
            pkg.distResources = list( set().union(
                pkg.distResources if pkg.distResources else [], 
                self.distResources if self.distResources else [] ) )
                                                
        pkg.qtCppConfig = self.qtCppConfig
        return pkg

    def qtIfwPackageXml( self ) :
        return QtIfwPackageXml( self.__ifwPkgName(), 
                self.productName, self.description, self.__versionStr(), 
                scriptName=self.ifwPkgScriptName,
                isDefault=self.ifwPkgIsDefault, 
                isRequired=self.ifwPkgIsRequired,
                isHidden=self.ifwPkgIsHidden )
    
    def qtIfwPackageScript( self, pyInstConfig=None ) :
        if self.ifwPkgScript : return self.ifwPkgScript
        self.__pkgPyInstConfig = pyInstConfig

        # Build the shortcut object 
        # (shortcuts are script generated on the target, not bundled resources) 
        shortcutCmd = ( self.pkgExeWrapper._shortcutCmd
                        if self.pkgExeWrapper else None )
        shortcutArgs = ( self.pkgExeWrapper._shortcutArgs
                         if self.pkgExeWrapper else [] )
        shortcutWinStyle = ( self.pkgExeWrapper._shortcutWinStyle
                             if self.pkgExeWrapper else None )                        
        shortcutExeDir = ( 
            joinPathQtIfw( QT_IFW_TARGET_DIR, self.pkgSubDirName )
            if self.pkgSubDirName else QT_IFW_TARGET_DIR )
                
        if IS_LINUX:
            # TODO: fix this to handle relative source paths
            #       and nested destination paths
            #       (use util._toSrcDestPair)
            # Currently just cheating by assuming png icon is going on app dir root...  
            if self.__pkgPyInstConfig:
                cfg=self.__pkgPyInstConfig                 
                pngIconPath = cfg._pngIconResPath
            #    relSrcDir = dirPath( 
            #        cfg.sourceDir if cfg.sourceDir else THIS_DIR )                
            elif self.iconFilePath:    
                pngIconPath = self.iconFilePath
                #pngIconPath = normIconName( self.iconFilePath, 
                #                            isPathPreserved=True )
                #relSrcDir = dirPath( self.iconFilePath )
            #if pngIconPath:
            #    srcDir, srcFile = splitPath( pngIconPath )
            #    if srcDir=="" or not isParentDir( relSrcDir, srcDir ):
            #        pngIconPath = joinPath( 
            #            relpath( srcDir, relSrcDir ), srcFile )            
            pngIconPath = normIconName( self.iconFilePath, 
                                        isPathPreserved=False )                   
        else : pngIconPath = None                         
        
        defShortcut = QtIfwShortcut(                    
                        productName=self.productName,
                        command=shortcutCmd,
                        args=shortcutArgs,
                        exeDir=shortcutExeDir,
                        exeName=self.__pkgExeName(),                            
                        exeVersion=self.__versionStr(),
                        isGui=self.isGui,                                  
                        pngIconResPath=pngIconPath )  
        defShortcut.windowStyle = shortcutWinStyle
        
        bundledScripts=[]
        if self.pkgExeWrapper and self.pkgExeWrapper.wrapperScript:
            bundledScripts.append( self.pkgExeWrapper.wrapperScript )
                    
        script = QtIfwPackageScript( 
                    self.__ifwPkgName(), self.__versionStr(),
                    pkgSubDirName=self.pkgSubDirName,
                    shortcuts=[ defShortcut ],
                    bundledScripts=bundledScripts,
                    fileName=self.ifwPkgScriptName,
                    script=self.ifwPkgScriptText, 
                    scriptPath=self.ifwPkgScriptPath )
        
        if IS_LINUX and self.pkgExeWrapper:
            script.isAskPassProgRequired = self.pkgExeWrapper.isElevated
            
        return script

    def qtIfwExeWrapper( self, wrapperScript=None,
                         workingDir=None, isElevated=False, 
                         envVars=None, args=None, 
                         isExe=False ) : # Windows only option!
        return QtIfwExeWrapper( self.__pkgExeName(), isGui=self.isGui, 
                wrapperScript=wrapperScript,
                exeDir=( joinPathQtIfw( QT_IFW_TARGET_DIR, self.pkgSubDirName )
                         if self.pkgSubDirName else QT_IFW_TARGET_DIR ),                 
                workingDir=workingDir, isElevated=isElevated, 
                envVars=envVars, args=args, isExe=isExe )        

    def __versionTuple( self ): return versionTuple( self.version )
                    
    def __versionStr( self ): return versionStr( self.version )
        
    def __ifwPkgId( self ):
        if self.ifwPkgId : return self.ifwPkgId
        if self.cfgId : return self.cfgId
        prod = ( self.__pkgPyInstConfig.name if self.__pkgPyInstConfig 
                 else self.productName )        
        prod = prod.replace(" ", "").replace(".", "").lower()            
        return prod

    def __ifwPkgType( self ):
        if self.pkgType : return self.pkgType
        if self.__pkgPyInstConfig : return QtIfwPackage.Type.PY_INSTALLER
        if self.pkgSrcExePath is None:
            return ( QtIfwPackage.Type.DATA if self.binaryName is None else
                     QtIfwPackage.Type.PY_INSTALLER )
        return None
    
    def __ifwPkgName( self ):
        if self.ifwPkgName : return self.ifwPkgName
        comp = ( self.companyTradeName if self.companyTradeName
                 else self.companyLegalName )
        comp = comp.replace(" ", "").replace(".", "").lower()
        prod = ( self.__pkgPyInstConfig.name if self.__pkgPyInstConfig 
                 else self.productName )        
        prod = prod.replace(" ", "").replace(".", "").lower()            
        return "%s.%s.%s" % (self.ifwPkgNamePrefix, comp, prod)

    def __pkgSrcDirPath( self ):
        if self.__pkgPyInstConfig : return absPath( self.__pkgPyInstConfig.name )
        if self.pkgSrcDirPath : return self.pkgSrcDirPath
        if( self.__ifwPkgType()==QtIfwPackage.Type.PY_INSTALLER and 
            self.binaryName ): 
            return absPath( self.binaryName )               
        return None                 

    def __pkgExeName( self ):
        if self.binaryName : return self.binaryName
        if self.pkgSrcExePath: 
            return normBinaryName( self.pkgSrcExePath, isGui=self.isGui )  
        return None
        
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
        self.onInitialize()
        self._body()
        self.onFinalize()
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
   
    def onInitialize( self ): """VIRTUAL"""
    def onFinalize( self ):   """VIRTUAL"""

# -----------------------------------------------------------------------------
class PyToBinPackageProcess( _DistBuildProcessBase ):

    def __init__( self, configFactory,                  
                  name="Python to Binary Package Process",
                  isZipped=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )        
        self.isZipped = isZipped
        
        self.isWarningSuppression   = True
        self.isUnBufferedStdIo      = False                
        self.isPyInstDupDataPatched = None
        self.isObfuscationTest      = False
        self.isExeTest              = False
        self.isElevatedTest         = False
        self.exeTestArgs            = []        
        
        self._pyInstConfig = None
        
        # Results
        self.binDir = None
        self.binPath = None
        
    def _body( self ):        
        
        if self.configFactory.isObfuscating :
            opyConfig = self.configFactory.opyConfig() 
            self.onOpyConfig( opyConfig )
            if self.isObfuscationTest:
                _, obPath = obfuscatePy( opyConfig )
                runPy( obPath, self.exeTestArgs, self.isElevatedTest )
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
            spec.isUnBufferedStdIo = self.isUnBufferedStdIo        
            if self.isWarningSuppression:
                spec.warningBehavior = PyInstSpec.WARN_IGNORE                  
        spec = self._pyInstConfig.pyInstSpec            
        if self.isWarningSuppression or self.isUnBufferedStdIo:                
            spec.injectInterpreterOptions()
        if self.isPyInstDupDataPatched and self._pyInstConfig.isOneFile:                    
            spec.injectDuplicateDataPatch()
        if spec.isInjected: spec.write()            
        self.onMakeSpec( spec )
        spec.debug()
            
        self.binDir, self.binPath = (
            buildExecutable( pyInstConfig=self._pyInstConfig, 
                             opyConfig=opyConfig ) )
        if self.isExeTest : 
            run( self.binPath, self.exeTestArgs,
                 isElevated=self.isElevatedTest, isDebug=True )
        
        if self.isZipped :
            toZipFile( self.binDir, zipDest=None, removeScr=True )
                    
    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onInitialize( self ):        """VIRTUAL"""    
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onMakeSpec( self, spec ):    """VIRTUAL"""
    def onFinalize( self ):          """VIRTUAL"""
                            
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
        
        self.isInstallTest            = False        
        self.isAutoInstallTest        = False
        self.isVerboseInstallTest     = True
        self.isScriptDebugInstallTest = False
        
        # Results
        self.setupPath = None
        
    def _body( self ):        

        for p in self.pyToBinPkgProcesses :
            p.run()
            self.ifwPackages.append(                
                p.configFactory.qtIfwPackage( p._pyInstConfig, 
                                              isTempSrc=True )
            )
        self.onPyPackagesBuilt( self.ifwPackages )
            
        ifwConfig = self.configFactory.qtIfwConfig( packages=self.ifwPackages )
        self.onQtIfwConfig( ifwConfig )     
        
        _stageInstallerPackages( ifwConfig, self.configFactory.isSilentSetup )
        self.onPackagesStaged( ifwConfig, ifwConfig.packages )
                   
        self.setupPath = _buildInstaller( 
            ifwConfig, self.configFactory.isSilentSetup )
        
        if self.isDesktopTarget :
            self.setupPath = moveToDesktop( self.setupPath )
        elif self.isHomeDirTarget :
            self.setupPath = moveToHomeDir( self.setupPath )    
        if self.isInstallTest or self.isAutoInstallTest:            
            if self.isVerboseInstallTest:
                verboseArgs = ( [QT_IFW_SILENT_DEBUG_SWITCH] 
                                if self.configFactory.isSilentSetup else
                                [QT_IFW_VERBOSE_SWITCH] )  
            else: verboseArgs = []                             
            debugArgs = _DEBUG_SCRIPTS_ARGS if self.isScriptDebugInstallTest else [] 
            autoArgs = ( 
                ( _SILENT_FORCED_ARGS if self.configFactory.isSilentSetup else
                  _LOUD_FORCED_ARGS ) 
                if self.isAutoInstallTest else [] )
            run( self.setupPath, verboseArgs + debugArgs + autoArgs,
                 isDebug=True, isElevated=self.isAutoInstallTest )
        
    # Override these to further customize the build process once the 
    # ConfigFactory has produced the initial config object
    def onInitialize( self ):                """VIRTUAL"""
    def onPyPackagesBuilt( self, pkgs ):     """VIRTUAL"""
    def onQtIfwConfig( self, cfg ):          """VIRTUAL"""
    def onPackagesStaged( self, cfg, pkgs ): """VIRTUAL"""     
    def onFinalize( self ):                  """VIRTUAL"""
    
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
                                   
        prc = CallbackPyToBinPackageProcess( self, configFactory )
        self.onPyPackageProcess( prc )
            
        _BuildInstallerProcess.__init__( self, 
            configFactory, name,
            pyToBinPkgProcesses=[ prc ],                                         
            isDesktopTarget=isDesktopTarget, 
            isHomeDirTarget=isHomeDirTarget )

    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onInitialize( self ):             """VIRTUAL"""    
    def onPyPackageProcess( self, prc ):  """VIRTUAL"""
    def onOpyConfig( self, cfg ):         """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ):      """VIRTUAL"""
    def onMakeSpec( self, spec ):         """VIRTUAL"""
    def onQtIfwConfig( self, cfg ):       """VIRTUAL"""                                                                
    def onFinalize( self ):               """VIRTUAL"""
                                                                                                
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
            def onInitialize( self ):
                self.__parent.onPyPackageInitialize( self.__key )           
            def onOpyConfig( self, cfg ):    
                self.__parent.onOpyConfig( self.__key, cfg )                    
            def onPyInstConfig( self, cfg ): 
                self.__parent.onPyInstConfig( self.__key, cfg )
            def onMakeSpec( self, spec ):    
                self.__parent.onMakeSpec( self.__key, spec )       
            def onFinalize( self ):          
                self.__parent.onPyPackageFinalize( self.__key )           
    
        binPrcs = []
        for key, factory in six.iteritems( pyPkgConfigFactoryDict ) :        
            if factory is None :
                factory = ConfigFactory.copy( masterConfigFactory )
                factory.cfgId = key
                self.onConfigFactory( key, factory )
            prc = CallbackPyToBinPackageProcess( self, key, factory )
            self.onPyPackageProcess( key, prc )    
            binPrcs.append( prc )        
        
        _BuildInstallerProcess.__init__( self, 
            masterConfigFactory, name,
            ifwPackages=ifwPackages,
            pyToBinPkgProcesses=binPrcs,                                         
            isDesktopTarget=isDesktopTarget, 
            isHomeDirTarget=isHomeDirTarget )

    # Override these to further customize the build process  
    def onInitialize( self ):                     """VIRTUAL"""        
    def onConfigFactory( self, key, factory ):    """VIRTUAL"""
    def onPyPackageProcess( self, key, prc ):     """VIRTUAL"""
    def onPyPackageInitialize( self, key ):       """VIRTUAL"""
    def onOpyConfig( self, key, cfg ):            """VIRTUAL"""                    
    def onPyInstConfig( self, key, cfg ):         """VIRTUAL"""
    def onMakeSpec( self, key, spec ):            """VIRTUAL"""
    def onPyPackageFinalize( self, key ):         """VIRTUAL"""           
    def onPyPackagesBuilt( self, pkgs ):          """VIRTUAL"""
    def onQtIfwConfig( self, cfg ):               """VIRTUAL"""     
    def onPackagesStaged( self, cfg, pkgs ):      """VIRTUAL"""                                                     
    def onFinalize( self ):                       """VIRTUAL"""
