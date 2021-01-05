from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
    QtIfwExternalOp, QtIfwPackageScript, ExecutableScript, \
    joinPath, qtIfwDynamicValue, qtIfwTempDataFilePath, \
    IS_WINDOWS, QT_IFW_DESKTOP_DIR, QT_IFW_HOME_DIR
    
ON_INSTALL = QtIfwExternalOp.ON_INSTALL

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

        def customizeFinishedPage( cfg ):
            # Disable the run program check box by default, for this example. 
            cfg.controlScript.isRunProgChecked = False

        # A boolean state may be represented via a file's existence,
        # created (or not) during an installer operation...                     
        def setBoolCascadeOp( fileName ):
            return QtIfwExternalOp.CreateTempDataFile( ON_INSTALL, fileName )

        # A boolean state may be evaluated via a file's existence,
        # during a subsequent installer operation...                      
        def getBoolCascadeOp( fileName, destFilePath ):            
            createFileScript = ExecutableScript( "createBoolEvalFile", script=([               
                  'set "msg=FALSE"'  
                , 'if exist "{srcFilePath}" set "msg=TRUE"'
                , 'echo %msg% > "{destFilePath}"' 
            ] if IS_WINDOWS else [
                  'msg="FALSE"'
                , '[ -f "{srcFilePath}" ] && msg="TRUE"'   
                , 'echo "${msg}" > "{destFilePath}"' 
            ]), replacements={ 
                  'srcFilePath' : qtIfwTempDataFilePath( fileName )
                , 'destFilePath': destFilePath  
            })
            return QtIfwExternalOp( script=createFileScript, 
                uninstScript=QtIfwExternalOp.RemoveFileScript( destFilePath ) )

        # An installer variable may be set somewhere in the QtScript...
        def setInstallerVaribale( pkgScript, varName ):
            # Package Script preOpSupport is a convenient place to test this
            # Change the value assigned to test the results...
            pkgScript.preOpSupport = QtIfwPackageScript.setValue( 
                varName, QT_IFW_HOME_DIR )  
 
        # An installer variable can be written to a data file...                     
        def setVaribaleCascadeOp( fileName, varName ):
            return QtIfwExternalOp.WriteTempDataFile( ON_INSTALL, fileName, 
                        qtIfwDynamicValue( varName ) )

        # Or a dynamic value may be determined in a script and then written 
        # to a data file during an installer operation...                     
        def setTimeCascadeViaScriptOp( fileName ):
            passTimeScript= ExecutableScript( "createTimeFile", script=([               
                'echo %time% > "{timeFilePath}"' 
            ] if IS_WINDOWS else [
                'echo $(date +"%T") > "{timeFilePath}"' 
            ]), replacements={ 
                'timeFilePath': qtIfwTempDataFilePath( fileName )  
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
                  'srcFilePath' : qtIfwTempDataFilePath( fileName ) 
                , 'destFilePath': destFilePath  
            })
            return QtIfwExternalOp( script=createFileScript, 
                uninstScript=QtIfwExternalOp.RemoveFileScript( destFilePath ) )

        if IS_WINDOWS:
            def setAppFoundFileOp( appName, is32Bit, fileName ):
                return QtIfwExternalOp.CreateWindowsAppFoundTempFile( 
                    QtIfwExternalOp.ON_BOTH, 
                    appName, fileName, isAutoBitContext=(not is32Bit) )                                        

        BOOL_FILE_NAME         = "boolData"
        BOOL_EVAL_FILE_NAME    = "cascadingBool.txt"
        VAR_NAME               = "myDynamicPath"
        VAR_FILE_NAME          = "varData"        
        VAR_FETCH_FILE_NAME    = "cascadingVar.txt"
        TIME_FILE_NAME         = "timeData"
        TIME_FETCH_FILE_NAME   = "cascadingTime.txt"

        customizeFinishedPage( cfg )                                
        pkg = cfg.packages[0]
        setInstallerVaribale( pkg.pkgScript, VAR_NAME )    
                        
        pkg.pkgScript.externalOps += [ 
            setBoolCascadeOp( BOOL_FILE_NAME ), # comment this out to test!    
            getBoolCascadeOp( BOOL_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, BOOL_EVAL_FILE_NAME ) ),            
            
            setVaribaleCascadeOp( VAR_FILE_NAME, VAR_NAME ),
            getVaribaleCascadeOp( VAR_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, VAR_FETCH_FILE_NAME ) ),
            
            setTimeCascadeViaScriptOp( TIME_FILE_NAME ),
            getVaribaleCascadeOp( TIME_FILE_NAME,
                joinPath( QT_IFW_DESKTOP_DIR, TIME_FETCH_FILE_NAME ) ),
        ]         

        if IS_WINDOWS:
            APP_NAME = "Hello World Tk Example"
            IS_32BIT_APP = True
            APP_FOUND_FILENAME = "HelloWorldTkInstalled"
            pkg.pkgScript.externalOps += [
                setAppFoundFileOp( APP_NAME, IS_32BIT_APP, APP_FOUND_FILENAME )                
            ] 
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
# uncomment to leave scripts in temp directory, post any dynamic modifications 
# p.isScriptDebugInstallTest = True   
p.run()       
