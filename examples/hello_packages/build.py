from distbuilder import( RobustInstallerProcess, ConfigFactory,
    QtIfwControlScript, QtIfwOnFinishedCheckbox,
    findQtIfwPackage )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Packages Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloPackagesSetup"

# Define a package factory dictionary 
# (None values==clone the master, then allow customization from that "base")
TK_CONFIG_KEY  = "tk"
CLI_CONFIG_KEY = "cli"
pkgFactories={ TK_CONFIG_KEY:None, CLI_CONFIG_KEY:None }

class BuildProcess( RobustInstallerProcess ):
    
    def onConfigFactory( self, key, f ):
        if key==TK_CONFIG_KEY: 
            f.productName      = "Hello World Tk Example"
            f.description      = "Tk Example"
            f.binaryName       = "HelloWorldTk"
            f.version          = (1,0,0,0)
            f.isGui            = True        
            f.sourceDir        = "../hello_world_tk"
            f.entryPointPy     = "hello.py"  
            f.isObfuscating    = True
            f.iconFilePath     = "demo.ico"             
        elif key==CLI_CONFIG_KEY: 
            f.productName      = "Hello World CLI Example"
            f.description      = "CLI Example"
            f.binaryName       = "HelloWorld"
            f.version          = (1,0,0,0)
            f.isGui            = False
            f.sourceDir        = "../hello_world"
            f.entryPointPy     = "hello.py"  
            f.isObfuscating    = False
            f.iconFilePath     = None             
            f.distResources    = ["LICENSE"]
            
    def onOpyConfig( self, key, cfg ):
        if key==TK_CONFIG_KEY:    
            cfg.external_modules.extend( [ 'tkinter', 'tkinter.ttk' ] )
            
    def onQtIfwConfig( self, cfg ):     

        def defineComponentsOrder( tkPkg, cliPkg ):
            # Listed / installed in descending order 
            # (i.e. highest *priority* first)
            tkPkg.pkgXml.SortingPriority  = 10
            cliPkg.pkgXml.SortingPriority = 1
            
        def customizeFinishedPage( cfg, tkPkg, cliPkg ):
            # Disable/remove the standard run on exit checkbox
            cfg.controlScript.isRunProgChecked = False
            cfg.controlScript.isRunProgVisible = False  
            
            # Add some custom widgets to the page
            # Note: QtIfwOnFinishedCheckbox objects are implicitly 
            # placed on the finished page.  The page order for such is 
            # dictated by the object instantiation order, by default.
            runTkCheckbox = QtIfwOnFinishedCheckbox( 
                "runTk",  "Run Tk Example",  action=None ) 
            runCliCheckbox = QtIfwOnFinishedCheckbox( 
                "runCli", "Run CLI Example", action=None )            
            cfg.addUiElements( [ runTkCheckbox, runCliCheckbox ] )            

            # Add custom QScript to the finished page 
            SCRPT       = QtIfwControlScript
            ELSE        = SCRPT.ELSE 
            CONCAT      = SCRPT.CONCAT
            SBLK        = SCRPT.START_BLOCK
            EBLK        = SCRPT.END_BLOCK
            MSG_LBL     = SCRPT.FINISHED_MESSAGE_LABEL
            DEFAULT_MSG = SCRPT.DEFAULT_FINISHED_MESSAGE
            TK_INSTALLED_MSG = SCRPT.quote(
                '<br /><br />Thank you installing the <b>Tk Example</b>!' )
            CLI_INSTALLED_MSG = SCRPT.quote(
                '<br /><br />Thank you installing the <b>CLI Example</b>!' )
            cfg.controlScript.finishedPageCallBackTail =( 
                SCRPT.ifMaintenanceTool( isMultiLine=True ) + 
                    SCRPT.setText( MSG_LBL, DEFAULT_MSG ) +
                    runTkCheckbox.setChecked( False ) +
                    runTkCheckbox.setVisible( False ) +
                    runCliCheckbox.setChecked( False ) +
                    runCliCheckbox.setVisible( False ) +
                EBLK + ELSE + SBLK +
                    SCRPT.setText( MSG_LBL, DEFAULT_MSG ) +                                    
                    SCRPT.ifComponentInstalled( tkPkg.name ) +
                        SCRPT.setText( MSG_LBL, SCRPT.getText( MSG_LBL ) + 
                            CONCAT + TK_INSTALLED_MSG,
                            varNames=False, isAutoQuote=False ) +
                    SCRPT.ifComponentInstalled( cliPkg.name ) +
                        SCRPT.setText( MSG_LBL, SCRPT.getText( MSG_LBL ) + 
                            CONCAT + CLI_INSTALLED_MSG,
                            varNames=False, isAutoQuote=False ) +
                    runTkCheckbox.setChecked( 
                        SCRPT.isComponentInstalled( tkPkg.name ) ) +
                    runTkCheckbox.setVisible( 
                        SCRPT.isComponentInstalled( tkPkg.name ) ) +
                    runCliCheckbox.setChecked( 
                        SCRPT.isComponentInstalled( cliPkg.name ) ) +
                    runCliCheckbox.setVisible( 
                        SCRPT.isComponentInstalled( cliPkg.name ) ) +                            
                EBLK                        
            )        

        pkgs   = cfg.packages
        tkPkg  = findQtIfwPackage( pkgs, TK_CONFIG_KEY )            
        cliPkg = findQtIfwPackage( pkgs, CLI_CONFIG_KEY )        
        defineComponentsOrder( tkPkg, cliPkg )       
        customizeFinishedPage( cfg, tkPkg, cliPkg )
            
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
