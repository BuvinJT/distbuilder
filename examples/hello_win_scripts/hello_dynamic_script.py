from distbuilder import( WinScriptToBinPackageProcess, ConfigFactory, 
                         ExecutableScript )

DEMO_TYPE = ExecutableScript.BATCH_EXT

def createFileScript( scriptExt, fileName ):
    scriptOptions = {
          ExecutableScript.BATCH_EXT :    
            'echo. > "%userprofile%\Desktop\{fileName}"'
        , ExecutableScript.POWERSHELL_EXT: [
              '$DesktopPath = [Environment]::GetFolderPath( "Desktop" )'
            , '$FilePath    = Join-Path $DesktopPath {fileName}'
            , 'New-Item $FilePath'
        ]
        , ExecutableScript.VBSCRIPT_EXT: [ 
              'Set oShell   = CreateObject( "WScript.Shell" )'
            , 'Set oFSO     = CreateObject( "Scripting.FileSystemObject" )'
            , 'sDesktopPath = oShell.SpecialFolders( "Desktop" )'
            , 'sFilePath    = oFSO.BuildPath( sDesktopPath, "{fileName}" )'
            , 'oFSO.CreateTextFile( sFilePath )' 
        ]
    }    
    script = scriptOptions.get( scriptExt )
    if not script: raise Exception( "Invalid Script Type!" )        
    return ExecutableScript( "createFile", extension=scriptExt, script=script,
                             replacements={ "fileName":fileName } ) 

f = configFactory  = ConfigFactory()
f.productName      = "Hello Dynamic Windows Script Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloDynamicWinScript"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = createFileScript( DEMO_TYPE, 
                                       "distbuilder_dynamic_example.txt" )

p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True )
p.isExeTest = True
p.run()       

