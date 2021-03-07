from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport

class WinScriptConfig:
    
    BAT_IEXPRESS_INIT=(
r'''
:: >>> IExpress Initialization <<<
@echo off
for %%t in ("%temp%\%~nx0.%random%%random%%random%%random%%random%.tmp") do > "%%~ft" (
    wmic process where "Name='wmic.exe' and CommandLine like '%%_%random%%random%%random%_%%'" get ParentProcessId
    for /f "skip=1" %%a in ('type "%%~ft"') do set "PID=%%a"
) & 2>nul del /q "%%~ft"
for %%t in ("%temp%\%~nx0.%random%%random%%random%%random%%random%.tmp") do > "%%~ft" (
    wmic process where "ProcessId='%PID%'" get ParentProcessId
    for /f "skip=1" %%a in ('type "%%~ft"') do set "PPID=%%a"
) & 2>nul del /q "%%~ft"
for %%t in ("%temp%\%~nx0.%random%%random%%random%%random%%random%.tmp") do > "%%~ft" (
    wmic process where "ProcessId='%PPID%'" get ExecutablePath
    for /f "delims=" %%a in ('type "%%~ft"') do set "EXE_PATH=%%a"
) & 2>nul del /q "%%~ft"
call :__dirname THIS_DIR "%EXE_PATH%"
goto :__skip_dirname
:__dirname <resultVar> <pathVar> 
( set "%~1=%~dp2" && exit /b )
:__skip_dirname
set "THIS_DIR=%THIS_DIR:~0,-1%"
set "RES_DIR=%CD%"
cd "%THIS_DIR%"
:: ------------------------------------------------ 
''')

    PS_IEXPRESS_INIT=(
r''' 
# >>> IExpress Initialization <<<
# $PID is implicitly defined!
$PPID     = (gwmi win32_process -Filter "processid='$PID'").ParentProcessId
$EXE_PATH = (Get-Process -Id $PPID -FileVersionInfo).FileName
$THIS_DIR = [System.IO.Path]::GetDirectoryName( $EXE_PATH )
$RES_DIR  = Get-Location
Set-Location $THIS_DIR
# ------------------------------------------------
''')
    
    VBS_IEXPRESS_INIT=(
r''' 
' >>> IExpress Initialization <<<
Dim PID, PPID, EXE_PATH, THIS_DIR, RES_DIR
sub IExpressInit()
    Dim oShell : Set oShell = CreateObject( "WScript.Shell" )
    Dim oFSO   : Set oFSO   = CreateObject( "Scripting.FileSystemObject" )
    Dim oWMI   : Set oWMI   = GetObject( "winmgmts:root\cimv2" )
    Dim oCmd   : Set oCmd   = CreateObject( "WScript.Shell" ).Exec( "%ComSpec%" )
    PID = oWMI.Get( "Win32_Process.Handle='" & oCmd.ProcessID & "'" ).ParentProcessId
    oCmd.Terminate
    PPID = oWMI.Get( "Win32_Process.Handle='" & PID & "'" ).ParentProcessId
    EXE_PATH = oWMI.Get( "Win32_Process.Handle='" & PPID & "'" ).ExecutablePath
    RES_DIR  = oShell.CurrentDirectory
    THIS_DIR = oFSO.GetParentFolderName( EXE_PATH )
    oShell.CurrentDirectory = THIS_DIR
End Sub
Call IExpressInit
' ------------------------------------------------
''')

    initSnippets = { ExecutableScript.BATCH_EXT      : BAT_IEXPRESS_INIT
                   , ExecutableScript.POWERSHELL_EXT : PS_IEXPRESS_INIT
                   , ExecutableScript.VBSCRIPT_EXT   : VBS_IEXPRESS_INIT
                   }

    def __init__( self ):
        self.name             = None
        self.sourceDir        = None
        
        self.entryPointScript = None
        self.scriptHeader     = None

        self.versionInfo      = None
        self.iconFilePath     = None

        self.distResources    = []
        self.distDirs         = [] 
        
        self.destDirPath      = None 
        
def winScriptToExe( name=None, entryPointScript=None, 
                    winScriptConfig=None,                                     
                    distResources=None, distDirs=None ):
    ''' returns: (binDir, binPath) '''   
    
    if not IS_WINDOWS: util._onPlatformErr()   

    if distResources is None: distResources=[]
    if distDirs is None: distDirs=[]
     
    # Resolve WinScriptConfig and the overlapping parameters passed directly
    # (PyInstallerConfig values are given priority)    
    if winScriptConfig is None: 
        winScriptConfig = WinScriptConfig()
        winScriptConfig.name             = name
        winScriptConfig.entryPointScript = entryPointScript
        winScriptConfig.distResources    = distResources
        winScriptConfig.distDirs         = distDirs
    else :
        name             = winScriptConfig.name   
        entryPointScript = winScriptConfig.entryPointScript
        distResources    = winScriptConfig.distResources
        distDirs         = winScriptConfig.distDirs             
    
    # Verify the required parameters are present    
    if not winScriptConfig.name :         
        raise DistBuilderError( "Binary name is required" )
    if not winScriptConfig.entryPointScript : 
        raise DistBuilderError( "Binary entry point is required" )
    
    script = entryPointScript 
    isOnTheFly = isinstance( script, ExecutableScript )
    scriptPath =( absPath( script.filePath(), 
                    basePath=winScriptConfig.sourceDir )
                  if isOnTheFly else script )

    if isOnTheFly:
        winScriptConfig.scriptHeader = WinScriptConfig.initSnippets.get( 
                                            script.extension ) 
        if winScriptConfig.scriptHeader: 
            script.script = winScriptConfig.scriptHeader + script.script
        script.write()

    # auto assign some winScriptConfig values        
    destDirPath = joinPath( THIS_DIR, winScriptConfig.name ) 
    destPath= normBinaryName( joinPath( destDirPath, winScriptConfig.name ), 
                              isPathPreserved=True )
    winScriptConfig.destDirPath = destDirPath
        
    __runIExpress( scriptPath, destPath )
    
    if isOnTheFly: script.remove()
            
    embedExeVerInfo( destPath, winScriptConfig.versionInfo )        
    if winScriptConfig.iconFilePath: 
        embedExeIcon( destPath, absPath( 
            winScriptConfig.iconFilePath,
            basePath=winScriptConfig.sourceDir ) )
        
    # TODO: Eliminate code duplication from py_installer.pyScriptToExe        
    # Add additional distribution resources        
    for res in winScriptConfig.distResources:
        src, dest = util._toSrcDestPair( res, destDir=destDirPath,
                            basePath=winScriptConfig.sourceDir )
        print( 'Copying "%s" to "%s"...' % ( src, dest ) )
        if isFile( src ) :
            destDir = dirPath( dest )
            if not exists( destDir ): makeDir( destDir )
            try: copyFile( src, dest ) 
            except Exception as e: printExc( e )
        elif isDir( src ):
            try: copyDir( src, dest ) 
            except Exception as e: printExc( e )
        else:
            printErr( 'Invalid path: "%s"' % (src,) )                            
    for d in distDirs:
        dirToMk = joinPath( destDirPath, d )
        print( '"Making directory "%s"...' % ( dirToMk ) )
        try: makeDir( dirToMk ) # works recursively
        except Exception as e: printExc( e )   
    print('')
            
    return dirPath( destPath ), destPath         

def __runIExpress( scrScriptPath, destExePath ):        
    from distbuilder.qt_installer import QtIfwExternalOp
    scrScriptPath = absPath( scrScriptPath )
    destExePath = absPath( normBinaryName( destExePath,isPathPreserved=True ) )    
    QtIfwExternalOp.Script2ExeScript( scrScriptPath, destExePath )._execute( 
        isOnTheFly=True, isDebug=True )
    if not isFile( destExePath ):
        raise DistBuilderError( "Failed to create executable: %s" %
                                (destExePath,) )
