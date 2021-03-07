from distbuilder import( WinScriptToBinInstallerProcess, ConfigFactory,
                         ExecutableScript )

f = configFactory  = ConfigFactory()
f.productName      = "Hello Windows Script Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWinScript"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.distResources    = ["../hello_world_tk/LICENSE.TXT"]
f.entryPointScript = ExecutableScript( "openTextFile", script=( 
    r'start "" "%windir%\system32\notepad.exe" "LICENSE.TXT"' ) )
f.setupName        = "HelloWinScriptSetup"
 
p = WinScriptToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       

