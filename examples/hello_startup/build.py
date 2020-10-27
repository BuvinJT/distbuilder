from distbuilder import PyToBinInstallerProcess, ConfigFactory

f = configFactory  = ConfigFactory()
f.productName      = "Hello Startup Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloStartup"
f.isGui            = True        
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
#f.isGui            = False 
#f.entryPointPy     = "../run_conditions_app/hello_terminal.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.startOnBoot      = True # options: CURRENT_USER (same as True), ALL_USERS
f.setupName        = "HelloStartupSetup"

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       
