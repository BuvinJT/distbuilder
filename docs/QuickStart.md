# Quick Start Guide
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Installation 

### Easy installation (via pip)

Depending upon your computer's configuration, installation may be as simple 
as executing the following on your terminal / command prompt:

	pip install distbuilder

Alternatively, you might need to use the "long version" of that:  

	python -m pip install distbuilder
 
Within some environments, it may necessary to run pip installations
with elevated privileges, e.g. by prefixing the command with `sudo`.

### From source installation

To install from the raw source instead (useful if you want a 
"cutting edge" alpha release), you may perform a Git clone from 
`https://github.com/BuvinJT/distbuilder.git`, 
or otherwise download the repository in a "flat" manner 
from the [GitHub Page](https://github.com/BuvinJT/distbuilder).
You may also visit the [PyPi downloads](https://pypi.org/project/distbuilder/#files) 
page for this project to instantly acquire an official release in the form 
of a tarball.

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
More than likley, you already have that installed.  If not, note that the installation 
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
      
## Implementation Overview

The "standard" way distbuilder is intended to be used is by
adding a `build.py` script to the root directory of the
project you wish to distribute. (Note: the file may have 
any name of your choice - "build.py" is merely a 
recommended naming convention).  After defining that 
script, you simply run it to build your distribution package. 

In `build.py`, you may wish to import everything 
from this library via `import distbuilder *`.  If 
your build script will use a large collection of the 
"low level functions" offered by the library, starting it 
in that manner is often a convenient choice.  If you will only 
be employing the high level classes and functions, you may be better 
off to selectively import them.  The first example project, 
for instance, only needs two specific imports, and so it starts out
`from distbuilder import PyToBinPackageProcess, ConfigFactory`.      

## Getting Started

The easiest way for most people to learn how to use distbuilder is to view
an example.  All of the examples discussed here are included in the
"source distribution" of the library. The [PyPi downloads](https://pypi.org/project/distbuilder/#files) 
page for this project is arguably the fastest route to acquire the examples.
See [From source installation](#from-source-installation) for other means
of achieving this.

## Hello World Example

The Hello World Example is a demonstration of using the 
[PyToBinPackageProcess](HighLevel.md#pytobinpackageprocess) class. 
This is one of the most straightforward, and typical use cases for the library.  

If you did not download the full source for the library (inclusive of the examples) 
you may download/copy the following individual files directly from GitHub into a local directory. 
It is recommended that you place them in a directory named `hello_world`.   

- Example program: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/hello.py)
- Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/build.py)
- Example resource: [LICENSE](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/LICENSE)

Start by confirming you can run the program script in the "natural" manner:

	python hello.py

Don't expect it to do much...  It simply writes "Hello World!" to the console.

Now, run the build script:

    python build.py

The build script should achieve the following:

- converts the Python script to a stand-alone executable binary
- bundles the example resource (license file) into a directory with the binary
- compresses the distribution into a simple zip file (left in the same directory as the source)
	
Having witnessed that function, review the [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/build.py)
 script for yourself.  It should be self-explanatory for a moderately 
 seasoned Python developer.  

## Hello World Tk Example

This next example is a more comprehensive version of the first Hello World.
It is a demonstration of using the 
[PyToBinInstallerProcess](HighLevel.md#pytobininstallerprocess) class.

*Note: This example requires the standard Python [TKinter](https://tkdocs.com/tutorial/install.html) 
library	be installed.*

You may download/copy the following individual files directly from GitHub into a local directory.  
It is recommended that you place them in a directory named `hello_world_tk`.   

- Example app: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/hello.py)
- Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/build.py)
- Windows resource: [demo.ico](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.ico)
- Mac resource: [demo.icns](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.icns)
- Linux resource: [demo.png](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.png)

Start by confirming you can run the program script in the "natural" manner:

	python hello.py
	
The program is a single button GUI. Clicking the button writes "Hello World!" 
to the console. 

Now, run the build script:

    python build.py
    
The build script should achieve the following:

- obfuscates the code (to mitigate the risk of reverse engineering) 
- converts the obfuscated version of the source to a stand-alone executable
- builds a full installer with the executable bundled into it
- moves the installer to your desktop (for convenience)
- launches the installer (for testing)
	
Proceed through the installer, and then run the program	
to confirm it works.  

Having witnessed everything function, review the 
[build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/build.py) 
script. The script is a simple example, but covers a good portion of the 
"core" distbuilder features.

### Extended feature demo: "debug mode"

Here is a good place to illustrate one very useful extended feature of this library,
which may prove immeaditely valuable to you.  This is will also help you to understand
a common pattern for using some of the primary distbuilder classes. 

Locate the following commented out line in the Hello World Tk build script:

    #def onPyPackageProcess( self, prc ): prc.isTestingExe = True

Uncomment that, and run the build process again.  In the 
middle of the process, the standalone binary will be run 
for you in "debug" mode.  Upon closing the program, the 
rest of the build process will continue.  

This code demonstrates a design pattern employed by the "high level" 
process classes in distbuilder.  That pattern is for a high level 
class to generate a "configuration object", or a lower level "process 
object", automatically set it up for the client implementation,
and then "pass it through" an overridable function where you may
access such and revise it for your own needs prior to its use.  

So, what's the point of setting `prc.isTestingExe = True` ?
If you have run this example program, the most astute observer may notice 
(on Windows or Mac, but not Linux...) 
that the stdout/err messages (seen by clicking the "Hello Tkinter" 
button when running the raw .py script) are not produced on the terminal
by the *standalone version* of the program when it is launched in the 
normal manner.  That is due to a feature of PyInstaller (and/or by additional platform
details regarding standard output streams) to "swallow" console 
messages produced by gui applications. That may be desired behavior for a 
public release, but it may be also be highly counterproductive for debugging, 
since there are times when the standalone version may require specialized
coding to make it work correctly in that context compared to how it did as a 
basic .py script. As such, distbuilder has included a solution for this, as 
demonstrated here. Refer to [Testing](LowLevel.md#testing) for more details.    

## Hello Silent Example

It is another demonstration of using the 
[PyToBinInstallerProcess](HighLevel.md#pytobininstallerprocess) class.

Hello Silent demonstrates how one can use distbuilder to build "silent" installers. 
These do not require user interactions for them to complete their tasks.  Instead, 
they run automatically, while having the same flexible options present in the gui 
installers made available via command line arguments.

"Silent" installers built by distbuilder provide a very important additional feature.  
They are able to be run in **non-gui contexts**, such as on "headless servers".
Silent installers are, of course, also desirable (on any platform) for mass 
installation purposes such as when a network administrator needs to install the 
same program on countless workstations. 

Building a silent installer requires nothing more than setting the 
`isSilentSetup` configuration option to `True`.  As such, you can easily define a 
full blown packaging and installation process that could be run in Windows (for example) 
using an interactive graphical interface, AND could also be used on a CentOS server 
(for example), with nothing but a terminal interface available. 
You would only have to toggle the `isSilentSetup` option before running the build script!

This example expects that you already downloaded the first example 
(Hello World). That must be present in the testing environment within a directory 
adjacent to where you place the next file.  That first directory must be 
named `hello_world` for this "master" script (which draws upon that) to function.

You may download/copy the example file directly from GitHub 
(into a `hello_silent` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_silent/build.py)

Upon building the silent installer, the demo is set to test "Auto Installation" of it. 
With that enabled, it will run the installer with the command line argument to 
"force installation". If run more than once, that option will cause it to uninstall 
any prior existing installation rather than exiting with an error, as it would do
by default when a conflict was detected.

For more information, refer to [Silent Installers](LowLevel.md#silent-installers).

## Hello Packages Example

The Hello Packages Example is a demonstration of using the 
[RobustInstallerProcess](HighLevel.md#robustinstallerprocess) class.
It demonstrates a way that you can generate and then "combine" multiple 
"packages" into a single installer with a single build process.
In this case, those become separate components which may be 
installed *selectively* by the end user. 

This example requires that both of the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place the next file.
Those first two must be named `hello_world` and `hello_world_tk` for this
"master" script to function.

You may download/copy the example file directly from GitHub 
(into a `hello_packages` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_packages/build.py)

## Hello Merge Example

This is another demonstration of using the 
[RobustInstallerProcess](HighLevel.md#robust-installer-process) class.

Similar to the Hello Packages Example, Hello Merge demonstrates 
how you can "merge" multiple "packages" into a *single package* within
an installer.  The content of the two programs, which worked independently,
become one component which may *NOT* be installed selectively by the user. 

This example requires that both of the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place the next file.
Those first two must be named `hello_world` and `hello_world_tk` for this
"master" script to function.

You may download/copy the example file directly from GitHub 
(into a `hello_merge` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_merge/build.py)

## Learn More  

For a more thorough explanation of how to use the 
library, continue on to [High Level Classes](HighLevel.md) next. 
Then, review [Configuration Classes](ConfigClasses.md#configuration-classes) 
and/or [Low Level Classes And Functions](LowLevel.md) for even more 
details.
