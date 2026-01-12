# Fix Chocolatey Lock File Issue
# This script removes the lock file that's preventing FFmpeg installation

Write-Host "Chocolatey Lock File Fixer" -ForegroundColor Cyan
Write-Host "==========================" -ForegroundColor Cyan
Write-Host ""

$lockFile = "C:\ProgramData\chocolatey\lib\c00565a56f0e64a50f2ea5badcb97694d43e0755"

if (Test-Path $lockFile) {
    Write-Host "Found lock file: $lockFile" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Attempting to remove lock file..." -ForegroundColor Cyan
    
    try {
        Remove-Item -Path $lockFile -Force -ErrorAction Stop
        Write-Host "Lock file removed successfully!" -ForegroundColor Green
        Write-Host ""
        Write-Host "You can now try installing FFmpeg again:" -ForegroundColor Cyan
        Write-Host "  choco install ffmpeg" -ForegroundColor White
        Write-Host ""
        Write-Host "Note: You may need to run PowerShell as Administrator for Chocolatey to work properly." -ForegroundColor Yellow
    }
    catch {
        Write-Host "Failed to remove lock file: $_" -ForegroundColor Red
        Write-Host ""
        Write-Host "You may need to:" -ForegroundColor Yellow
        Write-Host "1. Run PowerShell as Administrator" -ForegroundColor White
        Write-Host "2. Close any other Chocolatey processes" -ForegroundColor White
        Write-Host "3. Manually delete the file: $lockFile" -ForegroundColor White
    }
}
else {
    Write-Host "Lock file not found. It may have already been removed." -ForegroundColor Green
    Write-Host ""
    Write-Host "If you are still having issues, try:" -ForegroundColor Cyan
    Write-Host "1. Running PowerShell as Administrator" -ForegroundColor White
    Write-Host "2. Running: choco install ffmpeg" -ForegroundColor White
}

Write-Host ""
