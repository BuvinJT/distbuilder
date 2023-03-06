## **IExpressConfig**`#!py3 class` { #IExpressConfig data-toc-label=IExpressConfig }



**Magic Methods:**

 - [`__init__`](#IExpressConfig-init)

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

### **IExpressConfig**`#!py3 ()` { #IExpressConfig-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**iExpEmbResPath**`#!py3 (self, path)` { #iExpEmbResPath data-toc-label=iExpEmbResPath }


### *obj*.**iExpLibPath**`#!py3 (self, path)` { #iExpLibPath data-toc-label=iExpLibPath }


### *obj*.**iExpResPath**`#!py3 (self, path, isEmbedded=False)` { #iExpResPath data-toc-label=iExpResPath }


### *obj*.**scriptType**`#!py3 (self)` { #scriptType data-toc-label=scriptType }


### *obj*.**name** *class 'NoneType'* default: *None* { #name data-toc-label=name }


### *obj*.**sourceDir** *class 'NoneType'* default: *None* { #sourceDir data-toc-label=sourceDir }


### *obj*.**entryPointScript** *class 'NoneType'* default: *None* { #entryPointScript data-toc-label=entryPointScript }


### *obj*.**scriptHeader** *class 'NoneType'* default: *None* { #scriptHeader data-toc-label=scriptHeader }


### *obj*.**isScriptDebug** *class 'bool'* default: *False* { #isScriptDebug data-toc-label=isScriptDebug }


### *obj*.**versionInfo** *class 'NoneType'* default: *None* { #versionInfo data-toc-label=versionInfo }


### *obj*.**iconFilePath** *class 'NoneType'* default: *None* { #iconFilePath data-toc-label=iconFilePath }


### *obj*.**isAutoElevated** *class 'bool'* default: *False* { #isAutoElevated data-toc-label=isAutoElevated }


### *obj*.**scriptImports** *class 'list'* default: *[]* { #scriptImports data-toc-label=scriptImports }


### *obj*.**embeddedResources** *class 'list'* default: *[]* { #embeddedResources data-toc-label=embeddedResources }


### *obj*.**distResources** *class 'list'* default: *[]* { #distResources data-toc-label=distResources }


### *obj*.**distDirs** *class 'list'* default: *[]* { #distDirs data-toc-label=distDirs }


### *obj*.**codeSignConfig** *class 'list'* default: *[]* { #codeSignConfig data-toc-label=codeSignConfig }


### *obj*.**codeSignTargets** *class 'list'* default: *[]* { #codeSignTargets data-toc-label=codeSignTargets }


### *obj*.**destDirPath** *class 'NoneType'* default: *None* { #destDirPath data-toc-label=destDirPath }



______

## **IExpressInstallerProcess**`#!py3 class` { #IExpressInstallerProcess data-toc-label=IExpressInstallerProcess }



**Base Classes:**

_DistBuildProcessBase, _BuildInstallerProcess


**Magic Methods:**

 - [`__init__`](#IExpressInstallerProcess-init)

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

**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

### **IExpressInstallerProcess**`#!py3 (configFactory, name='Windows Script to Binary Installer Process', isDesktopTarget=False, isHomeDirTarget=False)` { #IExpressInstallerProcess-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
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


### *IExpressInstallerProcess*.**DIVIDER** *class 'str'* default: *"------------------------------------"* { #DIVIDER data-toc-label=DIVIDER }



______

## **IExpressPackageProcess**`#!py3 class` { #IExpressPackageProcess data-toc-label=IExpressPackageProcess }



**Base Classes:**

_DistBuildProcessBase, _BuildPackageProcess


**Magic Methods:**

 - [`__init__`](#IExpressPackageProcess-init)

**Instance Methods:** 

 - [`onFinalize`](#onFinalize)
 - [`onIExpressConfig`](#onIExpressConfig)
 - [`onInitialize`](#onInitialize)
 - [`run`](#run)

**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

### **IExpressPackageProcess**`#!py3 (configFactory, name='Windows Script to Binary Package Process', isZipped=False, isDesktopTarget=False, isHomeDirTarget=False)` { #IExpressPackageProcess-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**onFinalize**`#!py3 (self)` { #onFinalize data-toc-label=onFinalize }

VIRTUAL
### *obj*.**onIExpressConfig**`#!py3 (self, cfg)` { #onIExpressConfig data-toc-label=onIExpressConfig }

VIRTUAL
### *obj*.**onInitialize**`#!py3 (self)` { #onInitialize data-toc-label=onInitialize }

VIRTUAL
### *obj*.**run**`#!py3 (self)` { #run data-toc-label=run }


### *IExpressPackageProcess*.**DIVIDER** *class 'str'* default: *"------------------------------------"* { #DIVIDER data-toc-label=DIVIDER }



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

