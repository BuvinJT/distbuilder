from distbuilder import PyToBinPackageProcess, ConfigFactory, \
    signExe, SignToolConfig, absPath

f = configFactory  = ConfigFactory()
f.productName      = "Hello World Example"
f.description      = "A Distribution Builder Example"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorld"
f.version          = (1,0,0,0)
f.entryPointPy     = "../hello_world/hello.py"  

p = PyToBinPackageProcess( configFactory )       
p.run()  
signExe( p.binPath, SignToolConfig( pfxFilePath=absPath( "SomeCompany.pfx" ) ) )        