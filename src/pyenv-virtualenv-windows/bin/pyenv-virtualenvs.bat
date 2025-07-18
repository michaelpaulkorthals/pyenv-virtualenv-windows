@echo off
setlocal
REM Windows Command Line Script (Batch) to launch "pyenv-virtualenvs.py".
REM
REM Dependencies:
REM   * pyenv
REM   * pyenv-virtualenv
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM For legal details see documentation.
REM
REM 2025-07-11
REM
REM This script is located in the subfolder "bin"
REM in the project main directory.
REM
REM Simply open it in Windows Explorer or call it by path
REM in the Windows CMD terminal.
REM
REM The script returns RC = 0 or another value in case of
REM error.

REM This job is too challenging for Windows CMD language.
REM Calling python script to bypass all the painful CMD problems.
REM Using the Python version, which is globally set by "pyenv".
call python "%~dp0pyenv-virtualenvs.py" %*
set /a RC=%ERRORLEVEL%
if %RC% equ 130 goto cancel
if %RC% neq 0 goto error1
endlocal
exit /b 0
REM Display error messages
:error1
echo.
echo [91mERROR:    Failed to list Python virtual environments (RC = %RC%).[0m
echo [37mINFO:     Check if Python, "pyenv" and plugin "pyenv-virtualenv" are correctly installed/configured.[0m
endlocal
exit /b 1
REM Cancel program silently
:cancel
endlocal
exit /b 130
