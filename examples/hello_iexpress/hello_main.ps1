if( !(Test-Path variable:global:LIB_DIR) ){ $LIB_DIR="." } # support raw testing context

Import-Module -Name "$LIB_DIR\Popups.psm1"

Show-InfoPopup( "Hello World!" )
Show-ErrorPopup( "Whoops!" )
