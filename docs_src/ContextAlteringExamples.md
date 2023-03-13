# Context Altering Examples
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

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

## Hello Startup Example

TODO: FILL IN!
