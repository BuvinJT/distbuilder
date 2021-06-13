from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
                         ConfigParser, normConfigName, startLogging, 
                         QT_IFW_TARGET_DIR ) 

startLogging()

f = configFactory  = ConfigFactory()
f.productName      = "Hello Dynamic Ini Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.distResources    = ["../hello_world/LICENSE.TXT"]
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwDynamicIniSetup"

dynamic_config = ConfigParser() 
sec='default'
dynamic_config.add_section( sec )
dynamic_config.set( sec, 'program_dir', QT_IFW_TARGET_DIR )
dynamic_config.set( sec, 'is_debug',    str(False) )

f.pkgConfigs = { "test.ini": None                                  # from file   
               ,  normConfigName("dynamic_config"): dynamic_config # from object
               }
            
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.isScriptDebugInstallTest=True
p.run()       