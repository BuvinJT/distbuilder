# Quick Start Guide
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/distbuilder128.png)

## Pre-Requisites

### Opy

This library requires a fork from the open source project 
"Opy", dubbed "Opy for Distribution Builder". When installing 
distbuilder via the "natural" method of using `pip`, this 
dependency will be **automatically installed**. If using an 
alternate, less automated method, that library can be 
acquired instead from: 

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
requirement, but is strongly recommended, so 
that you may employ the distbuilder installation
building features.

QtIFW can be acquired from: [QtIFW Downloads](http://download.qt.io/official_releases/qt-installer-framework)

Once installed, the best way to integrate it 
with distbuilder is to define an environmental
variable name `QT_IFW_DIR` and the set value
for that equal to the directory where you 
installed the utility. Refer to the 
[Installers](Reference.md#installers) section of 
the [Reference Manual](Reference.md#installers) for 
more details. 
      
## Installation 

Normally, installation is as simple as executing the following 
on your terminal / command prompt: 

	pip install distbuilder

To install from the raw source instead, you may perform a 
Git clone from `https://github.com/BuvinJT/distbuilder.git`, 
or otherwise download the repository from the 
[GitHub](https://github.com/BuvinJT/distbuilder) page.


With you local copy of the source, on Windows you may 
simply run `install.bat` (or `install3.bat`). 
On Mac or Linux, you may use the counterpart `install.sh` 
(or `install3.sh`) instead.

If you encounter failures with those scripts, try
this "manual" approach. From a command line interface, 
change to the directory containing this repo, then execute:

	pip install .    

(Don't miss the period at the end!)

Or, if that doesn't work for some reason, try:

	python -m pip install .

Finally, as a last resort, if you don't have pip 
installed for some reason, you can use this:

	python setup.py install


## Use Overview

The standard way the library was intended for use is to
add a `build.py` script to the root directory of the
project you wish to distribute. (Note: the file may have 
any name of your choice - "build.py" is merely a 
recommended naming convention).  After defining that 
script, you run it to build your distribution package. 

In `build.py`, you may wish to simply import everything 
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
is include in the "source distribution" of the library.
You may visit the [PyPi](https://pypi.org/project/distbuilder/#files) 
downloads page for the project to acquire this.

Alternatively, you may download/copy the source files directly from GitHub into a local directory:   

[hello.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/hello.py)

[build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/build.py)

[demo.ico](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_world_tk/demo.ico)

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

Note: The most astute observer may notice 
that the stdout messages are not produced on the terminal
by the binary version of the example. It is a feature of PyInstaller, 
to "swallow" console messages produced by gui applications.  
This may be counterproductive for debugging most especially, 
and as such distbuilder provides a direct "solution" for this. 
Refer to the [Testing](Reference.md#testing) section of 
the [Reference Manual](Reference.md#installers) for 
more details.)    

## Learn More  

For a more thorough explanation for how to use
the library, refer to the [Reference Manual](Reference.md).
