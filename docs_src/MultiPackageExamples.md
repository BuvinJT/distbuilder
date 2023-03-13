# Multi-Package Examples
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

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
