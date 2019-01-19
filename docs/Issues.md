# Troubleshooting
![distbuilder logo](https://raw.githubusercontent.com/BuvinJT/distbuilder/master/docs/img/distbuilder128.png)

## Tested On

Python
- 2.7
- 3.5
- 3.7
  
Windows    
- 8.0
- 10

macOS    
- Sierra

Linux   
- Ubuntu 16.04
- Ubuntu 18.04

## Qt Installer Framework issues

### Setting `QT_IFW_DIR` 

TODO

### Windows: Launch App at end of install failures

TODO

### Windows 8 (and earlier?): Crash at end of install

Recent versions of QtIFW have been observed to crash at the 
end of the installation on Windows 8.  This bug has been 
reported to Qt and they are supposed to be patching it.

The current work around is to directly launch the installer 
with elevated priviledges (i.e as an administrator).

## Get Help 

Refer to [Post An Issue](Contribute.md#post-an-issue).