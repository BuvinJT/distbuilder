from sys import stdout, argv
from os.path import normpath, join as joinpath, \
    dirname, realpath, exists
import traceback
from six import PY2 # pip install six
from future.moves.configparser import RawConfigParser # pip install future @UnresolvedImport
import argparse # pip install argparse
import simplecrypt # pip install simple-crypt

THIS_DIR = dirname( realpath( argv[0] ) )
CONFIG_FILE_NAME_DEFAULT = "krypto.ini"       
CONFIG_FILE_SECTION      = "default"
DEFAULT_ENCODING         = "utf-8"

# -----------------------------------------------------------------------------        
def main():
    try :
        scrPath, destPath, configPath, isDecrypt, isOverwrite = getArgs()
        cryptKey, plainEncoding = getConfig( configPath )
        if not isOverwrite and exists( destPath ):
            raise Exception( 
                "Destination file exists! Use overwrite switch (-o) to allow..." )                    
        stdout.write( "Processing..." )            
        with open( scrPath,  'rb' ) as scrFile: scrData = scrFile.read()
        destData = ( toDecrypted( scrData, cryptKey, plainEncoding ) if isDecrypt else
                     toEncrypted( scrData, cryptKey, plainEncoding ) )
        with open( destPath, 'wb' ) as destFile: destFile.write( destData )
        stdout.write( "Success!" )
    except : traceback.print_exc()
                
def getArgs():
    parser = argparse.ArgumentParser(
        description="KRYPTO: Simple Symmetric Encryption Utility" )
    parser.add_argument( "scrPath",  help="path to source file" )
    parser.add_argument( "destPath", help="path to destination file" )
    parser.add_argument( "-c", "--configPath",
        help="(optional) path to config file (defaults to adjacent %s)" 
            % (CONFIG_FILE_NAME_DEFAULT,) )
    parser.add_argument( '-d', "--decrypt", default=False, action='store_true', 
        help="(optional) decrypt switch (defaults to encrypt)" )
    parser.add_argument( '-o', "--overwrite", default=False, action='store_true', 
        help="(optional) overwrite switch (to allow destination overwrite)" )    
    # vars converts the "magic" ArgumentParser object to a dictionary, 
    # which the Opy obfuscation utility is then able to handle
    args = vars(parser.parse_args()) 
    return ( normpath(args.get("scrPath")), normpath(args.get("destPath")),
             args.get("configPath"), args.get("decrypt"), args.get("overwrite") )

def getConfig( configPath=None ):    
    parser = RawConfigParser()
    configPath = ( joinpath( THIS_DIR, CONFIG_FILE_NAME_DEFAULT )
                   if configPath is None else
                   normpath( configPath ) )
    parser.read( configPath )       
    cryptKey = parser.get( CONFIG_FILE_SECTION, "key" )       
    try:    plainEncoding = parser.get( CONFIG_FILE_SECTION, "encoding" )
    except: plainEncoding = DEFAULT_ENCODING
    return ( cryptKey, plainEncoding )
                
def toEncrypted( plainText, cryptKey, plainEncoding ) :
    if PY2 : plainText = plainText.encode( plainEncoding )     
    return simplecrypt.encrypt( cryptKey, plainText )
        
def toDecrypted( encryptedData, cryptKey, plainEncoding ) :    
    plainText = simplecrypt.decrypt( cryptKey, encryptedData )
    if PY2 : plainText = plainText.decode( plainEncoding )
    return plainText   
    
# -----------------------------------------------------------------------------
if __name__ == "__main__" : main()