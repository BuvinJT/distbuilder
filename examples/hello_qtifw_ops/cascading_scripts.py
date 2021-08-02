from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
    QtIfwControlScript, QtIfwPackageScript, 
    QtIfwExternalOp, ExecutableScript, startLogging,
    normBinaryName, joinPath, joinPathQtIfw, 
    qtIfwOpDataPath, qtIfwDynamicValue, qtIfwDetachedOpDataPath, 
    IS_WINDOWS, IS_LINUX, 
    QT_IFW_DESKTOP_DIR, QT_IFW_HOME_DIR, QT_IFW_APPS_DIR, QT_IFW_APPS_X86_DIR  
    )

# NOTE: to evaluate what this demo accomplishes: look at contents of the 
# assorted files left on the desktop as a result of running the installer.
    
startLogging()
    
ON_INSTALL = QtIfwExternalOp.ON_INSTALL
opDataPath = QtIfwExternalOp.opDataPath

DEMO_ARG_TO_OPS_KEY = "user_op_arg"
DEMO_ARG_TO_OPS_FILE_NAME = DEMO_ARG_TO_OPS_KEY

if IS_WINDOWS:
    APP_FOUND_FILENAME = "AppFound"
if IS_LINUX:
    PKG_FOUND_FILENAME = "PkgFound"

f = configFactory  = ConfigFactory()
f.productName      = "Hello Cascading Scripts Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwCascadingScriptsSetup"

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):    

        def refineIntroductionPage( cfg ):
            # On the first wizard page (which is still programmatically 
            # processed by silent installers btw...), once all other resources 
            # have loaded:
            #
            # Create a "operations data file". Selectively do this in 
            # either install mode, maintain mode, or both. 
            #
            # The data for such might be derived in many ways. In this demo,
            # we use a value supplied at run time as a program argument.                        
            #
            # To test, execute either the installer or uninstaller from a 
            # terminal supplying an argument `"user_op_arg=my test data"`.  
            # Then, observe the file created with this same base name in the 
            # temp directory (or sub temp directory) upon launching the 
            # installer/uninstaller.  This illustrates where other custom 
            # "operations" could fetch this information dynamically. 
            #
            # Optionally, test this: 
            #     QtIfwControlScript.writeDetachedOpDataFile 
            #     (in place of QtIfwControlScript.writeOpDataFile)
            # With that, the temp file will persist beyond the life 
            # of the installer or uninstaller...            
            #
            writeArgOpFileSnippet = QtIfwControlScript.writeOpDataFile(
                DEMO_ARG_TO_OPS_FILE_NAME, 
                QtIfwControlScript.lookupValue( DEMO_ARG_TO_OPS_KEY ), 
                isAutoQuote=False )  
            cfg.controlScript.introductionPageOnInstall  = (
                writeArgOpFileSnippet ) 
            cfg.controlScript.introductionPageOnMaintain = (
                writeArgOpFileSnippet )

        def refineFinishedPage( cfg ):
            # Disable the run program check box by default, for this example. 
            cfg.controlScript.isRunProgChecked = False

            if IS_WINDOWS:
                Script = QtIfwControlScript
                cfg.controlScript.finishedPageOnInstall =(
                    Script.log( '"App found: " + ' + Script.pathExists( 
                                    qtIfwOpDataPath( APP_FOUND_FILENAME ) ), 
                                isAutoQuote=False ) 
                )
    
        # A boolean state may be represented via a file's existence,
        # created, or not created, during installer operations.
        # If optionally passing a variable name to CreateOpFlagFile, the 
        # operation will pivot upon the boolean evaluation of that 
        # QtScript managed value.                      
        def setBoolCascadeOp( fileName, varName=None ):
            return QtIfwExternalOp.CreateOpFlagFile( ON_INSTALL, 
                    fileName, varName )

        # A boolean state may be evaluated via a file's existence,
        # during any subsequently executed custom scripts you may add...                      
        def getBoolCascadeOp( fileName, destFilePath ):            
            createFileScript = ExecutableScript( "%sEvalFile" % (fileName,),  
                script=([               
                  'set "msg=FALSE"'  
                , 'if exist "{srcFilePath}" set "msg=TRUE"'
                , 'echo %msg% > "{destFilePath}"' 
            ] if IS_WINDOWS else [
                  'msg="FALSE"'
                , '[ -f "{srcFilePath}" ] && msg="TRUE"'   
                , 'echo "${msg}" > "{destFilePath}"' 
            ]), replacements={ 
                  'srcFilePath' : opDataPath( fileName )
                , 'destFilePath': destFilePath  
            })
            return QtIfwExternalOp( script=createFileScript, 
                uninstScript=QtIfwExternalOp.RemoveFileScript( destFilePath ) )

        # An installer variable may be set at various stages in the QtScript.
        # Using QtIfwPackageScript.preOpSupport is a convenient place to
        # set values dynamically (during an installation context).
        # That fires during the event prior to creating the operation objects.
        # I.e. during an initialization phase of the installer. 
        def setInstallerVarInPreOp( pkgScript, varName, value ):
            pkgScript.preOpSupport = QtIfwPackageScript.setValue( 
                varName, value )  
 
        # An installer variable can be written to a data file...                     
        def setVaribaleCascadeOp( fileName, varName ):
            return QtIfwExternalOp.WriteOpDataFile( ON_INSTALL, fileName, 
                        qtIfwDynamicValue( varName ) )

        # Or a dynamic value may be determined in a script and then written 
        # to a data file during an installer operation...                     
        def setTimeCascadeViaScriptOp( fileName ):
            passTimeScript= ExecutableScript( "createTimeFile", script=([               
                'echo %time% > "{timeFilePath}"' 
            ] if IS_WINDOWS else [
                'echo $(date +"%T") > "{timeFilePath}"' 
            ]), replacements={ 
                'timeFilePath': opDataPath( fileName )  
            })
            return QtIfwExternalOp( script=passTimeScript ) 
                        
        # A value can be read from a data file during an installer operation...
        def getVaribaleCascadeOp( fileName, destFilePath ):            
            createFileScript = ExecutableScript( "%sFetch" % (fileName,), 
                script=([               
                  'set /p msg=< "{srcFilePath}"'  
                , 'echo %msg% > "{destFilePath}"' 
            ] if IS_WINDOWS else [
                  'msg=$(cat "{srcFilePath}")'
                , 'echo "${msg}" > "{destFilePath}"' 
            ]), replacements={ 
                  'srcFilePath' : opDataPath( fileName ) 
                , 'destFilePath': destFilePath  
            })
            return QtIfwExternalOp( script=createFileScript, 
                uninstScript=QtIfwExternalOp.RemoveFileScript( destFilePath ) )

        # Assorted "convenience" operations in the library have built-in 
        # options to pivot on the state of a given "run condition file".
        # I.e. the "boolean" temp file concept (previously shown in an explicit
        # manner) maybe applied via these abstractions.        
        if IS_WINDOWS:
            def setAppFoundFileOp( event, appName, is32BitRegistration, fileName ):
                return QtIfwExternalOp.CreateWindowsAppFoundFlagFile( event, 
                    appName, fileName, isAutoBitContext=is32BitRegistration )                                        
        
        elif IS_LINUX:    
            def setPackageFoundFileOp( event, altPkgNames, fileName ):
                return QtIfwExternalOp.CreateExternPackageFoundFlagFile( 
                    event, altPkgNames, fileName )

        def launchAppIfFound( event, exePath, conditionalFileName ):               
            return QtIfwExternalOp.RunProgram( event, 
                exePath, arguments=["Launched By Cascading Scripts"], 
                isHidden=False, isSynchronous=False, 
                runConditionFileName=conditionalFileName, 
                isRunConditionNegated=False )                                   
        
        STATIC_BOOL_FILE_NAME       = "staticBoolData"
        STATIC_BOOL_EVAL_FILE_NAME  = "staticCascadingBool.txt"
        DYNAMIC_BOOL_FILE_NAME      = "dynamicBoolData"
        DYNAMIC_BOOL_EVAL_FILE_NAME = "dynamicCascadingBool.txt"
        VAR_NAME                    = "myDynamicPath"
        VAR_FILE_NAME               = "varData"                
        VAR_FETCH_FILE_NAME         = "cascadingVar.txt"
        TIME_FILE_NAME              = "timeData"
        TIME_FETCH_FILE_NAME        = "cascadingTime.txt"

        refineIntroductionPage( cfg )
        refineFinishedPage( cfg )                                
        pkg = cfg.packages[0]

        # comment any / all of these out to test!
        setInstallerVarInPreOp( pkg.pkgScript, VAR_NAME, QT_IFW_HOME_DIR )   
        #setInstallerVarInPreOp( pkg.pkgScript, VAR_NAME, 
        #                      QtIfwControlScript.toBool( True ) )
        #setInstallerVarInPreOp( pkg.pkgScript, VAR_NAME, 
        #                      QtIfwControlScript.toBool( False ) )
                        
        pkg.pkgScript.externalOps += [ 
            setBoolCascadeOp( STATIC_BOOL_FILE_NAME ), # comment this out to test!    
            getBoolCascadeOp( STATIC_BOOL_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, STATIC_BOOL_EVAL_FILE_NAME ) ),            
            
            setBoolCascadeOp( DYNAMIC_BOOL_FILE_NAME, VAR_NAME ),      
            getBoolCascadeOp( DYNAMIC_BOOL_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, DYNAMIC_BOOL_EVAL_FILE_NAME ) ),            

            setVaribaleCascadeOp( VAR_FILE_NAME, VAR_NAME ),
            getVaribaleCascadeOp( VAR_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, VAR_FETCH_FILE_NAME ) ),
            
            setTimeCascadeViaScriptOp( TIME_FILE_NAME ),
            getVaribaleCascadeOp( TIME_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, TIME_FETCH_FILE_NAME ) ),
        ]         

        APP_NAME     = "Hello Cascading Scripts Example"
        COMPANY_NAME = "Some Company"
        EXE_NAME     = "RunConditionsTest"            
        EXE_PATH = joinPathQtIfw( QT_IFW_APPS_DIR, COMPANY_NAME, APP_NAME, 
                                  normBinaryName( EXE_NAME ) )

        # This demos conditionally launching an app on BOTH install and 
        # uninstall.  Since operations are executed in REVERSE order during 
        # uninstallation, for cascading scripts to flow into each other 
        # correctly, we need to account for that nuance.  As such, this
        # example shows a setAppFoundFileOp call in the list both before
        # and after the launchAppIfFound.    

        if IS_WINDOWS:
            # On Windows, we'll demo an easy means check for app installation 
            # via a registry query done for you.
            # Then, we pivot on if the app we want to launch was indicated 
            # to be installed, from the first operation.  
            IS_32BIT_REG = False
            EXE_PATH = joinPath( QT_IFW_APPS_X86_DIR, COMPANY_NAME, APP_NAME, 
                                 EXE_NAME )
            pkg.pkgScript.externalOps += [
                setAppFoundFileOp( QtIfwExternalOp.ON_INSTALL,
                                   APP_NAME, IS_32BIT_REG, APP_FOUND_FILENAME ),
                launchAppIfFound( QtIfwExternalOp.ON_BOTH, EXE_PATH, APP_FOUND_FILENAME ),
                setAppFoundFileOp( QtIfwExternalOp.ON_UNINSTALL,
                                   APP_NAME, IS_32BIT_REG, APP_FOUND_FILENAME ),                                
            ] 
        elif IS_LINUX:            
            # On Linux, we'll demo an external package lookup / dependency.
            # If the package is installed, the demo app will be launched.
            # Otherwise, it will not. 
            
            REQUIRED_PKG = "screen"
             
            def setPackageFoundFileOp( event, altPkgNames, fileName ):
                return QtIfwExternalOp.CreateExternPackageFoundFlagFile( 
                    event, altPkgNames, fileName )

            pkg.pkgScript.externalOps += [
                setPackageFoundFileOp( QtIfwExternalOp.ON_INSTALL,
                                       REQUIRED_PKG, PKG_FOUND_FILENAME ),
                launchAppIfFound( QtIfwExternalOp.ON_BOTH, EXE_PATH, PKG_FOUND_FILENAME ),
                setPackageFoundFileOp( QtIfwExternalOp.ON_UNINSTALL,
                                       REQUIRED_PKG, PKG_FOUND_FILENAME ),                                
            ] 
                    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
# uncomment to leave scripts in temp directory, post any dynamic modifications 
p.isScriptDebugInstallTest = True   
p.run()       
