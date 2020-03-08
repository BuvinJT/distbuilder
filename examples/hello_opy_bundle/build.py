from distbuilder import ConfigFactory, PyToBinPackageProcess, absPath, \
    ExtLibHandling, OpyPatch, obfuscatedId
    
f = configFactory  = ConfigFactory()
f.productName      = "Krypto"
f.description      = "Simple Symmetric Encryption Utility"
f.companyLegalName = "Some Company Inc."
f.binaryName       = "Krypto"
f.version          = (1,0,0,0)
f.entryPointPy     = "krypto.py"  
f.isGui            = False        
f.isObfuscating    = True    
f.distResources    = ["krypto.ini"]

class BuildProcess( PyToBinPackageProcess ):
    def onOpyConfig( self, cfg ):    
        
        cfg.extLibHandling = ExtLibHandling.BUNDLE    
        cfg.bundleRounds   = 1

        cfg.skip_path_fragments.extend( ["setup.py"] )
        
        # patching function call with keyword argument
        simpleCryptInitLine42 =( 
            "    {0} = {1}.new({2}, {1}.MODE_CTR, counter={3})".format( 
            obfuscatedId("cipher"), obfuscatedId("AES"), 
            obfuscatedId("cipher_key"), obfuscatedId("counter") ) ) 
        cfg.patches = [ 
            OpyPatch( "simplecrypt/__init__.py", 
                      [ ( 42, simpleCryptInitLine42 ) ] ) 
        ]                
        
p = BuildProcess( configFactory )
p.isTestingObfuscation = True
#p.isTestingExe = True
p.exeTestArgs = [ absPath("clear-text-sample.txt"), 
                  absPath("encrypted-result.bin"), "-o" ]
p.run()       
