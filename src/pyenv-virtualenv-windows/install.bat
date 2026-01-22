@echo off
setlocal
REM Windows Command Line Script (Batch) to install the plugin "pyenv-virtualenv".
REM
REM Dependencies:
REM   * pyenv
REM   * pyenv-virtualenv
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM For legal details see documentation.
REM
REM 2025-07-31
REM
REM This script is located in the project main directory.
REM
REM Simply open it in Windows Explorer or call it by path
REM in the Windows CMD terminal.
REM
REM The script returns RC = 0 or another value in case of
REM error.

REM Get version string of the package
set /p VERSION=<"%~dp0.version"
REM Output installation purpose
echo.
echo [92mSUCCESS  -----------------------------------------------------------------------[0m
echo [92mSUCCESS  Installing/docking plugin "pyenv-virtualenv" v%VERSION% for Windows ...[0m
echo [92mSUCCESS  -----------------------------------------------------------------------[0m
echo [37mINFO     Setting up plugin folder tree ...[0m
REM Check if "pyenv" variable "PYENV_ROOT" is installed
if not defined PYENV_ROOT goto error1
REM Check if "pyenv" root folder exists
if not exist "%PYENV_ROOT%" goto error2
REM Ensure that subfolder ".\plugins" exists
if exist "%PYENV_ROOT%plugins" goto endif1
	mkdir "%PYENV_ROOT%plugins"
	set /a RC=%ERRORLEVEL%
	if %RC% neq 0 goto error3
:endif1
REM Ensure that required subfolders exist
if exist "%PYENV_ROOT%plugins\pyenv-virtualenv" goto endif2
	REM Make "pyenv-virtualenv" folder tree
	mkdir "%PYENV_ROOT%plugins\pyenv-virtualenv"
	set /a RC=%ERRORLEVEL%
	if %RC% neq 0 goto error4
:endif2
REM Copy "pyenv-virtualenv" folder tree
echo [37mINFO     Copying files could take some seconds ...[0m
if defined VERBOSE goto else3
	xcopy "%~dp0*" "%PYENV_ROOT%plugins\pyenv-virtualenv" /s /e /k /r /v /q /y
	set /a RC=%ERRORLEVEL%
	goto endif3
:else3
	set /a VERBOSE=%VERBOSE%
	if %VERBOSE% neq 0 goto else3a
		xcopy "%~dp0*" "%PYENV_ROOT%plugins\pyenv-virtualenv" /s /e /k /r /v /q /y
		set /a RC=%ERRORLEVEL%
		goto endif3a
	:else3a
		xcopy "%~dp0*" "%PYENV_ROOT%plugins\pyenv-virtualenv" /s /e /k /r /v /y
		set /a RC=%ERRORLEVEL%
	:endif3a
:endif3
if %RC% neq 0 goto error5
REM Patch the file "pyenv.bat"
REM Check "pyenv" version
set /P PYENV_VERSION=<"%PYENV_ROOT%..\.version"
if not exist "%PYENV_ROOT%plugins\pyenv-virtualenv\patch\pyenv_ptc_%PYENV_VERSION%.bat" goto error6
echo [37mINFO     Activating command forwarding from "pyenv" to "pyenv-virtualenv" ...[0m
if exist "%PYENV_ROOT%plugins\pyenv-virtualenv\shims\pyenv.bat" del /f "%PYENV_ROOT%plugins\pyenv-virtualenv\shims\pyenv.bat"
echo [37mINFO     Creating symbolic link "%PYENV_ROOT%plugins\pyenv-virtualenv\shims\pyenv.bat" → "%PYENV_ROOT%plugins\pyenv-virtualenv\patch\pyenv_ptc_%PYENV_VERSION%.bat" ...[0m
REM Check privileges
net session >nul 2>&1
if %ERRORLEVEL% == 0 goto else4
	REM Running with 'User' privileges.
	REM Bypassing Windows "'mklink' only as 'Administrator'" limitation.
	choice /C YN /M "[94mDo you permit needed 'Administrator' privileges[0m"
	if not %ERRORLEVEL% == 1 goto error7
	REM IMPORTATNT: Wait until the process returns
	powershell -command "Start-Process '%~dp0install_mklink.bat' -Verb runAs -Wait"
	goto endif4
:else4
	REM Running with 'Administrator' privileges.
	powershell -file "%~dp0install_mklink.ps1"
:endif4
set /a RC=%ERRORLEVEL%
if %RC% neq 0 goto error7
if not exist "%PYENV_ROOT%plugins\pyenv-virtualenv\shims\pyenv.bat" goto else5
	echo [92mSUCCESS  Symbolic link "%PYENV_ROOT%plugins\pyenv-virtualenv\shims\pyenv.bat" → "%PYENV_ROOT%plugins\pyenv-virtualenv\patch\pyenv_ptc_%PYENV_VERSION%.bat" has been written.[0m
	goto endif5
:else5
	set /a RC=1
	goto error7
:endif5
REM Audit the 'Machine' PATH and the 'User' PATH for path conflicts
powershell -file install_audit.ps1
set /a RC=%ERRORLEVEL%
if %RC% neq 0 goto finish
REM Set the 'shims' directory at the beginning of the 'User' PATH 
REM or 'Machine' if needed or possible.
powershell -file modify_path.ps1
set /a RC=%ERRORLEVEL%
if %RC% neq 0 goto finish
echo.
echo [92mSUCCESS  Plugin package "pyenv-virtualenv" v%VERSION% for Windows is installed (RC = %RC%).[0m
echo.
echo [95mNOTICE   You are recommended to read the unit 'Usage' in the documentation.[0m
echo [37mINFO     Execute:[0m
echo [37mINFO     "%PYENV_ROOT%plugins\pyenv-virtualenv\docs\html\index.html"[0m
goto finish
REM Display error messages
:error1
set RC=1
echo.
echo [91mERROR    Variable "PYENV_ROOT" is not set (RC = %RC%).[0m
echo [37mINFO     Check/install/configure "pyenv" for Windows. Then try again.[0m
goto finish
:error2
set RC=2
echo.
echo [91mERROR    Directory "%PYENV_ROOT%" not found (RC = %RC%).[0m
echo [37mINFO     Check/install/configure "pyenv" for Windows. Then try again.[0m
goto finish
:error3
echo.
echo [91mERROR    Cannot make directory "%PYENV_ROOT%plugins" (RC = %RC%).[0m
echo [37mINFO     Analyze/configure your file access/permissions to "%PYENV_ROOT%". Then try again.[0m
goto finish
:error4
echo.
echo [91mERROR    Cannot make directory tree in "%PYENV_ROOT%plugins" (RC = %RC%).[0m
echo [37mINFO     Analyze/configure your file access/permissions to "%PYENV_ROOT%plugins". Then try again.[0m
goto finish
:error5
echo.
echo [91mERROR    Failed to install "pyenv-virtualenv" v%VERSION% for Windows (RC = %RC%).[0m
echo [37mINFO     Observe the logging why this has going wrong. Reconfigure/repair. Then try again.[0m
goto finish
:error6
echo.
echo [91mERROR    Cannot find patch file for actual installed "pyenv" version "%PYENV_VERSION%" (RC = %RC%).[0m
copy /a /y /v "%PYENV_ROOT%bin\pyenv.bat" "%PYENV_ROOT%plugins\pyenv-virtualenv\patch\pyenv_ori_%PYENV_VERSION%.bat"
dir  "%PYENV_ROOT%plugins\pyenv-virtualenv\patch\*.*"
echo [37mINFO     Download the latest "pyenv-virtualenv" version from PyPi. Then try again.[0m
echo [37mINFO     Alternatively develop the matching patch file for version "%PYENV_VERSION%" and patch the file manually.[0m
echo [37mINFO     See the related chapter in the "Development Manual" in documentation "%PYENV_ROOT%plugins\pyenv-virtualenv\docs\html\index.html".[0m
goto finish
:error7
echo.
echo [91mERROR    Cannot create link to patch file for "pyenv" version "%PYENV_VERSION%" in the "shims" directory of this plugin (RC = %RC%).[0m
echo [37mINFO     Analyze/configure your file access/permissions to "%PYENV_ROOT%plugins\pyenv-virtualenv\shims" or decide to call this script as 'Administrator'. Then try again.[0m
goto finish
REM Exit program with return code
:finish
if exist "%~dp0.*.~~~" del /f "%~dp0.*.~~~"
exit /b %RC%


REM --- END OF CODE ----------------------------------------------------

