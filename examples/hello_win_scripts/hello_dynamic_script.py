from distbuilder import( WinScriptToBinPackageProcess, ConfigFactory, 
                         ExecutableScript )

# SET A DEMO OPTION TO TEST A GIVEN SCRIPT TYPE
(BATCH, POWERSHELL, VBSCRIPT) = range(3)
DEMO_OPTION = BATCH

def demoScript( scriptType ):
    if scriptType==BATCH:       
        ext      = "bat"
        script   = 'echo. > "%userprofile%\Desktop\{fileName}"'
        fileName = "distbuilder_bat_example.txt"
    elif scriptType==POWERSHELL:
        ext = "ps1"
        script = [
              '$DesktopPath = [Environment]::GetFolderPath( "Desktop" )'
            , '$FilePath    = Join-Path $DesktopPath {fileName}'
            , 'New-Item $FilePath'
        ]
        fileName = "distbuilder_ps1_example.txt" 
    elif scriptType==VBSCRIPT:
        ext = "vbs"
        script =[ 
              'Set oShell   = CreateObject( "WScript.Shell" )'
            , 'Set oFSO     = CreateObject( "Scripting.FileSystemObject" )'
            , 'sDesktopPath = oShell.SpecialFolders( "Desktop" )'
            , 'sFilePath    = oFSO.BuildPath( sDesktopPath, "{fileName}" )'
            , 'oFSO.CreateTextFile( sFilePath )' 
        ]
        fileName = "distbuilder_vbs_example.txt"
    else : raise Exception( "Invalid Script Type!" )    
    return ExecutableScript( "createFile", extension=ext, script=script,
                             replacements={ "fileName":fileName } ) 

f = configFactory  = ConfigFactory()
f.productName      = "Hello Dynamic Windows Script Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloDynamicWinScript"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = demoScript( DEMO_OPTION )

p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True )
p.run()       

