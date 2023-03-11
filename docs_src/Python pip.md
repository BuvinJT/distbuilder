## **PipConfig**`#!py3 class` { #PipConfig data-toc-label=PipConfig }

See Pip docs for details on these settings.

Important Note: source maybe a: 
package name, git repo url, or local path

**Magic Methods:**

 - [`__init__`](#PipConfig-init)

**Instance Methods:** 


**Instance Attributes:** 

 - [`pipCmdBase`](#pipCmdBase)
 - [`source`](#source)
 - [`version`](#version)
 - [`verEquality`](#verEquality)
 - [`destPath`](#destPath)
 - [`asSource`](#asSource)
 - [`incDependencies`](#incDependencies)
 - [`isForced`](#isForced)
 - [`isCacheUsed`](#isCacheUsed)
 - [`isUpgrade`](#isUpgrade)
 - [`otherPipArgs`](#otherPipArgs)

### **PipConfig**`#!py3 (source=None, version=None, verEquality='==', destPath=None, asSource=False, incDependencies=True, isForced=False, isCacheUsed=True, isUpgrade=False, otherPipArgs='')` { #PipConfig-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**pipCmdBase** *class 'str'* default: *""c:\python37\python3.exe" -m pip"* { #pipCmdBase data-toc-label=pipCmdBase }


### *obj*.**source** *class 'NoneType'* default: *None* { #source data-toc-label=source }


### *obj*.**version** *class 'NoneType'* default: *None* { #version data-toc-label=version }


### *obj*.**verEquality** *class 'NoneType'* default: *None* { #verEquality data-toc-label=verEquality }


### *obj*.**destPath** *class 'NoneType'* default: *None* { #destPath data-toc-label=destPath }


### *obj*.**asSource** *class 'NoneType'* default: *None* { #asSource data-toc-label=asSource }


### *obj*.**incDependencies** *class 'NoneType'* default: *None* { #incDependencies data-toc-label=incDependencies }


### *obj*.**isForced** *class 'NoneType'* default: *None* { #isForced data-toc-label=isForced }


### *obj*.**isCacheUsed** *class 'NoneType'* default: *None* { #isCacheUsed data-toc-label=isCacheUsed }


### *obj*.**isUpgrade** *class 'NoneType'* default: *None* { #isUpgrade data-toc-label=isUpgrade }


### *obj*.**otherPipArgs** *class 'NoneType'* default: *None* { #otherPipArgs data-toc-label=otherPipArgs }



______

## **Functions** { #Functions data-toc-label=Functions }

### **installLibraries**`#!py3 (*libs)` { #installLibraries data-toc-label=installLibraries }



______

### **installLibrary**`#!py3 (name, opyConfig=None, pipConfig=None)` { #installLibrary data-toc-label=installLibrary }



______

### **uninstallLibrary**`#!py3 (name)` { #uninstallLibrary data-toc-label=uninstallLibrary }



______

### **updatePip**`#!py3 ()` { #updatePip data-toc-label=updatePip }



______

### **vcsUrl**`#!py3 (name, baseUrl, vcs='git', subDir=None)` { #vcsUrl data-toc-label=vcsUrl }



______

