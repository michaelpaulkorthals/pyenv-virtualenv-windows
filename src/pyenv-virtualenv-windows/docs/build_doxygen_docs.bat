@echo off
setlocal
REM Windows Command Line Script (Batch) to build the documentation.
REM 
REM Dependencies:
REM   * Doxygen 1.13+
REM   * ..\docs.doxyfile
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM For legal details see documentation.
REM 
REM 2025-07-10
REM
REM This script is located in the subfolder "docs"
REM in the project main directory.
REM
REM Simply open it in Windows Explorer or call it by path
REM in the Windows CMD terminal.
REM 
REM The HTML documentation will appear as subfolder ".\html".
REM
REM The script returns RC = 0 or another value in case of
REM compilation errors.

REM Show what is going on here
echo Updating documentation ...
REM Remember the original directory
cd > ".cwd.~"
set /p ORI_DIR=<".cwd.~"
del ".cwd.~"
REM Change to the drive and directory of this script
cd /d "%~dp0"
REM Change to the project root directory
REM in which the "docs" folder is located.
cd ..
REM Determine the Doxygen configuration file path
cd > ".cwd.~"
set /p CWD=<".cwd.~"
del ".cwd.~"
set "CONFIG_PATH=%CWD%\docs.doxyfile"
echo Configuring Doxygen by file:
echo %CONFIG_PATH%
REM Compile the documentation
echo Compiling. This could take a while ...
echo.
doxygen %CONFIG_PATH%
set /a RC=%ERRORLEVEL%
if %RC% neq 0 goto finish
REM Pack the Doxygen HTML documentation into '%~dp0\doxygen.zip'.
for %%I in (.) do set "BASENAME=%%~nxI"
echo.
echo Archiving into 'doxygen_%BASENAME%.zip'. This could take a while ...
cd /d "%~dp0"
if exist doxygen_%BASENAME%.zip del doxygen_%BASENAME%.zip
7z a -r doxygen_%BASENAME%.zip .\html\*.*
set /a RC=%ERRORLEVEL%
:finish
REM Check an output return code
echo.
if %RC% neq 0 goto else1
	REM Display success
	echo [92mSUCCESS  (RC = %RC%).[0m
	echo [37mINFO     But, be aware of [93mwarnings[0m in the console log.[0m
	goto endif1
:else1
	REM Display failure
	echo [91mERROR    (RC = %RC%).[0m
	echo [95mNOTICE   Check Doxygen console logging and repair.[0m
	goto endif1
:endif1
echo.
REM Pause and exit
pause
REM Change to the original drive and directory
if defined ORI_DIR cd /d %ORI_DIR%
exit /b %RC%
