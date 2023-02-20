## **CodeSignConfig**`#!py3 class` { #CodeSignConfig data-toc-label=CodeSignConfig }



**Class/Static Attributes:** 

 - [`DEFAULT_DIGEST`](#DEFAULT_DIGEST)
 - [`DEFAULT_TIMESTAMP_SERVER`](#DEFAULT_TIMESTAMP_SERVER)

**Instance Attributes:** 

 - [`keyFilePath`](#keyFilePath)
 - [`keyPassword`](#keyPassword)
 - [`signToolPath`](#signToolPath)
 - [`fileDigest`](#fileDigest)
 - [`timeStampDigest`](#timeStampDigest)
 - [`timeStampServerUrl`](#timeStampServerUrl)
 - [`otherSignToolArgs`](#otherSignToolArgs)
 - [`isDebugMode`](#isDebugMode)

### *CodeSignConfig*.**DEFAULT_DIGEST** *class 'str'* default: *"sha256"* { #DEFAULT_DIGEST data-toc-label=DEFAULT_DIGEST }


### *CodeSignConfig*.**DEFAULT_TIMESTAMP_SERVER** *class 'str'* default: *"http://timestamp.digicert.com"* { #DEFAULT_TIMESTAMP_SERVER data-toc-label=DEFAULT_TIMESTAMP_SERVER }


### *obj*.**keyFilePath** *class 'NoneType'* default: *None* { #keyFilePath data-toc-label=keyFilePath }


### *obj*.**keyPassword** *class 'NoneType'* default: *None* { #keyPassword data-toc-label=keyPassword }


### *obj*.**signToolPath** *class 'NoneType'* default: *None* { #signToolPath data-toc-label=signToolPath }


### *obj*.**fileDigest** *class 'str'* default: *"sha256"* { #fileDigest data-toc-label=fileDigest }


### *obj*.**timeStampDigest** *class 'str'* default: *"sha256"* { #timeStampDigest data-toc-label=timeStampDigest }


### *obj*.**timeStampServerUrl** *class 'str'* default: *"http://timestamp.digicert.com"* { #timeStampServerUrl data-toc-label=timeStampServerUrl }


### *obj*.**otherSignToolArgs** *class 'str'* default: *"&lt;empty string&gt;"* { #otherSignToolArgs data-toc-label=otherSignToolArgs }


### *obj*.**isDebugMode** *class 'bool'* default: *True* { #isDebugMode data-toc-label=isDebugMode }



______

## **SelfSignedCertConfig**`#!py3 class` { #SelfSignedCertConfig data-toc-label=SelfSignedCertConfig }



**Class/Static Attributes:** 

 - [`DEFAULT_END_DATE`](#DEFAULT_END_DATE)
 - [`LIFETIME_SIGNING_EKU`](#LIFETIME_SIGNING_EKU)
 - [`NO_MAX_CHILDREN`](#NO_MAX_CHILDREN)

**Instance Attributes:** 

 - [`commonName`](#commonName)
 - [`endDate`](#endDate)
 - [`destDirPath`](#destDirPath)
 - [`caCertPath`](#caCertPath)
 - [`privateKeyPath`](#privateKeyPath)
 - [`makeCertPath`](#makeCertPath)
 - [`otherArgs`](#otherArgs)
 - [`isDebugMode`](#isDebugMode)

### *SelfSignedCertConfig*.**DEFAULT_END_DATE** *class 'str'* default: *None* { #DEFAULT_END_DATE data-toc-label=DEFAULT_END_DATE }


### *SelfSignedCertConfig*.**LIFETIME_SIGNING_EKU** *class 'str'* default: *None* { #LIFETIME_SIGNING_EKU data-toc-label=LIFETIME_SIGNING_EKU }


### *SelfSignedCertConfig*.**NO_MAX_CHILDREN** *class 'int'* default: *None* { #NO_MAX_CHILDREN data-toc-label=NO_MAX_CHILDREN }


### *obj*.**commonName** *class 'NoneType'* default: *None* { #commonName data-toc-label=commonName }


### *obj*.**endDate** *class 'NoneType'* default: *None* { #endDate data-toc-label=endDate }


### *obj*.**destDirPath** *class 'NoneType'* default: *None* { #destDirPath data-toc-label=destDirPath }


### *obj*.**caCertPath** *class 'NoneType'* default: *None* { #caCertPath data-toc-label=caCertPath }


### *obj*.**privateKeyPath** *class 'NoneType'* default: *None* { #privateKeyPath data-toc-label=privateKeyPath }


### *obj*.**makeCertPath** *class 'NoneType'* default: *None* { #makeCertPath data-toc-label=makeCertPath }


### *obj*.**otherArgs** *class 'NoneType'* default: *None* { #otherArgs data-toc-label=otherArgs }


### *obj*.**isDebugMode** *class 'NoneType'* default: *None* { #isDebugMode data-toc-label=isDebugMode }



______

## **TrustInstallerBuilderProcess**`#!py3 class` { #TrustInstallerBuilderProcess data-toc-label=TrustInstallerBuilderProcess }



**Class/Static Attributes:** 

 - [`DIVIDER`](#DIVIDER)

**Instance Methods:** 

 - [`onFinalize`](#onFinalize)
 - [`onInitialize`](#onInitialize)
 - [`onMakeSpec`](#onMakeSpec)
 - [`onOpyConfig`](#onOpyConfig)
 - [`onPyInstConfig`](#onPyInstConfig)
 - [`run`](#run)

### *TrustInstallerBuilderProcess*.**DIVIDER** *class 'str'* default: *"------------------------------------"* { #DIVIDER data-toc-label=DIVIDER }


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



______

## **Functions** { #Functions data-toc-label=Functions }

### **generateTrustCerts**`#!py3 (certConfig, keyPassword=None, isOverwrite=False)` { #generateTrustCerts data-toc-label=generateTrustCerts }

Returns CA Cert Path, Key Path 

______

### **signExe**`#!py3 (exePath, codeSignConfig)` { #signExe data-toc-label=signExe }

Returns exePath 

______

### **trustCertInstallerConfigFactory**`#!py3 (companyTradeName, caCertPath, keyFilePath, keyPassword=None, companyLegalName=None, version=(1, 0, 0, 0), iconFilePath=None, isSilent=False, script=None)` { #trustCertInstallerConfigFactory data-toc-label=trustCertInstallerConfigFactory }



______

## **Constants and Globals** { #Constants-and-Globals data-toc-label="Constants and Globals" }

### **MAKECERT_PATH_ENV_VAR** *class 'str'* default: *"MAKECERT_PATH"* { #MAKECERT_PATH_ENV_VAR data-toc-label=MAKECERT_PATH_ENV_VAR }



______

### **PVK2PFX_PATH_ENV_VAR** *class 'str'* default: *"PVK2PFX_PATH"* { #PVK2PFX_PATH_ENV_VAR data-toc-label=PVK2PFX_PATH_ENV_VAR }



______

### **SIGNTOOL_PATH_ENV_VAR** *class 'str'* default: *"SIGNTOOL_PATH"* { #SIGNTOOL_PATH_ENV_VAR data-toc-label=SIGNTOOL_PATH_ENV_VAR }



______

