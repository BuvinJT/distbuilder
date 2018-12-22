# Distribution Builder (distbuilder) 
### Quick Start Guide

#### Pre-Installation instructions:

This library requires a custom fork from the open 
source library "Opy" version *1.1.28.1* or later.  
Currently, that version can be acquired from:

	https://github.com/BuvinJT/Opy

Or, via the direct git clone url:

	https://github.com/BuvinJT/Opy.git

(Soon, that fork will be merged into the parent
"Opy" project and may available via pip download...)

---------------

Additionally, the "Qt Installer Framework"
is recommended.  This component is not a hard
requirement, but is strongly recommended, so 
that you may employ the distbuilder installation
building features.

QtIFW can be acquired from:

	http://download.qt.io/official_releases/qt-installer-framework/

Once installed, the best way to integrate it 
with distbuilder is to define an environmental
variable name "QT_IFW_DIR" and the set value
for that equal to the directory where you 
installed the utility.
      
#### Installation instructions:

Generally speaking, installation is as simple as this: 

	pip install distbuilder

If you are installing from the raw source for this 
project, however, you may Git clone, or otherwise 
download the repository to your local machine.

On Windows, you may then simply run install.bat
(or install3.bat). On Mac or Linux, you may use the 
counterpart install.sh (or install3.sh) instead.

If you encounter failures with those scripts, try
the "manual approach":

From a command line interface, change to the 
directory containing this repo, then execute:

	pip install .    

(Don't miss the period at the end!)

Or, if that doesn't work for some reason, try:

	python -m pip install .

Or
	
	sudo python -m pip install .

Finally, if you don't have pip 
installed for some reason, try this:

	python setup.py install


#### To use:

Add a "build.py" script to the root directory of the
project you wish to distribute. (Note: the file may have 
any name of your choice - "build.py" is merely a 
recommended naming convention).  After defining that 
script, run it to build your distribution package. 

In build.py, you may wish to simply import everything 
from this library via `import distbuilder *`.  If 
your build script does not need to do much aside from 
implement these library functions, starting it in that 
manner is often a convenient choice.    

#### Getting started:

The easiest way learn how to use distbuilder is likely 
to reference an example.  Review and test the included
"Hello World Tk Example" (found at this relative path):
	
	../examples/hello_world_tk

This example requires the standard Python TKinter 
library	be installed.

Start by confirming you can run the program 
script in the "natural" manner:

	python ../examples/hello_world_tk/hello.py

Assuming that works, run the build script.  It
will obfuscate the code, convert the obfuscated .py 
to a stand-alone binary, build an installer with 
that bundled into it, move the installer to your 
desktop (for convenience), and launch it (for testing)! 
Execute the following:

	python ../examples/hello_world_tk/build.py
	
If all goes well, you will end up with an 
installer launched at the end of the script.
Proceed through that, and then run the program	
to confirm it works as a stand-alone executable.

Review the build.py script.  It should be fairly
self-explanatory for a moderately seasoned Python 
developer.  The script is a relatively simple
example, but covers a good portion of the major
distbuilder features so as to provide a feel for 
what it does, and how it works.

For a more thorough explanation for how to use
the library, refer to the Reference.md file.
