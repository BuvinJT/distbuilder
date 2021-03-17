from distbuilder import IExpressPackageProcess, ConfigFactory

f = configFactory  = ConfigFactory()
f.productName      = "Hello VBScript Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloVBScript"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = "hello.vbs"  

p = IExpressPackageProcess( configFactory, isDesktopTarget=True )
p.isExeTest=True
p.run()       

