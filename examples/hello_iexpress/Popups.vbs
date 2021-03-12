Sub ShowInfoPopup( sMsg )
    MsgBox sMsg, vbOKOnly+vbInformation, "Success"
End Sub 

Sub ShowErrorPopup( sMsg )
    MsgBox sMsg, vbOKOnly+vbCritical, "Error"
End Sub

