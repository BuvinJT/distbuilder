from distbuilder import( IExpressPackageProcess, ConfigFactory, 
                         ExecutableScript )

DEMO_TYPE = ExecutableScript.BATCH_EXT

def popupMessageScript( scriptExt ):
    scriptOptions = {
          ExecutableScript.BATCH_EXT :    
            r'start "Message" /wait cmd /c "echo Directory: %CD% & pause"'
        , ExecutableScript.POWERSHELL_EXT: [
            r'Add-Type -AssemblyName PresentationCore,PresentationFramework'
          , r'[System.Windows.MessageBox]::Show("Directory: "+(Get-Location))'
        ]
        , ExecutableScript.VBSCRIPT_EXT:  
            r'MsgBox "Directory: " & '
                r'CreateObject("WScript.Shell").CurrentDirectory'
    }    
    script = scriptOptions.get( scriptExt )
    if not script: raise Exception( "Invalid Script Type!" )        
    return ExecutableScript( "popup", extension=scriptExt, script=script ) 

f = configFactory  = ConfigFactory()
f.productName      = "Hello Dynamic Script Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloDynamicScript"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = popupMessageScript( DEMO_TYPE )

p = IExpressPackageProcess( configFactory, isDesktopTarget=True )
p.isExeTest = True
p.run()       

