# Basic Examples
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Hello World Example

The Hello World Example is a simple demonstration of using the 
[PyToBinPackageProcess](HighLevel.md#pytobinpackageprocess) class. 
This is one of the most straightforward, simple use cases for the library.  

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

### Feature spotlight: "file name normalization"

You might notice that binary names/paths (in any of the examples) may or may not
include extensions such as `.exe`.  Likewise, icons may or may not have extensions
such as `.ico` specified.  Yet, these scripts work cross platform, where the extensions
differ!  That is due to the use of [normBinaryName](LowLevel.md#normbinaryname) and
[normIconName](LowLevel.md#normiconname) functions under the hood of distbuilder's processes.
The library corrects those names for you automatically based upon the environmental context.

Currently, alternate icon resources must be provided which align with the platform context.
There are plans, however, for future releases of the library to generate missing icon formats
for you as needed.    

### Extended feature demo: "debug mode"

Here is a good place to illustrate one very useful extended feature of this library,
which may prove immeaditely valuable to you.  This is will also help you to understand
a common pattern for using some of the primary distbuilder classes. 

Locate the following commented out line in the Hello World Tk build script:

    #def onPyPackageProcess( self, prc ): prc.isExeTest = True

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

So, what's the point of setting `prc.isExeTest = True` ?
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
