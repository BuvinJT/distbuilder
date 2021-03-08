from distbuilder import( IExpressInstallerProcess, ConfigFactory,
                         ExecutableScript, baseFileName ) 

LICENSE_FILE_PATH = "../hello_world_tk/LICENSE.TXT"

f = configFactory  = ConfigFactory()
f.productName      = "Hello PowerShell Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloPowerShell"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.distResources    = [ LICENSE_FILE_PATH ]
f.setupName        = "HelloPowerShellSetup"
f.entryPointScript = ExecutableScript( "openTextFile", 
    extension=ExecutableScript.POWERSHELL_EXT, script=([ 
      r'Add-Type -AssemblyName PresentationCore,PresentationFramework'
    , r'[System.Windows.MessageBox]::Show( '
            r'"Click OK to continue..." )'      
    , r'Start-Process -FilePath "$env:windir\system32\notepad.exe"'
            r' -ArgumentList "{fileName}"'                        
    ]), replacements={ "fileName" : baseFileName(LICENSE_FILE_PATH) } )

p = IExpressInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       

