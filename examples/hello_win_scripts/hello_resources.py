from distbuilder import( WinScriptToBinPackageProcess, ConfigFactory,
                         ExecutableScript )

def openTextFileScript( scriptExt, fileName ):
    scriptOptions = {
          ExecutableScript.BATCH_EXT : 
            r'start "" "%windir%\system32\notepad.exe" "{fileName}"'
        , ExecutableScript.POWERSHELL_EXT :
            r'Start-Process -FilePath "$env:windir\system32\notepad.exe" -ArgumentList "{fileName}"'            
        , ExecutableScript.VBSCRIPT_EXT: [
              r'Dim oShell : Set oShell = CreateObject( "WScript.Shell" )'
            , r'oShell.Exec( "%ComSpec% /c start """" ""%windir%\system32\notepad.exe"" ""{fileName}""" )'
        ]
    }
    script = scriptOptions.get( scriptExt )
    if not script: raise Exception( "Invalid Script Type!" )    
    return ExecutableScript( "openTextFile", extension=scriptExt, script=script,
                             replacements={ "fileName":fileName } ) 

f = configFactory  = ConfigFactory()
f.productName      = "Hello Script Resources Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloScriptResources"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.distResources    = ["../hello_world_tk/LICENSE.TXT"]
f.entryPointScript = openTextFileScript( ExecutableScript.BATCH_EXT, 
                                         "LICENSE.TXT" )
 
p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True,
                                  isZipped=False )
p.isExeTest = True
p.run()       

