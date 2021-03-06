@ECHO OFF

SET SUCCESS_CODE=0
SET ERROR_CODE=1
SET "FILE_NAME=distbuilder_bat_example.txt"

SET "desktopPath=%userprofile%\Desktop"
SET "filePath=%desktopPath%\%FILE_NAME%"

ECHO "Hello World!" > "%filePath%"

IF EXIST "%filePath%" (
    ECHO "Created: %filePath%" 
    SET retCode=%SUCCESS_CODE%
) else (
    ECHO "Could not create: %filePath%" 1>&2
    SET retCode=%ERROR_CODE%
)

EXIT /b %retCode%