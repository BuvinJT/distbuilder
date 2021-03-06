from distbuilder import( WinScriptToBinPackageProcess, ConfigFactory,
                         ExecutableScript )

def openTextFileScript( scriptExt, fileName ):
    scriptOptions = {
          ExecutableScript.BATCH_EXT : 
            'echo. > "%userprofile%\Desktop\{fileName}"'
        , ExecutableScript.PS_EXT :
            r'Start-Process -FilePath "notepad" -ArgumentList "{fileName}"'            
        , ExecutableScript.VBS_EXT: [
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
f.entryPointScript = openTextFileScript( ExecutableScript.VBS_EXT, 
                                         "LICENSE.TXT" )
 
p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True,
                                  isZipped=False )
p.isExeTest = True
p.run()       

