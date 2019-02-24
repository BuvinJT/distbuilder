from distbuilder import PyToBinPackageProcess, ConfigFactory

f = configFactory  = ConfigFactory()
f.productName      = "Hello World Example"
f.description      = "A Distribution Builder Example"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorld"
f.entryPointPy     = "hello.py"  
f.version          = (1,0,0,0)
f.distResources    = ["LICENSE"]

PyToBinPackageProcess( configFactory, isZipped=True ).run()       