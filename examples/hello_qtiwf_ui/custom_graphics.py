from distbuilder import PyToBinInstallerProcess, ConfigFactory, QtIfwConfigXml 

f = configFactory   = ConfigFactory()
f.productName       = "Hello Custom Graphics Example"
f.description       = "A Distribution Builder Example"
f.companyTradeName  = "Some Company"
f.companyLegalName  = "Some Company Inc."    
f.binaryName        = "HelloWorldTk"
f.isGui             = True        
f.entryPointPy      = "../hello_world_tk/hello.py"  
f.iconFilePath      = "../hello_world_tk/demo.ico" 
f.version           = (1,0,0,0)
f.setupName         = "HelloIfwGraphicsSetup"
f.ifwWizardStyle    = QtIfwConfigXml.WizardStyle.MODERN
f.ifwLogoFilePath   = "demo_logo.png"

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):
        cfg.configXml.TitleColor = "#FF0000"
        #cfg.configXml.WizardDefaultWidth  = 800
        #cfg.configXml.WizardDefaultHeight = 800
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       