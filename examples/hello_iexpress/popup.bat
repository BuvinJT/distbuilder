@echo off

call :%*
exit /b %errorlevel%

:ShowInfoPopup
start "Information" /wait cmd /c "echo %~1 & pause"
exit /b 0

:ShowErrorPopup
start "Error" /wait cmd /c "echo %~1 & pause"
 exit /b 0