@echo off
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)

::adb wait-for-device

@REM @echo ------------------- ADB log -----------------------
@REM adb logcat -t 5 > log.txt

@echo ------------------- python -----------------------
python auto_log_analysis.py
@REM python open_file.py


@echo ------------------- EXIT ---------------------------
echo=
pause
exit

::----------- delay_ms sub-function (unit : 10 ms) --------------------
:delay_ms
@echo off
if "%1"=="" goto :eof
set delay_msTime=%1
set TotalTime=0
set NowTime=%time%
:: read init time, format : 13:01:05.95
:delay_ms_continue
set /a minute1=1%NowTime:~3,2%-100
set /a second1=1%NowTime:~-5,2%%NowTime:~-2%0-100000
set NowTime=%time%
set /a minute2=1%NowTime:~3,2%-100
set /a second2=1%NowTime:~-5,2%%NowTime:~-2%0-100000
set /a TotalTime+=(%minute2%-%minute1%+60)%%60*60000+%second2%-%second1%
if %TotalTime% lss %delay_msTime% goto delay_ms_continue
goto :eof
:ColorText
@echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof