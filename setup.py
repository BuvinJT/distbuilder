from setuptools import setup
exec(open('distbuilder/_version.py').read()) # defines __version__

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
		'Programming Language :: Python :: 2.7',
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
		  "six"
		, "PyInstaller"   # Tested on PyInstaller v3.4
		, "opy_distbuilder"  
	],
	include_package_data=True # extra files defined in MANIFEST.in 
)
