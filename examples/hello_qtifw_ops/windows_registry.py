from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
        QtIfwControlScript, QtIfwPackageScript, QtIfwExternalOp as ExOp, \
        joinPath
from distbuilder.qt_installer import qtIfwDynamicValue

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

# NOTE: Review the installer/maintenancetool verbose output, plus the registry 
# (via regedit.exe) to inspect the results of the sample code.               
class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):
        
        # Tip: define key paths via "raw" string literals (using the r prefix) to 
        # avoid having to escape the backslashes (\) by doubling them up as (\\). 
        # Use joinPath( head, tail ) to build the keys.  
        CUR_VER_REGKEY  = r"HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion"
        RUN_ONCE_REGKEY = joinPath( CUR_VER_REGKEY, "RunOnce" )

        PC_NAME_REGKEY = r"HKLM:\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName"
        PC_NAME_REGVAL = "ComputerName"
        
        INVALID_REGKEY  = joinPath( CUR_VER_REGKEY, "RunTwice" )
        INVALID_REGVAL  = "NotReally" 
        
        PC_NAME_INSTALLER_KEY = "pcName"
        
        SIMPLE_DEMO_REGVAL  = "DistbuilderExample"
        SIMPLE_RUN_ONCE_CMD = 'cmd /Q /C "echo testing 1,2,3..."'

        DYNAMIC_DEMO_REGKEY  = r"HKLM:\SOFTWARE\SomeCompany\DistbuilderExample"
        DYNAMIC_DEMO_REGVAL  = "Greeting"
        DYNAMIC_GREETING     = 'Hello %s' % ( 
            qtIfwDynamicValue( PC_NAME_INSTALLER_KEY ) )
        
        def addControlScriptRegQueries( cntrlScript ):                
            Script = QtIfwControlScript
            ELSE = Script.ELSE 
            EBLK = Script.END_BLOCK        
            RETURN_LOG_PREFIX = '"Function returned: " + '

            # Note: Set isAutoBitContext=False to access native 64 bit entries from  
            # the installer's 32 bit context.        
            cntrlScript.introductionPageOnInstall =(
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryKeyExists( RUN_ONCE_REGKEY, isAutoBitContext=False ),
                    isAutoQuote=False ) +
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryKeyExists( INVALID_REGKEY, isAutoBitContext=False ),
                    isAutoQuote=False ) +                                    
                Script.ifRegistryKeyExists( RUN_ONCE_REGKEY, isAutoBitContext=False ) +
                    Script.debugPopup( "RunOnce Registry Key exists!" ) +
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryKeyExistsLike( CUR_VER_REGKEY, "run", 
                        isAutoBitContext=False, isCaseSensitive=False, 
                        isRecursive=False ),
                    isAutoQuote=False ) +
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryKeyExistsLike( CUR_VER_REGKEY, "walk", 
                        isAutoBitContext=False, isCaseSensitive=False, 
                        isRecursive=False ),
                    isAutoQuote=False )                                                  
            ) 
            
            cntrlScript.introductionPageOnMaintain =(
               Script.log( RETURN_LOG_PREFIX +
                    Script.registryEntryExists( 
                        RUN_ONCE_REGKEY, None, # None == default value for registry key  
                        isAutoBitContext=False ),
                    isAutoQuote=False ) +
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryEntryExists( 
                        INVALID_REGKEY, INVALID_REGVAL, 
                        isAutoBitContext=False ),
                    isAutoQuote=False ) +                                    
                Script.ifRegistryEntryExists( 
                    DYNAMIC_DEMO_REGKEY, DYNAMIC_DEMO_REGVAL, 
                    isMultiLine=True ) +
                        Script.ifAutoPilot() +
                            Script.log( "Demo 32 Bit Registry Value exists!" ) +
                        ELSE +
                            Script.debugPopup( "Demo 32 Bit Registry Value exists!" ) +
                    EBLK +        
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryEntryExistsLike( 
                        RUN_ONCE_REGKEY, "Distbuilder", 
                        isAutoBitContext=False, isCaseSensitive=False, 
                        isRecursive=False ),
                    isAutoQuote=False ) +
                Script.log( RETURN_LOG_PREFIX +
                    Script.registryEntryExistsLike( 
                        RUN_ONCE_REGKEY, "NotThere", 
                        isAutoBitContext=False, isCaseSensitive=False, 
                        isRecursive=False ),
                    isAutoQuote=False )                                       
            )
            
        def addRegistryOperations( pkgScript ):            
            Script = QtIfwPackageScript            
                        
            # Create a registry entry, from a static string, with automatic
            # removal of it upon uninstallation.
            # Write it to a 64 bit location, from this 32 bit installer.                         
            createSimpleRunOnceRegEntryOp = ExOp.CreateRegistryEntry( 
                    ExOp.AUTO_UNDO, 
                    RUN_ONCE_REGKEY, SIMPLE_DEMO_REGVAL, 
                    value=SIMPLE_RUN_ONCE_CMD, isAutoBitContext=False ) 

            # Query the registry, saving the result in the installer's
            # dynamic value dictionary.  
            pkgScript.preOpSupport = Script.setValueFromRegistryEntry( 
                PC_NAME_INSTALLER_KEY, 
                PC_NAME_REGKEY, PC_NAME_REGVAL, isAutoBitContext=False )

            # Create a registry value with what was queried during "pre op".  
            # Write to a 32 bit (WOW6432Node) location implicitly.
            # Include separate, explicit, create / remove ops - 
            # note that CreateRegistryEntry will also create any parent keys
            # as needed, thus pairing it with RemoveRegistryKey will ensure 
            # the demo application's entire key is removed - not just the 
            # "Greeting" entry (the higher level company key will be left 
            # behind however).                                              
            createDynamicRunOnceRegEntryOp = ExOp.CreateRegistryEntry( 
                    ExOp.ON_INSTALL, 
                    DYNAMIC_DEMO_REGKEY, DYNAMIC_DEMO_REGVAL, 
                    value=DYNAMIC_GREETING ) 
            removeDynamicRunOnceRegEntryOp = ExOp.RemoveRegistryKey( 
                    ExOp.ON_UNINSTALL, 
                    DYNAMIC_DEMO_REGKEY ) 
                                     
            pkgScript.externalOps += [ 
                createSimpleRunOnceRegEntryOp,
                createDynamicRunOnceRegEntryOp,
                removeDynamicRunOnceRegEntryOp 
            ]
        
        addControlScriptRegQueries( cfg.controlScript )                
        pkg = cfg.packages[0]
        addRegistryOperations( pkg.pkgScript )
                
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       