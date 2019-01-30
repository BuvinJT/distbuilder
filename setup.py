from setuptools import setup

# Override standard setuptools commands. 
# Enforce the order of dependency installation
#-------------------------------------------------
PREREQS = [ "six" ]

from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

def requires( packages ): 
    from os import system
    from sys import executable as PYTHON_PATH
    from pkg_resources import require
    require( "pip" )
    CMD_TMPLT = '"' + PYTHON_PATH + '" -m pip install %s'
    for pkg in packages: system( CMD_TMPLT % (pkg,) )   	

class OrderedInstall( install ):
    def run( self ):
        requires( PREREQS )
        install.run( self )        
        
class OrderedDevelop( develop ):
    def run( self ):
        requires( PREREQS )
        develop.run( self )        
        
class OrderedEggInfo( egg_info ):
    def run( self ):
        requires( PREREQS )
        egg_info.run( self )        

CMD_CLASSES = { 
     "install" : OrderedInstall
   , "develop" : OrderedDevelop
   , "egg_info": OrderedEggInfo 
}        
#-------------------------------------------------

# get __version__ and readme
exec( open('distbuilder/_version.py').read() ) 
with open( "README.md", "r" ) as f: readme = f.read()

setup (	
	name             = "distbuilder",
	version          = __version__,  # @UndefinedVariable
	author           = "BuvinJ",
    author_email     = "buvintech@gmail.com",
    description      = "Wrapper for other libraries and tools including PyInstaller, " +
    				   "the Qt Installer Framework, Opy (a code obfuscater), PIP, and more.",
    long_description = readme,
    long_description_content_type = "text/markdown",
    keywords=[ 
		'distbuilder', 'dist', 
		'distribution', 'install', 'package',
		'distutils', 'setuptools'		 
	],
    url              = "https://github.com/BuvinJT/distbuilder",	
	classifiers=[
		"Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",        
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Build Tools",
		'Natural Language :: English',		
		"Development Status :: 3 - Alpha"
    ],    
	packages         = ["distbuilder"],
	install_requires = [		  
          "six"           # Forced as a prerequisite too
        , "ast"   
		, "PyInstaller"   
		, "opy_distbuilder"  
	],
	include_package_data=True, # extra files defined in MANIFEST.in
    cmdclass = CMD_CLASSES
)
