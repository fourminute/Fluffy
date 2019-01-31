@echo off

rem Check if we already have a venv folder. If so, stop and exit
if exist .\venv\ (
	echo.
	echo Previous Virtual Environment detected!
	echo Fluffy should already be ready to run!
	echo.
	echo If you want to recreate the Virtual Environment, please delete the `venv\` folder
	echo.
	timeout /T 5 1> NUL
	exit /B
)

rem First, create the virtual environment.
rem IMPORTANT: virtualenv utility doens't work with pythonw! Using the stdlib one!
cls
echo.
echo Performing first time setup of the Virtual Environment for Fluffy. Please wait...
echo.
python -m venv venv 1> NUL

rem Activate the virtual environment
echo.
echo Activating Virtual Environment...
echo.
call venv\Scripts\activate.bat

rem Upgrade the pip install in the enviroment to the latest
echo.
echo Upgrading venv's pip installation...
echo.
easy_install -U pip 1> NUL

rem Install the required packages on the environment
echo.
echo Installing required packages for Fluffy...
echo.
pip install -r requirements.txt 1> NUL

rem Print success message and wait 5 seconds before closing
echo.
echo Setup complete! You can run Fluffy now!
echo.
timeout /T 5
