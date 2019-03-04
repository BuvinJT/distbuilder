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
for you. To acquire the source for that directly, and manually install
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
supply the path within your implementation script. 
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
your build script will use a collection of the 
"low level functions" offered by the library, starting it 
in that manner is often a convenient choice.  If you will only 
be employing the high level classes and functions, you may be better 
off to selectively import them.  The first example project, 
for instance, only needs two specific imports, and so it starts out
`from distbuilder import PyToBinPackageProcess, ConfigFactory`.      

## Getting Started

The easiest way learn how to use distbuilder is likely 
to reference an example.  The all of the examples 
are included in the "source distribution" of the library.
You may visit the [PyPi](https://pypi.org/project/distbuilder/#files) 
downloads page for the project to acquire this in the form of a tarball.
That's arguably the fastest route if you plan to step through each
example.

## Hello World Example

The Hello World Example is a demonstration of using the `PyToBinPackageProcess`
class. This is one of most straightforward, and typical use cases for the library.  

If you did not download the full source for the library, incluive of the examples, 
you may download/copy the following example files directly from 
GitHub into a local directory.  It is recommended that you place them in a directory
named `hello_world`.   

Example program: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/hello.py)

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/build.py)

Example resource: [LICENSE](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/LICENSE)

Start by confirming you can run the program script in the "natural" manner:

	python hello.py

It doesn't do much.  It simply writes "Hello World!" to the console.
Now, run the build script to achieve the following:

- convert the python script to a stand-alone executable binary
- bundle the example resource (license file) into a directory with the binary
- compress the distribution into a zip file
 
Simply execute the following:

	python build.py
	
Having witnessed that function, now review the 
`build.py` script.  It should be fairly
self-explanatory for a moderately seasoned Python 
developer.  

## Hello World Tk Example

This next example is a more comprehensive version of the first Hello World.

*Note: This example requires the standard Python [TKinter](https://tkdocs.com/tutorial/install.html) 
library	be installed.*

You may download/copy the following example files directly from 
GitHub into a local directory.  It is recommended that you place them in a directory
named `hello_world_tk`.   

Example app: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/hello.py)

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/build.py)

Windows resource: [demo.ico](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.ico)

Mac resource: [demo.icns](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.icns)

Linux resource: [demo.png](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.png)

Start by confirming you can run the program 
script in the "natural" manner:

	python hello.py
	
The program is a single button GUI. Clicking the button writes "Hello World!" 
to the console. 

Run the build script to achieve the following:

- obfuscate the code (to mitigate the risk of reverse engineering) 
- convert the obfuscation to a stand-alone executable
- build an installer with the executable bundled into it
- move the installer to your desktop (for convenience)
- launch it (for testing)
 
Simply execute the following:

	python build.py
	
Proceed through the installer, and then run the program	
to confirm it works.  

Having witnessed everything function, now review the 
`build.py` script. The script is a simple example, but 
covers a good portion of the "core" distbuilder 
features.

Note: The most astute observer may notice (on most platforms) 
that the stdout/err messages are not produced on the terminal
by the binary version of the example (as they are normally seen by 
clicking the "Hello Tkinter" button when run the raw .py script). 
This is caused by a feature of PyInstaller, to "swallow" console 
messages produced by gui applications and/or by additional platform
details regarding standard output streams. This may be highly
counterproductive for debugging, and as such distbuilder has included
a direct solution for this issue. Refer to [Testing](LowLevel.md#testing)
for more details.    

## Hello Packages Example

The Hello Packages Example demonstrates one way that you can generate
and then "combine" multiple "packages" into a single installer with a single
build process.  In this case, those become separate components which may be 
installed selectively by the user. 

This example requires that the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place these files.
Those first two must be named `hello_world` and `hello_world_tk`.

You may download/copy these example files directly from GitHub 
(into a `hello_packages` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_packages/build.py)

## Hello Merge Example

Similar to the Hello Packages Example,  Hello Merge demonstrates 
how you can "merge" multiple "packages" into a single package within
an installer.  The content of the two programs, which worked independently,  
become one component which may NOT be installed selectively by the user. 

This example also requires that the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place these files.
Those first two must be named `hello_world` and `hello_world_tk`.

You may download/copy these example files directly from GitHub 
(into a `hello_merge` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_merge/build.py)

## Learn More  

For a more thorough explanation of how to use the 
library, refer to [High Level Classes](HighLevel.md) and then
[Low Level Classes And Functions](LowLevel.md).
