import yt_dlp
import os
import shutil
from utils.helpers import clean_title

def get_playlist_info(playlist_url):
    """Get playlist information without downloading."""
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Don't download, just get info
        'ignoreerrors': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        return info

def download_single_video(video_id, playlist_url, output_dir, index):
    """Download a single video from a playlist."""
    # Check if FFmpeg is available
    has_ffmpeg = shutil.which("ffmpeg") is not None
    
    if has_ffmpeg:
        # If FFmpeg is available, prefer best quality with merging
        format_selector = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    else:
        # If no FFmpeg, only use single-file formats (no merging required)
        # Prefer mp4, webm, or any single-file format
        format_selector = 'best[ext=mp4]/best[ext=webm]/best'
    
    # Construct video URL
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    ydl_opts = {
        'format': format_selector,
        'outtmpl': os.path.join(output_dir, f'{index}_%(title)s.%(ext)s'),
        'quiet': False,  # Show progress for individual downloads
        'prefer_free_formats': False,
        'ignoreerrors': False,  # We want to know if this specific video fails
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            if info:
                clean_title_text = clean_title(info.get('title', 'untitled'))
                video_path = ydl.prepare_filename(info)
                return {
                    "title": clean_title_text,
                    "path": video_path if os.path.exists(video_path) else None
                }
    except Exception as e:
        print(f"⚠️  Error downloading video {index}: {e}")
        return None
    
    return None
