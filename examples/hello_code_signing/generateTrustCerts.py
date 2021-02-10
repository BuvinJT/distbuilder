from distbuilder import( MakeCertConfig, 
                         getPassword, generateTrustCerts, buildTrustCertInstaller ) 

companyTradeName = "Some Company"
companyLegalName = "Some Company Inc."
password         = getPassword( isGuiPrompt=True )

caCertPath, _, pfxFilePath = generateTrustCerts( 
    MakeCertConfig( companyTradeName ), pfxPassword=password, isOverwrite=True )

buildTrustCertInstaller( 
    companyTradeName, caCertPath, pfxFilePath, pfxPassword=password,
    companyLegalName=companyLegalName, iconFilePath="../hello_world_tk/demo.ico", 
    isSilent=False, isTest=True )