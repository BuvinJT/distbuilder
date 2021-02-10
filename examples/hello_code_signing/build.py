from distbuilder import PyToBinPackageProcess, ConfigFactory, \
    SignToolConfig, signExe, getPassword

f = configFactory  = ConfigFactory()
f.productName      = "Hello World Example"
f.description      = "A Distribution Builder Example"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorld"
f.version          = (1,0,0,0)
f.entryPointPy     = "../hello_world/hello.py"  

p = PyToBinPackageProcess( configFactory )       
p.run()  

# You must run the generateTrustCerts example first, to have this PFX!
signExe( p.binPath, SignToolConfig(pfxFilePath="SomeCompany.pfx",
                                   pfxPassword=getPassword(isGuiPrompt=True)) )        