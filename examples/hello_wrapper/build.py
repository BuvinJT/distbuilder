from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
    ExecutableScript, normBinaryName, rootFileName, \
    IS_WINDOWS, IS_MACOS, IS_LINUX, QT_IFW_TARGET_DIR, \
    DEBUG_ENV_VAR_NAME, DEBUG_ENV_VAR_VALUE

f = configFactory  = ConfigFactory()
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWrapper"
f.isGui            = True        
f.entryPointPy     = "../run_conditions_app/hello_gui.py"  
#f.isGui            = False 
#f.entryPointPy     = "../run_conditions_app/hello_terminal.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)

# "STANDARD" for direct comparison
#------------------------------------------------------------------------------
f.productName      = "Hello UnWrapped Example"
f.setupName        = "HelloUnWrappedSetup"
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello WorkDir Example"
f.setupName     = "HelloWorkDirSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( workingDir=QT_IFW_TARGET_DIR )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello EnvVars Example"
f.setupName     = "HelloEnvVarsSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( envVars={ "TEST_ENV_VAR": "test" } )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello Args Example"
f.setupName     = "HelloArgsSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( args=["arg1", "arg 2 w spaces", "arg3"] )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello Elevated Example"
f.setupName     = "HelloElevatedSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( isElevated=True )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello MultiWrap Example"
f.setupName     = "HelloMultiWrapSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper(
      isElevated = True 
    , workingDir = QT_IFW_TARGET_DIR 
    , envVars={ "TEST_ENV_VAR": "test" }
    , args=["arg1", "arg 2 w spaces", "arg3"]
)  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
licenseName = "LICENSE.TXT"

if IS_WINDOWS :
    textViewer = "notepad"
    launchScript = (
"""
@echo off
set appname=%~n0
set dirname=%~dp0
start "" "%dirname%\%appname%" %*
start "" {0} "%dirname%\{1}"
""")
elif IS_MACOS :
    # Note: this script is specific for use with a macOS *GUI* app
    textViewer = "TextEdit"
    launchScript = ( 
"""
appname=_`basename "$0"`
dirname=`dirname "$0"`
tmp="${dirname#?}"
if [ "${dirname%$tmp}" != "/" ]; then dirname="$PWD/$dirname"; fi
appParentDir="$dirname/../../.."
open -a {0} "$appParentDir/{1}" 
if [ "{2}" == "{3}" ]; then 
    "$dirname/$appname" "$@"
else 
    "$dirname/$appname" "$@" &
fi   
""")
elif IS_LINUX :
    # Note this is not a "perfect" cross Linux distro / environment example,
    # as this depends upon `gedit` and `screen` being present...
    f.pkgExternalDependencies = [ "screen" ]
    textViewer = "gedit"
    launchScript = (
"""
appname=`basename "$0" | sed s,\.sh$,,`
dirname=`dirname "$0"`
tmp="${dirname#?}"
if [ "${dirname%$tmp}" != "/" ]; then dirname="$PWD/$dirname"; fi
screen -d -m "$dirname/$appname" "$@"
screen -d -m {0} "$dirname/{1}"
""")

# Using explicit string replace because standard string 
# formatting functions took issue with some of the characters
# in the scripts 
launchScript = launchScript.replace( 
    "{0}", textViewer ).replace( 
    "{1}", licenseName ).replace( 
    "{2}", DEBUG_ENV_VAR_NAME ).replace( 
    "{3}", DEBUG_ENV_VAR_VALUE )
        
f.productName   = "Hello WrapperScript Example"
f.setupName     = "HelloWrapperScriptSetup"
f.distResources = ["../hello_world/{0}".format( licenseName ) ]
f.pkgExeWrapper = f.qtIfwExeWrapper( wrapperScript=launchScript )  
#    , isElevated = True 
#    , workingDir = QT_IFW_TARGET_DIR 
#    , envVars={ "TEST_ENV_VAR": "test" }
#    , args=["arg1", "arg 2 w spaces", "arg3"]
#)
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
#p.run()       

#------------------------------------------------------------------------------
if IS_WINDOWS :    
    # Generating a binary "wrapper" over another (well a "proxy" for original),   
    # is only currently supported on the Windows implementation of the library
    licenseName = "LICENSE.TXT"
    textViewer  = "notepad"
    # Note this alternate, more robust, style for defining a script which  
    # includes dynamic variables (e.g. QT_IFW_TARGET_DIR) supplied by the  
    # installer at *run time* - per end user input.
    launchScript = ExecutableScript( rootFileName( f.binaryName ), script=([
        'start "" "{dirName}\{appName}"',
        'start "" {textViewer} "{dirName}\{licenseName}"']), 
        replacements={
        "dirName": QT_IFW_TARGET_DIR, "appName": normBinaryName( f.binaryName ), 
        "textViewer": textViewer, "licenseName": licenseName }
    )        
    f.productName   = "Hello WrapperExe Example"
    f.setupName     = "HelloWrapperExeSetup"
    f.distResources = ["../hello_world/{0}".format( licenseName ) ]
    f.pkgExeWrapper = f.qtIfwExeWrapper( wrapperScript=launchScript, isExe=True )
    p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
    p.isInstallTest = True
    p.run()       
