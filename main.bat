@echo off
set /p port="Please, enter with the port: "
if not [%port%] == [] goto launch
  set port="9092"
:launch

echo Launching xabbo.py on port %port%

python "code\main.py" -p %port%
pause
