from distbuilder import( WinScriptToBinPackageProcess, ConfigFactory,
                         ExecutableScript )

f = configFactory  = ConfigFactory()
f.productName      = "Hello Script Resources Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloScriptResources"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.distResources    = ["../hello_world_tk/LICENSE.TXT"]
f.entryPointScript = "test.vbs"
f.entryPointScript = ExecutableScript( "openLicense", extension="vbs", script=(
r''' 
Dim oShell : Set oShell = CreateObject( "WScript.Shell" )
oShell.Exec( "%ComSpec% /c start """" ""%windir%\system32\notepad.exe"" ""{fileName}""" )
'''), replacements={"fileName":"LICENSE.TXT"} )
 
p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True,
                                  isZipped=False )
p.isExeTest = True
p.run()       

