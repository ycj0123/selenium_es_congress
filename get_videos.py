from gettext import find
import pandas as pd
import requests
from tqdm import tqdm
from os import makedirs
from os.path import join

download_path = '/mnt/storage2t/spanish_congress'
makedirs(download_path, exist_ok=True)

# source_df = pd.read_csv('video_links.csv', index_col=0)
# links = source_df['link'].tolist()
# source_df['downloaded'] = 0

while True:
    # read csv again to find the first file not downloaded yet 
    source_df = pd.read_csv('video_downloaded.csv', index_col=0)
    links = source_df['link'].tolist()
    downloaded = source_df['downloaded'].tolist()
    i = downloaded.index(0)
    l = links[i]
    print(f'Start downloading file {i:5}/{len(downloaded):5}.')

    # 1 for downloading files
    source_df.loc[i, 'downloaded'] = 1
    source_df.to_csv('video_downloaded.csv')
    filepath = join(download_path, l.split('/')[-1])
    with open (filepath, "wb") as f:
        f.write(requests.get(l).content)
    # 2 for downloaded files
    source_df = pd.read_csv('video_downloaded.csv', index_col=0)
    source_df.loc[i, 'downloaded'] = 2
    source_df.to_csv('video_downloaded.csv')
    