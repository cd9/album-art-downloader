#!/usr/bin/env python3

import re
from sacad import search_and_download, SUPPORTED_IMG_FORMATS
import asyncio
from sys import argv

IMAGE_WIDTH = 500
CONCURRENCY = 25

if len(argv) > 1 and argv[1].isnumeric():
  IMAGE_WIDTH = int(argv[1])

async def download_album_art(artist, album):
  fname = re.sub(r'\W+', '', artist+album)
  await search_and_download(album, artist, SUPPORTED_IMG_FORMATS["png"], IMAGE_WIDTH,
                            f'{fname}.png', size_tolerance_prct=25, amazon_tlds=(), no_lq_sources=False, preserve_format=False)

data = []
with open("input.txt", "r") as f:
  for line in f.readlines():
    data.append(line.split("-"))

async def download_all(): 
  all_tasks = []
  for d in data:
    print(f"Downloading {d}")
    if len(all_tasks)<CONCURRENCY and d != data[-1]:
      all_tasks.append(download_album_art(d[0], d[1][:-1]))
    else:
      await asyncio.gather(*all_tasks)
      all_tasks = []

asyncio.run(download_all())