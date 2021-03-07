Add-Type -AssemblyName PresentationCore,PresentationFramework

$SUCCESS_CODE = 0
$ERROR_CODE   = 1
$FILE_NAME    = "distbuilder_ps1_example.txt"

$DesktopPath = [Environment]::GetFolderPath( "Desktop" )
$FilePath    = Join-Path $DesktopPath $FILE_NAME

Set-Content -Path $FilePath -Value "Hello World!"

if( (Test-Path $FilePath -PathType Leaf) ) {
    Write-Host "Created: $FilePath"
    [System.Windows.MessageBox]::Show( "Created: $FilePath", "Success",
        [System.Windows.MessageBoxButton]::Ok, 
        [System.Windows.MessageBoxImage]::Information )
    $RetCode = $SUCCESS_CODE
}
else {
    Write-Error "Could not created: $FilePath"
    [System.Windows.MessageBox]::Show( "Could not created: $FilePath", "Error", 
        [System.Windows.MessageBoxButton]::Ok, 
        [System.Windows.MessageBoxImage]::Error )
    $RetCode = $ERROR_CODE
}

[Environment]::Exit( $RetCode )