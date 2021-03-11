from distbuilder import IExpressPackageProcess, ConfigFactory, ExecutableScript

f = configFactory  = ConfigFactory()
f.productName      = "Hello Script Imports Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloScriptImports"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = ExecutableScript( "main", 
    extension=ExecutableScript.POWERSHELL_EXT, scriptPath="hello_main.ps1" ) 
 
class BuildProcess( IExpressPackageProcess ):
    def onIExpressConfig(self, cfg):
        cfg.scriptImports = [ "popup.psm1" ]

p = BuildProcess( configFactory, isDesktopTarget=True )
p.isExeTest=True 
p.run()       

