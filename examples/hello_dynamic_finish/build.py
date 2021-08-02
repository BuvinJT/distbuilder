from distbuilder import( RobustInstallerProcess, ConfigFactory,
    QtIfwOnFinishedCheckbox, QtIfwOnFinishedDetachedExec, 
    QtIfwControlScript, QtIfwExternalOp, ExecutableScript, 
    startLogging, findQtIfwPackage, joinPathQtIfw, joinPath, 
    IS_WINDOWS, IS_MACOS, QT_IFW_TARGET_DIR, QT_IFW_DESKTOP_DIR )

startLogging()
  
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

        IS_CLI_APP_INSTALLED_KEY = "isCliAppInstalled"
        IS_TK_APP_INSTALLED_KEY  = "isTkAppInstalled"

        def reviseControllerConstructor( cfg ): 
            # When running the installer (not the maintenance tool), and not
            # using "remove all mode" (e.g. via silent installer -u),
            # define additional arguments for the maintenance tool
            # (unless a manual override was provided for that...) 
            # so it will skip the custom uninstallation detached execution  
            # during an a forced uninstall, i.e. an "update" context.               
            Script = QtIfwControlScript
            TAB  = Script.TAB
            EBLK = Script.END_BLOCK
            NOT_EQUAL_TO = Script.NOT_EQUAL_TO
            ASSIGN = Script.ASSIGN
            FALSE = Script.FALSE
            cfg.controlScript.controllerConstructorInjection =(
                Script.ifInstalling( isMultiLine=True ) +
                TAB + Script.ifCondition( Script.cmdLineArg( 
                    Script.MAINTAIN_MODE_CMD_ARG ) + NOT_EQUAL_TO +
                    Script.quote( Script.MAINTAIN_MODE_OPT_REMOVE_ALL ), 
                    isMultiLine=True ) +
                (2*TAB) + Script.ifCmdLineArg( Script.MAINTAIN_PASSTHRU_CMD_ARG, 
                                               isNegated=True ) +
                    (3*TAB) + Script.setValue( Script.MAINTAIN_PASSTHRU_CMD_ARG,
                        IS_TK_APP_INSTALLED_KEY + ASSIGN + FALSE ) +                    
                TAB + EBLK +                
                EBLK
            )

        def customizeReadyForInstallPage( cfg, tkPkg, cliPkg ):
            # Unfortunately, there is no built-in QtIFW means to determine 
            # which components were installed via QtScript from an uninstaller. 
            # To work around that: Set an installer variable(s) indicating  
            # component (i.e. package) selection just prior to the installation 
            # process,  so that such will be persisted, and thus available, in  
            # the uninstaller.              
            cfg.controlScript.readyForInstallationPageOnInstall =(
                QtIfwControlScript.setBoolValue( IS_TK_APP_INSTALLED_KEY, 
                    QtIfwControlScript.isComponentSelected( tkPkg ) ) +
                QtIfwControlScript.setBoolValue( IS_CLI_APP_INSTALLED_KEY, 
                    QtIfwControlScript.isComponentSelected( cliPkg ) )                                                            
            )
            
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
            # To this end, QtIfwExternalOp provides a collection of helper
            # script snippet functions
                                        
            scripts = {}                      
            if  IS_WINDOWS:
                textViewer = "notepad"        
                # TODO: FIX 
                # (shell commands with quotes don't work currently...)                      
                openLicCommand=(
                    'start "" {textViewer} "@TargetDir@\{licenseName}"' )
                openLicBatchScript = ExecutableScript( "openLic", script=([ # as line list
                    'start "" {textViewer} "@TargetDir@\{licenseName}"',
                    QtIfwExternalOp.batchSelfDestructSnippet()
                ]) )                     
                openLicPowerShellScript = ExecutableScript( 
                    "openLic", extension="ps1", script=([ # as line list
                    'Start-Process -FilePath "{textViewer}" '
                        '-ArgumentList "@TargetDir@\{licenseName}"',
                    QtIfwExternalOp.powerShellSelfDestructSnippet()
                ]) )
                openLicVbScript = ExecutableScript( 
                    "openLic", extension="vbs", script=([ # as line list
                    'Set oShell = WScript.CreateObject("WScript.Shell")',
                    'oShell.Run "{textViewer} ""@TargetDir@\{licenseName}"""',                    
                    'Set oShell = Nothing',
                    QtIfwExternalOp.vbScriptSelfDestructSnippet()             #       V
                ]) )  
                scripts.update( { SHELL:      openLicBatchScript,  
                                  POWERSHELL: openLicPowerShellScript,
                                  VBSCRIPT:   openLicVbScript } )                
            elif IS_MACOS :
                textViewer = "TextEdit"                 
                openLicCommand=( 
                    'open -a {textViewer} "@TargetDir@/{licenseName}"' )  
                # TODO: Add self-destruction          
                openLicShellScript = ExecutableScript( "openLic", script=([
                    'open -a {textViewer} "@TargetDir@/{licenseName}"' 
                    ,QtIfwExternalOp.shellScriptSelfDestructSnippet()
                ]) )     
                scripts.update( { SHELL: openLicShellScript } )                
            else: # IS_LINUX 
                textViewer = "gedit" # distro specific...                                
                openLicCommand=( 
                    'screen -d -m {textViewer} "@TargetDir@/{licenseName}"' )
                # TODO: Add self-destruction
                openLicShellScript = ExecutableScript( "openLic", script=([
                    'screen -d -m {textViewer} "@TargetDir@/{licenseName}"'
                    ,QtIfwExternalOp.shellScriptSelfDestructSnippet()
                ]) )                     
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
            # TODO: Fix this!  (It's broken on Windows at least...)
            openLicViaCmdCheckbox = QtIfwOnFinishedCheckbox( 
                "openLicViaCommand", text="Open License w/ Command now. (broken!)", 
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
            SBLK        = Script.START_BLOCK
            EBLK        = Script.END_BLOCK
            ELSE        = Script.ELSE
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
                            Script.isComponentInstalled( pkg ),
                            isChecked ]) ) +
                        checkbox.setVisible( 
                            Script.isComponentInstalled( pkg ) ) )

            cfg.controlScript.finishedPageOnInstall =( 
                Script.setText( MSG_LBL, DEFAULT_MSG ) +                                    
                Script.ifComponentInstalled( tkPkg ) +
                    Script.setText( MSG_LBL, Script.getText( MSG_LBL ) + 
                        CONCAT + TK_INSTALLED_MSG,
                        varNames=False, isAutoQuote=False ) +
                Script.ifComponentInstalled( cliPkg ) +
                    Script.setText( MSG_LBL, Script.getText( MSG_LBL ) + 
                        CONCAT + CLI_INSTALLED_MSG,
                        varNames=False, isAutoQuote=False ) +                                  
                showIfInstalled( runTkCheckbox, tkPkg ) +
                showIfInstalled( runCliCheckbox, cliPkg ) +
                Script.ifInternetConnected( isMultiLine=True ) +
                    openOnlineManualViaOsCheckbox.enable( True ) +
                    openOnlineManualViaOsCheckbox.setChecked( True ) +
                EBLK + ELSE + SBLK +
                    openOnlineManualViaOsCheckbox.enable( False ) +
                    openOnlineManualViaOsCheckbox.setChecked( False ) +                                    
                EBLK +                                        
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

            # Add onFinishedDetachedExecutions (not directly bound to gui)
            # -----------------------------------------------------------------
            # Define a detached execution scripts, to be invoked post 
            # installation and uninstallation, unconditionally.  
            EXAMPLE_FILE_PATH = joinPath( QT_IFW_DESKTOP_DIR, "detached" )
            createExampleFileExec = QtIfwOnFinishedDetachedExec( 
                "createExampleFile",  QtIfwOnFinishedDetachedExec.ON_INSTALL,
                script = ExecutableScript( "createFile", script=(
                    ['echo. > "%s"' % (EXAMPLE_FILE_PATH,)
                    ,QtIfwExternalOp.batchSelfDestructSnippet()]
                    if IS_WINDOWS else
                    ['touch "%s"'  % (EXAMPLE_FILE_PATH,) 
                    ,QtIfwExternalOp.shellScriptSelfDestructSnippet()]) 
                )  
            )                         
            removeExampleFileExec = QtIfwOnFinishedDetachedExec( 
                "removeExampleFile",  QtIfwOnFinishedDetachedExec.ON_UNINSTALL,
                script = ExecutableScript( "removeFile", script=(
                    ['del /q "%s"' % (EXAMPLE_FILE_PATH,)
                    ,QtIfwExternalOp.batchSelfDestructSnippet()]
                    if IS_WINDOWS else
                    ['rm "%s"'  % (EXAMPLE_FILE_PATH,)
                    ,QtIfwExternalOp.shellScriptSelfDestructSnippet()])
                ) 
            )                        
                            
            # Define a detached execution action, to be invoked post  
            # uninstallation, conditionally controlled by the persisted 
            # variable stored during installation.  
            openPyPiPageViaOsExec = QtIfwOnFinishedDetachedExec( 
                "openPyPiPageViaOs",  QtIfwOnFinishedDetachedExec.ON_UNINSTALL,
                openViaOsPath="https://pypi.org/project/distbuilder/",
                ifCondition=Script.andList([
                      Script.isInternetConnected()
                    , Script.lookupBoolValue( IS_TK_APP_INSTALLED_KEY )
                ]) 
            )                        
            
            cfg.controlScript.onFinishedDetachedExecutions = [
                  createExampleFileExec
                , removeExampleFileExec
                , openPyPiPageViaOsExec
            ]            

        pkgs   = cfg.packages
        tkPkg  = findQtIfwPackage( pkgs, TK_CONFIG_KEY )            
        cliPkg = findQtIfwPackage( pkgs, CLI_CONFIG_KEY )     
        reviseControllerConstructor( cfg )
        customizeReadyForInstallPage( cfg, tkPkg, cliPkg )   
        customizeFinishedPage( cfg, tkPkg, cliPkg )
            
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
