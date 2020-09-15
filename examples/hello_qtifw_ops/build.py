from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp as IfwExOp, ExecutableScript, \
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

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):    

        #def addCustomOperations( cfg ):
        #    cfg.packages[0].pkgScript.customOperations = None
            
        def addExternalOperations( cfg ):        
            filePath = joinPath( QT_IFW_HOME_DIR, "distbuilder-ops-test.txt" ) 
            createFileScript = ExecutableScript( "createFile", script=(
                'echo. > "%s"' % (filePath,) if IS_WINDOWS else
                'touch "%s"'  % (filePath,) ) )
            removeFileScript = ExecutableScript( "removeFile" , script=( 
                'del /q "%s"' % (filePath,) if IS_WINDOWS else
                'rm "%s"'  % (filePath,) ) )                        
            cfg.packages[0].pkgScript.externalOps += [ 
                IfwExOp( script=createFileScript, 
                   uninstScript=removeFileScript )
            ]
        
        #addCustomOperations( cfg )
        addExternalOperations( cfg )
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       