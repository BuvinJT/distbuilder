if "%LIB_DIR%" == "" set "LIB_DIR=%~dp0"

set "PopupLib=%LIB_DIR%\Popups.bat"

Call %PopupLib% ShowInfoPopup "Hello World!"
Call %PopupLib% ShowErrorPopup "Whoops!" 
