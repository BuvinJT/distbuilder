from distbuilder.master import ConfigFactory
from distbuilder.qt_installer import QtIfwPackage, QtIfwExeWrapper
from distbuilder.util import * # @UnusedWildImport
from distbuilder import util 

from argparse import ArgumentParser

QT_BIN_DIR_ENV_VAR = "QT_BIN_DIR"
 
def qmakeInit():     
    args = qmakeArgs()
    installDeployTools( args.askPass )    
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

def qmakeMasterConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()
    f = ConfigFactory()
    f.productName         = args.title
    f.description         = args.descr
    f.companyTradeName    = args.company
    f.companyLegalName    = args.legal    
    f.iconFilePath        = args.icon
    f.version             = args.version
    f.setupName           = args.setup
    return f

def qmakePackageConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()
    cppConfig = QtCppConfig( args.qtBinDirPath, args.binCompiler, 
                             qmlScrDirPath=args.qml )
    f = ConfigFactory()
    f.pkgType             = QtIfwPackage.Type.QT_CPP
    f.qtCppConfig         = cppConfig               
    f.pkgSrcExePath       = args.srcExePath
    f.pkgExeWrapper       = QtCppConfig.exeWrapper( args.srcExePath, args.gui )
    f.isGui               = args.gui
    f.productName         = args.title
    f.description         = args.descr
    f.companyTradeName    = args.company
    f.companyLegalName    = args.legal    
    f.iconFilePath        = args.icon
    f.version             = args.version
    return f

def qmakeArgs(): 
    args = qmakeArgParser().parse_args()
    args.version = versionTuple( args.version )
    if not IS_LINUX : args.askPass = None
    return args

def qmakeArgParser():      
    parser = ArgumentParser( description="Build a Qt installer." )
    parser.add_argument( "srcExePath", help="path to the source executable" )
    parser.add_argument( "qtBinDirPath", help="path to the Qt Bin directory" )
    parser.add_argument( "-g", "--gui", default=False, action='store_true', help="is gui exe" )
    parser.add_argument( "-t", "--title", default="?", help="Product title" )
    parser.add_argument( "-d", "--descr", default="?", help="Product description" )
    parser.add_argument( "-c", "--company", default="?", help="Company trade name" )
    parser.add_argument( "-l", "--legal", default=None, help="Company legal name" )
    parser.add_argument( "-i", "--icon", default=None, help="Icon path" )
    parser.add_argument( "-v", "--version", default="0.0.0.0", help="Product version" )
    parser.add_argument( "-s", "--setup", default=None, help="Setup name" )
    parser.add_argument( "-b", '--binCompiler', default=None, 
                         choices=QtCppConfig.srcCompilerOptions(),
                         help='compiler used (for dependency gathering)' )
    parser.add_argument( "-q", "--qml", default=None, help="path to the QML source directory" )
    if IS_LINUX :
        parser.add_argument( "-a", "--askPass", default=None, help='Path to an "AskPass" program' )    
    return parser

# -----------------------------------------------------------------------------
class QtCppConfig:
        
    def __init__( self, qtBinDirPath, binCompiler,  
                  qmlScrDirPath=None ):
        self.qtBinDirPath   = qtBinDirPath          
        self.binCompiler    = binCompiler
        self.qmlScrDirPath  = qmlScrDirPath   

    def validate( self ):
        if IS_WINDOWS or ( IS_LINUX and _isCqtdeployerInstalled() ):
            if self.qtBinDirPath is None:
                self.qtBinDirPath = getEnv( QT_BIN_DIR_ENV_VAR )    
            if self.qtBinDirPath is None or not isDir(self.qtBinDirPath):        
                raise Exception( "Valid Qt Bin directory path required" )
    
    # Refer to: https://doc.qt.io/qt-5/deployment.html
    def addDependencies( self, package ) :
        print( "Adding binary dependencies...\n" )        
        self.validate()                
        destDirPath = package.contentDirPath()
        exePath = joinPath( destDirPath, package.exeName )
        if IS_WINDOWS :
            self.__useWindeployqt( destDirPath, exePath )
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
                
    def __useCqtdeployer( self, destDirPath, exePath ):             
        # collect required dependencies via the third party cqtdeployer utility
        qmakePath = normpath( joinPath( 
            self.qtBinDirPath, QtCppConfig.__QMAKE_EXE_NAME ) )
        cmdList = [QtCppConfig.__C_QT_DEPLOYER_CMD,                   
                   QtCppConfig.__C_QT_DEPLOYER_BIN_SWITCH, exePath,
                   QtCppConfig.__C_QT_DEPLOYER_QMAKE_SWITCH, qmakePath,
                   QtCppConfig.__C_QT_DEPLOYER_TARGET_SWITCH, destDirPath ]
        # optionally detect and bundle QML resources
        if self.qmlScrDirPath is not None:
            cmdList.extend( [QtCppConfig.__C_QT_DEPLOYER_QML_SWITCH,
                             normpath( self.qmlScrDirPath )] )                    
        util._system( list2cmdline( cmdList ) )
        # return where the exe ends up
        exePath = joinPath( joinPath( 
            destDirPath, QtCppConfig.__C_QT_DEPLOYER_TARGET_BIN_DIR ),
            normBinaryName(exePath) )
        return exePath
    
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
        #TODO: continue to develop this, so it almost revivals cqtdeploy
        
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
                                    wrapperScript=exeScript )            
        else: return None

    __QMAKE_EXE_NAME = normBinaryName( "qmake" )
            
    __QT_WINDOWS_DEPLOY_EXE_NAME   = "windeployqt.exe"
    __QT_WINDOWS_DEPLOY_QML_SWITCH = "--qmldir"
    
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
        _system( list2cmdline(cmdList) )
    
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
    
