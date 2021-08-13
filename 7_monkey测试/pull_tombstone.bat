@echo off
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)

setlocal ENABLEDELAYEDEXPANSION

@echo ------------------- ADB ROOT -----------------------

::adb wait-for-device
adb wait-for-device

@adb root
call :delay_ms 2000

md log_file

@echo ------------------- push  blacklist-----------------
adb push blacklist.txt /data/blacklist.txt

set test_ig_num=3
set test_no_ig_num=1
set event_num=200000
set delay_time=2000
set /a ii=1
echo=
REM @echo ------------------- test 0--------------------------

REM adb shell monkey --pkg-blacklist-file /data/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v -v -v %event_num% > log_file/log0.txt


@echo ------------------- ignore crash--------------------


@echo ------------------- test 1--------------------------

adb shell monkey --pkg-blacklist-file /data/blacklist.txt -s 1597350977063 --throttle %delay_time% --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v -v -v %event_num% > log_file/log_ig_crash1.txt

@echo ------------------- test 2--------------------------

adb shell monkey --pkg-blacklist-file /data/blacklist.txt -s 1597301604329 --throttle %delay_time% --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v -v -v %event_num% > log_file/log_ig_crash2.txt

@echo ------------------- test 3--------------------------

adb shell monkey --pkg-blacklist-file /data/blacklist.txt -s 1597377445313 --throttle %delay_time% --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v -v -v %event_num% > log_file/log_ig_crash3.txt


@echo ------------------- no ignore crash--------------------


@echo ------------------- test no_ig 1--------------------------


adb shell monkey --pkg-blacklist-file /data/blacklist.txt --throttle %delay_time% --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v -v -v %event_num% > log_file/log_no_ig_crash1.txt

echo test_num=%%I,event_num=%event_num%




echo=
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