from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport
from distbuilder.opy_library import obfuscatePyLib, OBFUS_DIR_PATH

PIP_PATH      = util._pythonScriptsPath( "pip" )
PIP_INSTALL   = "install" 
PIP_UNINSTALL = "uninstall"

__PIP_INSTALL_TMPLT = '%s %s %s'
__PIP_UNINSTALL_TMPLT = '%s %s --yes %s'
__VCS_BASE_TEMPLT = "%s+%s#egg=%s"
__VCS_SUBDIR_TEMPLT = __VCS_BASE_TEMPLT + "&subdirectory=%s"

# -----------------------------------------------------------------------------
class PipConfig:
    """
    See Pip docs for details on these settings.

    Important Note: source maybe a: 
        package name, git repo url, or local path
    """    
    def __init__( self
                , source = None
                , version = None
                , verEquality = "==" 
                , destPath = None
                , asSource = False
                , incDependencies = True        
                , isForced= False                
                , isUpgrade = False
                , otherPipArgs = "" ) :
        self.pipPath         = PIP_PATH
        self.source          = source
        self.version         = version
        self.verEquality     = verEquality 
        self.destPath        = destPath
        self.asSource        = asSource
        self.incDependencies = incDependencies        
        self.isForced        = isForced                
        self.isUpgrade       = isUpgrade
        self.otherPipArgs    = otherPipArgs # open ended

    def __str__( self ) :
        if self.source is None : 
            self.source = "." # i.e. this directory
        elif exists( self.source ) :
            self.source = '"%s"' % (self.source,) 
        sourceSpec = ( self.source if self.version is None else
            ("%s%s%s" % (self.sourceSpec, self.verEquality, self.version)) )
        destSpec = '--target "%s"' % (self.destPath, ) if self.destPath else "" 
        editableSwitch    = "--editable" if self.asSource else ""
        forcedSwitch      = "--force-reinstall" if self.isForced else ""
        upgradeSwitch     = "--upgrade" if self.isUpgrade else ""
        incDpndncsSwitch  = "" if self.incDependencies else "--no-deps"
        self.otherPipArgs += " "
        tokens = (destSpec, upgradeSwitch, forcedSwitch, incDpndncsSwitch,                     
                  self.otherPipArgs, editableSwitch, sourceSpec )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

# -----------------------------------------------------------------------------   
def installLibrary( name, opyConfig=None, pipConfig=PipConfig() ):

    # Set the pip source and working directory. 
    # Optionally, create obfuscated version of source
    if opyConfig is None:
        wrkDir = None
        if pipConfig.source is None: pipConfig.source = name
    else:
        wrkDir, _ = obfuscatePyLib( name, opyConfig )
        pipConfig.source = None
        
    util._system( __PIP_INSTALL_TMPLT % 
        ( pipConfig.pipPath, PIP_INSTALL, str(pipConfig) ), wrkDir )  

    # Discard temp files
    if( opyConfig is not None and 
        exists( OBFUS_DIR_PATH ) ): 
        removeDir( OBFUS_DIR_PATH )    
    
def uninstallLibrary( name ):
    util._system( __PIP_UNINSTALL_TMPLT % ( PIP_PATH, PIP_UNINSTALL, name ) )  

#https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
#https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support
def vcsUrl( name, baseUrl, vcs="git", subDir=None ):    
    return ( __VCS_BASE_TEMPLT % (vcs, baseUrl, name)            
            if subDir is None else
            __VCS_SUBDIR_TEMPLT % (vcs, baseUrl, name, subDir)
           )
