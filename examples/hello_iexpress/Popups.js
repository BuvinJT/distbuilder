function showInfoPopup( sMsg ){
    WScript.CreateObject( "WScript.Shell" ).Popup( 
        sMsg, 0, "Success", 0x0 + 0x40 ); // ok + info
}

function showErrorPopup( sMsg ){
    WScript.CreateObject( "WScript.Shell" ).Popup(
        sMsg, 0, "Error", 0x0 + 0x10 ); // ok + stop    
}

