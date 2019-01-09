@echo off

set /a errors=0

:while_no_errors
	timeout /t 600
	type .\assets\txt\watching.txt

	python watch.py

	echo error watching files
	set /a errors+=1
	if %errors% gtr 7 (
		goto reset_task
	)
	else (
		goto while_no_errors
	)

:reset_task
	type .\assets\txt\errors.txt
	echo %DATE% %TIME% >> .\watcher-errors.log
	set /a errors=0
	goto while_no_errors