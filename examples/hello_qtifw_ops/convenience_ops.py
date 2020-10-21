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

        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]

        def addLaunchOnStartupOp( pkg ):
            pkg.pkgScript.externalOps += [ 
                                # Notable option: isAllUsers=True
                QtIfwExternalOp.CreateStartupEntry( pkg ) ] 

        if IS_WINDOWS:
            def addCreateExeFromBatch( pkg ):
                pkg.pkgScript.externalOps += [
                    QtIfwExternalOp.CreateExeFromScript( 
                        ExecutableScript( "NotepadLauncherBat", script=(
                            'start "" notepad '
                            '"@TargetDir@\InstallationLog.txt"' )), 
                        {"companyName":configFactory.companyLegalName}, 
                        configFactory.iconFilePath,
                        targetDir=QT_IFW_DESKTOP_DIR ) ]

            def addCreateExeFromPowerShell( pkg ):
                pkg.pkgScript.externalOps += [
                    QtIfwExternalOp.CreateExeFromScript( 
                        ExecutableScript( "NotepadLauncherPs",  extension="ps1", 
                            script=('Start-Process -FilePath "notepad" '
                                    '-ArgumentList "@TargetDir@\InstallationLog.txt"') ), 
                        {"companyName":configFactory.companyLegalName}, 
                        configFactory.iconFilePath,
                        targetDir=QT_IFW_DESKTOP_DIR ) ]

            def addCreateExeFromVbs( pkg ):
                pkg.pkgScript.externalOps += [
                    QtIfwExternalOp.CreateExeFromScript( 
                        ExecutableScript( "NotepadLauncherVbs",  extension="vbs", 
                            script=(
"""
Set oShell = WScript.CreateObject("WScript.Shell")
oShell.Run "notepad ""@TargetDir@\InstallationLog.txt"" "
Set oShell = Nothing
""" )), 
                        {"companyName":configFactory.companyLegalName}, 
                        configFactory.iconFilePath,
                        targetDir=QT_IFW_DESKTOP_DIR ) ]

        
        pkg = cfg.packages[0]

        # TO TEST KILL OPS, THE TARGET PROGRAM MUST BE 
        # RUNNING WHEN INSTALL/UNINSTALL PROCESS IS BEGUN            
        addKillOps( pkg ) 

        # TO TEST / CONFIRM FUNCTIONALITY, REBOOT POST INSTALL  
        addLaunchOnStartupOp( pkg )        
                
        if IS_WINDOWS: 
            addCreateExeFromBatch( pkg )
            addCreateExeFromPowerShell( pkg )
            addCreateExeFromVbs( pkg )               
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       