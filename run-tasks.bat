@echo off

start watch
set /a days=0

:while_a_day
if %days% lss 8 (

	timeout /t 86400

	set /a days+=1
	REM echo days: %days%
	type .\assets\txt\updates.txt
	echo.
	python update.py all
	goto while_a_day
)

python clean.py all
set /a days=0

goto while_a_day