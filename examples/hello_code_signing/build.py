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

# You must run the generateTrustCerts example first, to have the PFX file
# referenced below.
# Supply the PFX password using one of the following options shown. 
signConfig = SignToolConfig( pfxFilePath="./certs/SomeCompany.pfx",
                             keyPassword=getPassword( isGuiPrompt=True ) )
                            #keyPassword=None )
                            #keyPassword="my-secure-password" ) 
signExe( p.binPath, signConfig )        