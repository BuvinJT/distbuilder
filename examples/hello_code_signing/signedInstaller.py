from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
                         CodeSignConfig, getPassword )

# TODO: ADD SUPPORT FOR THIS FEATURE OUTSIDE OF WINDOWS

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

# NOTE: BOTH the installer and program binary will be signed in this process. 
# You must run the generateTrustCerts example first, to have the key file
# referenced below.
# Supply the key password using one of the following options shown. 
f.codeSignConfig = CodeSignConfig( keyFilePath="./certs/SomeCompany.pfx",
                                   keyPassword=getPassword( isGuiPrompt=True ) )
                                    #keyPassword=None )
                                    #keyPassword="my-secure-password" ) 

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isAutoInstallTest = True
p.run()       
