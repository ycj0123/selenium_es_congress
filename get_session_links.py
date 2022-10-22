# selenium 4
import pandas as pd
import pickle
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

with open('saved_links.pickle', 'rb') as f:
    saved_links = pickle.load(f)

all_vids = []
all_titles = []
all_dates = []
for l in saved_links:
    driver.get(l)
        
    table_element = driver.find_element(By.CSS_SELECTOR, 'table[class="table table-striped table-hover table-agenda"]')
    vid_elements = table_element.find_elements(By.CSS_SELECTOR, 'a[target="_blank"][rel="noopener noreferrer"]')
    vids = [e.get_attribute('href') for e in vid_elements]
    # print(vids)

    row_elements = table_element.find_elements(By.TAG_NAME, 'tr')
    title_elements = [e.find_elements(By.TAG_NAME, 'td')[1] for e in row_elements if len(e.find_elements(By.TAG_NAME, 'td')) == 4]
    titles = [e.text.split('\n')[0] for e in title_elements]
    # print(titles)


    if len(titles) == len(vids):
        dates = [l for _ in titles]
        all_vids = all_vids + vids
        all_titles = all_titles + titles
        all_dates = all_dates + dates
        df = pd.DataFrame({'link_date': all_dates, 'title': all_titles, 'link': all_vids})
        df.to_csv('video_links.csv')


# with open('inconsistent.pickle', 'wb') as f:
#     pickle.dump(inconsistent, f)