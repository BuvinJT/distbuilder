from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp, ExecutableScript, \
        joinPath, printErr, QT_IFW_HOME_DIR, IS_WINDOWS, IS_MACOS

f = configFactory  = ConfigFactory()
f.productName      = "Hello Custom Installer Ops Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwOpsSetup"

# SET A DEMO OPTION TO TEST A GIVEN SCRIPT TYPE
(SHELL, VBSCRIPT, POWERSHELL, APPLESCRIPT) = range(4)
DEMO_OPTION = POWERSHELL

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):    

        def addExternalOps( pkg ):                    

            # Short 'n sweet one liner shell commands
            # By default, an "ExecutableScript" is run as **Batch** on Windows 
            # (i.e. literally vs the slight nuance of "cmd command syntax"). 
            # On Linux or macOS, the *default* shell script interpreter ("sh") 
            # e.g. **Bash** is employed. (TODO: respect shebangs in QtIFW!)       
            def shellCreateFileOp( filePath ):                    
                createFileScript = ExecutableScript( "createFile", script=(
                    'echo. > "%s"' % (filePath,) if IS_WINDOWS else
                    'touch "%s"'  % (filePath,) ) )
                removeFileScript = ExecutableScript( "removeFile" , script=( 
                    'del /q "%s"' % (filePath,) if IS_WINDOWS else
                    'rm "%s"'  % (filePath,) ) )                        
                return QtIfwExternalOp( script=createFileScript, 
                                  uninstScript=removeFileScript )
    
            # The PowerShell equivalent 
            def powerShellCreateFileOp( filePath ):
                if not IS_WINDOWS: 
                    printErr( "PowerShell scripts are not INHERTENTLY "
                              "supported by this platform!", isFatal=True )                         
                createFileScript = ExecutableScript( 
                    "createFile", extension="ps1", script=(
                    "New-Item '%s'" % (filePath,) ))
                removeFileScript = ExecutableScript( 
                    "removeFile" , extension="ps1", script=( 
                    "Remove-Item '%s'" % (filePath,) ))                        
                return QtIfwExternalOp( script=createFileScript, 
                                  uninstScript=removeFileScript )
    
            # A more robust illustration of the same operations written in VBScript.
            # Note: The stdout / stderr messages will appear in the installer log, 
            # and in the verbose / detailed output.
            # If an error code is returned, QtIFW will alert the user, allowing them 
            # to terminate the process, retry it, or ignore it.   
            def vbScriptCreateFileOp( filePath ):        
                if not IS_WINDOWS: 
                    printErr( "VBScript is not supported by this platform!", 
                              isFatal=True )                                 
                createFileScript = ExecutableScript( 
                    "createFile", extension="vbs", script=(
"""
On Error Resume Next
Const ERROR_CODE=1
Set oFSO = CreateObject("Scripting.FileSystemObject")
Set oFile = oFSO.CreateTextFile("{0}")
If oFSO.FileExists("{0}") Then
    WScript.StdOut.WriteLine "Created: {0}"
Else
    WScript.StdErr.WriteLine "Could not create: {0}"
    WScript.Quit ERROR_CODE
End If
""" ).format(filePath) )
                removeFileScript = ExecutableScript( 
                    "removeFile", extension="vbs", script=(
"""
On Error Resume Next
Const ERROR_CODE=1
Set oFSO = CreateObject("Scripting.FileSystemObject")
oFSO.DeleteFile "{0}"
If oFSO.FileExists("{0}") Then
    WScript.StdErr.WriteLine "Could not remove: {0}"
    WScript.Quit ERROR_CODE
Else
    WScript.StdOut.WriteLine "Removed: {0}" 
End If
""" ).format(filePath) )
                return QtIfwExternalOp( script=createFileScript, 
                                  uninstScript=removeFileScript )
            
            # An AppleScript equivalent (for macOS)
            def appleScriptCreateFileOp( filePath ): 
                if not IS_MACOS:
                    printErr( "AppleScript is not supported by this platform!", 
                              isFatal=True )                                 
                createFileScript = ExecutableScript( 
                    "createFile", extension="scpt", script=(
"""
set exampleFile to open for access "{0}" with write permission
close access exampleFile
""" ).format(filePath) )
                removeFileScript = ExecutableScript( 
                    "removeFile" , extension="scpt", script=( 
"""
tell application "Finder"
    delete file "{0}"
end tell
""" ).format(filePath) )
                return QtIfwExternalOp( script=createFileScript, 
                                  uninstScript=removeFileScript )                

            filePath = joinPath( QT_IFW_HOME_DIR, "distbuilder-example.dat" )
            genOp = { SHELL:       shellCreateFileOp
                    , POWERSHELL:  powerShellCreateFileOp
                    , VBSCRIPT:    vbScriptCreateFileOp
                    , APPLESCRIPT: appleScriptCreateFileOp
                    }
            pkg.pkgScript.externalOps += [ genOp[ DEMO_OPTION ]( filePath ) ]        
        
        # TO TEST A KILL OP, THE TARGET PROGRAM MUST BE RUNNING 
        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]
        
        pkg = cfg.packages[0]            
        addExternalOps( pkg )
        addKillOps( pkg )
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       