from distbuilder import PyToBinInstallerProcess, ConfigFactory, QtIfwInstallerTool

f = configFactory  = ConfigFactory()
f.productName      = "Hello World Tk Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorldTk"
f.isGui            = True        
f.entryPointPy     = "hello.py"  
f.isObfuscating    = True
f.iconFilePath     = "demo.ico" 
f.licensePath      = "LICENSE"
f.version          = (1,0,0,0)
f.setupName        = "HelloWorldTkSetup"

class BuildProcess( PyToBinInstallerProcess ):
    def onOpyConfig( self, cfg ):    
        cfg.external_modules.extend( [ 'tkinter', 'tkinter.ttk' ] )
    #def onPyPackageProcess( self, prc ): prc.isExeTest = True
    def onQtIfwConfig( self, cfg ):       
        script = cfg.packages[0].pkgScript
        script.installTools.append( QtIfwInstallerTool("rh.exe", True) )
        
p = BuildProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.isAutoInstallTest = True
p.run()       