from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
        startLogging, joinPathQtIfw, QT_IFW_HOME_DIR )

# Refer to the QtIFW built-in operations list: 
#     https://doc.qt.io/qtinstallerframework/operations.html

startLogging()

f = configFactory  = ConfigFactory()
f.productName      = "Hello Installer Built-in Ops Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.distResources    = ["../hello_world/LICENSE.TXT"]
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwBuiltOpsInSetup"
 
class BuildProcess( PyToBinInstallerProcess ):

    def onQtIfwConfig( self, cfg ):            

        def addMakeDataDirOp( pkg ):
            dirPath  = joinPathQtIfw( QT_IFW_HOME_DIR, "distbuilder-example" )
            filePath = joinPathQtIfw( dirPath, "distbuilder-example.txt" )
            pkg.pkgScript.addSimpleOperation( "Mkdir", dirPath )
            pkg.pkgScript.addSimpleOperation( "AppendFile", 
                                              [ filePath, "Sample data." ] )
                                    
        pkg = cfg.packages[0]
        addMakeDataDirOp( pkg )
            
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       