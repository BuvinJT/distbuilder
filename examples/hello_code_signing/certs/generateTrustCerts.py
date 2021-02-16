from distbuilder import( SelfSignedCertConfig, TrustInstallerBuilderProcess, 
    trustCertInstallerConfigFactory, generateTrustCerts, getPassword ) 

companyTradeName = "Some Company"
companyLegalName = "Some Company Inc."
iconFilePath     = "../../hello_world_tk/demo.ico"

# Supply a key password using one of the following options. 
password = getPassword( isGuiPrompt=True )
#password = None # Verify in prompts that appear that you really don't want a password!
#password = "my-secure-password"

# Generate code signing files to retain (securely!) in house
# It is recommended you set isOverwrite=False in production, to prevent
# accidental losses of certs / keys!
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
