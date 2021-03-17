from distbuilder import( IExpressPackageProcess, ConfigFactory, 
                         ExecutableScript )

SCRIPT_TYPE = ExecutableScript.VBSCRIPT_EXT

def scriptAndImports( scriptType ):
    entryPointScripts = {
          ExecutableScript.BATCH_EXT      : 'hello_main.bat'
        , ExecutableScript.POWERSHELL_EXT : 'hello_main.ps1'
        , ExecutableScript.VBSCRIPT_EXT   : 'hello_main.vbs'
        , ExecutableScript.JSCRIPT_EXT    : 'hello_main.js'
    }
    scriptImports = {
          ExecutableScript.BATCH_EXT      : ['Popups.bat' ]
        , ExecutableScript.POWERSHELL_EXT : ['Popups.psm1']
        , ExecutableScript.VBSCRIPT_EXT   : ['Popups.vbs' ]
        , ExecutableScript.JSCRIPT_EXT    : ['Popups.js' ]
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
f.version          = (3,5,6,8)
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.entryPointScript = demoScript  
 
class BuildProcess( IExpressPackageProcess ):
    def onIExpressConfig(self, cfg):
        cfg.scriptImports = scriptImports
        #cfg.isScriptDebug = True
        #cfg.isAutoElevated = True

p = BuildProcess( configFactory, isDesktopTarget=True )
p.isExeTest=True 
p.run()       

