from __future__ import unicode_literals
import youtube_dl
import json

ydl_opts = {}
with youtube_dl.YoutubeDL() as ydl:
    url = ydl.extract_info('https://www.youtube.com/watch?v=fsu5ZZwzFyk', download=False)
    print(url ["formats"] [-1] ["url"])
