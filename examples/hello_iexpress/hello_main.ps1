# Uncomment for raw/direct script development
# Comment out for IExpress Context...
#$LIB_DIR="."

Import-Module -Name "$LIB_DIR\Popups.psm1"

Show-InfoPopup( "Hello World!" )
Show-ErrorPopup( "Whoops!" )
