# Uncomment for raw/direct script development
# Comment out for IExpress Context...
#$RES_DIR="."

Import-Module -Name "$RES_DIR\popup.psm1"

Show-InfoPopup( "Hello World!" )
Show-ErrorPopup( "Whoops!" )
