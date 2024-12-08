@echo off
set SOFTWARE_DIR=D:\Softwares
if not exist %SOFTWARE_DIR% ( 
    set SOFTWARE_DIR=%USERPROFILE%\Downloads
)

set PYTHON_DIR=%SOFTWARE_DIR%\python-3.10.8-amd64-portable
set PATH=%PYTHON_DIR%;%PYTHON_DIR%\Scripts;%PATH%

python main.py

pause