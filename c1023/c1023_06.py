import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

url='http://www.naver.com'

browser = webdriver.Chrome() # 크롬브라우저 열기
browser.get(url) # 네이버 페이지 이동
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW') # 로그인 버튼 선택
elem.click() # 클릭
time.sleep(random.randint(2,5))

### 자바스크립트 호출방법
input_js = 'document.getElementById("id").value="{id}";\
  document.getElementById("pw").value="{pw}";'.format(id="mylim52",pw="")
browser.execute_script(input_js)
time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,'btn_login')
elem.click()

time.sleep(100)

# # id값 입력
# elem = browser.find_element(By.ID,'id')
# elem.send_keys('mylim52')
# time.sleep(random.randint(2,5))
# # pw값 입력
# elem = browser.find_element(By.ID,'pw')
# elem.send_keys('')
# time.sleep(random.randint(2,5))

# elem = browser.find_element(By.CLASS_NAME,'btn_login')
# elem.click()