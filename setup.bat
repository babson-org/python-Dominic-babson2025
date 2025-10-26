@echo off
REM ==========================================
REM 🧰 One-Time Setup  (Temporary Bypass)
REM ==========================================
setlocal
set "_scriptdir=%~dp0"

echo.
echo === Unblocking PowerShell scripts ===
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "Unblock-File '%_scriptdir%fix_execution_policy.ps1';" ^
  "Unblock-File '%_scriptdir%setup_envirionment.ps1';" ^
  "Unblock-File '%_scriptdir%sync_class_to_student.ps1'"

echo.
echo === Running fix_execution_policy.ps1 ===
REM ----------------------------------------------------
REM Try to use pwsh if it exists, otherwise fall back to
REM Windows PowerShell so it never crashes.
REM ----------------------------------------------------
where pwsh.exe >nul 2>&1
if %errorlevel%==0 (
    pwsh -ExecutionPolicy Bypass -File "%_scriptdir%fix_execution_policy.ps1"
) else (
    powershell.exe -ExecutionPolicy Bypass -File "%_scriptdir%fix_execution_policy.ps1"
)

echo.
echo ✅ Setup complete.  Close this window when finished.
pause
endlocal

