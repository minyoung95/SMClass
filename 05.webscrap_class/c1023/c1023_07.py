import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

url = 'http://www.daum.net'

browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.CLASS_NAME,'btn_login')
elem.click()
time.sleep(random.randint(2,5))
id = "mylim52@naver.com"
pw = ""
input_js = f'document.getElementById("loginId--1").value = "{id}";\
  document.getElementById("password--2").value = "{pw}"'
browser.execute_script(input_js)
time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,'btn_g highlight submit')
elem.click()

time.sleep(100)