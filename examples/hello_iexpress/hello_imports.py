from distbuilder import( IExpressPackageProcess, ConfigFactory, 
                         ExecutableScript )

SCRIPT_TYPE = ExecutableScript.VBSCRIPT_EXT

def scriptAndImports( scriptType ):
    entryPointScripts = {
          ExecutableScript.BATCH_EXT      : 'hello_main.bat'
        , ExecutableScript.POWERSHELL_EXT : 'hello_main.ps1'
        , ExecutableScript.VBSCRIPT_EXT   : 'hello_main.vbs'
    }
    scriptImports = {
          ExecutableScript.BATCH_EXT      : ['popup.bat']
        , ExecutableScript.POWERSHELL_EXT : ['popup.ps1']
        , ExecutableScript.VBSCRIPT_EXT   : ['popup.vbs']
    }
    path = entryPointScripts.get( scriptType )     
    if not path: raise Exception( "Invalid Script Type!" )
    return( ExecutableScript( "ImportDemo", extension=scriptType, 
                              scriptPath=path )
          , scriptImports.get( scriptType ) ) 

demoScript, scriptImports = scriptAndImports( SCRIPT_TYPE )

f = configFactory  = ConfigFactory()
f.productName      = "Hello Script Imports Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloScriptImports"
f.version          = (1,0,0,0)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = demoScript  
 
class BuildProcess( IExpressPackageProcess ):
    def onIExpressConfig(self, cfg):
        cfg.scriptImports = scriptImports
        #cfg.isScriptDebug = True

p = BuildProcess( configFactory, isDesktopTarget=True )
p.isExeTest=True 
p.run()       

