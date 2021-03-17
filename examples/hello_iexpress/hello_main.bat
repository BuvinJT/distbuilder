if "%LIB_DIR%" == "" set "LIB_DIR=."

set "PopupLib=%LIB_DIR%\Popups.bat"

Call %PopupLib% ShowInfoPopup "Hello World!"
Call %PopupLib% ShowErrorPopup "Whoops!" 
