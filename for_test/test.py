import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from concurrent.futures.thread import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://zoon.ru/msk/m/spa_protsedury/'
path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
driver.get(url)
clicks = 8
for click in range(0, clicks):
    if click == clicks:
        print('Открытие завершено')
    else:
        button = driver.find_element_by_xpath('//*[@id="catalogContainer"]/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div[2]/div/span')
        button.click()
        sleep(4)

links = driver.find_elements_by_class_name('fs-largest')
targets = []
for link in links:
    ActionChains(driver).move_to_element_with_offset(link, -150, 1).context_click().send_keys(Keys.CONTROL, Keys.SHIFT,
                                                                                              'i').perform()
    targets.append(link.get_attribute("href"))



while a:
    b = a.pop()
    print(b)
    if b == 3:
        a.append(b)
        break