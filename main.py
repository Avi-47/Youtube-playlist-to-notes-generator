from downloader.youtube_downloader import get_playlist_info, download_single_video
from frame_extractor.extract_frames import extract_frames_from_video
from exporter.pdf_exporter import images_to_pdf
from exporter.zip_exporter import zip_output
from utils.helpers import check_ffmpeg, get_ffmpeg_info, clean_title
import os
import sys
import re

# Check for FFmpeg (warning only, as it may work for some videos without it)
if not check_ffmpeg():
    print("⚠️  WARNING: FFmpeg is not installed or not in PATH", file=sys.stderr)
    print("   Some videos may fail to download or process.", file=sys.stderr)
    print(r"   To install FFmpeg, run: .\install_ffmpeg.ps1", file=sys.stderr)
    print("   Or see README.md for installation instructions.", file=sys.stderr)
    print("")
    response = input("Continue anyway? (y/n): ").lower()
    if response != 'y':
        print("Exiting. Please install FFmpeg and try again.")
        sys.exit(1)
else:
    ffmpeg_info = get_ffmpeg_info()
    if ffmpeg_info:
        print(f"✓ {ffmpeg_info}")
        print("")

PLAYLIST_URL = input("Enter YouTube Playlist URL: ")
OUTPUT_DIR = "output"

# Ask where to save the ZIP file
print("\nWhere would you like to save the ZIP file?")
print("1. D: drive (New Volume D)")
print("2. Current project directory")
print("3. Custom path")
zip_location = input("Enter choice (1/2/3) [default: 1]: ").strip() or "1"

if zip_location == "1":
    ZIP_OUTPUT_DIR = "D:\\"
elif zip_location == "2":
    ZIP_OUTPUT_DIR = os.getcwd()
elif zip_location == "3":
    custom_path = input("Enter full path (e.g., D:\\Downloads): ").strip()
    ZIP_OUTPUT_DIR = custom_path if custom_path else os.getcwd()
else:
    ZIP_OUTPUT_DIR = "D:\\"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get playlist information first
print("📋 Getting playlist information...")
playlist_info = get_playlist_info(PLAYLIST_URL)
total_videos = len([e for e in playlist_info.get('entries', []) if e])
print(f"Found {total_videos} videos in playlist\n")

# Process each video one at a time: download → extract frames → create PDF
processed_count = 0
for idx, entry in enumerate(playlist_info.get('entries', []), start=1):
    if not entry:
        continue
    
    # Get video ID - could be 'id' or extracted from 'url'
    video_id = entry.get('id')
    if not video_id and entry.get('url'):
        # Extract ID from URL if needed
        url_match = re.search(r'[?&]v=([a-zA-Z0-9_-]+)', entry.get('url', ''))
        if url_match:
            video_id = url_match.group(1)
    
    if not video_id:
        print(f"⚠️  Skipping video {idx}: Could not get video ID")
        continue
    
    print(f"\n{'='*60}")
    print(f"Processing video {idx}/{total_videos}")
    print(f"{'='*60}")
    
    # Download the video
    print(f"⬇️  Downloading video {idx}...")
    video = download_single_video(video_id, PLAYLIST_URL, OUTPUT_DIR, idx)
    
    if not video or not video.get("path") or not os.path.exists(video["path"]):
        print(f"⚠️  Skipping video {idx}: Download failed")
        continue
    
    # Clean the title to ensure it's a valid Windows filename
    clean_video_title = video['title']
    video_dir = os.path.join(OUTPUT_DIR, f"{idx}_{clean_video_title}")
    os.makedirs(video_dir, exist_ok=True)

    try:
        # Extract frames
        print(f"🖼️  Extracting frames from video {idx}...")
        frames_dir = extract_frames_from_video(video["path"], video_dir)
        
        # Create PDF with index number in filename
        pdf_filename = f"{idx}_{clean_video_title}.pdf"
        pdf_path = os.path.join(video_dir, pdf_filename)
        print(f"📄 Creating PDF: {pdf_filename}...")
        images_to_pdf(frames_dir, pdf_path)
        
        # Optionally remove the video file to save space (uncomment if needed)
        # os.remove(video["path"])
        
        processed_count += 1
        print(f"✅ Completed video {idx}/{total_videos}: {clean_video_title}")
    except Exception as e:
        print(f"⚠️  Error processing video {idx} ({clean_video_title}): {e}")
        continue

print(f"\n{'='*60}")
print(f"Processed {processed_count}/{total_videos} videos successfully")
print(f"{'='*60}\n")

ZIP_FILE_NAME = "playlist_notes.zip"
ZIP_FILE_PATH = os.path.join(ZIP_OUTPUT_DIR, ZIP_FILE_NAME)
zip_output(OUTPUT_DIR, ZIP_FILE_PATH)

print(f"✅ ZIP file created successfully!")
print(f"📦 Location: {ZIP_FILE_PATH}")
