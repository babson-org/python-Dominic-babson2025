@echo off

REM ============================================
REM check_software.bat  (failsafe version)
REM Runs check_software.ps1 under PowerShell 7
REM ============================================

REM --- Ensure folder exists ---
cd /d C:\PythonClass

if errorlevel 1 (
  echo ERROR: Could not change directory to C:\PythonClass.
  pause
  exit /b
)

REM --- Ensure PowerShell 7 is in PATH ---
where pwsh >nul 2>&1

if errorlevel 1 (
  echo "ERROR: PowerShell 7 (pwsh) not found in PATH. Install PowerShell 7 and try again."
  pause
  exit /b
)


echo Working folder: %CD%
echo Running check_software.ps1 under PowerShell 7...
echo.

REM --- Run the PowerShell script with temporary ExecutionPolicy Bypass ---
pwsh -NoProfile -ExecutionPolicy Bypass -Command "if (Test-Path '.\check_software.ps1') {Unblock-File '.\check_software.ps1'; & '.\check_software.ps1'} else {Write-Host 'Script not found in C:\PythonClass'}"


echo.
pause
