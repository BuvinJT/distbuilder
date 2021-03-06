from distbuilder import WinScriptToBinPackageProcess, ConfigFactory

f = configFactory  = ConfigFactory()
f.productName      = "Hello VBScript Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloVBScript"
f.version          = (1,0,0,0)
f.entryPointScript = "hello.vbs"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 

p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True )
p.run()       

