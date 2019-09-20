from distbuilder import RobustInstallerProcess, \
    IS_LINUX, normBinaryName, normIconName, \
    QtIfwShortcut, QtIfwPackageScript
    
from distbuilder.qt_cpp import qmakeInit

args, configFactory = qmakeInit()
f = configFactory

helloQtPkg = f.qtIfwPackage()
helloQtPkg.srcExePath = args.binaryPath
helloQtPkg.exeName = normBinaryName(args.binaryPath) #eww...
helloQtPkg.isGui = True
helloQtPkg.isQtCppExe = True
helloQtPkg.isMingwExe = (args.binCompiler=='mingw')

class BuildProcess( RobustInstallerProcess ): 
    def onQtIfwConfig( self, cfg ):
        cfg.qtBinDirPath = args.qtBinDirPath  

        if cfg.packages is None: return    
        
        firstPkg = cfg.packages[0]          
          
        if cfg.configXml.RunProgram is None:            
            cfg.configXml.RunProgramDescription = firstPkg.pkgXml.DisplayName
            cfg.configXml.primaryContentExe = normBinaryName( firstPkg.exeName, 
                                                              isGui=firstPkg.isGui )                         
            cfg.configXml.setDefaultPaths()        
            
        pngIconResPath = ( normIconName(f.iconFilePath, isPathPreserved=True)
                           if IS_LINUX else None )             
        versionStr = args.version
                
        defShortcut= QtIfwShortcut(                    
                        productName=f.productName,
                        exeName=firstPkg.exeName,    
                        exeVersion=versionStr,
                        isGui=firstPkg.isGui,                                  
                        pngIconResPath=pngIconResPath )  
        cfg.packages[0].pkgScript = QtIfwPackageScript( firstPkg.name, 
                    shortcuts=[ defShortcut ],
                    fileName=f.ifwPkgScriptName,
                    script=f.ifwPkgScriptText, 
                    scriptPath=f.ifwPkgScriptPath )
                    
p = BuildProcess( configFactory, ifwPackages=[helloQtPkg],
                  isDesktopTarget=True )
p.isTestingInstall = True
p.run()
