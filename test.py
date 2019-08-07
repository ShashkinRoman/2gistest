# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

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

from selenium.webdriver.common.action_chains import ActionChains #- для движения мышью
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome('C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe')

driver.get("https://m.2gis.ru/moscow/search/%D1%80%D0%B5%D1%81%D0%BD%D0%B8%D1%86%D1%8B?lang=ru")
button = driver.find_element_by_class_name('searchResults__content')
button.click()
time.sleep(1)

elem = driver.find_elements_by_class_name("minicardPlain__title")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("minicardPlain__title")

for post in post_elems:
    print(post.text)


# Пример из документации

'''import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service
service = service.Service('/path/to/chromedriver')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()'''


Actions oAction = new Actions(driver);
oAction.moveToElement(Webelement);
oAction.contextClick(Webelement).build().perform();  /* this will perform right click */
WebElement elementOpen = driver.findElement(By.linkText("Open")); /*This will select menu after right click */

elementOpen.click();