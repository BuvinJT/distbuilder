from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, ExecutableScript as Script, \
        joinPath, toNativePath, QT_IFW_HOME_DIR, IS_WINDOWS

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
        
        def ops():
            fileName = "distbuilder-ops-test.txt"
            filePath = toNativePath( joinPath( QT_IFW_HOME_DIR, fileName ) )
            createCmd =( 'echo .> "%s"' % (filePath,) if IS_WINDOWS else
                         'touch "%s"'  % (filePath,) )
            removeCmd =( 'del /q "%s"' % (filePath,) if IS_WINDOWS else
                         'rm "%s"'  % (filePath,) )            
            createFileOp = QtIfwExternalOp( 
                      script=Script( "create",  script=createCmd ), 
                uninstScript=Script( "remove" , script=removeCmd )                     
            )                         
            return [ createFileOp ]        
    
        cfg.packages[0].pkgScript.externalOps = ops() 
         
        #script.customOperations = None
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       