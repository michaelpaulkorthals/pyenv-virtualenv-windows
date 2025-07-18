@echo off
call %~dp0..\bin\pyenv-virtualenv-delete.bat %*
exit /b %ERRORLEVEL%
