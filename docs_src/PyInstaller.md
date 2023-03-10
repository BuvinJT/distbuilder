## **PyInstHook**`#!py3 class` { #PyInstHook data-toc-label=PyInstHook }



**Base Classes:**

ExecutableScript


**Magic Methods:**

 - [`__init__`](#PyInstHook-init)

**Instance Methods:** 

 - [`asSnippet`](#asSnippet)
 - [`debug`](#debug)
 - [`exists`](#exists)
 - [`fileName`](#fileName)
 - [`filePath`](#filePath)
 - [`fromBase64`](#fromBase64)
 - [`fromLines`](#fromLines)
 - [`injectLine`](#injectLine)
 - [`read`](#read)
 - [`remove`](#remove)
 - [`toBase64`](#toBase64)
 - [`toLines`](#toLines)
 - [`write`](#write)

**Instance Attributes:** 

 - [`isContribHook`](#isContribHook)
 - [`isRunTimeHook`](#isRunTimeHook)
 - [`hooksDirPath`](#hooksDirPath)

**Class/Static Methods:** 

 - [`linesToStr`](#linesToStr)
 - [`strToLines`](#strToLines)
 - [`typeOf`](#typeOf)

**Class/Static Attributes:** 

 - [`APPLESCRIPT_EXT`](#APPLESCRIPT_EXT)
 - [`BATCH_EXT`](#BATCH_EXT)
 - [`FILE_NAME_PREFIX`](#FILE_NAME_PREFIX)
 - [`JSCRIPT_EXT`](#JSCRIPT_EXT)
 - [`POWERSHELL_EXT`](#POWERSHELL_EXT)
 - [`SHELL_EXT`](#SHELL_EXT)
 - [`SUPPORTED_EXTS`](#SUPPORTED_EXTS)
 - [`VBSCRIPT_EXT`](#VBSCRIPT_EXT)

### **PyInstHook**`#!py3 (name, script=None, isContribHook=True, isRunTimeHook=False)` { #PyInstHook-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**asSnippet**`#!py3 (self)` { #asSnippet data-toc-label=asSnippet }


### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**exists**`#!py3 (self, scriptDirPath=None)` { #exists data-toc-label=exists }


### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**filePath**`#!py3 (self)` { #filePath data-toc-label=filePath }


### *obj*.**fromBase64**`#!py3 (self, data)` { #fromBase64 data-toc-label=fromBase64 }


### *obj*.**fromLines**`#!py3 (self, lines)` { #fromLines data-toc-label=fromLines }


### *obj*.**injectLine**`#!py3 (self, injection, lineNo)` { #injectLine data-toc-label=injectLine }


### *obj*.**read**`#!py3 (self)` { #read data-toc-label=read }


### *obj*.**remove**`#!py3 (self)` { #remove data-toc-label=remove }


### *obj*.**toBase64**`#!py3 (self, toString=False)` { #toBase64 data-toc-label=toBase64 }


### *obj*.**toLines**`#!py3 (self)` { #toLines data-toc-label=toLines }


### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**isContribHook** *class 'NoneType'* default: *None* { #isContribHook data-toc-label=isContribHook }


### *obj*.**isRunTimeHook** *class 'NoneType'* default: *None* { #isRunTimeHook data-toc-label=isRunTimeHook }


### *obj*.**hooksDirPath** *class 'NoneType'* default: *None* { #hooksDirPath data-toc-label=hooksDirPath }


### *PyInstHook*.**linesToStr**`#!py3 (lines)` { #linesToStr data-toc-label=linesToStr }


### *PyInstHook*.**strToLines**`#!py3 (s)` { #strToLines data-toc-label=strToLines }


### *PyInstHook*.**typeOf**`#!py3 (path)` { #typeOf data-toc-label=typeOf }


### *PyInstHook*.**APPLESCRIPT_EXT** *class 'str'* default: *"scpt"* { #APPLESCRIPT_EXT data-toc-label=APPLESCRIPT_EXT }


### *PyInstHook*.**BATCH_EXT** *class 'str'* default: *"bat"* { #BATCH_EXT data-toc-label=BATCH_EXT }


### *PyInstHook*.**FILE_NAME_PREFIX** *class 'str'* default: *"hook-"* { #FILE_NAME_PREFIX data-toc-label=FILE_NAME_PREFIX }


### *PyInstHook*.**JSCRIPT_EXT** *class 'str'* default: *"js"* { #JSCRIPT_EXT data-toc-label=JSCRIPT_EXT }


### *PyInstHook*.**POWERSHELL_EXT** *class 'str'* default: *"ps1"* { #POWERSHELL_EXT data-toc-label=POWERSHELL_EXT }


### *PyInstHook*.**SHELL_EXT** *class 'str'* default: *"sh"* { #SHELL_EXT data-toc-label=SHELL_EXT }


### *PyInstHook*.**SUPPORTED_EXTS** *class 'list'* default: *['sh', 'bat', 'vbs', 'js', 'ps1', 'scpt']* { #SUPPORTED_EXTS data-toc-label=SUPPORTED_EXTS }


### *PyInstHook*.**VBSCRIPT_EXT** *class 'str'* default: *"vbs"* { #VBSCRIPT_EXT data-toc-label=VBSCRIPT_EXT }



______

## **PyInstSpec**`#!py3 class` { #PyInstSpec data-toc-label=PyInstSpec }



**Base Classes:**

PlasticFile


**Magic Methods:**

 - [`__init__`](#PyInstSpec-init)

**Instance Methods:** 

 - [`debug`](#debug)
 - [`fromLines`](#fromLines)
 - [`injectDuplicateDataPatch`](#injectDuplicateDataPatch)
 - [`injectInterpreterOptions`](#injectInterpreterOptions)
 - [`injectLine`](#injectLine)
 - [`path`](#path)
 - [`read`](#read)
 - [`remove`](#remove)
 - [`toLines`](#toLines)
 - [`write`](#write)

**Instance Attributes:** 

 - [`filePath`](#filePath)
 - [`pyInstConfig`](#pyInstConfig)
 - [`warningBehavior`](#warningBehavior)
 - [`isUnBufferedStdIo`](#isUnBufferedStdIo)
 - [`isModInitDebug`](#isModInitDebug)

**Class/Static Methods:** 

 - [`cfgToPath`](#cfgToPath)

**Class/Static Attributes:** 

 - [`WARN_ERROR`](#WARN_ERROR)
 - [`WARN_IGNORE`](#WARN_IGNORE)
 - [`WARN_ONCE`](#WARN_ONCE)

### **PyInstSpec**`#!py3 (filePath=None, pyInstConfig=None, content=None)` { #PyInstSpec-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**fromLines**`#!py3 (self, lines)` { #fromLines data-toc-label=fromLines }


### *obj*.**injectDuplicateDataPatch**`#!py3 (self)` { #injectDuplicateDataPatch data-toc-label=injectDuplicateDataPatch }

This patches a known bug in PyInstaller on Windows. 
PyInstaller analysis can build a set of data file names
which contain "duplicates" due to the Windows 
file system case insensitivity.  This patch eliminates
such duplicates, thus preventing runtime errors in the 
binary produced.
### *obj*.**injectInterpreterOptions**`#!py3 (self)` { #injectInterpreterOptions data-toc-label=injectInterpreterOptions }


### *obj*.**injectLine**`#!py3 (self, injection, lineNo)` { #injectLine data-toc-label=injectLine }


### *obj*.**path**`#!py3 (self)` { #path data-toc-label=path }


### *obj*.**read**`#!py3 (self)` { #read data-toc-label=read }


### *obj*.**remove**`#!py3 (self)` { #remove data-toc-label=remove }


### *obj*.**toLines**`#!py3 (self)` { #toLines data-toc-label=toLines }


### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**filePath** *class 'NoneType'* default: *None* { #filePath data-toc-label=filePath }


### *obj*.**pyInstConfig** *class 'NoneType'* default: *None* { #pyInstConfig data-toc-label=pyInstConfig }


### *obj*.**warningBehavior** *class 'NoneType'* default: *None* { #warningBehavior data-toc-label=warningBehavior }


### *obj*.**isUnBufferedStdIo** *class 'bool'* default: *False* { #isUnBufferedStdIo data-toc-label=isUnBufferedStdIo }


### *obj*.**isModInitDebug** *class 'bool'* default: *False* { #isModInitDebug data-toc-label=isModInitDebug }


### *PyInstSpec*.**cfgToPath**`#!py3 (pyInstConfig)` { #cfgToPath data-toc-label=cfgToPath }


### *PyInstSpec*.**WARN_ERROR** *class 'int'* default: *2* { #WARN_ERROR data-toc-label=WARN_ERROR }


### *PyInstSpec*.**WARN_IGNORE** *class 'int'* default: *0* { #WARN_IGNORE data-toc-label=WARN_IGNORE }


### *PyInstSpec*.**WARN_ONCE** *class 'int'* default: *1* { #WARN_ONCE data-toc-label=WARN_ONCE }



______

## **PyInstallerConfig**`#!py3 class` { #PyInstallerConfig data-toc-label=PyInstallerConfig }

See PyInstaller docs for details on these settings.

**Magic Methods:**

 - [`__init__`](#PyInstallerConfig-init)

**Instance Methods:** 

 - [`toArgs`](#toArgs)

**Instance Attributes:** 

 - [`name`](#name)
 - [`sourceDir`](#sourceDir)
 - [`entryPointPy`](#entryPointPy)
 - [`pyInstSpec`](#pyInstSpec)
 - [`isGui`](#isGui)
 - [`iconFilePath`](#iconFilePath)
 - [`versionInfo`](#versionInfo)
 - [`versionFilePath`](#versionFilePath)
 - [`isAutoElevated`](#isAutoElevated)
 - [`isOneFile`](#isOneFile)
 - [`importPaths`](#importPaths)
 - [`hiddenImports`](#hiddenImports)
 - [`dataFilePaths`](#dataFilePaths)
 - [`binaryFilePaths`](#binaryFilePaths)
 - [`distResources`](#distResources)
 - [`distDirs`](#distDirs)
 - [`codeSignConfig`](#codeSignConfig)
 - [`codeSignTargets`](#codeSignTargets)
 - [`distDirPath`](#distDirPath)
 - [`otherPyInstArgs`](#otherPyInstArgs)
 - [`isSpecFileRemoved`](#isSpecFileRemoved)

### **PyInstallerConfig**`#!py3 ()` { #PyInstallerConfig-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**toArgs**`#!py3 (self, isMakeSpec=False)` { #toArgs data-toc-label=toArgs }


### *obj*.**name** *class 'NoneType'* default: *None* { #name data-toc-label=name }


### *obj*.**sourceDir** *class 'NoneType'* default: *None* { #sourceDir data-toc-label=sourceDir }


### *obj*.**entryPointPy** *class 'NoneType'* default: *None* { #entryPointPy data-toc-label=entryPointPy }


### *obj*.**pyInstSpec** *class 'NoneType'* default: *None* { #pyInstSpec data-toc-label=pyInstSpec }


### *obj*.**isGui** *class 'bool'* default: *False* { #isGui data-toc-label=isGui }


### *obj*.**iconFilePath** *class 'NoneType'* default: *None* { #iconFilePath data-toc-label=iconFilePath }


### *obj*.**versionInfo** *class 'NoneType'* default: *None* { #versionInfo data-toc-label=versionInfo }


### *obj*.**versionFilePath** *class 'NoneType'* default: *None* { #versionFilePath data-toc-label=versionFilePath }


### *obj*.**isAutoElevated** *class 'bool'* default: *False* { #isAutoElevated data-toc-label=isAutoElevated }


### *obj*.**isOneFile** *class 'bool'* default: *True* { #isOneFile data-toc-label=isOneFile }


### *obj*.**importPaths** *class 'list'* default: *[]* { #importPaths data-toc-label=importPaths }


### *obj*.**hiddenImports** *class 'list'* default: *[]* { #hiddenImports data-toc-label=hiddenImports }


### *obj*.**dataFilePaths** *class 'list'* default: *[]* { #dataFilePaths data-toc-label=dataFilePaths }


### *obj*.**binaryFilePaths** *class 'list'* default: *[]* { #binaryFilePaths data-toc-label=binaryFilePaths }


### *obj*.**distResources** *class 'list'* default: *[]* { #distResources data-toc-label=distResources }


### *obj*.**distDirs** *class 'list'* default: *[]* { #distDirs data-toc-label=distDirs }


### *obj*.**codeSignConfig** *class 'list'* default: *[]* { #codeSignConfig data-toc-label=codeSignConfig }


### *obj*.**codeSignTargets** *class 'list'* default: *[]* { #codeSignTargets data-toc-label=codeSignTargets }


### *obj*.**distDirPath** *class 'NoneType'* default: *None* { #distDirPath data-toc-label=distDirPath }


### *obj*.**otherPyInstArgs** *class 'str'* default: *"&lt;empty string&gt;"* { #otherPyInstArgs data-toc-label=otherPyInstArgs }


### *obj*.**isSpecFileRemoved** *class 'bool'* default: *False* { #isSpecFileRemoved data-toc-label=isSpecFileRemoved }



______

## **PyToBinInstallerProcess**`#!py3 class` { #PyToBinInstallerProcess data-toc-label=PyToBinInstallerProcess }



**Base Classes:**

_DistBuildProcessBase, _BuildInstallerProcess


**Magic Methods:**

 - [`__init__`](#PyToBinInstallerProcess-init)

**Instance Methods:** 

 - [`onFinalize`](#onFinalize)
 - [`onIExpressPackagesBuilt`](#onIExpressPackagesBuilt)
 - [`onInitialize`](#onInitialize)
 - [`onMakeSpec`](#onMakeSpec)
 - [`onOpyConfig`](#onOpyConfig)
 - [`onPackagesStaged`](#onPackagesStaged)
 - [`onPyInstConfig`](#onPyInstConfig)
 - [`onPyPackageProcess`](#onPyPackageProcess)
 - [`onPyPackagesBuilt`](#onPyPackagesBuilt)
 - [`onQtIfwConfig`](#onQtIfwConfig)
 - [`run`](#run)

**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

### **PyToBinInstallerProcess**`#!py3 (configFactory, name='Python to Binary Installer Process', isDesktopTarget=False, isHomeDirTarget=False)` { #PyToBinInstallerProcess-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**onFinalize**`#!py3 (self)` { #onFinalize data-toc-label=onFinalize }

VIRTUAL
### *obj*.**onIExpressPackagesBuilt**`#!py3 (self, pkgs)` { #onIExpressPackagesBuilt data-toc-label=onIExpressPackagesBuilt }

VIRTUAL
### *obj*.**onInitialize**`#!py3 (self)` { #onInitialize data-toc-label=onInitialize }

VIRTUAL
### *obj*.**onMakeSpec**`#!py3 (self, spec)` { #onMakeSpec data-toc-label=onMakeSpec }

VIRTUAL
### *obj*.**onOpyConfig**`#!py3 (self, cfg)` { #onOpyConfig data-toc-label=onOpyConfig }

VIRTUAL
### *obj*.**onPackagesStaged**`#!py3 (self, cfg, pkgs)` { #onPackagesStaged data-toc-label=onPackagesStaged }

VIRTUAL
### *obj*.**onPyInstConfig**`#!py3 (self, cfg)` { #onPyInstConfig data-toc-label=onPyInstConfig }

VIRTUAL
### *obj*.**onPyPackageProcess**`#!py3 (self, prc)` { #onPyPackageProcess data-toc-label=onPyPackageProcess }

VIRTUAL
### *obj*.**onPyPackagesBuilt**`#!py3 (self, pkgs)` { #onPyPackagesBuilt data-toc-label=onPyPackagesBuilt }

VIRTUAL
### *obj*.**onQtIfwConfig**`#!py3 (self, cfg)` { #onQtIfwConfig data-toc-label=onQtIfwConfig }

VIRTUAL
### *obj*.**run**`#!py3 (self)` { #run data-toc-label=run }


### *PyToBinInstallerProcess*.**DIVIDER** *class 'str'* default: *"------------------------------------"* { #DIVIDER data-toc-label=DIVIDER }



______

## **PyToBinPackageProcess**`#!py3 class` { #PyToBinPackageProcess data-toc-label=PyToBinPackageProcess }



**Base Classes:**

_DistBuildProcessBase, _BuildPackageProcess


**Magic Methods:**

 - [`__init__`](#PyToBinPackageProcess-init)

**Instance Methods:** 

 - [`onFinalize`](#onFinalize)
 - [`onInitialize`](#onInitialize)
 - [`onMakeSpec`](#onMakeSpec)
 - [`onOpyConfig`](#onOpyConfig)
 - [`onPyInstConfig`](#onPyInstConfig)
 - [`run`](#run)

**Instance Attributes:** 

 - [`isObfuscationTest`](#isObfuscationTest)
 - [`isWarningSuppression`](#isWarningSuppression)
 - [`isUnBufferedStdIo`](#isUnBufferedStdIo)
 - [`isPyInstDupDataPatched`](#isPyInstDupDataPatched)

**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

### **PyToBinPackageProcess**`#!py3 (configFactory, name='Python to Binary Package Process', isZipped=False, isDesktopTarget=False, isHomeDirTarget=False)` { #PyToBinPackageProcess-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**onFinalize**`#!py3 (self)` { #onFinalize data-toc-label=onFinalize }

VIRTUAL
### *obj*.**onInitialize**`#!py3 (self)` { #onInitialize data-toc-label=onInitialize }

VIRTUAL
### *obj*.**onMakeSpec**`#!py3 (self, spec)` { #onMakeSpec data-toc-label=onMakeSpec }

VIRTUAL
### *obj*.**onOpyConfig**`#!py3 (self, cfg)` { #onOpyConfig data-toc-label=onOpyConfig }

VIRTUAL
### *obj*.**onPyInstConfig**`#!py3 (self, cfg)` { #onPyInstConfig data-toc-label=onPyInstConfig }

VIRTUAL
### *obj*.**run**`#!py3 (self)` { #run data-toc-label=run }


### *obj*.**isObfuscationTest** *class 'bool'* default: *False* { #isObfuscationTest data-toc-label=isObfuscationTest }


### *obj*.**isWarningSuppression** *class 'bool'* default: *True* { #isWarningSuppression data-toc-label=isWarningSuppression }


### *obj*.**isUnBufferedStdIo** *class 'bool'* default: *False* { #isUnBufferedStdIo data-toc-label=isUnBufferedStdIo }


### *obj*.**isPyInstDupDataPatched** *class 'NoneType'* default: *None* { #isPyInstDupDataPatched data-toc-label=isPyInstDupDataPatched }


### *PyToBinPackageProcess*.**DIVIDER** *class 'str'* default: *"------------------------------------"* { #DIVIDER data-toc-label=DIVIDER }



______

## **Functions** { #Functions data-toc-label=Functions }

### **PyInstallerMajorMinorVer**`#!py3 ()` { #PyInstallerMajorMinorVer data-toc-label=PyInstallerMajorMinorVer }



______

### **PyInstallerMajorVer**`#!py3 ()` { #PyInstallerMajorVer data-toc-label=PyInstallerMajorVer }



______

### **PyInstallerVersion**`#!py3 ()` { #PyInstallerVersion data-toc-label=PyInstallerVersion }



______

### **installPyInstaller**`#!py3 (version=None)` { #installPyInstaller data-toc-label=installPyInstaller }



______

### **makePyInstSpec**`#!py3 (pyInstConfig, opyConfig=None)` { #makePyInstSpec data-toc-label=makePyInstSpec }



______

### **pyScriptToExe**`#!py3 (name=None, entryPointPy=None, pyInstConfig=<py_installer.PyInstallerConfig object at 0x04056E50>, opyConfig=None, distResources=None, distDirs=None)` { #pyScriptToExe data-toc-label=pyScriptToExe }

returns: (binDir, binPath) 

______

### **uninstallPyInstaller**`#!py3 ()` { #uninstallPyInstaller data-toc-label=uninstallPyInstaller }



______

