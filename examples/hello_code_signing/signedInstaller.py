from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
                         CodeSignConfig, getPassword)

f = configFactory  = ConfigFactory()
f.productName      = "Hello World Tk Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorldTk"
f.isGui            = True        
f.entryPointPy     = "../hello_world_tk/hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloSignedSetup"

# You must run the generateTrustCerts example first, to have the PFX file
# referenced below.
# Supply the PFX password using one of the following options shown. 
f.codeSignConfig = CodeSignConfig( pfxFilePath="./certs/SomeCompany.pfx",
                             keyPassword=getPassword( isGuiPrompt=True ) )
                            #keyPassword=None )
                            #keyPassword="my-secure-password" ) 

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isAutoInstallTest = True
p.run()       
