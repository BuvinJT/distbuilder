from distbuilder import RobustInstallerProcess, IS_LINUX   
from distbuilder.qt_cpp import qmakeInit, QtCppConfig
    
masterFactory, packageFactory = qmakeInit()
if IS_LINUX :
    cfg = QtCppConfig.CQtDeployerConfig()
    cfg.hiddenQml = [ "QtQuick.Scene3D" ]
    packageFactory.qtCppConfig.cQtDeployerConfig = cfg 
helloQtPkg = packageFactory.qtIfwPackage()
p = RobustInstallerProcess( masterFactory, ifwPackages=[helloQtPkg],
                            isDesktopTarget=True )
p.isInstallTest = True
p.run()
