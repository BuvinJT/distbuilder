from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp, ExecutableScript, IS_WINDOWS

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

        if IS_WINDOWS:
            def addCreateExeFromBatch( pkg ):
                pkg.pkgScript.externalOps += [
                    QtIfwExternalOp.CreateExeFromBatch( 
                        ExecutableScript( "NotepadLauncher", 
                                          script=('start "" notepad') ), 
                        {"companyName":configFactory.companyLegalName}, 
                        configFactory.iconFilePath ) ]

        def addLaunchOnStartupOp( pkg ):
            pkg.pkgScript.externalOps += [ 
                                # Notable option: isAllUsers=True
                QtIfwExternalOp.CreateStartupEntry( pkg ) ] 

        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]
        
        pkg = cfg.packages[0]
        
        if IS_WINDOWS: addCreateExeFromBatch( pkg )
                
        # TO TEST / CONFIRM FUNCTIONALITY, REBOOT POST INSTALL  
        addLaunchOnStartupOp( pkg )        
        
        # TO TEST KILL OPS, THE TARGET PROGRAM MUST BE 
        # RUNNING WHEN INSTALL/UNINSTALL PROCESS IS BEGUN            
        addKillOps( pkg ) 
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       