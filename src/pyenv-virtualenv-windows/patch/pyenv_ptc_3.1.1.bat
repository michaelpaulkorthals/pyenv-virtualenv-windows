@echo off
setlocal
chcp 65001 >nul 2>&1

REM --------------------------------------------------------------------
REM --- PATCH 1 FOR PYENV-VIRTUALENV 2025-07-14 ---
REM --------------------------------------------------------------------

REM Determine log level
if not defined LOG_LEVEL goto log_level1
  set /a LOG_LEVEL=%LOG_LEVEL% 
  goto log_level2
:log_level1
  set /a LOG_LEVEL=20
:log_level2

REM Determine pyenv root folder
if not defined PYENV_ROOT goto undefined0
if not exist "%PYENV_ROOT%" goto nonexist0
goto continue0
undefined0:
  echo [101mCRITICAL Cannot find "PYENV_ROOT" environment variable.[0m
  echo [37mINFO     Check/install/configure "pyenv". Then try again.[0m
  exit /b 1
:nonexist0
  echo [101mCRITICAL Cannot find environment "pyenv root" directory "%PYENV_ROOT%".[0m
  echo [37mINFO     Check/repair/configure "pyenv". Then try again.[0m
  exit /b 1
:continue0

REM NOTE: In addition all substrings "%~dp0..\" has been replaced
REM by "%PYENV_ROOT%" to make this script independent from its location
REM on the system hard disk.

REM --------------------------------------------------------------------

set "pyenv=cscript //nologo "%PYENV_ROOT%libexec\pyenv.vbs""

:: if 'pyenv' called alone, then run pyenv.vbs
if [%1]==[] (
  %pyenv% || goto :error
  exit /b
)

set "skip=-1"
for /f "delims=" %%i in ('echo skip') do (call :incrementskip)
if [%skip%]==[0] set "skip_arg="
if not [%skip%]==[0] set "skip_arg=skip=%skip% "

if /i [%1%2]==[version] call :check_path

:: use pyenv.vbs to aid resolving absolute path of "active" version into 'bindir'
set "bindir="
set "extrapaths="
for /f "%skip_arg%delims=" %%i in ('%pyenv% vname') do call :extrapath "%PYENV_ROOT%versions\%%i"

:: Add %AppData% Python Scripts to %extrapaths%.
for /F "tokens=1,2 delims=-" %%i in ('%pyenv% vname') do (
  if /i "%%j" == "win32" (
    for /F "tokens=1,2,3 delims=." %%a in ("%%i") do (
        set "extrapaths=%extrapaths%%AppData%\Python\Python%%a%%b-32\Scripts;"
    )
  ) else (
     for /F "tokens=1,2,3 delims=." %%a in ("%%i") do (
        set "extrapaths=%extrapaths%%AppData%\Python\Python%%a%%b\Scripts;"
    )
  )
)

:: all help implemented as plugin
if /i [%2]==[--help] goto :plugin
if /i [%1]==[--help] (
  call :plugin %2 %1 || goto :error
  exit /b
)
if /i [%1]==[help] (
  if [%2]==[] call :plugin help --help || goto :error
  if not [%2]==[] call :plugin %2 --help || goto :error
  exit /b
)

:: let pyenv.vbs handle these
set "commands=rehash global local version vname version-name versions commands shims which whence help --help"
for %%a in (%commands%) do (
  if /i [%1]==[%%a] (
    rem endlocal not really needed here since above commands do not set any variable
    rem endlocal closed automatically with exit
    rem no need to update PATH either
    %pyenv% %* || goto :error
    exit /b
  )
)

:: jump to plugin or fall to exec
if /i not [%1]==[exec] goto :plugin
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:exec

if not exist "%bindir%" (
  echo No global/local python version has been set yet. Please set the global/local version by typing:
  echo pyenv global 3.7.4
  echo pyenv local 3.7.4
  exit /b 1
)

set cmdline=%*
set cmdline=%cmdline:~5%

:: update PATH to active version and run command
:: endlocal needed only if cmdline sets a variable: SET FOO=BAR
call :remove_shims_from_path
%cmdline% ||  goto :error

endlocal
exit /b
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:remove_shims_from_path
set "python_shims=%PYENV_ROOT%shims"
call :normalizepath "%python_shims%" python_shims
set "_path=%path%"
set "path=%extrapaths%"

:: arcane magic courtesy of StackOverflow question 5471556
:: https://stackoverflow.com/a/7940444/381865
setlocal DisableDelayedExpansion
:: escape all special characters
set "_path=%_path:"=""%"
set "_path=%_path:^=^^%"
set "_path=%_path:&=^&%"
set "_path=%_path:|=^|%"
set "_path=%_path:<=^<%"
set "_path=%_path:>=^>%"
set "_path=%_path:;=^;^;%"
:: the 'missing' quotes below are intended
set _path=%_path:""="%
:: " => ""Q (like quote)
set "_path=%_path:"=""Q%"
:: ;; => "S"S (like semicolon)
set "_path=%_path:;;="S"S%"
set "_path=%_path:^;^;=;%"
set "_path=%_path:""="%"
setlocal EnableDelayedExpansion

:: "Q => <empty>
set "_path=!_path:"Q=!"
:: "S"S => ";"
for %%a in ("!_path:"S"S=";"!") do (
  if "!!"=="" (
    endlocal
    endlocal
  )
  if %%a neq "" (
    if /i not "%%~dpfa"=="%python_shims%" call :append_to_path %%~dpfa
  )
)

exit /b
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:append_to_path
set "path=%path%%*;"
exit /b
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:plugin
set "exe=%PYENV_ROOT%libexec\pyenv-%1"
rem TODO needed?
call :normalizepath %exe% exe

if exist "%exe%.bat" (
  set "exe=call "%exe%.bat""

) else if exist "%exe%.cmd" (
  set "exe=call "%exe%.cmd""

) else if exist "%exe%.vbs" (
  set "exe=cscript //nologo "%exe%.vbs""

) else if exist "%exe%.lnk" (
  set "exe=start '' "%exe%.bat""
) else (
  REM --------------------------------------------------------------------
  REM --- PATCH 2 FOR PYENV-VIRTUALENV 2025-07-14 ---
  REM --------------------------------------------------------------------
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Cannot find executable "%exe%.*".[0m
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Redirecting command "pyenv %1" to related plugin ...[0m
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Working around entropy caused by deviations from 'pyenv-virtualenv' common command design ...[0m
  REM Determine the plugin name
  REM NOTE: The "virtualenv" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="virtualenv" goto redirect_to_virtualenv
  REM NOTE: The "virtualenvs" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="virtualenvs" goto redirect_to_virtualenv
  REM NOTE: The "activate" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="activate" goto redirect_to_virtualenv
  REM NOTE: The "deactivate" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="deactivate" goto redirect_to_virtualenv
  goto endworkaround1
  :redirect_to_virtualenv
    set "PLUGIN_NAME=virtualenv"
    goto continue1
  :endworkaround1
    if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Detecting plugin name in command name "%1" ...[0m
    for /f "tokens=1 delims=-" %%a in ("%1") do set "PLUGIN_NAME=%%a"
	REM NOTE: All commands starting with "venv-" will be redirected to "pyenv-virtualenv".
	if "%PLUGIN_NAME%"=="venv" goto redirect_to_virtualenv
	REM NOTE: All other commands will be forwarded to other installed plugins if available.
	goto continue1
  :continue1
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Plugin name: "%PLUGIN_NAME%".[0m
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Plugin command: "%1".[0m
  REM Forward the command to the detected plugin
  set "exe=%PYENV_ROOT%plugins\pyenv-%PLUGIN_NAME%\libexec\pyenv-%1"
  call :normalizepath %exe% exe
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Plugin call: "%exe%".[0m
  REM Calculate path to existing executable only
  if exist "%exe%.bat" (
    set "exe=call "%exe%.bat""
  ) else if exist "%exe%.cmd" (
    set "exe=call "%exe%.cmd""
  ) else if exist "%exe%.vbs" (
    set "exe=cscript //nologo "%exe%.vbs""
  ) else if exist "%exe%.lnk" (
    set "exe=start '' "%exe%.bat""
  ) else (
	REM Not existing
    if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Cannot find executable "%exe%.*".[0m
    echo pyenv: no such command '%1'
	REM Cancel with error level 1
    exit /b 1
  )
  REM The following 2 lines are obsolete now and has been commented:
  REM echo pyenv: no such command '%1'
  REM exit /b 1
  
  REM ------------------------------------------------------------------
)

:: replace first arg with %exe%
set cmdline=%*
set cmdline=%cmdline:^=^^%
set cmdline=%cmdline:!=^!%
set "arg1=%1"
set "len=1"
:loop_len
set /a len=%len%+1
set "arg1=%arg1:~1%"
if not [%arg1%]==[] goto :loop_len

setlocal enabledelayedexpansion
set cmdline=!exe! !cmdline:~%len%!
:: run command (no need to update PATH for plugins)
:: endlocal needed to ensure exit will not automatically close setlocal
:: otherwise PYTHON_VERSION will be lost
endlocal && endlocal && %cmdline% || goto :error
exit /b
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: convert path which may have relative nodes (.. or .)
:: to its absolute value so can be used in PATH
:normalizepath
set "%~2=%~dpf1"
goto :eof
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: compute list of paths to add for all activated python versions
:extrapath
call :normalizepath %1 bindir
set "extrapaths=%extrapaths%%bindir%;%bindir%\Scripts;%bindir%\bin;"
goto :eof
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: check pyenv python shim is first in PATH
:check_path
set "python_shim=%PYENV_ROOT%shims\python.bat"
if not exist "%python_shim%" goto :eof
call :normalizepath "%python_shim%" python_shim
set "python_where="
for /f "%skip_arg%delims=" %%a in ('where python') do (
  if /i "%python_shim%"=="%%~dpfa" goto :eof
  call :set_python_where %%~dpfa
)
call :bad_path "%python_where%"
exit /b
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: set python_where variable if empty
:set_python_where
if "%python_where%"=="" set "python_where=%*"
goto :eof
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: tell bad PATH and exit
:bad_path
set "bad_python=%~1"
set "bad_dir=%~dp1"
echo [91mFATAL: Found [95m%bad_python%[91m version before pyenv in PATH.[0m
echo [91mPlease remove [95m%bad_dir%[91m from PATH for pyenv to work properly.[0m
goto :eof
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: if AutoExec/AutoRun is configured for cmd it probably ends with the `cls` command
:: meaning there will be a Form Feed (U+000C) included in the output.
:: so we add it as a dilimiter so that we can skip x number of lines.
:: we find out how many to skip and pass that tot the skip option of the for loop,
:: EXCEPT skip=0 gives errors...
:: so we prepend every command with `echo skip` to force skip being at least 1
:incrementskip
set /a skip=%skip%+1
goto :eof

:error
exit /b %errorlevel%
