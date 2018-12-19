import sys
from distbuilder import *  # @UnusedWildImport

# Product details    
exeName      = "HelloWorld"
productName  = "Hello World Example"
version      = "1.0"
publisher    = "Some Company Inc."
versionFile  = "exe_version"
iconPath     = "demo.ico"
entryPointPy = "hello.py"  
ifwPkgName   = "com.somecompany.helloworld"
setupName    = "HelloWorldSetup.exe"

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
pyInstConfig = PyInstallerConfig()
pyInstConfig.isGui           = True
pyInstConfig.iconFilePath    = iconPath
pyInstConfig.versionFilePath = versionFile
binDir, binPath = buildExecutable( exeName, entryPointPy, 
                    opyConfig=opyConfig, pyInstConfig=pyInstConfig )
if IS_TESTING_EXE : run( binPath, isDebug=True )

# Installer creation / testing       
ifwConfig = QtIfwConfig( binDir, pkgName=ifwPkgName, setupExeName=setupName ) 
ifwConfigXml = QtIfwConfigXml( productName, exeName, version, publisher, iconPath )
setupPath = buildInstaller( ifwConfig, ifwConfigXml, isPkgSrcRemoved=True )
setupPath = moveToDesktop( setupPath )
if IS_TESTING_INSTALL : run( setupPath ) #, QT_IFW_VERBOSE_SWITCH )  
