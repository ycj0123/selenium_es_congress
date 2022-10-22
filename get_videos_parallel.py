from multiprocessing import Process
import pandas as pd
import requests
from tqdm import tqdm
from os import makedirs
from os.path import join
import time

download_path = '/mnt/storage2t/spanish_congress'
makedirs(download_path, exist_ok=True)

source_df = pd.read_csv('video_downloaded.csv', index_col=0)
print(source_df)
links = source_df['link'].tolist()

class Download(Process):
    def __init__(self, dir_path, link, idx):
        super(Process, self).__init__()
        self.dir_path = dir_path
        self.link = link
        self.idx = idx

    def run(self):
        filepath = join(self.dir_path, self.link.split('/')[-1])
        # print(f'Started {filepath}')
        with open (filepath, "wb") as f:
            f.write(requests.get(self.link).content)
            f.flush()
        # print(f'Finished {filepath}')

p = [None for _ in range(64)]
for i, l in enumerate(tqdm(links)):
    if source_df.loc[i, 'downloaded'] == 1:
        continue
    # else:
    #     print(source_df.loc[i])

    for j in range(len(p)):
        if p[j] is not None:
            if not p[j].is_alive():
                p[j].close()
                p[j] = Download(download_path, l, i)
                p[j].start()
                break
        else:
            p[j] = Download(download_path, l, i)
            p[j].start()
            break
    
    next_loop = False
    while next_loop == False:
        for job in p:
            if job is not None:
                if not job.is_alive():
                    source_df.loc[job.idx, 'downloaded'] = 1
                    source_df.to_csv('video_downloaded.csv')
                    next_loop = True
                    break
            else:
                next_loop = True
                break
        time.sleep(1)
    