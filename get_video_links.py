# selenium 4
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

source_df = pd.read_csv('session_links.csv', index_col=0)
sessions = source_df['link'].tolist()

all_vids = []
all_titles = []
all_sessions = []
err_link = []
err_msg = []
for l in sessions:
    driver.get(l)
    try:
        table_element = driver.find_element(By.CSS_SELECTOR, 'table[class="tablaSesionesSemidirecto"]')
        vid_elements = table_element.find_elements(By.XPATH, '//a[contains(@href, ".mp4")]')
        vids = [e.get_attribute('href') for e in vid_elements]
        vids = list(np.unique(np.array(vids)))
        # print(vids)
        # quit()

        title_elements = driver.find_elements(By.CSS_SELECTOR, 'span[title="Reproducir video"]')
        titles = [e.text for e in title_elements]
        # print(titles)
        # print(len(title_elements))
        # quit()

        if len(titles) == len(vids):
            sessions = [l for _ in titles]
            all_vids = all_vids + vids
            all_titles = all_titles + titles
            all_sessions = all_sessions + sessions
            output_df = pd.DataFrame({'link_session': all_sessions, 'title': all_titles, 'link': all_vids})
            output_df.to_csv('video_links.csv')
        else:
            print('Title and video numbers don\'t match.', l)
            err_link.append(l)
            err_msg.append('Title and video numbers don\'t match.')
            err_df = pd.DataFrame({'link': err_link, 'message': err_msg})
            err_df.to_csv('err_log.csv')
    except Exception as e:
        print(e, l)
        err_link.append(l)
        err_msg.append(e)
        err_df = pd.DataFrame({'link': err_link, 'message': err_msg})
        err_df.to_csv('err_log.csv')
    