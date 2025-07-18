@echo off
REM Windows Command Line Script (Batch) to activate virtual environment.
REM
REM Dependencies:
REM   * pyenv
REM   * pyenv-virtualenv-init
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM For legal details see documentation.
REM
REM 2025-07-18
REM
REM This script is located in the subfolder "shims"
REM in the project main directory.
REM
REM The script returns RC = 0 or another value in case of
REM error.
REM
REM NOTOCE: The "setlocal" command jeopardizes the activation.
REM         Do not use it,
REM         So, all variables must be global now and the  
REM         locally used ones must be undefined at the end.
REM

REM Check if virtual environment is already activated.
if not "%_PYENV_VENV_DEACTIVATE%"=="" goto obsolete
if not "%_PYENV_VENV_OLD_PATH%"=="" goto obsolete
if not "%_PYENV_VENV_OLD_PROMPT%"=="" goto obsolete
REM Check if "pyenv" is installed
if "%PYENV_ROOT%"=="" goto error0
if not exist "%PYENV_ROOT%" goto error0
REM Parse dynamically positional arguments
set "_PYENV_VERSION=*"
set "_PYENV_NAME=*"
if "%~1"=="" goto scanversion
	if "%~2"=="" goto parse1
		 set "_PYENV_VERSION=%~1"
		 set "_PYENV_NAME=%~2"
		 REM STATUS: Input by arguments is complete.
		 goto activate
	:parse1
		set "_PYENV_NAME=%~1"
		REM STATUS: Input by argument gave name, but version is missing.
		goto scanversion
:scanversion
REM Scan for
REM locally inherited version, virtual global version or global version.
cd > "%~dp0.cwd.~"
set /p _PYENV_FOLDER=<"%~dp0.cwd.~"
:loopversion1
	REM DEBUG: echo Trying folder "%_PYENV_FOLDER%" ...
	if exist "%_PYENV_FOLDER%\.python-version" goto breakversion1
	REM Detect "oldest" ancestor folder by string length
	echo %_PYENV_FOLDER% > %~dp0.len.~
	for %%j in (%~dp0.len.~) do set /a _PYENV_STR_LEN=%%~zj - 3
	REM DEBUG: echo Remaining string length: %_PYENV_STR_LEN%
	if %_PYENV_STR_LEN% leq 3 goto breakversion2
	REM Get next ancestor folder
	for %%i in ("%_PYENV_FOLDER%\..") do set "_PYENV_FOLDER=%%~fi"
	REM Continue loop
	goto loopversion1
:breakversion1
    REM Load locally inherited version
	set /p _PYENV_VERSION=<"%_PYENV_FOLDER%\.python-version"
	REM DEBUG: echo Locally inherited version: %_PYENV_VERSION%
	goto scanname
:breakversion2
	REM Scan for virtual global python version
	if not exist "%PYENV_ROOT%plugins\pyenv-virtualenv\version" goto elseversion1
	    REM Load virtual global version
		set /p _PYENV_VERSION=<"%PYENV_ROOT%plugins\pyenv-virtualenv\version"
	    REM DEBUG: echo Virtual global version: %_PYENV_VERSION%
	    goto scanname
	:elseversion1
		REM Scan for global version
		if not exist "%PYENV_ROOT%version" goto error1
		REM Load global version
		set /p _PYENV_VERSION=<"%PYENV_ROOT%version"
	    REM DEBUG: echo Global version: %_PYENV_VERSION%
	    goto scanname
:scanname
	REM Check if name is already known
	if not "%_PYENV_NAME%"=="*" goto activate
		REM Scan for
		REM locally inherited name or virtual global name.
		cd > "%~dp0.cwd.~"
		set /p _PYENV_FOLDER=<"%~dp0.cwd.~"
		:loopname1
			REM DEBUG: echo Trying folder "%_PYENV_FOLDER%" ...
			if exist "%_PYENV_FOLDER%\.python-env" goto breakname1
			REM Detect "oldest" ancestor folder by string length
			echo %_PYENV_FOLDER% > %~dp0.len.~
			for %%j in (%~dp0.len.~) do set /a _PYENV_STR_LEN=%%~zj - 3
			REM DEBUG: echo Remaining string length: %_PYENV_STR_LEN%
			if %_PYENV_STR_LEN% leq 3 goto breakname2
			REM Get next ancestor folder
			for %%i in ("%_PYENV_FOLDER%\..") do set "_PYENV_FOLDER=%%~fi"
			REM Continue loop
			goto loopname1
		:breakname1
		    REM Load locally inherited name
			set /p _PYENV_NAME=<"%_PYENV_FOLDER%\.python-env"
			REM DEBUG: echo Locally inherited name: %_PYENV_NAME%
			goto activate
		:breakname2
			REM Scan for virtual global name
			if not exist "%_PYENV_ROOT%\plugins\pyenv-virtualenv\env" goto elsename1
			    REM Load virtual global name
				set /p _PYENV_NAME=<"%PYENV_ROOT%plugins\pyenv-virtualenv\env"
				goto activate
			:elsename1
				REM STATUS: Name cannot be determined
				goto error2
:activate
REM Remove temprary files
if exist "%~dp0.cwd.~" del "%~dp0.cwd.~"
if exist "%~dp0.len.~" del "%~dp0.len.~"
REM Check if "activate.bat" is available in expected location
if not exist "%PYENV_ROOT%versions\%_PYENV_VERSION%\envs\%_PYENV_NAME%\Scripts\activate.bat" goto error3
REM Set the %PROMPT% to _PYENV_VENV_OLD_PROMPT.
REM These is used in "deactivate.bat"
REM to regenerate old prompt and old path.
set "_PYENV_VENV_DEACTIVATE=%PYENV_ROOT%versions\%_PYENV_VERSION%\envs\%_PYENV_NAME%\Scripts\deactivate.bat"
set "_PYENV_VENV_OLD_PROMPT=%PROMPT%"
set "_PYENV_VENV_OLD_PATH=%PATH%"
REM Set the colorized Python version prompt section in light cyan
REM and theCWD section in light blue.
set "PROMPT=[96m(%_PYENV_VERSION%)[0m [94m%PROMPT%[0m"
REM Activate the selected Python version and virtual environment
REM DEBUG: echo Venv launcher: "%PYENV_ROOT%versions\%_PYENV_VERSION%\envs\%_PYENV_NAME%\Scripts\activate.bat"
call "%PYENV_ROOT%versions\%_PYENV_VERSION%\envs\%_PYENV_NAME%\Scripts\activate.bat"
if not "%ERRORLEVEL%"=="0" goto error4
set "PATH=%PYENV_ROOT%plugins\pyenv-virtualenv\shims;%PATH%"S
REM Colorize the virtual environment prompt section in yellow
set "PROMPT=[93m%PROMPT%"
goto succeed
REM Display error messages
:error0
echo.
echo [101mCRITICAL Environment variable "PYENV_ROOT" is incorrect.[0m
echo [37mINFO     Check if "pyenv" for Windows is correctly installed/configured.[0m
goto fail
:error1
echo.
echo [91mERROR	 Cannot find neither local inherited, virtual global nor global Python version.[0m
echo [37mINFO	 Use "pyenv install ..." and/or "pyenv global ..." or "pyenv virtualenv-props ..." to configure the version for first.[0m
goto fail
:error2
echo.
echo [91mERROR   Cannot determine the virtual envirionment name for Python version "%_PYENV_VERSION%".[0m
echo [37mINFO    Possibly give the name as argument or set it using "pyenv virtualenv-props ...".[0m
goto fail
:error3
echo.
echo [91mERROR   Cannot find Python virtual environment  "(%_PYENV_NAME%) (%_PYENV_VERSION%)".[0m
echo [37mINFO    Check existence by calling "pyenv virtualenvs". Check if version and name are correctly given/configured.[0m
goto fail
:error4
echo.
echo [91mERROR   Failed to activate Python virtual evvironment (RC = %ERRORLEVEL%).[0m
echo [37mINFO    Check if Python %_PYENV_VERSION% and virtual environment "%_PYENV_NAME%" are correctly installed/configured.[0m
goto fail
:obsolete
echo.
echo [93mWARNING  Virtual evvironment is already activated.[0m
goto succeed
REM Finish
:succeed
set _PYENV_VERSION=
set _PYENV_NAME=
set _PYENV_STR_LEN=
set _PYENV_FOLDER=
exit /b 0
:fail
set _PYENV_VERSION=
set _PYENV_NAME=
set _PYENV_STR_LEN=
set _PYENV_FOLDER=
exit /b 1


REM --- END OF CODE ----------------------------------------------------

