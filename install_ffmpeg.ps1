# FFmpeg Installation Helper Script for Windows
# This script helps download and set up FFmpeg on Windows

Write-Host "FFmpeg Installation Helper" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host ""

# Check if FFmpeg is already installed
$ffmpegPath = Get-Command ffmpeg -ErrorAction SilentlyContinue
if ($ffmpegPath) {
    Write-Host "FFmpeg is already installed!" -ForegroundColor Green
    Write-Host "Location: $($ffmpegPath.Source)" -ForegroundColor Gray
    ffmpeg -version | Select-Object -First 1
    exit 0
}

Write-Host "FFmpeg is not installed." -ForegroundColor Yellow
Write-Host ""
Write-Host "Installation Options:" -ForegroundColor Cyan
Write-Host "1. Manual Installation (Recommended)" -ForegroundColor White
Write-Host "   - Download from: https://www.gyan.dev/ffmpeg/builds/" -ForegroundColor Gray
Write-Host "   - Extract to C:\ffmpeg" -ForegroundColor Gray
Write-Host "   - Add C:\ffmpeg\bin to your PATH" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Using Chocolatey (if installed)" -ForegroundColor White
Write-Host "   Run: choco install ffmpeg" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Using Scoop (if installed)" -ForegroundColor White
Write-Host "   Run: scoop install ffmpeg" -ForegroundColor Gray
Write-Host ""

# Check if Chocolatey is available
$chocoPath = Get-Command choco -ErrorAction SilentlyContinue
if ($chocoPath) {
    Write-Host "Chocolatey detected! Would you like to install FFmpeg using Chocolatey? (Y/N)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -eq 'Y' -or $response -eq 'y') {
        Write-Host "Installing FFmpeg via Chocolatey..." -ForegroundColor Cyan
        choco install ffmpeg -y
        if ($LASTEXITCODE -eq 0) {
            Write-Host "FFmpeg installed successfully!" -ForegroundColor Green
            Write-Host "Please restart your terminal and run 'ffmpeg -version' to verify." -ForegroundColor Yellow
        }
        exit 0
    }
}

# Check if Scoop is available
$scoopPath = Get-Command scoop -ErrorAction SilentlyContinue
if ($scoopPath) {
    Write-Host "Scoop detected! Would you like to install FFmpeg using Scoop? (Y/N)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -eq 'Y' -or $response -eq 'y') {
        Write-Host "Installing FFmpeg via Scoop..." -ForegroundColor Cyan
        scoop install ffmpeg
        if ($LASTEXITCODE -eq 0) {
            Write-Host "FFmpeg installed successfully!" -ForegroundColor Green
        }
        exit 0
    }
}

Write-Host "For manual installation instructions, see the README.md file." -ForegroundColor Cyan
Write-Host ""
