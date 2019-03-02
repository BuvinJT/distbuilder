from distbuilder import RobustInstallerProcess, ConfigFactory, mergeQtIfwPackages
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Merge Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloMergeSetup"

TK_CONFIG_KEY  = "tk"
CLI_CONFIG_KEY = "cli"
pkgFactories={ TK_CONFIG_KEY:None, CLI_CONFIG_KEY:None }
 
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
            f.isObfuscating    = True
            f.iconFilePath     = "demo.ico"             
        elif key==CLI_CONFIG_KEY: 
            f.productName      = "Hello World CLI Example"
            f.description      = "CLI Example"
            f.binaryName       = "HelloWorld"
            f.version          = (1,0,0,0)
            f.isGui            = False
            f.sourceDir        = "../hello_world"
            f.entryPointPy     = "hello.py"  
            f.isObfuscating    = False
            f.iconFilePath     = None             
            f.distResources    = ["LICENSE"]
            
    def onOpyConfig( self, key, cfg ):
        if key==TK_CONFIG_KEY:    
            cfg.external_modules.extend( [ 'tkinter', 'tkinter.ttk' ] )
            
    def onPyToBinPkgsBuilt( self, pkgs ):
        comboPkg = mergeQtIfwPackages( pkgs, CLI_CONFIG_KEY, TK_CONFIG_KEY )
        comboPkg.pkgXml.DisplayName = "Hello World Examples"
        comboPkg.pkgXml.Description = "Tk and CLI Examples"
    
    def onQtIfwConfig( self, cfg ):
        cfg.configXml.RunProgramDescription = "Start Hello World Tk Example"
            
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isTestingInstall = True
p.run()       
