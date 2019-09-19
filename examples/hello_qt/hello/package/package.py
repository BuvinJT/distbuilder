from distbuilder import RobustInstallerProcess, ConfigFactory, \
    IS_LINUX, normBinaryName, QtIfwShortcut, QtIfwPackageScript
from distbuilder.util import _normIconName

# Get arguments from QMake
from argparse import ArgumentParser
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

args = parser.parse_args()

f = configFactory  = ConfigFactory()
f.productName      = args.title
f.description      = args.descr
f.companyTradeName = args.company
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

        if cfg.packages is None: return    
        
        firstPkg = cfg.packages[0]          
          
        if cfg.configXml.RunProgram is None:            
            cfg.configXml.RunProgramDescription = firstPkg.pkgXml.DisplayName
            cfg.configXml.primaryContentExe = normBinaryName( firstPkg.exeName, 
                                                              isGui=firstPkg.isGui )                         
            cfg.configXml.setDefaultPaths()        
            
        pngIconResPath = ( _normIconName(f.iconFilePath, isPathPreserved=True)
                           if IS_LINUX else None )             
        versionStr = args.version
                
        defShortcut= QtIfwShortcut(                    
                        productName=f.productName,
                        exeName=firstPkg.exeName,    
                        exeVersion=versionStr,
                        isGui=firstPkg.isGui,                                  
                        pngIconResPath=pngIconResPath )  
        cfg.packages[0].pkgScript = QtIfwPackageScript( firstPkg.name, 
                    shortcuts=[ defShortcut ],
                    fileName=f.ifwPkgScriptName,
                    script=f.ifwPkgScriptText, 
                    scriptPath=f.ifwPkgScriptPath )
                    
p = BuildProcess( configFactory, ifwPackages=[helloQtPkg],
                  isDesktopTarget=True )
p.isTestingInstall = True
p.run()
