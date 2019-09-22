from argparse import ArgumentParser
from distbuilder.master import ConfigFactory
from distbuilder.qt_installer import QtIfwPackage, \
    QT_BIN_DIR_ENV_VAR, SRC_COMPILER_OPTIONS 
from distbuilder.util import versionTuple, setEnv 

def qmakeInit(): 
    factory = qmakeConfigFactory()
    package = factory.qtIfwPackage()
    return factory, package

def qmakeConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()
    setEnv( QT_BIN_DIR_ENV_VAR, args.qtBinDirPath )
    f = ConfigFactory()
    f.pkgType          = QtIfwPackage.Type.QT_CPP    
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
    parser.add_argument( "-b", '--binCompiler', default=None, choices=SRC_COMPILER_OPTIONS,
                         help='compiler used (for dependency gathering)' )
    return parser
 