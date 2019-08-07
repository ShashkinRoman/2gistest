import requests
from concurrent.futures.thread import ThreadPoolExecutor
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains #- для движения мышью
from selenium.webdriver.remote.webelement import WebElement
from seleniumrequests import Chrome
from selenium.webdriver.common.by import By


def get_urls_from_page(url, object):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all(attrs={"class": "fs-largest invisible-links"})
    for page in pages:
        object.urls8.append(page.next_element.next_element.attrs['href'])


class Ads:
    def __init__(self):
        self.flats = []
        self.counter = 0
        self.urls = []

    def ret_flats(self):
        return self.flats


object = Ads()




def click_more(url):
    counter = 0
    driver = webdriver.Chrome(
        'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe')
    driver.get(url)
    clicks = 10
    for click in range(0, clicks):
        if click == clicks:
            break
        else:
            try:
                button = driver.find_element_by_xpath('//*[@id="catalogContainer"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/span')
                button.click()
                counter += 1
                sleep(3)
            except:
                button = driver.find_element_by_xpath('//*[@id="catalogContainer"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/span')
                button.click()
                counter += 1
                sleep(5)



def main():
    url = 'https://zoon.ru/msk/m/spa_protsedury/'
    ads_obj = Ads()


if __name__ == '__main__':
    main()


options = new ChromeOptions();