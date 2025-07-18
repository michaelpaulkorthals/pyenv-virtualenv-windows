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
REM 2025-07-10
REM
REM This script is located in the subfolder "shims"
REM in the project main directory.
REM
REM Call it by name in the special Windows CMD terminal,
REM which has been modified, calling "virtualenv.init".
REM
REM The script returns RC = 0 or another value in case of
REM error.
REM
REM NOTE: Command "setlocal" would jeopardize the deactivation.
REM	   All local variables are global inside the shell.
REM	   Finally, these must be cleaned to reduce risks.

if "%_PYENV_VENV_DEACTIVATE%"=="" goto error0
if "%_PYENV_VENV_OLD_PROMPT%"=="" goto error0
if "%_PYENV_VENV_OLD_PATH%"=="" goto error0
REM Call "%_PYENV_VENV_DEACTIVATE%" and remember its return code
call "%_PYENV_VENV_DEACTIVATE%" %*
echo %ERRORLEVEL% > "%~dp0.deactivate_rc.~" 
REM DEBUG: echo Return code: %ERRORLEVEL%
REM Restore the %_PYENV_VENV_OLD_PROMPT% before activating the virtual environment
set "PROMPT=%_PYENV_VENV_OLD_PROMPT%"
REM Restore the %_PYENV_VENV_OLD_PATH% from before activating the virtual environment
set "PATH=%_PYENV_VENV_OLD_PATH%"
REM Remove temporary variables
set _PYENV_VENV_DEACTIVATE=
set _PYENV_VENV_OLD_PROMPT=
set _PYENV_VENV_OLD_PATH=
REM Return deactivate return code
setlocal
set /p RC_STR=<"%~dp0.deactivate_rc.~"
set /a RC=%RC_STR%
REM DEBUG: echo Return code: %RC%
del "%~dp0.deactivate_rc.~" 
REM DEBUG: echo Return code: %RC%
exit /b %RC%
:error0
echo [93mWARNING  Virtual environment is not activated.[0m
exit /b 0