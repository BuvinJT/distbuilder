from distbuilder import RobustInstallerProcess   
from distbuilder.qt_cpp import qmakeInit

args, configFactory = qmakeInit()
f = configFactory

helloQtPkg = f.qtIfwPackage()
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
