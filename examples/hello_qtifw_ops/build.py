from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp, ExecutableScript, \
        joinPath, QT_IFW_HOME_DIR, IS_WINDOWS

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

# TODO: Add more!
(NATIVE, VBSCRIPT, POWERSCRIPT, APPLESCRIPT) = range(4)
DEMO_OPTION = VBSCRIPT 

EXAMPLE_FILEPATH = joinPath( QT_IFW_HOME_DIR, "distbuilder-example.dat" )

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):    
        
        # short 'n sweet one liner shell commands   
        def addNativeScriptOps( pkg ):                    
            createFileScript = ExecutableScript( "createFile", script=(
                'echo. > "%s"' % (EXAMPLE_FILEPATH,) if IS_WINDOWS else
                'touch "%s"'  % (EXAMPLE_FILEPATH,) ) )
            removeFileScript = ExecutableScript( "removeFile" , script=( 
                'del /q "%s"' % (EXAMPLE_FILEPATH,) if IS_WINDOWS else
                'rm "%s"'  % (EXAMPLE_FILEPATH,) ) )                        
            pkg.pkgScript.externalOps += [ 
                QtIfwExternalOp( script=createFileScript, 
                           uninstScript=removeFileScript )
            ]

        # robust demo
        def addVbScriptOps( pkg ):                                
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
""" ).format(EXAMPLE_FILEPATH) )
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
""" ).format(EXAMPLE_FILEPATH) )
            pkg.pkgScript.externalOps += [ 
                QtIfwExternalOp( script=createFileScript, 
                           uninstScript=removeFileScript )
            ]
        
        def addPowerScriptOps( pkg ): pass # TODO
        
        def addAppleScriptOps( pkg ): pass # TODO    
        
        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]
        
        pkg = cfg.packages[0]    
        if   DEMO_OPTION == NATIVE:      addNativeScriptOps( pkg )
        elif DEMO_OPTION == VBSCRIPT:    addVbScriptOps( pkg )
        elif DEMO_OPTION == POWERSCRIPT: addPowerScriptOps( pkg )
        elif DEMO_OPTION == APPLESCRIPT: addAppleScriptOps( pkg )
        addKillOps( pkg )
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       