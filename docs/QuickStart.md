# Quick Start Guide
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Installation 

### Easy installation (via PIP)

Standard installation should be as simple as executing the following 
on your terminal / command prompt: 

	python -m pip install distbuilder

Or, based upon your environment, even just:

	pip install distbuilder

Within some environments, you may need to run the installation
with elevated rights, e.g. by prefixing the command with `sudo`.

### From source installation

To install from the raw source instead (useful if you want a 
cutting edge alpha release), you may perform a Git clone from 
`https://github.com/BuvinJT/distbuilder.git`, 
or otherwise download the repository in a "flat" manner 
from the [GitHub](https://github.com/BuvinJT/distbuilder) page.

With a local copy of the full source, on Windows you may be able
to simply run `install.bat` (or `install3.bat`). 
On Mac or Linux, you may use the counterpart `install.sh` 
(or `install3.sh`) instead.

If you encounter failures with those scripts, you probably need to 
tweak them slightly for your environment.  Before attempting that, 
however, try this "manual" approach. From a command line interface, 
change to the directory containing the source, then execute:

	python -m pip install .

    (Don't miss the period at the end!)

## Pre-Requisites

### Pip

Both the distbuilder installation, and the use of *some features within it*, 
require [pip](https://docs.python.org/3/installing/index.html). 
More than likley, you already have that installed.  If not, note that the installation 
process may be slightly different based on your platform or environmental details 
(e.g. having multiple Python installations).  The scope of such matters is beyond what 
can be addressed here.  Refer to these links as a starting point: 

[Pip on Windows](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)

[Pip on Mac](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)

[Pip on Linux](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

### Opy

The distbuilder library requires a fork from the open source project 
"Opy", dubbed "Opy for Distribution Builder". When installing 
distbuilder, this dependency should be **automatically installed**
for you. To acquire the source for that directly, and manually install
it instead, you may use the links/urls below:  

[Opy for Distribution Builder](https://github.com/QQuick/Opy/tree/opy_distbuilder)  

Or, via the direct git clone url:

`https://github.com/QQuick/Opy.git`
	
BRANCH: opy_distbuilder
	
The most recent (development) commits, however, are 
accessible via:   

`https://github.com/BuvinJT/Opy.git`		

### Qt Installer Framework (optional / recommended) 

Additionally, the "Qt Installer Framework"
is recommended.  This component is not a hard
requirement, but is *strongly recommended*, so 
that you may employ the distbuilder installer
creation features.

When you use the distbuilder features that require 
this external utility, it will be **automatically installed** 
for you, if it is not already present on the system (or 
cannot be found).

If desired, you may also manually install it. 
Installation and uninstallation can, in fact, be accomplished
with functions provided by distbuilder. (Refer to 
[Installers](LowLevel.md#installers) for details.)

Alternatively, QtIFW can be directly acquired from: 
[QtIFW Downloads](http://download.qt.io/official_releases/qt-installer-framework)

Once manually installed, the best way to integrate it 
with distbuilder is to define an environmental
variable named `QT_IFW_DIR` and the set value
for that equal to the directory where you 
installed the utility. Note, it also possible to
supply the path within your implementation script. 
Again, refer to [Installers](LowLevel.md#installers) 
for more details on such. 
      
## Implementation Overview

The standard way the library is intended to be used is by
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

The easiest way learn how to use distbuilder is likely 
to review an example.  The all of the examples discussed here are 
included in the "source distribution" of the library.
You may visit the [PyPi](https://pypi.org/project/distbuilder/#files) 
downloads page for the project to acquire this in the form of a tarball.
That's arguably the fastest route if you plan to step through each
example.

## Hello World Example

The Hello World Example is a demonstration of using the `PyToBinPackageProcess`
class. This is one of most straightforward, and typical use cases for the library.  

If you did not download the full source for the library (inclusive of the examples) 
you may download/copy the following files directly from GitHub into a local directory.  
It is recommended that you place them in a directory named `hello_world`.   

Example program: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/hello.py)

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/build.py)

Example resource: [LICENSE](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world/LICENSE)

Start by confirming you can run the program script in the "natural" manner:

	python hello.py

It doesn't do much...  It simply writes "Hello World!" to the console.

Now, run the build script:

    python build.py

The build script should achieve the following:

- converts the Python script to a stand-alone executable binary
- bundles the example resource (license file) into a directory with the binary
- compresses the distribution into a simple zip file (left in the same directory as the source)
	
Having witnessed that function, review the `build.py` script for yourself.  It should be 
self-explanatory for a moderately seasoned Python developer.  

## Hello World Tk Example

This next example is a more comprehensive version of the first Hello World.

*Note: This example requires the standard Python [TKinter](https://tkdocs.com/tutorial/install.html) 
library	be installed.*

You may download/copy the following example files directly from GitHub into a local directory.  
It is recommended that you place them in a directory named `hello_world_tk`.   

Example app: [hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/hello.py)

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/build.py)

Windows resource: [demo.ico](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.ico)

Mac resource: [demo.icns](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.icns)

Linux resource: [demo.png](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.png)

Start by confirming you can run the program script in the "natural" manner:

	python hello.py
	
The program is a single button GUI. Clicking the button writes "Hello World!" 
to the console. 

Now, run the build script:

    python build.py
    
The build script should achieve the following:

- obfuscates the code (to mitigate the risk of reverse engineering) 
- converts the obfuscation to a stand-alone executable
- builds a full installer with the executable bundled into it
- moves the installer to your desktop (for convenience)
- launches the installer (for testing)
	
Proceed through the installer, and then run the program	
to confirm it works.  

Having witnessed everything function, review the 
`build.py` script. The script is a simple example, but 
covers a good portion of the "core" distbuilder 
features.

### Extended feature demo: "debug mode"

Now, locate the following commented out line in the Hello World Tk build script:

    #def onPyPackageProcess( self, prc ): prc.isTestingExe = True

Uncomment that, and run the build process again.  In the 
middle of the process, the standalone binary will be run 
for you in "debug" mode.  Upon closing the program, the 
rest of the build process will continue.

The most astute observer may notice (on Windows or Mac) 
that the stdout/err messages (seen by clicking the "Hello Tkinter" 
button when running the raw .py script) are not produced on the terminal
by the standalone version of the program when it is launched in the 
normal manner.  That is due to a feature of PyInstaller (and/or by additional platform
details regarding standard output streams) to "swallow" console 
messages produced by gui applications. That may be desired behavior for a 
public release, but it may be also be highly counterproductive for debugging, 
since there are times when the stand-alone version may require specialized
coding to make it work correctly in that context vs as a basic .py script. 
As such, distbuilder has included a solution for this, as demonstrated here. 
Refer to [Testing](LowLevel.md#testing) for more details.    

## Hello Packages Example

The Hello Packages Example demonstrates one way that you can generate
and then "combine" multiple "packages" into a single installer with a single
build process.  In this case, those become separate components which may be 
installed selectively by the user. 

This example requires that the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place the next file.
Those first two must be named `hello_world` and `hello_world_tk` for this
"master" script to function.

You may download/copy the example file directly from GitHub 
(into a `hello_packages` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_packages/build.py)

## Hello Merge Example

Similar to the Hello Packages Example, Hello Merge demonstrates 
how you can "merge" multiple "packages" into a single package within
an installer.  The content of the two programs, which worked independently,  
become one component which may NOT be installed selectively by the user. 

This example also requires that the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place the next file.
Those first two must be named `hello_world` and `hello_world_tk` for this
"master" script to function.

You may download/copy the example file directly from GitHub 
(into a `hello_merge` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_merge/build.py)

## Hello Silent Example

Hello Silent demonstrates how one can build "silent" installers, which do not
require user interactions for them to complete their tasks.  Instead, they run
automatically, while having the same flexible installation options made available
via command line arguments provided at the time they are launched.

"Silent" installers built by distbuilder provide a very important additional feature
implicitly.  Such are able to be run in **non-gui contexts**, such as on "headless servers".
Silent installers are also, of course, desirable for mass installation purposes
such as when a network administrator needs to install the same program on countless 
workstations for which they are responsible. 

Building a silent installer requires nothing more than setting the `isSilent` configuration
option to `True`.  As such, you can easily define a full blown packaging and installation
process that could be run in Windows (for example) using an interactive graphical interface,
AND could also be used on a CentOS server (for example), with nothing but a terminal interface
available.  Just toggle the isSilent option in the build script!

This example is akin to Hello Packages and Hello Merge, in that it expects you already 
downloaded and ran the first example (Hello World). That must be present in the testing 
environment within a directory adjacent to where you place the next file.
The first directory must be named `hello_world` for this "master" script to function.

You may download/copy the example file directly from GitHub 
(into a `hello_silent` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_silent/build.py)

Upon building the silent installer, the demo is set to test "Auto Installation" of it. With that enabled, it will
automatically passing the command line argument to "force installation".  Running the installer with that option
will cause it to uninstall and existing installation (if encountered) rather than exiting with an error, as is 
the default behavior.

Refer to [Installers](LowLevel.md#installers) for more details on silent installers.

## Learn More  

For a more thorough explanation of how to use the 
library, refer to [High Level Classes](HighLevel.md) and then
[Low Level Classes And Functions](LowLevel.md).
