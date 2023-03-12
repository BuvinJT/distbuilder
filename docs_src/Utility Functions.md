### **absPath**`#!py3 (relativePath, basePath=None)` { #absPath data-toc-label=absPath }



______

### **allPathPattern**`#!py3 (basePath)` { #allPathPattern data-toc-label=allPathPattern }



______

### **assertMinVer**`#!py3 (ver, minVer, parts=4, partLen=3, descr=None)` { #assertMinVer data-toc-label=assertMinVer }



______

### **collectDirs**`#!py3 (srcDirPaths, destDirPath)` { #collectDirs data-toc-label=collectDirs }

Move a list of directories into a common parent directory 

______

### **containsPathPattern**`#!py3 (match, basePath=None)` { #containsPathPattern data-toc-label=containsPathPattern }



______

### **copyExeIcon**`#!py3 (srcExePath, destExePath, iconName=None)` { #copyExeIcon data-toc-label=copyExeIcon }



______

### **copyExeVerInfo**`#!py3 (srcExePath, destExePath)` { #copyExeVerInfo data-toc-label=copyExeVerInfo }



______

### **copyToDesktop**`#!py3 (path)` { #copyToDesktop data-toc-label=copyToDesktop }



______

### **copyToDir**`#!py3 (srcPaths, destDirPath=None)` { #copyToDir data-toc-label=copyToDir }

Copy files OR directories to a given destination.
The argument srcPaths may be a singular path (i.e. a string)
or an iterable (i.e. a list or tuple).  

______

### **copyToHomeDir**`#!py3 (path)` { #copyToHomeDir data-toc-label=copyToHomeDir }



______

### **delEnv**`#!py3 (varName)` { #delEnv data-toc-label=delEnv }



______

### **desktopPath**`#!py3 (relPath=None)` { #desktopPath data-toc-label=desktopPath }



______

### **download**`#!py3 (url, saveToPath=None, preserveName=True)` { #download data-toc-label=download }



______

### **embedAutoElevation**`#!py3 (exePath)` { #embedAutoElevation data-toc-label=embedAutoElevation }



______

### **embedExeIcon**`#!py3 (exePath, iconPath)` { #embedExeIcon data-toc-label=embedExeIcon }



______

### **embedExeVerInfo**`#!py3 (exePath, exeVerInfo)` { #embedExeVerInfo data-toc-label=embedExeVerInfo }



______

### **embedManifest**`#!py3 (exePath, manifestPath)` { #embedManifest data-toc-label=embedManifest }



______

### **endsWithPathPattern**`#!py3 (match, basePath=None)` { #endsWithPathPattern data-toc-label=endsWithPathPattern }



______

### **exists**`#!py3 (path)` { #exists data-toc-label=exists }

Test whether a path exists.  Returns False for broken symbolic links

______

### **extPathPattern**`#!py3 (ext, basePath=None)` { #extPathPattern data-toc-label=extPathPattern }



______

### **extractExeIcons**`#!py3 (srcExePath, destDirPath)` { #extractExeIcons data-toc-label=extractExeIcons }



______

### **getEnv**`#!py3 (varName, default=None)` { #getEnv data-toc-label=getEnv }



______

### **getPassword**`#!py3 (isGuiPrompt=False)` { #getPassword data-toc-label=getPassword }



______

### **halt**`#!py3 ()` { #halt data-toc-label=halt }



______

### **homePath**`#!py3 (relPath=None)` { #homePath data-toc-label=homePath }



______

### **importFromPath**`#!py3 (path, memberName=None)` { #importFromPath data-toc-label=importFromPath }



______

### **isDebug**`#!py3 ()` { #isDebug data-toc-label=isDebug }



______

### **isDir**`#!py3 (path)` { #isDir data-toc-label=isDir }



______

### **isFile**`#!py3 (path)` { #isFile data-toc-label=isFile }



______

### **isImportableFromModule**`#!py3 (moduleName, memberName)` { #isImportableFromModule data-toc-label=isImportableFromModule }



______

### **isImportableModule**`#!py3 (moduleName)` { #isImportableModule data-toc-label=isImportableModule }



______

### **isParentDir**`#!py3 (parent, child, basePath=None)` { #isParentDir data-toc-label=isParentDir }



______

### **joinExt**`#!py3 (rootName, extension=None)` { #joinExt data-toc-label=joinExt }



______

### **mergeDirs**`#!py3 (srcDirPaths, destDirPath, isRecursive=True)` { #mergeDirs data-toc-label=mergeDirs }



______

### **modulePackagePath**`#!py3 (moduleName)` { #modulePackagePath data-toc-label=modulePackagePath }



______

### **modulePath**`#!py3 (moduleName)` { #modulePath data-toc-label=modulePath }



______

### **move**`#!py3 (src, dst, copy_function=<function copy2 at 0x020EE858>)` { #move data-toc-label=move }

Recursively move a file or directory to another location. This is
similar to the Unix "mv" command. Return the file or directory's
destination.

If the destination is a directory or a symlink to a directory, the source
is moved inside the directory. The destination path must not already
exist.

If the destination already exists but is not a directory, it may be
overwritten depending on os.rename() semantics.

If the destination is on our current filesystem, then rename() is used.
Otherwise, src is copied to the destination and then removed. Symlinks are
recreated under the new name if os.rename() fails because of cross
filesystem renames.

The optional `copy_function` argument is a callable that will be used
to copy the source or it will be delegated to `copytree`.
By default, copy2() is used, but any function that supports the same
signature (like copy()) can be used.

A lot more could be done here...  A look at a mv.c shows a lot of
the issues this implementation glosses over.

______

### **moveToDesktop**`#!py3 (path)` { #moveToDesktop data-toc-label=moveToDesktop }



______

### **moveToDir**`#!py3 (srcPaths, destDirPath=None)` { #moveToDir data-toc-label=moveToDir }

Move files OR directories to a given destination.
The argument srcPaths may be a singular path (i.e. a string)
or an iterable (i.e. a list or tuple).  

______

### **moveToHomeDir**`#!py3 (path)` { #moveToHomeDir data-toc-label=moveToHomeDir }



______

### **normBinaryName**`#!py3 (path, isPathPreserved=False, isGui=False)` { #normBinaryName data-toc-label=normBinaryName }



______

### **normConfigName**`#!py3 (path, isPathPreserved=False)` { #normConfigName data-toc-label=normConfigName }



______

### **normIconName**`#!py3 (path, isPathPreserved=False)` { #normIconName data-toc-label=normIconName }



______

### **normLibName**`#!py3 (path, isPathPreserved=False)` { #normLibName data-toc-label=normLibName }



______

### **printErr**`#!py3 (msg, isFatal=False)` { #printErr data-toc-label=printErr }



______

### **printExc**`#!py3 (e, isDetailed=False, isFatal=False)` { #printExc data-toc-label=printExc }



______

### **removeFromDir**`#!py3 (subPaths, parentDirPath=None)` { #removeFromDir data-toc-label=removeFromDir }

Removes files OR directories from a given directory.
The argument subPaths may be a singular path (i.e. a string)
or an iterable collection (i.e. a list or tuple).  

______

### **renameInDir**`#!py3 (namePairs, parentDirPath=None)` { #renameInDir data-toc-label=renameInDir }

Renames files OR directories in a given destination.
The argument namePairs may be a singular tuple (oldName, newName)
or an iterable (i.e. a list or tuple) of such tuple pairs.  

______

### **reserveTempFilePath**`#!py3 (suffix='', isSplitRet=False)` { #reserveTempFilePath data-toc-label=reserveTempFilePath }



______

### **rootFileName**`#!py3 (path)` { #rootFileName data-toc-label=rootFileName }



______

### **run**`#!py3 (binPath, args=None, wrkDir=None, isElevated=False, isDebug=False, askpassPath=None)` { #run data-toc-label=run }



______

### **runPy**`#!py3 (pyPath, args=None, isElevated=False, askpassPath=None)` { #runPy data-toc-label=runPy }



______

### **setEnv**`#!py3 (varName, value)` { #setEnv data-toc-label=setEnv }



______

### **sitePackagePath**`#!py3 (packageName)` { #sitePackagePath data-toc-label=sitePackagePath }



______

### **startsWithPathPattern**`#!py3 (match, basePath=None)` { #startsWithPathPattern data-toc-label=startsWithPathPattern }



______

### **tempDirPath**`#!py3 ()` { #tempDirPath data-toc-label=tempDirPath }



______

### **toCabFile**`#!py3 (sourceDir, cabDest=None, removeScr=True, isWrapperDirIncluded=False)` { #toCabFile data-toc-label=toCabFile }



______

### **toNativePath**`#!py3 (path)` { #toNativePath data-toc-label=toNativePath }



______

### **toZipFile**`#!py3 (sourceDir, zipDest=None, removeScr=True, isWrapperDirIncluded=False)` { #toZipFile data-toc-label=toZipFile }



______

### **versionNo**`#!py3 (ver, parts=4, partLen=3)` { #versionNo data-toc-label=versionNo }



______

### **versionStr**`#!py3 (ver, parts=4)` { #versionStr data-toc-label=versionStr }



______

### **versionTuple**`#!py3 (ver, parts=4)` { #versionTuple data-toc-label=versionTuple }



______

