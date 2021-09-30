#!/usr/bin/env python3

import re
from sacad import search_and_download, SUPPORTED_IMG_FORMATS
import asyncio
from sys import argv

image_width = 500
if len(argv) > 1 and argv[1].isnumeric():
  image_width = int(argv[1])


async def download_album_art(artist, album):
  fname = re.sub(r'\W+', '', artist+album)
  await search_and_download(album, artist, SUPPORTED_IMG_FORMATS["png"], image_width,
                            f'{fname}.png', size_tolerance_prct=25, amazon_tlds=(), no_lq_sources=False, preserve_format=False)

data = []
with open("input.txt", "r") as f:
  for line in f.readlines():
    data.append(line.split("-"))


all_tasks = []
for d in data:
  print(f"Downloading {d}")
  all_tasks.append(download_album_art(d[0], d[1][:-1]))


async def await_tasks():
  await asyncio.gather(*all_tasks)

asyncio.run(await_tasks())
