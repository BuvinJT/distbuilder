from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
    QtIfwExeWrapper, \
    IS_WINDOWS, IS_MACOS, IS_LINUX
from distbuilder.qt_installer import QT_IFW_TARGET_DIR, QT_IFW_HOME_DIR

f = configFactory  = ConfigFactory()
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWrapper"
f.isGui            = True        
f.sourceDir        = "../hello_world_tk"
f.entryPointPy     = "hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)

#------------------------------------------------------------------------------
f.productName      = "Hello Elevated Example"
f.setupName        = "HelloElevatedSetup"
f.pkgExeWrapper    = QtIfwExeWrapper( f.binaryName, isElevated=True )
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       

#------------------------------------------------------------------------------
f.productName      = "Hello WorkDir Example"
f.setupName        = "HelloWorkDirSetup"
f.pkgExeWrapper    = QtIfwExeWrapper( f.binaryName, workingDir=QT_IFW_TARGET_DIR )
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       

#------------------------------------------------------------------------------
licenseName = "LICENSE"

if IS_WINDOWS :
    launchScript = (
"""@echo off
set PROG_DIR=%~dp0
start "{0}" "%PROG_DIR%\{1}"
start "Display License" notepad "%PROG_DIR%\{2}"
""".format( f.productName, f.binaryName, licenseName ) )
elif IS_MACOS :
    launchScript = None # TODO
elif IS_LINUX :
    launchScript = None # TODO        
        
f.productName      = "Hello WrapperScript Example"
f.setupName        = "HelloWrapperScriptSetup"
f.distResources    = ["../hello_world/{0}".format( licenseName ) ]
f.pkgExeWrapper    = QtIfwExeWrapper( f.binaryName, 
        wrapperScript=launchScript )
        #wrapperScript=launchScript, isElevated=True, workingDir=QT_IFW_HOME_DIR )
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       
