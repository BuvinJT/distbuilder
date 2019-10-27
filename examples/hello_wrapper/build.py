from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
    QtIfwExeWrapper, \
    IS_WINDOWS, IS_MACOS, IS_LINUX

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
f.pkgExeWrapper    = QtIfwExeWrapper( f.binaryName, workingDir="@TargetDir@" )
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       

#------------------------------------------------------------------------------
f.productName      = "Hello WrapperScript Example"
f.setupName        = "HelloWrapperScriptSetup"
f.distResources    = ["../hello_world/LICENSE"]
if IS_WINDOWS :
    script = (
"""@echo off
cd "%~dp0"
start "{0}" "{1}"
start "Display License" notepad LICENSE""".format( f.productName, f.binaryName ) )
elif IS_MACOS :
    script = None # TODO
elif IS_LINUX :
    script = None # TODO            
f.pkgExeWrapper    = QtIfwExeWrapper( f.binaryName, wrapperScript=script )
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       
