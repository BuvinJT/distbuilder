from distbuilder import RobustInstallerProcess   
from distbuilder.qt_cpp import qmakeInit

masterFactory, packageFactory = qmakeInit()
helloQtPkg = packageFactory.qtIfwPackage()
p = RobustInstallerProcess( masterFactory, ifwPackages=[helloQtPkg],
                            isDesktopTarget=True )
p.isInstallTest = True
p.run()
