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

                       
            if  IS_WINDOWS:
                textViewer = "notepad"  
                
                # Batch / "Native"
                openLicCommand=( 
                    '{textViewer} "@TargetDir@\{licenseName}"' )     
                #openLicScript = openLicCommand                             
                #scriptExtension=True # True==auto assign    
                
                # PowerShell
                #openLicScript =(
                #    'Start-Process -FilePath "{textViewer}" '
                #        '-ArgumentList "@TargetDir@\{licenseName}"' ) 
                #scriptExtension = "ps1"

                # VBScript
                openLicScript =([ # as line list
                    'Set oShell = WScript.CreateObject("WScript.Shell")',
                    'oShell.Run "{textViewer} ""@TargetDir@\{licenseName}"""',
                    'Set oShell = Nothing'
                ])  
                scriptExtension = "vbs"                        
                
            elif IS_MACOS :
                textViewer = "TextEdit" 
                
                # Shell Script / "Native"
                openLicCommand=( 
                    'open -a {textViewer} "@TargetDir@/{licenseName}"' )
                openLicScript = openLicCommand
                scriptExtension=True # True==auto assign      
                              
            else: # IS_LINUX 
                textViewer = "gedit" # distro specific...   
                             
                # Shell Script / "Native"
                openLicCommand=( 
                    '{textViewer} "@TargetDir@/{licenseName}"' )
                openLicScript = openLicCommand
                scriptExtension=True # True==auto assign    
                          
            # Add custom widgets to the page
            # Note: QtIfwOnFinishedCheckbox objects are implicitly 
            # placed on the *finished* page.  The page order for such is 
            # dictated by the object instantiation order, by default
            # (but can be explicitly defined during construction).
            runTkCheckbox  = QtIfwOnFinishedCheckbox( 
                "runTk",  ifwPackage=tkPkg ) 
            runCliCheckbox = QtIfwOnFinishedCheckbox( 
                "runCli", ifwPackage=cliPkg )             
            openOnlineManualViaOsCheckbox = QtIfwOnFinishedCheckbox( 
                "openOnlineManualViaOs", text="Open Online Manual", 
                openViaOsPath="https://distribution-builder.readthedocs.io/en/latest/" )             
            openLicViaOsCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaOs", text="Open License w/ Default Editor", 
                openViaOsPath=joinPathQtIfw( QT_IFW_TARGET_DIR, licenseName ) )
            openLicViaProgCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaProg", text="Open License w/ Program", 
                runProgram=textViewer, # on system path, else use full path here
                argList=[joinPathQtIfw( QT_IFW_TARGET_DIR, licenseName )] )
            openLicViaCmdCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaCommand", text="Open License w/ Command", 
                shellCmd=openLicCommand.replace(
                "{textViewer}" , textViewer ).replace(
                "{licenseName}", licenseName ) )
            openLicViaScriptCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaScript", text="Open License w/ Script", 
                script=ExecutableScript( 
                    "openLic", extension=scriptExtension,
                    script=openLicScript, replacements={ 
                      "textViewer" : textViewer 
                    , "licenseName": licenseName } ) )
            rebootCheckbox = QtIfwOnFinishedCheckbox( 
                "rebootNow", isReboot=True )
            cfg.addUiElements([ 
                  runTkCheckbox
                , runCliCheckbox
                , openOnlineManualViaOsCheckbox 
                , openLicViaOsCheckbox
                , openLicViaProgCheckbox
                , openLicViaCmdCheckbox
                , openLicViaScriptCheckbox
                , rebootCheckbox
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
            
            def showIfInstalled( checkbox, pkg, isChecked=True ):
                return( checkbox.setChecked( Script.andList([
                            Script.isComponentInstalled( pkg.name ),
                            isChecked ]) ) +
                        checkbox.setVisible( 
                            Script.isComponentInstalled( pkg.name ) ) )

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
                showIfInstalled( runTkCheckbox, tkPkg ) +
                showIfInstalled( runCliCheckbox, cliPkg ) +
                openOnlineManualViaOsCheckbox.setChecked( True ) +
                openOnlineManualViaOsCheckbox.setVisible( True ) +                    
                showIfInstalled( openLicViaOsCheckbox, cliPkg ) +
                showIfInstalled( openLicViaProgCheckbox, cliPkg,   
                                 isChecked=False ) +
                showIfInstalled( openLicViaCmdCheckbox, cliPkg,    
                                 isChecked=False ) +
                showIfInstalled( openLicViaScriptCheckbox, cliPkg, 
                                 isChecked=False ) +
                rebootCheckbox.setChecked( False ) +
                rebootCheckbox.setVisible( True )
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
