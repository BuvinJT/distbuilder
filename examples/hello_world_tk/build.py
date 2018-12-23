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
verInfo = WindowsExeVersionInfo()
verInfo.major = verMajor
verInfo.minor = verMinor
verInfo.micro = verMicro
verInfo.build = verBuild
verInfo.companyName = companyName
verInfo.productName = productName
verInfo.description = description
verInfo.exeName     = exeName
            
pyInstConfig = PyInstallerConfig()
pyInstConfig.isGui           = True
pyInstConfig.iconFilePath    = iconPath
pyInstConfig.versionInfo     = verInfo
binDir, binPath = buildExecutable( exeName, entryPointPy, 
                    opyConfig=opyConfig, pyInstConfig=pyInstConfig )
if IS_TESTING_EXE : run( binPath, isDebug=True )

# Installer creation / testing       
ifwConfig = QtIfwConfig( binDir, pkgName=ifwPkgName, setupExeName=setupName ) 
ifwConfigXml = QtIfwConfigXml( productName, exeName, version, companyName, iconPath )
setupPath = buildInstaller( ifwConfig, ifwConfigXml, isPkgSrcRemoved=True )
setupPath = moveToDesktop( setupPath )
if IS_TESTING_INSTALL : run( setupPath ) #, QT_IFW_VERBOSE_SWITCH )  
