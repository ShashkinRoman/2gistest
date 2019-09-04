import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from concurrent.futures.thread import ThreadPoolExecutor
from torrequest import TorRequest
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from selenium.webdriver.common.keys import Keys
#
# from selenium.webdriver.common.action_chains import ActionChains #- для движения мышью
# from selenium.webdriver.remote.webelement import WebElement
# from seleniumrequests import Chrome
# from selenium.webdriver.common.by import By
def take_proxy():
    pass


def get_urls_from_page(object, driver):
    # Дописать параметр сессии, для того
    # чтобы реквестом получать информацию с селениума
    driver = driver
    find_html = driver.find_element_by_tag_name('html')
    html = find_html.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    hrefs = soup.find_all(attrs={'class': 'fs-largest invisible-links'})
    for hr in hrefs:
        object.urls.append(hr.find('a').get('href'))


def get_info_from_page(url, object):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    # С помощью torrequests делаем запросы через тор
    with TorRequest() as tr:
        html = tr.get(url, headers=header).text

    ads = BeautifulSoup(html, 'html.parser')

    try:
        phone = ads.find(attrs={'class': 'js-phone phoneView phone-hidden'}).find('a').get('href').split('+')[1]
    except:
        phone = 'не получен'
    try:
        adress = ads.find(attrs={'class': 'iblock'}).text
    except:
        adress = 'не получен'
    try:
        title = ads.find(attrs={'class': 'iblock'}).text
    except:
        title = 'не получен'
    try:
        site = ads.find(attrs={'class': 'service-website'}).find('a').get('href')
    except:
        site = 'не получен'
    ads_dict = {'title': title,
                'phone': phone,
                'adress': adress,
                'site': site
                }
    object.ads.append(ads_dict)
    print(ads_dict)
# объяляем метакласс базы данных

Base = declarative_base()



# объявляем класс БД, указываем столбцы, прописываем бизнес-логику
# задаем название таблицы
class InformationFromAds(Base):
    __tablename__ = 'Moscow test'
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    title = Column(String)
    adress = Column(String)
    site = Column(String)

    def __repr__(self):
        return f'Phone: {self.phone}, имя: {self.title}'

    def __str__(self):
        return f'Phone ID: {self.phone}, имя: {self.title}'


zapros = ''
engine = create_engine('sqlite:///test data base2.db')
session_object = sessionmaker()
session_object.configure(bind=engine)
Base.metadata.create_all(engine)
session = session_object()


class Ads:
    def __init__(self):
        self.ads = []
        self.counter = 0
        self.urls = []

    def ret_ads(self):
        return self.ads


object = Ads()



def click_more(url, driver):
    try:
        jopa = driver
        counter = 0
        jopa.get(url)
        clicks = 8
        for click in range(0, clicks):
            if click == clicks:
                print('Открытие завершено')
            else:
                button = driver.find_element_by_xpath('//*[@id="catalogContainer"]/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div[2]/div/span')
                button.click()
                counter += 1
                sleep(4)
    except:
        pass


def main():
    plases = ['Авиамоторная', 'Автозаводская', 'Автозаводская%20(Московское%20центральное%20кольцо)']
    for plase in plases:
        url = 'https://zoon.ru/msk/m/uhod_za_resnitsami/?locations-metro%5B%5D=' + plase
        ads_obj = Ads()
        path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=path, options=chrome_options)
        driver.get(url)
        click_more(url, driver)
        get_urls_from_page(object, driver)
        with ThreadPoolExecutor(max_workers=25) as executor:
            for url in object.urls:
                future = executor.submit(get_info_from_page, url, object)
                print(future)
        ads = object.ret_ads()
        counter = 0
        for ad in ads_obj.ads:
            counter +=1
            ads_db = InformationFromAds(**ad)
            session.add(ads_db)
            if counter % 10 == 0:
                session.commit()
        session.commit()
        print(ads)

if __name__ == '__main__':
    main()
