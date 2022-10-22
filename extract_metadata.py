from gettext import find
import pandas as pd
import requests
from tqdm import tqdm
from os import makedirs
from os.path import join

source_df = pd.read_csv('video_links.csv', index_col=0)
idLegislature = []
date = []
session = source_df['link_session'].tolist()

for i, s in enumerate(session):
    s_list = s.split("&")
    assert len(s_list) == 4, i
    idLegislature.append(int(s_list[2].split('=')[-1]))
    date.append(str(s_list[3].split('=')[-1]))

source_df['idLegislature'] = idLegislature
source_df['date'] = date

source_df.to_csv("metadata.csv")