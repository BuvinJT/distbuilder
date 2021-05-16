from distbuilder import( RobustInstallerProcess, ConfigFactory,
                         QtIfwPackage, findQtIfwPackage, desktopPath )
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Packages Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloPackagesSetup"

TK_CONFIG_KEY   = "tk"
CLI_CONFIG_KEY  = "cli"
DATA_CONFIG_KEY = "data"

# Define a "Python Package Factory Dictionary" 
# Note: None values for a ConfigFactory results in making a clone of the 
# master, which can then be customization from that "base" within 
# RobustInstallerProcess.onConfigFactory
pyPkgFactories={ TK_CONFIG_KEY:None, CLI_CONFIG_KEY:None }

# OPTIONAL DEMO, UNCOMMENT TO TEST
"""
# Define a raw DATA package
d = dataPkgCfgFactory = ConfigFactory.copy( masterConfigFactory )
d.cfgId         = DATA_CONFIG_KEY
d.pkgType       = QtIfwPackage.Type.DATA
d.productName   = "Data"
d.description   = "Raw File Collection"
d.version       = (1,0,0,0)
d.sourceDir     = "test_res" # or try: desktopPath( "test_res" )
d.distResources = [ "*" ]
dataPkg = d.qtIfwPackage()
ifwPackages=[ dataPkg ]
"""

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
            f.distResources    = ["*.txt","*.md"] 
        elif key==CLI_CONFIG_KEY: 
            f.productName      = "Hello World CLI Example"
            f.description      = "CLI Example"
            f.binaryName       = "HelloWorld"
            f.version          = (1,0,0,0)
            f.isGui            = False
            f.sourceDir        = "../hello_world"
            f.entryPointPy     = "hello.py"  
            f.iconFilePath     = None             
            f.distResources    = ["LICENSE.TXT"]           
                
    def onQtIfwConfig( self, cfg ):     

        def defineComponentsOrder( tkPkg, cliPkg, dataPkg ):
            # Listed / installed in descending order 
            # (i.e. highest *priority* first)
            tkPkg.pkgXml.SortingPriority   = 100
            cliPkg.pkgXml.SortingPriority  = 10
            dataPkg.pkgXml.SortingPriority = 1
            
        def customizeFinishedPage( cfg, tkPkg ):
            # Explicitly enforce which package exe is "primary" 
            # and should be run post installation 
            cfg.configXml.setPrimaryContentExe( tkPkg )           
            
        pkgs    = cfg.packages
        tkPkg   = findQtIfwPackage( pkgs, TK_CONFIG_KEY )            
        cliPkg  = findQtIfwPackage( pkgs, CLI_CONFIG_KEY )        
        dataPkg = findQtIfwPackage( pkgs, DATA_CONFIG_KEY )
        defineComponentsOrder( tkPkg, cliPkg, dataPkg )       
        customizeFinishedPage( cfg, tkPkg )
            
p = BuildProcess( masterConfigFactory, 
                  pyPkgConfigFactoryDict=pyPkgFactories, 
                  ifwPackages=ifwPackages, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
