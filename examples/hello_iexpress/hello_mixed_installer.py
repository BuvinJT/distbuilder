from distbuilder import( RobustInstallerProcess, ConfigFactory,
                         ExecutableScript, findQtIfwPackage )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Mixed Source Types Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloMixedSourceSetup"

PY_CONFIG_KEY    = "py"
BATCH_CONFIG_KEY = "bat"

class BuildProcess( RobustInstallerProcess ):
    
    def onConfigFactory( self, key, f ):
        if key==PY_CONFIG_KEY: 
            f.productName      = "Hello World Tk Example"
            f.description      = "Tk Example"
            f.binaryName       = "HelloWorldTk"
            f.version          = (1,0,0,0)
            f.isGui            = True        
            f.sourceDir        = "../hello_world_tk"
            f.entryPointPy     = "hello.py"  
            f.iconFilePath     = "demo.ico"             
        elif key==BATCH_CONFIG_KEY: 
            f.productName      = "Hello Batch Popup Example"
            f.description      = "Batch Popup Example"
            f.binaryName       = "HelloBatchPopup"
            f.version          = (1,0,0,0)
            f.iconFilePath     = "../hello_world_tk/demo.ico" 
            f.entryPointScript = ExecutableScript( 
                "popup", extension=ExecutableScript.BATCH_EXT, script=(
                    r'start "Message" /wait cmd /c '
                        '"echo PWD: %CD% & echo RES: %RES_DIR% & pause"' ) )            

    def onQtIfwConfig( self, cfg ):     

        def defineComponentsOrder( pyPkg, batchPkg ):
            # Listed / installed in descending order 
            # (i.e. highest *priority* first)
            pyPkg.pkgXml.SortingPriority  = 10
            batchPkg.pkgXml.SortingPriority = 1
            
        def customizeFinishedPage( cfg, pyPkg ):
            # Explicitly enforce which package exe is "primary" 
            # and should be run post installation 
            cfg.configXml.setPrimaryContentExe( pyPkg )           
            
        pkgs     = cfg.packages
        pyPkg    = findQtIfwPackage( pkgs, PY_CONFIG_KEY )            
        batchPkg = findQtIfwPackage( pkgs, BATCH_CONFIG_KEY )        
        defineComponentsOrder( pyPkg, batchPkg )       
        customizeFinishedPage( cfg, pyPkg )
            
p = BuildProcess( masterConfigFactory, 
                  pyPkgConfigFactoryDict={ PY_CONFIG_KEY:None },
                  iExpressPkgConfigFactoryDict={ BATCH_CONFIG_KEY:None }, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       

