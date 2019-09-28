from distbuilder.master import ConfigFactory
from distbuilder.qt_installer import QtIfwPackage
from distbuilder.util import * # @UnusedWildImport
from distbuilder import util 

from argparse import ArgumentParser
 
QT_BIN_DIR_ENV_VAR = "QT_BIN_DIR"

def qmakeInit(): 
    factory = qmakeConfigFactory()
    package = factory.qtIfwPackage()
    return factory, package

def qmakeConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()
    cppConfig = QtCppConfig( args.qtBinDirPath, args.binCompiler, 
                             qmlScrDirPath=args.qml )
    f = ConfigFactory()
    f.pkgType          = QtIfwPackage.Type.QT_CPP
    f.qtCppConfig      = cppConfig           
    f.pkgSrcExePath    = args.srcExePath
    f.isGui            = args.gui
    f.productName      = args.title
    f.description      = args.descr
    f.companyTradeName = args.company
    f.companyLegalName = args.legal    
    f.iconFilePath     = args.icon
    f.version          = args.version
    f.setupName        = args.setup
    return f

def qmakeArgs(): 
    args = qmakeArgParser().parse_args()
    args.version = versionTuple( args.version )
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
    return parser

# -----------------------------------------------------------------------------
class QtCppConfig:

    __QT_WINDOWS_DEPLOY_EXE_NAME   = "windeployqt.exe"
    __QT_WINDOWS_DEPLOY_QML_SWITCH = "--qmldir"

    __LINUX_DYNAMIC_DEPENDENCIES_UTIL_NAME = "ldd"
    __LDD_DELIMITER_SRC = "=>"
    __LDD_DELIMITER_PATH = " "
        
    #TODO: Add more of these dlls?  
    #TODO: Add additional logic to determine the need for this...
    __MINGW_DLL_LIST = [
          "libgcc_s_dw2-1.dll"
        , "libstdc++-6.dll"
        , "libwinpthread-1.dll"
    ]
    
    __MSVC_BIN  = "msvc"
    __MINGW_BIN = "mingw"

    _LINUX_BIN_WRAPPER_SCRIPT = (
"""#!/bin/sh
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
    
    @staticmethod    
    def srcCompilerOptions(): 
        return [ QtCppConfig.__MSVC_BIN
               , QtCppConfig.__MINGW_BIN 
        ] 
                
    def __init__( self, qtBinDirPath, binCompiler,  
                  qmlScrDirPath=None ):
        self.qtBinDirPath   = qtBinDirPath          
        self.binCompiler    = binCompiler
        self.qmlScrDirPath  = qmlScrDirPath   

    def validate( self ):
        if self.qtBinDirPath is None:
            self.qtBinDirPath = getEnv( QT_BIN_DIR_ENV_VAR )    
        if( self.qtBinDirPath is None or
            not isDir(self.qtBinDirPath) ):        
            raise Exception( "Valid Qt Bin directory path required" )
    
    # Refer to: https://doc.qt.io/qt-5/deployment.html
    def addDependencies( self, package ) :
        print( "Adding binary dependencies...\n" )
        self.validate()                
        # TODO: Add the counterparts here for other platforms
        destDirPath = package.contentDirPath()
        exePath = joinPath( destDirPath, package.exeName )
        if IS_WINDOWS :
            qtUtilityPath =  normpath( joinPath( 
                self.qtBinDirPath, QtCppConfig.__QT_WINDOWS_DEPLOY_EXE_NAME ) )                    
            cmdList = [qtUtilityPath, exePath]
            if self.qmlScrDirPath is not None:
                cmdList.append( QtCppConfig.__QT_WINDOWS_DEPLOY_QML_SWITCH )
                cmdList.append( normpath( self.qmlScrDirPath ) )
            util._system( list2cmdline( cmdList ) )
            if self.binCompiler == QtCppConfig.__MINGW_BIN:            
                for fileName in QtCppConfig.__MINGW_DLL_LIST:
                    copyToDir( joinPath( self.qtBinDirPath, fileName ), 
                               destDirPath=destDirPath )
        elif IS_LINUX:            
            cmdList = [QtCppConfig.__LINUX_DYNAMIC_DEPENDENCIES_UTIL_NAME, 
                       exePath]            
            lddLines = util._subProcessStdOut( 
                                cmdList, asCleanLines=True, isDebug=True )
            for line in lddLines:
                try :
                    src = line.split( QtCppConfig.__LDD_DELIMITER_SRC )[1].strip()
                    path = src.split( QtCppConfig.__LDD_DELIMITER_PATH )[0].strip()
                    if isFile( path ): 
                        copyToDir( path, destDirPath=destDirPath )                        
                except: pass
            binWrapperPath = "%s.sh" % (joinPath( destDirPath, package.exeName ),)
            print("Writing binary wrapper script:\n\n%s\n" % 
                  (QtCppConfig._LINUX_BIN_WRAPPER_SCRIPT))   
            with open( binWrapperPath, 'w' ) as f:
                f.write( QtCppConfig._LINUX_BIN_WRAPPER_SCRIPT )              
