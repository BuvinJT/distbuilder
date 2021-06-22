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
off to selectively import them.  The first example project
[Hello World Example](Examples.md#hello-world-example), 
for instance, only needs two specific imports, and so it starts out
`from distbuilder import PyToBinPackageProcess, ConfigFactory`.      

Additionally, distbuilder may serve you well as a `setup.py` script,
which you run within a given development environment to install dependencies
and/or perform other initialization tasks for working on the project.
For more on this usage, refer to:

* [Library Installation](LowLevel.md#library-installation)

* [Module import utilities](LowLevel.md#module-import-utilities) 

* [download](LowLevel.md#download)

* [run](LowLevel.md#run)

## Getting Started

The easiest way for most people to learn how to use distbuilder is to step through
some [examples](Examples.md). Unfortunately, it is not practical to provide, and
describe, demonstrations of all of the library's features (and no reader would likely
wish to invest the time required for such an endeavor!) If you spend just 10 minutes
reviewing a handful of the ones provided, however, you should come away with a solid 
base from which start employing this tool.  

## Learn More  

For a more thorough explanation of how to use the 
library, continue on to [High Level Classes](HighLevel.md) next. 
Then, review [Configuration Classes](ConfigClasses.md#configuration-classes) 
and/or [Low Level Functions](LowLevel.md) for even more details.
