On Error Resume Next

Const SUCCESS_CODE = 0
Const ERROR_CODE   = 1
Const FILE_NAME    = "distbuilder_vbs_example.txt"

Dim oShell, oFSO, nRetCode
Set oShell = CreateObject( "WScript.Shell" )
Set oFSO   = CreateObject( "Scripting.FileSystemObject" )

Dim sDesktopPath, sFilePath
sDesktopPath = oShell.SpecialFolders( "Desktop" )
sFilePath    = oFSO.BuildPath( sDesktopPath, FILE_NAME )

Set oFile = oFSO.CreateTextFile( sFilePath )
oFile.WriteLine "Hello World!"
oFile.Close
Set oFile = Nothing

If oFSO.FileExists( sFilePath ) Then
    WScript.StdOut.WriteLine "Created: " & sFilePath
    MsgBox "Created: " & sFilePath, vbOKOnly+vbInformation, "Success"
    nRetCode = SUCCESS_CODE
Else
    WScript.StdErr.WriteLine "Could not create: " & sFilePath
    MsgBox "Could not create: " & sFilePath, vbOKOnly+vbCritical, "Error"
    nRetCode = ERROR_CODE    
End If

Set oShell = Nothing
Set oFSO   = Nothing
WScript.Quit nRetCode
