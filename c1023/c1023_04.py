import time
import random

# # a = [0]*100
# # for i in range(100):
# #   a[i] = i
# # print(a)

# # b = [i for i in range(100)]
# # print(b)

# # for i in b:
# #   print(i)
# #   time.sleep(1)

# print(random.uniform(1,3)) # 1,3 사이의 무작위 숫자(실수)
# print(random.randint(1,3)) # 1,3 사이의 무작위 숫자(정수)

## 다음사이트에서 검색창 주식정보 입력해서 페이지 이동을 하세요.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.daum.net')

elem = browser.find_element(By.ID,'q')
elem.click()
elem.send_keys('주식정보')
elem.send_keys(Keys.ENTER)

time.sleep(100)
browser.get('http//www.naver.com')
elem = browser.find_element(By.CLASS_NAME,'search_input')
elem.send_keys('주식정보')
time.sleep(3)
elem.send_keys(Keys.ENTER)


time.sleep(100)