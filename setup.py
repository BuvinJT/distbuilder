from setuptools import setup
from distbuilder import __version__
setup (
	name        = 'distbuilder',
	version     = __version__,
	description = 'Assorted utility wrappers and functions for building distributions.',
	author      = 'BuvinJ',
	packages    = ['distbuilder'],
	install_requires = [
		  'six'
		, 'PyInstaller'   # Tested on PyInstaller v3.4 
		, 'Opy==1.1.28.1' # Custom Opy Fork 
	]  
)
