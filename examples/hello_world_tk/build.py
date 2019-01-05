from distbuilder import PyToBinInstallerProcess, ConfigFactory

factory = ConfigFactory()
factory.productName      = "Hello World Example"
factory.description      = "A Distribution Builder Example"
factory.companyTradeName = "Some Company"
factory.companyLegalName = "Some Company Inc."    
factory.binaryName       = "HelloWorld"
factory.isGui            = True        
factory.entryPointPy     = "hello.py"  
factory.iconFilePath     = "demo.ico" 
factory.version          = (1,0,0,0)
factory.setupName        = "HelloWorldSetup.exe"

class BuildProcess( PyToBinInstallerProcess ):
    def onOpyConfig( self, cfg ):    
        cfg.external_modules.extend( [ 'tkinter', 'tkinter.ttk' ] )
BuildProcess( factory, isObfuscating=True, isMovedToDesktop=True ).run()       