@echo off
call %~dp0..\bin\pyenv-virtualenv-props.bat %*
exit /b %ERRORLEVEL%
