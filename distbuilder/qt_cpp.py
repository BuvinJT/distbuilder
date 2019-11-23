from distbuilder.master import ConfigFactory
from distbuilder.qt_installer import QtIfwPackage, QtIfwExeWrapper
from distbuilder.util import * # @UnusedWildImport
from distbuilder import util 

from argparse import ArgumentParser

QT_BIN_DIR_ENV_VAR = "QT_BIN_DIR"
 
def qmakeInit():     
    args = qmakeArgs()
    installDeployTools( args.askPass )
    if args.exeName: renameExe( args )    
    return qmakeMasterConfigFactory( args ), qmakePackageConfigFactory( args )

def installDeployTools( askPassPath=None ):             
    if IS_LINUX:
        # Attempt to install the third-party utility "cqtdeployer". The 
        # installation mechanism requires "snapd".  Since this script is 
        # intended to be run inside of  QtCreator, we need to assert an  
        # "AskPass" program is available (when that context is detected) in 
        # order to run sudo commands. If the utility can't be installed, print      
        # the errors, and continue  on, as there is a "fallback" option ("ldd")
        # to try when needed instead of this preferred mechanism.                       
        util._assertAskPassAvailable( askPassPath ) 
        if not _isCqtdeployerInstalled():
            isSnapdInstalled = _isSnapdInstalled()
            if not isSnapdInstalled:
                try: _installSnapd()
                except Exception as e: printExc( e ) 
                isSnapdInstalled = _isSnapdInstalled() # confirm success
            if isSnapdInstalled:
                try: _installCqtdeployer()
                except Exception as e: printExc( e )
        util._restoreAskPass()        

def renameExe( args=None ):
    if args.exeName is None: return
    parentDir, oldName = splitPath( args.exePath )
    newName = normBinaryName( args.exeName, isGui=args.gui )
    newPath = joinPath( parentDir, newName )
    if isFile( newPath  ): args.exePath = newPath  
    else: args.exePath = renameInDir( (oldName, newName), parentDir )
         
def qmakeMasterConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()
    f = ConfigFactory()
    
    f.isGui               = args.gui
    f.iconFilePath        = args.icon    
    f.setupName           = args.setupName

    f.productName         = args.title
    f.description         = args.descr
    f.companyTradeName    = args.company
    f.companyLegalName    = args.legal
    f.version             = args.version
            
    return f

def qmakePackageConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()
    cppConfig = QtCppConfig( args.qtBinDir, args.binCompiler, 
                             qmlScrDirPath=args.qmlDir )
    f = ConfigFactory()
    
    f.pkgType             = QtIfwPackage.Type.QT_CPP
    f.qtCppConfig         = cppConfig               
    
    f.sourceDir           =( args.srcDir if args.srcDir else 
                             dirPath( args.exePath ) )
    f.pkgSrcExePath       = args.exePath
    f.pkgExeWrapper       = QtCppConfig.exeWrapper( args.exePath, args.gui )

    f.isGui               = args.gui
    f.iconFilePath        = args.icon    
    f.distResources       = [r for r in args.resource]
    
    f.productName         = args.title
    f.description         = args.descr
    f.companyTradeName    = args.company
    f.companyLegalName    = args.legal        
    f.version             = args.version
    
    return f

def qmakeArgs(): 
    args = qmakeArgParser().parse_args()
    args.version = versionTuple( args.version )
    if not IS_LINUX : args.askPass = None
    return args

def qmakeArgParser():      
    parser = ArgumentParser( description="Build a Qt installer." )
    
    # required paths
    parser.add_argument( "exePath", 
                         help="executable path (within Qt build directory)" )
    parser.add_argument( "qtBinDir", 
                         help="Qt Bin directory path (QMake directory)" )
    
    # optional paths
    parser.add_argument( "-s", "--srcDir", default=None, 
                         help="project (root) source directory" )
    parser.add_argument( "-q", "--qmlDir", default=None, 
                         help="QML source directory" )
    parser.add_argument( "-i", "--icon", default=None, 
                         help="icon path" )
    parser.add_argument( "-r", "--resource", default=[], action="append", 
                         help="resource path (repeatable option)" )    

    # build details
    parser.add_argument( "-g", "--gui", default=True, action='store_true', 
                         help="is a GUI program" )
    parser.add_argument( "-b", "--binCompiler", default=None, 
                         choices=QtCppConfig.srcCompilerOptions(),
                         help="compiler used (dependency gathering)" )
    parser.add_argument( "-n", "--setupName", default=None, 
                         help="setup name" )   
    parser.add_argument( "-e", "--exeName", default=None, 
                         help="executable REname" )

    # meta info / product branding
    parser.add_argument( "-t", "--title", default="?", 
                         help="product title" )
    parser.add_argument( "-d", "--descr", default="?", 
                         help="product description" )
    parser.add_argument( "-c", "--company", default="?", 
                         help="company trade name" )
    parser.add_argument( "-l", "--legal", default=None, 
                         help="company legal name" )
    parser.add_argument( "-v", "--version", default="0.0.0.0", 
                         help="product version" )
    
    # build utilities    
    if IS_LINUX :
        parser.add_argument( "-a", "--askPass", default=None, 
                             help='Path to an "AskPass" program' )    
    return parser

# -----------------------------------------------------------------------------
class QtCppConfig:
        
    def __init__( self, qtBinDirPath, binCompiler,  
                  qmlScrDirPath=None ):
        self.qtBinDirPath  = qtBinDirPath          
        self.binCompiler   = binCompiler
        self.qmlScrDirPath = qmlScrDirPath
                
        self.cQtDeployerConfig = None

    def qtDirPath( self ):
        qtDir = self.qtBinDirPath
        head, tail = splitPath( qtDir )
        if tail=="bin" : qtDir=head
        return qtDir 
        
    def validate( self ):
        if self.qtBinDirPath is None:
            self.qtBinDirPath = getEnv( QT_BIN_DIR_ENV_VAR )    
        if self.qtBinDirPath is None or not isDir( self.qtBinDirPath ):        
            raise Exception( "Valid Qt Bin directory path required" )
    
    # Refer to: https://doc.qt.io/qt-5/deployment.html
    def addDependencies( self, package ) :
        print( "Adding binary dependencies...\n" )        
        self.validate()                
        destDirPath = package.contentDirPath()
        exePath = joinPath( destDirPath, package.exeName )
        if IS_WINDOWS :
            self.__useWindeployqt( destDirPath, exePath )
        elif IS_MACOS :
            self.__useMacdeployqt( destDirPath, exePath )    
        elif IS_LINUX:       
            if _isCqtdeployerInstalled():
                exePath = self.__useCqtdeployer( destDirPath, exePath )
            else :                
                printErr(
                    "\n\n>>> WARNING: Cannot utilize cqtdeployer tool! <<<\n\n"
                    "Attempting to use primitive built-in method...\n"
                    "(The resulting distro may not function!)\n")
                self.__useLdd( destDirPath, exePath )

    def __useWindeployqt( self, destDirPath, exePath ):             
        # collect required dependencies via the Qt deploy utility for Windows
        qtUtilityPath =  normpath( joinPath( 
            self.qtBinDirPath, QtCppConfig.__QT_WINDOWS_DEPLOY_EXE_NAME ) )                                
        cmdList = [qtUtilityPath, exePath]
        # optionally detect and bundle QML resources
        if self.qmlScrDirPath is not None:
            cmdList.extend( [QtCppConfig.__QT_WINDOWS_DEPLOY_QML_SWITCH,
                             normpath( self.qmlScrDirPath )] )
        util._system( list2cmdline( cmdList ) )
        # add additional .dlls the Qt utility seems to miss
        if self.binCompiler == QtCppConfig.__MINGW:            
            for fileName in QtCppConfig.__MINGW_DLL_LIST:
                copyToDir( joinPath( self.qtBinDirPath, fileName ), 
                           destDirPath=destDirPath )

    def __useMacdeployqt( self, destDirPath, exePath ):             
        # collect required dependencies via the Qt deploy utility for MacOS
        qtUtilityPath =  normpath( joinPath( 
            self.qtBinDirPath, QtCppConfig.__QT_MACOS_DEPLOY_EXE_NAME ) )                                
        cmdList = [qtUtilityPath, exePath]
        cmd = list2cmdline( cmdList )
        # optionally detect and bundle QML resources
        if self.qmlScrDirPath is not None:
            cmd = '%s %s="%s"' % (cmd, QtCppConfig.__QT_MACOS_DEPLOY_QML_SWITCH,
                                  normpath( self.qmlScrDirPath ))
        util._system( cmd )

    def __useCqtdeployer( self, destDirPath, exePath ):             
        # collect required dependencies via the third party cqtdeployer utility
        qmakePath = normpath( joinPath( 
            self.qtBinDirPath, QtCppConfig.__QMAKE_EXE_NAME ) )
        cmdList = [QtCppConfig.__C_QT_DEPLOYER_CMD,                   
                   QtCppConfig.__C_QT_DEPLOYER_BIN_SWITCH, exePath,
                   QtCppConfig.__C_QT_DEPLOYER_QMAKE_SWITCH, qmakePath,
                   QtCppConfig.__C_QT_DEPLOYER_TARGET_SWITCH, destDirPath ]
        # optionally detect and bundle QML resources
        if self.qmlScrDirPath:
            cmdList.extend( [QtCppConfig.__C_QT_DEPLOYER_QML_SWITCH,
                             normpath( self.qmlScrDirPath )] )
        cmd = list2cmdline( cmdList )
        # optionally tack on extended cQtDeployer options
        cfg = self.cQtDeployerConfig
        if cfg:
            extArgs = cfg._extendedCmdArgs()
            if len(extArgs) > 0: cmd = "%s %s" % (cmd, extArgs)            
        util._system( cmd )
        # resolve where the exe ends up
        exePath = joinPath( joinPath( 
            destDirPath, QtCppConfig.__C_QT_DEPLOYER_TARGET_BIN_DIR ),
            normBinaryName(exePath) )
        # inject missing qml packages
        if cfg and len(cfg.hiddenQml) > 0:
            qmlSrcDirPath = joinPath( self.qtDirPath(), "qml" )
            qmlDestDirPath = joinPath( 
                destDirPath, QtCppConfig.__C_QT_DEPLOYER_TARGET_QML_DIR )            
            for pkg in cfg.hiddenQml:
                subDir = pkg.replace( ".", PATH_DELIM )
                src  = joinPath( qmlSrcDirPath,  subDir )
                dest = joinPath( qmlDestDirPath, subDir )
                print( "Copying %s to %s..." % (src, dest) )
                copyDir( src, dest )    
        # return the path to the exe produced  
        return exePath

    # This a fallback (limited) option to attempt on Linux systems which don't
    # have the cqtdeploy utility installed.  
    # TODO: continue to develop this, so it more closely revivals cqtdeploy...    
    def __useLdd( self, destDirPath, exePath ):             
        # get the list of .so libraries the binary links against within the 
        # local environment, via the standard Linux utility for this.  
        # Parse that output and collect the files. 
        cmdList = [QtCppConfig.__LDD_CMD, 
                   exePath]            
        lddLines = util._subProcessStdOut( cmdList, asCleanLines=True )
        for line in lddLines:
            try :
                src = line.split( QtCppConfig.__LDD_DELIMITER_SRC )[1].strip()
                path = src.split( QtCppConfig.__LDD_DELIMITER_PATH )[0].strip()
                if isFile( path ): 
                    copyToDir( path, destDirPath=destDirPath )                        
            except: pass
        # The Qt produced binary does not have execute permissions automatically!
        chmod( exePath, 0o755 )
                
    class CQtDeployerConfig:
            
        def __init__( self ):            
            self.libDirs    = []
            self.plugins    = []           
            self.hiddenQml  = []
            
            self.ignoreLibs = [] 
            self.ignoreEnv  = [] 
            
            self.recurseDepth = 0
            self.deploySystem = False            
            self.deployLibc   = False
            self.allQml       = False

            self.strip        = True 
            self.translations = True

            self.otherArgs = None
            
        def _extendedCmdArgs( self ):
            def _argList( l ): return ",".join(l)
            
            args = ""

            if len(self.libDirs) > 0: 
                args += " -libDir " + _argList(self.libDirs) 
            if len(self.plugins) > 0: 
                args += " -extraPlugin " + _argList(self.plugins)
                 
            if len(self.ignoreLibs) > 0: 
                args += " -ignore " + _argList(self.ignoreLibs)
            if len(self.ignoreEnv) > 0: 
                args += " -ignoreEnv " + _argList(self.ignoreEnv)         
                    
            if self.recurseDepth > 0: 
                args += " -recursiveDepth %d" % (self.recurseDepth,)            
            if self.deploySystem: args += " deploySystem" 
            if self.deployLibc:   args += " deploySystem-with-libc"
            if self.allQml:       args += " allQmlDependes"

            if not self.strip:        args += " noStrip"
            if not self.translations: args += " noTranslations"
            
            if self.otherArgs: args += " " + self.otherArgs
            
            return args.strip()
             
        
    @staticmethod    
    def srcCompilerOptions(): 
        if IS_WINDOWS :
            return [ QtCppConfig.__MSVC, QtCppConfig.__MINGW ] 
        return ["default"]

    @staticmethod    
    def exeWrapper( exePath, isGui ): 
        if IS_LINUX:            
            exeScript = ExecutableScript( rootFileName( exePath ), 
                script=( None if _isCqtdeployerInstalled() else   
                         QtCppConfig.__DEFAULT_LINUX_BIN_WRAPPER_SCRIPT ) )            
            return QtIfwExeWrapper( normBinaryName(exePath, isGui),
                                    isGui=isGui,
                                    wrapperScript=exeScript )            
        else: return None

    __QMAKE_EXE_NAME = normBinaryName( "qmake" )
            
    __QT_WINDOWS_DEPLOY_EXE_NAME   = "windeployqt.exe"
    __QT_WINDOWS_DEPLOY_QML_SWITCH = "--qmldir"

    __QT_MACOS_DEPLOY_EXE_NAME   = "macdeployqt"
    __QT_MACOS_DEPLOY_QML_SWITCH = "-qmldir"
    
    #TODO: Add more of these dlls?  
    #TODO: Add additional logic to determine the need for this...
    __MINGW_DLL_LIST = [
          "libgcc_s_dw2-1.dll"
        , "libstdc++-6.dll"
        , "libwinpthread-1.dll"
    ]
    
    __MSVC  = "msvc"
    __MINGW = "mingw"
    
    __C_QT_DEPLOYER_CMD            = "cqtdeployer" 
    __C_QT_DEPLOYER_BIN_SWITCH     = "-bin" 
    __C_QT_DEPLOYER_QMAKE_SWITCH   = "-qmake" 
    __C_QT_DEPLOYER_TARGET_SWITCH  = "-targetDir"
    __C_QT_DEPLOYER_TARGET_BIN_DIR = "bin"
    __C_QT_DEPLOYER_TARGET_QML_DIR = "qml"
    __C_QT_DEPLOYER_QML_SWITCH     = "-qmlDir"    

    __LDD_CMD            = "ldd"
    __LDD_DELIMITER_SRC  = "=>"
    __LDD_DELIMITER_PATH = " "
        
    # Note: this is nearly a verbatim copy of the script Qt
    # offers up for this purpose.  The only change is the addition
    # of quotes in a few places, which allows for paths with spaces.   
    # The shebang is omitted because class ExecutableScript injects that. 
    __DEFAULT_LINUX_BIN_WRAPPER_SCRIPT = (
"""
appname=`basename "$0" | sed s,\.sh$,,`
dirname=`dirname "$0"`
tmp="${dirname#?}"
if [ "${dirname%$tmp}" != "/" ]; then
dirname="$PWD/$dirname"
fi
LD_LIBRARY_PATH="$dirname"
export LD_LIBRARY_PATH
"$dirname/$appname" "$@"
""")
        
# -----------------------------------------------------------------------------

if IS_LINUX:
    __C_QT_DEPLOYER_CMD        = "cqtdeployer"
    __C_QT_DEPLOYER_FOUND_TEST = "help"
    __C_QT_DEPLOYER_SNAP_NAME  = "cqtdeployer"    
        
    __SNAP_CMD         = "snap"
    __SNAP_FOUND_TEST  = "version"
    __SNAP_INSTALL_OPT = "install"

    def _isCqtdeployerInstalled():
        try: 
            check_call( [__C_QT_DEPLOYER_CMD, __C_QT_DEPLOYER_FOUND_TEST], 
                        stdout=DEVNULL, stderr=DEVNULL )
            return True                                                              
        except: return False    
    
    def _installCqtdeployer():
        cmdList = ["sudo", __SNAP_CMD,
                   __SNAP_INSTALL_OPT, __C_QT_DEPLOYER_SNAP_NAME]
        util._system( list2cmdline(cmdList) )
    
    def _isSnapdInstalled():
        try: 
            check_call( [__SNAP_CMD, __SNAP_FOUND_TEST], 
                        stdout=DEVNULL, stderr=DEVNULL )
            return True                                                              
        except: return False    
        
    def _installSnapd():
        # For now, don't even try to do this in a cross distro manner...
        raise Exception( "Snapd installation must be performed manually."
            "Refer to https://snapcraft.io/docs/installing-snapd" )
    
