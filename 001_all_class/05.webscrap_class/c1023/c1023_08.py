import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

url = 'https://flight.naver.com/'

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)
time.sleep(random.randint(1,3))

## 출발지 선택
# XPATH : 무조건 하나, 유일한 위치점
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb').send_keys('김포')
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a').click()
time.sleep(random.randint(1,3))

## 도착지 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb').send_keys('제주')
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b').click()
time.sleep(random.randint(1,3))

## 가는날 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button/b').click()
time.sleep(random.randint(1,3))
## 오는날 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button/b').click()
time.sleep(random.randint(1,3))

## 인원 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(random.randint(1,3))

## 항공권 검색
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]/span').click()
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]/span').click()

# 데이터 나타날때까지 대기 (7초)
time.sleep(7)

### 화면 대기함수
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC 

# # 화면에 찾으려고 하는 <html>요소가 있는지 확인
# elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]')) # 최대 120초까지 대기, 찾으려는 데이터가 나오면 

## 화면 스크롤 내리기
while True:
  prev_height = browser.execute_script('return document.body.scrollHeight') # 자바스크립트 호출 > 현재 높이를 알려줌
  print("최초 높이 :", prev_height)
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 스크롤 내리기(0~현재높이까지)
  time.sleep(2) # 스크롤을 내린 후 새로운데이터가 추가될때까지 대기
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height: # 이전 데이터 갯수와 내린 후 데이터 갯수가 같아졌을 때
    break
  prev_height = curr_height
  print('현재 높이 :',curr_height)

## 데이터 처리 // 웹스크래핑
soup = BeautifulSoup(browser.page_source, 'lxml')
with open('c1023/flight.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())
print("Enter키를 입력하면 종료됩니다.")
browser.quit()

time.sleep(1000)