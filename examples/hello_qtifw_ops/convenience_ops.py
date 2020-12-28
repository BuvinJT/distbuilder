from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp, ExecutableScript, \
        IS_WINDOWS, IS_MACOS, QT_IFW_DESKTOP_DIR

f = configFactory  = ConfigFactory()
f.productName      = "Hello Installer Conveniences Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.distResources    = ["../hello_world/LICENSE.TXT"]
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwConveniencesSetup"
 
class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):            

        # TO TEST KILL OPS, THE TARGET PROGRAM MUST BE 
        # RUNNING WHEN INSTALL/UNINSTALL PROCESS IS BEGUN            
        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]

        if IS_WINDOWS:
            # These exes are created on the fly, by the installer!  
            # This feature is currently only supported on the Windows 
            # implementation of the library.
            
            def addCreateExeFromScript( pkg, name, ext, script ):
                pkg.pkgScript.externalOps += [
                    QtIfwExternalOp.CreateExeFromScript( 
                        ExecutableScript( name, extension=ext, script=script ), 
                        configFactory.exeVersionInfo(), 
                        configFactory.iconFilePath,
                        targetDir=QT_IFW_DESKTOP_DIR ) ]
                            
            def addCreateExeFromBatch( pkg ):
                addCreateExeFromScript( pkg, "InstallLogViewer_BAT", "bat", 
                    'start "" notepad "@TargetDir@\InstallationLog.txt"' )
                
            def addCreateExeFromPowerShell( pkg ):
                addCreateExeFromScript( pkg, "InstallLogViewer_PS", "ps1", 
                    'Start-Process -FilePath "notepad" '
                        '-ArgumentList "@TargetDir@\InstallationLog.txt"' ) 

            def addCreateExeFromVbs( pkg ):
                addCreateExeFromScript( pkg, "InstallLogViewer_VBS", "vbs", [ 
                    'Set oShell = WScript.CreateObject("WScript.Shell")',
                    'oShell.Run "notepad ""@TargetDir@\InstallationLog.txt"""',
                    'Set oShell = Nothing'
                ])  
        
            def addUninstallWindowsApp( pkg ):
                # This example app must be installed to truly test this!                
                APP_NAME = "Hello World Tk Example"
                pkg.pkgScript.externalOps += [ 
                    QtIfwExternalOp.UninstallWindowsApp( 
                        QtIfwExternalOp.ON_INSTALL,
                        APP_NAME, arguments=[], 
                        isHidden=True, 
                        isSynchronous=False,
                        isAutoBitContext=False,
                        isSuccessOnNotFound=True ) ]

        def addRunProgramOp( pkg ):
            if IS_WINDOWS: progPath = "notepad"                
            elif IS_MACOS: progPath = "TextEdit"                  
            else         : progPath = "gedit"                                                
            args = [ "@TargetDir@\LICENSE.TXT" ]
            pkg.pkgScript.externalOps += [
                QtIfwExternalOp.RunProgram(
                    QtIfwExternalOp.ON_INSTALL,
                    progPath, args,
                    # note: if you hide this, you'll need to kill the process
                    # manually in this demo context via kill commands, or the
                    # Windows task manger etc.!                      
                    isHidden=False,
                    # note: if isSynchronous is True, the installer will block 
                    # mid install operations in this demo until you close the 
                    # text viewer... 
                    isSynchronous=False, 
                    isElevated=False )
                ]    
        
        pkg = cfg.packages[0]
        addKillOps( pkg ) 
        if IS_WINDOWS:            
            addCreateExeFromBatch( pkg )
            addCreateExeFromPowerShell( pkg )
            addCreateExeFromVbs( pkg )       
            addUninstallWindowsApp( pkg )        
        addRunProgramOp( pkg )
            
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       