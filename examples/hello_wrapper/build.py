from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
    IS_WINDOWS, IS_MACOS, IS_LINUX, QT_IFW_TARGET_DIR, \
    DEBUG_ENV_VAR_NAME, DEBUG_ENV_VAR_VALUE

f = configFactory  = ConfigFactory()
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWrapper"
f.isGui            = True        
f.entryPointPy     = "hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)

#------------------------------------------------------------------------------
f.productName      = "Hello UnWrapped Example"
f.setupName        = "HelloUnWrappedSetup"
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello WorkDir Example"
f.setupName     = "HelloWorkDirSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( workingDir=QT_IFW_TARGET_DIR )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello Elevated Example"
f.setupName     = "HelloElevatedSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( isElevated=True )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       

#------------------------------------------------------------------------------
f.productName   = "Hello EnvVars Example"
f.setupName     = "HelloEnvVarsSetup"
f.pkgExeWrapper = f.qtIfwExeWrapper( envVars={ "TEST_ENV_VAR": "test" } )  
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
p.run()       

#------------------------------------------------------------------------------
licenseName = "LICENSE"

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
    # not a "perfect" cross Linux distro / environment example,
    # as this depends upon `gedit` and `screen` being present...
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
launchScript = launchScript.replace( "{0}", textViewer )
launchScript = launchScript.replace( "{1}", licenseName )
launchScript = launchScript.replace( "{2}", DEBUG_ENV_VAR_NAME )
launchScript = launchScript.replace( "{3}", DEBUG_ENV_VAR_VALUE )
        
f.productName   = "Hello WrapperScript Example"
f.setupName     = "HelloWrapperScriptSetup"
f.distResources = ["../hello_world/{0}".format( licenseName ) ]
f.pkgExeWrapper = f.qtIfwExeWrapper( wrapperScript=launchScript ) 
#f.pkgExeWrapper.isElevated = True 
#f.pkgExeWrapper.workingDir = QT_IFW_TARGET_DIR 
p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isTestingInstall = True
#p.run()       
