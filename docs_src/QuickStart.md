# Quick Start Guide
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Installation 

Easy as pie:

	pip install distbuilder

> Trouble? See: [Installation Help](Issues.md#Installation-Help)
      
## Use

### Build Scripts

A standard way for distbuilder to be used is to have a `build.py` script placed in the root directory of a project.  The script employs this library to "build" a product of some form or another.  A developer may run the  script on demand, or it may be included in an automated process such as a build pipeline.

Typically, build scripts follow a general pattern where they create a [ConfigFactory](ConfigClasses.md#configfactory) along with an instance of a [Process Class](HighLevel.md). A collection of parameters are defined through the ConfigFactory and the Process is run to produce an archive file, an executable, an installer, or some other "distribution package".

### Setup Scripts

Distbuilder is great to use within a `setup.py` script as well. It is a common Python practice to provide such a script to be run by each developer within their work environment. A setup script will install dependencies and perform other initialization tasks for working on the project. For more on this usage, refer to:

* [Library Installation](LowLevel.md#library-installation)
* [Module import utilities](LowLevel.md#module-import-utilities) 
* [download](LowLevel.md#download)
* [run](LowLevel.md#run)

### Getting Started

The easiest way for most people to learn how to use distbuilder is to dive right into the [Basic Examples](BasicExamples.md).  From that, you should come away with a basic idea for how you might to use the tool.  

If you want to begin a more thorough examination of the library, continue on to [Process Classes](HighLevel.md)...
