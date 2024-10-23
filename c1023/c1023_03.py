### Selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
browser = webdriver.Chrome() # 크롬브라우저 띄우기
# 괄호 안 위치점(크롬드라이버가 있는) 정해주기 (D:/down/---)
# 같은 루트에 파일이 저장되어 있으면 입력하지 않아도 된다.
browser.get('https://naver.com') # 주소창에 네이버를 넣기 

# html 위치 찾기 - requests:select
# 클래스네임이 xx인 곳을 찾기
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW') 
elem.click() # elem 클릭
# browser.back() 뒤로가기
# browser.forward() 앞으로가기
# browser.refresh() 새로고침
elem = browser.find_element(By.NAME,'pw')
elem = browser.find_element(By.ID,'query')
elem.send_keys('네이버 영화') # 글자 입력
elem.send_keys(Keys.ENTER) # 엔터키 입력

browser.switch_to.window(browser.window_handles[0]) # 페이지 이동


time.sleep(10)