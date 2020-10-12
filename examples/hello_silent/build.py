from distbuilder import PyToBinInstallerProcess, ConfigFactory

f = configFactory  = ConfigFactory()
f.productName      = "Hello World CLI Example"
f.description      = "CLI Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorld"
f.version          = (1,0,0,0)
f.sourceDir        = "../hello_world"
f.entryPointPy     = "hello.py"  
f.distResources    = ["LICENSE"]
f.licensePath      = "LICENSE"
f.setupName        = "HelloWorldSilentSetup"
f.isSilentSetup    = True

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isAutoInstallTest = True
p.run()       