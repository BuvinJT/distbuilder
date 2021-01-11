from distbuilder import PyToBinInstallerProcess, ConfigFactory, \
    QtIfwSimpleTextPage, QT_IFW_TARGET_DIR_PAGE, QtIfwControlScript as Script

f = configFactory  = ConfigFactory()
f.productName      = "Hello Custom Installer UI Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorldTk"
f.isGui            = True        
f.entryPointPy     = "../hello_world_tk/hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwUiSetup"

f.ifwUiPages = QtIfwSimpleTextPage( "Example", QT_IFW_TARGET_DIR_PAGE, 
    title="Custom Page",
    text="This is a custom page for the @ProductName@ wizard!", 
    onEnter=( Script.assignCustomPageWidgetVar( "Example" ) +
        Script.ifYesNoPopup( "Would you like to perform a dynamic action?" ) +            
            'page.description.setText( ' +
                '"<p style=\\"color: red\\">" + page.description.text + "</p>");'
    ) 
)

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       