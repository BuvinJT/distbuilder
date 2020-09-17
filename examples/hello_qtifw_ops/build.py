from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, QtIfwKillOp, ExecutableScript, \
        joinPath,QT_IFW_HOME_DIR, IS_WINDOWS

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

EXAMPLE_FILEPATH = joinPath( QT_IFW_HOME_DIR, "distbuilder-example.dat" )

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):    
            
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
        
        def addKillOps( pkg ):
            pkg.pkgScript.killOps += [ QtIfwKillOp( pkg ) ]
        
        pkg = cfg.packages[0]            
        addNativeScriptOps( pkg )
        addKillOps( pkg )
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       