import os
import re

albums = []
artists = []
def download_album_art(artist, album):
    fname = re.sub(r'\W+', '', artist+album)
    os.system(f'sacad "{artist}" "{album}" 1500 {fname}.png')

data = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        data.append(line.split("-"))

for d in data:
    print(f"Downloading {d}")
    download_album_art(d[0], d[1][:-1])
