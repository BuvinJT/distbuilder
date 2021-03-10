;@echo off

;;;;; rem start of the batch part  ;;;;;
;
;for %%a in (/h /help -h -help) do ( 
;   if /I "%~1" equ "%%~a" if "%~2" equ "" (
;       echo compressing directory to cab file  
;       echo Usage:
;       echo(
;       echo %~nx0 "directory" "cabfile" [-w/-wrapper]
;       echo(
;       echo to uncompress use:
;       echo EXTRAC32 cabfile.cab /E /L .
;       echo(
;       echo Example:
;       echo(
;       echo %~nx0 "c:\directory\logs" "logs" 
;       exit /b 0
;   )
; )
;
; if "%~2" equ "" (
;   echo invalid arguments.For help use:
;   echo %~nx0 -h
;   exit /b 1
;)
;
; set "dir_to_cab=%~f1"
;
; set "path_to_dir=%~pn1"
; set "dir_name=%~n1" 
; set "drive_of_dir=%~d1"
; set "cab_file=%~2"
; 
; if not exist "%dir_to_cab%\" (
;   echo no valid directory passed
;   exit /b 1
;)

; :: Toggle the wrapper directory option
;set "wrapperdir="
;for %%a in (-w -wrapper) do ( 
;   if /I "%~3" equ "%%~a" set "wrapperdir=%dir_name%"
;)

;
;break>"%tmp%\makecab.dir.ddf"
;
;setlocal enableDelayedExpansion

;:: Generate a DDF file via a recursive directory listing
;for /d /r "%dir_to_cab%" %%a in (*) do (
;   
;   set "_dir=%%~pna"
;   set "destdir=%wrapperdir%!_dir:%path_to_dir%=!"
;   (echo(.Set DestinationDir=!destdir!>>"%tmp%\makecab.dir.ddf")
;   for %%# in ("%%a\*") do (
;       (echo("%%~f#"  /inf=no>>"%tmp%\makecab.dir.ddf")
;   )
;)
;(echo(.Set DestinationDir=!wrapperdir!>>"%tmp%\makecab.dir.ddf")
;   for %%# in ("%~f1\*") do (
;       (echo("%%~f#"  /inf=no>>"%tmp%\makecab.dir.ddf")
;   )

;:: Run makecab against the DDF file 
;makecab /F "%~f0" /f "%tmp%\makecab.dir.ddf" /d DiskDirectory1="%cd%" /d CabinetNameTemplate=%cab_file%.cab

;:: You might comment out this DDF file deletion for debugging purposes...
;del /q /f "%tmp%\makecab.dir.ddf"

;exit /b %errorlevel%

;;
;;;; rem end of the batch part ;;;;;

;;;; directives part ;;;;;
;;
.New Cabinet
.set GenerateInf=OFF
.Set Cabinet=ON
.Set Compress=ON
.Set UniqueFiles=ON
.Set MaxDiskSize=1215751680;

.set RptFileName=nul
.set InfFileName=nul

.set MaxErrors=1
;;
;;;; end of directives part ;;;;;