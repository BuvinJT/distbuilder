## **LibToBundle**`#!py3 class` { #LibToBundle data-toc-label=LibToBundle }



**Instance Attributes:** 

 - [`name`](#name)
 - [`localDirPath`](#localDirPath)
 - [`pipConfig`](#pipConfig)
 - [`isObfuscated`](#isObfuscated)

### *obj*.**name** *undefined* { #name data-toc-label=name }

### *obj*.**localDirPath** *undefined* { #localDirPath data-toc-label=localDirPath }

### *obj*.**pipConfig** *undefined* { #pipConfig data-toc-label=pipConfig }

### *obj*.**isObfuscated** *undefined* { #isObfuscated data-toc-label=isObfuscated }


______

## **OpyConfig**`#!py3 class` { #OpyConfig data-toc-label=OpyConfig }

See opy_config.txt for details on these settings.

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

### *obj*.**toVirtualFile**`#!py3 (self)` { #toVirtualFile data-toc-label=toVirtualFile }


### *obj*.**obfuscate_strings** *undefined* { #obfuscate_strings data-toc-label=obfuscate_strings }

### *obj*.**obfuscated_name_tail** *undefined* { #obfuscated_name_tail data-toc-label=obfuscated_name_tail }

### *obj*.**plain_marker** *undefined* { #plain_marker data-toc-label=plain_marker }

### *obj*.**pep8_comments** *undefined* { #pep8_comments data-toc-label=pep8_comments }

### *obj*.**source_extensions** *undefined* { #source_extensions data-toc-label=source_extensions }

### *obj*.**skip_extensions** *undefined* { #skip_extensions data-toc-label=skip_extensions }

### *obj*.**skip_path_fragments** *undefined* { #skip_path_fragments data-toc-label=skip_path_fragments }

### *obj*.**apply_standard_exclusions** *undefined* { #apply_standard_exclusions data-toc-label=apply_standard_exclusions }

### *obj*.**preserve_unresolved_imports** *undefined* { #preserve_unresolved_imports data-toc-label=preserve_unresolved_imports }

### *obj*.**error_on_unresolved_imports** *undefined* { #error_on_unresolved_imports data-toc-label=error_on_unresolved_imports }

### *obj*.**external_modules** *undefined* { #external_modules data-toc-label=external_modules }

### *obj*.**replacement_modules** *undefined* { #replacement_modules data-toc-label=replacement_modules }

### *obj*.**plain_files** *undefined* { #plain_files data-toc-label=plain_files }

### *obj*.**plain_names** *undefined* { #plain_names data-toc-label=plain_names }

### *obj*.**mask_external_modules** *undefined* { #mask_external_modules data-toc-label=mask_external_modules }

### *obj*.**skip_public** *undefined* { #skip_public data-toc-label=skip_public }

### *obj*.**subset_files** *undefined* { #subset_files data-toc-label=subset_files }

### *obj*.**dry_run** *undefined* { #dry_run data-toc-label=dry_run }

### *obj*.**prepped_only** *undefined* { #prepped_only data-toc-label=prepped_only }


______

## **OpyPatch**`#!py3 class` { #OpyPatch data-toc-label=OpyPatch }



**Instance Methods:** 

 - [`apply`](#apply)
 - [`obfuscatePath`](#obfuscatePath)

**Instance Attributes:** 

 - [`relPath`](#relPath)
 - [`path`](#path)
 - [`patches`](#patches)

### *obj*.**apply**`#!py3 (self, opyResults)` { #apply data-toc-label=apply }


### *obj*.**obfuscatePath**`#!py3 (self, opyResults)` { #obfuscatePath data-toc-label=obfuscatePath }


### *obj*.**relPath** *undefined* { #relPath data-toc-label=relPath }

### *obj*.**path** *undefined* { #path data-toc-label=path }

### *obj*.**patches** *undefined* { #patches data-toc-label=patches }


______

## **Functions** { #Functions data-toc-label=Functions }

### **createStageDir**`#!py3 (bundleLibs=None, sourceDir='C:\\Python37\\Scripts')` { #createStageDir data-toc-label=createStageDir }

returns: stageDir 

______

### **obfuscatePy**`#!py3 (opyConfig)` { #obfuscatePy data-toc-label=obfuscatePy }



______

### **opyAnalyze**`#!py3 (opyConfig, filesSubset=None)` { #opyAnalyze data-toc-label=opyAnalyze }



______

