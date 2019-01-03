import sys
from distbuilder import *  # @UnusedWildImport

# Product details    
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
       
# Process options
IS_OBFUSCATING         = True
IS_TESTING_OBFUSCATION = False
IS_TESTING_EXE         = False
IS_TESTING_INSTALL     = True

# Obfuscation settings / testing
if IS_OBFUSCATING :
    opyConfig = factory.opyConfig() 
    opyConfig.external_modules.extend( [ 'tkinter', 'tkinter.ttk' ] )
    if IS_TESTING_OBFUSCATION:
        obDir, obPath = obfuscatePy( opyConfig )
        runPy( obPath )
        sys.exit()
else: opyConfig = None

# Executable creation / testing
pyInstConfig = factory.pyInstallerConfig()
binDir, binPath = buildExecutable( pyInstConfig=pyInstConfig, 
                                   opyConfig=opyConfig )
if IS_TESTING_EXE : run( binPath, isDebug=True )

# Installer creation / testing        
ifwConfig = factory.qtIfwConfig()
setupPath = buildInstaller( ifwConfig, isPkgSrcRemoved=True )
setupPath = moveToDesktop( setupPath )
if IS_TESTING_INSTALL : run( setupPath ) #, QT_IFW_VERBOSE_SWITCH )  
