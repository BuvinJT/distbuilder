from distbuilder import RobustInstallerProcess, ConfigFactory, \
    mergeQtIfwPackages, nestQtIfwPackage  
  
f = masterConfigFactory = ConfigFactory()
f.productName      = "Hello Merge Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloMergeSetup"

# Define a "Package Factory Dictionary" 
# Note: None values for a ConfigFactory results in making a clone of the 
# master, which can then be customization from that "base" within 
# RobustInstallerProcess.onConfigFactory
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
            f.iconFilePath     = "demo.ico"             
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
                        
    def onPackagesStaged( self, cfg, pkgs ):
        # Swap these commented out functions to test alternate merge types
        comboPkg = mergeQtIfwPackages( pkgs, CLI_CONFIG_KEY, TK_CONFIG_KEY )
        #comboPkg = nestQtIfwPackage( pkgs, CLI_CONFIG_KEY, TK_CONFIG_KEY )

        # Note: it may be slightly more efficient to set these to the desired 
        # values prior to the package merge, but this illustrates how you can  
        # revise these configurations manually at this point in the build 
        # process.  
        configXml = cfg.configXml
        configXml.RunProgramDescription = "Start Hello World Tk Example"
        print( "Regenerating {0}...".format( configXml.path() ) )
        configXml.debug()
        configXml.write()
        
        pkgXml = comboPkg.pkgXml
        pkgXml.DisplayName = "Hello World Examples"
        pkgXml.Description = "Tk and CLI Examples"
        print( "Regenerating {0}...".format( pkgXml.path() ) )
        pkgXml.debug()
        pkgXml.write()
                    
p = BuildProcess( masterConfigFactory, pyPkgConfigFactoryDict=pkgFactories, 
                  isDesktopTarget=True )
p.isInstallTest = True
p.run()       
