from distbuilder import RobustInstallerProcess, ConfigFactory, normBinaryName
from argparse import ArgumentParser

# Get arguments from QMake
parser = ArgumentParser( description="Build a Qt installer." )
parser.add_argument( "binaryPath", help="path to the source executable" )
parser.add_argument( "qtBinDirPath", help="path to the Qt Bin directory" )
parser.add_argument( "-t", "--title", default="?", help="Product title" )
parser.add_argument( "-d", "--descr", default="?", help="Product description" )
parser.add_argument( "-c", "--company", default="?", help="Company name" )
parser.add_argument( "-l", "--legal", default=None, help="Company legal name" )
parser.add_argument( "-i", "--icon", default=None, help="Icon path" )
parser.add_argument( "-v", "--version", default="0.0.0.0", help="Product version" )
parser.add_argument( "-s", "--setup", default=None, help="Setup name" )
parser.add_argument( "-b", '--binCompiler', default=None, choices=['msvc', 'mingw'],
                     help='compiler used (for dependency gathering)' )

args = parser.parse_args()

f = configFactory  = ConfigFactory()
f.productName      = args.title
f.description      = args.descr
f.companyName      = args.company
f.companyLegalName = args.legal    
f.iconFilePath     = args.icon
f.version          = tuple(args.version.split(".")[:-4])
f.setupName        = args.setup

helloQtPkg = f.qtIfwPackage()
helloQtPkg.srcExePath = args.binaryPath
helloQtPkg.exeName = normBinaryName(args.binaryPath) #eww...
helloQtPkg.isGui = True
helloQtPkg.isQtCppExe = True
helloQtPkg.isMingwExe = (args.binCompiler=='mingw')

class BuildProcess( RobustInstallerProcess ): 
    def onQtIfwConfig( self, cfg ):
        cfg.qtBinDirPath = args.qtBinDirPath              
p = BuildProcess( configFactory, ifwPackages=[helloQtPkg],
                  isDesktopTarget=True )
p.isTestingInstall = True
p.run()
