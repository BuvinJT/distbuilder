# Installer UI Examples
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Custom Graphics Examples

TODO: FILL IN!

## Custom Interactions Examples

TODO: FILL IN!

## Custom Pages Examples

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

## Widget Injections Example

TODO: FILL IN!

## Hello Dynamic Finish Example

TODO: FILL IN!
