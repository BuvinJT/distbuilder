from setuptools import setup

import os, platform
__plat = platform.system()
IS_WINDOWS = __plat == "Windows"
IS_MACOS   = __plat == "Darwin"
IS_LINUX   = __plat == "Linux"

def package_file_paths( package_dirname, exclude_dirnames=None ):
    paths = []
    for root, dirnames, filenames in os.walk( package_dirname ):
        print(root, dirnames, filenames)
        if exclude_dirnames:
            for name in exclude_dirnames:
                if name in dirnames:
                    dirnames.remove( name ) 
        for filename in filenames:
            paths.append( os.path.join('..', root, filename) )
    return paths

__RES_TOP_DIR_NAME    = "distbuilder"
__RES_SUBDIR_NAMES    = [ "util_res", "qtifw_res", "code_sign_res" ]
__PLAT_RES_DIR_NAMES  = {"Windows":"windows", "Darwin":"macos", "Linux":"linux"}
__PLAT_RES_DIR_NAME   = __PLAT_RES_DIR_NAMES[ __plat ] 
__PLAT_RES_EXCLUDE_DIR_NAMES = [ n for _,n in __PLAT_RES_DIR_NAMES.items() 
                                 if n != __PLAT_RES_DIR_NAME ]  

conditional_resources=[]
for dirname in __RES_SUBDIR_NAMES:
    conditional_resources.extend( package_file_paths( 
        os.path.join(__RES_TOP_DIR_NAME, dirname ),  
        exclude_dirnames=__PLAT_RES_EXCLUDE_DIR_NAMES ) )
conditional_resources = {'':conditional_resources}
    
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
    package_data = conditional_resources
)
