from distbuilder import WinScriptToBinPackageProcess, ConfigFactory

f = configFactory  = ConfigFactory()
f.productName      = "Hello Batch Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloBatch"
f.version          = (1,0,0,0)
f.entryPointScript = "hello.bat"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 

p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True )
p.run()       

