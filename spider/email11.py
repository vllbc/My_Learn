from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://mail.qq.com/")
browser.switch_to.frame('login_frame')
browser.find_element_by_id("u").clear()
browser.find_element_by_id("u").send_keys("1683070754")
browser.find_element_by_id("p").clear()
browser.find_element_by_id("p").send_keys("WangLingbo6")
browser.find_element_by_id("login_button").click()
print(browser)

