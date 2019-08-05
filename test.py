# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Chrome()
#
# browser.get("https://m.2gis.ru/moscow/search/%D1%80%D0%B5%D1%81%D0%BD%D0%B8%D1%86%D1%8B?lang=ru&m=37.585011%2C55.774368%2F17")
# time.sleep(1)
#
# elem = browser.find_element_by_tag_name("body")
#
# no_of_pagedowns = 20
#
# while no_of_pagedowns:
#     elem.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)
#     no_of_pagedowns-=1
#
# post_elems = browser.find_elements_by_class_name("minicardPlain__title")
#
# for post in post_elems:
#     print(post.text)
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://medium.com/top-100/december-2013")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("post-item-title")

for post in post_elems:
    print(post.text)