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
;(echo(AppLaunched={launchCmd})>>"%temp%\\2exe.sed"
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

__BATCH_IEXPRESS_EXE_INIT_TMPLT=(
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
{extractCmd}
cd "%THIS_DIR%"
:: ------------------------------------------------ 
''')

__POWERSHELL_IEXPRESS_EXE_INIT_TMPLT=(
r''' 
# >>> IExpress Initialization <<<
# $PID is implicitly defined!
$PPID     = (gwmi win32_process -Filter "processid='$PID'").ParentProcessId
$EXE_PATH = (Get-Process -Id $PPID -FileVersionInfo).FileName
$THIS_DIR = [System.IO.Path]::GetDirectoryName( $EXE_PATH )
$RES_DIR  = (Get-Location)
{extractCmd}
Set-Location $THIS_DIR
# ------------------------------------------------
''')
    
__VBSCRIPT_IEXPRESS_EXE_INIT_TMPLT=(
r''' 
' >>> IExpress Initialization <<<
' Option Explicit ' DISABLED to support 3rd party libraries 
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
    {extractCmd}
    oShell.CurrentDirectory = THIS_DIR
End Sub
Call IExpressInit

Const bVALIDATE_IMPORTS    = {isDebug}
Const bINJECT_LOGGING      = {isDebug}
Const bSHOW_32BIT_RELAUNCH = {isDebug}
Const sLOG_PATH            = "%temp%\vbDebug.log"
Const sRELAUNCH_ENV_VAR    = "__Relaunch"

Sub Import( sRelativeFilePath )    
    Dim oFs : Set oFs = CreateObject("Scripting.FileSystemObject")
    Dim sThisFolder : sThisFolder = oFs.GetParentFolderName( WScript.ScriptFullName )
    Dim sAbsFilePath : sAbsFilePath = oFs.BuildPath( sThisFolder, sRelativeFilePath )
    Dim sLibrary : sLibrary = oFs.OpenTextFile( sAbsFilePath ).readAll()
    if bVALIDATE_IMPORTS Then 
        Force32BitContext
        ValidateSource sLibrary
    End If        
    If bINJECT_LOGGING Then 
        InjectRoutineLogging sLibrary, _
            oFs.OpenTextFile( sAbsFilePath ), sRelativeFilePath
    End If
    ExecuteGlobal sLibrary
End Sub

Sub StartLogging()   
    Force32BitContext 
    If sLOG_PATH <> "" Then 
        Dim oShell: Set oShell = CreateObject( "WScript.Shell" )
        Dim sRelaunchVar: sRelaunchVar = "%" & sRELAUNCH_ENV_VAR & "%"
        Dim bIsRelaunch: bIsRelaunch = CBool( oShell.ExpandEnvironmentStrings( _
                                              sRelaunchVar ) <> sRelaunchVar )
        If Not bIsRelaunch Then Relaunch False, False
    End If
End Sub

Sub Force32BitContext()    
    Dim oShell: Set oShell = CreateObject( "WScript.Shell" )
    Dim Is32Bit: Is32Bit = CBool( oShell.ExpandEnvironmentStrings( _
                                  "%PROCESSOR_ARCHITECTURE%" ) = "x86" )
    If Not Is32Bit Then
        Dim nShow
        If bSHOW_32BIT_RELAUNCH Then
            nShow = 1
            WScript.StdErr.WriteLine "WARNING: Forced execution in 32 bit context"
        Else 
            nShow = 0        
        End If    
        Relaunch True, nShow 
    End If        
End Sub

Sub Relaunch( bForce32Bit, nShow )    
    Dim oShell: Set oShell = CreateObject( "WScript.Shell" )
    Dim ComSpec: ComSpec = "%ComSpec%"
    If bForce32Bit Then ComSpec = "%windir%\SysWOW64\cmd.exe"
    Dim sCmd: sCmd = """" & ComSpec & """ /c " & _
                     "set " & sRELAUNCH_ENV_VAR & "=1 & " & _
                     "cscript.exe """ & WScript.ScriptFullName & """"
    If sLOG_PATH <> "" Then 
        nShow = 0
        sCmd = sCmd + " > """ & sLOG_PATH & """ 2>&1"          
        WScript.Echo "Logging To: " & sLOG_PATH
    End if    
    Dim nExitCode: nExitCode = oShell.Run( sCmd, nShow, True )  
    WScript.Quit nExitCode
End Sub

Sub ValidateSource( ByRef sLibrary )
    On Error Resume Next
    Dim oSC : Set oSC = CreateObject("MSScriptControl.ScriptControl")
    With oSC
        .Language = "VBScript"
        .UseSafeSubset = False
        .AllowUI = False
        .AddCode sLibrary
    End With
    With oSC.Error
        If .Number <> 0 then
            WScript.Echo sAbsFilePath & "(" & .Line & "," & .Column & ")" & _
                " Microsoft VBScript compilation error: " & _
                "(" & .Number & ") " & .Description
            WScript.Quit 1
        End If
    End With
    On Error Goto 0
End Sub

Sub InjectRoutineLogging( ByRef sLibrary, ByRef oFile, sFilePath )
    sLibrary = ""        
    Dim sLine, sParseLine, sAppendLine, sPrependLine
    Dim bIsRoutineBody : bIsRoutineBody = False
    Dim sRoutineName   : sRoutineName = ""
    Dim aStartKeywords : aStartKeywords = Array( "SUB", "FUNCTION" )
    Dim aEndKeywords   : aEndKeywords   = Array( "END SUB", "END FUNCTION" )    
    Do Until oFile.AtEndOfStream
        sLine        = oFile.ReadLine            
        sParseLine   = Trim(sLine)            
        sPrependLine = ""
        sAppendLine  = ""                
        ' Find routine signature starts (and the save name)
        If sRoutineName = "" Then                                 
            For Each sKeyword In aStartKeywords                
                If Left( UCase(sParseLine), Len(sKeyword) ) = sKeyword Then
                    sParseLine = Right( sParseLine, _
                                        Len(sParseLine)-Len(sKeyword) )
                    sRoutineName = Trim(Split( sParseLine, "(" )(0))
                End If
            Next            
        End If                
        If sRoutineName <> "" Then            
            If Not bIsRoutineBody Then                   
                ' Find end of routine signature 
                ' (figuring in line continuations and eol comments)                
                ' Inject start log
                sParseLine = Trim(Split(sParseLine, "'")(0)) 
                If Right( sParseLine, 1 ) = ")" Then                    
                    sAppendLine = "WScript.Echo" & _
                        """Start " & sRoutineName & _
                        " (" & sFilePath & ")..." & """" & vbCrLF
                    bIsRoutineBody = True
                End If    
            Else                    
                ' Find routine end
                ' Inject end log 
                For Each sKeyword In aEndKeywords                
                    If Left( UCase(sParseLine), Len(sKeyword) ) = sKeyword Then
                        sPrependLine = "WScript.Echo ""...End " & _
                                        sRoutineName & " "" " 
                        sRoutineName = ""
                        bIsRoutineBody = False
                    End If
                Next                                        
            End If                            
        End If
        ' Append lines
        If sPrependLine <> "" Then sLibrary = sLibrary & sPrependLine & vbCrLF
        sLibrary = sLibrary & sLine & vbCrLF
        If sAppendLine  <> "" Then sLibrary = sLibrary & sAppendLine  & vbCrLF
    Loop        
End Sub
{startLogging}
' ------------------------------------------------
''')

__IEXRESS_EXE_INIT_TMPLTS = { 
      ExecutableScript.BATCH_EXT      : __BATCH_IEXPRESS_EXE_INIT_TMPLT
    , ExecutableScript.POWERSHELL_EXT : __POWERSHELL_IEXPRESS_EXE_INIT_TMPLT
    , ExecutableScript.VBSCRIPT_EXT   : __VBSCRIPT_IEXPRESS_EXE_INIT_TMPLT
}

__BATCH_EXTRACT_CAB_CMD_TMPLT =( 
r'''%windir%\system32\extrac32.exe "{0}" /e /l . 
del /q /f "{0}"''')
__POWERSHELL_EXTRACT_CAB_CMD_TMPLT =( 
r'''Start-Process -Wait -FilePath "$env:windir\system32\extrac32.exe" -ArgumentList '"{0}"','/e','/l','.'
Remove-Item "{0}"''')    
__VBSCRIPT_EXTRACT_CAB_CMD_TMPLT=( 
r'''If oFSO.FileExists( "{0}" ) Then 
    oShell.Run """%windir%\system32\extrac32.exe"" ""{0}"" /e /l .", 1, True
    oFSO.DeleteFile "{0}"
End If    
''')
                           

__EXTRACT_CMD_TMPLTS = { 
      ExecutableScript.BATCH_EXT      : __BATCH_EXTRACT_CAB_CMD_TMPLT
    , ExecutableScript.POWERSHELL_EXT : __POWERSHELL_EXTRACT_CAB_CMD_TMPLT
    , ExecutableScript.VBSCRIPT_EXT   : __VBSCRIPT_EXTRACT_CAB_CMD_TMPLT
}

__FILE_NAME_TMPLT        = ';(echo(FILE{0}="{1}")>>"%temp%\\2exe.sed"\n'
__DIR_PATH_TMPLT         = ';(echo(SourceFiles{0}="{1}")>>"%temp%\\2exe.sed"\n'
__DIR_TREE_HEADER_TMPLT  = ';(echo([SourceFiles{0}])>>"%temp%\\2exe.sed"\n'
__FILE_TREE_HEADER_TMPLT = ';(echo(%%FILE{0}%%=)>>"%temp%\\2exe.sed"\n'

__DEFAULT_SCRIPT_NAME = "iexpress-build"

__LAUNCH_CMDS={ ExecutableScript.BATCH_EXT : 'cmd.exe /c "%script_name%"'
       , ExecutableScript.POWERSHELL_EXT   : ('powershell.exe '
            '-ExecutionPolicy Bypass -InputFormat None -File "%script_name%"' )
       , ExecutableScript.VBSCRIPT_EXT     : 'cscript.exe "%script_name%"'
       }

__DEL_SRC_TMPT = 'del /q /f "%s"'  

__CAB_SOURCE_DIR_NAME    = "__res"
__EMBEDDED_CAB_FILE_NAME = "res"
__FLAT_EMBEDDING_WARNING = (
    'WARNING: IExpress only directly supports "flat" resource embedding.' 
    '(Use "isTwoStageEmbedding")'
    )


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
    launchCmd = __LAUNCH_CMDS.get( ExecutableScript.typeOf( srcPath ) )
    if launchCmd is None: 
        raise DistBuilderError( "File type not supported: %s" % (srcPath,) )      
           
    if name is None: name = __DEFAULT_SCRIPT_NAME
    removeSrc =( __DEL_SRC_TMPT % (srcPath.replace( '\\', '\\\\' ),) 
                 if isSrcRemoved else "" ) 
        
    resFileNames = ""
    resDirPaths = ""
    resFileTree = ""
    if embeddedResources is not None:

        fileNamesInTree = []
        srcFilesTreeEntries=[]
        if embeddedResources is not None:
            for res in embeddedResources:
                src = absPath( res, basePath=sourceDir )        
                if isFile( src ): 
                    srcDir   = dirPath( src )
                    fileName = baseFileName( src ) # flatten dest!
                    if fileName in fileNamesInTree:
                        printErr( __FLAT_EMBEDDING_WARNING +
                                  'Unique filenames are required '
                                  '(across ALL package sub directories)'
                                  ': "%s"' % (src,) )
                    else:          
                        fileNamesInTree.append( fileName )          
                        srcFilesTreeEntries.append( (srcDir, fileName) )
                elif isDir( src ): 
                    printErr( __FLAT_EMBEDDING_WARNING +
                              'Cannot embed a *directory*: '
                              ': "%s"' % (src,) )
                else: printErr( 'Invalid path: "%s"' % (src,) )
                                                                    
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
        "launchCmd": launchCmd, "removeSrc": removeSrc } )

class IExpressConfig:
    def __init__( self ):
        self.name             = None
        self.sourceDir        = None
                
        self.entryPointScript = None
        self.scriptHeader     = None
        self.isScriptDebug    = False

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

    destDirPath = joinPath( THIS_DIR, iExpressConfig.name ) 
    iExpressConfig.destDirPath = destDirPath
    destPath = normBinaryName( joinPath( destDirPath, iExpressConfig.name ), 
                               isPathPreserved=True )
    
    script = entryPointScript 
    isOnTheFly = isinstance( script, ExecutableScript )
    scriptPath =( absPath( script.filePath(), 
                    basePath=iExpressConfig.sourceDir )
                  if isOnTheFly else script )
    sourceDir = iExpressConfig.sourceDir
    embeddedResources =( iExpressConfig.scriptImports + 
                         iExpressConfig.embeddedResources )
    isDebug = iExpressConfig.isScriptDebug

    tempCabSrcDirPath   = None
    tempCabDestPath     = None
    isTwoStageEmbedding = False
    if embeddedResources is not None:
        for res in embeddedResources:
            src, dest = util._toSrcDestPair( res, destDir=destDirPath,
                                             basePath=sourceDir )
            isNestedDest = dirPath( relpath( dest, destDirPath ) ) != ""                     
            isTwoStageEmbedding = isDir( src ) or isNestedDest
            if isTwoStageEmbedding: break 
    if isTwoStageEmbedding:
        print( "Using 2 stage resource embedding..." ) 
        tempCabSrcDirPath = joinPath( destDirPath, __CAB_SOURCE_DIR_NAME )
        tempCabDestPath   = joinPath( destDirPath, __EMBEDDED_CAB_FILE_NAME )
        __copyResources( embeddedResources, None, tempCabSrcDirPath, sourceDir )                         
        if not isDebug:
            embeddedResources = [ 
                toCabFile( tempCabSrcDirPath, tempCabDestPath ) ]       

    if isOnTheFly:                
        iExpressConfig.scriptHeader = __IEXRESS_EXE_INIT_TMPLTS.get( 
                                            script.extension )
        if isTwoStageEmbedding and embeddedResources:
            extractCmd = __EXTRACT_CMD_TMPLTS.get( script.extension )
            if extractCmd: 
                extractCmd = extractCmd.format( 
                    baseFileName( embeddedResources[0] ), ) 
        else: extractCmd = ""        
        try: script.replacements["extractCmd"] = extractCmd
        except: script.replacements={"extractCmd": extractCmd}
        script.replacements["isDebug"] = str(isDebug)        
        if script.extension == ExecutableScript.VBSCRIPT_EXT:
            script.replacements["startLogging"] =( "StartLogging" 
                                            if isDebug else "" )                    
        if iExpressConfig.scriptHeader: 
            script.script = iExpressConfig.scriptHeader + script.script
        script.write()
        if isDebug: 
            filePath = script.filePath()
            if isTwoStageEmbedding:
                filePath = moveToDir( filePath, tempCabSrcDirPath )
            printErr( "Debug script left at: %s" % (filePath,), 
                      isFatal=True )
         
    __runIExpress( scriptPath, destPath, embeddedResources, sourceDir )

    if isDir( tempCabSrcDirPath ): removeDir( tempCabSrcDirPath )
    if isFile( tempCabDestPath ): removeFile( tempCabDestPath )
    
    if isOnTheFly: script.remove()
            
    embedExeVerInfo( destPath, iExpressConfig.versionInfo )        
    if iExpressConfig.iconFilePath: 
        embedExeIcon( destPath, absPath( 
            iExpressConfig.iconFilePath, basePath=sourceDir ) )

    __copyResources( distResources, distDirs, destDirPath,
                      iExpressConfig.sourceDir )
            
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

def __copyResources( resources, mkDirs, destDirPath, sourceDir ):
    for res in resources:
        src, dest = util._toSrcDestPair( res, destDir=destDirPath,
                                         basePath=sourceDir )
        print( 'Copying "%s" to "%s"...' % ( src, dest ) )
        if isFile( src ) :
            destDir = dirPath( dest )
            if not exists( destDir ): makeDir( destDir )
            try: copyFile( src, dest ) 
            except Exception as e: printExc( e )
        elif isDir( src ):
            try: copyDir( src, dest ) 
            except Exception as e: printExc( e )
        else: printErr( 'Invalid path: "%s"' % (src,) )         
    if mkDirs:
        for d in mkDirs:
            dirToMk = joinPath( destDirPath, d )
            print( '"Making directory "%s"...' % ( dirToMk ) )
            try: makeDir( dirToMk ) # works recursively
            except Exception as e: printExc( e )   
        print('')
    