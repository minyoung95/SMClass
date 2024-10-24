import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.yanolja.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(3)

# 검색창 열기
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()
time.sleep(random.randint(1,3))

# 날짜검색
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()
time.sleep(random.randint(1,3))

# 강릉호텔 검색
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
elem.click()
time.sleep(random.randint(1,3))
elem.send_keys('강릉호텔')
time.sleep(random.randint(1,3))
elem.send_keys(Keys.ENTER)


# time.sleep(8)
# 로딩 대기 (최대 30초까지 대기).until (화면의 검색내용이 뜰때까지 대기)
WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))


while True:
  prev_height = browser.execute_script('return document.body.scrollHeight') # execute_script : 자바스크립트 실행함수
  print('최초 높이 : ',prev_height)
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  time.sleep(2)
  curr_height = browser.execute_script('return document.body.scrollHeight') # 페이지 로딩 후 길어진 스크롤 높이를 다시 가져옴
  
  if prev_height == curr_height:
    break
  prev_height = curr_height # 길어진 스크롤의 현재 높이를 이전 높이에 입력시킴 
  print('현재 높이 : ',curr_height)

print('스크롤 내리기 완료')

time.sleep(100000)

soup = BeautifulSoup(browser.page_source,'lxml')

# 파일(html)저장
with open('c1024/yanolja.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

# 파일 불러와서 soup으로 파싱(변환)
# with open('c1024/yanolja.html','r',encoding='utf-8') as f:
#   soup = BeautifulSoup(f, 'lxml')

## 평점 4.8이상 금액 170000 이하 검색하여 출력

data = soup.select_one('div.PlaceListBody_listContainer__2qFG1')
lists = data.select('div.PlaceListItemText_container__fUIgA text-unit PlaceListBody_textItem__1yTQ6')
print(len(lists))