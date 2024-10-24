import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup

# 파일 불러와서 soup으로 파싱(변환)
with open('c1024/yanolja.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

# 평점 4.8이상 금액 170000 이하 검색하여 출력

data = soup.select_one('div.PlaceListBody_listContainer__2qFG1')
lists = data.select('a.common_clearfix__M6urU')
print(len(lists))
list1 = []
list2 = []
list3 = []

for idx,list in enumerate(lists):
  try:
    rating = float(list.select_one('span.PlaceListScore_rating__3Glxf').text.strip())
    price = list.select_one('span.PlacePriceInfoV2_discountPrice__1PuwK').text.strip()
    price = int(price.replace(',',''))
    name = list.select_one('strong.PlaceListTitle_text__2511B').text.strip()
    if rating < 4.8 or price > 170000: 
      print(f"{idx + 1}번 제외")
      print('-'*50)
      list1.append(list)
      continue
    print(f"[ {idx+1}. ]")
    print("호텔 명 : ",name)
    print("평점 : ",rating)
    print("금액 : ",price)
    print('-'*50)
    list2.append([idx+1,name,rating,price])

  
  except Exception as e:
    print(idx+1, '예외처리',e)
    list3.append(list)

print('[ 검색 정보 ]')
print('1. 조건 맞지 않은 개수 :',len(list1))
print('2. 조건에 맞는 개수 :',len(list2))
print('3. 예외처리된 갯수 :',len(list3))

print(list2)
