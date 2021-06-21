from distbuilder import( PyToBinPackageProcess, ConfigFactory, 
                         CodeSignConfig, getPassword )

# TODO: ADD SUPPORT FOR THIS FEATURE OUTSIDE OF WINDOWS

f = configFactory  = ConfigFactory()
f.productName      = "Hello World Example"
f.description      = "A Distribution Builder Example"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorld"
f.version          = (1,0,0,0)
f.entryPointPy     = "../hello_world/hello.py"  

# You must run the generateTrustCerts example first, to have the key file
# referenced below.
# Supply the key password using one of the following options shown. 
f.codeSignConfig = CodeSignConfig( keyFilePath="./certs/SomeCompany.pfx",
                                   keyPassword=getPassword( isGuiPrompt=True ) )
                                    #keyPassword=None )
                                    #keyPassword="my-secure-password" ) 

p = PyToBinPackageProcess( configFactory )       
p.run()  
