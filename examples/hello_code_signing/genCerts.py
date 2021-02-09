from distbuilder import( 
    MakeCertConfig, generateTrustCerts, buildTrustCertInstaller ) 

companyName = "My Company"

caCertPath, _, pfxFilePath = generateTrustCerts( 
    MakeCertConfig( companyName ), isOverwrite=True )

buildTrustCertInstaller( companyName, caCertPath, pfxFilePath,
    iconFilePath="../hello_world_tk/demo.ico", isSilent=False, isTest=True )