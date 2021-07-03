# Distribution Builder Python Library
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Introduction

"Distribution Builder" (distbuilder) is an open source Python library.
It is a "meta tool", which wraps and combines other related libraries and utilities 
including [PyInstaller](http://www.pyinstaller.org), [IExpress](https://en.wikipedia.org/wiki/IExpress),
the [Qt Installer Framework](http://doc.qt.io/qtinstallerframework), 
[Opy](https://pypi.org/project/opy-distbuilder/) (Obfuscator for Python), 
[pip](https://pypi.org/project/pip/), and more.  

As one might guess, the primary role which Distribution Builder can serve for your development 
needs is packaging and deploying Python based programs. It can, however, be employed for 
distributing software written in other languages as well.  To this end, a dedicated module, 
has been provided which is specific for [Qt C++ Integration](QtCpp.md).  The library also
includes the means to transform simple Windows scripts 
(Batch, PowerShell, VBScript, or JScript) 
into full blown executable programs.  More cross language / 
cross framework integration modules will become available in the future.

This library is compatible with both Python 2 and 3.  It has been tested on recent versions of 
Windows, macOS, and multiple Linux distros. It features the ability to create stand-alone 
binaries, and is capable of building installers in a 
cross platform manner (via QtIFW). These installers can be produced for either gui or 
*non-gui* (i.e terminal interface) contexts. Note that the later is a feature QtIFW does not naturally provide. 
The library can also be used to **obfuscate** code (via Opy), so as to protect proprietary work.

See the [Quick Start Guide](QuickStart.md) for instructions on installation 
and getting started with the tool. For a more thorough explanation of how to use it, 
it is recommended you proceed to [High Level Classes](HighLevel.md).
Then, as needed, move on to [Configuration Classes](ConfigClasses.md) and/or
[Low Level Classes And Functions](LowLevel.md).
	
If you wish to contribute, please review the [To-Do List](ToDo.md) 
for a collection of desired tasks to be completed and the priority 
they have been currently designated, as part of a loose road map for planned
releases.
	
## Additional Project Goals

In addition to everything which is already fleshed out and functional within it, 
"Distribution Builder" will soon supply a **new development paradigm**...  Using the 
obfuscation and library management features, it will provide the ability for collaborators 
to work on a **Python** project together, **without directly sharing source code**!

We acknowledge this idea may to be deemed "anti-Pythonic" by purists, since the language is
commonly employed for open source purposes, and the Python ecosystem is almost 100%
open source.  Note that the "Distribution Builder" developers are not anti-open source!
In fact, observe that this project is itself open source, and built over the top of other open 
source projects!  We are, however, pro-security, and we advocate for the owners of 
intellectual property. We argue that if it is not universally "wrong" to produce 
close sourced programs, doing so should not be dubbed off limits with Python,
if an organization or individual so choses.   

Once theses features (in development) are completed and smoothed over, each Python developer 
on a project could independently create libraries with a clear text 
*public* interface, but which employ code bases that are obfuscated.  Other developers 
could then implement the functionality of those libraries as they develop their modules.
"Distribution Builder" could next seamlessly bring together everyone's work into a single 
project, where all of the protected code bases work together and even the "seams" between 
those public interfaces become obfuscated. In this scenario, each developer will have this 
capability, and therefore be able to test their own work - on the fly - within the context 
of the larger product.  

Producing software in this manner, allows engineers to work together 
on endeavors where there are gray areas pertaining to intellectual rights and/or the
legalities of such have yet to be solidified.  This mechanism mitigates the risk
of an individual stealing an entire code base, or being "boxed out" of a project for
which they made considerable contributions.  

While this overarching *concept* has long been available with other languages (e.g. with 
C++ dll's and other analogous compiled components), this has not generally been an option 
for Python.  Even in those languages where such is a "ready option", a development scheme 
of this nature is often too cumbersome to employ, or simply not an option developers have
considered. "Distribution Builder" aims to make this a painless and realistic mode of 
operation for Python.
 
## Important Notes

*BEFORE USE, BACK UP YOUR CODE TO ENSURE THERE COULD NOT POSSIBLY BE ANYTHING LOST!!!* 

This library is actively under development. It is not yet officially released for 
production use. Function signatures, class definitions, etc. are NOT currently 
guaranteed to be stable / backwards compatible. Client implementations may require 
modification upon pulling the latest revisions to this.

At the present time, the weakest components in the library are admittedly the obfuscation 
features. There is a bit of a learning curve for utilizing such, and a fair degree of 
effort is likely required to perfect it for your own project right now.  It is recommended 
that you employ these security features only after getting the rest of your build process 
defined.
 