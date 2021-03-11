:: Uncomment for raw/direct script development
:: Comment out for IExpress Context...
::set "RES_DIR=."

set "PopupLib=%RES_DIR%\popup.bat"

Call %PopupLib% ShowInfoPopup "Hello World!"
Call %PopupLib% ShowErrorPopup "Whoops!" 
