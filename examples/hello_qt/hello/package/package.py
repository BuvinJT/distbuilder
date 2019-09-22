from distbuilder import RobustInstallerProcess   
from distbuilder.qt_cpp import qmakeInit

configFactory, helloQtPkg = qmakeInit()
p = RobustInstallerProcess( configFactory, ifwPackages=[helloQtPkg],
                            isDesktopTarget=True )
p.isTestingInstall = True
p.run()
