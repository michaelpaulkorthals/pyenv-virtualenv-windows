@echo off
setlocal
REM Windows Command Line Script (Batch) to open the documentation
REM in the default web browser.
REM
REM It does not wait and returns immediately.
REM 
REM Dependencies:
REM   * Default web browser
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM See documentation for legal details.
REM 2025-07-08
REM
REM This script is located in the sub folder "docs"
REM in the project main directory.
REM
REM Simply open it in Windows Explorer or call it by command:
REM   > pyenv virtualenv --docs

set "FILE_PATH=%~dp0\html\index.html"
if not exist %FILE_PATH% goto error1
REM Show what is going on here
echo [37mINFO     Opening documentation in default web browser ...[0m
REM Open the documentation
start "Doxygen Documentation" "%FILE_PATH%"
echo [92mSUCCESS  DONE.[0m
endlocal
exit /b 0
REM Error messages
:error1
echo.
echo [91mERROR    Cannot find the documention index HTML file.[0m
echo [37mINFO     Check/Reinstall the program.[0m
echo.
pause
endlocal
exit /b 1
