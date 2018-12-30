import sys
from distbuilder import *  # @UnusedWildImport

# Product details    
exeName      = "HelloWorld"
productName  = "Hello World Example"
description  = "A Distribution Builder Example"
verMajor     = 1
verMinor     = 0
verMicro     = 0
verBuild     = 0
version      = "%d.%d.%d.%d" % (verMajor,verMinor,verMicro,verBuild)
companyName  = "Some Company Inc."
iconPath     = "demo.ico"
entryPointPy = "hello.py"  
ifwPkgName   = "com.somecompany.helloworld"
setupName    = "HelloWorldSetup.exe"

factory = ConfigFactory()
factory.productName      = "Hello World Example"
factory.description      = "A Distribution Builder Example"
factory.companyTradeName = "Some Company"
factory.companyLegalName = "Some Company Inc."    
factory.binaryName       = "HelloWorld"
factory.isGui            = True        
factory.entryPointPy     = "hello.py"  
factory.iconFilePath     = "demo.ico" 
factory.verMajor         = 1
factory.verMinor         = 0
factory.verMicro         = 0
factory.verBuild         = 0 
factory.setupName        = "HelloWorldSetup.exe"
factory.ifwPkgName       = "com.somecompany.helloworld"

pyInstConfig = factory.pyInstallerConfig()
       
# Process options
IS_OBFUSCATING         = True
IS_TESTING_OBFUSCATION = False
IS_TESTING_EXE         = False
IS_TESTING_INSTALL     = True

# Obfuscation settings / testing
if IS_OBFUSCATING :
    opyConfig = OpyConfig() 
    opyConfig.external_modules.extend( [ 'tkinter', 'tkinter.ttk' ] )
    if IS_TESTING_OBFUSCATION:
        obDir, obPath = obfuscatePy( exeName, entryPointPy, opyConfig )
        runPy( obPath )
        sys.exit()
else: opyConfig = None

# Executable creation / testing
binDir, binPath = buildExecutable( pyInstConfig=pyInstConfig, 
                                   opyConfig=opyConfig )
if IS_TESTING_EXE : run( binPath, isDebug=True )

# Installer creation / testing        
ifwConfigXml = QtIfwConfigXml( productName, exeName, version, companyName, iconPath )
ifwPackageScript = QtIfwPackageScript( ifwPkgName, exeName=exeName )
ifwPackageXml = QtIfwPackageXml( ifwPkgName, productName, description, version, 
                                 scriptName=ifwPackageScript.fileName )
ifwConfig = QtIfwConfig( binDir, pkgName=ifwPkgName, setupExeName=setupName, 
    configXml=ifwConfigXml, pkgXml=ifwPackageXml, pkgScript=ifwPackageScript )
setupPath = buildInstaller( ifwConfig, isPkgSrcRemoved=True )
setupPath = moveToDesktop( setupPath )
if IS_TESTING_INSTALL : run( setupPath ) #, QT_IFW_VERBOSE_SWITCH )  
