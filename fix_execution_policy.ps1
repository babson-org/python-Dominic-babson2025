# ==========================================
# 🧰 Fix Execution Policy (Temporary Only)
# ==========================================
# 1. Runs safely under ExecutionPolicy Bypass (set by .bat launcher)
# 2. Verifies PowerShell version
# 3. Unblocks setup_envirionment.ps1
# 4. Runs setup_envirionment.ps1
# 5. Verifies Git installation
# ==========================================

Write-Host "`n=== Temporary Environment Setup ===`n" -ForegroundColor Cyan

# Ensure running from correct folder
Set-Location C:\PythonClass

# --- Verify PowerShell version ---
$ver = $PSVersionTable.PSVersion.Major
if ($ver -lt 7) {
    Write-Host "❌ Please run this script in PowerShell 7 or higher (pwsh), not Windows PowerShell 5.1." -ForegroundColor Red
    exit 1
}

Write-Host "✅ PowerShell version $($PSVersionTable.PSVersion) detected." -ForegroundColor Green

# --- Unblock setup script ---
Write-Host "`n--- Unblocking setup_envirionment.ps1 ---" -ForegroundColor Yellow
if (Test-Path .\setup_envirionment.ps1) {
    Unblock-File .\setup_envirionment.ps1
    Write-Host "✅ setup_envirionment.ps1 unblocked." -ForegroundColor Green
} else {
    Write-Host "⚠️ setup_envirionment.ps1 not found in C:\PythonClass." -ForegroundColor Yellow
}

# --- Run setup script ---
Write-Host "`n--- Running setup_envirionment.ps1 ---" -ForegroundColor Yellow
try {
    pwsh -ExecutionPolicy Bypass -File .\setup_envirionment.ps1
} catch {
    Write-Host "❌ setup_envirionment.ps1 failed: $_" -ForegroundColor Red
}

# --- Verify Git installation ---
Write-Host "`n--- Checking Git installation ---" -ForegroundColor Yellow
try {
    $gitVersion = (& git --version) 2>$null
    if ($LASTEXITCODE -eq 0 -and $gitVersion) {
        Write-Host "✅ Git detected: $gitVersion" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Git not found or not on PATH." -ForegroundColor Yellow
        Write-Host "   Install manually: winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements"
    }
} catch {
    Write-Host "❌ Error checking Git installation: $_" -ForegroundColor Red
}

Write-Host "`n🎯 Setup complete. You can now run sync_class_to_student.ps1 safely.`n" -ForegroundColor Cyan
