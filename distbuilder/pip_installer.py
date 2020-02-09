from distbuilder import util 
from distbuilder.util import *  # @UnusedWildImport
from distbuilder.opy_library import obfuscatePy, OBFUS_DIR_PATH

PIP_CMD_BASE = '"' + PYTHON_PATH + '" -m pip'

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
                , isForced = False         
                , isCacheUsed = True       
                , isUpgrade = False
                , otherPipArgs = "" ) :
        self.pipCmdBase      = PIP_CMD_BASE
        self.source          = source
        self.version         = version
        self.verEquality     = verEquality 
        self.destPath        = destPath
        self.asSource        = asSource
        self.incDependencies = incDependencies        
        self.isForced        = isForced
        self.isCacheUsed     = isCacheUsed                
        self.isUpgrade       = isUpgrade
        self.otherPipArgs    = otherPipArgs # open ended

    def __str__( self ) :
        if self.source is None : 
            self.source = "." # i.e. this directory
        elif exists( self.source ) :
            self.source = '"%s"' % (self.source,) 
        sourceSpec = ( self.source if self.version is None else
            ("%s%s%s" % (self.source, self.verEquality, self.version)) )
        destSpec = '--target "%s"' % (self.destPath, ) if self.destPath else "" 
        editableSwitch    = "--editable" if self.asSource else ""
        forcedSwitch      = "--force-reinstall" if self.isForced else ""
        upgradeSwitch     = "--upgrade" if self.isUpgrade else ""
        noCacheSwitch     = "" if self.isCacheUsed else "--no-cache-dir" 
        incDpndncsSwitch  = "" if self.incDependencies else "--no-deps"
        self.otherPipArgs += " "
        tokens = (destSpec, upgradeSwitch, forcedSwitch, incDpndncsSwitch, 
                  noCacheSwitch, self.otherPipArgs, editableSwitch, sourceSpec )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )         

# -----------------------------------------------------------------------------
def installLibraries( *libs ):
        
    # Note: *libs allows a tuple of arbitrary length to be provided as  
    # series of arguments (like varargs in C++/Java...)
    # Else, a single tuple or list, may be passed
    # OR a single item like a string will be converted to a 1 item tuple...
    if len(libs)==1: libs=libs[0]
    if not isinstance(libs, tuple) and not isinstance(libs, list): libs=(libs,)
         
    for lib in libs:
        # each lib item maybe a tuple/list, and then treated as
        # the argument list for installLibrary, or it may be 
        # just a string, representing the name  
        if isinstance(lib, tuple) or isinstance(lib, list):
            try   : name      = lib[0]
            except: name      = None  
            try   : opyConfig = lib[1]
            except: opyConfig = None  
            try   : pipConfig = lib[2]
            except: pipConfig = PipConfig()  
            installLibrary( name, opyConfig, pipConfig )
        elif isinstance(lib, dict): installLibrary( **lib )                        
        else: installLibrary( lib )
                
def installLibrary( name, opyConfig=None, pipConfig=None ):
 
    if pipConfig is None : pipConfig=PipConfig()
    
    # Set the pip source and working directory. 
    # Optionally, create obfuscated version of source
    if opyConfig :
        opyConfig.name = name
        opyConfig.isLibrary = True
        wrkDir, _ = obfuscatePy( opyConfig )
        pipConfig.source = None
    else :                
        wrkDir = None
        if pipConfig.source is None: pipConfig.source = name

    util._system( __PIP_INSTALL_TMPLT % 
        ( pipConfig.pipCmdBase, PIP_INSTALL, str(pipConfig) ), wrkDir )  

    # Discard temp files
    if( opyConfig is not None and 
        exists( OBFUS_DIR_PATH ) ): 
        removeDir( OBFUS_DIR_PATH )    
    
def uninstallLibrary( name ):
    util._system( __PIP_UNINSTALL_TMPLT % ( PIP_CMD_BASE, PIP_UNINSTALL, name ) )  

#https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
#https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support
def vcsUrl( name, baseUrl, vcs="git", subDir=None ):    
    return ( __VCS_BASE_TEMPLT % (vcs, baseUrl, name)            
            if subDir is None else
            __VCS_SUBDIR_TEMPLT % (vcs, baseUrl, name, subDir)
           )
