
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=8Jl3N6K-fXQ')
st_query = yt.streams
stream = st_query.get_highest_resolution()
print("size :", stream.filesize_mb)
print("downloading..", stream.download("/Users/ambuj.kumar/Desktop/demo"))
