import pandas as pd

link_list = pd.read_csv('video_links.csv', index_col=0)
log = pd.read_csv('video_downloaded.csv', index_col=0)
links = log['link'].tolist()
count = [0 for _ in links]
link_list['downloaded'] = 0
for i in range(len(log)):
    if link_list.loc[i, 'link'] == log.loc[i, 'link']:
        link_list.loc[i, 'downloaded'] = 1

print(link_list['downloaded'].to_numpy().sum())
link_list.to_csv('video_downloaded_cal.csv')