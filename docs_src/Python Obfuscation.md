## **LibToBundle**`#!py3 class` { #LibToBundle data-toc-label=LibToBundle }



**Magic Methods:**

 - [`__init__`](#LibToBundle-init)

**Instance Methods:** 


**Instance Attributes:** 

 - [`name`](#name)
 - [`localDirPath`](#localDirPath)
 - [`pipConfig`](#pipConfig)
 - [`isObfuscated`](#isObfuscated)

### **LibToBundle**`#!py3 (name, localDirPath=None, pipConfig=None, isObfuscated=False)` { #LibToBundle-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**name** *<class 'NoneType'>* default: *None* { #name data-toc-label=name }


### *obj*.**localDirPath** *<class 'NoneType'>* default: *None* { #localDirPath data-toc-label=localDirPath }


### *obj*.**pipConfig** *<class 'NoneType'>* default: *None* { #pipConfig data-toc-label=pipConfig }


### *obj*.**isObfuscated** *<class 'NoneType'>* default: *None* { #isObfuscated data-toc-label=isObfuscated }



______

## **OpyConfig**`#!py3 class` { #OpyConfig data-toc-label=OpyConfig }

See opy_config.txt for details on these settings.

**Magic Methods:**

 - [`__init__`](#OpyConfig-init)

**Instance Methods:** 

 - [`toVirtualFile`](#toVirtualFile)

**Instance Attributes:** 

 - [`obfuscate_strings`](#obfuscate_strings)
 - [`obfuscated_name_tail`](#obfuscated_name_tail)
 - [`plain_marker`](#plain_marker)
 - [`pep8_comments`](#pep8_comments)
 - [`source_extensions`](#source_extensions)
 - [`skip_extensions`](#skip_extensions)
 - [`skip_path_fragments`](#skip_path_fragments)
 - [`apply_standard_exclusions`](#apply_standard_exclusions)
 - [`preserve_unresolved_imports`](#preserve_unresolved_imports)
 - [`error_on_unresolved_imports`](#error_on_unresolved_imports)
 - [`external_modules`](#external_modules)
 - [`replacement_modules`](#replacement_modules)
 - [`plain_files`](#plain_files)
 - [`plain_names`](#plain_names)
 - [`mask_external_modules`](#mask_external_modules)
 - [`skip_public`](#skip_public)
 - [`subset_files`](#subset_files)
 - [`dry_run`](#dry_run)
 - [`prepped_only`](#prepped_only)

### **OpyConfig**`#!py3 ()` { #OpyConfig-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**toVirtualFile**`#!py3 (self)` { #toVirtualFile data-toc-label=toVirtualFile }


### *obj*.**obfuscate_strings** *<class 'bool'>* default: *True* { #obfuscate_strings data-toc-label=obfuscate_strings }


### *obj*.**obfuscated_name_tail** *<class 'str'>* default: *"_opy_"* { #obfuscated_name_tail data-toc-label=obfuscated_name_tail }


### *obj*.**plain_marker** *<class 'str'>* default: *"_opy_"* { #plain_marker data-toc-label=plain_marker }


### *obj*.**pep8_comments** *<class 'bool'>* default: *False* { #pep8_comments data-toc-label=pep8_comments }


### *obj*.**source_extensions** *<class 'list'>* default: *['py', 'pyx']* { #source_extensions data-toc-label=source_extensions }


### *obj*.**skip_extensions** *<class 'list'>* default: *['pyc', 'txt', 'project', 'pydevproject', 'settings']* { #skip_extensions data-toc-label=skip_extensions }


### *obj*.**skip_path_fragments** *<class 'list'>* default: *['opy_config.txt', 'opy_config.py', 'standard_exclusions.txt']* { #skip_path_fragments data-toc-label=skip_path_fragments }


### *obj*.**apply_standard_exclusions** *<class 'bool'>* default: *True* { #apply_standard_exclusions data-toc-label=apply_standard_exclusions }


### *obj*.**preserve_unresolved_imports** *<class 'bool'>* default: *True* { #preserve_unresolved_imports data-toc-label=preserve_unresolved_imports }


### *obj*.**error_on_unresolved_imports** *<class 'bool'>* default: *True* { #error_on_unresolved_imports data-toc-label=error_on_unresolved_imports }


### *obj*.**external_modules** *<class 'list'>* default: *[]* { #external_modules data-toc-label=external_modules }


### *obj*.**replacement_modules** *<class 'dict'>* default: *{}* { #replacement_modules data-toc-label=replacement_modules }


### *obj*.**plain_files** *<class 'list'>* default: *[]* { #plain_files data-toc-label=plain_files }


### *obj*.**plain_names** *<class 'list'>* default: *[]* { #plain_names data-toc-label=plain_names }


### *obj*.**mask_external_modules** *<class 'bool'>* default: *True* { #mask_external_modules data-toc-label=mask_external_modules }


### *obj*.**skip_public** *<class 'bool'>* default: *False* { #skip_public data-toc-label=skip_public }


### *obj*.**subset_files** *<class 'list'>* default: *[]* { #subset_files data-toc-label=subset_files }


### *obj*.**dry_run** *<class 'bool'>* default: *False* { #dry_run data-toc-label=dry_run }


### *obj*.**prepped_only** *<class 'bool'>* default: *False* { #prepped_only data-toc-label=prepped_only }



______

## **OpyPatch**`#!py3 class` { #OpyPatch data-toc-label=OpyPatch }



**Magic Methods:**

 - [`__init__`](#OpyPatch-init)

**Instance Methods:** 

 - [`apply`](#apply)
 - [`obfuscatePath`](#obfuscatePath)

**Instance Attributes:** 

 - [`relPath`](#relPath)
 - [`path`](#path)
 - [`patches`](#patches)

### **OpyPatch**`#!py3 (relPath, patches, parentDir='C:\\Python37\\Scripts\\obfuscated')` { #OpyPatch-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**apply**`#!py3 (self, opyResults)` { #apply data-toc-label=apply }


### *obj*.**obfuscatePath**`#!py3 (self, opyResults)` { #obfuscatePath data-toc-label=obfuscatePath }


### *obj*.**relPath** *<class 'NoneType'>* default: *None* { #relPath data-toc-label=relPath }


### *obj*.**path** *<class 'NoneType'>* default: *None* { #path data-toc-label=path }


### *obj*.**patches** *<class 'NoneType'>* default: *None* { #patches data-toc-label=patches }



______

## **Functions** { #Functions data-toc-label=Functions }

### **createStageDir**`#!py3 (bundleLibs=None, sourceDir='C:\\Python37\\Scripts')` { #createStageDir data-toc-label=createStageDir }

returns: stageDir 

______

### **obfuscatePy**`#!py3 (opyConfig)` { #obfuscatePy data-toc-label=obfuscatePy }



______

### **opyAnalyze**`#!py3 (opyConfig, filesSubset=None)` { #opyAnalyze data-toc-label=opyAnalyze }



______

