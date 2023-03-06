## **ConfigFactory**`#!py3 class` { #ConfigFactory data-toc-label=ConfigFactory }



**Magic Methods:**

 - [`__init__`](#ConfigFactory-init)

**Instance Methods:** 

 - [`exeVersionInfo`](#exeVersionInfo)
 - [`iExpressConfig`](#iExpressConfig)
 - [`opyConfig`](#opyConfig)
 - [`pyInstallerConfig`](#pyInstallerConfig)
 - [`qtIfwConfig`](#qtIfwConfig)
 - [`qtIfwConfigXml`](#qtIfwConfigXml)
 - [`qtIfwControlScript`](#qtIfwControlScript)
 - [`qtIfwExeWrapper`](#qtIfwExeWrapper)
 - [`qtIfwPackage`](#qtIfwPackage)
 - [`qtIfwPackageScript`](#qtIfwPackageScript)
 - [`qtIfwPackageXml`](#qtIfwPackageXml)

**Instance Attributes:** 

 - [`cfgId`](#cfgId)
 - [`productName`](#productName)
 - [`description`](#description)
 - [`companyTradeName`](#companyTradeName)
 - [`companyLegalName`](#companyLegalName)
 - [`version`](#version)
 - [`isGui`](#isGui)
 - [`binaryName`](#binaryName)
 - [`sourceDir`](#sourceDir)
 - [`iconFilePath`](#iconFilePath)
 - [`entryPointPy`](#entryPointPy)
 - [`specFilePath`](#specFilePath)
 - [`isOneFile`](#isOneFile)
 - [`entryPointScript`](#entryPointScript)
 - [`distResources`](#distResources)
 - [`isObfuscating`](#isObfuscating)
 - [`opyBundleLibs`](#opyBundleLibs)
 - [`opyPatches`](#opyPatches)
 - [`isSilentSetup`](#isSilentSetup)
 - [`setupName`](#setupName)
 - [`ifwDefDirPath`](#ifwDefDirPath)
 - [`ifwPackages`](#ifwPackages)
 - [`isLimitedMaintenance`](#isLimitedMaintenance)
 - [`replaceTarget`](#replaceTarget)
 - [`ifwWizardStyle`](#ifwWizardStyle)
 - [`ifwLogoFilePath`](#ifwLogoFilePath)
 - [`ifwBannerFilePath`](#ifwBannerFilePath)
 - [`licensePath`](#licensePath)
 - [`ifwUiPages`](#ifwUiPages)
 - [`ifwWidgets`](#ifwWidgets)
 - [`ifwCntrlScript`](#ifwCntrlScript)
 - [`ifwCntrlScriptText`](#ifwCntrlScriptText)
 - [`ifwCntrlScriptPath`](#ifwCntrlScriptPath)
 - [`ifwCntrlScriptName`](#ifwCntrlScriptName)
 - [`ifwPkgId`](#ifwPkgId)
 - [`ifwPkgName`](#ifwPkgName)
 - [`ifwPkgNamePrefix`](#ifwPkgNamePrefix)
 - [`ifwPkgIsDefault`](#ifwPkgIsDefault)
 - [`ifwPkgIsRequired`](#ifwPkgIsRequired)
 - [`ifwPkgIsHidden`](#ifwPkgIsHidden)
 - [`ifwPkgScript`](#ifwPkgScript)
 - [`ifwPkgScriptText`](#ifwPkgScriptText)
 - [`ifwPkgScriptPath`](#ifwPkgScriptPath)
 - [`ifwPkgScriptName`](#ifwPkgScriptName)
 - [`pkgType`](#pkgType)
 - [`pkgSubDirName`](#pkgSubDirName)
 - [`pkgSrcDirPath`](#pkgSrcDirPath)
 - [`pkgSrcExePath`](#pkgSrcExePath)
 - [`pkgCodeSignTargets`](#pkgCodeSignTargets)
 - [`pkgExeWrapper`](#pkgExeWrapper)
 - [`pkgExternalDependencies`](#pkgExternalDependencies)
 - [`pkgConfigs`](#pkgConfigs)
 - [`startOnBoot`](#startOnBoot)
 - [`codeSignConfig`](#codeSignConfig)
 - [`qtCppConfig`](#qtCppConfig)

**Class/Static Methods:** 

 - [`copy`](#copy)

### **ConfigFactory**`#!py3 (cfgId=None)` { #ConfigFactory-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**exeVersionInfo**`#!py3 (self, ifwConfig=None)` { #exeVersionInfo data-toc-label=exeVersionInfo }


### *obj*.**iExpressConfig**`#!py3 (self)` { #iExpressConfig data-toc-label=iExpressConfig }


### *obj*.**opyConfig**`#!py3 (self)` { #opyConfig data-toc-label=opyConfig }


### *obj*.**pyInstallerConfig**`#!py3 (self)` { #pyInstallerConfig data-toc-label=pyInstallerConfig }


### *obj*.**qtIfwConfig**`#!py3 (self, packages=None)` { #qtIfwConfig data-toc-label=qtIfwConfig }


### *obj*.**qtIfwConfigXml**`#!py3 (self)` { #qtIfwConfigXml data-toc-label=qtIfwConfigXml }


### *obj*.**qtIfwControlScript**`#!py3 (self, configXml)` { #qtIfwControlScript data-toc-label=qtIfwControlScript }


### *obj*.**qtIfwExeWrapper**`#!py3 (self, wrapperScript=None, workingDir=None, isElevated=False, envVars=None, args=None, isExe=False)` { #qtIfwExeWrapper data-toc-label=qtIfwExeWrapper }


### *obj*.**qtIfwPackage**`#!py3 (self, pyInstConfig=None, iExpressConfig=None, isTempSrc=False)` { #qtIfwPackage data-toc-label=qtIfwPackage }


### *obj*.**qtIfwPackageScript**`#!py3 (self, pyInstConfig=None)` { #qtIfwPackageScript data-toc-label=qtIfwPackageScript }


### *obj*.**qtIfwPackageXml**`#!py3 (self)` { #qtIfwPackageXml data-toc-label=qtIfwPackageXml }


### *obj*.**cfgId** *class 'NoneType'* default: *None* { #cfgId data-toc-label=cfgId }


### *obj*.**productName** *class 'NoneType'* default: *None* { #productName data-toc-label=productName }


### *obj*.**description** *class 'NoneType'* default: *None* { #description data-toc-label=description }


### *obj*.**companyTradeName** *class 'NoneType'* default: *None* { #companyTradeName data-toc-label=companyTradeName }


### *obj*.**companyLegalName** *class 'NoneType'* default: *None* { #companyLegalName data-toc-label=companyLegalName }


### *obj*.**version** *class 'tuple'* default: *(0, 0, 0, 0)* { #version data-toc-label=version }


### *obj*.**isGui** *class 'bool'* default: *False* { #isGui data-toc-label=isGui }


### *obj*.**binaryName** *class 'NoneType'* default: *None* { #binaryName data-toc-label=binaryName }


### *obj*.**sourceDir** *class 'NoneType'* default: *None* { #sourceDir data-toc-label=sourceDir }


### *obj*.**iconFilePath** *class 'NoneType'* default: *None* { #iconFilePath data-toc-label=iconFilePath }


### *obj*.**entryPointPy** *class 'NoneType'* default: *None* { #entryPointPy data-toc-label=entryPointPy }


### *obj*.**specFilePath** *class 'NoneType'* default: *None* { #specFilePath data-toc-label=specFilePath }


### *obj*.**isOneFile** *class 'bool'* default: *True* { #isOneFile data-toc-label=isOneFile }


### *obj*.**entryPointScript** *class 'NoneType'* default: *None* { #entryPointScript data-toc-label=entryPointScript }


### *obj*.**distResources** *class 'list'* default: *[]* { #distResources data-toc-label=distResources }


### *obj*.**isObfuscating** *class 'bool'* default: *False* { #isObfuscating data-toc-label=isObfuscating }


### *obj*.**opyBundleLibs** *class 'NoneType'* default: *None* { #opyBundleLibs data-toc-label=opyBundleLibs }


### *obj*.**opyPatches** *class 'NoneType'* default: *None* { #opyPatches data-toc-label=opyPatches }


### *obj*.**isSilentSetup** *class 'bool'* default: *False* { #isSilentSetup data-toc-label=isSilentSetup }


### *obj*.**setupName** *class 'str'* default: *"setup.exe"* { #setupName data-toc-label=setupName }


### *obj*.**ifwDefDirPath** *class 'NoneType'* default: *None* { #ifwDefDirPath data-toc-label=ifwDefDirPath }


### *obj*.**ifwPackages** *class 'NoneType'* default: *None* { #ifwPackages data-toc-label=ifwPackages }


### *obj*.**isLimitedMaintenance** *class 'bool'* default: *True* { #isLimitedMaintenance data-toc-label=isLimitedMaintenance }


### *obj*.**replaceTarget** *class 'bool'* default: *False* { #replaceTarget data-toc-label=replaceTarget }


### *obj*.**ifwWizardStyle** *class 'NoneType'* default: *None* { #ifwWizardStyle data-toc-label=ifwWizardStyle }


### *obj*.**ifwLogoFilePath** *class 'NoneType'* default: *None* { #ifwLogoFilePath data-toc-label=ifwLogoFilePath }


### *obj*.**ifwBannerFilePath** *class 'NoneType'* default: *None* { #ifwBannerFilePath data-toc-label=ifwBannerFilePath }


### *obj*.**licensePath** *class 'NoneType'* default: *None* { #licensePath data-toc-label=licensePath }


### *obj*.**ifwUiPages** *class 'NoneType'* default: *None* { #ifwUiPages data-toc-label=ifwUiPages }


### *obj*.**ifwWidgets** *class 'NoneType'* default: *None* { #ifwWidgets data-toc-label=ifwWidgets }


### *obj*.**ifwCntrlScript** *class 'NoneType'* default: *None* { #ifwCntrlScript data-toc-label=ifwCntrlScript }


### *obj*.**ifwCntrlScriptText** *class 'NoneType'* default: *None* { #ifwCntrlScriptText data-toc-label=ifwCntrlScriptText }


### *obj*.**ifwCntrlScriptPath** *class 'NoneType'* default: *None* { #ifwCntrlScriptPath data-toc-label=ifwCntrlScriptPath }


### *obj*.**ifwCntrlScriptName** *class 'str'* default: *"installscript.qs"* { #ifwCntrlScriptName data-toc-label=ifwCntrlScriptName }


### *obj*.**ifwPkgId** *class 'NoneType'* default: *None* { #ifwPkgId data-toc-label=ifwPkgId }


### *obj*.**ifwPkgName** *class 'NoneType'* default: *None* { #ifwPkgName data-toc-label=ifwPkgName }


### *obj*.**ifwPkgNamePrefix** *class 'str'* default: *"com"* { #ifwPkgNamePrefix data-toc-label=ifwPkgNamePrefix }


### *obj*.**ifwPkgIsDefault** *class 'bool'* default: *True* { #ifwPkgIsDefault data-toc-label=ifwPkgIsDefault }


### *obj*.**ifwPkgIsRequired** *class 'bool'* default: *False* { #ifwPkgIsRequired data-toc-label=ifwPkgIsRequired }


### *obj*.**ifwPkgIsHidden** *class 'bool'* default: *False* { #ifwPkgIsHidden data-toc-label=ifwPkgIsHidden }


### *obj*.**ifwPkgScript** *class 'NoneType'* default: *None* { #ifwPkgScript data-toc-label=ifwPkgScript }


### *obj*.**ifwPkgScriptText** *class 'NoneType'* default: *None* { #ifwPkgScriptText data-toc-label=ifwPkgScriptText }


### *obj*.**ifwPkgScriptPath** *class 'NoneType'* default: *None* { #ifwPkgScriptPath data-toc-label=ifwPkgScriptPath }


### *obj*.**ifwPkgScriptName** *class 'str'* default: *"installscript.qs"* { #ifwPkgScriptName data-toc-label=ifwPkgScriptName }


### *obj*.**pkgType** *class 'NoneType'* default: *None* { #pkgType data-toc-label=pkgType }


### *obj*.**pkgSubDirName** *class 'NoneType'* default: *None* { #pkgSubDirName data-toc-label=pkgSubDirName }


### *obj*.**pkgSrcDirPath** *class 'NoneType'* default: *None* { #pkgSrcDirPath data-toc-label=pkgSrcDirPath }


### *obj*.**pkgSrcExePath** *class 'NoneType'* default: *None* { #pkgSrcExePath data-toc-label=pkgSrcExePath }


### *obj*.**pkgCodeSignTargets** *class 'NoneType'* default: *None* { #pkgCodeSignTargets data-toc-label=pkgCodeSignTargets }


### *obj*.**pkgExeWrapper** *class 'NoneType'* default: *None* { #pkgExeWrapper data-toc-label=pkgExeWrapper }


### *obj*.**pkgExternalDependencies** *class 'NoneType'* default: *None* { #pkgExternalDependencies data-toc-label=pkgExternalDependencies }


### *obj*.**pkgConfigs** *class 'NoneType'* default: *None* { #pkgConfigs data-toc-label=pkgConfigs }


### *obj*.**startOnBoot** *class 'bool'* default: *False* { #startOnBoot data-toc-label=startOnBoot }


### *obj*.**codeSignConfig** *class 'NoneType'* default: *None* { #codeSignConfig data-toc-label=codeSignConfig }


### *obj*.**qtCppConfig** *class 'NoneType'* default: *None* { #qtCppConfig data-toc-label=qtCppConfig }


### *ConfigFactory*.**copy**`#!py3 (instance)` { #copy data-toc-label=copy }



______

