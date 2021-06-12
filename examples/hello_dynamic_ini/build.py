from distbuilder import PyToBinInstallerProcess, ConfigFactory, startLogging

startLogging()

f = configFactory  = ConfigFactory()
f.productName      = "Hello Dynamic Ini Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "RunConditionsTest"
f.isGui            = True
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
f.distResources    = ["../hello_world/LICENSE.TXT"]
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwDynamicIniSetup"
f.pkgIniFilePaths  = ["test.ini"]  
            
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.isScriptDebugInstallTest=True
p.run()       