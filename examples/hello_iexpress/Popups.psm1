Add-Type -AssemblyName PresentationCore,PresentationFramework

function Show-InfoPopup {
param( $msg )
   [System.Windows.MessageBox]::Show( $msg, "Information",
        [System.Windows.MessageBoxButton]::Ok, 
        [System.Windows.MessageBoxImage]::Information )
}

function Show-ErrorPopup {
param( $msg )
    [System.Windows.MessageBox]::Show( $msg, "Error", 
        [System.Windows.MessageBoxButton]::Ok, 
        [System.Windows.MessageBoxImage]::Error )
}

Export-ModuleMember -Function Show-InfoPopup
Export-ModuleMember -Function Show-ErrorPopup