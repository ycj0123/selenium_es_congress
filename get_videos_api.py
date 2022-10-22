import pandas as pd
import requests
from tqdm import tqdm
import time

log_file = 'video_downloaded.csv'
source_df = pd.read_csv(log_file, index_col=0)
links = source_df['link'].tolist()

for i, l in enumerate(tqdm(links)):
    if source_df.loc[i, 'downloaded'] == 1:
        continue

    response = requests.get('https://vm88ymzsba.execute-api.ap-northeast-3.amazonaws.com/dev/es_congress_download', params={'url': l})
    # if response.ok:
    #     if response.json()['downloaded_link'] == l:
    #         print('success')
    #     else:
    #         print('return message error')
    # else:
    #     print('response not ok')
    source_df.loc[i, 'downloaded'] = 1
    source_df.to_csv(log_file)

    # time.sleep(3)