from distbuilder import PyToBinInstallerProcess, ConfigFactory, QtIfwExeWrapper

f = configFactory  = ConfigFactory()
f.productName      = "Hello Wrapper Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWrapper"
f.isGui            = True        
f.sourceDir        = "../hello_world_tk"
f.entryPointPy     = "hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloWrapperSetup"
f.pkgExeWrapper    = QtIfwExeWrapper( f.binaryName, isElevated=True )

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       
