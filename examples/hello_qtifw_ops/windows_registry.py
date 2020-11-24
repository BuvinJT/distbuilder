from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwControlScript, joinPath

f = configFactory  = ConfigFactory()
f.productName      = "Hello Registry Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwRegistrySetup"

# NOTE: Review the installer's log / verbose output to view the results of the  
# example function calls.               
class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):
        # Tip: define key paths via "raw" string literals (using the r prefix) to 
        # avoid having to escape the backslashes (\) by doubling them up as (\\). 
        # Use joinPath( head, tail ) to build the keys.  
        CURRENT_VER_KEY = r"HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion"
        RUN_ONCE_KEY    = joinPath( CURRENT_VER_KEY, "RunOnce" )
        FAKE_KEY        = joinPath( CURRENT_VER_KEY, "RunTwice" )

        Script = QtIfwControlScript
        RETURN_LOG_PREFIX = '"Function returned: " + '

        # Note: Set isAutoBitContext=False to access native 64 bit entries from  
        # the installer's 32 bit context.        
        cfg.controlScript.introductionPageOnInstall =(
            Script.log( RETURN_LOG_PREFIX +
                Script.registryKeyExists( RUN_ONCE_KEY, isAutoBitContext=False ),
                isAutoQuote=False ) +
            Script.log( RETURN_LOG_PREFIX +
                Script.registryKeyExists( FAKE_KEY, isAutoBitContext=False ),
                isAutoQuote=False ) +                                    
            Script.ifRegistryKeyExists( RUN_ONCE_KEY, isAutoBitContext=False ) +
                Script.debugPopup( "RunOnce Registry Key exists!" ) +
            Script.log( RETURN_LOG_PREFIX +
                Script.registryKeyExistsLike( CURRENT_VER_KEY, "run", 
                    isAutoBitContext=False, isCaseSensitive=False, 
                    isRecursive=False ),
                isAutoQuote=False ) +
            Script.log( RETURN_LOG_PREFIX +
                Script.registryKeyExistsLike( CURRENT_VER_KEY, "walk", 
                    isAutoBitContext=False, isCaseSensitive=False, 
                    isRecursive=False ),
                isAutoQuote=False )                 
                             
        ) 
        
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       