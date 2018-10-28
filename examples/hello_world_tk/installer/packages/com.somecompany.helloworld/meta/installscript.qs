function Component() {}

Component.prototype.createOperations = function() {

    component.createOperations(); // required super class call

    // Create icons for the primary exe
    // on the startmenu, desktop, and in the startup folder

    if (systemInfo.productType === "windows") {
        component.addOperation( "CreateShortcut",
            "@TargetDir@/HelloWorld.exe",
            "@StartMenuDir@/@ProductName@.lnk",
            "workingDirectory=@TargetDir@",
            "iconPath=@TargetDir@/HelloWorld.exe",
            "iconId=0");
        component.addOperation( "CreateShortcut",
            "@TargetDir@/HelloWorld.exe",
            "@DesktopDir@/@ProductName@.lnk",
            "workingDirectory=@TargetDir@",
            "iconPath=@TargetDir@/HelloWorld.exe",
            "iconId=0");
    }
}