import subprocess
import shutil
import re

def clean_title(title):
    """
    Clean a title to be a valid Windows filename.
    Removes or replaces invalid characters: < > : " / \ | ? * and control characters.
    """
    # Windows invalid characters: < > : " / \ | ? *
    # Also remove control characters (0-31) and replace with underscore
    invalid_chars = r'[<>:"/\\|?*\x00-\x1f]'
    cleaned = re.sub(invalid_chars, '_', title)
    
    # Remove leading/trailing spaces and dots (Windows doesn't allow these)
    cleaned = cleaned.strip(' .')
    
    # Replace multiple consecutive underscores with a single one
    cleaned = re.sub(r'_+', '_', cleaned)
    
    # Windows doesn't allow certain reserved names, but we'll just ensure it's not empty
    if not cleaned or cleaned.isspace():
        cleaned = "untitled"
    
    # Limit length to 255 characters (Windows path limit)
    if len(cleaned) > 255:
        cleaned = cleaned[:255]
    
    return cleaned

def check_ffmpeg():
    """Check if FFmpeg is available in the system PATH."""
    return shutil.which("ffmpeg") is not None

def get_ffmpeg_info():
    """Get FFmpeg version if available, otherwise return None."""
    if not check_ffmpeg():
        return None
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            # Extract version from first line
            version_line = result.stdout.split('\n')[0]
            return version_line
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None
