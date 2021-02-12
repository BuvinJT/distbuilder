from distbuilder import( SelfSignedCertConfig, TrustInstallerBuilderProcess, 
    getPassword, generateTrustCerts, trustCertInstallerConfigFactory ) 

companyTradeName = "Some Company"
companyLegalName = "Some Company Inc."
iconFilePath     = "../../hello_world_tk/demo.ico"

# Supply a PFX password using one of the following options. 
password = getPassword( isGuiPrompt=True )
#password = None # click ok through the prompts if you really don't want a password!
#password = "my-secure-password"

# Generate code signing files to retain (securely!) in house
# It is recommended you set isOverwrite=False in production, to prevent
# accidental losses of certs / keys.
certConfig = SelfSignedCertConfig( companyTradeName )
caCertPath, keyFilePath = generateTrustCerts( 
    certConfig, keyPassword=password, isOverwrite=True )

configFactory = trustCertInstallerConfigFactory( 
    companyTradeName, caCertPath, keyFilePath, keyPassword=password, 
    companyLegalName=companyLegalName, iconFilePath=iconFilePath,    
    isSilent=False )

p = TrustInstallerBuilderProcess( configFactory, isDesktopTarget=True )
p.isExeTest      = True
p.isElevatedTest = True
p.run()
 