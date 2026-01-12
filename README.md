# YouTube Notes Generator

Extracts frames from YouTube videos/playlists every 5 seconds
and exports them as a ZIP file.

## Requirements
- Python 3.9+
- yt-dlp
- FFmpeg

## Installation

### 1. Install Python dependencies
```powershell
pip install -r requirements.txt
```

### 2. Install FFmpeg on Windows

**Quick Check & Install Helper:**
```powershell
.\install_ffmpeg.ps1
```
This script will check if FFmpeg is installed and guide you through installation options.

**Manual Installation Options:**

**Option A: Using Chocolatey (if installed)**
```powershell
choco install ffmpeg
```

**Option B: Using Scoop (if installed)**
```powershell
scoop install ffmpeg
```

**Option C: Using winget (Windows 10/11)**
```powershell
winget install ffmpeg
```

**Option D: Manual Installation**
1. Download FFmpeg from https://www.gyan.dev/ffmpeg/builds/
2. Extract the zip file to a folder (e.g., `C:\ffmpeg`)
3. Add FFmpeg to your system PATH:
   - Open System Properties → Environment Variables
   - Under "System variables", find and select "Path", then click "Edit"
   - Click "New" and add the path to the `bin` folder (e.g., `C:\ffmpeg\bin`)
   - Click "OK" to save
4. Restart your terminal/PowerShell

After installation, verify FFmpeg is installed:
```powershell
ffmpeg -version
```

**Note:** The application will warn you if FFmpeg is not found, but you can still try to run it. Some videos may work without FFmpeg, but many will require it.

## Run
```powershell
python main.py
