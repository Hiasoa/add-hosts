@echo off
echo @echo off^&cd/d %cd%^&py main.pyw^&copy hosts C:\\Windows\\System32\\drivers\\etc\\hosts^ > main.bat
echo CreateObject("Shell.Application").ShellExecute "%cd%\main.bat", "", "", "runas">"editfilepermission.vbs"
editfilepermission.vbs
