## **IExpressConfig**`#!py3 class` { #IExpressConfig data-toc-label=IExpressConfig }



**Instance Methods:** 

 - [`iExpEmbResPath`](#iExpEmbResPath)
 - [`iExpLibPath`](#iExpLibPath)
 - [`iExpResPath`](#iExpResPath)
 - [`scriptType`](#scriptType)

**Instance Attributes:** 

 - [`name`](#name)
 - [`sourceDir`](#sourceDir)
 - [`entryPointScript`](#entryPointScript)
 - [`scriptHeader`](#scriptHeader)
 - [`isScriptDebug`](#isScriptDebug)
 - [`versionInfo`](#versionInfo)
 - [`iconFilePath`](#iconFilePath)
 - [`isAutoElevated`](#isAutoElevated)
 - [`scriptImports`](#scriptImports)
 - [`embeddedResources`](#embeddedResources)
 - [`distResources`](#distResources)
 - [`distDirs`](#distDirs)
 - [`codeSignConfig`](#codeSignConfig)
 - [`codeSignTargets`](#codeSignTargets)
 - [`destDirPath`](#destDirPath)

### *obj*.**iExpEmbResPath**`#!py3 (self, path)` { #iExpEmbResPath data-toc-label=iExpEmbResPath }


### *obj*.**iExpLibPath**`#!py3 (self, path)` { #iExpLibPath data-toc-label=iExpLibPath }


### *obj*.**iExpResPath**`#!py3 (self, path, isEmbedded=False)` { #iExpResPath data-toc-label=iExpResPath }


### *obj*.**scriptType**`#!py3 (self)` { #scriptType data-toc-label=scriptType }


### *obj*.**name** *undefined* { #name data-toc-label=name }

### *obj*.**sourceDir** *undefined* { #sourceDir data-toc-label=sourceDir }

### *obj*.**entryPointScript** *undefined* { #entryPointScript data-toc-label=entryPointScript }

### *obj*.**scriptHeader** *undefined* { #scriptHeader data-toc-label=scriptHeader }

### *obj*.**isScriptDebug** *undefined* { #isScriptDebug data-toc-label=isScriptDebug }

### *obj*.**versionInfo** *undefined* { #versionInfo data-toc-label=versionInfo }

### *obj*.**iconFilePath** *undefined* { #iconFilePath data-toc-label=iconFilePath }

### *obj*.**isAutoElevated** *undefined* { #isAutoElevated data-toc-label=isAutoElevated }

### *obj*.**scriptImports** *undefined* { #scriptImports data-toc-label=scriptImports }

### *obj*.**embeddedResources** *undefined* { #embeddedResources data-toc-label=embeddedResources }

### *obj*.**distResources** *undefined* { #distResources data-toc-label=distResources }

### *obj*.**distDirs** *undefined* { #distDirs data-toc-label=distDirs }

### *obj*.**codeSignConfig** *undefined* { #codeSignConfig data-toc-label=codeSignConfig }

### *obj*.**codeSignTargets** *undefined* { #codeSignTargets data-toc-label=codeSignTargets }

### *obj*.**destDirPath** *undefined* { #destDirPath data-toc-label=destDirPath }


______

## **IExpressInstallerProcess**`#!py3 class` { #IExpressInstallerProcess data-toc-label=IExpressInstallerProcess }



**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

**Instance Methods:** 

 - [`onFinalize`](#onFinalize)
 - [`onIExpressConfig`](#onIExpressConfig)
 - [`onIExpressPackageProcess`](#onIExpressPackageProcess)
 - [`onIExpressPackagesBuilt`](#onIExpressPackagesBuilt)
 - [`onInitialize`](#onInitialize)
 - [`onPackagesStaged`](#onPackagesStaged)
 - [`onPyPackagesBuilt`](#onPyPackagesBuilt)
 - [`onQtIfwConfig`](#onQtIfwConfig)
 - [`run`](#run)

### *IExpressInstallerProcess*.**DIVIDER** *class 'str'* { #DIVIDER data-toc-label=DIVIDER }

### *obj*.**onFinalize**`#!py3 (self)` { #onFinalize data-toc-label=onFinalize }

VIRTUAL
### *obj*.**onIExpressConfig**`#!py3 (self, cfg)` { #onIExpressConfig data-toc-label=onIExpressConfig }

VIRTUAL
### *obj*.**onIExpressPackageProcess**`#!py3 (self, prc)` { #onIExpressPackageProcess data-toc-label=onIExpressPackageProcess }

VIRTUAL
### *obj*.**onIExpressPackagesBuilt**`#!py3 (self, pkgs)` { #onIExpressPackagesBuilt data-toc-label=onIExpressPackagesBuilt }

VIRTUAL
### *obj*.**onInitialize**`#!py3 (self)` { #onInitialize data-toc-label=onInitialize }

VIRTUAL
### *obj*.**onPackagesStaged**`#!py3 (self, cfg, pkgs)` { #onPackagesStaged data-toc-label=onPackagesStaged }

VIRTUAL
### *obj*.**onPyPackagesBuilt**`#!py3 (self, pkgs)` { #onPyPackagesBuilt data-toc-label=onPyPackagesBuilt }

VIRTUAL
### *obj*.**onQtIfwConfig**`#!py3 (self, cfg)` { #onQtIfwConfig data-toc-label=onQtIfwConfig }

VIRTUAL
### *obj*.**run**`#!py3 (self)` { #run data-toc-label=run }



______

## **IExpressPackageProcess**`#!py3 class` { #IExpressPackageProcess data-toc-label=IExpressPackageProcess }



**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

**Instance Methods:** 

 - [`onFinalize`](#onFinalize)
 - [`onIExpressConfig`](#onIExpressConfig)
 - [`onInitialize`](#onInitialize)
 - [`run`](#run)

### *IExpressPackageProcess*.**DIVIDER** *class 'str'* { #DIVIDER data-toc-label=DIVIDER }

### *obj*.**onFinalize**`#!py3 (self)` { #onFinalize data-toc-label=onFinalize }

VIRTUAL
### *obj*.**onIExpressConfig**`#!py3 (self, cfg)` { #onIExpressConfig data-toc-label=onIExpressConfig }

VIRTUAL
### *obj*.**onInitialize**`#!py3 (self)` { #onInitialize data-toc-label=onInitialize }

VIRTUAL
### *obj*.**run**`#!py3 (self)` { #run data-toc-label=run }



______

## **Functions** { #Functions data-toc-label=Functions }

### **batchScriptToExe**`#!py3 (name=None, entryPointScript=None, iExpressConfig=None, distResources=None, distDirs=None)` { #batchScriptToExe data-toc-label=batchScriptToExe }



______

### **iExpEmbResPath**`#!py3 (path, scriptType)` { #iExpEmbResPath data-toc-label=iExpEmbResPath }



______

### **iExpLibPath**`#!py3 (path, scriptType)` { #iExpLibPath data-toc-label=iExpLibPath }



______

### **iExpResPath**`#!py3 (path, scriptType, isEmbedded)` { #iExpResPath data-toc-label=iExpResPath }



______

### **jScriptToExe**`#!py3 (name=None, entryPointScript=None, iExpressConfig=None, distResources=None, distDirs=None)` { #jScriptToExe data-toc-label=jScriptToExe }



______

### **powerShellScriptToExe**`#!py3 (name=None, entryPointScript=None, iExpressConfig=None, distResources=None, distDirs=None)` { #powerShellScriptToExe data-toc-label=powerShellScriptToExe }



______

### **vbScriptToExe**`#!py3 (name=None, entryPointScript=None, iExpressConfig=None, distResources=None, distDirs=None)` { #vbScriptToExe data-toc-label=vbScriptToExe }



______

