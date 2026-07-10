import sys
from yt_dlp import YoutubeDL

query = sys.argv[1]

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(f"ytsearch:{query}", download=False)
    video = info['entries'][0]
    print(video['id'])