# 🎬 YouTube Notes Generator

> **Transform YouTube videos into visual study notes automatically**

Convert any YouTube video or playlist into frame-by-frame PDF notes. Perfect for students, researchers, and anyone who learns visually.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## 🌟 Features

- **📥 Multi-source Support** — Download single videos or entire playlists
- **🖼️ Smart Frame Extraction** — Captures frames every 5 seconds using FFmpeg
- **📄 Auto-PDF Generation** — Creates organized PDF notes per video
- **📦 Batch Export** — Packages everything into a convenient ZIP file
- **⚡ Progress Tracking** — Real-time progress bars for all operations
- **🧹 Safe Filenames** — Automatically sanitizes names for cross-platform compatibility
- **⚠️ Dependency Checks** — Detects missing tools and provides installation guidance

---

## 📋 Table of Contents

- [Requirements](#-requirements)
- [Installation](#-installation)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [Usage](#-usage)
- [Output Structure](#-output-structure)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧰 Requirements

### System Requirements
- **Python** 3.9 or higher
- **FFmpeg** (required for video processing)
- **10GB+** free disk space (for video processing)
- Internet connection

### Python Dependencies
All dependencies are installed automatically via `requirements.txt`:
- `yt-dlp` — YouTube video downloader
- `opencv-python` — Video frame extraction
- `Pillow` — Image processing
- `reportlab` — PDF generation
- `tqdm` — Progress bars

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-notes-generator.git
cd youtube-notes-generator
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

#### Windows

**Option A: Using Package Manager (Recommended)**
```powershell
# Using Chocolatey
choco install ffmpeg

# Using Scoop
scoop install ffmpeg

# Using Winget (Windows 10/11)
winget install ffmpeg
```

**Option B: Manual Installation**
1. Download from [gyan.dev/ffmpeg](https://www.gyan.dev/ffmpeg/builds/)
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your System PATH:
   - Press `Win + X` → System → Advanced system settings
   - Environment Variables → System variables → Path → Edit
   - Add new entry: `C:\ffmpeg\bin`
4. Restart PowerShell/Command Prompt

**Verify Installation:**
```powershell
ffmpeg -version
```

#### macOS

```bash
# Using Homebrew (recommended)
brew install ffmpeg

# Using MacPorts
sudo port install ffmpeg
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

---

## ▶️ Usage

### Basic Usage

Run the script:
```bash
python main.py
```

You'll be prompted to:
1. **Enter YouTube URL** (video or playlist)
2. **Choose output location** for the ZIP file
3. **Confirm** if FFmpeg warning appears

### Example Session

```
=== YouTube Notes Generator ===

Enter YouTube playlist URL: https://www.youtube.com/playlist?list=...
Enter output ZIP file path: lecture_notes.zip

Processing playlist...
✓ Found 12 videos

Downloading: Introduction to Python
Progress: [████████████████████] 100%

Extracting frames...
Progress: [████████████████████] 100%

Generating PDF...
✓ Saved: output/1_Introduction_to_Python.pdf

...

✓ All notes saved to: lecture_notes.zip
```

---

## 📁 Output Structure

```
output/
├── 1_Video_Title/
│   ├── frames/
│   │   ├── frame_0000.jpg
│   │   ├── frame_0001.jpg
│   │   └── ...
│   └── 1_Video_Title.pdf
├── 2_Another_Video/
│   ├── frames/
│   └── 2_Another_Video.pdf
└── playlist_notes.zip (final output)
```

Each PDF contains:
- Video title as header
- All extracted frames in chronological order
- Optimized layout for readability

---

## ⚙️ Configuration

### Adjust Frame Extraction Rate

Edit `main.py` to change the frame capture interval:

```python
# Extract every 5 seconds (default)
fps = cap.get(cv2.CAP_PROP_FPS)
interval = int(fps * 5)  # Change '5' to your desired seconds

# Examples:
# Every 3 seconds: int(fps * 3)
# Every 10 seconds: int(fps * 10)
# Every frame: 1
```

### Custom Output Directory

Modify the output path in `main.py`:

```python
output_dir = "my_custom_output"  # Default: "output"
```

---

## 🛠️ Troubleshooting

### FFmpeg Not Found

**Error:**
```
⚠️ WARNING: FFmpeg not found!
```

**Solution:**
1. Install FFmpeg using instructions above
2. Restart your terminal/command prompt
3. Verify with: `ffmpeg -version`

### Video Download Fails

**Common Causes:**
- Video is private/unavailable
- Age-restricted content
- Region-locked video

**Solution:**
```bash
# Update yt-dlp to latest version
pip install --upgrade yt-dlp
```

### Permission Denied Errors

**Windows:**
```powershell
# Run PowerShell as Administrator
Right-click PowerShell → Run as administrator
```

**macOS/Linux:**
```bash
# Check directory permissions
chmod +w output/
```

### Out of Disk Space

**Solution:**
- Each video requires ~500MB-2GB during processing
- Clean up `output/` directory regularly
- Process playlists in smaller batches

### PDF Generation Fails

**Error:**
```
Error generating PDF: ...
```

**Solution:**
```bash
# Reinstall reportlab
pip uninstall reportlab
pip install reportlab
```

---

## ❓ FAQ

**Q: Can I process age-restricted videos?**  
A: Some age-restricted videos may require authentication. Consider using cookies from your browser with `yt-dlp`.

**Q: How long does processing take?**  
A: Depends on video length and quality. Typical 10-minute video: ~2-3 minutes.

**Q: Can I extract audio as well?**  
A: Currently video-only. Audio extraction could be added in future versions.

**Q: Is there a maximum playlist size?**  
A: No hard limit, but longer playlists require more disk space and time.

**Q: Can I customize PDF layout?**  
A: Yes! Edit the PDF generation section in `main.py` to adjust:
- Image sizes
- Margins
- Headers/footers
- Page orientation

**Q: Does this work with private videos?**  
A: No, only publicly accessible videos can be downloaded.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions
- [ ] Audio transcription to text
- [ ] OCR for text extraction from frames
- [ ] GUI interface
- [ ] Parallel video processing
- [ ] Custom templates for PDFs
- [ ] Integration with note-taking apps

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**TL;DR:** Free to use, modify, and distribute. Just keep the original license notice.

---

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Robust YouTube downloader
- [FFmpeg](https://ffmpeg.org/) — Video processing backbone
- [ReportLab](https://www.reportlab.com/) — PDF generation library

---

## ⭐ Star History

If this project helped you, consider giving it a ⭐ on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/youtube-notes-generator&type=Date)](https://star-history.com/#yourusername/youtube-notes-generator&Date)

---

<div align="center">

**Made with ❤️ by [Your Name]**

[Report Bug](https://github.com/yourusername/youtube-notes-generator/issues) · [Request Feature](https://github.com/yourusername/youtube-notes-generator/issues)

</div>

