var SUCCESS_CODE = 0;
var ERROR_CODE   = 1;
var FILE_NAME    = "distbuilder_js_example.txt";

var nRetCode;
var oShell = WScript.CreateObject( "WScript.Shell" );
var oFSO   = WScript.CreateObject( "Scripting.FileSystemObject" );

var sDesktopPath = oShell.SpecialFolders( "Desktop" );
var sFilePath    = oFSO.BuildPath( sDesktopPath, FILE_NAME );

var oFile = oFSO.CreateTextFile( sFilePath );
oFile.WriteLine( "Hello World!" );
oFile.Close();
oFile = null;

if( oFSO.FileExists( sFilePath ) ){
    WScript.StdOut.WriteLine( "Created: " + sFilePath ); 
    oShell.Popup( "Created: " + sFilePath, 0, "Success", 0x0 + 0x40 ); // ok + info
    nRetCode = SUCCESS_CODE;
}
else {
    WScript.StdErr.WriteLine( "Could not create: " + sFilePath );
    oShell.Popup( "Could not create: " + sFilePath, 0, "Error", 0x0 + 0x10 ); // ok + stop    
    nRetCode = ERROR_CODE;    
}

oShell = null;
oFSO   = null;
WScript.Quit( nRetCode );
