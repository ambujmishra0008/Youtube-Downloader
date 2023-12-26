from pytube import YouTube
from pytube.contrib.playlist import Playlist
import os

PLAYLIST_LINK = "https://www.youtube.com/watch?v=JwynE-3tCXY&list=PLiIEMWCZ1m9EPbpuJur25AGe6gCgP_zR_"
DIR_NAME = "crux_project"

BASE_DIR = os.getcwd()
os.chdir(BASE_DIR)

os.mkdir(DIR_NAME)
SAVE_PATH = os.chdir(DIR_NAME)
# SAVE_PATH = /Users/ambuj.kumar/Desktop/demo/crux_project

playlist = Playlist(PLAYLIST_LINK)
print("playlist:", playlist.title)

yt_videos =playlist.videos

idx = 0
for yt_video in yt_videos:
    try:
        idx = idx+1
        yt_stream_query = yt_video.streams
        yt_stream = yt_stream_query.get_highest_resolution()
        # yt_stream = yt_stream_query.filter(resolution = '1080p', progressive=True)
        print(f"downloading {yt_stream.default_filename} size: {yt_stream.filesize_mb}.mb")
        yt_stream.download(output_path = SAVE_PATH, filename=f"{idx}_{yt_stream.default_filename}")
    except:
        print("fail to download video ", idx)

