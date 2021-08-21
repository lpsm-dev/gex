@echo off
set /p port="Please, enter with the port: "
if not [%port%] == [] goto launch
  set port="9092"
:launch

echo Launching gex on port %port%

python "gex\main.py" -p %port%
pause
