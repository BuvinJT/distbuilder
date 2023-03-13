# Distribution Builder Python Library
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

**Distribution Builder** (aka `distbuilder`) is an open source [Python](https://www.python.org/) library. It is a "meta tool" which wraps and interlinks a collection of powerful utilities behind a single Python interface.

The most prominent `distbuilder` features include the ability to create **stand-alone binaries** from Python scripts, and to create **installers** in a **cross platform** manner. The installers can be built for either **gui** or **non-gui** contexts. Additionally, the library can be used to **obfuscate** Python, protecting your intellectual property.

Distribution Builder is able to do all this by leveraging the power of many other open source technologies, including: [pip](https://pypi.org/project/pip/), [PyInstaller](http://www.pyinstaller.org), [The Qt Installer Framework](http://doc.qt.io/qtinstallerframework), [IExpress](https://en.wikipedia.org/wiki/IExpress), [Opy](https://pypi.org/project/opy-distbuilder/), and more. 

This library is an *ideal* tool for packaging and deploying **Python** based programs.  Beyond that, it can also help you to distribute software written in practically **any language**!  To this end, a specific module has been added to ease cross platform [Qt C++ Integration](QtCpp.md) with distbuilder. And on Windows specifically, the library provides the [additional means](HighLevel.md#iexpresspackageprocess) to transform simple scripts written in [Batch](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands), [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2), [VBScript](https://learn.microsoft.com/en-us/windows/win32/lwef/using-vbscript), or [JScript](https://learn.microsoft.com/en-us/windows/win32/lwef/using-javascript-and-jscript) into stand-alone executables. There are plans for more more cross language, and cross framework, integration modules to become available in the future.

This library has been tested on recent versions of Windows, macOS, and multiple Linux distros. It is intended for Python 3, but is backwards compatible with Python 2.7+. 

This [Quick Start Guide](QuickStart.md) will help you take the first step towards distributing your software to the world!
