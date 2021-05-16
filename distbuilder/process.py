from distbuilder import util    # @UnusedImport
from distbuilder.util import * # @UnusedWildImport

from distbuilder.py_installer import (
      pyScriptToExe 
    , makePyInstSpec 
    , PyInstallerConfig 
    , PyInstSpec 
)

from distbuilder.iexpress import (
      IExpressConfig 
    , _scriptToExe 
)

from distbuilder.opy_library import (
      obfuscatePy 
    , OpyConfigExt as OpyConfig
)    
    
from distbuilder.qt_installer import(
      _stageInstallerPackages 
    , _buildInstaller 
    , joinPathQtIfw 
    , QtIfwConfig 
    , QtIfwConfigXml 
    , QtIfwControlScript 
    , QtIfwPackage 
    , QtIfwPackageXml 
    , QtIfwPackageScript 
    , QtIfwShortcut 
    , QtIfwExeWrapper 
    , QtIfwExternalOp 
    , _QtIfwScript 
    , DEFAULT_SETUP_NAME 
    , DEFAULT_QT_IFW_SCRIPT_NAME 
    , QT_IFW_VERBOSE_SWITCH 
    , QT_IFW_SILENT_DEBUG_SWITCH 
    , _DEBUG_SCRIPTS_ARGS 
    , QT_IFW_TARGET_DIR 
    , _SILENT_FORCED_ARGS 
    , _LOUD_FORCED_ARGS 
)
   
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

        self.version       = (0,0,0,0)
        self.isGui         = False

        self.binaryName    = None          
        self.sourceDir     = None              
        self.iconFilePath  = None
        
        # PyInstaller
        self.entryPointPy  = None               
        self.specFilePath  = None
        self.isOneFile     = True # this differs from the PyInstaller default

        # Other Script to Binary sources 
        self.entryPointScript = None
       
        # Basic resource bundling
        self.distResources = []

        # Python Obfuscation
        self.isObfuscating = False                
        self.opyBundleLibs = None
        self.opyPatches    = None
        
        # For Installers: applied via "master" factories        
        self.isSilentSetup = False
        self.setupName     = DEFAULT_SETUP_NAME
        
        self.ifwDefDirPath = None        
        self.ifwPackages   = None
         
        self.isLimitedMaintenance = True
        self.replaceTarget = False # TODO: Fix this, or drop it!

        self.ifwWizardStyle    = None
        self.ifwLogoFilePath   = None
        self.ifwBannerFilePath = None
                
        self.licensePath = None        
        self.ifwUiPages  = None
        self.ifwWidgets  = None                    
        
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
        
        self.pkgType            = None
        self.pkgSubDirName      = None
        self.pkgSrcDirPath      = None
        self.pkgSrcExePath      = None
        self.pkgExeWrapper      = None 
        self.pkgCodeSignTargets = None

        self.startOnBoot   = False
       
        # code signing
        self.codeSignConfig = None

        # Configurations for specific package types               
        self.__pkgPyInstConfig = None
        self.__pkgIExpressConfig = None
        self.qtCppConfig = None
                            
    def pyInstallerConfig( self ): 
        cfg = PyInstallerConfig()        
        cfg.name          = self.binaryName
        cfg.sourceDir     = self.sourceDir
        cfg.entryPointPy  = self.entryPointPy
        cfg.isOneFile     = self.isOneFile 
        cfg.isGui         = self.isGui
        cfg.iconFilePath  = self.iconFilePath        
        cfg.distResources = self.distResources 
        cfg.codeSignConfig   = self.codeSignConfig
        cfg.codeSignTargets  = self.pkgCodeSignTargets         
        if self.specFilePath :
            cfg.pyInstSpec = PyInstSpec( self.specFilePath )
        if IS_WINDOWS: cfg.versionInfo = self .exeVersionInfo()
        return cfg

    if IS_WINDOWS :

        def iExpressConfig( self ):        
            cfg = IExpressConfig()            
            cfg.name             = self.binaryName
            cfg.sourceDir        = self.sourceDir
            cfg.entryPointScript = self.entryPointScript
            cfg.versionInfo      = self.exeVersionInfo()
            cfg.iconFilePath     = self.iconFilePath
            cfg.distResources    = self.distResources
            cfg.codeSignConfig   = self.codeSignConfig
            cfg.codeSignTargets  = self.pkgCodeSignTargets 
            return cfg
        
        def exeVersionInfo( self, ifwConfig=None ):
            verInfo = WindowsExeVersionInfo()
            if ifwConfig:
                xml = ifwConfig.configXml
                verInfo.description = xml._titleDisplayed()        
                ( verInfo.major,
                  verInfo.minor,
                  verInfo.micro,
                  verInfo.build
                ) = versionTuple( xml.Version )
                verInfo.productName = xml.Name
                verInfo.companyName = xml.Publisher                
                verInfo.exeName     = ifwConfig.setupExeName                                            
            else:
                verInfo.description = self.description
                ( verInfo.major,
                  verInfo.minor,
                  verInfo.micro,
                  verInfo.build
                ) = self.__versionTuple()
                verInfo.productName = self.productName
                verInfo.companyName = self.companyLegalName                                
                verInfo.exeName     = self.binaryName
            return verInfo 
    
    def opyConfig( self ):
        return OpyConfig( self.binaryName, self.entryPointPy,
                          sourceDir=self.sourceDir,
                          bundleLibs=self.opyBundleLibs,
                          patches=self.opyPatches )                 
    
    def qtIfwConfig( self, packages=None ):
        if packages is not None: self.ifwPackages = packages
        configXml     = self.qtIfwConfigXml()  
        controlScript = self.qtIfwControlScript( configXml )              
        cfg = QtIfwConfig( installerDefDirPath=self.ifwDefDirPath,
                           packages=self.ifwPackages,
                           configXml=configXml, 
                           controlScript=controlScript,
                           setupExeName=self.setupName ) 
        cfg.addLicense( self.licensePath )
        cfg.addUiElements( self.ifwUiPages )
        cfg.addUiElements( self.ifwWidgets )
        cfg._scrubEmbeddedResources()        
        self.ifwPackages = cfg.packages
        return cfg 

    def qtIfwConfigXml( self ) :
        xml = QtIfwConfigXml( self.productName,  
                              self.__versionStr(), self.companyLegalName,                              
                              iconFilePath=self.iconFilePath, 
                              primaryContentExe=self.binaryName,
                              isPrimaryExeGui=self.isGui,
                              primaryExeWrapper=self.pkgExeWrapper,                               
                              companyTradeName=self.companyTradeName,
                              wizardStyle=self.ifwWizardStyle,
                              logoFilePath=self.ifwLogoFilePath,
                              bannerFilePath=self.ifwBannerFilePath
                            )
        if xml.RunProgram is None and self.ifwPackages is not None:
            xml.setPrimaryContentExe( self.ifwPackages[0] )
        return xml

    def qtIfwControlScript( self, configXml ) :
        if self.ifwCntrlScript : return self.ifwCntrlScript 
        if( self.ifwCntrlScript == False and
            self.ifwCntrlScriptText is None and 
            self.ifwCntrlScriptPath is None ):
            return None     
        script = QtIfwControlScript(
                fileName=self.ifwCntrlScriptName,
                script=self.ifwCntrlScriptText, 
                scriptPath=self.ifwCntrlScriptPath )
        
        script._wizardStyle = configXml.WizardStyle
        script.isLimitedMaintenance = self.isLimitedMaintenance 
                
        # TODO: Fix this, as it is no longer respected!
        if self.replaceTarget:
            script.virtualArgs={ _QtIfwScript.TARGET_EXISTS_OPT_CMD_ARG:
                                 _QtIfwScript.TARGET_EXISTS_OPT_REMOVE } 
        return script
    
    def qtIfwPackage( self, pyInstConfig=None, iExpressConfig=None, isTempSrc=False ):
        self.__pkgPyInstConfig = pyInstConfig        
        self.__pkgIExpressConfig = iExpressConfig
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
        if( IS_WINDOWS and # On the fly, installer generated exe is only currently supported on Windows! 
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
            if pkg.pkgType == QtIfwPackage.Type.DATA:
                pkg.distResources = util._expandSrcDestPairs( 
                    pkg.distResources, destDir=None, 
                    basePath=pkg.resBasePath ) 

        if self.codeSignConfig:
            # These package types already signed the primary exe
            if( pkgType != QtIfwPackage.Type.PY_INSTALLER and          
                pkgType != QtIfwPackage.Type.IEXPRESS ):
                try: self.pkgCodeSignTargets.append( pkg.exeName )
                except: self.pkgCodeSignTargets=[ pkg.exeName ]
            # EXE wrappers can't be signed (a design limitation)    
            if( isinstance( pkg.exeWrapper, QtIfwExeWrapper ) and 
                pkg.exeWrapper.isExe ):
                exeName = pkg.exeWrapper.wrapperExeName
                printErr( "WARNING: %s will be generated at install time and "
                          "therefore cannot be code signed (as your private "
                          "key would be be required in the distribution)!" % 
                          (exeName,), 
                          isFatal=False)
            pkg.codeSignTargets = self.pkgCodeSignTargets
                                                       
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
        prod =( self.__pkgPyInstConfig.name if self.__pkgPyInstConfig 
                else self.__pkgIExpressConfig.name if self.__pkgIExpressConfig
                else self.productName )        
        prod = prod.replace(" ", "").replace(".", "").lower()            
        return prod

    def __ifwPkgType( self ):
        if self.pkgType is not None: return self.pkgType
        if self.__pkgPyInstConfig : return QtIfwPackage.Type.PY_INSTALLER
        if self.__pkgIExpressConfig: return QtIfwPackage.Type.IEXPRESS
        if self.pkgSrcExePath is None:
            return ( QtIfwPackage.Type.DATA if self.binaryName is None else
                     QtIfwPackage.Type.PY_INSTALLER )
        return None
    
    def __ifwPkgName( self ):
        if self.ifwPkgName : return self.ifwPkgName
        comp = ( self.companyTradeName if self.companyTradeName
                 else self.companyLegalName )
        comp = comp.replace(" ", "").replace(".", "").lower()
        prod =( self.__pkgPyInstConfig.name if self.__pkgPyInstConfig 
                else self.__pkgIExpressConfig.name if self.__pkgIExpressConfig
                else self.productName )        
        prod = prod.replace(" ", "").replace(".", "").lower()            
        return "%s.%s.%s" % (self.ifwPkgNamePrefix, comp, prod)

    def __pkgSrcDirPath( self ):
        if self.__pkgPyInstConfig : return absPath( self.__pkgPyInstConfig.name )
        if self.__pkgIExpressConfig : return absPath( self.__pkgIExpressConfig.name )
        if self.pkgSrcDirPath : return self.pkgSrcDirPath
        if( self.__ifwPkgType() in [QtIfwPackage.Type.PY_INSTALLER,
                                    QtIfwPackage.Type.IEXPRESS] and             
            self.binaryName ): 
            return absPath( self.binaryName )               
        return None                 

    def __pkgExeName( self ):
        if self.binaryName : return self.binaryName
        if self.pkgSrcExePath: 
            return normBinaryName( self.pkgSrcExePath, isGui=self.isGui )  
        return None
        
# -----------------------------------------------------------------------------
@add_metaclass(ABCMeta)
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
        print( "Python Translator:\n    %s" % (sysVersion,) )
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
@add_metaclass(ABCMeta)
class _BuildPackageProcess( _DistBuildProcessBase ):
    def __init__( self, configFactory,                  
                  name="Binary Package Process",
                  isZipped=False, isDesktopTarget=False, isHomeDirTarget=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )                
        
        self.isZipped        = isZipped        
        self.isDesktopTarget = isDesktopTarget
        self.isHomeDirTarget = isHomeDirTarget
        
        self.isExeTest       = False
        self.isElevatedTest  = False
        self.exeTestArgs     = []          
                      
        # Results
        self.binDir = None
        self.binPath = None
                    
    def _moveToDestAndTest( self ):        
          
        destDirPath =( util._userDesktopDirPath() if self.isDesktopTarget else 
                       util._userHomeDirPath()    if self.isHomeDirTarget else 
                       None )          
        if self.isZipped :
            # test exe first!
            if self.isExeTest : self.__testExe() 
            # bin path is actually the zip now...
            self.binPath = toZipFile( self.binDir, zipDest=None, removeScr=True )
            if destDirPath and self.binDir != destDirPath: 
                self.binPath = moveToDir( self.binPath, destDirPath ) 
                self.binDir  = destDirPath
        else:         
            if destDirPath and self.binDir != destDirPath:
                binName = baseFileName( self.binPath )
                isOtherContent = len( [item for item in listdir( self.binDir ) 
                                      if item != binName] ) > 0                                      
                if isOtherContent:
                    self.binDir  = moveToDir( self.binDir, destDirPath )
                    self.binPath = joinPath( self.binDir, binName )
                else:
                    originDirPath = self.binDir 
                    self.binPath = moveToDir( self.binPath, destDirPath )
                    self.binDir  = destDirPath 
                    removeDir( originDirPath )
            if self.isExeTest : self.__testExe()
            
    def __testExe( self ):
        run( self.binPath, self.exeTestArgs,
             isElevated=self.isElevatedTest, isDebug=True )
                    
# -----------------------------------------------------------------------------
class PyToBinPackageProcess( _BuildPackageProcess ):

    def __init__( self, configFactory,                  
                  name="Python to Binary Package Process",
                  isZipped=False, isDesktopTarget=False, isHomeDirTarget=False ) :
        _BuildPackageProcess.__init__( self, configFactory, name,
            isZipped, isDesktopTarget, isHomeDirTarget )        

        self.isObfuscationTest      = False

        self.isWarningSuppression   = True
        self.isUnBufferedStdIo      = False                
        self.isPyInstDupDataPatched = None
                        
        self._pyInstConfig = None
                
    def _body( self ):        
        
        if self.configFactory.isObfuscating :
            opyConfig = self.configFactory.opyConfig() 
            self.onOpyConfig( opyConfig )
            if self.isObfuscationTest:
                _, obPath = obfuscatePy( opyConfig )
                runPy( obPath, self.exeTestArgs, self.isElevatedTest )
                exit()
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
            pyScriptToExe( pyInstConfig=self._pyInstConfig, 
                           opyConfig=opyConfig ) )
        
        self._moveToDestAndTest()
                    
    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onInitialize( self ):        """VIRTUAL"""    
    def onOpyConfig( self, cfg ):    """VIRTUAL"""                    
    def onPyInstConfig( self, cfg ): """VIRTUAL"""
    def onMakeSpec( self, spec ):    """VIRTUAL"""
    def onFinalize( self ):          """VIRTUAL"""

# -----------------------------------------------------------------------------
class IExpressPackageProcess( _BuildPackageProcess ):
    def __init__( self, configFactory,                  
                  name="Windows Script to Binary Package Process",
                  isZipped=False, isDesktopTarget=False, isHomeDirTarget=False ) :
        if not IS_WINDOWS: util._onPlatformErr()
        _BuildPackageProcess.__init__( self, configFactory, name,
            isZipped, isDesktopTarget, isHomeDirTarget )        

        self._iExpressConfig = None
                    
    def _body( self ):        
        self._iExpressConfig = self.configFactory.iExpressConfig()       
        self.onIExpressConfig( self._iExpressConfig )                      
        self.binDir, self.binPath = _scriptToExe( iExpressConfig=
                                                  self._iExpressConfig )        
        self._moveToDestAndTest()
                    
    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onInitialize( self ):          """VIRTUAL"""    
    def onIExpressConfig( self, cfg ): """VIRTUAL"""
    def onFinalize( self ):            """VIRTUAL"""
                            
# -----------------------------------------------------------------------------                        
class _BuildInstallerProcess( _DistBuildProcessBase ):

    def __init__( self, configFactory,
                  name="Build Installer Process",  
                  pyToBinPkgProcesses=None, 
                  iexpressPkgProcesses=None,
                  ifwPackages=None,                                                                                   
                  isDesktopTarget=False, isHomeDirTarget=False ) :
        _DistBuildProcessBase.__init__( self, configFactory, name )
        
        self.pyToBinPkgProcesses =( pyToBinPkgProcesses 
                                    if pyToBinPkgProcesses else [] )
        self.iexpressPkgProcesses=( iexpressPkgProcesses
                                        if iexpressPkgProcesses else [] )        
        self.ifwPackages         = ifwPackages if ifwPackages else [] 
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
                p.configFactory.qtIfwPackage(
                    pyInstConfig=p._pyInstConfig, isTempSrc=True )
            )
        self.onPyPackagesBuilt( self.ifwPackages )
        
        if IS_WINDOWS:
            for p in self.iexpressPkgProcesses:
                p.run()
                self.ifwPackages.append(                
                    p.configFactory.qtIfwPackage( 
                        iExpressConfig=p._iExpressConfig, isTempSrc=True )
                )
            self.onIExpressPackagesBuilt( self.ifwPackages )
            
        ifwConfig = self.configFactory.qtIfwConfig( packages=self.ifwPackages )
        self.onQtIfwConfig( ifwConfig )     
        
        _stageInstallerPackages( ifwConfig, self.configFactory.isSilentSetup )
        self.onPackagesStaged( ifwConfig, ifwConfig.packages )

        if self.configFactory.codeSignConfig:
            for pkg in self.ifwPackages:
                if pkg.codeSignTargets:
                    for relPath in pkg.codeSignTargets: 
                        exePath = absPath( relPath, pkg.contentDirPath() )
                        signExe( exePath, self.configFactory.codeSignConfig ) 
                   
        self.setupPath = _buildInstaller( 
            ifwConfig, self.configFactory.isSilentSetup, 
            self.configFactory.codeSignConfig )
        
        if IS_WINDOWS:
            embedExeVerInfo( self.setupPath, 
                             self.configFactory.exeVersionInfo( ifwConfig ) )
        
        if self.configFactory.codeSignConfig :
            signExe( self.setupPath, self.configFactory.codeSignConfig ) 
        
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
            
            if( self.configFactory.isSilentSetup and  
                IS_WINDOWS and not util._isPrivateRedirectAvailable() ):
                printErr( "WARNING: Silent installer debugging messages "
                          "may not appear in the build log on this LEGACY "
                          "version of Windows! Manual testing of the installer "
                          "should still work in this environment though..." )
            
            run( self.setupPath, verboseArgs + debugArgs + autoArgs,
                 isDebug=True, isElevated=self.isAutoInstallTest )
        
    # Override these to further customize the build process once the 
    # ConfigFactory has produced the initial config object
    def onInitialize( self ):                   """VIRTUAL"""
    def onPyPackagesBuilt( self, pkgs ):        """VIRTUAL"""
    def onIExpressPackagesBuilt( self, pkgs ):  """VIRTUAL"""
    def onQtIfwConfig( self, cfg ):             """VIRTUAL"""
    def onPackagesStaged( self, cfg, pkgs ):    """VIRTUAL"""     
    def onFinalize( self ):                     """VIRTUAL"""
    
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
class IExpressInstallerProcess( _BuildInstallerProcess ):
    
    def __init__( self, configFactory,                  
                  name="Windows Script to Binary Installer Process",
                  isDesktopTarget=False, isHomeDirTarget=False ) :
        
        class CallbackIExpressToBinPackageProcess( IExpressPackageProcess ):
            def __init__( self, parent, configFactory ):
                IExpressPackageProcess.__init__( self, configFactory )
                self.__parent = parent
            def onIExpressConfig( self, cfg ): self.__parent.onIExpressConfig( cfg )
                                       
        prc = CallbackIExpressToBinPackageProcess( self, configFactory )
        self.onIExpressPackageProcess( prc )
            
        _BuildInstallerProcess.__init__( self, 
            configFactory, name,
            iexpressPkgProcesses=[ prc ],                                         
            isDesktopTarget=isDesktopTarget, 
            isHomeDirTarget=isHomeDirTarget )

    # Override these to further customize the build process once the 
    # ConfigFactory has produced each initial config object
    def onInitialize( self ):                    """VIRTUAL"""    
    def onIExpressPackageProcess( self, prc ):   """VIRTUAL"""
    def onIExpressConfig( self, cfg ):           """VIRTUAL"""
    def onQtIfwConfig( self, cfg ):              """VIRTUAL"""                                                                
    def onFinalize( self ):                      """VIRTUAL"""
                                                                                                
# -----------------------------------------------------------------------------                        
class RobustInstallerProcess( _BuildInstallerProcess ):
    
    def __init__( self, masterConfigFactory, 
                  name="Robust Installer Process",
                  pyPkgConfigFactoryDict=None,
                  iExpressPkgConfigFactoryDict=None, 
                  ifwPackages=None,                                     
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

        class CallbackIExpressToBinPackageProcess( IExpressPackageProcess ):
            def __init__( self, parent, key, configFactory ):
                IExpressPackageProcess.__init__( self, configFactory )
                self.__parent = parent
                self.__key    = key                 
            def onInitialize( self ):
                self.__parent.onIExpressPackageInitialize( self.__key )         
            def onIExpressConfig( self, cfg ): 
                self.__parent.onIExpressConfig( self.__key, cfg )                  
            def onFinalize( self ):          
                self.__parent.onIExpressPackageFinalize( self.__key )           
    
        if pyPkgConfigFactoryDict is None: pyPkgConfigFactoryDict={}
        if iExpressPkgConfigFactoryDict is None: 
            iExpressPkgConfigFactoryDict={}
        if ifwPackages is None: ifwPackages=[]

        pyBinPrcs = []
        for key, factory in iteritems( pyPkgConfigFactoryDict ) :        
            if factory is None :
                factory = ConfigFactory.copy( masterConfigFactory )
                factory.cfgId = key
                self.onConfigFactory( key, factory )
            prc = CallbackPyToBinPackageProcess( self, key, factory )
            self.onPyPackageProcess( key, prc )    
            pyBinPrcs.append( prc )        

        if IS_WINDOWS:
            iExpressBinPrcs = []
            for key, factory in iteritems( iExpressPkgConfigFactoryDict ) :        
                if factory is None :
                    factory = ConfigFactory.copy( masterConfigFactory )
                    factory.cfgId = key
                    self.onConfigFactory( key, factory )
                prc = CallbackIExpressToBinPackageProcess( self, key, factory )
                self.onIExpressPackageProcess( key, prc )    
                iExpressBinPrcs.append( prc )        
        
        _BuildInstallerProcess.__init__( self, 
            masterConfigFactory, name,
            ifwPackages=ifwPackages,
            pyToBinPkgProcesses=pyBinPrcs,          
            iexpressPkgProcesses=iExpressBinPrcs,                               
            isDesktopTarget=isDesktopTarget, 
            isHomeDirTarget=isHomeDirTarget )

    # Override these to further customize the build process  
    def onInitialize( self ):                        """VIRTUAL"""        
    def onConfigFactory( self, key, factory ):       """VIRTUAL"""
    
    def onPyPackageProcess( self, key, prc ):        """VIRTUAL"""
    def onPyPackageInitialize( self, key ):          """VIRTUAL"""
    def onOpyConfig( self, key, cfg ):               """VIRTUAL"""                    
    def onPyInstConfig( self, key, cfg ):            """VIRTUAL"""
    def onMakeSpec( self, key, spec ):               """VIRTUAL"""
    def onPyPackageFinalize( self, key ):            """VIRTUAL"""           
    def onPyPackagesBuilt( self, pkgs ):             """VIRTUAL"""
    
    def onIExpressPackageProcess( self, key, prc ): """VIRTUAL"""
    def onIExpressPackageInitialize( self, key ):   """VIRTUAL"""
    def onIExpressConfig( self, key, cfg ):         """VIRTUAL"""
    def onIExpressPackageFinalize( self, key ):     """VIRTUAL"""
    def onIExpressPackagesBuilt( self, pkgs ):      """VIRTUAL"""
        
    def onQtIfwConfig( self, cfg ):                  """VIRTUAL"""     
    def onPackagesStaged( self, cfg, pkgs ):         """VIRTUAL"""                                                     
    def onFinalize( self ):                          """VIRTUAL"""
