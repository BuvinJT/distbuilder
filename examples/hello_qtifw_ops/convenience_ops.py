from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp

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

        def addLaunchOnStartupOp( pkg ):
            pkg.pkgScript.externalOps += [ 
                QtIfwExternalOp.CreateStartupEntry( pkg ) ]

        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]
        
        pkg = cfg.packages[0]
        # TO TEST ...
        addLaunchOnStartupOp( pkg )        
        # TO TEST KILL OPS, THE TARGET PROGRAM MUST BE LEFT RUNNING!            
        addKillOps( pkg ) 
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.isScriptDebugTestInstall = True
p.run()       