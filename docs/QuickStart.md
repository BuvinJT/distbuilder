# Quick Start Guide
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Pre-Requisites

### Pip

Both the distbuilder installation, and the use of some features within it, require [pip](https://docs.python.org/3/installing/index.html).  More than likley, you already have that installed.  If not, note that installation process may be slightly different based on your platform or environmental details (e.g. having multiple Python installations).  The scope of such matters is beyond what can be addressed here.  Refer to these links as a starting point: 

[Pip on Windows](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)

[Pip on Mac](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)

[Pip on Linux](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

### Opy

This library requires a fork from the open source project 
"Opy", dubbed "Opy for Distribution Builder". When installing 
distbuilder, this dependency should be **automatically installed**
for you. To aquire the source for that directly, and manually install
it, you may use the links/urls below:  

[Opy for Distribution Builder](https://github.com/QQuick/Opy/tree/opy_distbuilder)  

Or, via the direct git clone url:

`https://github.com/QQuick/Opy.git`
	
BRANCH: opy_distbuilder
	
The most recent (development) commits, however, are 
accessible via:   

`https://github.com/BuvinJT/Opy.git`		

### Qt Installer Framework (Optional / Recommended) 

Additionally, the "Qt Installer Framework"
is recommended.  This component is not a hard
requirement, but is *strongly recommended*, so 
that you may employ the distbuilder installer
creation features.

QtIFW can be acquired from: [QtIFW Downloads](http://download.qt.io/official_releases/qt-installer-framework)

Once installed, the best way to integrate it 
with distbuilder is to define an environmental
variable name `QT_IFW_DIR` and the set value
for that equal to the directory where you 
installed the utility. Note, it also possible to
supply the path within your implemenation script. 
Refer to the [Installers](Reference.md#installers) section of 
the Reference Manual for details. 
      
## Installation 

Standard installation is as simple as executing the following 
on your terminal / command prompt: 

	python -m pip install distbuilder

To install from the raw source instead, you may perform a 
Git clone from `https://github.com/BuvinJT/distbuilder.git`, 
or otherwise download the repository from the 
[GitHub](https://github.com/BuvinJT/distbuilder) page.

With a local copy of the full source, on Windows you may 
simply run `install.bat` (or `install3.bat`). 
On Mac or Linux, you may use the counterpart `install.sh` 
(or `install3.sh`) instead.

If you encounter failures with those scripts, try
this "manual" approach. From a command line interface, 
change to the directory containing the source, then execute:

	python -m pip install .

    (Don't miss the period at the end!)

## Implementation Overview

The standard way the library was intended for use is to
add a `build.py` script to the root directory of the
project you wish to distribute. (Note: the file may have 
any name of your choice - "build.py" is merely a 
recommended naming convention).  After defining that 
script, you simply run it to build your distribution package. 

In `build.py`, you may wish to import everything 
from this library via `import distbuilder *`.  If 
your build script will use the "low level functions" offered 
by the library, starting it in that manner is often a 
convenient choice.  If you will only be employing the 
most high level classes and functions, you may be better 
off to selectively import them.  The example project, 
for instance, starts out
`from distbuilder import PyToBinInstallerProcess, ConfigFactory`.      

## Basic Example

*Note: This example requires the standard Python [TKinter](https://tkdocs.com/tutorial/install.html) 
library	be installed.*

The easiest way learn how to use distbuilder is likely 
to reference an example.  The "Hello World Tk Example" 
is included in the "source distribution" of the library.
You may visit the [PyPi](https://pypi.org/project/distbuilder/#files) 
downloads page for the project to acquire this in the form of a tarball.

Alternatively, you may download/copy these example files directly from GitHub into a local directory:   

Example app: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/hello.py)

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/build.py)

Windows resource: [demo.ico](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.ico)

Mac resource: [demo.icns](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.icns)

Linux resource: [demo.png](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.png)

Start by confirming you can run the program 
script in the "natural" manner:

	python hello.py

Assuming that works, run the build script to achieve the following:

- obfuscate the code
- convert the obfuscation to a stand-alone executable
- build an installer with the executable bundled into it
- move the installer to your desktop (for convenience)
- launch it (for testing)
 
Simply execute the following:

	python build.py
	
Proceed through the installer, and then run the program	
to confirm it works.  

Having witnessed everything function, now review the 
`build.py` script.  It should be fairly
self-explanatory for a moderately seasoned Python 
developer.  The script is a simple example, but 
covers a good portion of the major distbuilder 
features so as to provide a feel for what it does, 
and how it works.

Note: The most astute observer may notice (on most platforms) 
that the stdout/err messages are not produced on the terminal
by the binary version of the example (as they are normally seen by 
clicking the "Hello Tkinter" button when run the raw .py script). 
This is caused by a feature of PyInstaller, to "swallow" console 
messages produced by gui applications and/or by additional platform
details regarding standard output streams. This may be highly
counterproductive for debugging, and as such distbuilder has included
a direct solution for this issue. Refer to the 
[Testing](Reference.md#testing) section of the 
Reference Manual for more details.    

## Learn More  

For a more thorough explanation for how to use
the library, refer to the [Reference Manual](Reference.md).
