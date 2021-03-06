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
' PROCESS INFO BOILER PLATER
Dim THIS_PID, PARENT_PID, EXE_PATH, THIS_DIR, oWMI, oCmd
Set oWMI = GetObject("winmgmts:root\cimv2")
Set oCmd = CreateObject("WScript.Shell").Exec("cmd.exe")
THIS_PID = oWMI.Get("Win32_Process.Handle='" & oCmd.ProcessID & "'").ParentProcessId
oCmd.Terminate
PARENT_PID = oWMI.Get("Win32_Process.Handle='" & THIS_PID & "'").ParentProcessId
EXE_PATH = oWMI.Get("Win32_Process.Handle='" & PARENT_PID & "'").ExecutablePath
THIS_DIR = CreateObject( "Scripting.FileSystemObject" ).GetParentFolderName( EXE_PATH )
Set oWMI = Nothing
Set oCmd = Nothing
' ---------------------------
Const FILE_NAME = "{fileName}"
Dim oShell, oFSO, sFilePath
Set oShell = CreateObject( "WScript.Shell" )
Set oFSO   = CreateObject( "Scripting.FileSystemObject" )
sFilePath = oFSO.BuildPath( THIS_DIR, FILE_NAME )
oShell.Exec( "cmd /c start """" ""%windir%\system32\notepad.exe"" """ & sFilePath & """" )
' ---------------------------
'''), replacements={"fileName":"LICENSE.TXT"} )
 
p = WinScriptToBinPackageProcess( configFactory, isDesktopTarget=True,
                                  isZipped=False )
p.isExeTest = True
p.run()       

