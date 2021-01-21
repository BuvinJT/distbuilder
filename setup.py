from setuptools import setup

import platform
__plat = platform.system()
IS_WINDOWS = __plat == "Windows"
IS_LINUX   = __plat == "Linux"
IS_MACOS   = __plat == "Darwin"

platform_resources = {}
if IS_WINDOWS:
    platform_resources['distbuilder'] = [
         'qtifw_res/windows/*'
        ,'code_sign_res/windows/signtool/*'
    ] 
    
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
		'distbuilder', 'dist', 'distribute', 
		'distribution', 'install', 'installer',
        'package', 'distutils', 'setuptools'		 
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
          "six"           
		, "PyInstaller"   
		, "argparse"        
        , "opy_distbuilder>=0.9.1.1" # workaround, as 0.9.2.X is still in dev...
		#, "opy_distbuilder>=0.9.2.2"  
	],
	include_package_data=True, # extra files defined in MANIFEST.in    
    package_data = platform_resources
)
