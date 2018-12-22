from setuptools import setup
from distbuilder import __version__

with open( "README.md", "r" ) as f: readme = f.read()

setup (
	name             = "distbuilder",
	version          = __version__,
	author           = "BuvinJ",
    author_email     = "buvintech@gmail.com",
    description      = "Assorted utility wrappers and functions for building distributions.",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url              = "https://github.com/BuvinJT/distbuilder",	
	classifiers=[
		"Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",        
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Build Tools",
		"Development Status :: 3 - Alpha"
    ],    
	packages         = ["distbuilder","docs","examples"],
	install_requires = [
		  "six"
		, "PyInstaller"   # Tested on PyInstaller v3.4 
		, "Opy==1.1.28.1" # Custom Opy Fork 
	],
	include_package_data=True # extra files defined in MANIFEST.in 
)
