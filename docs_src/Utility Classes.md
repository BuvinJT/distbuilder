## **ConfigParser**`#!py3 class` { #ConfigParser data-toc-label=ConfigParser }

ConfigParser implementing interpolation.

**Base Classes:**

Container, Iterable, Sized, Collection, Mapping, MutableMapping, RawConfigParser


**Instance Methods:** 

 - [`add_section`](#add_section)
 - [`clear`](#clear)
 - [`defaults`](#defaults)
 - [`get`](#get)
 - [`getboolean`](#getboolean)
 - [`getfloat`](#getfloat)
 - [`getint`](#getint)
 - [`has_option`](#has_option)
 - [`has_section`](#has_section)
 - [`items`](#items)
 - [`keys`](#keys)
 - [`options`](#options)
 - [`optionxform`](#optionxform)
 - [`pop`](#pop)
 - [`popitem`](#popitem)
 - [`read`](#read)
 - [`read_dict`](#read_dict)
 - [`read_file`](#read_file)
 - [`read_string`](#read_string)
 - [`readfp`](#readfp)
 - [`remove_option`](#remove_option)
 - [`remove_section`](#remove_section)
 - [`sections`](#sections)
 - [`set`](#set)
 - [`setdefault`](#setdefault)
 - [`values`](#values)
 - [`write`](#write)

**Class/Static Methods:** 

 - [`update`](#update)

**Class/Static Attributes:** 

 - [`BOOLEAN_STATES`](#BOOLEAN_STATES)
 - [`NONSPACECRE`](#NONSPACECRE)
 - [`OPTCRE`](#OPTCRE)
 - [`OPTCRE_NV`](#OPTCRE_NV)
 - [`SECTCRE`](#SECTCRE)
 - [`converters`](#converters)

### *obj*.**add_section**`#!py3 (self, section)` { #add_section data-toc-label=add_section }

Create a new section in the configuration.  Extends
RawConfigParser.add_section by validating if the section name is
a string.
### *obj*.**clear**`#!py3 (self)` { #clear data-toc-label=clear }

D.clear() - None.  Remove all items from D.
### *obj*.**defaults**`#!py3 (self)` { #defaults data-toc-label=defaults }


### *obj*.**get**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>)` { #get data-toc-label=get }

Get an option value for a given section.

If `vars' is provided, it must be a dictionary. The option is looked up
in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
If the key is not found and `fallback' is provided, it is used as
a fallback value. `None' can be provided as a `fallback' value.

If interpolation is enabled and the optional argument `raw' is False,
all interpolations are expanded in the return values.

Arguments `raw', `vars', and `fallback' are keyword only.

The section DEFAULT is special.
### *obj*.**getboolean**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getboolean data-toc-label=getboolean }


### *obj*.**getfloat**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getfloat data-toc-label=getfloat }


### *obj*.**getint**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getint data-toc-label=getint }


### *obj*.**has_option**`#!py3 (self, section, option)` { #has_option data-toc-label=has_option }

Check for the existence of a given option in a given section.
If the specified `section' is None or an empty string, DEFAULT is
assumed. If the specified `section' does not exist, returns False.
### *obj*.**has_section**`#!py3 (self, section)` { #has_section data-toc-label=has_section }

Indicate whether the named section is present in the configuration.

The DEFAULT section is not acknowledged.
### *obj*.**items**`#!py3 (self, section=<object object at 0x00934920>, raw=False, vars=None)` { #items data-toc-label=items }

Return a list of (name, value) tuples for each option in a section.

All % interpolations are expanded in the return values, based on the
defaults passed into the constructor, unless the optional argument
`raw' is true.  Additional substitutions may be provided using the
`vars' argument, which must be a dictionary whose contents overrides
any pre-existing defaults.

The section DEFAULT is special.
### *obj*.**keys**`#!py3 (self)` { #keys data-toc-label=keys }

D.keys() - a set-like object providing a view on D's keys
### *obj*.**options**`#!py3 (self, section)` { #options data-toc-label=options }

Return a list of option names for the given section name.
### *obj*.**optionxform**`#!py3 (self, optionstr)` { #optionxform data-toc-label=optionxform }


### *obj*.**pop**`#!py3 (self, key, default=<object object at 0x00934098>)` { #pop data-toc-label=pop }

D.pop(k[,d]) - v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
### *obj*.**popitem**`#!py3 (self)` { #popitem data-toc-label=popitem }

Remove a section from the parser and return it as
a (section_name, section_proxy) tuple. If no section is present, raise
KeyError.

The section DEFAULT is never returned because it cannot be removed.
### *obj*.**read**`#!py3 (self, filenames, encoding=None)` { #read data-toc-label=read }

Read and parse a filename or an iterable of filenames.

Files that cannot be opened are silently ignored; this is
designed so that you can specify an iterable of potential
configuration file locations (e.g. current directory, user's
home directory, systemwide directory), and all existing
configuration files in the iterable will be read.  A single
filename may also be given.

Return list of successfully read files.
### *obj*.**read_dict**`#!py3 (self, dictionary, source='<dict>')` { #read_dict data-toc-label=read_dict }

Read configuration from a dictionary.

Keys are section names, values are dictionaries with keys and values
that should be present in the section. If the used dictionary type
preserves order, sections and their keys will be added in order.

All types held in the dictionary are converted to strings during
reading, including section names, option names and keys.

Optional second argument is the `source' specifying the name of the
dictionary being read.
### *obj*.**read_file**`#!py3 (self, f, source=None)` { #read_file data-toc-label=read_file }

Like read() but the argument must be a file-like object.

The `f' argument must be iterable, returning one line at a time.
Optional second argument is the `source' specifying the name of the
file being read. If not given, it is taken from f.name. If `f' has no
`name' attribute, `???' is used.
### *obj*.**read_string**`#!py3 (self, string, source='<string>')` { #read_string data-toc-label=read_string }

Read configuration from a given string.
### *obj*.**readfp**`#!py3 (self, fp, filename=None)` { #readfp data-toc-label=readfp }

Deprecated, use read_file instead.
### *obj*.**remove_option**`#!py3 (self, section, option)` { #remove_option data-toc-label=remove_option }

Remove an option.
### *obj*.**remove_section**`#!py3 (self, section)` { #remove_section data-toc-label=remove_section }

Remove a file section.
### *obj*.**sections**`#!py3 (self)` { #sections data-toc-label=sections }

Return a list of section names, excluding [DEFAULT]
### *obj*.**set**`#!py3 (self, section, option, value=None)` { #set data-toc-label=set }

Set an option.  Extends RawConfigParser.set by validating type and
interpolation syntax on the value.
### *obj*.**setdefault**`#!py3 (self, key, default=None)` { #setdefault data-toc-label=setdefault }

D.setdefault(k[,d]) - D.get(k,d), also set D[k]=d if k not in D
### *obj*.**values**`#!py3 (self)` { #values data-toc-label=values }

D.values() - an object providing a view on D's values
### *obj*.**write**`#!py3 (self, fp, space_around_delimiters=True)` { #write data-toc-label=write }

Write an .ini-format representation of the configuration state.

If `space_around_delimiters' is True (the default), delimiters
between keys and values are surrounded by spaces.
### *ConfigParser*.**update**`#!py3 (*args, **kwds)` { #update data-toc-label=update }

D.update([E, ]**F) - None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v
### *ConfigParser*.**BOOLEAN_STATES** *class 'dict'* default: *None* { #BOOLEAN_STATES data-toc-label=BOOLEAN_STATES }


### *ConfigParser*.**NONSPACECRE** *class 're.Pattern'* default: *None* { #NONSPACECRE data-toc-label=NONSPACECRE }


### *ConfigParser*.**OPTCRE** *class 're.Pattern'* default: *None* { #OPTCRE data-toc-label=OPTCRE }


### *ConfigParser*.**OPTCRE_NV** *class 're.Pattern'* default: *None* { #OPTCRE_NV data-toc-label=OPTCRE_NV }


### *ConfigParser*.**SECTCRE** *class 're.Pattern'* default: *None* { #SECTCRE data-toc-label=SECTCRE }


### *ConfigParser*.**converters** *class 'property'* default: *None* { #converters data-toc-label=converters }



______

## **ExecutableScript**`#!py3 class` { #ExecutableScript data-toc-label=ExecutableScript }



**Magic Methods:**

 - [`__init__`](#ExecutableScript-init)

**Instance Methods:** 

 - [`asSnippet`](#asSnippet)
 - [`debug`](#debug)
 - [`exists`](#exists)
 - [`fileName`](#fileName)
 - [`filePath`](#filePath)
 - [`fromBase64`](#fromBase64)
 - [`fromLines`](#fromLines)
 - [`injectLine`](#injectLine)
 - [`read`](#read)
 - [`remove`](#remove)
 - [`toBase64`](#toBase64)
 - [`toLines`](#toLines)
 - [`write`](#write)

**Instance Attributes:** 

 - [`rootName`](#rootName)
 - [`scriptDirPath`](#scriptDirPath)
 - [`replacements`](#replacements)
 - [`isIfwVarEscapeBackslash`](#isIfwVarEscapeBackslash)
 - [`isDebug`](#isDebug)

**Class/Static Methods:** 

 - [`linesToStr`](#linesToStr)
 - [`strToLines`](#strToLines)
 - [`typeOf`](#typeOf)

**Class/Static Attributes:** 

 - [`APPLESCRIPT_EXT`](#APPLESCRIPT_EXT)
 - [`BATCH_EXT`](#BATCH_EXT)
 - [`JSCRIPT_EXT`](#JSCRIPT_EXT)
 - [`POWERSHELL_EXT`](#POWERSHELL_EXT)
 - [`SHELL_EXT`](#SHELL_EXT)
 - [`SUPPORTED_EXTS`](#SUPPORTED_EXTS)
 - [`VBSCRIPT_EXT`](#VBSCRIPT_EXT)

### **ExecutableScript**`#!py3 (rootName, extension=True, shebang=True, script=None, scriptPath=None, scriptDirPath=None, replacements=None, isDebug=True)` { #ExecutableScript-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**asSnippet**`#!py3 (self)` { #asSnippet data-toc-label=asSnippet }


### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**exists**`#!py3 (self, scriptDirPath=None)` { #exists data-toc-label=exists }


### *obj*.**fileName**`#!py3 (self)` { #fileName data-toc-label=fileName }


### *obj*.**filePath**`#!py3 (self)` { #filePath data-toc-label=filePath }


### *obj*.**fromBase64**`#!py3 (self, data)` { #fromBase64 data-toc-label=fromBase64 }


### *obj*.**fromLines**`#!py3 (self, lines)` { #fromLines data-toc-label=fromLines }


### *obj*.**injectLine**`#!py3 (self, injection, lineNo)` { #injectLine data-toc-label=injectLine }


### *obj*.**read**`#!py3 (self, scriptDirPath=None)` { #read data-toc-label=read }


### *obj*.**remove**`#!py3 (self, scriptDirPath=None)` { #remove data-toc-label=remove }


### *obj*.**toBase64**`#!py3 (self, toString=False)` { #toBase64 data-toc-label=toBase64 }


### *obj*.**toLines**`#!py3 (self)` { #toLines data-toc-label=toLines }


### *obj*.**write**`#!py3 (self, scriptDirPath=None)` { #write data-toc-label=write }


### *obj*.**rootName** *class 'NoneType'* default: *None* { #rootName data-toc-label=rootName }


### *obj*.**scriptDirPath** *class 'NoneType'* default: *None* { #scriptDirPath data-toc-label=scriptDirPath }


### *obj*.**replacements** *class 'dict'* default: *{}* { #replacements data-toc-label=replacements }


### *obj*.**isIfwVarEscapeBackslash** *class 'bool'* default: *False* { #isIfwVarEscapeBackslash data-toc-label=isIfwVarEscapeBackslash }


### *obj*.**isDebug** *class 'NoneType'* default: *None* { #isDebug data-toc-label=isDebug }


### *ExecutableScript*.**linesToStr**`#!py3 (lines)` { #linesToStr data-toc-label=linesToStr }


### *ExecutableScript*.**strToLines**`#!py3 (s)` { #strToLines data-toc-label=strToLines }


### *ExecutableScript*.**typeOf**`#!py3 (path)` { #typeOf data-toc-label=typeOf }


### *ExecutableScript*.**APPLESCRIPT_EXT** *class 'str'* default: *"scpt"* { #APPLESCRIPT_EXT data-toc-label=APPLESCRIPT_EXT }


### *ExecutableScript*.**BATCH_EXT** *class 'str'* default: *"bat"* { #BATCH_EXT data-toc-label=BATCH_EXT }


### *ExecutableScript*.**JSCRIPT_EXT** *class 'str'* default: *"js"* { #JSCRIPT_EXT data-toc-label=JSCRIPT_EXT }


### *ExecutableScript*.**POWERSHELL_EXT** *class 'str'* default: *"ps1"* { #POWERSHELL_EXT data-toc-label=POWERSHELL_EXT }


### *ExecutableScript*.**SHELL_EXT** *class 'str'* default: *"sh"* { #SHELL_EXT data-toc-label=SHELL_EXT }


### *ExecutableScript*.**SUPPORTED_EXTS** *class 'list'* default: *['sh', 'bat', 'vbs', 'js', 'ps1', 'scpt']* { #SUPPORTED_EXTS data-toc-label=SUPPORTED_EXTS }


### *ExecutableScript*.**VBSCRIPT_EXT** *class 'str'* default: *"vbs"* { #VBSCRIPT_EXT data-toc-label=VBSCRIPT_EXT }



______

## **RawConfigParser**`#!py3 class` { #RawConfigParser data-toc-label=RawConfigParser }

ConfigParser that does not do interpolation.

**Base Classes:**

Container, Iterable, Sized, Collection, Mapping, MutableMapping


**Magic Methods:**

 - [`__init__`](#RawConfigParser-init)

**Instance Methods:** 

 - [`add_section`](#add_section)
 - [`clear`](#clear)
 - [`defaults`](#defaults)
 - [`get`](#get)
 - [`getboolean`](#getboolean)
 - [`getfloat`](#getfloat)
 - [`getint`](#getint)
 - [`has_option`](#has_option)
 - [`has_section`](#has_section)
 - [`items`](#items)
 - [`keys`](#keys)
 - [`options`](#options)
 - [`optionxform`](#optionxform)
 - [`pop`](#pop)
 - [`popitem`](#popitem)
 - [`read`](#read)
 - [`read_dict`](#read_dict)
 - [`read_file`](#read_file)
 - [`read_string`](#read_string)
 - [`readfp`](#readfp)
 - [`remove_option`](#remove_option)
 - [`remove_section`](#remove_section)
 - [`sections`](#sections)
 - [`set`](#set)
 - [`setdefault`](#setdefault)
 - [`values`](#values)
 - [`write`](#write)

**Instance Attributes:** 

 - [`default_section`](#default_section)

**Class/Static Methods:** 

 - [`update`](#update)

**Class/Static Attributes:** 

 - [`BOOLEAN_STATES`](#BOOLEAN_STATES)
 - [`NONSPACECRE`](#NONSPACECRE)
 - [`OPTCRE`](#OPTCRE)
 - [`OPTCRE_NV`](#OPTCRE_NV)
 - [`SECTCRE`](#SECTCRE)
 - [`converters`](#converters)

### **RawConfigParser**`#!py3 (defaults=None, dict_type=<class 'collections.OrderedDict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x00934920>, converters=<object object at 0x00934920>)` { #RawConfigParser-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**add_section**`#!py3 (self, section)` { #add_section data-toc-label=add_section }

Create a new section in the configuration.

Raise DuplicateSectionError if a section by the specified name
already exists. Raise ValueError if name is DEFAULT.
### *obj*.**clear**`#!py3 (self)` { #clear data-toc-label=clear }

D.clear() - None.  Remove all items from D.
### *obj*.**defaults**`#!py3 (self)` { #defaults data-toc-label=defaults }


### *obj*.**get**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>)` { #get data-toc-label=get }

Get an option value for a given section.

If `vars' is provided, it must be a dictionary. The option is looked up
in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
If the key is not found and `fallback' is provided, it is used as
a fallback value. `None' can be provided as a `fallback' value.

If interpolation is enabled and the optional argument `raw' is False,
all interpolations are expanded in the return values.

Arguments `raw', `vars', and `fallback' are keyword only.

The section DEFAULT is special.
### *obj*.**getboolean**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getboolean data-toc-label=getboolean }


### *obj*.**getfloat**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getfloat data-toc-label=getfloat }


### *obj*.**getint**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getint data-toc-label=getint }


### *obj*.**has_option**`#!py3 (self, section, option)` { #has_option data-toc-label=has_option }

Check for the existence of a given option in a given section.
If the specified `section' is None or an empty string, DEFAULT is
assumed. If the specified `section' does not exist, returns False.
### *obj*.**has_section**`#!py3 (self, section)` { #has_section data-toc-label=has_section }

Indicate whether the named section is present in the configuration.

The DEFAULT section is not acknowledged.
### *obj*.**items**`#!py3 (self, section=<object object at 0x00934920>, raw=False, vars=None)` { #items data-toc-label=items }

Return a list of (name, value) tuples for each option in a section.

All % interpolations are expanded in the return values, based on the
defaults passed into the constructor, unless the optional argument
`raw' is true.  Additional substitutions may be provided using the
`vars' argument, which must be a dictionary whose contents overrides
any pre-existing defaults.

The section DEFAULT is special.
### *obj*.**keys**`#!py3 (self)` { #keys data-toc-label=keys }

D.keys() - a set-like object providing a view on D's keys
### *obj*.**options**`#!py3 (self, section)` { #options data-toc-label=options }

Return a list of option names for the given section name.
### *obj*.**optionxform**`#!py3 (self, optionstr)` { #optionxform data-toc-label=optionxform }


### *obj*.**pop**`#!py3 (self, key, default=<object object at 0x00934098>)` { #pop data-toc-label=pop }

D.pop(k[,d]) - v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
### *obj*.**popitem**`#!py3 (self)` { #popitem data-toc-label=popitem }

Remove a section from the parser and return it as
a (section_name, section_proxy) tuple. If no section is present, raise
KeyError.

The section DEFAULT is never returned because it cannot be removed.
### *obj*.**read**`#!py3 (self, filenames, encoding=None)` { #read data-toc-label=read }

Read and parse a filename or an iterable of filenames.

Files that cannot be opened are silently ignored; this is
designed so that you can specify an iterable of potential
configuration file locations (e.g. current directory, user's
home directory, systemwide directory), and all existing
configuration files in the iterable will be read.  A single
filename may also be given.

Return list of successfully read files.
### *obj*.**read_dict**`#!py3 (self, dictionary, source='<dict>')` { #read_dict data-toc-label=read_dict }

Read configuration from a dictionary.

Keys are section names, values are dictionaries with keys and values
that should be present in the section. If the used dictionary type
preserves order, sections and their keys will be added in order.

All types held in the dictionary are converted to strings during
reading, including section names, option names and keys.

Optional second argument is the `source' specifying the name of the
dictionary being read.
### *obj*.**read_file**`#!py3 (self, f, source=None)` { #read_file data-toc-label=read_file }

Like read() but the argument must be a file-like object.

The `f' argument must be iterable, returning one line at a time.
Optional second argument is the `source' specifying the name of the
file being read. If not given, it is taken from f.name. If `f' has no
`name' attribute, `???' is used.
### *obj*.**read_string**`#!py3 (self, string, source='<string>')` { #read_string data-toc-label=read_string }

Read configuration from a given string.
### *obj*.**readfp**`#!py3 (self, fp, filename=None)` { #readfp data-toc-label=readfp }

Deprecated, use read_file instead.
### *obj*.**remove_option**`#!py3 (self, section, option)` { #remove_option data-toc-label=remove_option }

Remove an option.
### *obj*.**remove_section**`#!py3 (self, section)` { #remove_section data-toc-label=remove_section }

Remove a file section.
### *obj*.**sections**`#!py3 (self)` { #sections data-toc-label=sections }

Return a list of section names, excluding [DEFAULT]
### *obj*.**set**`#!py3 (self, section, option, value=None)` { #set data-toc-label=set }

Set an option.
### *obj*.**setdefault**`#!py3 (self, key, default=None)` { #setdefault data-toc-label=setdefault }

D.setdefault(k[,d]) - D.get(k,d), also set D[k]=d if k not in D
### *obj*.**values**`#!py3 (self)` { #values data-toc-label=values }

D.values() - an object providing a view on D's values
### *obj*.**write**`#!py3 (self, fp, space_around_delimiters=True)` { #write data-toc-label=write }

Write an .ini-format representation of the configuration state.

If `space_around_delimiters' is True (the default), delimiters
between keys and values are surrounded by spaces.
### *obj*.**default_section** *class 'NoneType'* default: *None* { #default_section data-toc-label=default_section }


### *RawConfigParser*.**update**`#!py3 (*args, **kwds)` { #update data-toc-label=update }

D.update([E, ]**F) - None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v
### *RawConfigParser*.**BOOLEAN_STATES** *class 'dict'* default: *None* { #BOOLEAN_STATES data-toc-label=BOOLEAN_STATES }


### *RawConfigParser*.**NONSPACECRE** *class 're.Pattern'* default: *None* { #NONSPACECRE data-toc-label=NONSPACECRE }


### *RawConfigParser*.**OPTCRE** *class 're.Pattern'* default: *None* { #OPTCRE data-toc-label=OPTCRE }


### *RawConfigParser*.**OPTCRE_NV** *class 're.Pattern'* default: *None* { #OPTCRE_NV data-toc-label=OPTCRE_NV }


### *RawConfigParser*.**SECTCRE** *class 're.Pattern'* default: *None* { #SECTCRE data-toc-label=SECTCRE }


### *RawConfigParser*.**converters** *class 'property'* default: *None* { #converters data-toc-label=converters }



______

## **SafeConfigParser**`#!py3 class` { #SafeConfigParser data-toc-label=SafeConfigParser }

ConfigParser alias for backwards compatibility purposes.

**Base Classes:**

Container, Iterable, Sized, Collection, Mapping, MutableMapping, RawConfigParser, ConfigParser


**Magic Methods:**

 - [`__init__`](#SafeConfigParser-init)

**Instance Methods:** 

 - [`add_section`](#add_section)
 - [`clear`](#clear)
 - [`defaults`](#defaults)
 - [`get`](#get)
 - [`getboolean`](#getboolean)
 - [`getfloat`](#getfloat)
 - [`getint`](#getint)
 - [`has_option`](#has_option)
 - [`has_section`](#has_section)
 - [`items`](#items)
 - [`keys`](#keys)
 - [`options`](#options)
 - [`optionxform`](#optionxform)
 - [`pop`](#pop)
 - [`popitem`](#popitem)
 - [`read`](#read)
 - [`read_dict`](#read_dict)
 - [`read_file`](#read_file)
 - [`read_string`](#read_string)
 - [`readfp`](#readfp)
 - [`remove_option`](#remove_option)
 - [`remove_section`](#remove_section)
 - [`sections`](#sections)
 - [`set`](#set)
 - [`setdefault`](#setdefault)
 - [`values`](#values)
 - [`write`](#write)

**Class/Static Methods:** 

 - [`update`](#update)

**Class/Static Attributes:** 

 - [`BOOLEAN_STATES`](#BOOLEAN_STATES)
 - [`NONSPACECRE`](#NONSPACECRE)
 - [`OPTCRE`](#OPTCRE)
 - [`OPTCRE_NV`](#OPTCRE_NV)
 - [`SECTCRE`](#SECTCRE)
 - [`converters`](#converters)

### **SafeConfigParser**`#!py3 (*args, **kwargs)` { #SafeConfigParser-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**add_section**`#!py3 (self, section)` { #add_section data-toc-label=add_section }

Create a new section in the configuration.  Extends
RawConfigParser.add_section by validating if the section name is
a string.
### *obj*.**clear**`#!py3 (self)` { #clear data-toc-label=clear }

D.clear() - None.  Remove all items from D.
### *obj*.**defaults**`#!py3 (self)` { #defaults data-toc-label=defaults }


### *obj*.**get**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>)` { #get data-toc-label=get }

Get an option value for a given section.

If `vars' is provided, it must be a dictionary. The option is looked up
in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
If the key is not found and `fallback' is provided, it is used as
a fallback value. `None' can be provided as a `fallback' value.

If interpolation is enabled and the optional argument `raw' is False,
all interpolations are expanded in the return values.

Arguments `raw', `vars', and `fallback' are keyword only.

The section DEFAULT is special.
### *obj*.**getboolean**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getboolean data-toc-label=getboolean }


### *obj*.**getfloat**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getfloat data-toc-label=getfloat }


### *obj*.**getint**`#!py3 (self, section, option, *, raw=False, vars=None, fallback=<object object at 0x00934920>, **kwargs)` { #getint data-toc-label=getint }


### *obj*.**has_option**`#!py3 (self, section, option)` { #has_option data-toc-label=has_option }

Check for the existence of a given option in a given section.
If the specified `section' is None or an empty string, DEFAULT is
assumed. If the specified `section' does not exist, returns False.
### *obj*.**has_section**`#!py3 (self, section)` { #has_section data-toc-label=has_section }

Indicate whether the named section is present in the configuration.

The DEFAULT section is not acknowledged.
### *obj*.**items**`#!py3 (self, section=<object object at 0x00934920>, raw=False, vars=None)` { #items data-toc-label=items }

Return a list of (name, value) tuples for each option in a section.

All % interpolations are expanded in the return values, based on the
defaults passed into the constructor, unless the optional argument
`raw' is true.  Additional substitutions may be provided using the
`vars' argument, which must be a dictionary whose contents overrides
any pre-existing defaults.

The section DEFAULT is special.
### *obj*.**keys**`#!py3 (self)` { #keys data-toc-label=keys }

D.keys() - a set-like object providing a view on D's keys
### *obj*.**options**`#!py3 (self, section)` { #options data-toc-label=options }

Return a list of option names for the given section name.
### *obj*.**optionxform**`#!py3 (self, optionstr)` { #optionxform data-toc-label=optionxform }


### *obj*.**pop**`#!py3 (self, key, default=<object object at 0x00934098>)` { #pop data-toc-label=pop }

D.pop(k[,d]) - v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
### *obj*.**popitem**`#!py3 (self)` { #popitem data-toc-label=popitem }

Remove a section from the parser and return it as
a (section_name, section_proxy) tuple. If no section is present, raise
KeyError.

The section DEFAULT is never returned because it cannot be removed.
### *obj*.**read**`#!py3 (self, filenames, encoding=None)` { #read data-toc-label=read }

Read and parse a filename or an iterable of filenames.

Files that cannot be opened are silently ignored; this is
designed so that you can specify an iterable of potential
configuration file locations (e.g. current directory, user's
home directory, systemwide directory), and all existing
configuration files in the iterable will be read.  A single
filename may also be given.

Return list of successfully read files.
### *obj*.**read_dict**`#!py3 (self, dictionary, source='<dict>')` { #read_dict data-toc-label=read_dict }

Read configuration from a dictionary.

Keys are section names, values are dictionaries with keys and values
that should be present in the section. If the used dictionary type
preserves order, sections and their keys will be added in order.

All types held in the dictionary are converted to strings during
reading, including section names, option names and keys.

Optional second argument is the `source' specifying the name of the
dictionary being read.
### *obj*.**read_file**`#!py3 (self, f, source=None)` { #read_file data-toc-label=read_file }

Like read() but the argument must be a file-like object.

The `f' argument must be iterable, returning one line at a time.
Optional second argument is the `source' specifying the name of the
file being read. If not given, it is taken from f.name. If `f' has no
`name' attribute, `???' is used.
### *obj*.**read_string**`#!py3 (self, string, source='<string>')` { #read_string data-toc-label=read_string }

Read configuration from a given string.
### *obj*.**readfp**`#!py3 (self, fp, filename=None)` { #readfp data-toc-label=readfp }

Deprecated, use read_file instead.
### *obj*.**remove_option**`#!py3 (self, section, option)` { #remove_option data-toc-label=remove_option }

Remove an option.
### *obj*.**remove_section**`#!py3 (self, section)` { #remove_section data-toc-label=remove_section }

Remove a file section.
### *obj*.**sections**`#!py3 (self)` { #sections data-toc-label=sections }

Return a list of section names, excluding [DEFAULT]
### *obj*.**set**`#!py3 (self, section, option, value=None)` { #set data-toc-label=set }

Set an option.  Extends RawConfigParser.set by validating type and
interpolation syntax on the value.
### *obj*.**setdefault**`#!py3 (self, key, default=None)` { #setdefault data-toc-label=setdefault }

D.setdefault(k[,d]) - D.get(k,d), also set D[k]=d if k not in D
### *obj*.**values**`#!py3 (self)` { #values data-toc-label=values }

D.values() - an object providing a view on D's values
### *obj*.**write**`#!py3 (self, fp, space_around_delimiters=True)` { #write data-toc-label=write }

Write an .ini-format representation of the configuration state.

If `space_around_delimiters' is True (the default), delimiters
between keys and values are surrounded by spaces.
### *SafeConfigParser*.**update**`#!py3 (*args, **kwds)` { #update data-toc-label=update }

D.update([E, ]**F) - None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v
### *SafeConfigParser*.**BOOLEAN_STATES** *class 'dict'* default: *{'1': True, 'yes': True, 'true': True, 'on': True, '0': False, 'no': False, 'false': False, 'off': False}* { #BOOLEAN_STATES data-toc-label=BOOLEAN_STATES }


### *SafeConfigParser*.**NONSPACECRE** *class 're.Pattern'* default: *re.compile('\\S')* { #NONSPACECRE data-toc-label=NONSPACECRE }


### *SafeConfigParser*.**OPTCRE** *class 're.Pattern'* default: *re.compile('\n        (?Poption.*?)                    # very permissive!\n        \\s*(?Pvi=|:)\\s*              # any number of space/tab,\n                                           # followed by any of t, re.VERBOSE)* { #OPTCRE data-toc-label=OPTCRE }


### *SafeConfigParser*.**OPTCRE_NV** *class 're.Pattern'* default: *re.compile('\n        (?Poption.*?)                    # very permissive!\n        \\s*(?:                             # any number of space/tab,\n        (?Pvi=|:)\\s*                 # optionally followed , re.VERBOSE)* { #OPTCRE_NV data-toc-label=OPTCRE_NV }


### *SafeConfigParser*.**SECTCRE** *class 're.Pattern'* default: *re.compile('\n        \\[                                 # [\n        (?Pheader[^]]+)                  # very permissive!\n        \\]                                 # ]\n        ', re.VERBOSE)* { #SECTCRE data-toc-label=SECTCRE }


### *SafeConfigParser*.**converters** *class 'property'* default: *configparser.ConverterMapping object at 0x039366F0* { #converters data-toc-label=converters }



______

## **WindowsExeVersionInfo**`#!py3 class` { #WindowsExeVersionInfo data-toc-label=WindowsExeVersionInfo }



**Base Classes:**

PlasticFile


**Magic Methods:**

 - [`__init__`](#WindowsExeVersionInfo-init)

**Instance Methods:** 

 - [`copyright`](#copyright)
 - [`debug`](#debug)
 - [`fromLines`](#fromLines)
 - [`injectLine`](#injectLine)
 - [`internalName`](#internalName)
 - [`path`](#path)
 - [`read`](#read)
 - [`remove`](#remove)
 - [`toLines`](#toLines)
 - [`version`](#version)
 - [`write`](#write)

**Instance Attributes:** 

 - [`major`](#major)
 - [`minor`](#minor)
 - [`micro`](#micro)
 - [`build`](#build)
 - [`companyName`](#companyName)
 - [`productName`](#productName)
 - [`description`](#description)
 - [`exeName`](#exeName)

**Class/Static Methods:** 

 - [`defaultPath`](#defaultPath)

### **WindowsExeVersionInfo**`#!py3 ()` { #WindowsExeVersionInfo-init data-toc-label="&lowbar;&lowbar;init&lowbar;&lowbar;" }

Initialize self.  See help(type(self)) for accurate signature.
### *obj*.**copyright**`#!py3 (self)` { #copyright data-toc-label=copyright }


### *obj*.**debug**`#!py3 (self)` { #debug data-toc-label=debug }


### *obj*.**fromLines**`#!py3 (self, lines)` { #fromLines data-toc-label=fromLines }


### *obj*.**injectLine**`#!py3 (self, injection, lineNo)` { #injectLine data-toc-label=injectLine }


### *obj*.**internalName**`#!py3 (self)` { #internalName data-toc-label=internalName }


### *obj*.**path**`#!py3 (self)` { #path data-toc-label=path }


### *obj*.**read**`#!py3 (self)` { #read data-toc-label=read }


### *obj*.**remove**`#!py3 (self)` { #remove data-toc-label=remove }


### *obj*.**toLines**`#!py3 (self)` { #toLines data-toc-label=toLines }


### *obj*.**version**`#!py3 (self, isCommaDelim=False)` { #version data-toc-label=version }


### *obj*.**write**`#!py3 (self)` { #write data-toc-label=write }


### *obj*.**major** *class 'int'* default: *0* { #major data-toc-label=major }


### *obj*.**minor** *class 'int'* default: *0* { #minor data-toc-label=minor }


### *obj*.**micro** *class 'int'* default: *0* { #micro data-toc-label=micro }


### *obj*.**build** *class 'int'* default: *0* { #build data-toc-label=build }


### *obj*.**companyName** *class 'str'* default: *"&lt;empty string&gt;"* { #companyName data-toc-label=companyName }


### *obj*.**productName** *class 'str'* default: *"&lt;empty string&gt;"* { #productName data-toc-label=productName }


### *obj*.**description** *class 'str'* default: *"&lt;empty string&gt;"* { #description data-toc-label=description }


### *obj*.**exeName** *class 'str'* default: *"&lt;empty string&gt;"* { #exeName data-toc-label=exeName }


### *WindowsExeVersionInfo*.**defaultPath**`#!py3 ()` { #defaultPath data-toc-label=defaultPath }



______

