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

# Set a visual style, rather an implicit (platform specific!) default 
# (Choose: MODERN, CLASSIC, MAC, or AERO)
f.ifwWizardStyle    = QtIfwConfigXml.WizardStyle.MODERN
# In MODERN or CLASSIC style, you can add a logo to the upper right corner of 
# the wizard.  This should be a .PNG with either ideally a transparent 
# background, or else a white background (for use with MODERN style). A height
# of 32 to 64px often works well, with a width of 64 to 128px, but adjust that  
# to suit your preferences and other stylizations.   
f.ifwLogoFilePath   = "demo_logo.png"

class BuildProcess( PyToBinInstallerProcess ):
    def onQtIfwConfig( self, cfg ):
        
        def customizeWizard( xml ):                     
            xml.Title      = "Custom Installer"
            xml.TitleColor = "#FF0000"
            #xml.WizardDefaultWidth  = 600
            #xml.WizardDefaultHeight = 600

        def customizeInfo( xml ):                     
            xml.ProductUrl = "http://www.SomeCompany.com"  # Appears in Windows, on the Control Panel Programs List, but yet to see this anywhere else...

        customizeWizard( cfg.configXml )
        customizeInfo( cfg.configXml )
    
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       