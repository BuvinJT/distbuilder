from argparse import ArgumentParser
from distbuilder.master import ConfigFactory
from distbuilder.util import *  # @UnusedWildImport

def qmakeArgParser():      
    parser = ArgumentParser( description="Build a Qt installer." )
    parser.add_argument( "binaryPath", help="path to the source executable" )
    parser.add_argument( "qtBinDirPath", help="path to the Qt Bin directory" )
    parser.add_argument( "-t", "--title", default="?", help="Product title" )
    parser.add_argument( "-d", "--descr", default="?", help="Product description" )
    parser.add_argument( "-c", "--company", default="?", help="Company trade name" )
    parser.add_argument( "-l", "--legal", default=None, help="Company legal name" )
    parser.add_argument( "-i", "--icon", default=None, help="Icon path" )
    parser.add_argument( "-v", "--version", default="0.0.0.0", help="Product version" )
    parser.add_argument( "-s", "--setup", default=None, help="Setup name" )
    parser.add_argument( "-b", '--binCompiler', default=None, choices=['msvc', 'mingw'],
                         help='compiler used (for dependency gathering)' )
    return parser
 
def qmakeArgs(): 
    args = qmakeArgParser().parse_args()
    args.version = versionTuple( args.version )
    return args

def qmakeConfigFactory( args=None ): 
    if args is None: args = qmakeArgs()    
    f = ConfigFactory()
    f.productName      = args.title
    f.description      = args.descr
    f.companyTradeName = args.company
    f.companyLegalName = args.legal    
    f.iconFilePath     = args.icon
    f.version          = args.version
    f.setupName        = args.setup
    return f

def qmakeInit(): 
    args = qmakeArgs()
    factory = qmakeConfigFactory( args )    
    return args, factory

