from distbuilder import( PyToBinInstallerProcess, ConfigFactory,     
    QtIfwUiPage, QtIfwSimpleTextPage, QtIfwDynamicOperationsPage, 
    QtIfwControlScript as Script,
    QT_IFW_TARGET_DIR_PAGE, QT_IFW_PRE_INSTALL )

f = configFactory  = ConfigFactory()
f.productName      = "Hello Custom Pages Example"
f.description      = "A Distribution Builder Example"
f.companyTradeName = "Some Company"
f.companyLegalName = "Some Company Inc."    
f.binaryName       = "HelloWorldTk"
f.isGui            = True        
f.entryPointPy     = "../hello_world_tk/hello.py"  
f.iconFilePath     = "../hello_world_tk/demo.ico" 
f.version          = (1,0,0,0)
f.setupName        = "HelloIfwPagesSetup"

RAW_UI_SOURCE, SIMPLE_TEXT_PAGE = range(2)

demo = RAW_UI_SOURCE

if demo==RAW_UI_SOURCE:
    # This demos the extreme flexibility you have when comes to adding custom pages
    # to the installer.
    # Try opening the demo.ui file with Qt Creator / Designer, then add some
    # UI controls and elements to the page through that WYSIWYG.
    # After saving the .ui, rebuild the installer and observe those same customizations!
    f.ifwUiPages = QtIfwUiPage( "Example", QT_IFW_TARGET_DIR_PAGE, sourcePath="demo_page.ui" )
elif demo==SIMPLE_TEXT_PAGE:
    # This demos a very easy to script page which would allow you to display 
    # dynamic text and prompts, along with the inclusion of other custom logic injections. 
    # With this method, there is no need for an external .ui resource file, or to be 
    # concerned with page design details at all!  
    f.ifwUiPages = QtIfwSimpleTextPage( "Example", QT_IFW_TARGET_DIR_PAGE, 
        title="Custom Page",
        text="This is a custom page for the @ProductName@ wizard!", 
        onEnter=( 
            Script.assignCustomPageWidgetVar( "Example" ) +
            Script.ifYesNoPopup( "Would you like to perform a dynamic action?" ) +            
                'page.description.setText( ' +
                    '"<p style=\\"color: red\\">" + page.description.text + "</p>");'
        ) 
    )
""" TODO: DEMO THIS WHOLE THING...
elif demo==DYNAMIC_OPS_PAGE:
    func = QtIfwDynamicOperationsPage.AsyncFunc(...) 
    f.ifwUiPages = QtIfwDynamicOperationsPage( name, operation="", asyncFuncs=[],
                                               order=QT_IFW_PRE_INSTALL, 
                                               onCompletedDelayMillis=None )
       
    """

p = PyToBinInstallerProcess( configFactory, isDesktopTarget=True )
p.isInstallTest = True
p.run()       