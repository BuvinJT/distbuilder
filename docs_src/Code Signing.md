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

### *CodeSignConfig*.**DEFAULT_DIGEST** *class 'str'* { #DEFAULT_DIGEST data-toc-label=DEFAULT_DIGEST }

### *CodeSignConfig*.**DEFAULT_TIMESTAMP_SERVER** *class 'str'* { #DEFAULT_TIMESTAMP_SERVER data-toc-label=DEFAULT_TIMESTAMP_SERVER }

### *obj*.**keyFilePath** *undefined* { #keyFilePath data-toc-label=keyFilePath }

### *obj*.**keyPassword** *undefined* { #keyPassword data-toc-label=keyPassword }

### *obj*.**signToolPath** *undefined* { #signToolPath data-toc-label=signToolPath }

### *obj*.**fileDigest** *undefined* { #fileDigest data-toc-label=fileDigest }

### *obj*.**timeStampDigest** *undefined* { #timeStampDigest data-toc-label=timeStampDigest }

### *obj*.**timeStampServerUrl** *undefined* { #timeStampServerUrl data-toc-label=timeStampServerUrl }

### *obj*.**otherSignToolArgs** *undefined* { #otherSignToolArgs data-toc-label=otherSignToolArgs }

### *obj*.**isDebugMode** *undefined* { #isDebugMode data-toc-label=isDebugMode }


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

### *SelfSignedCertConfig*.**DEFAULT_END_DATE** *class 'str'* { #DEFAULT_END_DATE data-toc-label=DEFAULT_END_DATE }

### *SelfSignedCertConfig*.**LIFETIME_SIGNING_EKU** *class 'str'* { #LIFETIME_SIGNING_EKU data-toc-label=LIFETIME_SIGNING_EKU }

### *SelfSignedCertConfig*.**NO_MAX_CHILDREN** *class 'int'* { #NO_MAX_CHILDREN data-toc-label=NO_MAX_CHILDREN }

### *obj*.**commonName** *undefined* { #commonName data-toc-label=commonName }

### *obj*.**endDate** *undefined* { #endDate data-toc-label=endDate }

### *obj*.**destDirPath** *undefined* { #destDirPath data-toc-label=destDirPath }

### *obj*.**caCertPath** *undefined* { #caCertPath data-toc-label=caCertPath }

### *obj*.**privateKeyPath** *undefined* { #privateKeyPath data-toc-label=privateKeyPath }

### *obj*.**makeCertPath** *undefined* { #makeCertPath data-toc-label=makeCertPath }

### *obj*.**otherArgs** *undefined* { #otherArgs data-toc-label=otherArgs }

### *obj*.**isDebugMode** *undefined* { #isDebugMode data-toc-label=isDebugMode }


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

### *TrustInstallerBuilderProcess*.**DIVIDER** *class 'str'* { #DIVIDER data-toc-label=DIVIDER }

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

### **MAKECERT_PATH_ENV_VAR** *class 'str'* { #MAKECERT_PATH_ENV_VAR data-toc-label=MAKECERT_PATH_ENV_VAR }


______

### **PVK2PFX_PATH_ENV_VAR** *class 'str'* { #PVK2PFX_PATH_ENV_VAR data-toc-label=PVK2PFX_PATH_ENV_VAR }


______

### **SIGNTOOL_PATH_ENV_VAR** *class 'str'* { #SIGNTOOL_PATH_ENV_VAR data-toc-label=SIGNTOOL_PATH_ENV_VAR }


______

