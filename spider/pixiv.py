from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from lxml import etree

logger = logging.getLogger('vllbc')
logger.setLevel(logging.DEBUG)

handle = logging.FileHandler('log.log', mode="w")
handle.setLevel(logging.DEBUG)
handle.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))

logger.addHandler(handle)

browser = webdriver.Chrome()
browser.get(
    "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page")
webwaiter = WebDriverWait(browser, 10)

account_input = browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[1]/input')
account_input.clear()
account_input.send_keys("vllbc66@gmail.com")


password_input = browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[2]/input')
password_input.clear()
password_input.send_keys("WangLingbo6")

button_click = browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/button')
button_click.click()

browser.implicitly_wait(10)

print(browser.get_cookies())

search_input = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/form/div/input')
search_input.clear()
search_input.send_keys("萝莉")
search_input.send_keys(Keys.ENTER)


