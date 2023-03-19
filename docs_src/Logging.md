## **Logger**`#!py3 class` { #Logger data-toc-label=Logger }



**Magic Methods:**

 - [`__init__`](#Logger-init)

**Instance Methods:** 

 - [`close`](#close)
 - [`filePath`](#filePath)
 - [`isOpen`](#isOpen)
 - [`isPaused`](#isPaused)
 - [`open`](#open)
 - [`pause`](#pause)
 - [`resume`](#resume)
 - [`toStderr`](#toStderr)
 - [`toStderrLn`](#toStderrLn)
 - [`toStdout`](#toStdout)
 - [`toStdoutLn`](#toStdoutLn)
 - [`write`](#write)
 - [`writeLn`](#writeLn)

**Instance Attributes:** 

 - [`name`](#name)
 - [`isUniqueFile`](#isUniqueFile)

**Class/Static Methods:** 

 - [`isSingletonOpen`](#isSingletonOpen)
 - [`singleton`](#singleton)

### **Logger**`#!py3 (name=None, isUniqueFile=False)` { #Logger-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**close**`#!py3 (self)` { #close data-toc-label=close }


### *obj*.**filePath**`#!py3 (self)` { #filePath data-toc-label=filePath }


### *obj*.**isOpen**`#!py3 (self)` { #isOpen data-toc-label=isOpen }


### *obj*.**isPaused**`#!py3 (self)` { #isPaused data-toc-label=isPaused }


### *obj*.**open**`#!py3 (self)` { #open data-toc-label=open }


### *obj*.**pause**`#!py3 (self)` { #pause data-toc-label=pause }


### *obj*.**resume**`#!py3 (self)` { #resume data-toc-label=resume }


### *obj*.**toStderr**`#!py3 (self, msg)` { #toStderr data-toc-label=toStderr }


### *obj*.**toStderrLn**`#!py3 (self, msg)` { #toStderrLn data-toc-label=toStderrLn }


### *obj*.**toStdout**`#!py3 (self, msg)` { #toStdout data-toc-label=toStdout }


### *obj*.**toStdoutLn**`#!py3 (self, msg)` { #toStdoutLn data-toc-label=toStdoutLn }


### *obj*.**write**`#!py3 (self, msg)` { #write data-toc-label=write }


### *obj*.**writeLn**`#!py3 (self, msg)` { #writeLn data-toc-label=writeLn }


### *obj*.**name** *<class 'str'>* default: *"pymkdocs"* { #name data-toc-label=name }


### *obj*.**isUniqueFile** *<class 'NoneType'>* default: *None* { #isUniqueFile data-toc-label=isUniqueFile }


### *Logger*.**isSingletonOpen**`#!py3 ()` { #isSingletonOpen data-toc-label=isSingletonOpen }


### *Logger*.**singleton**`#!py3 (name=None, isUniqueFile=False)` { #singleton data-toc-label=singleton }



______

## **Functions** { #Functions data-toc-label=Functions }

### **isLogging**`#!py3 ()` { #isLogging data-toc-label=isLogging }



______

### **log**`#!py3 (msg)` { #log data-toc-label=log }



______

### **startLogging**`#!py3 (name=None, isUniqueFile=False)` { #startLogging data-toc-label=startLogging }



______

### **stopLogging**`#!py3 ()` { #stopLogging data-toc-label=stopLogging }



______

