from distbuilder import util    # @UnusedImport
from distbuilder.util import *  # @UnusedWildImport

_RES_DIR_PATH = util._toLibResPath( joinPath( "code_sign_res", 
    ("linux" if IS_LINUX else "macos" if IS_MACOS else "windows") ) )

# WINDOWS CODE SIGNING
#------------------------------------------------------------------------------
SIGNTOOL_PATH_ENV_VAR = "SIGNTOOL_PATH"
            
class SignToolConfig:

    DEFAULT_DIGEST           = "sha256"
    DEFAULT_TIMESTAMP_SERVER = "http://timestamp.digicert.com"
    
    __RES_DIR_NAME = "signtool"
    __MSI_NAME     = "Windows SDK Signing Tools-x86_en-us.msi"
    
    __WINDOWS_KITS_DIR = r"Windows Kits\10\bin\10.0.19041.0" 
    __INTEL_32BIT_DIR  = "x86"
    __INTEL_64BIT_DIR  = "x64"
    __ARM_32BIT_DIR    = "arm"
    __ARM_64BIT_DIR    = "arm64"
    __SIGNTOOL_NAME    = "signtool.exe"

    @staticmethod
    def _builtInInstallerPath():    
        return joinPath( _RES_DIR_PATH, 
            SignToolConfig.__RES_DIR_NAME, SignToolConfig.__MSI_NAME )

    @staticmethod
    def _defaultSignToolPath( isVerified=False ):    
        if IS_ARM_CPU:
            subDirName =( SignToolConfig.__ARM_32BIT_DIR 
                          if IS_32_BIT_CONTEXT else 
                          SignToolConfig.__ARM_64BIT_DIR )
        else:
            subDirName =( SignToolConfig.__INTEL_32BIT_DIR 
                          if IS_32_BIT_CONTEXT else 
                          SignToolConfig.__INTEL_64BIT_DIR )                  
        path = joinPath( util._winProgs86DirPath(), 
            SignToolConfig.__WINDOWS_KITS_DIR, subDirName, 
            SignToolConfig.__SIGNTOOL_NAME )
        if isVerified and not isFile( path ): path = None            
        return path 

    def __init__( self, pfxFilePath=None, pfxPassword=None ):
  
        self.pfxFilePath  = pfxFilePath
        self.pfxPassword  = pfxPassword
 
        self.signToolPath = None # if None, this will be auto resolved 
       
        self.fileDigest         = SignToolConfig.DEFAULT_DIGEST        
        self.timeStampDigest    = SignToolConfig.DEFAULT_DIGEST
        self.timeStampServerUrl = SignToolConfig.DEFAULT_TIMESTAMP_SERVER
        self.otherSignToolArgs  = ""
        
        self.isDebugMode = True

    def __str__( self ) :
        if not isFile( self.pfxFilePath ):
            raise Exception( 
                "Missing or invalid pfx path in SignToolConfig: %s" %
                (self.pfxFilePath,) )        
        operation       = "sign"        
        verbose         = '/v' if self.isDebugMode else ''
        fileDigest      = "/fd %s" % (self.fileDigest,)
        timeStampServer = "/tr %s" % (self.timeStampServerUrl,)
        timeStampDigest = "/td %s" % (self.timeStampDigest,)
        pfxFile         = '/f "%s"%s' % (self.pfxFilePath, 
            ' "%s"' % (self.pfxPassword,) if self.pfxPassword else "" )                                
        tokens = (operation, verbose, fileDigest, 
                  timeStampServer, timeStampDigest, pfxFile,
                  self.otherSignToolArgs)
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )        

def __useSignTool( exePath, signToolConfig ):
    __validateSignToolConfig( signToolConfig )
    cmd = '"%s" %s "%s"' % ( signToolConfig.signToolPath, 
                             str(signToolConfig), exePath )
    if not util._isSystemSuccess( cmd ): 
        raise Exception( 'FAILED to code sign "%s"' % (exePath,) )
    print( "Signed successfully!" )
    return exePath           

def __validateSignToolConfig( cfg ):
    if not isFile( cfg.pfxFilePath ):         
        raise Exception( "Missing or invalid PFX file path: %s" % 
                         (cfg.pfxFilePath,) )
    if cfg.signToolPath is None: 
        cfg.signToolPath = getenv( SIGNTOOL_PATH_ENV_VAR )    
    if cfg.signToolPath is None: 
        cfg.signToolPath = (
            SignToolConfig._defaultSignToolPath( isVerified=True ) )    
    if cfg.signToolPath is None: 
        cfg.signToolPath = __installSignTool()   
    if cfg.signToolPath is None: 
        raise Exception( "Valid SignTool path required" )

def __installSignTool():
    print( "Installing SignTool utility...\n" )
    if not util._isSystemSuccess( SignToolConfig._builtInInstallerPath() ): 
        raise Exception( "SignTool installation FAILED" )
    return SignToolConfig._defaultSignToolPath( isVerified=True )

#------------------------------------------------------------------------------
MAKECERT_PATH_ENV_VAR = "MAKECERT_PATH"
            
class MakeCertConfig:

    NO_MAX_CHILDREN = 0
    LIFETIME_SIGNING_EKU = '1.3.6.1.5.5.7.3.3,1.3.6.1.4.1.311.10.3.13'
        
    __RES_DIR_NAME = "makecert"

    __INTEL_32BIT_DIR  = "x86"
    __INTEL_64BIT_DIR  = "x64"
    __ARM_32BIT_DIR    = "arm" # Not actually present...
    __ARM_64BIT_DIR    = "arm64"
    __MAKECERT_NAME    = "makecert.exe"

    __SUBJECT_KEY_EXT  = ".pvk"
    __CA_CERT_EXT      = ".cer"
    
    @staticmethod
    def _builtInMakeCertPath( isVerified=False ):    
        if IS_ARM_CPU:
            subDirName =( MakeCertConfig.__ARM_32BIT_DIR 
                          if IS_32_BIT_CONTEXT else 
                          MakeCertConfig.__ARM_64BIT_DIR )
        else:
            subDirName =( MakeCertConfig.__INTEL_32BIT_DIR 
                          if IS_32_BIT_CONTEXT else 
                          MakeCertConfig.__INTEL_64BIT_DIR )                  
        path = joinPath( _RES_DIR_PATH, 
            MakeCertConfig.__RES_DIR_NAME, subDirName, 
            MakeCertConfig.__MAKECERT_NAME )
        if isVerified and not isFile( path ): path = None            
        return path 

    def __init__( self, companyName, destDirPath=None ):
    
        self.commonName  = companyName
        self.destDirPath = destDirPath if destDirPath else THIS_DIR
        
        outputRoot = companyName.replace(" ", "").replace(".", "")        
        self.subjectKeyPath   = joinPath( self.destDirPath, 
            joinExt( outputRoot, MakeCertConfig.__SUBJECT_KEY_EXT ) )
        self.certPath         = joinPath( self.destDirPath, 
            joinExt( outputRoot, MakeCertConfig.__CA_CERT_EXT) )
        
        self.makeCertPath = None # if None, this will be auto resolved 

        self.maxCertChildren  = MakeCertConfig.NO_MAX_CHILDREN       
        self.enhancedKeyUsage = MakeCertConfig.LIFETIME_SIGNING_EKU
        self.otherMakeCertArgs  = ""
        
        self.isDebugMode = True

    def __str__( self ) :
        name               = '/n "CN=%s"' % (self.commonName,)
        selfSignedRootCert = '/r'
        maxCertChildren    = '/h %d' % (self.maxCertChildren,)
        enhancedKeyUsage   = '/eku %s' % (self.enhancedKeyUsage,)
        subjectKeyPath     = '/sv "%s"' % (self.subjectKeyPath,)
        certPath           = '"%s"' % (self.certPath,)                       
        tokens = (name, selfSignedRootCert, maxCertChildren,
                  enhancedKeyUsage,  self.otherMakeCertArgs,
                  subjectKeyPath, certPath )
        return ' '.join( (('%s ' * len(tokens)) % tokens).split() )        

def __useMakeCert( makeCertConfig ):
    __validateMakeCertConfig( makeCertConfig )
    cmd = '"%s" %s' % ( makeCertConfig.makeCertPath, str(makeCertConfig) )
    if not util._isSystemSuccess( cmd ): 
        raise Exception( 'FAILED to generate code signing certificates' )
    print( "Generated successfully!" )
    return makeCertConfig.destDirPath

def __validateMakeCertConfig( cfg ):
    if not isDir( cfg.destDirPath ): makeDir( cfg.destDirPath )         
    if cfg.makeCertPath is None: 
        cfg.makeCertPath = getenv( MAKECERT_PATH_ENV_VAR )    
    if cfg.makeCertPath is None: 
        cfg.makeCertPath = MakeCertConfig._builtInMakeCertPath()
    if cfg.makeCertPath is None: 
        raise Exception( "Valid MakeCert path required" )

#------------------------------------------------------------------------------
def generateCerts( config ):
    print( "Generating code signing certificates...\n" )
    if IS_WINDOWS: return __useMakeCert( config )    
    #TODO: SUPPORT OTHER PLATFORMS!!!
    util._onPlatformErr()
        
def signExe( exePath, config ):
    exePath = normBinaryName( exePath, isPathPreserved=True )
    print( "Code signing %s...\n" % (exePath,) )
    if IS_WINDOWS: return __useSignTool( exePath, config )    
    #TODO: SUPPORT OTHER PLATFORMS!!!
    util._onPlatformErr()
        