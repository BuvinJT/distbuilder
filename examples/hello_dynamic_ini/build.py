from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
                         ConfigParser, normConfigName, startLogging, joinPath, 
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

# define where to find config files / "templates"
SCR_CONFIG_DIR="ini"

# Alternately, define a config file dynamically, using the 
# Python built-in ConfigParser class 
dynamic_config = ConfigParser() 
sec='default'
dynamic_config.add_section( sec )
dynamic_config.set( sec, 'program_dir', QT_IFW_TARGET_DIR )
dynamic_config.set( sec, 'is_debug',    str(False) )

# pkgConfigs takes the form { scrDestPathPair : content,... }
# if content is None, it is read from the source path.
# Note that ConfigParser objects maybe passed as "content"!    
f.pkgConfigs = { 
    # example 1: from a sample file in a sub directory, 
    #            and with the same relative (nested) destination path i.e. ini/test.ini
   (joinPath(SCR_CONFIG_DIR,"test.ini"), True ): None      
   # example 2: from ConfigParser object
,  normConfigName("dynamic_config"): dynamic_config    
}
            
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.isScriptDebugInstallTest=True
p.run()       