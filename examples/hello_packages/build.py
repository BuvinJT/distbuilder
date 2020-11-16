from distbuilder import( RobustInstallerProcess, ConfigFactory,
    QtIfwControlScript, QtIfwOnFinishedCheckbox, ExecutableScript,
    findQtIfwPackage, joinPathQtIfw, 
    IS_WINDOWS, IS_MACOS, QT_IFW_TARGET_DIR )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Packages Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloPackagesSetup"

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
            f.distResources    = [licenseName]
            
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
            runTkCheckbox  = QtIfwOnFinishedCheckbox( 
                "runTk",  ifwPackage=tkPkg ) 
            runCliCheckbox = QtIfwOnFinishedCheckbox( 
                "runCli", ifwPackage=cliPkg )             
            openOnlineManualViaOsCheckbox = QtIfwOnFinishedCheckbox( 
                "openOnlineManualViaOs", text="Open Online Manual", 
                openViaOsPath="https://distribution-builder.readthedocs.io/en/latest/" )             
            openLicenseViaOsCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicenseViaOs", text="Open License w/ Default Editor", 
                openViaOsPath=joinPathQtIfw( QT_IFW_TARGET_DIR, licenseName ) )
            openLicenseViaScriptCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicenseViaScript", text="Open License w/ Script", 
                script=ExecutableScript( "openLicense", script=(
                'notepad "@TargetDir@\{licenseName}"'          if IS_WINDOWS else
                'open -a TextEdit "@TargetDir@/{licenseName}"' if IS_MACOS else
                'gedit "@TargetDir@/{licenseName}"'            #if IS_LINUX 
                ), 
                replacements={ "licenseName": licenseName } ) )
            cfg.addUiElements([ 
                  runTkCheckbox
                , runCliCheckbox
                , openOnlineManualViaOsCheckbox 
                , openLicenseViaOsCheckbox
                , openLicenseViaScriptCheckbox
            ])            

            # Add custom QScript to the finished page 
            Script      = QtIfwControlScript
            CONCAT      = Script.CONCAT
            MSG_LBL     = Script.FINISHED_MESSAGE_LABEL
            DEFAULT_MSG = Script.DEFAULT_FINISHED_MESSAGE
            TK_INSTALLED_MSG = Script.quote(
                '<br /><br />Thank you installing the <b>Tk Example</b>!' )
            CLI_INSTALLED_MSG = Script.quote(
                '<br /><br />Thank you installing the <b>CLI Example</b>!' )
            cfg.controlScript.finishedPageOnInstall =( 
                Script.setText( MSG_LBL, DEFAULT_MSG ) +                                    
                Script.ifComponentInstalled( tkPkg.name ) +
                    Script.setText( MSG_LBL, Script.getText( MSG_LBL ) + 
                        CONCAT + TK_INSTALLED_MSG,
                        varNames=False, isAutoQuote=False ) +
                Script.ifComponentInstalled( cliPkg.name ) +
                    Script.setText( MSG_LBL, Script.getText( MSG_LBL ) + 
                        CONCAT + CLI_INSTALLED_MSG,
                        varNames=False, isAutoQuote=False ) +
                runTkCheckbox.setChecked( 
                    Script.isComponentInstalled( tkPkg.name ) ) +
                runTkCheckbox.setVisible( 
                    Script.isComponentInstalled( tkPkg.name ) ) +
                runCliCheckbox.setChecked( 
                    Script.isComponentInstalled( cliPkg.name ) ) +
                runCliCheckbox.setVisible( 
                    Script.isComponentInstalled( cliPkg.name ) ) +                    
                openLicenseViaOsCheckbox.setChecked( 
                    Script.isComponentInstalled( cliPkg.name ) ) +
                openLicenseViaOsCheckbox.setVisible( 
                    Script.isComponentInstalled( cliPkg.name ) ) +
                openLicenseViaScriptCheckbox.setChecked( 
                    Script.isComponentInstalled( cliPkg.name ) ) +
                openLicenseViaScriptCheckbox.setVisible( 
                    Script.isComponentInstalled( cliPkg.name ) ) +
                openOnlineManualViaOsCheckbox.setChecked( True ) +
                openOnlineManualViaOsCheckbox.setVisible( True )                             
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
