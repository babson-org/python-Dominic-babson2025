# ==========================================
# Environment Verification Script
# Checks for required software:
#   1. PowerShell 7
#   2. Git
#   3. GitHub CLI (gh)
#   4. Python 3.x
#   5. Visual Studio Code
# ==========================================

Write-Host ""
Write-Host "=== Checking Local PythonClass Environment ===`n" -ForegroundColor Cyan

# --- PowerShell 7 ---
Write-Host "PowerShell 7:" -ForegroundColor Yellow
try {
    $ver = $PSVersionTable.PSVersion.Major
    if ($ver -ge 7) {
        Write-Host "  OK - PowerShell version $($PSVersionTable.PSVersion)" -ForegroundColor Green
    } else {
        Write-Host "  MISSING - Detected Windows PowerShell $($PSVersionTable.PSVersion). Install PowerShell 7 or newer." -ForegroundColor Red
    }
} catch {
    Write-Host "  ERROR - Unable to determine PowerShell version." -ForegroundColor Red
}

# --- Git ---
Write-Host "`nGit:" -ForegroundColor Yellow
try {
    $gitVersion = (& git --version) 2>$null
    if ($LASTEXITCODE -eq 0 -and $gitVersion) {
        Write-Host "  OK - $gitVersion" -ForegroundColor Green
    } else {
        Write-Host "  MISSING - Git not found on PATH." -ForegroundColor Red
    }
} catch {
    Write-Host "  ERROR - Git check failed." -ForegroundColor Red
}

# --- GitHub CLI (gh) ---
Write-Host "`nGitHub CLI (gh):" -ForegroundColor Yellow
try {
    $ghVersion = (& gh --version 2>$null) 
    if ($LASTEXITCODE -eq 0 -and $ghVersion) {
        # gh prints multiple lines; show first line
        $first = $ghVersion -split "`n" | Select-Object -First 1
        Write-Host "  OK - $first" -ForegroundColor Green
    } else {
        Write-Host "  MISSING - GitHub CLI (gh) not found on PATH." -ForegroundColor Red
    }
} catch {
    Write-Host "  ERROR - GitHub CLI check failed." -ForegroundColor Red
}

# --- Python ---
Write-Host "`nPython:" -ForegroundColor Yellow
try {
    $pyVersion = (& python --version 2>$null)
    if ($LASTEXITCODE -eq 0 -and $pyVersion) {
        Write-Host "  OK - $pyVersion" -ForegroundColor Green
    } else {
        Write-Host "  MISSING - Python not found on PATH." -ForegroundColor Red
    }
} catch {
    Write-Host "  ERROR - Python check failed." -ForegroundColor Red
}

# --- Visual Studio Code ---
Write-Host "`nVisual Studio Code:" -ForegroundColor Yellow
try {
    $codeVersion = (& code --version 2>$null | Select-Object -First 1)
    if ($LASTEXITCODE -eq 0 -and $codeVersion) {
        Write-Host "  OK - VS Code version $codeVersion" -ForegroundColor Green
    } else {
        Write-Host "  MISSING - VS Code not found on PATH." -ForegroundColor Red
    }
} catch {
    Write-Host "  ERROR - VS Code check failed." -ForegroundC
}