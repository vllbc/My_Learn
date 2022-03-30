# 淘宝搜索

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# input = browser.find_element_by_id('q')
# input.send_keys('ipad')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# button = browser.find_element_by_class_name("search-button")
# button.click()
# browser.close()


# ------------------------------------------------------------------------------------------
# iframe


# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# ------------------------------------------------------------------------------------
# 百度搜索


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# input = browser.find_element_by_id("kw")
# input.send_keys("python")
# wait = WebDriverWait(browser,10)
# boton = wait.until(EC.presence_of_element_located((By.ID,'su')))
# boton.click()
# print(boton,input)

# -----------------------------------------------------------------------------------------------
# 运行javascript


# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore') 
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# ------------------------------------------------------------------------------------------------
# cookie操作

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("https://www.zhihu.com/explore")
# print(browser.get_cookies())
# print("\n")
# browser.add_cookie({'name':'wlb','value':'germey'})
# print(browser.get_cookies())
# print("\n")
# browser.delete_all_cookies()
# print(browser.get_cookies())


# --------------------------------------------------------------------------------------------
# 选项卡操作

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')  # 开始打开百度
browser.execute_script('window.open()')  # 用js建立新的空白页
print(browser.window_handles)  # 显示列表有两个网页
# noinspection PyDeprecation
browser.switch_to.window(browser.window_handles[1])  # 切换到第二个
browser.get('https://www.taobao.com')  # 打开淘宝
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])  # 切换到第一个
browser.get('https://python.org')  # 打开python官网

# ---------------------------------------------------------------------------------------------------
#
