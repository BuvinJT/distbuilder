# Uncomment for raw/direct script development
# Comment out for IExpress Context...
#$LIB_DIR="."

Import-Module -Name "$LIB_DIR\popup.psm1"

Show-InfoPopup( "Hello World!" )
Show-ErrorPopup( "Whoops!" )
