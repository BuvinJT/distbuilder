from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwExternalOp, joinPathQtIfw, QT_IFW_HOME_DIR

f = configFactory  = ConfigFactory()
f.productName      = "Hello Custom Installer Ops Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorldTk"
f.isGui            = True        
f.entryPointPy     = "../hello_world_tk/hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwOpsSetup"

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):    
        
        def ops():
            fileName = "distbuilder-ops-test.txt"
            filePath = joinPathQtIfw( QT_IFW_HOME_DIR, fileName )
            # Windows?!
            createFileOp = QtIfwExternalOp( 
                      exePath="touch",       args=[filePath],
                uninstExePath="rm",    uninstArgs=[filePath] )         
            return [ createFileOp ]        
    
        cfg.packages[0].pkgScript.externalOps = ops() 
         
        #script.customOperations = None
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       