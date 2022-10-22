# selenium 4
import pickle
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.congreso.es/en/archivo-audiovisual')

term_element = Select(driver.find_element(by=By.ID, value='_emisiones_idLegislaturaElegida'))
terms = [e.get_attribute('value') for e in term_element.options]
# print(terms)
# year_element = Select(driver.switch_to.active_element.find_element(by=By.ID, value='calAnios'))
# years = [e.get_attribute('value') for e in year_element.options]
# month_element = Select(driver.switch_to.active_element.find_element(by=By.ID, value='calMeses'))
# months = [e.get_attribute('value') for e in month_element.options]
# print(months)

# cal_element = driver.find_element(by=By.ID, value='agenda-calendario')
# day_elements = cal_element.find_elements(By.CSS_SELECTOR, 'td[class="day actividad"]')
# day_elements.append(cal_element.find_element(By.CSS_SELECTOR, 'td[class="day today actividad"]'))
# days = [e.find_element(By.TAG_NAME, 'span').text for e in day_elements]
# print(sorted(days, key=lambda x: int(x)))
saved_links = []

for t in terms:
    term_element = Select(driver.find_element(by=By.ID, value='_emisiones_idLegislaturaElegida'))
    term_element.select_by_value(t)
    year_element = Select(driver.switch_to.active_element.find_element(by=By.ID, value='calAnios'))
    years = [e.get_attribute('value') for e in year_element.options]
    # print(years)
    for y in years:
        year_element = Select(driver.switch_to.active_element.find_element(by=By.ID, value='calAnios'))
        year_element.select_by_value(y)
        month_element = Select(driver.switch_to.active_element.find_element(by=By.ID, value='calMeses'))
        months = [e.get_attribute('value') for e in month_element.options]
        for m in months:
            month_element = Select(driver.switch_to.active_element.find_element(by=By.ID, value='calMeses'))
            month_element.select_by_value(m)
            cal_element = driver.find_element(by=By.ID, value='agenda-calendario')
            day_elements = cal_element.find_elements(By.CSS_SELECTOR, 'td[class="day actividad"]')
            day_elements.append(cal_element.find_element(By.CSS_SELECTOR, 'td[class="day today actividad"]'))
            days = [e.find_element(By.TAG_NAME, 'span').text for e in day_elements]
            days.sort(key=lambda x: int(x))
            new_links = [f'https://www.congreso.es/en/archivo-audiovisual?p_p_id=emisiones&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_emisiones_idLegislaturaElegida={t}&_emisiones_dia={d}&_emisiones_mes={str(int(m)+1)}&_emisiones_anio={y}' for d in days]
            print(f'Processing the {t:2}th term {y:4}/{int(m)+1:2}')
            print(f'New links:')
            for l in new_links:
                print(l)
            saved_links = saved_links + new_links
        with open('saved_links.pickle', 'wb') as f:
            pickle.dump(saved_links, f)
        print('Saving links')
driver.quit()