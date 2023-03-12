## **QtIfwConfig**`#!py3 class` { #QtIfwConfig data-toc-label=QtIfwConfig }



**Magic Methods:**

 - [`__init__`](#QtIfwConfig-init)

**Instance Methods:** 

 - [`addLicense`](#addLicense)
 - [`addUiElements`](#addUiElements)

**Instance Attributes:** 

 - [`installerDefDirPath`](#installerDefDirPath)
 - [`packages`](#packages)
 - [`configXml`](#configXml)
 - [`controlScript`](#controlScript)
 - [`setupExeName`](#setupExeName)
 - [`qtIfwDirPath`](#qtIfwDirPath)
 - [`isDebugMode`](#isDebugMode)
 - [`otherQtIfwArgs`](#otherQtIfwArgs)

### **QtIfwConfig**`#!py3 (installerDefDirPath=None, packages=None, configXml=None, controlScript=None, setupExeName='setup.exe')` { #QtIfwConfig-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**addLicense**`#!py3 (self, licensePath, name='End User License Agreement')` { #addLicense data-toc-label=addLicense }


### *obj*.**addUiElements**`#!py3 (self, uiElements, isOverWrite=True)` { #addUiElements data-toc-label=addUiElements }


### *obj*.**installerDefDirPath** *class 'NoneType'* default: *None* { #installerDefDirPath data-toc-label=installerDefDirPath }


### *obj*.**packages** *class 'NoneType'* default: *None* { #packages data-toc-label=packages }


### *obj*.**configXml** *class 'NoneType'* default: *None* { #configXml data-toc-label=configXml }


### *obj*.**controlScript** *class 'NoneType'* default: *None* { #controlScript data-toc-label=controlScript }


### *obj*.**setupExeName** *class 'NoneType'* default: *None* { #setupExeName data-toc-label=setupExeName }


### *obj*.**qtIfwDirPath** *class 'NoneType'* default: *None* { #qtIfwDirPath data-toc-label=qtIfwDirPath }


### *obj*.**isDebugMode** *class 'bool'* default: *True* { #isDebugMode data-toc-label=isDebugMode }


### *obj*.**otherQtIfwArgs** *class 'str'* default: *"&lt;empty string&gt;"* { #otherQtIfwArgs data-toc-label=otherQtIfwArgs }



______

## **QtIfwConfigXml**`#!py3 class` { #QtIfwConfigXml data-toc-label=QtIfwConfigXml }



**Base Classes:**

_QtIfwXml


**Magic Methods:**

 - [`__init__`](#QtIfwConfigXml-init)

**Instance Methods:** 

 - [`addCustomTags`](#addCustomTags)
 - [`debug`](#debug)
 - [`dirPath`](#dirPath)
 - [`exists`](#exists)
 - [`path`](#path)
 - [`setDefaultPaths`](#setDefaultPaths)
 - [`setDefaultTitle`](#setDefaultTitle)
 - [`setDefaultVersion`](#setDefaultVersion)
 - [`setPrimaryContentExe`](#setPrimaryContentExe)
 - [`toPrettyXml`](#toPrettyXml)
 - [`write`](#write)

**Instance Attributes:** 

 - [`primaryContentExe`](#primaryContentExe)
 - [`primaryExeWrapper`](#primaryExeWrapper)
 - [`runProgramArgList`](#runProgramArgList)
 - [`companyTradeName`](#companyTradeName)
 - [`iconFilePath`](#iconFilePath)
 - [`logoFilePath`](#logoFilePath)
 - [`bannerFilePath`](#bannerFilePath)
 - [`Name`](#Name)
 - [`Version`](#Version)
 - [`Publisher`](#Publisher)
 - [`Title`](#Title)
 - [`TitleColor`](#TitleColor)
 - [`ControlScript`](#ControlScript)
 - [`TargetDir`](#TargetDir)
 - [`StartMenuDir`](#StartMenuDir)
 - [`RunProgram`](#RunProgram)
 - [`RunProgramDescription`](#RunProgramDescription)
 - [`WizardStyle`](#WizardStyle)
 - [`WizardDefaultWidth`](#WizardDefaultWidth)
 - [`WizardDefaultHeight`](#WizardDefaultHeight)
 - [`Logo`](#Logo)
 - [`Banner`](#Banner)
 - [`ProductUrl`](#ProductUrl)

**Class/Static Attributes:** 

 - [`DEFAULT_WIZARD_STYLE`](#DEFAULT_WIZARD_STYLE)
 - [`WizardStyle`](#WizardStyle)

### **QtIfwConfigXml**`#!py3 (name, version, publisher, iconFilePath=None, controlScriptName=None, primaryContentExe=None, isPrimaryExeGui=True, primaryExeWrapper=None, companyTradeName=None, wizardStyle=None, logoFilePath=None, bannerFilePath=None)` { #QtIfwConfigXml-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**addCustomTags**`#!py3 (self, root)` { #addCustomTags data-toc-label=addCustomTags }

VIRTUAL
### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**dirPath**`#!py3 (self)` { #dirPath data-toc-label=dirPath }

PURE VIRTUAL
### *obj*.**exists**`#!py3 (self)` { #exists data-toc-label=exists }


### *obj*.**path**`#!py3 (self)` { #path data-toc-label=path }

PURE VIRTUAL
### *obj*.**setDefaultPaths**`#!py3 (self)` { #setDefaultPaths data-toc-label=setDefaultPaths }


### *obj*.**setDefaultTitle**`#!py3 (self)` { #setDefaultTitle data-toc-label=setDefaultTitle }


### *obj*.**setDefaultVersion**`#!py3 (self)` { #setDefaultVersion data-toc-label=setDefaultVersion }


### *obj*.**setPrimaryContentExe**`#!py3 (self, ifwPackage)` { #setPrimaryContentExe data-toc-label=setPrimaryContentExe }


### *obj*.**toPrettyXml**`#!py3 (self)` { #toPrettyXml data-toc-label=toPrettyXml }


### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**primaryContentExe** *class 'NoneType'* default: *None* { #primaryContentExe data-toc-label=primaryContentExe }


### *obj*.**primaryExeWrapper** *class 'NoneType'* default: *None* { #primaryExeWrapper data-toc-label=primaryExeWrapper }


### *obj*.**runProgramArgList** *class 'NoneType'* default: *None* { #runProgramArgList data-toc-label=runProgramArgList }


### *obj*.**companyTradeName** *class 'NoneType'* default: *None* { #companyTradeName data-toc-label=companyTradeName }


### *obj*.**iconFilePath** *class 'NoneType'* default: *None* { #iconFilePath data-toc-label=iconFilePath }


### *obj*.**logoFilePath** *class 'NoneType'* default: *None* { #logoFilePath data-toc-label=logoFilePath }


### *obj*.**bannerFilePath** *class 'NoneType'* default: *None* { #bannerFilePath data-toc-label=bannerFilePath }


### *obj*.**Name** *class 'NoneType'* default: *None* { #Name data-toc-label=Name }


### *obj*.**Version** *class 'NoneType'* default: *None* { #Version data-toc-label=Version }


### *obj*.**Publisher** *class 'NoneType'* default: *None* { #Publisher data-toc-label=Publisher }


### *obj*.**Title** *class 'NoneType'* default: *None* { #Title data-toc-label=Title }


### *obj*.**TitleColor** *class 'NoneType'* default: *None* { #TitleColor data-toc-label=TitleColor }


### *obj*.**ControlScript** *class 'NoneType'* default: *None* { #ControlScript data-toc-label=ControlScript }


### *obj*.**TargetDir** *class 'NoneType'* default: *None* { #TargetDir data-toc-label=TargetDir }


### *obj*.**StartMenuDir** *class 'NoneType'* default: *None* { #StartMenuDir data-toc-label=StartMenuDir }


### *obj*.**RunProgram** *class 'NoneType'* default: *None* { #RunProgram data-toc-label=RunProgram }


### *obj*.**RunProgramDescription** *class 'NoneType'* default: *None* { #RunProgramDescription data-toc-label=RunProgramDescription }


### *obj*.**WizardStyle** *class 'NoneType'* default: *None* { #WizardStyle data-toc-label=WizardStyle }


### *obj*.**WizardDefaultWidth** *class 'NoneType'* default: *None* { #WizardDefaultWidth data-toc-label=WizardDefaultWidth }


### *obj*.**WizardDefaultHeight** *class 'NoneType'* default: *None* { #WizardDefaultHeight data-toc-label=WizardDefaultHeight }


### *obj*.**Logo** *class 'NoneType'* default: *None* { #Logo data-toc-label=Logo }


### *obj*.**Banner** *class 'NoneType'* default: *None* { #Banner data-toc-label=Banner }


### *obj*.**ProductUrl** *class 'NoneType'* default: *None* { #ProductUrl data-toc-label=ProductUrl }


### *QtIfwConfigXml*.**DEFAULT_WIZARD_STYLE** *class 'int'* default: *None* { #DEFAULT_WIZARD_STYLE data-toc-label=DEFAULT_WIZARD_STYLE }


### *QtIfwConfigXml*.**WizardStyle** *class 'type'* default: *None* { #WizardStyle data-toc-label=WizardStyle }


## **QtIfwConfigXml.WizardStyle**`#!py3 class` { #QtIfwConfigXml.WizardStyle data-toc-label=QtIfwConfigXml.WizardStyle }



**Class/Static Attributes:** 

 - [`AERO`](#AERO)
 - [`CLASSIC`](#CLASSIC)
 - [`MAC`](#MAC)
 - [`MODERN`](#MODERN)

### *QtIfwConfigXml.WizardStyle*.**AERO** *class 'int'* default: *0* { #AERO data-toc-label=AERO }


### *QtIfwConfigXml.WizardStyle*.**CLASSIC** *class 'int'* default: *3* { #CLASSIC data-toc-label=CLASSIC }


### *QtIfwConfigXml.WizardStyle*.**MAC** *class 'int'* default: *2* { #MAC data-toc-label=MAC }


### *QtIfwConfigXml.WizardStyle*.**MODERN** *class 'int'* default: *1* { #MODERN data-toc-label=MODERN }



______

## **QtIfwControlScript**`#!py3 class` { #QtIfwControlScript data-toc-label=QtIfwControlScript }



**Base Classes:**

_QtIfwScript


**Magic Methods:**

 - [`__init__`](#QtIfwControlScript-init)

**Instance Methods:** 

 - [`debug`](#debug)
 - [`dirPath`](#dirPath)
 - [`exists`](#exists)
 - [`path`](#path)
 - [`registerAutoPilotEventHandler`](#registerAutoPilotEventHandler)
 - [`registerGuiEventHandler`](#registerGuiEventHandler)
 - [`registerStandardEventHandler`](#registerStandardEventHandler)
 - [`registerWidgetEventHandler`](#registerWidgetEventHandler)
 - [`write`](#write)

**Instance Attributes:** 

 - [`isLimitedMaintenance`](#isLimitedMaintenance)
 - [`virtualArgs`](#virtualArgs)
 - [`uiPages`](#uiPages)
 - [`widgets`](#widgets)
 - [`controllerGlobals`](#controllerGlobals)
 - [`isAutoGlobals`](#isAutoGlobals)
 - [`controllerConstructorBody`](#controllerConstructorBody)
 - [`controllerConstructorInjection`](#controllerConstructorInjection)
 - [`isAutoControllerConstructor`](#isAutoControllerConstructor)
 - [`onValueChangeCallbackBody`](#onValueChangeCallbackBody)
 - [`onValueChangeCallbackInjection`](#onValueChangeCallbackInjection)
 - [`isAutoValueChangeCallBack`](#isAutoValueChangeCallBack)
 - [`onPageChangeCallbackBody`](#onPageChangeCallbackBody)
 - [`onPageChangeCallbackInjection`](#onPageChangeCallbackInjection)
 - [`isAutoPageChangeCallBack`](#isAutoPageChangeCallBack)
 - [`onPageInsertRequestCallbackBody`](#onPageInsertRequestCallbackBody)
 - [`isAutoPageInsertRequestCallBack`](#isAutoPageInsertRequestCallBack)
 - [`onPageRemoveRequestCallbackBody`](#onPageRemoveRequestCallbackBody)
 - [`isAutoPageRemoveRequestCallBack`](#isAutoPageRemoveRequestCallBack)
 - [`onPageVisibilityRequestCallbackBody`](#onPageVisibilityRequestCallbackBody)
 - [`isAutoPageVisibilityRequestCallBack`](#isAutoPageVisibilityRequestCallBack)
 - [`onFinishedClickedCallbackBody`](#onFinishedClickedCallbackBody)
 - [`onFinishedClickedCallbackInjection`](#onFinishedClickedCallbackInjection)
 - [`onFinishedDetachedExecutions`](#onFinishedDetachedExecutions)
 - [`isAutoFinishedClickedCallbackBody`](#isAutoFinishedClickedCallbackBody)
 - [`isIntroductionPageVisible`](#isIntroductionPageVisible)
 - [`introductionPageCallbackBody`](#introductionPageCallbackBody)
 - [`introductionPageOnInstall`](#introductionPageOnInstall)
 - [`introductionPageOnMaintain`](#introductionPageOnMaintain)
 - [`isAutoIntroductionPageCallback`](#isAutoIntroductionPageCallback)
 - [`isTargetDirectoryPageVisible`](#isTargetDirectoryPageVisible)
 - [`targetDirectoryPageCallbackBody`](#targetDirectoryPageCallbackBody)
 - [`isAutoTargetDirectoryPageCallback`](#isAutoTargetDirectoryPageCallback)
 - [`isComponentSelectionPageVisible`](#isComponentSelectionPageVisible)
 - [`componentSelectionPageCallbackBody`](#componentSelectionPageCallbackBody)
 - [`componentSelectionPageInjection`](#componentSelectionPageInjection)
 - [`isAutoComponentSelectionPageCallback`](#isAutoComponentSelectionPageCallback)
 - [`isLicenseAgreementPageVisible`](#isLicenseAgreementPageVisible)
 - [`licenseAgreementPageCallbackBody`](#licenseAgreementPageCallbackBody)
 - [`isAutoLicenseAgreementPageCallback`](#isAutoLicenseAgreementPageCallback)
 - [`isStartMenuDirectoryPageVisible`](#isStartMenuDirectoryPageVisible)
 - [`startMenuDirectoryPageCallbackBody`](#startMenuDirectoryPageCallbackBody)
 - [`isAutoStartMenuDirectoryPageCallback`](#isAutoStartMenuDirectoryPageCallback)
 - [`isReadyForInstallationPageVisible`](#isReadyForInstallationPageVisible)
 - [`readyForInstallationPageCallbackBody`](#readyForInstallationPageCallbackBody)
 - [`readyForInstallationPageOnInstall`](#readyForInstallationPageOnInstall)
 - [`readyForInstallationPageOnMaintain`](#readyForInstallationPageOnMaintain)
 - [`isAutoReadyForInstallationPageCallback`](#isAutoReadyForInstallationPageCallback)
 - [`isPerformInstallationPageVisible`](#isPerformInstallationPageVisible)
 - [`performInstallationPageCallbackBody`](#performInstallationPageCallbackBody)
 - [`isAutoPerformInstallationPageCallback`](#isAutoPerformInstallationPageCallback)
 - [`isFinishedPageVisible`](#isFinishedPageVisible)
 - [`finishedPageCallbackBody`](#finishedPageCallbackBody)
 - [`finishedPageOnInstall`](#finishedPageOnInstall)
 - [`finishedPageOnMaintain`](#finishedPageOnMaintain)
 - [`isAutoFinishedPageCallback`](#isAutoFinishedPageCallback)
 - [`isRunProgVisible`](#isRunProgVisible)
 - [`isRunProgEnabled`](#isRunProgEnabled)
 - [`isRunProgChecked`](#isRunProgChecked)

**Class/Static Methods:** 

 - [`andList`](#andList)
 - [`assertInternetConnected`](#assertInternetConnected)
 - [`assignCurrentPageWidgetVar`](#assignCurrentPageWidgetVar)
 - [`assignCustomPageWidgetVar`](#assignCustomPageWidgetVar)
 - [`assignPageWidgetVar`](#assignPageWidgetVar)
 - [`assignRegistryEntryVar`](#assignRegistryEntryVar)
 - [`boolToString`](#boolToString)
 - [`clickButton`](#clickButton)
 - [`cmdLineArg`](#cmdLineArg)
 - [`cmdLineListArg`](#cmdLineListArg)
 - [`cmdLineSwitchArg`](#cmdLineSwitchArg)
 - [`connectButtonClickHandler`](#connectButtonClickHandler)
 - [`connectWidgetEventHandler`](#connectWidgetEventHandler)
 - [`currentPageWidget`](#currentPageWidget)
 - [`customPageWidget`](#customPageWidget)
 - [`debugPopup`](#debugPopup)
 - [`deleteDetachedOpDataFile`](#deleteDetachedOpDataFile)
 - [`deleteFile`](#deleteFile)
 - [`deleteOpDataFile`](#deleteOpDataFile)
 - [`disableQuit`](#disableQuit)
 - [`disableQuitPrompt`](#disableQuitPrompt)
 - [`dropElevation`](#dropElevation)
 - [`elevate`](#elevate)
 - [`embedResources`](#embedResources)
 - [`enable`](#enable)
 - [`enableComponent`](#enableComponent)
 - [`enableCustom`](#enableCustom)
 - [`enableNextButton`](#enableNextButton)
 - [`errorPopup`](#errorPopup)
 - [`genResources`](#genResources)
 - [`getComponent`](#getComponent)
 - [`getCustomText`](#getCustomText)
 - [`getEnv`](#getEnv)
 - [`getPageOwner`](#getPageOwner)
 - [`getText`](#getText)
 - [`hideDefaultPage`](#hideDefaultPage)
 - [`ifAutoPilot`](#ifAutoPilot)
 - [`ifBoolValue`](#ifBoolValue)
 - [`ifChecked`](#ifChecked)
 - [`ifCmdLineArg`](#ifCmdLineArg)
 - [`ifCmdLineSwitch`](#ifCmdLineSwitch)
 - [`ifComponentEnabled`](#ifComponentEnabled)
 - [`ifComponentInstalled`](#ifComponentInstalled)
 - [`ifComponentSelected`](#ifComponentSelected)
 - [`ifCondition`](#ifCondition)
 - [`ifCustomChecked`](#ifCustomChecked)
 - [`ifCustomEnabled`](#ifCustomEnabled)
 - [`ifCustomVisible`](#ifCustomVisible)
 - [`ifDryRun`](#ifDryRun)
 - [`ifElevated`](#ifElevated)
 - [`ifEnabled`](#ifEnabled)
 - [`ifInstalling`](#ifInstalling)
 - [`ifInternetConnected`](#ifInternetConnected)
 - [`ifMaintenanceTool`](#ifMaintenanceTool)
 - [`ifPathExists`](#ifPathExists)
 - [`ifPingable`](#ifPingable)
 - [`ifRegistryEntryExists`](#ifRegistryEntryExists)
 - [`ifRegistryEntryExistsLike`](#ifRegistryEntryExistsLike)
 - [`ifRegistryKeyExists`](#ifRegistryKeyExists)
 - [`ifRegistryKeyExistsLike`](#ifRegistryKeyExistsLike)
 - [`ifValueDefined`](#ifValueDefined)
 - [`ifVisible`](#ifVisible)
 - [`ifYesNoPopup`](#ifYesNoPopup)
 - [`insertCustomPage`](#insertCustomPage)
 - [`insertCustomWidget`](#insertCustomWidget)
 - [`isAutoPilot`](#isAutoPilot)
 - [`isChecked`](#isChecked)
 - [`isComponentEnabled`](#isComponentEnabled)
 - [`isComponentInstalled`](#isComponentInstalled)
 - [`isComponentSelected`](#isComponentSelected)
 - [`isCustomChecked`](#isCustomChecked)
 - [`isCustomEnabled`](#isCustomEnabled)
 - [`isCustomVisible`](#isCustomVisible)
 - [`isDryRun`](#isDryRun)
 - [`isElevated`](#isElevated)
 - [`isEnabled`](#isEnabled)
 - [`isInstalling`](#isInstalling)
 - [`isInternetConnected`](#isInternetConnected)
 - [`isMaintenanceTool`](#isMaintenanceTool)
 - [`isPingable`](#isPingable)
 - [`isVisible`](#isVisible)
 - [`killAll`](#killAll)
 - [`log`](#log)
 - [`logSwitch`](#logSwitch)
 - [`logValue`](#logValue)
 - [`lookupBoolValue`](#lookupBoolValue)
 - [`lookupValue`](#lookupValue)
 - [`lookupValueList`](#lookupValueList)
 - [`makeDir`](#makeDir)
 - [`openViaOs`](#openViaOs)
 - [`orList`](#orList)
 - [`pageWidget`](#pageWidget)
 - [`pathExists`](#pathExists)
 - [`productName`](#productName)
 - [`quit`](#quit)
 - [`quote`](#quote)
 - [`registryEntryExists`](#registryEntryExists)
 - [`registryEntryExistsLike`](#registryEntryExistsLike)
 - [`registryEntryValue`](#registryEntryValue)
 - [`registryKeyExists`](#registryKeyExists)
 - [`registryKeyExistsLike`](#registryKeyExistsLike)
 - [`removeCustomPage`](#removeCustomPage)
 - [`removeCustomWidget`](#removeCustomWidget)
 - [`removeDir`](#removeDir)
 - [`resolveDynamTxtVarsOperations`](#resolveDynamTxtVarsOperations)
 - [`resolveDynamicVars`](#resolveDynamicVars)
 - [`resolveScriptVars`](#resolveScriptVars)
 - [`resolveScriptVarsOperations`](#resolveScriptVarsOperations)
 - [`selectAllComponents`](#selectAllComponents)
 - [`selectComponent`](#selectComponent)
 - [`selectDefaultComponents`](#selectDefaultComponents)
 - [`setBoolValue`](#setBoolValue)
 - [`setChecked`](#setChecked)
 - [`setCustomCheckBox`](#setCustomCheckBox)
 - [`setCustomPageText`](#setCustomPageText)
 - [`setCustomPageTitle`](#setCustomPageTitle)
 - [`setCustomText`](#setCustomText)
 - [`setCustomVisible`](#setCustomVisible)
 - [`setText`](#setText)
 - [`setValue`](#setValue)
 - [`setValueFromRegistryEntry`](#setValueFromRegistryEntry)
 - [`setVisible`](#setVisible)
 - [`startMenuDir`](#startMenuDir)
 - [`stringToBool`](#stringToBool)
 - [`switchYesNoCancelPopup`](#switchYesNoCancelPopup)
 - [`targetDir`](#targetDir)
 - [`toBool`](#toBool)
 - [`toDefaultPageId`](#toDefaultPageId)
 - [`toNull`](#toNull)
 - [`warningPopup`](#warningPopup)
 - [`writeDetachedOpDataFile`](#writeDetachedOpDataFile)
 - [`writeFile`](#writeFile)
 - [`writeOpDataFile`](#writeOpDataFile)
 - [`yesNoCancelPopup`](#yesNoCancelPopup)
 - [`yesNoPopup`](#yesNoPopup)

**Class/Static Attributes:** 

 - [`ABORT`](#ABORT)
 - [`ACCEPT_EULA_CMD_ARG`](#ACCEPT_EULA_CMD_ARG)
 - [`ACCEPT_EULA_RADIO_BUTTON`](#ACCEPT_EULA_RADIO_BUTTON)
 - [`AND`](#AND)
 - [`ASSIGN`](#ASSIGN)
 - [`AUTH_ERROR_MSGBOX_ID`](#AUTH_ERROR_MSGBOX_ID)
 - [`AUTO_PILOT_CMD_ARG`](#AUTO_PILOT_CMD_ARG)
 - [`BACK_BUTTON`](#BACK_BUTTON)
 - [`CANCEL`](#CANCEL)
 - [`CANCEL_BUTTON`](#CANCEL_BUTTON)
 - [`CATCH`](#CATCH)
 - [`COMMIT_BUTTON`](#COMMIT_BUTTON)
 - [`CONCAT`](#CONCAT)
 - [`CUSTOM_BUTTON_1`](#CUSTOM_BUTTON_1)
 - [`CUSTOM_BUTTON_2`](#CUSTOM_BUTTON_2)
 - [`CUSTOM_BUTTON_3`](#CUSTOM_BUTTON_3)
 - [`DEFAULT_FINISHED_MESSAGE`](#DEFAULT_FINISHED_MESSAGE)
 - [`DEFAULT_TARGET_DIR_KEY`](#DEFAULT_TARGET_DIR_KEY)
 - [`DRYRUN_CMD_ARG`](#DRYRUN_CMD_ARG)
 - [`ELSE`](#ELSE)
 - [`END_BLOCK`](#END_BLOCK)
 - [`END_LINE`](#END_LINE)
 - [`EQUAL_TO`](#EQUAL_TO)
 - [`ERR_LOG_DEFAULT_PATH`](#ERR_LOG_DEFAULT_PATH)
 - [`ERR_LOG_PATH_CMD_ARG`](#ERR_LOG_PATH_CMD_ARG)
 - [`EXCLUDE_LIST_CMD_ARG`](#EXCLUDE_LIST_CMD_ARG)
 - [`EXIT_FUNCTION`](#EXIT_FUNCTION)
 - [`FALSE`](#FALSE)
 - [`FINISHED_MESSAGE_LABEL`](#FINISHED_MESSAGE_LABEL)
 - [`FINISH_BUTTON`](#FINISH_BUTTON)
 - [`HELP_BUTTON`](#HELP_BUTTON)
 - [`IF`](#IF)
 - [`INCLUDE_LIST_CMD_ARG`](#INCLUDE_LIST_CMD_ARG)
 - [`INSTALL_LIST_CMD_ARG`](#INSTALL_LIST_CMD_ARG)
 - [`INTERUPTED_KEY`](#INTERUPTED_KEY)
 - [`IS_NET_CONNECTED_KEY`](#IS_NET_CONNECTED_KEY)
 - [`MAINTAIN_MODE_CMD_ARG`](#MAINTAIN_MODE_CMD_ARG)
 - [`MAINTAIN_MODE_OPT_ADD_REMOVE`](#MAINTAIN_MODE_OPT_ADD_REMOVE)
 - [`MAINTAIN_MODE_OPT_REMOVE_ALL`](#MAINTAIN_MODE_OPT_REMOVE_ALL)
 - [`MAINTAIN_MODE_OPT_UPDATE`](#MAINTAIN_MODE_OPT_UPDATE)
 - [`MAINTAIN_PASSTHRU_CMD_ARG`](#MAINTAIN_PASSTHRU_CMD_ARG)
 - [`MAINTENANCE_TOOL_NAME`](#MAINTENANCE_TOOL_NAME)
 - [`NEW_LINE`](#NEW_LINE)
 - [`NEXT_BUTTON`](#NEXT_BUTTON)
 - [`NO`](#NO)
 - [`NOT`](#NOT)
 - [`NOT_EQUAL_TO`](#NOT_EQUAL_TO)
 - [`NULL`](#NULL)
 - [`OK`](#OK)
 - [`OR`](#OR)
 - [`OUT_LOG_DEFAULT_PATH`](#OUT_LOG_DEFAULT_PATH)
 - [`OUT_LOG_PATH_CMD_ARG`](#OUT_LOG_PATH_CMD_ARG)
 - [`PATH_SEP`](#PATH_SEP)
 - [`PRODUCT_NAME_KEY`](#PRODUCT_NAME_KEY)
 - [`QUIT_MSGBOX_ID`](#QUIT_MSGBOX_ID)
 - [`REBOOT_CMD_ARG`](#REBOOT_CMD_ARG)
 - [`RESTORE_MSGBOX_DEFAULT`](#RESTORE_MSGBOX_DEFAULT)
 - [`RUN_PROGRAM_CHECKBOX`](#RUN_PROGRAM_CHECKBOX)
 - [`RUN_PROGRAM_CMD_ARG`](#RUN_PROGRAM_CMD_ARG)
 - [`STARTMENU_DIR_KEY`](#STARTMENU_DIR_KEY)
 - [`START_BLOCK`](#START_BLOCK)
 - [`START_MENU_DIR_CMD_ARG`](#START_MENU_DIR_CMD_ARG)
 - [`START_MENU_DIR_EDITBOX`](#START_MENU_DIR_EDITBOX)
 - [`TAB`](#TAB)
 - [`TARGET_DIR_CMD_ARG`](#TARGET_DIR_CMD_ARG)
 - [`TARGET_DIR_EDITBOX`](#TARGET_DIR_EDITBOX)
 - [`TARGET_DIR_KEY`](#TARGET_DIR_KEY)
 - [`TARGET_EXISTS_OPT_CMD_ARG`](#TARGET_EXISTS_OPT_CMD_ARG)
 - [`TARGET_EXISTS_OPT_FAIL`](#TARGET_EXISTS_OPT_FAIL)
 - [`TARGET_EXISTS_OPT_PROMPT`](#TARGET_EXISTS_OPT_PROMPT)
 - [`TARGET_EXISTS_OPT_REMOVE`](#TARGET_EXISTS_OPT_REMOVE)
 - [`TRUE`](#TRUE)
 - [`TRY`](#TRY)
 - [`USER_KEY`](#USER_KEY)
 - [`VERBOSE_CMD_SWITCH_ARG`](#VERBOSE_CMD_SWITCH_ARG)
 - [`YES`](#YES)

### **QtIfwControlScript**`#!py3 (fileName='installscript.qs', script=None, scriptPath=None)` { #QtIfwControlScript-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**dirPath**`#!py3 (self)` { #dirPath data-toc-label=dirPath }

PURE VIRTUAL
### *obj*.**exists**`#!py3 (self)` { #exists data-toc-label=exists }


### *obj*.**path**`#!py3 (self)` { #path data-toc-label=path }

PURE VIRTUAL
### *obj*.**registerAutoPilotEventHandler**`#!py3 (self, signalName, slotName, slotBody)` { #registerAutoPilotEventHandler data-toc-label=registerAutoPilotEventHandler }


### *obj*.**registerGuiEventHandler**`#!py3 (self, signalName, slotName, slotBody)` { #registerGuiEventHandler data-toc-label=registerGuiEventHandler }


### *obj*.**registerStandardEventHandler**`#!py3 (self, signalName, slotName, slotBody)` { #registerStandardEventHandler data-toc-label=registerStandardEventHandler }


### *obj*.**registerWidgetEventHandler**`#!py3 (self, pageId, controlName, signalName, slotName, slotBody)` { #registerWidgetEventHandler data-toc-label=registerWidgetEventHandler }


### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**isLimitedMaintenance** *class 'bool'* default: *True* { #isLimitedMaintenance data-toc-label=isLimitedMaintenance }


### *obj*.**virtualArgs** *class 'NoneType'* default: *None* { #virtualArgs data-toc-label=virtualArgs }


### *obj*.**uiPages** *class 'list'* default: *[]* { #uiPages data-toc-label=uiPages }


### *obj*.**widgets** *class 'list'* default: *[]* { #widgets data-toc-label=widgets }


### *obj*.**controllerGlobals** *class 'NoneType'* default: *None* { #controllerGlobals data-toc-label=controllerGlobals }


### *obj*.**isAutoGlobals** *class 'bool'* default: *True* { #isAutoGlobals data-toc-label=isAutoGlobals }


### *obj*.**controllerConstructorBody** *class 'NoneType'* default: *None* { #controllerConstructorBody data-toc-label=controllerConstructorBody }


### *obj*.**controllerConstructorInjection** *class 'NoneType'* default: *None* { #controllerConstructorInjection data-toc-label=controllerConstructorInjection }


### *obj*.**isAutoControllerConstructor** *class 'bool'* default: *True* { #isAutoControllerConstructor data-toc-label=isAutoControllerConstructor }


### *obj*.**onValueChangeCallbackBody** *class 'NoneType'* default: *None* { #onValueChangeCallbackBody data-toc-label=onValueChangeCallbackBody }


### *obj*.**onValueChangeCallbackInjection** *class 'NoneType'* default: *None* { #onValueChangeCallbackInjection data-toc-label=onValueChangeCallbackInjection }


### *obj*.**isAutoValueChangeCallBack** *class 'bool'* default: *True* { #isAutoValueChangeCallBack data-toc-label=isAutoValueChangeCallBack }


### *obj*.**onPageChangeCallbackBody** *class 'NoneType'* default: *None* { #onPageChangeCallbackBody data-toc-label=onPageChangeCallbackBody }


### *obj*.**onPageChangeCallbackInjection** *class 'NoneType'* default: *None* { #onPageChangeCallbackInjection data-toc-label=onPageChangeCallbackInjection }


### *obj*.**isAutoPageChangeCallBack** *class 'bool'* default: *True* { #isAutoPageChangeCallBack data-toc-label=isAutoPageChangeCallBack }


### *obj*.**onPageInsertRequestCallbackBody** *class 'NoneType'* default: *None* { #onPageInsertRequestCallbackBody data-toc-label=onPageInsertRequestCallbackBody }


### *obj*.**isAutoPageInsertRequestCallBack** *class 'bool'* default: *True* { #isAutoPageInsertRequestCallBack data-toc-label=isAutoPageInsertRequestCallBack }


### *obj*.**onPageRemoveRequestCallbackBody** *class 'NoneType'* default: *None* { #onPageRemoveRequestCallbackBody data-toc-label=onPageRemoveRequestCallbackBody }


### *obj*.**isAutoPageRemoveRequestCallBack** *class 'bool'* default: *True* { #isAutoPageRemoveRequestCallBack data-toc-label=isAutoPageRemoveRequestCallBack }


### *obj*.**onPageVisibilityRequestCallbackBody** *class 'NoneType'* default: *None* { #onPageVisibilityRequestCallbackBody data-toc-label=onPageVisibilityRequestCallbackBody }


### *obj*.**isAutoPageVisibilityRequestCallBack** *class 'bool'* default: *True* { #isAutoPageVisibilityRequestCallBack data-toc-label=isAutoPageVisibilityRequestCallBack }


### *obj*.**onFinishedClickedCallbackBody** *class 'NoneType'* default: *None* { #onFinishedClickedCallbackBody data-toc-label=onFinishedClickedCallbackBody }


### *obj*.**onFinishedClickedCallbackInjection** *class 'NoneType'* default: *None* { #onFinishedClickedCallbackInjection data-toc-label=onFinishedClickedCallbackInjection }


### *obj*.**onFinishedDetachedExecutions** *class 'list'* default: *[]* { #onFinishedDetachedExecutions data-toc-label=onFinishedDetachedExecutions }


### *obj*.**isAutoFinishedClickedCallbackBody** *class 'bool'* default: *True* { #isAutoFinishedClickedCallbackBody data-toc-label=isAutoFinishedClickedCallbackBody }


### *obj*.**isIntroductionPageVisible** *class 'bool'* default: *True* { #isIntroductionPageVisible data-toc-label=isIntroductionPageVisible }


### *obj*.**introductionPageCallbackBody** *class 'NoneType'* default: *None* { #introductionPageCallbackBody data-toc-label=introductionPageCallbackBody }


### *obj*.**introductionPageOnInstall** *class 'NoneType'* default: *None* { #introductionPageOnInstall data-toc-label=introductionPageOnInstall }


### *obj*.**introductionPageOnMaintain** *class 'NoneType'* default: *None* { #introductionPageOnMaintain data-toc-label=introductionPageOnMaintain }


### *obj*.**isAutoIntroductionPageCallback** *class 'bool'* default: *True* { #isAutoIntroductionPageCallback data-toc-label=isAutoIntroductionPageCallback }


### *obj*.**isTargetDirectoryPageVisible** *class 'bool'* default: *True* { #isTargetDirectoryPageVisible data-toc-label=isTargetDirectoryPageVisible }


### *obj*.**targetDirectoryPageCallbackBody** *class 'NoneType'* default: *None* { #targetDirectoryPageCallbackBody data-toc-label=targetDirectoryPageCallbackBody }


### *obj*.**isAutoTargetDirectoryPageCallback** *class 'bool'* default: *True* { #isAutoTargetDirectoryPageCallback data-toc-label=isAutoTargetDirectoryPageCallback }


### *obj*.**isComponentSelectionPageVisible** *class 'bool'* default: *True* { #isComponentSelectionPageVisible data-toc-label=isComponentSelectionPageVisible }


### *obj*.**componentSelectionPageCallbackBody** *class 'NoneType'* default: *None* { #componentSelectionPageCallbackBody data-toc-label=componentSelectionPageCallbackBody }


### *obj*.**componentSelectionPageInjection** *class 'NoneType'* default: *None* { #componentSelectionPageInjection data-toc-label=componentSelectionPageInjection }


### *obj*.**isAutoComponentSelectionPageCallback** *class 'bool'* default: *True* { #isAutoComponentSelectionPageCallback data-toc-label=isAutoComponentSelectionPageCallback }


### *obj*.**isLicenseAgreementPageVisible** *class 'bool'* default: *True* { #isLicenseAgreementPageVisible data-toc-label=isLicenseAgreementPageVisible }


### *obj*.**licenseAgreementPageCallbackBody** *class 'NoneType'* default: *None* { #licenseAgreementPageCallbackBody data-toc-label=licenseAgreementPageCallbackBody }


### *obj*.**isAutoLicenseAgreementPageCallback** *class 'bool'* default: *True* { #isAutoLicenseAgreementPageCallback data-toc-label=isAutoLicenseAgreementPageCallback }


### *obj*.**isStartMenuDirectoryPageVisible** *class 'bool'* default: *True* { #isStartMenuDirectoryPageVisible data-toc-label=isStartMenuDirectoryPageVisible }


### *obj*.**startMenuDirectoryPageCallbackBody** *class 'NoneType'* default: *None* { #startMenuDirectoryPageCallbackBody data-toc-label=startMenuDirectoryPageCallbackBody }


### *obj*.**isAutoStartMenuDirectoryPageCallback** *class 'bool'* default: *True* { #isAutoStartMenuDirectoryPageCallback data-toc-label=isAutoStartMenuDirectoryPageCallback }


### *obj*.**isReadyForInstallationPageVisible** *class 'bool'* default: *True* { #isReadyForInstallationPageVisible data-toc-label=isReadyForInstallationPageVisible }


### *obj*.**readyForInstallationPageCallbackBody** *class 'NoneType'* default: *None* { #readyForInstallationPageCallbackBody data-toc-label=readyForInstallationPageCallbackBody }


### *obj*.**readyForInstallationPageOnInstall** *class 'NoneType'* default: *None* { #readyForInstallationPageOnInstall data-toc-label=readyForInstallationPageOnInstall }


### *obj*.**readyForInstallationPageOnMaintain** *class 'NoneType'* default: *None* { #readyForInstallationPageOnMaintain data-toc-label=readyForInstallationPageOnMaintain }


### *obj*.**isAutoReadyForInstallationPageCallback** *class 'bool'* default: *True* { #isAutoReadyForInstallationPageCallback data-toc-label=isAutoReadyForInstallationPageCallback }


### *obj*.**isPerformInstallationPageVisible** *class 'bool'* default: *True* { #isPerformInstallationPageVisible data-toc-label=isPerformInstallationPageVisible }


### *obj*.**performInstallationPageCallbackBody** *class 'NoneType'* default: *None* { #performInstallationPageCallbackBody data-toc-label=performInstallationPageCallbackBody }


### *obj*.**isAutoPerformInstallationPageCallback** *class 'bool'* default: *True* { #isAutoPerformInstallationPageCallback data-toc-label=isAutoPerformInstallationPageCallback }


### *obj*.**isFinishedPageVisible** *class 'bool'* default: *True* { #isFinishedPageVisible data-toc-label=isFinishedPageVisible }


### *obj*.**finishedPageCallbackBody** *class 'NoneType'* default: *None* { #finishedPageCallbackBody data-toc-label=finishedPageCallbackBody }


### *obj*.**finishedPageOnInstall** *class 'NoneType'* default: *None* { #finishedPageOnInstall data-toc-label=finishedPageOnInstall }


### *obj*.**finishedPageOnMaintain** *class 'NoneType'* default: *None* { #finishedPageOnMaintain data-toc-label=finishedPageOnMaintain }


### *obj*.**isAutoFinishedPageCallback** *class 'bool'* default: *True* { #isAutoFinishedPageCallback data-toc-label=isAutoFinishedPageCallback }


### *obj*.**isRunProgVisible** *class 'bool'* default: *True* { #isRunProgVisible data-toc-label=isRunProgVisible }


### *obj*.**isRunProgEnabled** *class 'bool'* default: *True* { #isRunProgEnabled data-toc-label=isRunProgEnabled }


### *obj*.**isRunProgChecked** *class 'bool'* default: *True* { #isRunProgChecked data-toc-label=isRunProgChecked }


### *QtIfwControlScript*.**andList**`#!py3 (conditions)` { #andList data-toc-label=andList }


### *QtIfwControlScript*.**assertInternetConnected**`#!py3 (isRefresh=False, errMsg=None, isAutoQuote=True)` { #assertInternetConnected data-toc-label=assertInternetConnected }


### *QtIfwControlScript*.**assignCurrentPageWidgetVar**`#!py3 (varName='page')` { #assignCurrentPageWidgetVar data-toc-label=assignCurrentPageWidgetVar }


### *QtIfwControlScript*.**assignCustomPageWidgetVar**`#!py3 (pageName, varName='page')` { #assignCustomPageWidgetVar data-toc-label=assignCustomPageWidgetVar }


### *QtIfwControlScript*.**assignPageWidgetVar**`#!py3 (pageId, varName='page')` { #assignPageWidgetVar data-toc-label=assignPageWidgetVar }


### *QtIfwControlScript*.**assignRegistryEntryVar**`#!py3 (key, valueName, isAutoBitContext=True, varName='regValue', isAutoQuote=True)` { #assignRegistryEntryVar data-toc-label=assignRegistryEntryVar }


### *QtIfwControlScript*.**boolToString**`#!py3 (b)` { #boolToString data-toc-label=boolToString }


### *QtIfwControlScript*.**clickButton**`#!py3 (buttonName, delayMillis=None)` { #clickButton data-toc-label=clickButton }


### *QtIfwControlScript*.**cmdLineArg**`#!py3 (arg, default='')` { #cmdLineArg data-toc-label=cmdLineArg }


### *QtIfwControlScript*.**cmdLineListArg**`#!py3 (arg, default=None)` { #cmdLineListArg data-toc-label=cmdLineListArg }


### *QtIfwControlScript*.**cmdLineSwitchArg**`#!py3 (arg, isNegated=False, isHardFalse=False)` { #cmdLineSwitchArg data-toc-label=cmdLineSwitchArg }


### *QtIfwControlScript*.**connectButtonClickHandler**`#!py3 (buttonName, slotName)` { #connectButtonClickHandler data-toc-label=connectButtonClickHandler }


### *QtIfwControlScript*.**connectWidgetEventHandler**`#!py3 (controlName, eventName, slotName)` { #connectWidgetEventHandler data-toc-label=connectWidgetEventHandler }


### *QtIfwControlScript*.**currentPageWidget**`#!py3 ()` { #currentPageWidget data-toc-label=currentPageWidget }


### *QtIfwControlScript*.**customPageWidget**`#!py3 (name)` { #customPageWidget data-toc-label=customPageWidget }


### *QtIfwControlScript*.**debugPopup**`#!py3 (msg, isAutoQuote=True)` { #debugPopup data-toc-label=debugPopup }


### *QtIfwControlScript*.**deleteDetachedOpDataFile**`#!py3 (fileName)` { #deleteDetachedOpDataFile data-toc-label=deleteDetachedOpDataFile }


### *QtIfwControlScript*.**deleteFile**`#!py3 (path, isAutoQuote=True)` { #deleteFile data-toc-label=deleteFile }


### *QtIfwControlScript*.**deleteOpDataFile**`#!py3 (fileName)` { #deleteOpDataFile data-toc-label=deleteOpDataFile }


### *QtIfwControlScript*.**disableQuit**`#!py3 ()` { #disableQuit data-toc-label=disableQuit }


### *QtIfwControlScript*.**disableQuitPrompt**`#!py3 ()` { #disableQuitPrompt data-toc-label=disableQuitPrompt }


### *QtIfwControlScript*.**dropElevation**`#!py3 ()` { #dropElevation data-toc-label=dropElevation }


### *QtIfwControlScript*.**elevate**`#!py3 ()` { #elevate data-toc-label=elevate }


### *QtIfwControlScript*.**embedResources**`#!py3 (embeddedResources)` { #embedResources data-toc-label=embedResources }


### *QtIfwControlScript*.**enable**`#!py3 (controlName, isEnable=True)` { #enable data-toc-label=enable }

DOES NOT WORK FOR WIZARD BUTTONS!!! 
### *QtIfwControlScript*.**enableComponent**`#!py3 (package, enable=True, isAutoQuote=True)` { #enableComponent data-toc-label=enableComponent }


### *QtIfwControlScript*.**enableCustom**`#!py3 (controlName, isEnable=True, pageVar='page')` { #enableCustom data-toc-label=enableCustom }

DOES NOT WORK FOR WIZARD BUTTONS!!! 
### *QtIfwControlScript*.**enableNextButton**`#!py3 (isEnable=True)` { #enableNextButton data-toc-label=enableNextButton }

ONLY WORKS ON DYNAMIC / CUSTOM PAGES! 
### *QtIfwControlScript*.**errorPopup**`#!py3 (msg, isAutoQuote=True)` { #errorPopup data-toc-label=errorPopup }


### *QtIfwControlScript*.**genResources**`#!py3 (embeddedResources, isTempRootTarget=False)` { #genResources data-toc-label=genResources }


### *QtIfwControlScript*.**getComponent**`#!py3 (name, isAutoQuote=True)` { #getComponent data-toc-label=getComponent }


### *QtIfwControlScript*.**getCustomText**`#!py3 (controlName, pageVar='page')` { #getCustomText data-toc-label=getCustomText }


### *QtIfwControlScript*.**getEnv**`#!py3 (varName, isAutoQuote=True)` { #getEnv data-toc-label=getEnv }


### *QtIfwControlScript*.**getPageOwner**`#!py3 (pageName, isAutoQuote=True)` { #getPageOwner data-toc-label=getPageOwner }


### *QtIfwControlScript*.**getText**`#!py3 (controlName)` { #getText data-toc-label=getText }


### *QtIfwControlScript*.**hideDefaultPage**`#!py3 (pageName)` { #hideDefaultPage data-toc-label=hideDefaultPage }


### *QtIfwControlScript*.**ifAutoPilot**`#!py3 (isNegated=False, isMultiLine=False)` { #ifAutoPilot data-toc-label=ifAutoPilot }


### *QtIfwControlScript*.**ifBoolValue**`#!py3 (key, isNegated=False, isHardFalse=False, isMultiLine=False)` { #ifBoolValue data-toc-label=ifBoolValue }


### *QtIfwControlScript*.**ifChecked**`#!py3 (checkboxName, isNegated=False, isMultiLine=False)` { #ifChecked data-toc-label=ifChecked }


### *QtIfwControlScript*.**ifCmdLineArg**`#!py3 (arg, isNegated=False, isMultiLine=False)` { #ifCmdLineArg data-toc-label=ifCmdLineArg }


### *QtIfwControlScript*.**ifCmdLineSwitch**`#!py3 (arg, isNegated=False, isHardFalse=False, isMultiLine=False)` { #ifCmdLineSwitch data-toc-label=ifCmdLineSwitch }


### *QtIfwControlScript*.**ifComponentEnabled**`#!py3 (package, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifComponentEnabled data-toc-label=ifComponentEnabled }


### *QtIfwControlScript*.**ifComponentInstalled**`#!py3 (package, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifComponentInstalled data-toc-label=ifComponentInstalled }


### *QtIfwControlScript*.**ifComponentSelected**`#!py3 (package, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifComponentSelected data-toc-label=ifComponentSelected }


### *QtIfwControlScript*.**ifCondition**`#!py3 (condition, isNegated=False, isMultiLine=False)` { #ifCondition data-toc-label=ifCondition }


### *QtIfwControlScript*.**ifCustomChecked**`#!py3 (checkboxName, pageVar='page', isNegated=False, isMultiLine=False)` { #ifCustomChecked data-toc-label=ifCustomChecked }


### *QtIfwControlScript*.**ifCustomEnabled**`#!py3 (controlName, pageVar='page', isNegated=False, isMultiLine=False)` { #ifCustomEnabled data-toc-label=ifCustomEnabled }


### *QtIfwControlScript*.**ifCustomVisible**`#!py3 (controlName, pageVar='page', isNegated=False, isMultiLine=False)` { #ifCustomVisible data-toc-label=ifCustomVisible }


### *QtIfwControlScript*.**ifDryRun**`#!py3 (isNegated=False, isMultiLine=False)` { #ifDryRun data-toc-label=ifDryRun }


### *QtIfwControlScript*.**ifElevated**`#!py3 (isNegated=False, isMultiLine=False)` { #ifElevated data-toc-label=ifElevated }


### *QtIfwControlScript*.**ifEnabled**`#!py3 (controlName, isNegated=False, isMultiLine=False)` { #ifEnabled data-toc-label=ifEnabled }


### *QtIfwControlScript*.**ifInstalling**`#!py3 (isNegated=False, isMultiLine=False)` { #ifInstalling data-toc-label=ifInstalling }


### *QtIfwControlScript*.**ifInternetConnected**`#!py3 (isRefresh=False, isNegated=False, isMultiLine=False)` { #ifInternetConnected data-toc-label=ifInternetConnected }


### *QtIfwControlScript*.**ifMaintenanceTool**`#!py3 (isNegated=False, isMultiLine=False)` { #ifMaintenanceTool data-toc-label=ifMaintenanceTool }


### *QtIfwControlScript*.**ifPathExists**`#!py3 (path, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifPathExists data-toc-label=ifPathExists }


### *QtIfwControlScript*.**ifPingable**`#!py3 (uri, pings=3, totalMaxSecs=12, isAutoQuote=True, isNegated=False, isMultiLine=False)` { #ifPingable data-toc-label=ifPingable }


### *QtIfwControlScript*.**ifRegistryEntryExists**`#!py3 (key, valueName, isAutoBitContext=True, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryEntryExists data-toc-label=ifRegistryEntryExists }


### *QtIfwControlScript*.**ifRegistryEntryExistsLike**`#!py3 (key, valueNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryEntryExistsLike data-toc-label=ifRegistryEntryExistsLike }


### *QtIfwControlScript*.**ifRegistryKeyExists**`#!py3 (key, isAutoBitContext=True, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryKeyExists data-toc-label=ifRegistryKeyExists }


### *QtIfwControlScript*.**ifRegistryKeyExistsLike**`#!py3 (parentKey, childKeyNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryKeyExistsLike data-toc-label=ifRegistryKeyExistsLike }


### *QtIfwControlScript*.**ifValueDefined**`#!py3 (key, isNegated=False, isMultiLine=False)` { #ifValueDefined data-toc-label=ifValueDefined }


### *QtIfwControlScript*.**ifVisible**`#!py3 (controlName, isNegated=False, isMultiLine=False)` { #ifVisible data-toc-label=ifVisible }


### *QtIfwControlScript*.**ifYesNoPopup**`#!py3 (msg, title='Question', resultVar='result', isMultiLine=False)` { #ifYesNoPopup data-toc-label=ifYesNoPopup }


### *QtIfwControlScript*.**insertCustomPage**`#!py3 (pageName, position)` { #insertCustomPage data-toc-label=insertCustomPage }


### *QtIfwControlScript*.**insertCustomWidget**`#!py3 (widgetName, pageName, position=None)` { #insertCustomWidget data-toc-label=insertCustomWidget }


### *QtIfwControlScript*.**isAutoPilot**`#!py3 (isNegated=False)` { #isAutoPilot data-toc-label=isAutoPilot }


### *QtIfwControlScript*.**isChecked**`#!py3 (checkboxName)` { #isChecked data-toc-label=isChecked }


### *QtIfwControlScript*.**isComponentEnabled**`#!py3 (package, isAutoQuote=True)` { #isComponentEnabled data-toc-label=isComponentEnabled }


### *QtIfwControlScript*.**isComponentInstalled**`#!py3 (package, isAutoQuote=True)` { #isComponentInstalled data-toc-label=isComponentInstalled }


### *QtIfwControlScript*.**isComponentSelected**`#!py3 (package, isAutoQuote=True)` { #isComponentSelected data-toc-label=isComponentSelected }


### *QtIfwControlScript*.**isCustomChecked**`#!py3 (checkboxName, pageVar='page')` { #isCustomChecked data-toc-label=isCustomChecked }


### *QtIfwControlScript*.**isCustomEnabled**`#!py3 (controlName, pageVar='page')` { #isCustomEnabled data-toc-label=isCustomEnabled }


### *QtIfwControlScript*.**isCustomVisible**`#!py3 (controlName, pageVar='page')` { #isCustomVisible data-toc-label=isCustomVisible }


### *QtIfwControlScript*.**isDryRun**`#!py3 (isNegated=False)` { #isDryRun data-toc-label=isDryRun }


### *QtIfwControlScript*.**isElevated**`#!py3 ()` { #isElevated data-toc-label=isElevated }


### *QtIfwControlScript*.**isEnabled**`#!py3 (controlName)` { #isEnabled data-toc-label=isEnabled }


### *QtIfwControlScript*.**isInstalling**`#!py3 (isNegated=False)` { #isInstalling data-toc-label=isInstalling }


### *QtIfwControlScript*.**isInternetConnected**`#!py3 (isRefresh=False)` { #isInternetConnected data-toc-label=isInternetConnected }


### *QtIfwControlScript*.**isMaintenanceTool**`#!py3 (isNegated=False)` { #isMaintenanceTool data-toc-label=isMaintenanceTool }


### *QtIfwControlScript*.**isPingable**`#!py3 (uri, pings=3, totalMaxSecs=12, isAutoQuote=True)` { #isPingable data-toc-label=isPingable }


### *QtIfwControlScript*.**isVisible**`#!py3 (controlName)` { #isVisible data-toc-label=isVisible }


### *QtIfwControlScript*.**killAll**`#!py3 (exeName, isAutoQuote=True)` { #killAll data-toc-label=killAll }


### *QtIfwControlScript*.**log**`#!py3 (msg, isAutoQuote=True)` { #log data-toc-label=log }


### *QtIfwControlScript*.**logSwitch**`#!py3 (key)` { #logSwitch data-toc-label=logSwitch }


### *QtIfwControlScript*.**logValue**`#!py3 (key, defaultVal='')` { #logValue data-toc-label=logValue }


### *QtIfwControlScript*.**lookupBoolValue**`#!py3 (key, isNegated=False, isHardFalse=False, isAutoQuote=True)` { #lookupBoolValue data-toc-label=lookupBoolValue }


### *QtIfwControlScript*.**lookupValue**`#!py3 (key, default='', isAutoQuote=True)` { #lookupValue data-toc-label=lookupValue }


### *QtIfwControlScript*.**lookupValueList**`#!py3 (key, defaultList=None, isAutoQuote=True, delimiter=None)` { #lookupValueList data-toc-label=lookupValueList }


### *QtIfwControlScript*.**makeDir**`#!py3 (path, isAutoQuote=True)` { #makeDir data-toc-label=makeDir }


### *QtIfwControlScript*.**openViaOs**`#!py3 (path, isAutoQuote=True)` { #openViaOs data-toc-label=openViaOs }


### *QtIfwControlScript*.**orList**`#!py3 (conditions)` { #orList data-toc-label=orList }


### *QtIfwControlScript*.**pageWidget**`#!py3 (pageId)` { #pageWidget data-toc-label=pageWidget }


### *QtIfwControlScript*.**pathExists**`#!py3 (path, isNegated=False, isAutoQuote=True)` { #pathExists data-toc-label=pathExists }


### *QtIfwControlScript*.**productName**`#!py3 ()` { #productName data-toc-label=productName }


### *QtIfwControlScript*.**quit**`#!py3 (msg, isError=True, isSilent=False, isAutoQuote=True)` { #quit data-toc-label=quit }


### *QtIfwControlScript*.**quote**`#!py3 (value)` { #quote data-toc-label=quote }


### *QtIfwControlScript*.**registryEntryExists**`#!py3 (key, valueName, isAutoBitContext=True, isAutoQuote=True)` { #registryEntryExists data-toc-label=registryEntryExists }


### *QtIfwControlScript*.**registryEntryExistsLike**`#!py3 (key, valueNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isAutoQuote=True)` { #registryEntryExistsLike data-toc-label=registryEntryExistsLike }


### *QtIfwControlScript*.**registryEntryValue**`#!py3 (key, valueName, isAutoBitContext=True, isAutoQuote=True)` { #registryEntryValue data-toc-label=registryEntryValue }


### *QtIfwControlScript*.**registryKeyExists**`#!py3 (key, isAutoBitContext=True, isAutoQuote=True)` { #registryKeyExists data-toc-label=registryKeyExists }


### *QtIfwControlScript*.**registryKeyExistsLike**`#!py3 (parentKey, childKeyNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isAutoQuote=True)` { #registryKeyExistsLike data-toc-label=registryKeyExistsLike }


### *QtIfwControlScript*.**removeCustomPage**`#!py3 (pageName)` { #removeCustomPage data-toc-label=removeCustomPage }


### *QtIfwControlScript*.**removeCustomWidget**`#!py3 (widgetName)` { #removeCustomWidget data-toc-label=removeCustomWidget }


### *QtIfwControlScript*.**removeDir**`#!py3 (path, isAutoQuote=True)` { #removeDir data-toc-label=removeDir }


### *QtIfwControlScript*.**resolveDynamTxtVarsOperations**`#!py3 (plasticFile, destPath)` { #resolveDynamTxtVarsOperations data-toc-label=resolveDynamTxtVarsOperations }


### *QtIfwControlScript*.**resolveDynamicVars**`#!py3 (s, varNames=None, isAutoQuote=True)` { #resolveDynamicVars data-toc-label=resolveDynamicVars }


### *QtIfwControlScript*.**resolveScriptVars**`#!py3 (scripts, subDir)` { #resolveScriptVars data-toc-label=resolveScriptVars }


### *QtIfwControlScript*.**resolveScriptVarsOperations**`#!py3 (scripts, subDir)` { #resolveScriptVarsOperations data-toc-label=resolveScriptVarsOperations }


### *QtIfwControlScript*.**selectAllComponents**`#!py3 (isSelect=True)` { #selectAllComponents data-toc-label=selectAllComponents }


### *QtIfwControlScript*.**selectComponent**`#!py3 (package, isSelect=True, isAutoQuote=True)` { #selectComponent data-toc-label=selectComponent }


### *QtIfwControlScript*.**selectDefaultComponents**`#!py3 ()` { #selectDefaultComponents data-toc-label=selectDefaultComponents }


### *QtIfwControlScript*.**setBoolValue**`#!py3 (key, b, isAutoQuote=True)` { #setBoolValue data-toc-label=setBoolValue }


### *QtIfwControlScript*.**setChecked**`#!py3 (checkboxName, isCheck=True)` { #setChecked data-toc-label=setChecked }


### *QtIfwControlScript*.**setCustomCheckBox**`#!py3 (checkboxName, isCheck=True, pageVar='page')` { #setCustomCheckBox data-toc-label=setCustomCheckBox }


### *QtIfwControlScript*.**setCustomPageText**`#!py3 (title, description, isAutoQuote=True, pageVar='page')` { #setCustomPageText data-toc-label=setCustomPageText }


### *QtIfwControlScript*.**setCustomPageTitle**`#!py3 (title, isAutoQuote=True, pageVar='page')` { #setCustomPageTitle data-toc-label=setCustomPageTitle }


### *QtIfwControlScript*.**setCustomText**`#!py3 (controlName, text, isAutoQuote=True, pageVar='page')` { #setCustomText data-toc-label=setCustomText }


### *QtIfwControlScript*.**setCustomVisible**`#!py3 (controlName, isVisible=True, pageVar='page')` { #setCustomVisible data-toc-label=setCustomVisible }

DOES NOT WORK FOR WIZARD BUTTONS!!! 
### *QtIfwControlScript*.**setText**`#!py3 (controlName, text, varNames=None, isAutoQuote=True)` { #setText data-toc-label=setText }


### *QtIfwControlScript*.**setValue**`#!py3 (key, value, isAutoQuote=True)` { #setValue data-toc-label=setValue }


### *QtIfwControlScript*.**setValueFromRegistryEntry**`#!py3 (key, regKey, valueName, isAutoBitContext=True, isAutoQuote=True)` { #setValueFromRegistryEntry data-toc-label=setValueFromRegistryEntry }


### *QtIfwControlScript*.**setVisible**`#!py3 (controlName, isVisible=True)` { #setVisible data-toc-label=setVisible }

DOES NOT WORK FOR WIZARD BUTTONS!!! 
### *QtIfwControlScript*.**startMenuDir**`#!py3 ()` { #startMenuDir data-toc-label=startMenuDir }


### *QtIfwControlScript*.**stringToBool**`#!py3 (value, isAutoQuote=True)` { #stringToBool data-toc-label=stringToBool }


### *QtIfwControlScript*.**switchYesNoCancelPopup**`#!py3 (msg, title='Question', resultVar='result', onYes='', onNo='', onCancel='')` { #switchYesNoCancelPopup data-toc-label=switchYesNoCancelPopup }


### *QtIfwControlScript*.**targetDir**`#!py3 ()` { #targetDir data-toc-label=targetDir }


### *QtIfwControlScript*.**toBool**`#!py3 (b)` { #toBool data-toc-label=toBool }


### *QtIfwControlScript*.**toDefaultPageId**`#!py3 (pageName)` { #toDefaultPageId data-toc-label=toDefaultPageId }


### *QtIfwControlScript*.**toNull**`#!py3 (v)` { #toNull data-toc-label=toNull }


### *QtIfwControlScript*.**warningPopup**`#!py3 (msg, isAutoQuote=True)` { #warningPopup data-toc-label=warningPopup }


### *QtIfwControlScript*.**writeDetachedOpDataFile**`#!py3 (fileName, content='', isAutoQuote=True)` { #writeDetachedOpDataFile data-toc-label=writeDetachedOpDataFile }


### *QtIfwControlScript*.**writeFile**`#!py3 (path, content, isAutoQuote=True)` { #writeFile data-toc-label=writeFile }


### *QtIfwControlScript*.**writeOpDataFile**`#!py3 (fileName, content='', isAutoQuote=True)` { #writeOpDataFile data-toc-label=writeOpDataFile }


### *QtIfwControlScript*.**yesNoCancelPopup**`#!py3 (msg, title='Question', resultVar='result')` { #yesNoCancelPopup data-toc-label=yesNoCancelPopup }


### *QtIfwControlScript*.**yesNoPopup**`#!py3 (msg, title='Question', resultVar='result')` { #yesNoPopup data-toc-label=yesNoPopup }


### *QtIfwControlScript*.**ABORT** *class 'str'* default: *"QMessageBox.Abort"* { #ABORT data-toc-label=ABORT }


### *QtIfwControlScript*.**ACCEPT_EULA_CMD_ARG** *class 'str'* default: *"accept"* { #ACCEPT_EULA_CMD_ARG data-toc-label=ACCEPT_EULA_CMD_ARG }


### *QtIfwControlScript*.**ACCEPT_EULA_RADIO_BUTTON** *class 'str'* default: *"AcceptLicenseRadioButton"* { #ACCEPT_EULA_RADIO_BUTTON data-toc-label=ACCEPT_EULA_RADIO_BUTTON }


### *QtIfwControlScript*.**AND** *class 'str'* default: *" && "* { #AND data-toc-label=AND }


### *QtIfwControlScript*.**ASSIGN** *class 'str'* default: *"="* { #ASSIGN data-toc-label=ASSIGN }


### *QtIfwControlScript*.**AUTH_ERROR_MSGBOX_ID** *class 'str'* default: *"AuthorizationError"* { #AUTH_ERROR_MSGBOX_ID data-toc-label=AUTH_ERROR_MSGBOX_ID }


### *QtIfwControlScript*.**AUTO_PILOT_CMD_ARG** *class 'str'* default: *"auto"* { #AUTO_PILOT_CMD_ARG data-toc-label=AUTO_PILOT_CMD_ARG }


### *QtIfwControlScript*.**BACK_BUTTON** *class 'str'* default: *"buttons.BackButton"* { #BACK_BUTTON data-toc-label=BACK_BUTTON }


### *QtIfwControlScript*.**CANCEL** *class 'str'* default: *"QMessageBox.Cancel"* { #CANCEL data-toc-label=CANCEL }


### *QtIfwControlScript*.**CANCEL_BUTTON** *class 'str'* default: *"buttons.CancelButton"* { #CANCEL_BUTTON data-toc-label=CANCEL_BUTTON }


### *QtIfwControlScript*.**CATCH** *class 'str'* default: *"catch(e) { "* { #CATCH data-toc-label=CATCH }


### *QtIfwControlScript*.**COMMIT_BUTTON** *class 'str'* default: *"buttons.CommitButton"* { #COMMIT_BUTTON data-toc-label=COMMIT_BUTTON }


### *QtIfwControlScript*.**CONCAT** *class 'str'* default: *" + "* { #CONCAT data-toc-label=CONCAT }


### *QtIfwControlScript*.**CUSTOM_BUTTON_1** *class 'str'* default: *"buttons.CustomButton1"* { #CUSTOM_BUTTON_1 data-toc-label=CUSTOM_BUTTON_1 }


### *QtIfwControlScript*.**CUSTOM_BUTTON_2** *class 'str'* default: *"buttons.CustomButton2"* { #CUSTOM_BUTTON_2 data-toc-label=CUSTOM_BUTTON_2 }


### *QtIfwControlScript*.**CUSTOM_BUTTON_3** *class 'str'* default: *"buttons.CustomButton3"* { #CUSTOM_BUTTON_3 data-toc-label=CUSTOM_BUTTON_3 }


### *QtIfwControlScript*.**DEFAULT_FINISHED_MESSAGE** *class 'str'* default: *"Click finish to exit the @ProductName@ Wizard."* { #DEFAULT_FINISHED_MESSAGE data-toc-label=DEFAULT_FINISHED_MESSAGE }


### *QtIfwControlScript*.**DEFAULT_TARGET_DIR_KEY** *class 'str'* default: *"DefaultTargetDir"* { #DEFAULT_TARGET_DIR_KEY data-toc-label=DEFAULT_TARGET_DIR_KEY }


### *QtIfwControlScript*.**DRYRUN_CMD_ARG** *class 'str'* default: *"dryrun"* { #DRYRUN_CMD_ARG data-toc-label=DRYRUN_CMD_ARG }


### *QtIfwControlScript*.**ELSE** *class 'str'* default: *"else "* { #ELSE data-toc-label=ELSE }


### *QtIfwControlScript*.**END_BLOCK** *class 'str'* default: *"}
"* { #END_BLOCK data-toc-label=END_BLOCK }


### *QtIfwControlScript*.**END_LINE** *class 'str'* default: *";
"* { #END_LINE data-toc-label=END_LINE }


### *QtIfwControlScript*.**EQUAL_TO** *class 'str'* default: *" == "* { #EQUAL_TO data-toc-label=EQUAL_TO }


### *QtIfwControlScript*.**ERR_LOG_DEFAULT_PATH** *class 'str'* default: *"%temp%\\installer.err"* { #ERR_LOG_DEFAULT_PATH data-toc-label=ERR_LOG_DEFAULT_PATH }


### *QtIfwControlScript*.**ERR_LOG_PATH_CMD_ARG** *class 'str'* default: *"errlog"* { #ERR_LOG_PATH_CMD_ARG data-toc-label=ERR_LOG_PATH_CMD_ARG }


### *QtIfwControlScript*.**EXCLUDE_LIST_CMD_ARG** *class 'str'* default: *"exclude"* { #EXCLUDE_LIST_CMD_ARG data-toc-label=EXCLUDE_LIST_CMD_ARG }


### *QtIfwControlScript*.**EXIT_FUNCTION** *class 'str'* default: *"
return;
"* { #EXIT_FUNCTION data-toc-label=EXIT_FUNCTION }


### *QtIfwControlScript*.**FALSE** *class 'str'* default: *"false"* { #FALSE data-toc-label=FALSE }


### *QtIfwControlScript*.**FINISHED_MESSAGE_LABEL** *class 'str'* default: *"MessageLabel"* { #FINISHED_MESSAGE_LABEL data-toc-label=FINISHED_MESSAGE_LABEL }


### *QtIfwControlScript*.**FINISH_BUTTON** *class 'str'* default: *"buttons.FinishButton"* { #FINISH_BUTTON data-toc-label=FINISH_BUTTON }


### *QtIfwControlScript*.**HELP_BUTTON** *class 'str'* default: *"buttons.HelpButton"* { #HELP_BUTTON data-toc-label=HELP_BUTTON }


### *QtIfwControlScript*.**IF** *class 'str'* default: *"if "* { #IF data-toc-label=IF }


### *QtIfwControlScript*.**INCLUDE_LIST_CMD_ARG** *class 'str'* default: *"include"* { #INCLUDE_LIST_CMD_ARG data-toc-label=INCLUDE_LIST_CMD_ARG }


### *QtIfwControlScript*.**INSTALL_LIST_CMD_ARG** *class 'str'* default: *"install"* { #INSTALL_LIST_CMD_ARG data-toc-label=INSTALL_LIST_CMD_ARG }


### *QtIfwControlScript*.**INTERUPTED_KEY** *class 'str'* default: *"isInterupted"* { #INTERUPTED_KEY data-toc-label=INTERUPTED_KEY }


### *QtIfwControlScript*.**IS_NET_CONNECTED_KEY** *class 'str'* default: *"isNetConnected"* { #IS_NET_CONNECTED_KEY data-toc-label=IS_NET_CONNECTED_KEY }


### *QtIfwControlScript*.**MAINTAIN_MODE_CMD_ARG** *class 'str'* default: *"mode"* { #MAINTAIN_MODE_CMD_ARG data-toc-label=MAINTAIN_MODE_CMD_ARG }


### *QtIfwControlScript*.**MAINTAIN_MODE_OPT_ADD_REMOVE** *class 'str'* default: *"addremove"* { #MAINTAIN_MODE_OPT_ADD_REMOVE data-toc-label=MAINTAIN_MODE_OPT_ADD_REMOVE }


### *QtIfwControlScript*.**MAINTAIN_MODE_OPT_REMOVE_ALL** *class 'str'* default: *"removeall"* { #MAINTAIN_MODE_OPT_REMOVE_ALL data-toc-label=MAINTAIN_MODE_OPT_REMOVE_ALL }


### *QtIfwControlScript*.**MAINTAIN_MODE_OPT_UPDATE** *class 'str'* default: *"update"* { #MAINTAIN_MODE_OPT_UPDATE data-toc-label=MAINTAIN_MODE_OPT_UPDATE }


### *QtIfwControlScript*.**MAINTAIN_PASSTHRU_CMD_ARG** *class 'str'* default: *"maintpassthru"* { #MAINTAIN_PASSTHRU_CMD_ARG data-toc-label=MAINTAIN_PASSTHRU_CMD_ARG }


### *QtIfwControlScript*.**MAINTENANCE_TOOL_NAME** *class 'str'* default: *"maintenancetool.exe"* { #MAINTENANCE_TOOL_NAME data-toc-label=MAINTENANCE_TOOL_NAME }


### *QtIfwControlScript*.**NEW_LINE** *class 'str'* default: *"
"* { #NEW_LINE data-toc-label=NEW_LINE }


### *QtIfwControlScript*.**NEXT_BUTTON** *class 'str'* default: *"buttons.NextButton"* { #NEXT_BUTTON data-toc-label=NEXT_BUTTON }


### *QtIfwControlScript*.**NO** *class 'str'* default: *"QMessageBox.No"* { #NO data-toc-label=NO }


### *QtIfwControlScript*.**NOT** *class 'str'* default: *"! "* { #NOT data-toc-label=NOT }


### *QtIfwControlScript*.**NOT_EQUAL_TO** *class 'str'* default: *" != "* { #NOT_EQUAL_TO data-toc-label=NOT_EQUAL_TO }


### *QtIfwControlScript*.**NULL** *class 'str'* default: *"null"* { #NULL data-toc-label=NULL }


### *QtIfwControlScript*.**OK** *class 'str'* default: *"QMessageBox.Yes"* { #OK data-toc-label=OK }


### *QtIfwControlScript*.**OR** *class 'str'* default: *" || "* { #OR data-toc-label=OR }


### *QtIfwControlScript*.**OUT_LOG_DEFAULT_PATH** *class 'str'* default: *"%temp%\\installer.out"* { #OUT_LOG_DEFAULT_PATH data-toc-label=OUT_LOG_DEFAULT_PATH }


### *QtIfwControlScript*.**OUT_LOG_PATH_CMD_ARG** *class 'str'* default: *"outlog"* { #OUT_LOG_PATH_CMD_ARG data-toc-label=OUT_LOG_PATH_CMD_ARG }


### *QtIfwControlScript*.**PATH_SEP** *class 'str'* default: *""\\""* { #PATH_SEP data-toc-label=PATH_SEP }


### *QtIfwControlScript*.**PRODUCT_NAME_KEY** *class 'str'* default: *"ProductName"* { #PRODUCT_NAME_KEY data-toc-label=PRODUCT_NAME_KEY }


### *QtIfwControlScript*.**QUIT_MSGBOX_ID** *class 'str'* default: *"cancelInstallation"* { #QUIT_MSGBOX_ID data-toc-label=QUIT_MSGBOX_ID }


### *QtIfwControlScript*.**REBOOT_CMD_ARG** *class 'str'* default: *"reboot"* { #REBOOT_CMD_ARG data-toc-label=REBOOT_CMD_ARG }


### *QtIfwControlScript*.**RESTORE_MSGBOX_DEFAULT** *class 'str'* default: *"QMessageBox.RestoreDefaults"* { #RESTORE_MSGBOX_DEFAULT data-toc-label=RESTORE_MSGBOX_DEFAULT }


### *QtIfwControlScript*.**RUN_PROGRAM_CHECKBOX** *class 'str'* default: *"RunItCheckBox"* { #RUN_PROGRAM_CHECKBOX data-toc-label=RUN_PROGRAM_CHECKBOX }


### *QtIfwControlScript*.**RUN_PROGRAM_CMD_ARG** *class 'str'* default: *"run"* { #RUN_PROGRAM_CMD_ARG data-toc-label=RUN_PROGRAM_CMD_ARG }


### *QtIfwControlScript*.**STARTMENU_DIR_KEY** *class 'str'* default: *"StartMenuDir"* { #STARTMENU_DIR_KEY data-toc-label=STARTMENU_DIR_KEY }


### *QtIfwControlScript*.**START_BLOCK** *class 'str'* default: *"{
"* { #START_BLOCK data-toc-label=START_BLOCK }


### *QtIfwControlScript*.**START_MENU_DIR_CMD_ARG** *class 'str'* default: *"startmenu"* { #START_MENU_DIR_CMD_ARG data-toc-label=START_MENU_DIR_CMD_ARG }


### *QtIfwControlScript*.**START_MENU_DIR_EDITBOX** *class 'str'* default: *"StartMenuPathLineEdit"* { #START_MENU_DIR_EDITBOX data-toc-label=START_MENU_DIR_EDITBOX }


### *QtIfwControlScript*.**TAB** *class 'str'* default: *"    "* { #TAB data-toc-label=TAB }


### *QtIfwControlScript*.**TARGET_DIR_CMD_ARG** *class 'str'* default: *"target"* { #TARGET_DIR_CMD_ARG data-toc-label=TARGET_DIR_CMD_ARG }


### *QtIfwControlScript*.**TARGET_DIR_EDITBOX** *class 'str'* default: *"TargetDirectoryLineEdit"* { #TARGET_DIR_EDITBOX data-toc-label=TARGET_DIR_EDITBOX }


### *QtIfwControlScript*.**TARGET_DIR_KEY** *class 'str'* default: *"TargetDir"* { #TARGET_DIR_KEY data-toc-label=TARGET_DIR_KEY }


### *QtIfwControlScript*.**TARGET_EXISTS_OPT_CMD_ARG** *class 'str'* default: *"onexist"* { #TARGET_EXISTS_OPT_CMD_ARG data-toc-label=TARGET_EXISTS_OPT_CMD_ARG }


### *QtIfwControlScript*.**TARGET_EXISTS_OPT_FAIL** *class 'str'* default: *"fail"* { #TARGET_EXISTS_OPT_FAIL data-toc-label=TARGET_EXISTS_OPT_FAIL }


### *QtIfwControlScript*.**TARGET_EXISTS_OPT_PROMPT** *class 'str'* default: *"prompt"* { #TARGET_EXISTS_OPT_PROMPT data-toc-label=TARGET_EXISTS_OPT_PROMPT }


### *QtIfwControlScript*.**TARGET_EXISTS_OPT_REMOVE** *class 'str'* default: *"remove"* { #TARGET_EXISTS_OPT_REMOVE data-toc-label=TARGET_EXISTS_OPT_REMOVE }


### *QtIfwControlScript*.**TRUE** *class 'str'* default: *"true"* { #TRUE data-toc-label=TRUE }


### *QtIfwControlScript*.**TRY** *class 'str'* default: *"try { "* { #TRY data-toc-label=TRY }


### *QtIfwControlScript*.**USER_KEY** *class 'str'* default: *"User"* { #USER_KEY data-toc-label=USER_KEY }


### *QtIfwControlScript*.**VERBOSE_CMD_SWITCH_ARG** *class 'str'* default: *"-v"* { #VERBOSE_CMD_SWITCH_ARG data-toc-label=VERBOSE_CMD_SWITCH_ARG }


### *QtIfwControlScript*.**YES** *class 'str'* default: *"QMessageBox.Yes"* { #YES data-toc-label=YES }



______

## **QtIfwDynamicOperationsPage**`#!py3 class` { #QtIfwDynamicOperationsPage data-toc-label=QtIfwDynamicOperationsPage }



**Base Classes:**

_QtIfwInterface, QtIfwUiPage


**Magic Methods:**

 - [`__init__`](#QtIfwDynamicOperationsPage-init)

**Instance Methods:** 

 - [`fileName`](#fileName)
 - [`resolve`](#resolve)
 - [`write`](#write)

**Instance Attributes:** 

 - [`supportScript`](#supportScript)
 - [`name`](#name)
 - [`args`](#args)
 - [`body`](#body)
 - [`delayMillis`](#delayMillis)
 - [`standardPageId`](#standardPageId)
 - [`customPageName`](#customPageName)

**Class/Static Methods:** 

 - [`onCompleted`](#onCompleted)

**Class/Static Attributes:** 

 - [`AsyncFunc`](#AsyncFunc)
 - [`BASE_ON_ENTER_TMPT`](#BASE_ON_ENTER_TMPT)
 - [`BASE_ON_LOAD_TMPT`](#BASE_ON_LOAD_TMPT)

### **QtIfwDynamicOperationsPage**`#!py3 (name, operation='', asyncFuncs=None, order=0, onCompletedDelayMillis=None)` { #QtIfwDynamicOperationsPage-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**resolve**`#!py3 (self, qtIfwConfig)` { #resolve data-toc-label=resolve }


### *obj*.**write**`#!py3 (self, dirPath)` { #write data-toc-label=write }


### *obj*.**supportScript** *class 'NoneType'* default: *None* { #supportScript data-toc-label=supportScript }


### *obj*.**name** *class 'NoneType'* default: *None* { #name data-toc-label=name }


### *obj*.**args** *class 'NoneType'* default: *None* { #args data-toc-label=args }


### *obj*.**body** *class 'NoneType'* default: *None* { #body data-toc-label=body }


### *obj*.**delayMillis** *class 'NoneType'* default: *None* { #delayMillis data-toc-label=delayMillis }


### *obj*.**standardPageId** *class 'NoneType'* default: *None* { #standardPageId data-toc-label=standardPageId }


### *obj*.**customPageName** *class 'NoneType'* default: *None* { #customPageName data-toc-label=customPageName }


### *QtIfwDynamicOperationsPage*.**onCompleted**`#!py3 (name)` { #onCompleted data-toc-label=onCompleted }


### *QtIfwDynamicOperationsPage*.**AsyncFunc** *class 'type'* default: *None* { #AsyncFunc data-toc-label=AsyncFunc }


### *QtIfwDynamicOperationsPage*.**BASE_ON_ENTER_TMPT** *class 'str'* default: *None* { #BASE_ON_ENTER_TMPT data-toc-label=BASE_ON_ENTER_TMPT }


### *QtIfwDynamicOperationsPage*.**BASE_ON_LOAD_TMPT** *class 'str'* default: *None* { #BASE_ON_LOAD_TMPT data-toc-label=BASE_ON_LOAD_TMPT }


## **QtIfwDynamicOperationsPage.AsyncFunc**`#!py3 class` { #QtIfwDynamicOperationsPage.AsyncFunc data-toc-label=QtIfwDynamicOperationsPage.AsyncFunc }



**Instance Methods:** 

 - [`invoke`](#invoke)

### *obj*.**invoke**`#!py3 (self, args=None, isAutoQuote=True)` { #invoke data-toc-label=invoke }



______

## **QtIfwExeWrapper**`#!py3 class` { #QtIfwExeWrapper data-toc-label=QtIfwExeWrapper }



**Magic Methods:**

 - [`__init__`](#QtIfwExeWrapper-init)

**Instance Methods:** 

 - [`refresh`](#refresh)

**Instance Attributes:** 

 - [`exeName`](#exeName)
 - [`isGui`](#isGui)
 - [`wrapperScript`](#wrapperScript)
 - [`exeDir`](#exeDir)
 - [`workingDir`](#workingDir)
 - [`args`](#args)
 - [`envVars`](#envVars)
 - [`isElevated`](#isElevated)
 - [`isExe`](#isExe)
 - [`wrapperExeName`](#wrapperExeName)
 - [`wrapperIconName`](#wrapperIconName)

### **QtIfwExeWrapper**`#!py3 (exeName, isGui=False, wrapperScript=None, exeDir='@TargetDir@', workingDir=None, args=None, envVars=None, isElevated=False, isExe=False)` { #QtIfwExeWrapper-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**refresh**`#!py3 (self)` { #refresh data-toc-label=refresh }


### *obj*.**exeName** *class 'NoneType'* default: *None* { #exeName data-toc-label=exeName }


### *obj*.**isGui** *class 'NoneType'* default: *None* { #isGui data-toc-label=isGui }


### *obj*.**wrapperScript** *class 'NoneType'* default: *None* { #wrapperScript data-toc-label=wrapperScript }


### *obj*.**exeDir** *class 'NoneType'* default: *None* { #exeDir data-toc-label=exeDir }


### *obj*.**workingDir** *class 'NoneType'* default: *None* { #workingDir data-toc-label=workingDir }


### *obj*.**args** *class 'NoneType'* default: *None* { #args data-toc-label=args }


### *obj*.**envVars** *class 'NoneType'* default: *None* { #envVars data-toc-label=envVars }


### *obj*.**isElevated** *class 'NoneType'* default: *None* { #isElevated data-toc-label=isElevated }


### *obj*.**isExe** *class 'NoneType'* default: *None* { #isExe data-toc-label=isExe }


### *obj*.**wrapperExeName** *class 'NoneType'* default: *None* { #wrapperExeName data-toc-label=wrapperExeName }


### *obj*.**wrapperIconName** *class 'NoneType'* default: *None* { #wrapperIconName data-toc-label=wrapperIconName }



______

## **QtIfwExternalOp**`#!py3 class` { #QtIfwExternalOp data-toc-label=QtIfwExternalOp }



**Magic Methods:**

 - [`__init__`](#QtIfwExternalOp-init)

**Instance Methods:** 


**Instance Attributes:** 

 - [`script`](#script)
 - [`exePath`](#exePath)
 - [`args`](#args)
 - [`successRetCodes`](#successRetCodes)
 - [`uninstScript`](#uninstScript)
 - [`uninstExePath`](#uninstExePath)
 - [`uninstArgs`](#uninstArgs)
 - [`uninstRetCodes`](#uninstRetCodes)
 - [`isElevated`](#isElevated)
 - [`workingDir`](#workingDir)
 - [`onErrorMessage`](#onErrorMessage)
 - [`resourceScripts`](#resourceScripts)
 - [`uninstResourceScripts`](#uninstResourceScripts)
 - [`externalRes`](#externalRes)

**Class/Static Methods:** 

 - [`CopyExeVerInfoScript`](#CopyExeVerInfoScript)
 - [`CopyExternalResource`](#CopyExternalResource)
 - [`CopyFile`](#CopyFile)
 - [`CopyFileScript`](#CopyFileScript)
 - [`CreateExeFromScript`](#CreateExeFromScript)
 - [`CreateOpFlagFile`](#CreateOpFlagFile)
 - [`CreateOpFlagFileScript`](#CreateOpFlagFileScript)
 - [`CreateRegistryEntry`](#CreateRegistryEntry)
 - [`CreateRegistryEntryScript`](#CreateRegistryEntryScript)
 - [`CreateRegistryKey`](#CreateRegistryKey)
 - [`CreateRegistryKeyScript`](#CreateRegistryKeyScript)
 - [`CreateStartupEntry`](#CreateStartupEntry)
 - [`CreateWindowsAppFoundFlagFile`](#CreateWindowsAppFoundFlagFile)
 - [`CreateWindowsAppFoundFlagFileScript`](#CreateWindowsAppFoundFlagFileScript)
 - [`EmbedExeVerInfoScript`](#EmbedExeVerInfoScript)
 - [`ExtractIconsFromExeScript`](#ExtractIconsFromExeScript)
 - [`MakeDir`](#MakeDir)
 - [`MakeDirScript`](#MakeDirScript)
 - [`RemoveDir`](#RemoveDir)
 - [`RemoveDirScript`](#RemoveDirScript)
 - [`RemoveFile`](#RemoveFile)
 - [`RemoveFileScript`](#RemoveFileScript)
 - [`RemoveRegistryEntry`](#RemoveRegistryEntry)
 - [`RemoveRegistryEntryScript`](#RemoveRegistryEntryScript)
 - [`RemoveRegistryKey`](#RemoveRegistryKey)
 - [`RemoveRegistryKeyScript`](#RemoveRegistryKeyScript)
 - [`ReplacePrimaryIconInExeScript`](#ReplacePrimaryIconInExeScript)
 - [`RunProgram`](#RunProgram)
 - [`RunProgramScript`](#RunProgramScript)
 - [`Script2Exe`](#Script2Exe)
 - [`Script2ExeScript`](#Script2ExeScript)
 - [`UninstallWindowsApp`](#UninstallWindowsApp)
 - [`UninstallWindowsAppScript`](#UninstallWindowsAppScript)
 - [`WaitForProcess`](#WaitForProcess)
 - [`WaitForProcessScript`](#WaitForProcessScript)
 - [`WrapperScript2Exe`](#WrapperScript2Exe)
 - [`WriteFile`](#WriteFile)
 - [`WriteFileScript`](#WriteFileScript)
 - [`WriteOpDataFile`](#WriteOpDataFile)
 - [`WriteOpDataFileScript`](#WriteOpDataFileScript)
 - [`appleScriptSelfDestructSnippet`](#appleScriptSelfDestructSnippet)
 - [`batchSelfDestructSnippet`](#batchSelfDestructSnippet)
 - [`opDataPath`](#opDataPath)
 - [`powerShellSelfDestructSnippet`](#powerShellSelfDestructSnippet)
 - [`shellScriptSelfDestructSnippet`](#shellScriptSelfDestructSnippet)
 - [`vbScriptSelfDestructSnippet`](#vbScriptSelfDestructSnippet)

**Class/Static Attributes:** 

 - [`AUTO_UNDO`](#AUTO_UNDO)
 - [`ON_BOTH`](#ON_BOTH)
 - [`ON_INSTALL`](#ON_INSTALL)
 - [`ON_UNINSTALL`](#ON_UNINSTALL)

### **QtIfwExternalOp**`#!py3 (script=None, exePath=None, args=None, successRetCodes=None, uninstScript=None, uninstExePath=None, uninstArgs=None, uninstRetCodes=None, isElevated=False, workingDir='@TargetDir@', onErrorMessage=None, resourceScripts=None, uninstResourceScripts=None, externalRes=None)` { #QtIfwExternalOp-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**script** *class 'NoneType'* default: *None* { #script data-toc-label=script }


### *obj*.**exePath** *class 'NoneType'* default: *None* { #exePath data-toc-label=exePath }


### *obj*.**args** *class 'list'* default: *[]* { #args data-toc-label=args }


### *obj*.**successRetCodes** *class 'list'* default: *[0]* { #successRetCodes data-toc-label=successRetCodes }


### *obj*.**uninstScript** *class 'NoneType'* default: *None* { #uninstScript data-toc-label=uninstScript }


### *obj*.**uninstExePath** *class 'NoneType'* default: *None* { #uninstExePath data-toc-label=uninstExePath }


### *obj*.**uninstArgs** *class 'list'* default: *[]* { #uninstArgs data-toc-label=uninstArgs }


### *obj*.**uninstRetCodes** *class 'list'* default: *[0]* { #uninstRetCodes data-toc-label=uninstRetCodes }


### *obj*.**isElevated** *class 'NoneType'* default: *None* { #isElevated data-toc-label=isElevated }


### *obj*.**workingDir** *class 'NoneType'* default: *None* { #workingDir data-toc-label=workingDir }


### *obj*.**onErrorMessage** *class 'NoneType'* default: *None* { #onErrorMessage data-toc-label=onErrorMessage }


### *obj*.**resourceScripts** *class 'list'* default: *[]* { #resourceScripts data-toc-label=resourceScripts }


### *obj*.**uninstResourceScripts** *class 'list'* default: *[]* { #uninstResourceScripts data-toc-label=uninstResourceScripts }


### *obj*.**externalRes** *class 'list'* default: *[]* { #externalRes data-toc-label=externalRes }


### *QtIfwExternalOp*.**CopyExeVerInfoScript**`#!py3 (srcExePath, destExePath)` { #CopyExeVerInfoScript data-toc-label=CopyExeVerInfoScript }


### *QtIfwExternalOp*.**CopyExternalResource**`#!py3 (event, externRes, destPath, contentKey=None, owner='@User@', group='@User@', access='644', isElevated=True)` { #CopyExternalResource data-toc-label=CopyExternalResource }


### *QtIfwExternalOp*.**CopyFile**`#!py3 (event, scrPath, destPath, owner='@User@', group='@User@', access='644', isElevated=True)` { #CopyFile data-toc-label=CopyFile }


### *QtIfwExternalOp*.**CopyFileScript**`#!py3 (srcPath, destPath, owner='@User@', group='@User@', access='644')` { #CopyFileScript data-toc-label=CopyFileScript }


### *QtIfwExternalOp*.**CreateExeFromScript**`#!py3 (script, exeVerInfo, srcIconPath, targetDir='@TargetDir@')` { #CreateExeFromScript data-toc-label=CreateExeFromScript }


### *QtIfwExternalOp*.**CreateOpFlagFile**`#!py3 (event, fileName, dynamicVar=None, isElevated=True)` { #CreateOpFlagFile data-toc-label=CreateOpFlagFile }


### *QtIfwExternalOp*.**CreateOpFlagFileScript**`#!py3 (fileName, dynamicVar=None)` { #CreateOpFlagFileScript data-toc-label=CreateOpFlagFileScript }


### *QtIfwExternalOp*.**CreateRegistryEntry**`#!py3 (event, key, valueName=None, value='', valueType='String', isAutoBitContext=True)` { #CreateRegistryEntry data-toc-label=CreateRegistryEntry }


### *QtIfwExternalOp*.**CreateRegistryEntryScript**`#!py3 (key, valueName=None, value='', valueType='String', isAutoBitContext=True, replacements=None)` { #CreateRegistryEntryScript data-toc-label=CreateRegistryEntryScript }


### *QtIfwExternalOp*.**CreateRegistryKey**`#!py3 (event, key, isAutoBitContext=True)` { #CreateRegistryKey data-toc-label=CreateRegistryKey }


### *QtIfwExternalOp*.**CreateRegistryKeyScript**`#!py3 (key, isAutoBitContext=True, replacements=None)` { #CreateRegistryKeyScript data-toc-label=CreateRegistryKeyScript }


### *QtIfwExternalOp*.**CreateStartupEntry**`#!py3 (pkg=None, exePath=None, displayName=None, isAllUsers=False)` { #CreateStartupEntry data-toc-label=CreateStartupEntry }


### *QtIfwExternalOp*.**CreateWindowsAppFoundFlagFile**`#!py3 (event, appName, fileName, isAutoBitContext=True)` { #CreateWindowsAppFoundFlagFile data-toc-label=CreateWindowsAppFoundFlagFile }


### *QtIfwExternalOp*.**CreateWindowsAppFoundFlagFileScript**`#!py3 (appName, fileName, isAutoBitContext=True, isSelfDestruct=False)` { #CreateWindowsAppFoundFlagFileScript data-toc-label=CreateWindowsAppFoundFlagFileScript }


### *QtIfwExternalOp*.**EmbedExeVerInfoScript**`#!py3 (exePath, exeVerInfo)` { #EmbedExeVerInfoScript data-toc-label=EmbedExeVerInfoScript }


### *QtIfwExternalOp*.**ExtractIconsFromExeScript**`#!py3 (exePath, targetDirPath)` { #ExtractIconsFromExeScript data-toc-label=ExtractIconsFromExeScript }


### *QtIfwExternalOp*.**MakeDir**`#!py3 (event, dirPath, owner='@User@', group='@User@', access='755', isElevated=True)` { #MakeDir data-toc-label=MakeDir }


### *QtIfwExternalOp*.**MakeDirScript**`#!py3 (dirPath, owner='@User@', group='@User@', access='755')` { #MakeDirScript data-toc-label=MakeDirScript }


### *QtIfwExternalOp*.**RemoveDir**`#!py3 (event, dirPath, isElevated=True)` { #RemoveDir data-toc-label=RemoveDir }


### *QtIfwExternalOp*.**RemoveDirScript**`#!py3 (dirPath)` { #RemoveDirScript data-toc-label=RemoveDirScript }


### *QtIfwExternalOp*.**RemoveFile**`#!py3 (event, filePath, isElevated=True)` { #RemoveFile data-toc-label=RemoveFile }


### *QtIfwExternalOp*.**RemoveFileScript**`#!py3 (filePath)` { #RemoveFileScript data-toc-label=RemoveFileScript }


### *QtIfwExternalOp*.**RemoveRegistryEntry**`#!py3 (event, key, valueName=None, isAutoBitContext=True)` { #RemoveRegistryEntry data-toc-label=RemoveRegistryEntry }


### *QtIfwExternalOp*.**RemoveRegistryEntryScript**`#!py3 (key, valueName=None, isAutoBitContext=True, replacements=None)` { #RemoveRegistryEntryScript data-toc-label=RemoveRegistryEntryScript }


### *QtIfwExternalOp*.**RemoveRegistryKey**`#!py3 (event, key, isAutoBitContext=True)` { #RemoveRegistryKey data-toc-label=RemoveRegistryKey }


### *QtIfwExternalOp*.**RemoveRegistryKeyScript**`#!py3 (key, isAutoBitContext=True, replacements=None)` { #RemoveRegistryKeyScript data-toc-label=RemoveRegistryKeyScript }


### *QtIfwExternalOp*.**ReplacePrimaryIconInExeScript**`#!py3 (exePath, iconDirPath, iconName=None, isIconDirRemoved=False)` { #ReplacePrimaryIconInExeScript data-toc-label=ReplacePrimaryIconInExeScript }

Note the use of if %PROCESSOR_ARCHITECTURE%==x86 ( "%windir%\sysnative\cmd" ...
That is **extremely important** here, as "ie4uinit" is a 64 bit program, 
and the installer runs in 32 bit context. The use %windir%\sysnative\cmd 
allows this 32 bit program to "see" and execute a 64 bit sub process.
Without that, you get mind blowing errors thrown back at you saying the  
the file does not even exist (including when you specify an absolute path 
to the file you know for a fact is found there)!
### *QtIfwExternalOp*.**RunProgram**`#!py3 (event, path, arguments=None, isAutoQuote=True, isHidden=False, isSynchronous=True, isElevated=True, runConditionFileName=None, isRunConditionNegated=False, isAutoBitContext=True)` { #RunProgram data-toc-label=RunProgram }


### *QtIfwExternalOp*.**RunProgramScript**`#!py3 (path, arguments=None, isAutoQuote=True, isHidden=False, isSynchronous=True, runConditionFileName=None, isRunConditionNegated=False, isAutoBitContext=True, replacements=None)` { #RunProgramScript data-toc-label=RunProgramScript }


### *QtIfwExternalOp*.**Script2Exe**`#!py3 (scriptPath, exePath, exeVerInfo, iconDirPath, iconName, isScriptRemoved=False, isIconDirRemoved=False)` { #Script2Exe data-toc-label=Script2Exe }


### *QtIfwExternalOp*.**Script2ExeScript**`#!py3 (srcPath, destPath, isSrcRemoved=False)` { #Script2ExeScript data-toc-label=Script2ExeScript }


### *QtIfwExternalOp*.**UninstallWindowsApp**`#!py3 (event, appName, arguments=None, isSynchronous=True, isHidden=True, isAutoBitContext=True, isSuccessOnNotFound=True)` { #UninstallWindowsApp data-toc-label=UninstallWindowsApp }


### *QtIfwExternalOp*.**UninstallWindowsAppScript**`#!py3 (appName, arguments=None, isSynchronous=True, isHidden=True, isAutoBitContext=True, isSelfDestruct=False)` { #UninstallWindowsAppScript data-toc-label=UninstallWindowsAppScript }


### *QtIfwExternalOp*.**WaitForProcess**`#!py3 (event, exeName=None, pidFileName=None, timeOutSeconds=30, isWaitForStart=False, isSuccessNoWait=True, isAutoBitContext=True)` { #WaitForProcess data-toc-label=WaitForProcess }


### *QtIfwExternalOp*.**WaitForProcessScript**`#!py3 (exeName=None, pidFileName=None, timeOutSeconds=30, onTimeout=None, isWaitForStart=False, isDeletePidFile=False, isExitOnSuccess=True, isExitOnNoWait=True, isExitOnTimeout=True, isSelfDestruct=False, isAutoBitContext=True)` { #WaitForProcessScript data-toc-label=WaitForProcessScript }


### *QtIfwExternalOp*.**WrapperScript2Exe**`#!py3 (scriptPath, exePath, targetPath, iconName=None)` { #WrapperScript2Exe data-toc-label=WrapperScript2Exe }


### *QtIfwExternalOp*.**WriteFile**`#!py3 (event, filePath, data, isOverwrite=True, owner='@User@', group='@User@', access='644', isElevated=True)` { #WriteFile data-toc-label=WriteFile }


### *QtIfwExternalOp*.**WriteFileScript**`#!py3 (filePath, data=None, isOverwrite=True, owner='@User@', group='@User@', access='644')` { #WriteFileScript data-toc-label=WriteFileScript }


### *QtIfwExternalOp*.**WriteOpDataFile**`#!py3 (event, fileName, data, isElevated=True)` { #WriteOpDataFile data-toc-label=WriteOpDataFile }


### *QtIfwExternalOp*.**WriteOpDataFileScript**`#!py3 (fileName, data=None)` { #WriteOpDataFileScript data-toc-label=WriteOpDataFileScript }


### *QtIfwExternalOp*.**appleScriptSelfDestructSnippet**`#!py3 ()` { #appleScriptSelfDestructSnippet data-toc-label=appleScriptSelfDestructSnippet }


### *QtIfwExternalOp*.**batchSelfDestructSnippet**`#!py3 ()` { #batchSelfDestructSnippet data-toc-label=batchSelfDestructSnippet }


### *QtIfwExternalOp*.**opDataPath**`#!py3 (rootFileName, isDetached=False, isNative=True, quotes=None, isDoubleBackslash=False)` { #opDataPath data-toc-label=opDataPath }


### *QtIfwExternalOp*.**powerShellSelfDestructSnippet**`#!py3 ()` { #powerShellSelfDestructSnippet data-toc-label=powerShellSelfDestructSnippet }


### *QtIfwExternalOp*.**shellScriptSelfDestructSnippet**`#!py3 ()` { #shellScriptSelfDestructSnippet data-toc-label=shellScriptSelfDestructSnippet }


### *QtIfwExternalOp*.**vbScriptSelfDestructSnippet**`#!py3 ()` { #vbScriptSelfDestructSnippet data-toc-label=vbScriptSelfDestructSnippet }


### *QtIfwExternalOp*.**AUTO_UNDO** *class 'int'* default: *3* { #AUTO_UNDO data-toc-label=AUTO_UNDO }


### *QtIfwExternalOp*.**ON_BOTH** *class 'int'* default: *2* { #ON_BOTH data-toc-label=ON_BOTH }


### *QtIfwExternalOp*.**ON_INSTALL** *class 'int'* default: *0* { #ON_INSTALL data-toc-label=ON_INSTALL }


### *QtIfwExternalOp*.**ON_UNINSTALL** *class 'int'* default: *1* { #ON_UNINSTALL data-toc-label=ON_UNINSTALL }



______

## **QtIfwExternalResource**`#!py3 class` { #QtIfwExternalResource data-toc-label=QtIfwExternalResource }



**Magic Methods:**

 - [`__init__`](#QtIfwExternalResource-init)

**Instance Methods:** 

 - [`targetDirPath`](#targetDirPath)
 - [`targetDirPathVar`](#targetDirPathVar)
 - [`targetPath`](#targetPath)
 - [`targetPathVar`](#targetPathVar)

**Instance Attributes:** 

 - [`name`](#name)
 - [`srcPath`](#srcPath)
 - [`destPath`](#destPath)
 - [`isMaintenanceNeed`](#isMaintenanceNeed)
 - [`contentKeys`](#contentKeys)

**Class/Static Methods:** 

 - [`BuiltIn`](#BuiltIn)

**Class/Static Attributes:** 

 - [`RESOURCE_HACKER`](#RESOURCE_HACKER)

### **QtIfwExternalResource**`#!py3 (name, srcPath, srcBasePath=None, destPath=None, isMaintenanceNeed=False, contentKeys=None)` { #QtIfwExternalResource-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**targetDirPath**`#!py3 (self)` { #targetDirPath data-toc-label=targetDirPath }


### *obj*.**targetDirPathVar**`#!py3 (self)` { #targetDirPathVar data-toc-label=targetDirPathVar }


### *obj*.**targetPath**`#!py3 (self, key=None)` { #targetPath data-toc-label=targetPath }


### *obj*.**targetPathVar**`#!py3 (self, key=None)` { #targetPathVar data-toc-label=targetPathVar }


### *obj*.**name** *class 'NoneType'* default: *None* { #name data-toc-label=name }


### *obj*.**srcPath** *class 'NoneType'* default: *None* { #srcPath data-toc-label=srcPath }


### *obj*.**destPath** *class 'NoneType'* default: *None* { #destPath data-toc-label=destPath }


### *obj*.**isMaintenanceNeed** *class 'NoneType'* default: *None* { #isMaintenanceNeed data-toc-label=isMaintenanceNeed }


### *obj*.**contentKeys** *class 'NoneType'* default: *None* { #contentKeys data-toc-label=contentKeys }


### *QtIfwExternalResource*.**BuiltIn**`#!py3 (name, isMaintenanceNeed=False)` { #BuiltIn data-toc-label=BuiltIn }


### *QtIfwExternalResource*.**RESOURCE_HACKER** *class 'str'* default: *None* { #RESOURCE_HACKER data-toc-label=RESOURCE_HACKER }



______

## **QtIfwKillOp**`#!py3 class` { #QtIfwKillOp data-toc-label=QtIfwKillOp }



**Magic Methods:**

 - [`__init__`](#QtIfwKillOp-init)

**Instance Methods:** 


**Instance Attributes:** 

 - [`processName`](#processName)
 - [`onInstall`](#onInstall)
 - [`onUninstall`](#onUninstall)
 - [`isElevated`](#isElevated)

### **QtIfwKillOp**`#!py3 (processName, onInstall=True, onUninstall=True)` { #QtIfwKillOp-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**processName** *class 'NoneType'* default: *None* { #processName data-toc-label=processName }


### *obj*.**onInstall** *class 'NoneType'* default: *None* { #onInstall data-toc-label=onInstall }


### *obj*.**onUninstall** *class 'NoneType'* default: *None* { #onUninstall data-toc-label=onUninstall }


### *obj*.**isElevated** *class 'bool'* default: *True* { #isElevated data-toc-label=isElevated }



______

## **QtIfwOnFinishedCheckbox**`#!py3 class` { #QtIfwOnFinishedCheckbox data-toc-label=QtIfwOnFinishedCheckbox }



**Base Classes:**

QtIfwOnFinishedDetachedExec, _QtIfwInterface, QtIfwWidget


**Magic Methods:**

 - [`__init__`](#QtIfwOnFinishedCheckbox-init)

**Instance Methods:** 

 - [`enable`](#enable)
 - [`fileName`](#fileName)
 - [`isChecked`](#isChecked)
 - [`resolve`](#resolve)
 - [`setChecked`](#setChecked)
 - [`setVisible`](#setVisible)
 - [`write`](#write)

**Instance Attributes:** 

 - [`checkboxName`](#checkboxName)
 - [`text`](#text)

**Class/Static Attributes:** 

 - [`BASE_ON_LOAD_TMPT`](#BASE_ON_LOAD_TMPT)
 - [`ON_BOTH`](#ON_BOTH)
 - [`ON_INSTALL`](#ON_INSTALL)
 - [`ON_UNINSTALL`](#ON_UNINSTALL)

### **QtIfwOnFinishedCheckbox**`#!py3 (name, text=None, position=None, ifwPackage=None, runProgram=None, argList=None, shellCmd=None, script=None, openViaOsPath=None, isReboot=False, rebootDelaySecs=2, isVisible=True, isEnabled=True, isChecked=True)` { #QtIfwOnFinishedCheckbox-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**enable**`#!py3 (self, isEnable=True)` { #enable data-toc-label=enable }


### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**isChecked**`#!py3 (self)` { #isChecked data-toc-label=isChecked }


### *obj*.**resolve**`#!py3 (self, qtIfwConfig)` { #resolve data-toc-label=resolve }


### *obj*.**setChecked**`#!py3 (self, isChecked=True)` { #setChecked data-toc-label=setChecked }


### *obj*.**setVisible**`#!py3 (self, isVisible=True)` { #setVisible data-toc-label=setVisible }


### *obj*.**write**`#!py3 (self, dirPath)` { #write data-toc-label=write }


### *obj*.**checkboxName** *class 'NoneType'* default: *None* { #checkboxName data-toc-label=checkboxName }


### *obj*.**text** *class 'NoneType'* default: *None* { #text data-toc-label=text }


### *QtIfwOnFinishedCheckbox*.**BASE_ON_LOAD_TMPT** *class 'str'* default: *None* { #BASE_ON_LOAD_TMPT data-toc-label=BASE_ON_LOAD_TMPT }


### *QtIfwOnFinishedCheckbox*.**ON_BOTH** *class 'int'* default: *None* { #ON_BOTH data-toc-label=ON_BOTH }


### *QtIfwOnFinishedCheckbox*.**ON_INSTALL** *class 'int'* default: *None* { #ON_INSTALL data-toc-label=ON_INSTALL }


### *QtIfwOnFinishedCheckbox*.**ON_UNINSTALL** *class 'int'* default: *None* { #ON_UNINSTALL data-toc-label=ON_UNINSTALL }



______

## **QtIfwOnFinishedDetachedExec**`#!py3 class` { #QtIfwOnFinishedDetachedExec data-toc-label=QtIfwOnFinishedDetachedExec }



**Magic Methods:**

 - [`__init__`](#QtIfwOnFinishedDetachedExec-init)

**Instance Methods:** 


**Instance Attributes:** 

 - [`name`](#name)
 - [`event`](#event)
 - [`runProgram`](#runProgram)
 - [`argList`](#argList)
 - [`script`](#script)
 - [`isReboot`](#isReboot)
 - [`ifCondition`](#ifCondition)

**Class/Static Attributes:** 

 - [`ON_BOTH`](#ON_BOTH)
 - [`ON_INSTALL`](#ON_INSTALL)
 - [`ON_UNINSTALL`](#ON_UNINSTALL)

### **QtIfwOnFinishedDetachedExec**`#!py3 (name, event=None, ifwPackage=None, runProgram=None, argList=None, shellCmd=None, script=None, openViaOsPath=None, isReboot=False, rebootDelaySecs=2, ifCondition=None)` { #QtIfwOnFinishedDetachedExec-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**name** *class 'NoneType'* default: *None* { #name data-toc-label=name }


### *obj*.**event** *class 'int'* default: *0* { #event data-toc-label=event }


### *obj*.**runProgram** *class 'NoneType'* default: *None* { #runProgram data-toc-label=runProgram }


### *obj*.**argList** *class 'NoneType'* default: *None* { #argList data-toc-label=argList }


### *obj*.**script** *class 'NoneType'* default: *None* { #script data-toc-label=script }


### *obj*.**isReboot** *class 'NoneType'* default: *None* { #isReboot data-toc-label=isReboot }


### *obj*.**ifCondition** *class 'NoneType'* default: *None* { #ifCondition data-toc-label=ifCondition }


### *QtIfwOnFinishedDetachedExec*.**ON_BOTH** *class 'int'* default: *2* { #ON_BOTH data-toc-label=ON_BOTH }


### *QtIfwOnFinishedDetachedExec*.**ON_INSTALL** *class 'int'* default: *0* { #ON_INSTALL data-toc-label=ON_INSTALL }


### *QtIfwOnFinishedDetachedExec*.**ON_UNINSTALL** *class 'int'* default: *1* { #ON_UNINSTALL data-toc-label=ON_UNINSTALL }



______

## **QtIfwPackage**`#!py3 class` { #QtIfwPackage data-toc-label=QtIfwPackage }



**Magic Methods:**

 - [`__init__`](#QtIfwPackage-init)

**Instance Methods:** 

 - [`contentDirPath`](#contentDirPath)
 - [`contentTopDirPath`](#contentTopDirPath)
 - [`dirPath`](#dirPath)
 - [`metaDirPath`](#metaDirPath)

**Instance Attributes:** 

 - [`pkgId`](#pkgId)
 - [`pkgType`](#pkgType)
 - [`name`](#name)
 - [`pkgXml`](#pkgXml)
 - [`pkgScript`](#pkgScript)
 - [`uiPages`](#uiPages)
 - [`widgets`](#widgets)
 - [`licenses`](#licenses)
 - [`isLicenseFormatPreserved`](#isLicenseFormatPreserved)
 - [`srcDirPath`](#srcDirPath)
 - [`srcExePath`](#srcExePath)
 - [`resBasePath`](#resBasePath)
 - [`distResources`](#distResources)
 - [`isTempSrc`](#isTempSrc)
 - [`subDirName`](#subDirName)
 - [`exeName`](#exeName)
 - [`isGui`](#isGui)
 - [`exeWrapper`](#exeWrapper)
 - [`codeSignTargets`](#codeSignTargets)
 - [`qtCppConfig`](#qtCppConfig)

**Class/Static Methods:** 

 - [`topDirPath`](#topDirPath)

**Class/Static Attributes:** 

 - [`Type`](#Type)

### **QtIfwPackage**`#!py3 (pkgId=None, pkgType=None, name=None, subDirName=None, srcDirPath=None, srcExePath=None, resBasePath=None, isTempSrc=False, pkgXml=None, pkgScript=None, licenses=None, uiPages=None, widgets=None)` { #QtIfwPackage-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**contentDirPath**`#!py3 (self)` { #contentDirPath data-toc-label=contentDirPath }


### *obj*.**contentTopDirPath**`#!py3 (self)` { #contentTopDirPath data-toc-label=contentTopDirPath }


### *obj*.**dirPath**`#!py3 (self)` { #dirPath data-toc-label=dirPath }


### *obj*.**metaDirPath**`#!py3 (self)` { #metaDirPath data-toc-label=metaDirPath }


### *obj*.**pkgId** *class 'NoneType'* default: *None* { #pkgId data-toc-label=pkgId }


### *obj*.**pkgType** *class 'NoneType'* default: *None* { #pkgType data-toc-label=pkgType }


### *obj*.**name** *class 'NoneType'* default: *None* { #name data-toc-label=name }


### *obj*.**pkgXml** *class 'NoneType'* default: *None* { #pkgXml data-toc-label=pkgXml }


### *obj*.**pkgScript** *class 'NoneType'* default: *None* { #pkgScript data-toc-label=pkgScript }


### *obj*.**uiPages** *class 'list'* default: *[]* { #uiPages data-toc-label=uiPages }


### *obj*.**widgets** *class 'list'* default: *[]* { #widgets data-toc-label=widgets }


### *obj*.**licenses** *class 'dict'* default: *{}* { #licenses data-toc-label=licenses }


### *obj*.**isLicenseFormatPreserved** *class 'bool'* default: *False* { #isLicenseFormatPreserved data-toc-label=isLicenseFormatPreserved }


### *obj*.**srcDirPath** *class 'NoneType'* default: *None* { #srcDirPath data-toc-label=srcDirPath }


### *obj*.**srcExePath** *class 'NoneType'* default: *None* { #srcExePath data-toc-label=srcExePath }


### *obj*.**resBasePath** *class 'NoneType'* default: *None* { #resBasePath data-toc-label=resBasePath }


### *obj*.**distResources** *class 'NoneType'* default: *None* { #distResources data-toc-label=distResources }


### *obj*.**isTempSrc** *class 'NoneType'* default: *None* { #isTempSrc data-toc-label=isTempSrc }


### *obj*.**subDirName** *class 'NoneType'* default: *None* { #subDirName data-toc-label=subDirName }


### *obj*.**exeName** *class 'NoneType'* default: *None* { #exeName data-toc-label=exeName }


### *obj*.**isGui** *class 'bool'* default: *False* { #isGui data-toc-label=isGui }


### *obj*.**exeWrapper** *class 'NoneType'* default: *None* { #exeWrapper data-toc-label=exeWrapper }


### *obj*.**codeSignTargets** *class 'NoneType'* default: *None* { #codeSignTargets data-toc-label=codeSignTargets }


### *obj*.**qtCppConfig** *class 'NoneType'* default: *None* { #qtCppConfig data-toc-label=qtCppConfig }


### *QtIfwPackage*.**topDirPath**`#!py3 ()` { #topDirPath data-toc-label=topDirPath }


### *QtIfwPackage*.**Type** *class 'type'* default: *class 'qt_installer.QtIfwPackage.Type'* { #Type data-toc-label=Type }


## **QtIfwPackage.Type**`#!py3 class` { #QtIfwPackage.Type data-toc-label=QtIfwPackage.Type }



**Class/Static Attributes:** 

 - [`DATA`](#DATA)
 - [`IEXPRESS`](#IEXPRESS)
 - [`PY_INSTALLER`](#PY_INSTALLER)
 - [`QT_CPP`](#QT_CPP)
 - [`RAW`](#RAW)
 - [`RESOURCE`](#RESOURCE)

### *QtIfwPackage.Type*.**DATA** *class 'int'* default: *1* { #DATA data-toc-label=DATA }


### *QtIfwPackage.Type*.**IEXPRESS** *class 'int'* default: *4* { #IEXPRESS data-toc-label=IEXPRESS }


### *QtIfwPackage.Type*.**PY_INSTALLER** *class 'int'* default: *3* { #PY_INSTALLER data-toc-label=PY_INSTALLER }


### *QtIfwPackage.Type*.**QT_CPP** *class 'int'* default: *5* { #QT_CPP data-toc-label=QT_CPP }


### *QtIfwPackage.Type*.**RAW** *class 'int'* default: *0* { #RAW data-toc-label=RAW }


### *QtIfwPackage.Type*.**RESOURCE** *class 'int'* default: *2* { #RESOURCE data-toc-label=RESOURCE }



______

## **QtIfwPackageScript**`#!py3 class` { #QtIfwPackageScript data-toc-label=QtIfwPackageScript }



**Base Classes:**

_QtIfwScript


**Magic Methods:**

 - [`__init__`](#QtIfwPackageScript-init)

**Instance Methods:** 

 - [`addSimpleOperation`](#addSimpleOperation)
 - [`debug`](#debug)
 - [`dirPath`](#dirPath)
 - [`exists`](#exists)
 - [`path`](#path)
 - [`write`](#write)

**Instance Attributes:** 

 - [`pkgName`](#pkgName)
 - [`pkgVersion`](#pkgVersion)
 - [`pkgSubDirName`](#pkgSubDirName)
 - [`shortcuts`](#shortcuts)
 - [`externalOps`](#externalOps)
 - [`killOps`](#killOps)
 - [`preOpSupport`](#preOpSupport)
 - [`customOperations`](#customOperations)
 - [`bundledScripts`](#bundledScripts)
 - [`dynamicTexts`](#dynamicTexts)
 - [`installResources`](#installResources)
 - [`externalDependencies`](#externalDependencies)
 - [`areDependenciesPreserved`](#areDependenciesPreserved)
 - [`uiPages`](#uiPages)
 - [`widgets`](#widgets)
 - [`packageGlobals`](#packageGlobals)
 - [`isAutoGlobals`](#isAutoGlobals)
 - [`componentConstructorBody`](#componentConstructorBody)
 - [`isAutoComponentConstructor`](#isAutoComponentConstructor)
 - [`componentLoadedCallbackBody`](#componentLoadedCallbackBody)
 - [`isAutoComponentLoadedCallback`](#isAutoComponentLoadedCallback)
 - [`componentEnteredCallbackBody`](#componentEnteredCallbackBody)
 - [`isAutoComponentEnteredCallback`](#isAutoComponentEnteredCallback)
 - [`componentCreateOperationsBody`](#componentCreateOperationsBody)
 - [`isAutoComponentCreateOperations`](#isAutoComponentCreateOperations)
 - [`componentCreateOperationsForArchiveBody`](#componentCreateOperationsForArchiveBody)
 - [`isAutoComponentCreateOperationsForArchive`](#isAutoComponentCreateOperationsForArchive)

**Class/Static Methods:** 

 - [`andList`](#andList)
 - [`assertInternetConnected`](#assertInternetConnected)
 - [`assignRegistryEntryVar`](#assignRegistryEntryVar)
 - [`boolToString`](#boolToString)
 - [`cmdLineArg`](#cmdLineArg)
 - [`cmdLineListArg`](#cmdLineListArg)
 - [`cmdLineSwitchArg`](#cmdLineSwitchArg)
 - [`debugPopup`](#debugPopup)
 - [`deleteDetachedOpDataFile`](#deleteDetachedOpDataFile)
 - [`deleteFile`](#deleteFile)
 - [`deleteOpDataFile`](#deleteOpDataFile)
 - [`disableQuit`](#disableQuit)
 - [`disableQuitPrompt`](#disableQuitPrompt)
 - [`dropElevation`](#dropElevation)
 - [`elevate`](#elevate)
 - [`embedResources`](#embedResources)
 - [`enableComponent`](#enableComponent)
 - [`errorPopup`](#errorPopup)
 - [`genResources`](#genResources)
 - [`getComponent`](#getComponent)
 - [`getEnv`](#getEnv)
 - [`getPageOwner`](#getPageOwner)
 - [`ifAutoPilot`](#ifAutoPilot)
 - [`ifBoolValue`](#ifBoolValue)
 - [`ifCmdLineArg`](#ifCmdLineArg)
 - [`ifCmdLineSwitch`](#ifCmdLineSwitch)
 - [`ifComponentEnabled`](#ifComponentEnabled)
 - [`ifComponentInstalled`](#ifComponentInstalled)
 - [`ifComponentSelected`](#ifComponentSelected)
 - [`ifCondition`](#ifCondition)
 - [`ifDryRun`](#ifDryRun)
 - [`ifElevated`](#ifElevated)
 - [`ifInstalling`](#ifInstalling)
 - [`ifInternetConnected`](#ifInternetConnected)
 - [`ifMaintenanceTool`](#ifMaintenanceTool)
 - [`ifPathExists`](#ifPathExists)
 - [`ifPingable`](#ifPingable)
 - [`ifRegistryEntryExists`](#ifRegistryEntryExists)
 - [`ifRegistryEntryExistsLike`](#ifRegistryEntryExistsLike)
 - [`ifRegistryKeyExists`](#ifRegistryKeyExists)
 - [`ifRegistryKeyExistsLike`](#ifRegistryKeyExistsLike)
 - [`ifValueDefined`](#ifValueDefined)
 - [`ifYesNoPopup`](#ifYesNoPopup)
 - [`isAutoPilot`](#isAutoPilot)
 - [`isComponentEnabled`](#isComponentEnabled)
 - [`isComponentInstalled`](#isComponentInstalled)
 - [`isComponentSelected`](#isComponentSelected)
 - [`isDryRun`](#isDryRun)
 - [`isElevated`](#isElevated)
 - [`isInstalling`](#isInstalling)
 - [`isInternetConnected`](#isInternetConnected)
 - [`isMaintenanceTool`](#isMaintenanceTool)
 - [`isPingable`](#isPingable)
 - [`killAll`](#killAll)
 - [`log`](#log)
 - [`logSwitch`](#logSwitch)
 - [`logValue`](#logValue)
 - [`lookupBoolValue`](#lookupBoolValue)
 - [`lookupValue`](#lookupValue)
 - [`lookupValueList`](#lookupValueList)
 - [`makeDir`](#makeDir)
 - [`orList`](#orList)
 - [`pathExists`](#pathExists)
 - [`productName`](#productName)
 - [`quit`](#quit)
 - [`quote`](#quote)
 - [`registryEntryExists`](#registryEntryExists)
 - [`registryEntryExistsLike`](#registryEntryExistsLike)
 - [`registryEntryValue`](#registryEntryValue)
 - [`registryKeyExists`](#registryKeyExists)
 - [`registryKeyExistsLike`](#registryKeyExistsLike)
 - [`removeDir`](#removeDir)
 - [`resolveDynamTxtVarsOperations`](#resolveDynamTxtVarsOperations)
 - [`resolveDynamicVars`](#resolveDynamicVars)
 - [`resolveScriptVars`](#resolveScriptVars)
 - [`resolveScriptVarsOperations`](#resolveScriptVarsOperations)
 - [`setBoolValue`](#setBoolValue)
 - [`setValue`](#setValue)
 - [`setValueFromRegistryEntry`](#setValueFromRegistryEntry)
 - [`startMenuDir`](#startMenuDir)
 - [`stringToBool`](#stringToBool)
 - [`switchYesNoCancelPopup`](#switchYesNoCancelPopup)
 - [`targetDir`](#targetDir)
 - [`toBool`](#toBool)
 - [`toNull`](#toNull)
 - [`warningPopup`](#warningPopup)
 - [`writeDetachedOpDataFile`](#writeDetachedOpDataFile)
 - [`writeFile`](#writeFile)
 - [`writeOpDataFile`](#writeOpDataFile)
 - [`yesNoCancelPopup`](#yesNoCancelPopup)
 - [`yesNoPopup`](#yesNoPopup)

**Class/Static Attributes:** 

 - [`ABORT`](#ABORT)
 - [`ACCEPT_EULA_CMD_ARG`](#ACCEPT_EULA_CMD_ARG)
 - [`AND`](#AND)
 - [`ASSIGN`](#ASSIGN)
 - [`AUTH_ERROR_MSGBOX_ID`](#AUTH_ERROR_MSGBOX_ID)
 - [`AUTO_PILOT_CMD_ARG`](#AUTO_PILOT_CMD_ARG)
 - [`CANCEL`](#CANCEL)
 - [`CATCH`](#CATCH)
 - [`CONCAT`](#CONCAT)
 - [`DEFAULT_TARGET_DIR_KEY`](#DEFAULT_TARGET_DIR_KEY)
 - [`DRYRUN_CMD_ARG`](#DRYRUN_CMD_ARG)
 - [`ELSE`](#ELSE)
 - [`END_BLOCK`](#END_BLOCK)
 - [`END_LINE`](#END_LINE)
 - [`EQUAL_TO`](#EQUAL_TO)
 - [`ERR_LOG_DEFAULT_PATH`](#ERR_LOG_DEFAULT_PATH)
 - [`ERR_LOG_PATH_CMD_ARG`](#ERR_LOG_PATH_CMD_ARG)
 - [`EXCLUDE_LIST_CMD_ARG`](#EXCLUDE_LIST_CMD_ARG)
 - [`EXIT_FUNCTION`](#EXIT_FUNCTION)
 - [`FALSE`](#FALSE)
 - [`IF`](#IF)
 - [`INCLUDE_LIST_CMD_ARG`](#INCLUDE_LIST_CMD_ARG)
 - [`INSTALL_LIST_CMD_ARG`](#INSTALL_LIST_CMD_ARG)
 - [`INTERUPTED_KEY`](#INTERUPTED_KEY)
 - [`IS_NET_CONNECTED_KEY`](#IS_NET_CONNECTED_KEY)
 - [`MAINTAIN_MODE_CMD_ARG`](#MAINTAIN_MODE_CMD_ARG)
 - [`MAINTAIN_MODE_OPT_ADD_REMOVE`](#MAINTAIN_MODE_OPT_ADD_REMOVE)
 - [`MAINTAIN_MODE_OPT_REMOVE_ALL`](#MAINTAIN_MODE_OPT_REMOVE_ALL)
 - [`MAINTAIN_MODE_OPT_UPDATE`](#MAINTAIN_MODE_OPT_UPDATE)
 - [`MAINTAIN_PASSTHRU_CMD_ARG`](#MAINTAIN_PASSTHRU_CMD_ARG)
 - [`MAINTENANCE_TOOL_NAME`](#MAINTENANCE_TOOL_NAME)
 - [`NEW_LINE`](#NEW_LINE)
 - [`NO`](#NO)
 - [`NOT`](#NOT)
 - [`NOT_EQUAL_TO`](#NOT_EQUAL_TO)
 - [`NULL`](#NULL)
 - [`OK`](#OK)
 - [`OR`](#OR)
 - [`OUT_LOG_DEFAULT_PATH`](#OUT_LOG_DEFAULT_PATH)
 - [`OUT_LOG_PATH_CMD_ARG`](#OUT_LOG_PATH_CMD_ARG)
 - [`PATH_SEP`](#PATH_SEP)
 - [`PRODUCT_NAME_KEY`](#PRODUCT_NAME_KEY)
 - [`QUIT_MSGBOX_ID`](#QUIT_MSGBOX_ID)
 - [`REBOOT_CMD_ARG`](#REBOOT_CMD_ARG)
 - [`RESTORE_MSGBOX_DEFAULT`](#RESTORE_MSGBOX_DEFAULT)
 - [`RUN_PROGRAM_CMD_ARG`](#RUN_PROGRAM_CMD_ARG)
 - [`STARTMENU_DIR_KEY`](#STARTMENU_DIR_KEY)
 - [`START_BLOCK`](#START_BLOCK)
 - [`START_MENU_DIR_CMD_ARG`](#START_MENU_DIR_CMD_ARG)
 - [`TAB`](#TAB)
 - [`TARGET_DIR_CMD_ARG`](#TARGET_DIR_CMD_ARG)
 - [`TARGET_DIR_KEY`](#TARGET_DIR_KEY)
 - [`TARGET_EXISTS_OPT_CMD_ARG`](#TARGET_EXISTS_OPT_CMD_ARG)
 - [`TARGET_EXISTS_OPT_FAIL`](#TARGET_EXISTS_OPT_FAIL)
 - [`TARGET_EXISTS_OPT_PROMPT`](#TARGET_EXISTS_OPT_PROMPT)
 - [`TARGET_EXISTS_OPT_REMOVE`](#TARGET_EXISTS_OPT_REMOVE)
 - [`TRUE`](#TRUE)
 - [`TRY`](#TRY)
 - [`USER_KEY`](#USER_KEY)
 - [`VERBOSE_CMD_SWITCH_ARG`](#VERBOSE_CMD_SWITCH_ARG)
 - [`YES`](#YES)

### **QtIfwPackageScript**`#!py3 (pkgName, pkgVersion, pkgSubDirName=None, shortcuts=None, bundledScripts=None, dynamicTexts=None, externalOps=None, installResources=None, uiPages=None, widgets=None, fileName='installscript.qs', script=None, scriptPath=None)` { #QtIfwPackageScript-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**addSimpleOperation**`#!py3 (self, name, parms=None, isElevated=False, isAutoQuote=True)` { #addSimpleOperation data-toc-label=addSimpleOperation }


### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**dirPath**`#!py3 (self)` { #dirPath data-toc-label=dirPath }

PURE VIRTUAL
### *obj*.**exists**`#!py3 (self)` { #exists data-toc-label=exists }


### *obj*.**path**`#!py3 (self)` { #path data-toc-label=path }

PURE VIRTUAL
### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**pkgName** *class 'NoneType'* default: *None* { #pkgName data-toc-label=pkgName }


### *obj*.**pkgVersion** *class 'NoneType'* default: *None* { #pkgVersion data-toc-label=pkgVersion }


### *obj*.**pkgSubDirName** *class 'NoneType'* default: *None* { #pkgSubDirName data-toc-label=pkgSubDirName }


### *obj*.**shortcuts** *class 'list'* default: *[]* { #shortcuts data-toc-label=shortcuts }


### *obj*.**externalOps** *class 'list'* default: *[]* { #externalOps data-toc-label=externalOps }


### *obj*.**killOps** *class 'list'* default: *[]* { #killOps data-toc-label=killOps }


### *obj*.**preOpSupport** *class 'NoneType'* default: *None* { #preOpSupport data-toc-label=preOpSupport }


### *obj*.**customOperations** *class 'NoneType'* default: *None* { #customOperations data-toc-label=customOperations }


### *obj*.**bundledScripts** *class 'list'* default: *[]* { #bundledScripts data-toc-label=bundledScripts }


### *obj*.**dynamicTexts** *class 'dict'* default: *{}* { #dynamicTexts data-toc-label=dynamicTexts }


### *obj*.**installResources** *class 'list'* default: *[]* { #installResources data-toc-label=installResources }


### *obj*.**externalDependencies** *class 'list'* default: *[]* { #externalDependencies data-toc-label=externalDependencies }


### *obj*.**areDependenciesPreserved** *class 'bool'* default: *True* { #areDependenciesPreserved data-toc-label=areDependenciesPreserved }


### *obj*.**uiPages** *class 'list'* default: *[]* { #uiPages data-toc-label=uiPages }


### *obj*.**widgets** *class 'list'* default: *[]* { #widgets data-toc-label=widgets }


### *obj*.**packageGlobals** *class 'NoneType'* default: *None* { #packageGlobals data-toc-label=packageGlobals }


### *obj*.**isAutoGlobals** *class 'bool'* default: *True* { #isAutoGlobals data-toc-label=isAutoGlobals }


### *obj*.**componentConstructorBody** *class 'NoneType'* default: *None* { #componentConstructorBody data-toc-label=componentConstructorBody }


### *obj*.**isAutoComponentConstructor** *class 'bool'* default: *True* { #isAutoComponentConstructor data-toc-label=isAutoComponentConstructor }


### *obj*.**componentLoadedCallbackBody** *class 'NoneType'* default: *None* { #componentLoadedCallbackBody data-toc-label=componentLoadedCallbackBody }


### *obj*.**isAutoComponentLoadedCallback** *class 'bool'* default: *True* { #isAutoComponentLoadedCallback data-toc-label=isAutoComponentLoadedCallback }


### *obj*.**componentEnteredCallbackBody** *class 'NoneType'* default: *None* { #componentEnteredCallbackBody data-toc-label=componentEnteredCallbackBody }


### *obj*.**isAutoComponentEnteredCallback** *class 'bool'* default: *True* { #isAutoComponentEnteredCallback data-toc-label=isAutoComponentEnteredCallback }


### *obj*.**componentCreateOperationsBody** *class 'NoneType'* default: *None* { #componentCreateOperationsBody data-toc-label=componentCreateOperationsBody }


### *obj*.**isAutoComponentCreateOperations** *class 'bool'* default: *True* { #isAutoComponentCreateOperations data-toc-label=isAutoComponentCreateOperations }


### *obj*.**componentCreateOperationsForArchiveBody** *class 'NoneType'* default: *None* { #componentCreateOperationsForArchiveBody data-toc-label=componentCreateOperationsForArchiveBody }


### *obj*.**isAutoComponentCreateOperationsForArchive** *class 'bool'* default: *True* { #isAutoComponentCreateOperationsForArchive data-toc-label=isAutoComponentCreateOperationsForArchive }


### *QtIfwPackageScript*.**andList**`#!py3 (conditions)` { #andList data-toc-label=andList }


### *QtIfwPackageScript*.**assertInternetConnected**`#!py3 (isRefresh=False, errMsg=None, isAutoQuote=True)` { #assertInternetConnected data-toc-label=assertInternetConnected }


### *QtIfwPackageScript*.**assignRegistryEntryVar**`#!py3 (key, valueName, isAutoBitContext=True, varName='regValue', isAutoQuote=True)` { #assignRegistryEntryVar data-toc-label=assignRegistryEntryVar }


### *QtIfwPackageScript*.**boolToString**`#!py3 (b)` { #boolToString data-toc-label=boolToString }


### *QtIfwPackageScript*.**cmdLineArg**`#!py3 (arg, default='')` { #cmdLineArg data-toc-label=cmdLineArg }


### *QtIfwPackageScript*.**cmdLineListArg**`#!py3 (arg, default=None)` { #cmdLineListArg data-toc-label=cmdLineListArg }


### *QtIfwPackageScript*.**cmdLineSwitchArg**`#!py3 (arg, isNegated=False, isHardFalse=False)` { #cmdLineSwitchArg data-toc-label=cmdLineSwitchArg }


### *QtIfwPackageScript*.**debugPopup**`#!py3 (msg, isAutoQuote=True)` { #debugPopup data-toc-label=debugPopup }


### *QtIfwPackageScript*.**deleteDetachedOpDataFile**`#!py3 (fileName)` { #deleteDetachedOpDataFile data-toc-label=deleteDetachedOpDataFile }


### *QtIfwPackageScript*.**deleteFile**`#!py3 (path, isAutoQuote=True)` { #deleteFile data-toc-label=deleteFile }


### *QtIfwPackageScript*.**deleteOpDataFile**`#!py3 (fileName)` { #deleteOpDataFile data-toc-label=deleteOpDataFile }


### *QtIfwPackageScript*.**disableQuit**`#!py3 ()` { #disableQuit data-toc-label=disableQuit }


### *QtIfwPackageScript*.**disableQuitPrompt**`#!py3 ()` { #disableQuitPrompt data-toc-label=disableQuitPrompt }


### *QtIfwPackageScript*.**dropElevation**`#!py3 ()` { #dropElevation data-toc-label=dropElevation }


### *QtIfwPackageScript*.**elevate**`#!py3 ()` { #elevate data-toc-label=elevate }


### *QtIfwPackageScript*.**embedResources**`#!py3 (embeddedResources)` { #embedResources data-toc-label=embedResources }


### *QtIfwPackageScript*.**enableComponent**`#!py3 (package, enable=True, isAutoQuote=True)` { #enableComponent data-toc-label=enableComponent }


### *QtIfwPackageScript*.**errorPopup**`#!py3 (msg, isAutoQuote=True)` { #errorPopup data-toc-label=errorPopup }


### *QtIfwPackageScript*.**genResources**`#!py3 (embeddedResources, isTempRootTarget=False)` { #genResources data-toc-label=genResources }


### *QtIfwPackageScript*.**getComponent**`#!py3 (name, isAutoQuote=True)` { #getComponent data-toc-label=getComponent }


### *QtIfwPackageScript*.**getEnv**`#!py3 (varName, isAutoQuote=True)` { #getEnv data-toc-label=getEnv }


### *QtIfwPackageScript*.**getPageOwner**`#!py3 (pageName, isAutoQuote=True)` { #getPageOwner data-toc-label=getPageOwner }


### *QtIfwPackageScript*.**ifAutoPilot**`#!py3 (isNegated=False, isMultiLine=False)` { #ifAutoPilot data-toc-label=ifAutoPilot }


### *QtIfwPackageScript*.**ifBoolValue**`#!py3 (key, isNegated=False, isHardFalse=False, isMultiLine=False)` { #ifBoolValue data-toc-label=ifBoolValue }


### *QtIfwPackageScript*.**ifCmdLineArg**`#!py3 (arg, isNegated=False, isMultiLine=False)` { #ifCmdLineArg data-toc-label=ifCmdLineArg }


### *QtIfwPackageScript*.**ifCmdLineSwitch**`#!py3 (arg, isNegated=False, isHardFalse=False, isMultiLine=False)` { #ifCmdLineSwitch data-toc-label=ifCmdLineSwitch }


### *QtIfwPackageScript*.**ifComponentEnabled**`#!py3 (package, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifComponentEnabled data-toc-label=ifComponentEnabled }


### *QtIfwPackageScript*.**ifComponentInstalled**`#!py3 (package, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifComponentInstalled data-toc-label=ifComponentInstalled }


### *QtIfwPackageScript*.**ifComponentSelected**`#!py3 (package, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifComponentSelected data-toc-label=ifComponentSelected }


### *QtIfwPackageScript*.**ifCondition**`#!py3 (condition, isNegated=False, isMultiLine=False)` { #ifCondition data-toc-label=ifCondition }


### *QtIfwPackageScript*.**ifDryRun**`#!py3 (isNegated=False, isMultiLine=False)` { #ifDryRun data-toc-label=ifDryRun }


### *QtIfwPackageScript*.**ifElevated**`#!py3 (isNegated=False, isMultiLine=False)` { #ifElevated data-toc-label=ifElevated }


### *QtIfwPackageScript*.**ifInstalling**`#!py3 (isNegated=False, isMultiLine=False)` { #ifInstalling data-toc-label=ifInstalling }


### *QtIfwPackageScript*.**ifInternetConnected**`#!py3 (isRefresh=False, isNegated=False, isMultiLine=False)` { #ifInternetConnected data-toc-label=ifInternetConnected }


### *QtIfwPackageScript*.**ifMaintenanceTool**`#!py3 (isNegated=False, isMultiLine=False)` { #ifMaintenanceTool data-toc-label=ifMaintenanceTool }


### *QtIfwPackageScript*.**ifPathExists**`#!py3 (path, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifPathExists data-toc-label=ifPathExists }


### *QtIfwPackageScript*.**ifPingable**`#!py3 (uri, pings=3, totalMaxSecs=12, isAutoQuote=True, isNegated=False, isMultiLine=False)` { #ifPingable data-toc-label=ifPingable }


### *QtIfwPackageScript*.**ifRegistryEntryExists**`#!py3 (key, valueName, isAutoBitContext=True, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryEntryExists data-toc-label=ifRegistryEntryExists }


### *QtIfwPackageScript*.**ifRegistryEntryExistsLike**`#!py3 (key, valueNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryEntryExistsLike data-toc-label=ifRegistryEntryExistsLike }


### *QtIfwPackageScript*.**ifRegistryKeyExists**`#!py3 (key, isAutoBitContext=True, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryKeyExists data-toc-label=ifRegistryKeyExists }


### *QtIfwPackageScript*.**ifRegistryKeyExistsLike**`#!py3 (parentKey, childKeyNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isNegated=False, isAutoQuote=True, isMultiLine=False)` { #ifRegistryKeyExistsLike data-toc-label=ifRegistryKeyExistsLike }


### *QtIfwPackageScript*.**ifValueDefined**`#!py3 (key, isNegated=False, isMultiLine=False)` { #ifValueDefined data-toc-label=ifValueDefined }


### *QtIfwPackageScript*.**ifYesNoPopup**`#!py3 (msg, title='Question', resultVar='result', isMultiLine=False)` { #ifYesNoPopup data-toc-label=ifYesNoPopup }


### *QtIfwPackageScript*.**isAutoPilot**`#!py3 (isNegated=False)` { #isAutoPilot data-toc-label=isAutoPilot }


### *QtIfwPackageScript*.**isComponentEnabled**`#!py3 (package, isAutoQuote=True)` { #isComponentEnabled data-toc-label=isComponentEnabled }


### *QtIfwPackageScript*.**isComponentInstalled**`#!py3 (package, isAutoQuote=True)` { #isComponentInstalled data-toc-label=isComponentInstalled }


### *QtIfwPackageScript*.**isComponentSelected**`#!py3 (package, isAutoQuote=True)` { #isComponentSelected data-toc-label=isComponentSelected }


### *QtIfwPackageScript*.**isDryRun**`#!py3 (isNegated=False)` { #isDryRun data-toc-label=isDryRun }


### *QtIfwPackageScript*.**isElevated**`#!py3 ()` { #isElevated data-toc-label=isElevated }


### *QtIfwPackageScript*.**isInstalling**`#!py3 (isNegated=False)` { #isInstalling data-toc-label=isInstalling }


### *QtIfwPackageScript*.**isInternetConnected**`#!py3 (isRefresh=False)` { #isInternetConnected data-toc-label=isInternetConnected }


### *QtIfwPackageScript*.**isMaintenanceTool**`#!py3 (isNegated=False)` { #isMaintenanceTool data-toc-label=isMaintenanceTool }


### *QtIfwPackageScript*.**isPingable**`#!py3 (uri, pings=3, totalMaxSecs=12, isAutoQuote=True)` { #isPingable data-toc-label=isPingable }


### *QtIfwPackageScript*.**killAll**`#!py3 (exeName, isAutoQuote=True)` { #killAll data-toc-label=killAll }


### *QtIfwPackageScript*.**log**`#!py3 (msg, isAutoQuote=True)` { #log data-toc-label=log }


### *QtIfwPackageScript*.**logSwitch**`#!py3 (key)` { #logSwitch data-toc-label=logSwitch }


### *QtIfwPackageScript*.**logValue**`#!py3 (key, defaultVal='')` { #logValue data-toc-label=logValue }


### *QtIfwPackageScript*.**lookupBoolValue**`#!py3 (key, isNegated=False, isHardFalse=False, isAutoQuote=True)` { #lookupBoolValue data-toc-label=lookupBoolValue }


### *QtIfwPackageScript*.**lookupValue**`#!py3 (key, default='', isAutoQuote=True)` { #lookupValue data-toc-label=lookupValue }


### *QtIfwPackageScript*.**lookupValueList**`#!py3 (key, defaultList=None, isAutoQuote=True, delimiter=None)` { #lookupValueList data-toc-label=lookupValueList }


### *QtIfwPackageScript*.**makeDir**`#!py3 (path, isAutoQuote=True)` { #makeDir data-toc-label=makeDir }


### *QtIfwPackageScript*.**orList**`#!py3 (conditions)` { #orList data-toc-label=orList }


### *QtIfwPackageScript*.**pathExists**`#!py3 (path, isNegated=False, isAutoQuote=True)` { #pathExists data-toc-label=pathExists }


### *QtIfwPackageScript*.**productName**`#!py3 ()` { #productName data-toc-label=productName }


### *QtIfwPackageScript*.**quit**`#!py3 (msg, isError=True, isSilent=False, isAutoQuote=True)` { #quit data-toc-label=quit }


### *QtIfwPackageScript*.**quote**`#!py3 (value)` { #quote data-toc-label=quote }


### *QtIfwPackageScript*.**registryEntryExists**`#!py3 (key, valueName, isAutoBitContext=True, isAutoQuote=True)` { #registryEntryExists data-toc-label=registryEntryExists }


### *QtIfwPackageScript*.**registryEntryExistsLike**`#!py3 (key, valueNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isAutoQuote=True)` { #registryEntryExistsLike data-toc-label=registryEntryExistsLike }


### *QtIfwPackageScript*.**registryEntryValue**`#!py3 (key, valueName, isAutoBitContext=True, isAutoQuote=True)` { #registryEntryValue data-toc-label=registryEntryValue }


### *QtIfwPackageScript*.**registryKeyExists**`#!py3 (key, isAutoBitContext=True, isAutoQuote=True)` { #registryKeyExists data-toc-label=registryKeyExists }


### *QtIfwPackageScript*.**registryKeyExistsLike**`#!py3 (parentKey, childKeyNameContains, isAutoBitContext=True, isCaseSensitive=False, isRecursive=False, isAutoQuote=True)` { #registryKeyExistsLike data-toc-label=registryKeyExistsLike }


### *QtIfwPackageScript*.**removeDir**`#!py3 (path, isAutoQuote=True)` { #removeDir data-toc-label=removeDir }


### *QtIfwPackageScript*.**resolveDynamTxtVarsOperations**`#!py3 (plasticFile, destPath)` { #resolveDynamTxtVarsOperations data-toc-label=resolveDynamTxtVarsOperations }


### *QtIfwPackageScript*.**resolveDynamicVars**`#!py3 (s, varNames=None, isAutoQuote=True)` { #resolveDynamicVars data-toc-label=resolveDynamicVars }


### *QtIfwPackageScript*.**resolveScriptVars**`#!py3 (scripts, subDir)` { #resolveScriptVars data-toc-label=resolveScriptVars }


### *QtIfwPackageScript*.**resolveScriptVarsOperations**`#!py3 (scripts, subDir)` { #resolveScriptVarsOperations data-toc-label=resolveScriptVarsOperations }


### *QtIfwPackageScript*.**setBoolValue**`#!py3 (key, b, isAutoQuote=True)` { #setBoolValue data-toc-label=setBoolValue }


### *QtIfwPackageScript*.**setValue**`#!py3 (key, value, isAutoQuote=True)` { #setValue data-toc-label=setValue }


### *QtIfwPackageScript*.**setValueFromRegistryEntry**`#!py3 (key, regKey, valueName, isAutoBitContext=True, isAutoQuote=True)` { #setValueFromRegistryEntry data-toc-label=setValueFromRegistryEntry }


### *QtIfwPackageScript*.**startMenuDir**`#!py3 ()` { #startMenuDir data-toc-label=startMenuDir }


### *QtIfwPackageScript*.**stringToBool**`#!py3 (value, isAutoQuote=True)` { #stringToBool data-toc-label=stringToBool }


### *QtIfwPackageScript*.**switchYesNoCancelPopup**`#!py3 (msg, title='Question', resultVar='result', onYes='', onNo='', onCancel='')` { #switchYesNoCancelPopup data-toc-label=switchYesNoCancelPopup }


### *QtIfwPackageScript*.**targetDir**`#!py3 ()` { #targetDir data-toc-label=targetDir }


### *QtIfwPackageScript*.**toBool**`#!py3 (b)` { #toBool data-toc-label=toBool }


### *QtIfwPackageScript*.**toNull**`#!py3 (v)` { #toNull data-toc-label=toNull }


### *QtIfwPackageScript*.**warningPopup**`#!py3 (msg, isAutoQuote=True)` { #warningPopup data-toc-label=warningPopup }


### *QtIfwPackageScript*.**writeDetachedOpDataFile**`#!py3 (fileName, content='', isAutoQuote=True)` { #writeDetachedOpDataFile data-toc-label=writeDetachedOpDataFile }


### *QtIfwPackageScript*.**writeFile**`#!py3 (path, content, isAutoQuote=True)` { #writeFile data-toc-label=writeFile }


### *QtIfwPackageScript*.**writeOpDataFile**`#!py3 (fileName, content='', isAutoQuote=True)` { #writeOpDataFile data-toc-label=writeOpDataFile }


### *QtIfwPackageScript*.**yesNoCancelPopup**`#!py3 (msg, title='Question', resultVar='result')` { #yesNoCancelPopup data-toc-label=yesNoCancelPopup }


### *QtIfwPackageScript*.**yesNoPopup**`#!py3 (msg, title='Question', resultVar='result')` { #yesNoPopup data-toc-label=yesNoPopup }


### *QtIfwPackageScript*.**ABORT** *class 'str'* default: *"QMessageBox.Abort"* { #ABORT data-toc-label=ABORT }


### *QtIfwPackageScript*.**ACCEPT_EULA_CMD_ARG** *class 'str'* default: *"accept"* { #ACCEPT_EULA_CMD_ARG data-toc-label=ACCEPT_EULA_CMD_ARG }


### *QtIfwPackageScript*.**AND** *class 'str'* default: *" && "* { #AND data-toc-label=AND }


### *QtIfwPackageScript*.**ASSIGN** *class 'str'* default: *"="* { #ASSIGN data-toc-label=ASSIGN }


### *QtIfwPackageScript*.**AUTH_ERROR_MSGBOX_ID** *class 'str'* default: *"AuthorizationError"* { #AUTH_ERROR_MSGBOX_ID data-toc-label=AUTH_ERROR_MSGBOX_ID }


### *QtIfwPackageScript*.**AUTO_PILOT_CMD_ARG** *class 'str'* default: *"auto"* { #AUTO_PILOT_CMD_ARG data-toc-label=AUTO_PILOT_CMD_ARG }


### *QtIfwPackageScript*.**CANCEL** *class 'str'* default: *"QMessageBox.Cancel"* { #CANCEL data-toc-label=CANCEL }


### *QtIfwPackageScript*.**CATCH** *class 'str'* default: *"catch(e) { "* { #CATCH data-toc-label=CATCH }


### *QtIfwPackageScript*.**CONCAT** *class 'str'* default: *" + "* { #CONCAT data-toc-label=CONCAT }


### *QtIfwPackageScript*.**DEFAULT_TARGET_DIR_KEY** *class 'str'* default: *"DefaultTargetDir"* { #DEFAULT_TARGET_DIR_KEY data-toc-label=DEFAULT_TARGET_DIR_KEY }


### *QtIfwPackageScript*.**DRYRUN_CMD_ARG** *class 'str'* default: *"dryrun"* { #DRYRUN_CMD_ARG data-toc-label=DRYRUN_CMD_ARG }


### *QtIfwPackageScript*.**ELSE** *class 'str'* default: *"else "* { #ELSE data-toc-label=ELSE }


### *QtIfwPackageScript*.**END_BLOCK** *class 'str'* default: *"}
"* { #END_BLOCK data-toc-label=END_BLOCK }


### *QtIfwPackageScript*.**END_LINE** *class 'str'* default: *";
"* { #END_LINE data-toc-label=END_LINE }


### *QtIfwPackageScript*.**EQUAL_TO** *class 'str'* default: *" == "* { #EQUAL_TO data-toc-label=EQUAL_TO }


### *QtIfwPackageScript*.**ERR_LOG_DEFAULT_PATH** *class 'str'* default: *"%temp%\\installer.err"* { #ERR_LOG_DEFAULT_PATH data-toc-label=ERR_LOG_DEFAULT_PATH }


### *QtIfwPackageScript*.**ERR_LOG_PATH_CMD_ARG** *class 'str'* default: *"errlog"* { #ERR_LOG_PATH_CMD_ARG data-toc-label=ERR_LOG_PATH_CMD_ARG }


### *QtIfwPackageScript*.**EXCLUDE_LIST_CMD_ARG** *class 'str'* default: *"exclude"* { #EXCLUDE_LIST_CMD_ARG data-toc-label=EXCLUDE_LIST_CMD_ARG }


### *QtIfwPackageScript*.**EXIT_FUNCTION** *class 'str'* default: *"
return;
"* { #EXIT_FUNCTION data-toc-label=EXIT_FUNCTION }


### *QtIfwPackageScript*.**FALSE** *class 'str'* default: *"false"* { #FALSE data-toc-label=FALSE }


### *QtIfwPackageScript*.**IF** *class 'str'* default: *"if "* { #IF data-toc-label=IF }


### *QtIfwPackageScript*.**INCLUDE_LIST_CMD_ARG** *class 'str'* default: *"include"* { #INCLUDE_LIST_CMD_ARG data-toc-label=INCLUDE_LIST_CMD_ARG }


### *QtIfwPackageScript*.**INSTALL_LIST_CMD_ARG** *class 'str'* default: *"install"* { #INSTALL_LIST_CMD_ARG data-toc-label=INSTALL_LIST_CMD_ARG }


### *QtIfwPackageScript*.**INTERUPTED_KEY** *class 'str'* default: *"isInterupted"* { #INTERUPTED_KEY data-toc-label=INTERUPTED_KEY }


### *QtIfwPackageScript*.**IS_NET_CONNECTED_KEY** *class 'str'* default: *"isNetConnected"* { #IS_NET_CONNECTED_KEY data-toc-label=IS_NET_CONNECTED_KEY }


### *QtIfwPackageScript*.**MAINTAIN_MODE_CMD_ARG** *class 'str'* default: *"mode"* { #MAINTAIN_MODE_CMD_ARG data-toc-label=MAINTAIN_MODE_CMD_ARG }


### *QtIfwPackageScript*.**MAINTAIN_MODE_OPT_ADD_REMOVE** *class 'str'* default: *"addremove"* { #MAINTAIN_MODE_OPT_ADD_REMOVE data-toc-label=MAINTAIN_MODE_OPT_ADD_REMOVE }


### *QtIfwPackageScript*.**MAINTAIN_MODE_OPT_REMOVE_ALL** *class 'str'* default: *"removeall"* { #MAINTAIN_MODE_OPT_REMOVE_ALL data-toc-label=MAINTAIN_MODE_OPT_REMOVE_ALL }


### *QtIfwPackageScript*.**MAINTAIN_MODE_OPT_UPDATE** *class 'str'* default: *"update"* { #MAINTAIN_MODE_OPT_UPDATE data-toc-label=MAINTAIN_MODE_OPT_UPDATE }


### *QtIfwPackageScript*.**MAINTAIN_PASSTHRU_CMD_ARG** *class 'str'* default: *"maintpassthru"* { #MAINTAIN_PASSTHRU_CMD_ARG data-toc-label=MAINTAIN_PASSTHRU_CMD_ARG }


### *QtIfwPackageScript*.**MAINTENANCE_TOOL_NAME** *class 'str'* default: *"maintenancetool.exe"* { #MAINTENANCE_TOOL_NAME data-toc-label=MAINTENANCE_TOOL_NAME }


### *QtIfwPackageScript*.**NEW_LINE** *class 'str'* default: *"
"* { #NEW_LINE data-toc-label=NEW_LINE }


### *QtIfwPackageScript*.**NO** *class 'str'* default: *"QMessageBox.No"* { #NO data-toc-label=NO }


### *QtIfwPackageScript*.**NOT** *class 'str'* default: *"! "* { #NOT data-toc-label=NOT }


### *QtIfwPackageScript*.**NOT_EQUAL_TO** *class 'str'* default: *" != "* { #NOT_EQUAL_TO data-toc-label=NOT_EQUAL_TO }


### *QtIfwPackageScript*.**NULL** *class 'str'* default: *"null"* { #NULL data-toc-label=NULL }


### *QtIfwPackageScript*.**OK** *class 'str'* default: *"QMessageBox.Yes"* { #OK data-toc-label=OK }


### *QtIfwPackageScript*.**OR** *class 'str'* default: *" || "* { #OR data-toc-label=OR }


### *QtIfwPackageScript*.**OUT_LOG_DEFAULT_PATH** *class 'str'* default: *"%temp%\\installer.out"* { #OUT_LOG_DEFAULT_PATH data-toc-label=OUT_LOG_DEFAULT_PATH }


### *QtIfwPackageScript*.**OUT_LOG_PATH_CMD_ARG** *class 'str'* default: *"outlog"* { #OUT_LOG_PATH_CMD_ARG data-toc-label=OUT_LOG_PATH_CMD_ARG }


### *QtIfwPackageScript*.**PATH_SEP** *class 'str'* default: *""\\""* { #PATH_SEP data-toc-label=PATH_SEP }


### *QtIfwPackageScript*.**PRODUCT_NAME_KEY** *class 'str'* default: *"ProductName"* { #PRODUCT_NAME_KEY data-toc-label=PRODUCT_NAME_KEY }


### *QtIfwPackageScript*.**QUIT_MSGBOX_ID** *class 'str'* default: *"cancelInstallation"* { #QUIT_MSGBOX_ID data-toc-label=QUIT_MSGBOX_ID }


### *QtIfwPackageScript*.**REBOOT_CMD_ARG** *class 'str'* default: *"reboot"* { #REBOOT_CMD_ARG data-toc-label=REBOOT_CMD_ARG }


### *QtIfwPackageScript*.**RESTORE_MSGBOX_DEFAULT** *class 'str'* default: *"QMessageBox.RestoreDefaults"* { #RESTORE_MSGBOX_DEFAULT data-toc-label=RESTORE_MSGBOX_DEFAULT }


### *QtIfwPackageScript*.**RUN_PROGRAM_CMD_ARG** *class 'str'* default: *"run"* { #RUN_PROGRAM_CMD_ARG data-toc-label=RUN_PROGRAM_CMD_ARG }


### *QtIfwPackageScript*.**STARTMENU_DIR_KEY** *class 'str'* default: *"StartMenuDir"* { #STARTMENU_DIR_KEY data-toc-label=STARTMENU_DIR_KEY }


### *QtIfwPackageScript*.**START_BLOCK** *class 'str'* default: *"{
"* { #START_BLOCK data-toc-label=START_BLOCK }


### *QtIfwPackageScript*.**START_MENU_DIR_CMD_ARG** *class 'str'* default: *"startmenu"* { #START_MENU_DIR_CMD_ARG data-toc-label=START_MENU_DIR_CMD_ARG }


### *QtIfwPackageScript*.**TAB** *class 'str'* default: *"    "* { #TAB data-toc-label=TAB }


### *QtIfwPackageScript*.**TARGET_DIR_CMD_ARG** *class 'str'* default: *"target"* { #TARGET_DIR_CMD_ARG data-toc-label=TARGET_DIR_CMD_ARG }


### *QtIfwPackageScript*.**TARGET_DIR_KEY** *class 'str'* default: *"TargetDir"* { #TARGET_DIR_KEY data-toc-label=TARGET_DIR_KEY }


### *QtIfwPackageScript*.**TARGET_EXISTS_OPT_CMD_ARG** *class 'str'* default: *"onexist"* { #TARGET_EXISTS_OPT_CMD_ARG data-toc-label=TARGET_EXISTS_OPT_CMD_ARG }


### *QtIfwPackageScript*.**TARGET_EXISTS_OPT_FAIL** *class 'str'* default: *"fail"* { #TARGET_EXISTS_OPT_FAIL data-toc-label=TARGET_EXISTS_OPT_FAIL }


### *QtIfwPackageScript*.**TARGET_EXISTS_OPT_PROMPT** *class 'str'* default: *"prompt"* { #TARGET_EXISTS_OPT_PROMPT data-toc-label=TARGET_EXISTS_OPT_PROMPT }


### *QtIfwPackageScript*.**TARGET_EXISTS_OPT_REMOVE** *class 'str'* default: *"remove"* { #TARGET_EXISTS_OPT_REMOVE data-toc-label=TARGET_EXISTS_OPT_REMOVE }


### *QtIfwPackageScript*.**TRUE** *class 'str'* default: *"true"* { #TRUE data-toc-label=TRUE }


### *QtIfwPackageScript*.**TRY** *class 'str'* default: *"try { "* { #TRY data-toc-label=TRY }


### *QtIfwPackageScript*.**USER_KEY** *class 'str'* default: *"User"* { #USER_KEY data-toc-label=USER_KEY }


### *QtIfwPackageScript*.**VERBOSE_CMD_SWITCH_ARG** *class 'str'* default: *"-v"* { #VERBOSE_CMD_SWITCH_ARG data-toc-label=VERBOSE_CMD_SWITCH_ARG }


### *QtIfwPackageScript*.**YES** *class 'str'* default: *"QMessageBox.Yes"* { #YES data-toc-label=YES }



______

## **QtIfwPackageXml**`#!py3 class` { #QtIfwPackageXml data-toc-label=QtIfwPackageXml }



**Base Classes:**

_QtIfwXml


**Magic Methods:**

 - [`__init__`](#QtIfwPackageXml-init)

**Instance Methods:** 

 - [`addCustomTags`](#addCustomTags)
 - [`debug`](#debug)
 - [`dirPath`](#dirPath)
 - [`exists`](#exists)
 - [`path`](#path)
 - [`toPrettyXml`](#toPrettyXml)
 - [`write`](#write)

**Instance Attributes:** 

 - [`pkgName`](#pkgName)
 - [`SortingPriority`](#SortingPriority)
 - [`DisplayName`](#DisplayName)
 - [`Description`](#Description)
 - [`Version`](#Version)
 - [`Script`](#Script)
 - [`ReleaseDate`](#ReleaseDate)
 - [`Virtual`](#Virtual)
 - [`Default`](#Default)
 - [`ForcedInstallation`](#ForcedInstallation)
 - [`Checkable`](#Checkable)
 - [`Dependencies`](#Dependencies)
 - [`AutoDependOn`](#AutoDependOn)
 - [`UserInterfaces`](#UserInterfaces)
 - [`Licenses`](#Licenses)

### **QtIfwPackageXml**`#!py3 (pkgName, displayName, description, version, scriptName=None, isDefault=True, isRequired=False, isHidden=False, isCheckable=True)` { #QtIfwPackageXml-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**addCustomTags**`#!py3 (self, root)` { #addCustomTags data-toc-label=addCustomTags }

VIRTUAL
### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**dirPath**`#!py3 (self)` { #dirPath data-toc-label=dirPath }

PURE VIRTUAL
### *obj*.**exists**`#!py3 (self)` { #exists data-toc-label=exists }


### *obj*.**path**`#!py3 (self)` { #path data-toc-label=path }

PURE VIRTUAL
### *obj*.**toPrettyXml**`#!py3 (self)` { #toPrettyXml data-toc-label=toPrettyXml }


### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**pkgName** *class 'NoneType'* default: *None* { #pkgName data-toc-label=pkgName }


### *obj*.**SortingPriority** *class 'NoneType'* default: *None* { #SortingPriority data-toc-label=SortingPriority }


### *obj*.**DisplayName** *class 'NoneType'* default: *None* { #DisplayName data-toc-label=DisplayName }


### *obj*.**Description** *class 'NoneType'* default: *None* { #Description data-toc-label=Description }


### *obj*.**Version** *class 'NoneType'* default: *None* { #Version data-toc-label=Version }


### *obj*.**Script** *class 'NoneType'* default: *None* { #Script data-toc-label=Script }


### *obj*.**ReleaseDate** *class 'datetime.date'* default: *2023-03-12* { #ReleaseDate data-toc-label=ReleaseDate }


### *obj*.**Virtual** *class 'NoneType'* default: *None* { #Virtual data-toc-label=Virtual }


### *obj*.**Default** *class 'NoneType'* default: *None* { #Default data-toc-label=Default }


### *obj*.**ForcedInstallation** *class 'NoneType'* default: *None* { #ForcedInstallation data-toc-label=ForcedInstallation }


### *obj*.**Checkable** *class 'bool'* default: *False* { #Checkable data-toc-label=Checkable }


### *obj*.**Dependencies** *class 'NoneType'* default: *None* { #Dependencies data-toc-label=Dependencies }


### *obj*.**AutoDependOn** *class 'NoneType'* default: *None* { #AutoDependOn data-toc-label=AutoDependOn }


### *obj*.**UserInterfaces** *class 'list'* default: *[]* { #UserInterfaces data-toc-label=UserInterfaces }


### *obj*.**Licenses** *class 'dict'* default: *{}* { #Licenses data-toc-label=Licenses }



______

## **QtIfwShortcut**`#!py3 class` { #QtIfwShortcut data-toc-label=QtIfwShortcut }



**Magic Methods:**

 - [`__init__`](#QtIfwShortcut-init)

**Instance Methods:** 


**Instance Attributes:** 

 - [`productName`](#productName)
 - [`command`](#command)
 - [`args`](#args)
 - [`exeDir`](#exeDir)
 - [`exeName`](#exeName)
 - [`isGui`](#isGui)
 - [`windowStyle`](#windowStyle)
 - [`isUserStartUpShortcut`](#isUserStartUpShortcut)
 - [`isAllUsersStartUpShortcut`](#isAllUsersStartUpShortcut)
 - [`exeVersion`](#exeVersion)
 - [`pngIconResPath`](#pngIconResPath)
 - [`isAppShortcut`](#isAppShortcut)
 - [`isDesktopShortcut`](#isDesktopShortcut)
 - [`isAdjancentShortcut`](#isAdjancentShortcut)

### **QtIfwShortcut**`#!py3 (productName='@ProductName@', command=None, args=None, exeDir='@TargetDir@', exeName=None, exeVersion='0.0.0.0', isGui=True, pngIconResPath=None)` { #QtIfwShortcut-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**productName** *class 'NoneType'* default: *None* { #productName data-toc-label=productName }


### *obj*.**command** *class 'NoneType'* default: *None* { #command data-toc-label=command }


### *obj*.**args** *class 'list'* default: *[]* { #args data-toc-label=args }


### *obj*.**exeDir** *class 'NoneType'* default: *None* { #exeDir data-toc-label=exeDir }


### *obj*.**exeName** *class 'NoneType'* default: *None* { #exeName data-toc-label=exeName }


### *obj*.**isGui** *class 'NoneType'* default: *None* { #isGui data-toc-label=isGui }


### *obj*.**windowStyle** *class 'NoneType'* default: *None* { #windowStyle data-toc-label=windowStyle }


### *obj*.**isUserStartUpShortcut** *class 'bool'* default: *False* { #isUserStartUpShortcut data-toc-label=isUserStartUpShortcut }


### *obj*.**isAllUsersStartUpShortcut** *class 'bool'* default: *False* { #isAllUsersStartUpShortcut data-toc-label=isAllUsersStartUpShortcut }


### *obj*.**exeVersion** *class 'NoneType'* default: *None* { #exeVersion data-toc-label=exeVersion }


### *obj*.**pngIconResPath** *class 'NoneType'* default: *None* { #pngIconResPath data-toc-label=pngIconResPath }


### *obj*.**isAppShortcut** *class 'bool'* default: *True* { #isAppShortcut data-toc-label=isAppShortcut }


### *obj*.**isDesktopShortcut** *class 'bool'* default: *False* { #isDesktopShortcut data-toc-label=isDesktopShortcut }


### *obj*.**isAdjancentShortcut** *class 'bool'* default: *False* { #isAdjancentShortcut data-toc-label=isAdjancentShortcut }



______

## **QtIfwSimpleTextPage**`#!py3 class` { #QtIfwSimpleTextPage data-toc-label=QtIfwSimpleTextPage }



**Base Classes:**

_QtIfwInterface, QtIfwUiPage


**Magic Methods:**

 - [`__init__`](#QtIfwSimpleTextPage-init)

**Instance Methods:** 

 - [`fileName`](#fileName)
 - [`resolve`](#resolve)
 - [`write`](#write)

**Class/Static Attributes:** 

 - [`BASE_ON_ENTER_TMPT`](#BASE_ON_ENTER_TMPT)
 - [`BASE_ON_LOAD_TMPT`](#BASE_ON_LOAD_TMPT)

### **QtIfwSimpleTextPage**`#!py3 (name, pageOrder=None, title='', text='', onLoad=None, onEnter=None)` { #QtIfwSimpleTextPage-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**resolve**`#!py3 (self, qtIfwConfig)` { #resolve data-toc-label=resolve }


### *obj*.**write**`#!py3 (self, dirPath)` { #write data-toc-label=write }


### *QtIfwSimpleTextPage*.**BASE_ON_ENTER_TMPT** *class 'str'* default: *"
var page = gui.pageWidgetByObjectName("Dynamic%s");
if( installer.value( "auto", "" )=="true" )
gui.clickButton(buttons.NextButton);
else {
%s                        
}
"* { #BASE_ON_ENTER_TMPT data-toc-label=BASE_ON_ENTER_TMPT }


### *QtIfwSimpleTextPage*.**BASE_ON_LOAD_TMPT** *class 'str'* default: *"    
var page = gui.pageWidgetByObjectName( "Dynamic%s" );
var wizardStyle = installer.value( "__wizardStyle", "Aero" );
switch( wizardStyle ){
case "Mac": 
page.minimumSize.width=300;
break;
case "Classic": 
page.minimumSize.width=475;
break;
case "Modern": 
page.minimumSize.width=480;
break;        
default: // "Aero" - This is the hard coded width of QtIfw example .ui's
page.minimumSize.width=491;   
}    
"* { #BASE_ON_LOAD_TMPT data-toc-label=BASE_ON_LOAD_TMPT }



______

## **QtIfwTargetDirPage**`#!py3 class` { #QtIfwTargetDirPage data-toc-label=QtIfwTargetDirPage }



**Base Classes:**

_QtIfwInterface, QtIfwUiPage


**Magic Methods:**

 - [`__init__`](#QtIfwTargetDirPage-init)

**Instance Methods:** 

 - [`fileName`](#fileName)
 - [`resolve`](#resolve)
 - [`write`](#write)

**Class/Static Attributes:** 

 - [`BASE_ON_ENTER_TMPT`](#BASE_ON_ENTER_TMPT)
 - [`BASE_ON_LOAD_TMPT`](#BASE_ON_LOAD_TMPT)
 - [`NAME`](#NAME)

### **QtIfwTargetDirPage**`#!py3 ()` { #QtIfwTargetDirPage-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**resolve**`#!py3 (self, qtIfwConfig)` { #resolve data-toc-label=resolve }


### *obj*.**write**`#!py3 (self, dirPath)` { #write data-toc-label=write }


### *QtIfwTargetDirPage*.**BASE_ON_ENTER_TMPT** *class 'str'* default: *"
var page = gui.pageWidgetByObjectName("Dynamic%s");
if( installer.value( "auto", "" )=="true" )
gui.clickButton(buttons.NextButton);
else {
%s                        
}
"* { #BASE_ON_ENTER_TMPT data-toc-label=BASE_ON_ENTER_TMPT }


### *QtIfwTargetDirPage*.**BASE_ON_LOAD_TMPT** *class 'str'* default: *"    
var page = gui.pageWidgetByObjectName( "Dynamic%s" );
var wizardStyle = installer.value( "__wizardStyle", "Aero" );
switch( wizardStyle ){
case "Mac": 
page.minimumSize.width=300;
break;
case "Classic": 
page.minimumSize.width=475;
break;
case "Modern": 
page.minimumSize.width=480;
break;        
default: // "Aero" - This is the hard coded width of QtIfw example .ui's
page.minimumSize.width=491;   
}    
"* { #BASE_ON_LOAD_TMPT data-toc-label=BASE_ON_LOAD_TMPT }


### *QtIfwTargetDirPage*.**NAME** *class 'str'* default: *"ReplaceTargetDirectory"* { #NAME data-toc-label=NAME }



______

## **QtIfwUiPage**`#!py3 class` { #QtIfwUiPage data-toc-label=QtIfwUiPage }



**Base Classes:**

_QtIfwInterface


**Magic Methods:**

 - [`__init__`](#QtIfwUiPage-init)

**Instance Methods:** 

 - [`fileName`](#fileName)
 - [`resolve`](#resolve)
 - [`write`](#write)

**Instance Attributes:** 

 - [`pageOrder`](#pageOrder)
 - [`isIncInAutoPilot`](#isIncInAutoPilot)

**Class/Static Attributes:** 

 - [`BASE_ON_ENTER_TMPT`](#BASE_ON_ENTER_TMPT)
 - [`BASE_ON_LOAD_TMPT`](#BASE_ON_LOAD_TMPT)

### **QtIfwUiPage**`#!py3 (name, pageOrder=None, sourcePath=None, content=None, onLoad=None, onEnter=None)` { #QtIfwUiPage-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**resolve**`#!py3 (self, qtIfwConfig)` { #resolve data-toc-label=resolve }


### *obj*.**write**`#!py3 (self, dirPath)` { #write data-toc-label=write }


### *obj*.**pageOrder** *class 'NoneType'* default: *None* { #pageOrder data-toc-label=pageOrder }


### *obj*.**isIncInAutoPilot** *class 'bool'* default: *False* { #isIncInAutoPilot data-toc-label=isIncInAutoPilot }


### *QtIfwUiPage*.**BASE_ON_ENTER_TMPT** *class 'str'* default: *"
var page = gui.pageWidgetByObjectName("Dynamic%s");
if( installer.value( "auto", "" )=="true" )
gui.clickButton(buttons.NextButton);
else {
%s                        
}
"* { #BASE_ON_ENTER_TMPT data-toc-label=BASE_ON_ENTER_TMPT }


### *QtIfwUiPage*.**BASE_ON_LOAD_TMPT** *class 'str'* default: *"    
var page = gui.pageWidgetByObjectName( "Dynamic%s" );
var wizardStyle = installer.value( "__wizardStyle", "Aero" );
switch( wizardStyle ){
case "Mac": 
page.minimumSize.width=300;
break;
case "Classic": 
page.minimumSize.width=475;
break;
case "Modern": 
page.minimumSize.width=480;
break;        
default: // "Aero" - This is the hard coded width of QtIfw example .ui's
page.minimumSize.width=491;   
}    
"* { #BASE_ON_LOAD_TMPT data-toc-label=BASE_ON_LOAD_TMPT }



______

## **QtIfwWidget**`#!py3 class` { #QtIfwWidget data-toc-label=QtIfwWidget }



**Base Classes:**

_QtIfwInterface


**Magic Methods:**

 - [`__init__`](#QtIfwWidget-init)

**Instance Methods:** 

 - [`fileName`](#fileName)
 - [`resolve`](#resolve)
 - [`write`](#write)

**Instance Attributes:** 

 - [`pageName`](#pageName)
 - [`position`](#position)

### **QtIfwWidget**`#!py3 (name, pageName, position=None, sourcePath=None, content=None, onLoad=None, onEnter=None)` { #QtIfwWidget-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**resolve**`#!py3 (self, qtIfwConfig)` { #resolve data-toc-label=resolve }


### *obj*.**write**`#!py3 (self, dirPath)` { #write data-toc-label=write }


### *obj*.**pageName** *class 'NoneType'* default: *None* { #pageName data-toc-label=pageName }


### *obj*.**position** *class 'NoneType'* default: *None* { #position data-toc-label=position }



______

## **RobustInstallerProcess**`#!py3 class` { #RobustInstallerProcess data-toc-label=RobustInstallerProcess }



**Base Classes:**

_DistBuildProcessBase, _BuildInstallerProcess


**Magic Methods:**

 - [`__init__`](#RobustInstallerProcess-init)

**Instance Methods:** 

 - [`onConfigFactory`](#onConfigFactory)
 - [`onFinalize`](#onFinalize)
 - [`onIExpressConfig`](#onIExpressConfig)
 - [`onIExpressPackageFinalize`](#onIExpressPackageFinalize)
 - [`onIExpressPackageInitialize`](#onIExpressPackageInitialize)
 - [`onIExpressPackageProcess`](#onIExpressPackageProcess)
 - [`onIExpressPackagesBuilt`](#onIExpressPackagesBuilt)
 - [`onInitialize`](#onInitialize)
 - [`onMakeSpec`](#onMakeSpec)
 - [`onOpyConfig`](#onOpyConfig)
 - [`onPackagesStaged`](#onPackagesStaged)
 - [`onPyInstConfig`](#onPyInstConfig)
 - [`onPyPackageFinalize`](#onPyPackageFinalize)
 - [`onPyPackageInitialize`](#onPyPackageInitialize)
 - [`onPyPackageProcess`](#onPyPackageProcess)
 - [`onPyPackagesBuilt`](#onPyPackagesBuilt)
 - [`onQtIfwConfig`](#onQtIfwConfig)
 - [`run`](#run)

**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

### **RobustInstallerProcess**`#!py3 (masterConfigFactory, name='Robust Installer Process', pyPkgConfigFactoryDict=None, iExpressPkgConfigFactoryDict=None, ifwPackages=None, isDesktopTarget=False, isHomeDirTarget=False)` { #RobustInstallerProcess-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**onConfigFactory**`#!py3 (self, key, factory)` { #onConfigFactory data-toc-label=onConfigFactory }

VIRTUAL
### *obj*.**onFinalize**`#!py3 (self)` { #onFinalize data-toc-label=onFinalize }

VIRTUAL
### *obj*.**onIExpressConfig**`#!py3 (self, key, cfg)` { #onIExpressConfig data-toc-label=onIExpressConfig }

VIRTUAL
### *obj*.**onIExpressPackageFinalize**`#!py3 (self, key)` { #onIExpressPackageFinalize data-toc-label=onIExpressPackageFinalize }

VIRTUAL
### *obj*.**onIExpressPackageInitialize**`#!py3 (self, key)` { #onIExpressPackageInitialize data-toc-label=onIExpressPackageInitialize }

VIRTUAL
### *obj*.**onIExpressPackageProcess**`#!py3 (self, key, prc)` { #onIExpressPackageProcess data-toc-label=onIExpressPackageProcess }

VIRTUAL
### *obj*.**onIExpressPackagesBuilt**`#!py3 (self, pkgs)` { #onIExpressPackagesBuilt data-toc-label=onIExpressPackagesBuilt }

VIRTUAL
### *obj*.**onInitialize**`#!py3 (self)` { #onInitialize data-toc-label=onInitialize }

VIRTUAL
### *obj*.**onMakeSpec**`#!py3 (self, key, spec)` { #onMakeSpec data-toc-label=onMakeSpec }

VIRTUAL
### *obj*.**onOpyConfig**`#!py3 (self, key, cfg)` { #onOpyConfig data-toc-label=onOpyConfig }

VIRTUAL
### *obj*.**onPackagesStaged**`#!py3 (self, cfg, pkgs)` { #onPackagesStaged data-toc-label=onPackagesStaged }

VIRTUAL
### *obj*.**onPyInstConfig**`#!py3 (self, key, cfg)` { #onPyInstConfig data-toc-label=onPyInstConfig }

VIRTUAL
### *obj*.**onPyPackageFinalize**`#!py3 (self, key)` { #onPyPackageFinalize data-toc-label=onPyPackageFinalize }

VIRTUAL
### *obj*.**onPyPackageInitialize**`#!py3 (self, key)` { #onPyPackageInitialize data-toc-label=onPyPackageInitialize }

VIRTUAL
### *obj*.**onPyPackageProcess**`#!py3 (self, key, prc)` { #onPyPackageProcess data-toc-label=onPyPackageProcess }

VIRTUAL
### *obj*.**onPyPackagesBuilt**`#!py3 (self, pkgs)` { #onPyPackagesBuilt data-toc-label=onPyPackagesBuilt }

VIRTUAL
### *obj*.**onQtIfwConfig**`#!py3 (self, cfg)` { #onQtIfwConfig data-toc-label=onQtIfwConfig }

VIRTUAL
### *obj*.**run**`#!py3 (self)` { #run data-toc-label=run }


### *RobustInstallerProcess*.**DIVIDER** *class 'str'* default: *"------------------------------------"* { #DIVIDER data-toc-label=DIVIDER }



______

## **Functions** { #Functions data-toc-label=Functions }

### **buildInstaller**`#!py3 (qtIfwConfig, isSilent)` { #buildInstaller data-toc-label=buildInstaller }

returns setupExePath 

______

### **findQtIfwPackage**`#!py3 (pkgs, pkgId)` { #findQtIfwPackage data-toc-label=findQtIfwPackage }



______

### **installQtIfw**`#!py3 (installerPath=None, version=None, targetPath=None)` { #installQtIfw data-toc-label=installQtIfw }



______

### **joinPathQtIfw**`#!py3 (head, *tail)` { #joinPathQtIfw data-toc-label=joinPathQtIfw }



______

### **mergeQtIfwPackages**`#!py3 (pkgs, srcId, destId)` { #mergeQtIfwPackages data-toc-label=mergeQtIfwPackages }



______

### **nestQtIfwPackage**`#!py3 (pkgs, childId, parentId, subDirName=None)` { #nestQtIfwPackage data-toc-label=nestQtIfwPackage }



______

### **qtIfwDetachedOpDataPath**`#!py3 (rootFileName)` { #qtIfwDetachedOpDataPath data-toc-label=qtIfwDetachedOpDataPath }



______

### **qtIfwDynamicValue**`#!py3 (name)` { #qtIfwDynamicValue data-toc-label=qtIfwDynamicValue }



______

### **qtIfwOpDataPath**`#!py3 (rootFileName)` { #qtIfwOpDataPath data-toc-label=qtIfwOpDataPath }



______

### **removeQtIfwPackage**`#!py3 (pkgs, pkgId)` { #removeQtIfwPackage data-toc-label=removeQtIfwPackage }



______

### **unInstallQtIfw**`#!py3 (qtIfwDirPath=None, version=None)` { #unInstallQtIfw data-toc-label=unInstallQtIfw }



______

## **Constants and Globals** { #Constants-and-Globals data-toc-label="Constants and Globals" }

### **QT_IFW_ALLUSERS_STARTMENU_DIR** *class 'str'* default: *"@AllUsersStartMenuProgramsPath@"* { #QT_IFW_ALLUSERS_STARTMENU_DIR data-toc-label=QT_IFW_ALLUSERS_STARTMENU_DIR }



______

### **QT_IFW_APPS_DIR** *class 'str'* default: *"@ApplicationsDir@"* { #QT_IFW_APPS_DIR data-toc-label=QT_IFW_APPS_DIR }



______

### **QT_IFW_APPS_X64_DIR** *class 'str'* default: *"@ApplicationsDirX64@"* { #QT_IFW_APPS_X64_DIR data-toc-label=QT_IFW_APPS_X64_DIR }



______

### **QT_IFW_APPS_X86_DIR** *class 'str'* default: *"@ApplicationsDirX86@"* { #QT_IFW_APPS_X86_DIR data-toc-label=QT_IFW_APPS_X86_DIR }



______

### **QT_IFW_COMPONENTS_PAGE** *class 'str'* default: *"ComponentSelection"* { #QT_IFW_COMPONENTS_PAGE data-toc-label=QT_IFW_COMPONENTS_PAGE }



______

### **QT_IFW_DEFAULT_TARGET_DIR** *class 'str'* default: *"@DefaultTargetDir@"* { #QT_IFW_DEFAULT_TARGET_DIR data-toc-label=QT_IFW_DEFAULT_TARGET_DIR }



______

### **QT_IFW_DESKTOP_DIR** *class 'str'* default: *"@DesktopDir@"* { #QT_IFW_DESKTOP_DIR data-toc-label=QT_IFW_DESKTOP_DIR }



______

### **QT_IFW_DYNAMIC_VARS** *class 'list'* default: *['TargetDir', 'DefaultTargetDir', 'RootDir', 'HomeDir', 'DesktopDir', 'ApplicationsDir', 'StartMenuDir', 'UserStartMenuProgramsPath', 'AllUsersStartMenuProgramsPath', 'ApplicationsDirX86', 'ApplicationsDirX64', 'TempDir', 'InstallerTempDir', 'MaintenanceTempDir', 'ScriptsDir', 'InstallerDirPath', 'InstallerFilePath', 'User', 'ProductName', 'ProductVersion', 'Title', 'Publisher', 'Url', 'os']* { #QT_IFW_DYNAMIC_VARS data-toc-label=QT_IFW_DYNAMIC_VARS }



______

### **QT_IFW_FINISHED_PAGE** *class 'str'* default: *"InstallationFinished"* { #QT_IFW_FINISHED_PAGE data-toc-label=QT_IFW_FINISHED_PAGE }



______

### **QT_IFW_HOME_DIR** *class 'str'* default: *"@HomeDir@"* { #QT_IFW_HOME_DIR data-toc-label=QT_IFW_HOME_DIR }



______

### **QT_IFW_INSTALLER_DIR** *class 'str'* default: *"@InstallerDirPath@"* { #QT_IFW_INSTALLER_DIR data-toc-label=QT_IFW_INSTALLER_DIR }



______

### **QT_IFW_INSTALLER_TEMP_DIR** *class 'str'* default: *"@InstallerTempDir@"* { #QT_IFW_INSTALLER_TEMP_DIR data-toc-label=QT_IFW_INSTALLER_TEMP_DIR }



______

### **QT_IFW_INSTALL_PAGE** *class 'str'* default: *"PerformInstallation"* { #QT_IFW_INSTALL_PAGE data-toc-label=QT_IFW_INSTALL_PAGE }



______

### **QT_IFW_INTALLER_PATH** *class 'str'* default: *"@InstallerFilePath@"* { #QT_IFW_INTALLER_PATH data-toc-label=QT_IFW_INTALLER_PATH }



______

### **QT_IFW_INTRO_PAGE** *class 'str'* default: *"Introduction"* { #QT_IFW_INTRO_PAGE data-toc-label=QT_IFW_INTRO_PAGE }



______

### **QT_IFW_LICENSE_PAGE** *class 'str'* default: *"LicenseCheck"* { #QT_IFW_LICENSE_PAGE data-toc-label=QT_IFW_LICENSE_PAGE }



______

### **QT_IFW_MAINTENANCE_TEMP_DIR** *class 'str'* default: *"@MaintenanceTempDir@"* { #QT_IFW_MAINTENANCE_TEMP_DIR data-toc-label=QT_IFW_MAINTENANCE_TEMP_DIR }



______

### **QT_IFW_OS** *class 'str'* default: *"@os@"* { #QT_IFW_OS data-toc-label=QT_IFW_OS }



______

### **QT_IFW_POST_INSTALL** *class 'int'* default: *1* { #QT_IFW_POST_INSTALL data-toc-label=QT_IFW_POST_INSTALL }



______

### **QT_IFW_PRE_INSTALL** *class 'int'* default: *0* { #QT_IFW_PRE_INSTALL data-toc-label=QT_IFW_PRE_INSTALL }



______

### **QT_IFW_PRODUCT_NAME** *class 'str'* default: *"@ProductName@"* { #QT_IFW_PRODUCT_NAME data-toc-label=QT_IFW_PRODUCT_NAME }



______

### **QT_IFW_PRODUCT_VERSION** *class 'str'* default: *"@ProductVersion@"* { #QT_IFW_PRODUCT_VERSION data-toc-label=QT_IFW_PRODUCT_VERSION }



______

### **QT_IFW_PUBLISHER** *class 'str'* default: *"@Publisher@"* { #QT_IFW_PUBLISHER data-toc-label=QT_IFW_PUBLISHER }



______

### **QT_IFW_READY_PAGE** *class 'str'* default: *"ReadyForInstallation"* { #QT_IFW_READY_PAGE data-toc-label=QT_IFW_READY_PAGE }



______

### **QT_IFW_REPLACE_PAGE_PREFIX** *class 'str'* default: *"Replace"* { #QT_IFW_REPLACE_PAGE_PREFIX data-toc-label=QT_IFW_REPLACE_PAGE_PREFIX }



______

### **QT_IFW_ROOT_DIR** *class 'str'* default: *"@RootDir@"* { #QT_IFW_ROOT_DIR data-toc-label=QT_IFW_ROOT_DIR }



______

### **QT_IFW_SCRIPTS_DIR** *class 'str'* default: *"@ScriptsDir@"* { #QT_IFW_SCRIPTS_DIR data-toc-label=QT_IFW_SCRIPTS_DIR }



______

### **QT_IFW_STARTMENU_DIR** *class 'str'* default: *"@StartMenuDir@"* { #QT_IFW_STARTMENU_DIR data-toc-label=QT_IFW_STARTMENU_DIR }



______

### **QT_IFW_START_MENU_PAGE** *class 'str'* default: *"StartMenuSelection"* { #QT_IFW_START_MENU_PAGE data-toc-label=QT_IFW_START_MENU_PAGE }



______

### **QT_IFW_TARGET_DIR** *class 'str'* default: *"@TargetDir@"* { #QT_IFW_TARGET_DIR data-toc-label=QT_IFW_TARGET_DIR }



______

### **QT_IFW_TARGET_DIR_PAGE** *class 'str'* default: *"TargetDirectory"* { #QT_IFW_TARGET_DIR_PAGE data-toc-label=QT_IFW_TARGET_DIR_PAGE }



______

### **QT_IFW_TEMP_DIR** *class 'str'* default: *"@TempDir@"* { #QT_IFW_TEMP_DIR data-toc-label=QT_IFW_TEMP_DIR }



______

### **QT_IFW_TITLE** *class 'str'* default: *"@Title@"* { #QT_IFW_TITLE data-toc-label=QT_IFW_TITLE }



______

### **QT_IFW_URL** *class 'str'* default: *"@Url@"* { #QT_IFW_URL data-toc-label=QT_IFW_URL }



______

### **QT_IFW_USER** *class 'str'* default: *"@User@"* { #QT_IFW_USER data-toc-label=QT_IFW_USER }



______

### **QT_IFW_USER_STARTMENU_DIR** *class 'str'* default: *"@UserStartMenuProgramsPath@"* { #QT_IFW_USER_STARTMENU_DIR data-toc-label=QT_IFW_USER_STARTMENU_DIR }



______

### **QT_IFW_VERBOSE_SWITCH** *class 'str'* default: *"-v"* { #QT_IFW_VERBOSE_SWITCH data-toc-label=QT_IFW_VERBOSE_SWITCH }



______

