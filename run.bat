@echo off

rem Check if we don't have a venv folder. If so, run the setup!
if not exist .\venv\ call setup.bat

rem Activate the virtual environment
call venv\Scripts\activate.bat

rem Run Fluffy!
start pythonw -m fluffy.pyw
