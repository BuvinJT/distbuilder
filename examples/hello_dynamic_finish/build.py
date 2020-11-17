from distbuilder import( RobustInstallerProcess, ConfigFactory,
    QtIfwControlScript, QtIfwOnFinishedCheckbox, ExecutableScript,
    findQtIfwPackage, joinPathQtIfw, 
    IS_WINDOWS, IS_MACOS, QT_IFW_TARGET_DIR )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Dynamic Finish Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloDynamicFinishSetup"

# Define a "Package Factory Dictionary" 
# Note: None values for a ConfigFactory results in making a clone of the 
# master, which can then be customization from that "base" within 
# RobustInstallerProcess.onConfigFactory
TK_CONFIG_KEY  = "tk"
CLI_CONFIG_KEY = "cli"
pkgFactories={ TK_CONFIG_KEY:None, CLI_CONFIG_KEY:None }

licenseName = "LICENSE.TXT"

# SET A DEMO OPTION TO TEST A GIVEN SCRIPT TYPE
# Note: SHELL==BATCH on Windows
(SHELL, POWERSHELL, VBSCRIPT, APPLESCRIPT) = range(4)
DEMO_OPTION = SHELL

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
            
        def customizeFinishedPage( cfg, tkPkg, cliPkg ):
                        
            # Disable/remove the standard run on exit checkbox
            cfg.controlScript.isRunProgChecked = False
            cfg.controlScript.isRunProgVisible = False  

            # Define platform specific example commands / scripts
                 
            # NOTE: DETACHED POST INSTALL SCRIPTS SHOULD SELF DESTRUCT!
            # The installer cannot delete them, because the installer
            # is normally closed before the scripts are completed.
            # If you do fail to include a self destruction (or the 
            # script crashes before it can do that successfully), it will
            # remain in your system temp folder until otherwise purged. 
            # This self destruction is a *best practice*, but it's not a
            # major calamity if you forget, or it fails...              
                                        
            scripts = {}                      
            if  IS_WINDOWS:
                textViewer = "notepad"        
                # TODO: FIX 
                # (shell commands with quotes don't work currently...)                      
                openLicCommand=(
                    'start "" {textViewer} "@TargetDir@\{licenseName}"' )
                openLicBatchScript = ExecutableScript( "openLic", script=([ # as line list
                    'start "" {textViewer} "@TargetDir@\{licenseName}"',
                    '(goto) 2>nul & del "%~f0"'                               # SELF DESTRUCT
                ]) )                     
                openLicPowerShellScript = ExecutableScript( 
                    "openLic", extension="ps1", script=([ # as line list
                    'Start-Process -FilePath "{textViewer}" '
                        '-ArgumentList "@TargetDir@\{licenseName}"',
                    'Remove-Item $script:MyInvocation.MyCommand.Path -Force'  # SELF DESTRUCT
                ]) )
                openLicVbScript = ExecutableScript( 
                    "openLic", extension="vbs", script=([ # as line list
                    'Set oShell = WScript.CreateObject("WScript.Shell")',
                    'oShell.Run "{textViewer} ""@TargetDir@\{licenseName}"""',                    
                    'Set oShell = Nothing',
                    'Set oFSO = CreateObject("Scripting.FileSystemObject")',  # SELF DESTRUCT                      
                    'oFSO.DeleteFile WScript.ScriptFullName',                 #       |      
                    'Set oFSO = Nothing'                                      #       V
                ]) )  
                scripts.update( { SHELL:      openLicBatchScript,  
                                  POWERSHELL: openLicPowerShellScript,
                                  VBSCRIPT:   openLicVbScript } )                
            elif IS_MACOS :
                textViewer = "TextEdit"                 
                openLicCommand=( 
                    'open -a {textViewer} "@TargetDir@/{licenseName}"' )            
                openLicShellScript = ExecutableScript( "openLic", script=(
                    'open -a {textViewer} "@TargetDir@/{licenseName}"' ) )     
                scripts.update( { SHELL: openLicShellScript } )                
            else: # IS_LINUX 
                textViewer = "gedit" # distro specific...                                
                openLicCommand=( 
                    'screen -d -m {textViewer} "@TargetDir@/{licenseName}"' )
                openLicShellScript = ExecutableScript( "openLic", script=(
                    'screen -d -m {textViewer} "@TargetDir@/{licenseName}"' ) )                     
                scripts.update( { SHELL: openLicShellScript } )
            openLicScript = scripts[ DEMO_OPTION ]
                            
            # raw string replacements
            openLicCommand.replace(
                "{textViewer}" , textViewer ).replace(
                "{licenseName}", licenseName ) 
            # slightly more friendly script "replacements"                               
            openLicScript.replacements={ 
                  "textViewer" : textViewer 
                , "licenseName": licenseName }                 
                          
            # Create custom checkbox widgets 
            # Note: QtIfwOnFinishedCheckbox objects are implicitly 
            # placed on the *finished* page.  The page order for such is 
            # dictated by the object instantiation order, by default
            # (but that can be explicitly defined during construction).
            runTkCheckbox  = QtIfwOnFinishedCheckbox( 
                "runTk",  ifwPackage=tkPkg ) 
            runCliCheckbox = QtIfwOnFinishedCheckbox( 
                "runCli", ifwPackage=cliPkg )             
            openOnlineManualViaOsCheckbox = QtIfwOnFinishedCheckbox( 
                "openOnlineManualViaOs", text="Open Online Manual w/ Default Browser now.", 
                openViaOsPath="https://distribution-builder.readthedocs.io/en/latest/" )             
            openLicViaOsCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaOs", text="Open License w/ Default Editor now.", 
                openViaOsPath=joinPathQtIfw( QT_IFW_TARGET_DIR, licenseName ) )
            openLicViaProgCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaProg", text="Open License w/ Program now.", 
                runProgram=textViewer, # on system path, else use full path here
                argList=[joinPathQtIfw( QT_IFW_TARGET_DIR, licenseName )] )
            openLicViaCmdCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaCommand", text="Open License w/ Command now.", 
                shellCmd=openLicCommand )
            openLicViaScriptCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaScript", text="Open License w/ Script now.", 
                script=openLicScript ) 
            rebootCheckbox = QtIfwOnFinishedCheckbox( "reboot", isReboot=True )
            
            # Add the checkbox widgets to the installer
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

            # Add custom QScript to the finished page, to dynamically set the 
            # message displayed, and to control when the checkboxes are visible  
            # and checked, etc.
            Script      = QtIfwControlScript
            CONCAT      = Script.CONCAT
            MSG_LBL     = Script.FINISHED_MESSAGE_LABEL
            DEFAULT_MSG = Script.DEFAULT_FINISHED_MESSAGE
            TK_INSTALLED_MSG = Script.quote(
                '<br /><br />Thank you installing the <b>Tk Example</b>!' )
            CLI_INSTALLED_MSG = Script.quote(
                '<br /><br />Thank you installing the <b>CLI Example</b>!' )
            
            # helper function
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
        customizeFinishedPage( cfg, tkPkg, cliPkg )
            
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
