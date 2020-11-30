# Examples
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Source Code / Resources

All of the examples discussed here are included in the "source distribution" 
of the library. The [PyPi downloads](https://pypi.org/project/distbuilder/#files) 
page for this project is arguably the fastest route to acquire that.
See [From source installation](QuickStart.md#from-source-installation) to learn 
about other ways of downloading these files.

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
will become one component which may *NOT* be installed selectively by the user. 

This example requires that both of the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place the next file.
Those first two must be named `hello_world` and `hello_world_tk` for this
"master" script to function.

You may download/copy the example file directly from GitHub 
(into a `hello_merge` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_merge/build.py)

The key points to this example are to demo the implementation of the  
[onPackagesStaged](HighLevel.md#onPackagesStaged) virtual function of
[RobustInstallerProcess](HighLevel.md#robust-installer-process).
Within that, [QtIfwPackage list manipulation](LowLevel.md#qtifwpackage-list-manipulation) 
is shown (by default) via [mergeQtIfwPackages](LowLevel.md#mergeQtIfwPackages).
If you comment that line out, and uncomment the call to 
[nestQtIfwPackage](LowLevel.md#nestQtIfwPackage) below it,
you may test the results of these alternate ways to combine packages.

The demo goes on to show low-level manipulations, and regenerations of the files
produced by, [QtIfwConfigXml](ConfigClasses.md#qtifwpackage) and 
[QtIfwPackageXml](ConfigClasses.md#qtifwpackage) objects to give you further
insight into the design patterns and functionality of the library. 

## Hello Dynamic Finish Example

TODO: FILL IN!

## Hello Installer UI Example

A QtIwf installer is extremely customizable.  In addition to simply copying
files to another machine, it can perform extended operations on that target 
to further refine the environment where the program will run.  Not only that,
but the installer's interface, and logic flow, can be manipulated to precisely 
fit your use case.  This example demonstrates a proof of concept modification
to that UI.     

This example requires the Hello World Tk files be present in the testing environment 
within a directory adjacent to where you will place the build script for this one.
That required folder must be named `hello_world_tk` for this "master" script to 
function.

You may download/copy the example file directly from GitHub 
(into a `hello_qtifw_ui` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_qtifw_ui/build.py)

The demo shows how one may assign the [ifwUiPages](HighLevel.md#ifwuipages) attribute of a ConfigFactory to to easily add or replace default installer "pages" / "screens"
with custom definitions.  Those pages are represented using [QtIfwUiPage](ConfigClasses.md#qtifwuipage) objects.  

The QtIfwUiPage class is designed with the expectation that you may wish to create custom pages using the [Qt Designer WYSIWYG](https://doc.qt.io/qt-5/designer-quick-start.html) tool. Alternatively, your needs maybe met by employing a derived class
e.g. [QtIfwSimpleTextPage](ConfigClasses.md#qtifwsimpletextpage), which draws upon
a built-in library resource file for the page layout.   

In concert with altering these visual dimensions of the user experience, you may
revise the logic via [Installer Scripting](LowLevel.md#installer-scripting), or call upon the higher level script abstraction classes [QtIfwControlScript](ConfigClasses.md#qtifwcontrolscript) or
[QtIfwPackageScript](ConfigClasses.md#qtifwpackagescript). 

## Hello Wrapper Example

This example provides a **collection** of demonstrations using the
[QtIfwExeWrapper](ConfigClasses.md#qtifwexewrapper) class. A "wrapper" 
can super impose environmental conditions on the context
within which the binary is run.  Notably, this may include an 
[ExecutableScript](LowLevel.md#executablescript) for maximum flexibility.
Follow the links to learn to more.

This example requires that both of the first examples 
(Hello World & Hello World Tk) be present in the testing environment 
within directories adjacent to a third directory where you place the next set of files.
Those first two must be named `hello_world` and `hello_world_tk` for this
"master" script to fully function.

You may download/copy the example files directly from GitHub 
(into a `hello_wrapper` directory):   

Build script: [build.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_wrapper/build.py)

GUI app: [hello_gui.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_wrapper/hello_gui.py)

Terminal app: [hello_terminal.py](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/examples/hello_wrapper/hello_terminal.py)

Within the build script, select a particular example to test and uncomment its `p.run()` line.  Then, run the script to see the results.  

In conjunction with choosing a wrapper feature to test, you may switch between
a gui and non-gui context. To do so, swap the commented out lines in the ConfigFactory
attributes. That is, near the top of the script change:

	f.isGui            = True        
	f.entryPointPy     = "hello_gui.py"

To:	
	  
	f.isGui            = False 
	f.entryPointPy     = "hello_terminal.py"   

When the resulting app is run, it will show the effect of implementing the 
various wrapper features e.g. the arguments the program received, or if you 
are running in an "elevated" context, etc.  

If desired, you may also wish to test running these demo programs post installation in 
"debug mode". See the documentation on the [run](LowLevel.md#run) function.

## Hello Operations Examples

TODO: FILL IN!

### High Level Convenience Operations Example

TODO: FILL IN!

### Low Level Embedded Script Operations Example

TODO: FILL IN!

### Windows Registry Interactions Example

TODO: FILL IN!

## Hello Startup Example

TODO: FILL IN!

## Hello Opy Example

TODO: FILL IN!

## Hello Opy Bundle Example

TODO: FILL IN!

## Hello World Qt Example

The [Hello World Qt Example](QtCpp.md#hello-world-qt-example) demos the 
[Qt C++ Integration](QtCpp.md) feature. If you wish to review / test the code, it is strongly recommended you read that section of the documentation in its entirety.  

## Hello World QML Example

See [Hello World QML Example](QtCpp.md#hello-world-qml-example) 

## Hello World QML New Example

See [Hello World QML New Example](QtCpp.md#hello-world-qml-new-example) 
