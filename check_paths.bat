@echo off
cls
REM ============================================================
REM check_paths.bat  –  Color version (ASCII-safe)
REM Verifies that required tools are installed and visible in PATH
REM ============================================================

REM Enable ANSI colors (Win10/11 build ≥16257)
for /f "tokens=2 delims==" %%A in ('"wmic os get buildnumber /value 2>nul"') do set "BUILD=%%A"
if "%BUILD%" geq "16257" reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul 2>&1

echo.
echo [36m=== Checking PATH Setup ===[0m
echo.

call :CheckTool "pwsh" "PowerShell 7"
call :CheckTool "git" "Git"
call :CheckTool "gh" "GitHub CLI"
call :CheckTool "python" "Python"
call :CheckTool "code" "Visual Studio Code"

echo.
echo [36m=== PATH (trimmed) ===[0m
echo %PATH%
echo.
echo [36m=== End of PATH Check ===[0m
echo.
pause
exit /b

:CheckTool
setlocal
set "CMD=%~1"
set "NAME=%~2"

where %CMD% >nul 2>&1
if %errorlevel%==0 (
    for /f "delims=" %%i in ('where %CMD% 2^>nul') do (
        echo [32m[OK] %NAME% found: %%i[0m
    )
) else (
    echo [31m[ERR] %NAME% not found in PATH.[0m
)
endlocal
echo.
exit /b
