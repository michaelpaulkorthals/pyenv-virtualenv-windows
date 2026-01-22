@echo off
powershell -file "%~dp0install_mklink.ps1"
set /a RC=%ERRORLEVEL%
exit /b %RC%
