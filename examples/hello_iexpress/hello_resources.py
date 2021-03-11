from distbuilder import( IExpressPackageProcess, ConfigFactory,
                         ExecutableScript, iExpressResPath, baseFileName )

IS_EMBEDDED = True
SCRIPT_TYPE = ExecutableScript.POWERSHELL_EXT

LICENSE_FILE_PATH = "../hello_world_tk/LICENSE.TXT"

def openTextFileScript( scriptType, isEmbedded, fileName ):
    scriptOptions = {
          ExecutableScript.BATCH_EXT : [ 
            r'start "Message" /wait cmd /c "echo Resource: {filePath} & pause"'              
          , r'"%windir%\system32\notepad.exe" "{filePath}"'
        ]
        , ExecutableScript.POWERSHELL_EXT : [
            r'Add-Type -AssemblyName PresentationCore,PresentationFramework'
          , r'[System.Windows.MessageBox]::Show("Resource: {filePath}")'            
          , r'Start-Process -Wait -FilePath "$env:windir\system32\notepad.exe" ' 
                r'-ArgumentList "{filePath}"'
        ]            
        , ExecutableScript.VBSCRIPT_EXT: [
              r'const nShowWindow=1, bWait=True'
            , r'Dim sFilePath : sFilePath = {filePath}'
            , r'MsgBox "Resource: " & sFilePath'
            , r'Dim oShell : Set oShell = CreateObject( "WScript.Shell" )'
            , r'oShell.Run '
                r'"""%windir%\system32\notepad.exe"" """ & sFilePath & """", '
                r'nShowWindow, bWait'
        ]
    }
    script = scriptOptions.get( scriptType )     
    if not script: raise Exception( "Invalid Script Type!" )
    return ExecutableScript( "openTextFile", extension=scriptType, 
        script=script, replacements={
        # Note: iExpressResPath resolves the absolute path to the resource.
        # Referring to the path by the file name alone, would imply it is found  
        # within the current working directory, i.e. the resource is in the 
        # directory where the exe resides.          
        "filePath" : iExpressResPath( scriptType, fileName, isEmbedded ) 
    }) 

f = configFactory  = ConfigFactory()
f.productName      = "Hello Script Resources Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloScriptResources"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = openTextFileScript( SCRIPT_TYPE, 
                                         IS_EMBEDDED, 
                                         baseFileName( LICENSE_FILE_PATH ) )
if not IS_EMBEDDED: 
    f.distResources = [ LICENSE_FILE_PATH ]
 
class BuildProcess( IExpressPackageProcess ):
    def onIExpressConfig(self, cfg):
        if IS_EMBEDDED:
            cfg.sourceDir = "../hello_world_tk/" 
            cfg.embeddedResources = [ LICENSE_FILE_PATH ]

p = BuildProcess( configFactory, isDesktopTarget=True, 
                  isZipped=(not IS_EMBEDDED) )
p.isExeTest=True 
p.run()       
