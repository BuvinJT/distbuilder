from distbuilder import( RobustInstallerProcess, ConfigFactory,
    QtIfwControlScript, findQtIfwPackage )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Custom UI Interactions Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloUiInteractionsSetup"

# Define a "Package Factory Dictionary" 
# Note: None values for a ConfigFactory results in making a clone of the 
# master, which can then be customization from that "base" within 
# RobustInstallerProcess.onConfigFactory
TK_CONFIG_KEY  = "tk"
CLI_CONFIG_KEY = "cli"
pkgFactories={ TK_CONFIG_KEY:None, CLI_CONFIG_KEY:None }

licenseName = "LICENSE.TXT"

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
            f.iconFilePath     = "demo.ico"             
        elif key==CLI_CONFIG_KEY: 
            f.productName      = "Hello World CLI Example"
            f.description      = "CLI Example"
            f.binaryName       = "HelloWorld"
            f.version          = (1,0,0,0)
            f.isGui            = False
            f.sourceDir        = "../hello_world"
            f.entryPointPy     = "hello.py"  
            f.iconFilePath     = None             
            f.distResources    = [licenseName]
            
    def onQtIfwConfig( self, cfg ):     
            
        def reviseComponentSelectionPage( cfg, tkPkg ):           
            Script = QtIfwControlScript
            TAB = Script.TAB
            ELSE = Script.ELSE 
            SBLK = Script.START_BLOCK
            EBLK = Script.END_BLOCK
            NET_ERR_MSG="The Tk Example requires an internet connection"
            cfg.controlScript.componentSelectionPageInjection =(
                Script.ifAutoPilot( isMultiLine=True ) +
                    TAB + Script.ifComponentSelected( tkPkg,
                                                      isMultiLine=True ) +
                    (2*TAB) + Script.assertInternetConnected( 
                        errMsg=NET_ERR_MSG ) +
                    TAB + EBLK +
                EBLK + ELSE + SBLK +
                    TAB + Script.ifInternetConnected( isRefresh=True, 
                                                      isMultiLine=True ) +
                        (2*TAB) + QtIfwControlScript.enableComponent( tkPkg, True ) +                    
                    TAB + EBLK + 
                    TAB + ELSE + SBLK +
                    (2*TAB) + QtIfwControlScript.warningPopup( NET_ERR_MSG ) +
                    (2*TAB) + QtIfwControlScript.selectComponent( tkPkg, False ) +                
                    (2*TAB) + QtIfwControlScript.enableComponent( tkPkg, False ) +
                    TAB + EBLK +                   
                EBLK                         
            )
                   
        pkgs   = cfg.packages
        tkPkg  = findQtIfwPackage( pkgs, TK_CONFIG_KEY )            
        cliPkg = findQtIfwPackage( pkgs, CLI_CONFIG_KEY )     
        reviseComponentSelectionPage( cfg, tkPkg )
            
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
