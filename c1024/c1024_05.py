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

# url = 'https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL'
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)
# time.sleep(1)

# pyautogui.moveTo(1270,540)
# time.sleep(1)
# pyautogui.moveTo(1270,480)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,780)
# time.sleep(1)
# prev_height = browser.execute_script('return articleListArea.scrollHeight')
# print('화면 높이 : ',prev_height) # 왼쪽 작은화면 스크롤
# while True:
#   # browser.execute_script('window.scroll(0,articleListArea.scrollHeight)')
#   pyautogui.scroll(-prev_height)
#   time.sleep(2)
#   curr_height = browser.execute_script('return articleListArea.scrollHeight')
#   if prev_height == curr_height : break
#   prev_height = curr_height
#   print('높이 : ',prev_height)
#   # all_height = browser.execute_script('return document.body.scrollHeight')
#   # print('전체 높이 : ',all_height) # 전체화면 스크롤

# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# with open("c1024/naver.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

with open('c1024/naver.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

data = soup.select_one('#articleListArea')
lists = data.select('div.item_inner')
print(len(lists))

## 숫자 변경
def num_chg(p):
  b = p.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(',',''))*10000
  else:
    s_num = 0
  price = f_num + s_num
  return price

## 평수 구하는 함수 (138/101m**2, 7/35층, 남향)
def spec_chg(spec):
  spec_a = spec.split(',') # , 나누기
  spec_b = spec_a[0].split('/') # / 나누기
  spec_c = int(spec_b[1][:-2])
  return spec_c

search_list1 = []
search_list2 = []
house_list = []
## 매매가격 낮은 5개, 전세가격 낮은 5개
for idx,list in enumerate(lists):
  print(f'[{idx+1}. ]')
  name = list.select_one('span.text').text.strip()
  print('아파트 명 : ',name)
  type = list.select_one('span.type').text.strip()
  if type == "월세": continue
  print('타입 : ',type)
  price = list.select_one('span.price').text.strip()
  price = num_chg(price)
  print('가격 : ',price)
  # 평수 나누기
  spec = list.select_one('span.spec').text.strip()
  spec = spec_chg(spec)
  print("평수 : ",spec)
  print('-'*50)
  house_list.append([[idx+1],type,price,spec])

# 리스트 저장


print('[ 리스트 출력 ]')
## 매매리스트
h1_list = [x for x in house_list if x[1]=='매매']
## 전세리스트
h2_list = [x for x in house_list if x[1]=='전세']


# 매매순차정렬
h1_list.sort(key=lambda x:x[2])
print(h1_list[:5]) # 낮은가격 5개

## 전세순차정렬
h2_list.sort(key=lambda x:x[2])
print(h2_list[:5]) # 낮은가격 5개

# ## 매매 평수순차정렬
# h1_list.sort(key=lambda x:x[3])
# print(h1_list[:20])
# print('-'*50)
# ## 전세 평수순차정렬
# h2_list.sort(key=lambda x:x[3])
# print(h2_list[:20])
