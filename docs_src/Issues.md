# Troubleshooting
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Tested Against

Python:  

* 2.7  
* 3.5  
* 3.7  
* 3.8
  
Windows:    

* 7
* 8.0  
* 10

macOS:    

* Sierra  
* Mojave

Linux:   

* Ubuntu 16.04  
* Ubuntu 18.04  
* CentOS 7.6 (minimal)

OS Language:  

* English  

PyInstaller:  

* 2.1
* 3.4
* 4.0
* Binary / Script

Qt Installer Framework:  

* 2.0.5
* 3.0.6
* 3.1.1
* 3.2.2        

Pip:  

* 8.x  
* 18.x  
* 19.x  
* 20.x

Opy distbuilder:  

* 0.9+  

Qt C++ Integration:

* Qt 5.8
* Qt 5.14
* MSVC
* MinGW
* Clang
* GCC/G++

## Installation Help

### Problems with Pip

- If a simple `pip` command is not working for you, you may need to use the "long version" of that command:  

```
python -m pip install distbuilder
```
 
- Within some environments, it may be necessary to run pip installations with **elevated privileges**, e.g. by prefixing the command with `sudo`.

### From source installation

To install the library from the raw source  (useful if you want a 
"cutting edge" alpha release!), you may perform a Git clone from 
`https://github.com/BuvinJT/distbuilder.git`, 
or otherwise download the repository in a "flat" manner 
from the [GitHub Page](https://github.com/BuvinJT/distbuilder).
You may also visit the [PyPi downloads](https://pypi.org/project/distbuilder/#files) 
page for this project to acquire the tarball of an "official release" .

With a local copy of the full source, on Windows you may be able
to simply run `install.bat` (or `install3.bat`). 
On Mac or Linux, you may use the counterpart `install.sh` 
(or `install3.sh`) instead.  Those scripts are found in the repo's
root.

If you encounter failures with those scripts, you probably need to 
tweak them slightly for your environment.  Before attempting that, 
however, try this "manual" approach. From a command line interface, 
change to the directory containing the source, then execute:

	python -m pip install .

    (Don't miss the period at the end!)

## Pre-Requisites

### Python 2.7 or Newer

If you don't have [Python](https://www.python.org/) installed, you'll 
need to start there!

While it *may* be possible to run distbuilder on versions of Python predating v.2.7,  
this is not a supported condition. It recommended that you use v.3.x if possible, since
Python 2 is now officially "dead" to begin with... 

### Pip

Both the distbuilder installation, and the use of *some features within it*, 
require [pip](https://docs.python.org/3/installing/index.html). 
More than likely, you already have that installed.  If not, note that the installation 
process may be slightly different based on your platform or environmental details 
(e.g. having multiple Python installations).  The scope of such matters is beyond what 
can be addressed here.  Refer to these links as a starting point: 

- [Pip on Windows](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
- [Pip on Mac](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)
- [Pip on Linux](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

### Opy

The distbuilder library requires a *fork* from the open source project 
"Opy", dubbed "**Opy for Distribution Builder**". When installing 
distbuilder, this dependency should be **automatically installed**
for you. To acquire the source for that directly, and manually install
it instead, you may use the links/urls below:  

[Opy for Distribution Builder](https://github.com/QQuick/Opy/tree/opy_distbuilder)  

Or, via the direct git clone url:

`https://github.com/QQuick/Opy.git`
	
BRANCH: opy_distbuilder
	
The most recent (development) commits, however, are 
accessible from the development [GitHub Page](https://github.com/BuvinJT/Opy)
or directly via git using:   

`https://github.com/BuvinJT/Opy.git`		

### Qt Installer Framework (optional / recommended) 

Additionally, the "Qt Installer Framework"
is a conditional dependency.  This component is not a hard
requirement, but is *strongly recommended*, so 
that you may employ the installer creating features
offered by distbuilder.

When you use the library's features which require 
this external utility, it will be **automatically installed** 
for you, if it is not already present on the system (or 
cannot be found).

If desired, you may also manually install it. 
Installation and uninstallation can, in fact, be accomplished
with functions provided by distbuilder. (Refer to 
[installQtIfw](LowLevel.md#installqtifw) / [unInstallQtIfw](LowLevel.md#uninstallqtifw)
for details.)

Alternatively, QtIFW can be directly acquired from: 
[QtIFW downloads](http://download.qt.io/official_releases/qt-installer-framework)

If manually installed, the "best" way to integrate it 
with distbuilder is to define an environmental
variable named `QT_IFW_DIR` and the set value
for that equal to the directory where you 
installed the utility. See [QtIFW issues](Issues.md#qt-installer-framework-issues) 
if you require help with that.  Note, it also possible to
supply the path within your implementation script. 
Refer to [QtIfwConfig](ConfigClasses.md#qtifwconfig)
or [buildInstaller](LowLevel.md#buildinstaller) for more details. 



## Binary launching runtime issues

### Relative resources

If your application uses "relative resources" (e.g. images, etc. packaged
with it external to the binary), you may encounter problems with such
based on the context in which your application is launched.

Perhaps the easiest solution to this may be to "force" the work directory 
prior to launching the program.  That can be accomplished via a "wrapper script"
around the binary. See [pkgExeWrapperScript](HighLevel.md#pkgexewrapperscript) 
and [ExecutableScript](LowLevel.md#executablescript) for help adding this
"quick fix".

Here is a better solution... Rather than depending upon the current working 
directory being set to your's program's location before it is started, you could
acquire the directory path programmatically, and then resolving your 
relative paths to ones which are absolute.  

In Python, you could use a function such as this `absPath` example.  
(Note, the `THIS_DIR` assignment shown here is valid in both a script and 
binary (i.e. "frozen") context.)

    import os, sys
	
    THIS_DIR = os.path.dirname( os.path.realpath( sys.argv[0] ) )    
    
    def absPath( relativePath ):    
        return os.path.normpath( os.path.join( THIS_DIR, relativePath ) )

Unfortunately, in some situations, that preferred approach would take a great deal
of effort to apply . In which case, yet another approach could be taken, which 
resembles the "wrapper script" concept, but is built into your program itself.
Just set the working directory when the program is launched, for inside of, and then
set it back to what it was upon exit.

Python example:

	import os, sys
	
	THIS_DIR = os.path.dirname( os.path.realpath( sys.argv[0] ) )    
	
	__INIT_DIR = None
	def normalizeWorkDir() :
	    global __INIT_DIR
	    __INIT_DIR = os.curdir
	    os.chdir( THIS_DIR )
	
	def restoreWorkDir() :
	    if __INIT_DIR : os.chdir( __INIT_DIR )
	
Example use of the above functions, to place in your "entry point":
	
	if __name__ == "__main__":
	    normalizeWorkDir()
	    launchApp()
	    restoreWorkDir()

### Crash / failure with no debugging info

If a (gui) PyInstaller built application fails,
and you are seeking debugging info, refer to the 
[Testing](Reference.md#testing) section of the 
Reference Manual for more details on viewing such.    

## Qt Installer Framework issues

### Setting `QT_IFW_DIR` 

To use the Qt Installer Framework integration (manually), it is 
recommended to you set the `QT_IFW_DIR` environmental 
variable on a *permanent* (non-volatile) basis (so it
doesn't have to set every time you want to use it). This 
method makes your build script portable across platforms and 
on all your project collaborator's machines.  If that proves
to be difficult, however, you may set that within the script.   
Refer to the [Installers](Reference.md#installers) section of 
the Reference Manual for details. 

Setting environmental variables is beyond the scope of this document,
but here some places to start looking for help.  

[Windows variables](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10)

[macOS variables](https://stackoverflow.com/questions/135688/setting-environment-variables-on-os-x)

[Ubuntu variables](https://askubuntu.com/questions/58814/how-do-i-add-environment-variables)

### Launch App at end of install failures

If the application appears to run in every other context, except
when launched at the end of the Qt installer, a likely
reason is that working directory is incorrect when it is 
executed. This library attempts to set the working
directory for any program to the location where it resides
implicitly.  QtIFW, however, does not currently support setting
the working directory as a "RunProgram" directive.
A feature request for this was filed with Qt (long ago):

https://bugreports.qt.io/browse/QTIFW-217

For now, while there are various potential solutions to this, 
the *best* one is arguably to resolve this directly within your program.  
See [Relative resources](relative-resources) for more help. 

If Qt does not finally resolve this themselves sometime in 
an upcoming IFW release, then distbuilder will provide a built-in
work around.  Note, this is also a known issue on macOS, when launching 
via symbolic links added to Applications or the desktop.  That is NOT
a problem via Windows shortcuts or Linux desktops entries.

### Windows 8 (and earlier?): Crash at end of install

Recent versions of QtIFW have been observed to crash at the 
end of the installation on Windows 8.  This bug has been 
reported to Qt and they appear to be actively patching it.

https://bugreports.qt.io/browse/QTIFW-1248

The current work around is to directly launch the installer 
with elevated privileges (i.e as an administrator) on this
version of Windows.

### Linux sudo password not accepted

It has been observed that sometimes the sudo password is
not accepted by the installer when it prompts for it. The
contexts and details have yet to be narrowed down.

The current work around is to directly launch the installer 
with elevated privileges (i.e as root / sudo) if you encounter
this (inconsistent/odd) behavior.

## Get Help 

Refer to [Post An Issue](Contribute.md#post-an-issue).
