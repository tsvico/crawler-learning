#coding:utf-8
'''
Web应用程序测试的工具,selenium
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
browser = webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id("kw")
    input.send_keys("Python")
    time.sleep(2)
    input.clear()
    input.send_keys("java")
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_all_elements_located((By.ID,"content_left")))
    print browser.current_url
    js = 'alert("当前网址是:http://www.baidu.com")'
    print js
    browser.execute_script(js)
    #print browser.get_cookie()
    #print browser.page_source
    time.sleep(10)
finally:
    browser.close()