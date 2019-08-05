import requests
from concurrent.futures.thread import ThreadPoolExecutor
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def proxy_and_headers():
#     http_proxy  = "http://1.10.137.253:8080"
#     https_proxy = "https://1.10.137.253:8080"
#     proxy_dict = {
#                   "http"  : http_proxy,
#                   "https" : https_proxy,
#                 }
#     ua = UserAgent()
#     header = {'User-Agent': str(ua.chrome)}
#     return header
    pass


def get_urls_ads(url_page, object):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    html = requests.get(url_page, headers=header).text #C проккси и заголовком
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all(attrs={'class': 'minicardPlain__title'}) #дописать класс, который нужно искать
    for page in pages:
        object.urls.append(page.find('a').get('href'))





def get_info_from_ads(url, header, object):
    try:
        html = requests.get('https://m.2gis.ru' + url, headers=header).text
        ad = BeautifulSoup(html, 'html.parser')
        try:
            title = ad.find(attrs={'class':'firmCardHeader__title'}).contents
        except:
            title = 'не получен'
        try:
            description = ad.find(attrs={'class':'firmCardHeader__extension'}).contents
        except:
            description = 'не получен'
        try:
            phone1 = ad.find(attrs={'class':'contacts__contact'}).contents
        except:
            phone1 = 'не получен'
        try:
            phone2 = ad.find(attrs={'class':'contacts__contact'}).contents
        except:
            phone2 = 'не получен'
        try:
            ads = {'title' : title,
                   'description' : description,
                   'phone1' : phone1,
                   'phone2' : phone2
                   }
            print(ads)
            object.urls.append(ads)
        except:
            print('словарь не создан')

    except:
        print('что-то пошло не так')


#убрать в будущем и работать напрямую с классом list
class Ads:
    def __init__(self):
        self.ads = []
        self.counter = 0
        self.urls = []

    def return_ads(self):
        return self.ads


object = Ads()


Base = declarative_base()


class InformationFromAds(Base):
    __tablename__ = 'Тeстовой название таблицы'
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    title = Column(String)
    price = Column(String)
    url = Column(String)


engine = create_engine('sqlite:///test_data_mbase.db')
session_object = sessionmaker()
session_object.configure(bind=engine)
Base.metadata.create_all(engine)
session = session_object()


def main():
    ads = Ads()
    zapros = 'ресницы'
    region = 'moscow'
    url_page = 'https://m.2gis.ru/' + region + '/search/' + zapros
    get_urls_ads(url_page, ads)
    with ThreadPoolExecutor(max_workers=1) as executor:
        for url_ad in ads.urls:
            url = executor.submit(get_info_from_ads, url_ad, ads)
            print(url)

    ads_re = ads.return_ads()
    counter = 0

    for ad in ads.ads_re:
        counter += 1
        ads_db = InformationFromAds(**ad)
        session.add(ads_db)
        if counter % 5 == 0:
            session.commit()
    session.commit()
    print(ads)


if __name__ == '__main__':
    main()