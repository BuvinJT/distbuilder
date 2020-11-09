from distbuilder import( RobustInstallerProcess, ConfigFactory,
    QtIfwControlScript, QtIfwOnInstallFinishedOptions,
    findQtIfwPackage )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Packages Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloPackagesSetup"

TK_CONFIG_KEY  = "tk"
CLI_CONFIG_KEY = "cli"
pkgFactories={ TK_CONFIG_KEY:None, CLI_CONFIG_KEY:None }

RUN_TK_WIDGET  = "RunTk"
RUN_CLI_WIDGET = "RunCli"
f.ifwWidgets       = [
      QtIfwOnInstallFinishedOptions( 
        RUN_TK_WIDGET,  "Run Tk Example",  action=None )
    , QtIfwOnInstallFinishedOptions( 
        RUN_CLI_WIDGET, "Run CLI Example", action=None )
]
 
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

        def customizeInstaller( cfg ):
            
            pkgs = cfg.packages
            tkPkg  = findQtIfwPackage( pkgs, TK_CONFIG_KEY )            
            cliPkg = findQtIfwPackage( pkgs, CLI_CONFIG_KEY )
            
            defineComponentsOrder( tkPkg, cliPkg )
            reviseRunProgram( cfg )                                
            reviseFinishedPage( cfg, tkPkg, cliPkg )

        def defineComponentsOrder( tkPkg, cliPkg ):
            # Listed in descending order! (highest *priority* first)
            tkPkg.pkgXml.SortingPriority  = 10
            cliPkg.pkgXml.SortingPriority = 1

        def reviseRunProgram( cfg ):      
            cfg.configXml.RunProgram = None 
            cfg.controlScript.isRunProgVisible = False
            
        def reviseFinishedPage( cfg, tkPkg, cliPkg ):
            SCRPT       = QtIfwControlScript
            ELSE        = SCRPT.ELSE 
            CONCAT      = SCRPT.CONCAT
            SBLK        = SCRPT.START_BLOCK
            EBLK        = SCRPT.END_BLOCK
            MSG_LBL     = SCRPT.FINISHED_MESSAGE_LABEL
            DEFAULT_MSG = SCRPT.DEFAULT_FINISHED_MESSAGE
            quote       = QtIfwControlScript.quote
            cfg.controlScript.finishedPageCallBackTail = ( 
                SCRPT.ifMaintenanceTool() + 
                    SCRPT.setText( MSG_LBL, DEFAULT_MSG ) +
                ELSE + SBLK +
                    SCRPT.setText( MSG_LBL, DEFAULT_MSG ) +                                    
                    SCRPT.ifComponentInstalled( tkPkg.name ) +
                        SCRPT.setText( MSG_LBL, SCRPT.getText( MSG_LBL ) + 
                            CONCAT + quote( 
                            '<br /><br />Thank you installing the <b>Tk Example</b>!'),
                            varNames=False, isAutoQuote=False ) +
                    SCRPT.ifComponentInstalled( cliPkg.name ) +
                        SCRPT.setText( MSG_LBL, SCRPT.getText( MSG_LBL ) + 
                            CONCAT + quote( 
                            '<br /><br />Thank you installing the <b>CLI Example</b>!'),
                            varNames=False, isAutoQuote=False ) +
                EBLK                        
            )        
        customizeInstaller( cfg )        
            
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
