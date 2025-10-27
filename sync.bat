@echo off
REM ==========================================
REM 🔁 sync.bat — safe launcher for sync_class_to_student.ps1
REM Runs the PS1 under a temporary ExecutionPolicy Bypass
REM Prefers PowerShell 7 (pwsh) and falls back to Windows PowerShell
REM ==========================================

setlocal
set "_scriptdir=%~dp0"
set "_ps_exe="

REM Look for pwsh first
where pwsh.exe >nul 2>&1
if %errorlevel%==0 (
    set "_ps_exe=pwsh.exe"
) else (
    where powershell.exe >nul 2>&1
    if %errorlevel%==0 (
        set "_ps_exe=powershell.exe"
    )
)

if "%_ps_exe%"=="" (
    echo ERROR: No PowerShell found on PATH. Please install PowerShell 7 or use Windows PowerShell.
    pause
    endlocal
    exit /b 1
)

set "_scriptpath=%_scriptdir%sync_class_to_student.ps1"

REM Check script exists
if not exist "%_scriptpath%" (
    echo ERROR: Could not find "%_scriptpath%".
    echo Make sure this batch file is in the same folder as sync_class_to_student.ps1
    pause
    endlocal
    exit /b 2
)

echo.
echo === Running sync_class_to_student.ps1 under temporary ExecutionPolicy Bypass ===
echo Using PowerShell: %_ps_exe%
echo Script: %_scriptpath%
echo.

REM Run the script; include -NoProfile -NoLogo for a predictable environment
"%_ps_exe%" -NoProfile -NoLogo -ExecutionPolicy Bypass -File "%_scriptpath%"
set "LAST=%ERRORLEVEL%"

if %LAST% EQU 0 (
    echo.
    echo ✅ Sync completed successfully.
) else (
    echo.
    echo ⚠️  Sync finished with exit code %LAST%.  If this looks unexpected, open the PowerShell terminal and run:
    echo     %_ps_exe% -NoProfile -ExecutionPolicy Bypass -File "%_scriptpath%"
)

echo.
pause
endlocal
exit /b %LAST%
