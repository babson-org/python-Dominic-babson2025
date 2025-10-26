# ==========================================
# 🔁 Weekly Sync Launcher (Safe Temporary Bypass)
# ==========================================
# Runs sync_class_to_student.ps1 even if the system
# execution policy is restrictive. Does NOT persist
# any changes to the user or machine policy.
# ==========================================

& {
    # 1️⃣ Temporarily allow scripts in this session only
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

    # 2️⃣ Run the actual sync script
    $scriptPath = "C:\PythonClass\sync_class_to_student.ps1"
    if (Test-Path $scriptPath) {
        Write-Host "`n🔁 Running sync_class_to_student.ps1 under temporary bypass..." -ForegroundColor Cyan
        . $scriptPath
        Write-Host "`n✅ Sync complete (or terminated after GitHub login prompt)." -ForegroundColor Green
    } else {
        Write-Host "❌ sync_class_to_student.ps1 not found at $scriptPath" -ForegroundColor Red
    }
}
