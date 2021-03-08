from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport

__IEXPRESS_TMPLT=(
r"""
;@echo off

;set "SOURCE_PATH={srcPath}"
;set "TARGET_PATH={destPath}"

;for %%I in ("%TARGET_PATH%") do set "target.exe=%%~I"
;for %%I in ("%SOURCE_PATH%") do set "script_file=%%~fI"
;for %%I in ("%SOURCE_PATH%") do set "script_name=%%~nxI"
;for %%I in ("%SOURCE_PATH%") do set "script_dir=%%~dpI"

;copy /y "%~f0" "%temp%\\2exe.sed" >nul

;(echo()>>"%temp%\\2exe.sed"
;(echo(AppLaunched={command})>>"%temp%\\2exe.sed"
;(echo(TargetName="%target.exe%")>>"%temp%\\2exe.sed"

;(echo(FILE0="%script_name%")>>"%temp%\\2exe.sed"
{resFileNames}

;(echo([SourceFiles])>>"%temp%\\2exe.sed"
;(echo(SourceFiles0="%script_dir%")>>"%temp%\\2exe.sed"
{resDirPaths}

;(echo([SourceFiles0])>>"%temp%\\2exe.sed"
;(echo(%%FILE0%%=)>>"%temp%\\2exe.sed"
{resFileTree}

;iexpress /n /q /m %temp%\\2exe.sed

;del /q /f "%temp%\\2exe.sed"
;{removeSrc}
;exit /b 0

[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=1
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
""")

__FILE_NAME_TMPLT        = ';(echo(FILE{0}="{1}")>>"%temp%\\2exe.sed"\n'
__DIR_PATH_TMPLT         = ';(echo(SourceFiles{0}="{1}")>>"%temp%\\2exe.sed"\n'
__DIR_TREE_HEADER_TMPLT  = ';(echo([SourceFiles{0}])>>"%temp%\\2exe.sed"\n'
__FILE_TREE_HEADER_TMPLT = ';(echo(%%FILE{0}%%=)>>"%temp%\\2exe.sed"\n'

__DEFAULT_SCRIPT_NAME = "iexpress-build"

__CMDS={ ExecutableScript.BATCH_EXT      : 'cmd.exe /c "%script_name%"'
       , ExecutableScript.POWERSHELL_EXT : ('powershell.exe '
            '-ExecutionPolicy Bypass -InputFormat None -File "%script_name%"' )
       , ExecutableScript.VBSCRIPT_EXT   : 'cscript.exe "%script_name%"'
       }

__DEL_SRC_TMPT = 'del /q /f "%s"'  

__EMBEDDED_RES_PATH_TMPLTS={ 
         ExecutableScript.BATCH_EXT      : '%RES_DIR%\\{0}'
       , ExecutableScript.POWERSHELL_EXT : '$RES_DIR\\{0}' 
       , ExecutableScript.VBSCRIPT_EXT   : '(RES_DIR & "\\{0}")'
       }
__EXTERNAL_RES_PATH_TMPLTS={ 
         ExecutableScript.BATCH_EXT      : '%THIS_DIR%\\{0}'
       , ExecutableScript.POWERSHELL_EXT : '$THIS_DIR\\{0}' 
       , ExecutableScript.VBSCRIPT_EXT   : '(THIS_DIR & "\\{0}")'
       }
def iExpressResPath( scriptExt, path, isEmbedded ):
    if path is None: raise DistBuilderError( "Path cannot be None" )
    try:
        if path[0]=='\\': path[1:]
    except: path = ""    
    return( __EMBEDDED_RES_PATH_TMPLTS[scriptExt].format( path )
            if isEmbedded else
            __EXTERNAL_RES_PATH_TMPLTS[scriptExt].format( path ) )

def _IExpressScript( srcPath, destPath, isSrcRemoved=False, name=None,
                     embeddedResources=None, sourceDir=None ):            
    command = __CMDS.get( ExecutableScript.typeOf( srcPath ) )
    if command is None: 
        raise DistBuilderError( "File type not supported: %s" % (srcPath,) )      
    
    if name is None: name = __DEFAULT_SCRIPT_NAME
    removeSrc = __DEL_SRC_TMPT % (srcPath,) if isSrcRemoved else "" 
    
    resFileNames = ""
    resDirPaths = ""
    resFileTree = ""
    if embeddedResources is not None:

        srcFilesTreeEntries=[]
        if embeddedResources is not None:
            for res in embeddedResources:
                src, dest = util._toSrcDestPair( res, destDir=None, # None==relative to base
                                                 basePath=sourceDir )        
                if isFile( src ): 
                    srcDir   = dirPath( src )
                    fileName = baseFileName( src ) # flatten dest!                
                    srcFilesTreeEntries.append( (srcDir, fileName) )
                elif isDir( src ): 
                    pass # TODO!
                #else: printErr( 'Invalid path: "%s"' % (src,) )                                                    
        srcFilesTreeEntries.sort( key=itemgetter(0) ) 

        dirsListed=[]    
        filesListed=[]        
        for srcDir, fileName in srcFilesTreeEntries:
            filesListed.append( fileName )                 
            resFileNames += __FILE_NAME_TMPLT.format( len(filesListed), fileName )
            if srcDir not in dirsListed:
                dirsListed.append( srcDir )
                resDirPaths += __DIR_PATH_TMPLT.format( len(dirsListed), 
                                srcDir.replace( '\\', '\\\\' ) )                
                resFileTree += __DIR_TREE_HEADER_TMPLT.format( len(dirsListed) )
            resFileTree += __FILE_TREE_HEADER_TMPLT.format( len(filesListed) ) 
    
    return ExecutableScript( name, script=__IEXPRESS_TMPLT, replacements={
        "srcPath": srcPath, "destPath": destPath, 
        "resFileNames": resFileNames, "resDirPaths": resDirPaths, 
        "resFileTree": resFileTree,
        "command": command, "removeSrc": removeSrc } )
    
BATCH_IEXPRESS_EXE_INIT=(
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

POWERSHELL_IEXPRESS_EXE_INIT=(
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
    
VBSCRIPT_IEXPRESS_EXE_INIT=(
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

class IExpressConfig:

    initSnippets = { 
          ExecutableScript.BATCH_EXT      : BATCH_IEXPRESS_EXE_INIT
        , ExecutableScript.POWERSHELL_EXT : POWERSHELL_IEXPRESS_EXE_INIT
        , ExecutableScript.VBSCRIPT_EXT   : VBSCRIPT_IEXPRESS_EXE_INIT
    }

    def __init__( self ):
        self.name             = None
        self.sourceDir        = None
        
        self.entryPointScript = None
        self.scriptHeader     = None

        self.versionInfo      = None
        self.iconFilePath     = None

        self.scriptImports     = []
        self.embeddedResources = []

        self.distResources    = []
        self.distDirs         = [] 
        
        self.destDirPath      = None 

def batchScriptToExe( name=None, entryPointScript=None,  iExpressConfig=None,                                     
                      distResources=None, distDirs=None ):
    return _scriptToExe( name, entryPointScript, iExpressConfig,                                     
                         distResources, distDirs )

def powerShellScriptToExe( name=None, entryPointScript=None,  iExpressConfig=None,                                     
                           distResources=None, distDirs=None ):
    return _scriptToExe( name, entryPointScript, iExpressConfig,                                     
                         distResources, distDirs )

def vbScriptToExe( name=None, entryPointScript=None,  iExpressConfig=None,                                     
                   distResources=None, distDirs=None ):
    return _scriptToExe( name, entryPointScript, iExpressConfig,                                     
                         distResources, distDirs )
        
def _scriptToExe( name=None, entryPointScript=None, iExpressConfig=None,                                     
                  distResources=None, distDirs=None ):
    ''' returns: (binDir, binPath) '''   
    
    if not IS_WINDOWS: util._onPlatformErr()   

    if distResources is None: distResources=[]
    if distDirs is None: distDirs=[]
     
    # Resolve IExpressConfig and the overlapping parameters passed directly
    # (IExpressConfig values are given priority)    
    if iExpressConfig is None: 
        iExpressConfig = IExpressConfig()
        iExpressConfig.name             = name
        iExpressConfig.entryPointScript = entryPointScript
        iExpressConfig.distResources    = distResources
        iExpressConfig.distDirs         = distDirs
    else :
        name             = iExpressConfig.name   
        entryPointScript = iExpressConfig.entryPointScript
        distResources    = iExpressConfig.distResources
        distDirs         = iExpressConfig.distDirs             
    
    # Verify the required parameters are present    
    if not iExpressConfig.name :         
        raise DistBuilderError( "Binary name is required" )
    if not iExpressConfig.entryPointScript : 
        raise DistBuilderError( "Binary entry point is required" )
    
    script = entryPointScript 
    isOnTheFly = isinstance( script, ExecutableScript )
    scriptPath =( absPath( script.filePath(), 
                    basePath=iExpressConfig.sourceDir )
                  if isOnTheFly else script )

    if isOnTheFly:
        iExpressConfig.scriptHeader = IExpressConfig.initSnippets.get( 
                                            script.extension ) 
        if iExpressConfig.scriptHeader: 
            script.script = iExpressConfig.scriptHeader + script.script
        script.write()

    # auto assign some iExpressConfig values        
    destDirPath = joinPath( THIS_DIR, iExpressConfig.name ) 
    destPath= normBinaryName( joinPath( destDirPath, iExpressConfig.name ), 
                              isPathPreserved=True )
    iExpressConfig.destDirPath = destDirPath
        
    __runIExpress( scriptPath, destPath, 
        iExpressConfig.scriptImports + iExpressConfig.embeddedResources,
        iExpressConfig.sourceDir )
    
    if isOnTheFly: script.remove()
            
    embedExeVerInfo( destPath, iExpressConfig.versionInfo )        
    if iExpressConfig.iconFilePath: 
        embedExeIcon( destPath, absPath( 
            iExpressConfig.iconFilePath,
            basePath=iExpressConfig.sourceDir ) )
            
    # Add additional distribution resources        
    for res in iExpressConfig.distResources:
        src, dest = util._toSrcDestPair( res, destDir=destDirPath,
                            basePath=iExpressConfig.sourceDir )
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

def __runIExpress( scrScriptPath, destExePath, embeddedResources, sourceDir ):        
    scrScriptPath = absPath( scrScriptPath )
    destExePath = absPath( normBinaryName( destExePath,isPathPreserved=True ) )    
    script = _IExpressScript( scrScriptPath, destExePath, 
                embeddedResources=embeddedResources, sourceDir=sourceDir )
    script._execute( isOnTheFly=True, isDebug=True )
    if not isFile( destExePath ):
        raise DistBuilderError( "Failed to create executable: %s" %
                                (destExePath,) )
