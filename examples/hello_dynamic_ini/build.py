from distbuilder import( PyToBinInstallerProcess, ConfigFactory, 
                         ConfigParser, normConfigName, startLogging, joinPath, 
                         QT_IFW_TARGET_DIR, QT_IFW_HOME_DIR ) 
startLogging()

f = configFactory  = ConfigFactory()
f.productName      = "Hello Dynamic Ini Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.setupName        = "HelloDynamicIniSetup"
f.binaryName       = "HelloWorldTk"
f.version          = (1,0,0,0)
f.isGui            = True        
f.sourceDir        = "../hello_world_tk"
f.entryPointPy     = "hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.licensePath      = "../hello_world/LICENSE.TXT"

# define where to find config files / "templates"
CONFIG_FILE_NAME          = "test.ini" 
RELATIVE_CONFIG_DIR_PATH  = "ini"
RELATIVE_CONFIG_FILE_PATH = joinPath( RELATIVE_CONFIG_DIR_PATH, CONFIG_FILE_NAME )

# you might wish to load a config source file in to memory, using the Python 
# built-in ConfigParser, then modify that data dynamically before packaging 
# a revised copy for your distribution  
dynamic_config_name = normConfigName( "dynamic_config" )
dynamic_config_dest = joinPath( RELATIVE_CONFIG_DIR_PATH, dynamic_config_name )
dynamic_config = ConfigParser()
dynamic_config.read( RELATIVE_CONFIG_FILE_PATH ) 
sec='default'
dynamic_config.set( sec, 'is_debug', str(True) )

# Alternately, you could define a config file in a *fully* dynamic manner
# (i.e. without a base source file)
# Note the use of QT_IFW_HOME_DIR and QT_IFW_TARGET_DIR here.  Those IFW 
# variables will be resolved at *runtime* by the installer, to determine
# where the file will be written and what content it will ultimately contain  
fully_dynamic_config_name = normConfigName( "fully_dynamic_config" )
fully_dynamic_config_dest = joinPath( 
    QT_IFW_HOME_DIR, ".dbldr_config_example", fully_dynamic_config_name )
fully_dynamic_config = ConfigParser() 
sec='default'
fully_dynamic_config.add_section( sec )
fully_dynamic_config.set( sec, 'program_dir', QT_IFW_TARGET_DIR )
fully_dynamic_config.set( sec, 'is_debug',    str(False) )
 
# pkgConfigs takes the form { scrDestPathPair : content,... }
# if content is None, it is read from the source path.
# if "content" is a ConfigParser object, a file will be generated from that    
f.pkgConfigs = { 
    # example 1: from a sample file in a sub directory, 
    #            and with the same relative (nested) destination path i.e. ini/test.ini
   (RELATIVE_CONFIG_FILE_PATH, True ): None      
   # example 2: from ConfigParser object
,  (dynamic_config_name, dynamic_config_dest): dynamic_config   
   # example 2: from ConfigParser object
,  (fully_dynamic_config_name, fully_dynamic_config_dest): fully_dynamic_config
}
            
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       