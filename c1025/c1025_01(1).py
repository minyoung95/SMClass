import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import pyautogui


# 네이버 쇼핑 검색창 입력 enter 키 입력
# 네이버  쇼핑 클릭
# 네이버 쇼핑에서 무선 마우스 검색창 입력 enter 키 입력

url = 'http://www.naver.com'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)

elem = browser.find_element(By.ID,'query')
elem.click()
elem.send_keys('네이버 쇼핑')
elem.send_keys(Keys.ENTER)
time.sleep(2)

elem = browser.find_element(By.CLASS_NAME,'link_name').click() # 새로운 탭으로 실행
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) #####탭 이동
elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.click()
elem.send_keys('무선 마우스')
elem.send_keys(Keys.ENTER)

input('엔터키 >>')