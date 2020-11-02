from distbuilder import updatePip, \
    installPyInstaller, uninstallPyInstaller, \
    installQtIfw, unInstallQtIfw

def updatePyInstaller():
    uninstallPyInstaller()
    installPyInstaller()

def updateQtIfw():
    # Typically, you'll need to specify the version to uninstall here...
    try:
        #unInstallQtIfw( version="3.1.1" )
        unInstallQtIfw( version="3.2.2" ) 
    except Exception as e: print(e)    
    installQtIfw()
    
updatePip()
updatePyInstaller()
updateQtIfw()