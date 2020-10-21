from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp, ExecutableScript, IS_WINDOWS, \
        QT_IFW_DESKTOP_DIR

f = configFactory  = ConfigFactory()
f.productName      = "Hello Installer Conveniences Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwConveniencesSetup"
 
class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):            

        # TO TEST KILL OPS, THE TARGET PROGRAM MUST BE 
        # RUNNING WHEN INSTALL/UNINSTALL PROCESS IS BEGUN            
        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]

        # TO TEST / CONFIRM FUNCTIONALITY, REBOOT POST INSTALL  
        def addLaunchOnStartupOp( pkg ):
            # Notable CreateStartupEntry option to try: isAllUsers=True
            pkg.pkgScript.externalOps += [                                 
                QtIfwExternalOp.CreateStartupEntry( pkg ) ] 

        if IS_WINDOWS:
            
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
        
        pkg = cfg.packages[0]
        addKillOps( pkg ) 
        addLaunchOnStartupOp( pkg )                        
        if IS_WINDOWS: 
            addCreateExeFromBatch( pkg )
            addCreateExeFromPowerShell( pkg )
            addCreateExeFromVbs( pkg )               
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       