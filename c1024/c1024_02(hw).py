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

##selenium 화면 숨김처리
options = Options()
options.add_argument('--headless') # 숨김처리
options.add_argument('--window-size=1920,1080') # 화면 사이즈(1920,1080 (최대))
# 차단 방지
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/130.0.0.0 Safari/537.36') 
# --------------------------------------------------------

for i in range(3):
  url = f'https://www.gmarket.co.kr/n/search?keyword=%eb%85%b8%ed%8a%b8%eb%b6%81&k=61&p={i+1}'
  browser = webdriver.Chrome(options=options)
  browser.get(url)
  time.sleep(3)
  
  soup = BeautifulSoup(browser.page_source,'lxml')

  with open(f'c1024/gmarket{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

  browser.get_screenshot_as_file(f'gmarket{i+1}.png') # 스크린샷
input('엔터키 입력완료 >>')

## 노트북으로 검색 된 사이트에서 1-3페이지에서 만족도 95% 이상, 금액 150만원 이하, 평가 수 100 이상


# for i in range(3):
#   with open(f'c1024/gmarket{i+1}.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f, 'lxml')

# data = soup.select_one('#section__inner-content-body-container')
# lists = data.select('div.box__item-container')
# print(len(lists))

# for idx,list in enumerate(lists):
#   try:
#     print("상품명 : ",list.select_one('span.text__item').text.strip())
#     print("만족도 : ",list.select_one('span.image__awards-points').select_one('span.for-a11y').text.strip())
#     print("평가수 : ",list.select_one('span.text').text.strip())
#     print("금액 : ",list.select_one('strong.text text__value').text.strip())
  
#   except Exception as e:
#     print("예외처리",e)