"""
TODO: This example, and the available functions of this nature need to be expanded upon...
"""

from distbuilder import installQtIfw, unInstallQtIfw

#TODO: Uninstall is working but throwing out a error message, 
# which seems to caused by a race condition...
unInstallQtIfw( version="3.1.1" ) 
installQtIfw()