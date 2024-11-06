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


# ### html 파일 저장
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(5):
#   url = f'https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i+1}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list'
#   time.sleep(3)
#   browser.get(url)
#   time.sleep(5)

#   while True:
#     prev_height = browser.execute_script('return document.body.scrollHeight')
#     print("최초 높이 : ",prev_height)
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     curr_height = browser.execute_script('return document.body.scrollHeight')
#     if prev_height == curr_height:
#       break
#     prev_height = curr_height
#     print("현재 높이 : ",curr_height)

#   soup = BeautifulSoup(browser.page_source, 'lxml')

#   with open(f'c1025/naver{i+1}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
### 파일 불러오기
for i in range(5):
  with open(f'c1025/naver{i+1}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  data = soup.select_one('div.basicList_list_basis__uNBZx > div')
  lists  = data.select('div.adProduct_item__1zC9h') + data.select('div.product_item__MDtDF')
  print(len(lists))

  def chg(val):
    r_val = 0
    if '만' in val:
      r_val = float(val[:-1])*10000
    else:
      r_val = float(val.replace(',',''))
    return r_val


  # for pro in lists:
  #   if pro['class'][0] == 'adProduct_item__1zC9h':
  #     print('adProduct_item__1zC9h')
  #   else:
  #     print('product_item__MDtDF')

### 제목, 가격, 평점, 평가수, 찜 정보를 1페이지에서 5페이지 까지 출력
### 평점4.8 이상, 평가수 1000명 이상, csv 파일로 저장
  a_list = []
  for idx,list in enumerate(lists):
    try:
      rating = float(list.select_one('div.product_etc_box__ElfVA').select_one('span.blind').next.next.strip())
      num = list.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div.product_item__MDtDF > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a > em').text.strip().replace(',','')[1:-1]
      num = chg(num)
      if rating >= 4.8 and num >= 1000:
        print(f'[{idx+1}]')
        name = list.select_one('div.product_title__Mmw2K').text.strip()
        print('상품 명 : ',name)
        price = list.select_one('span.price_num__S2p_v').text.strip().replace(',','').replace('\n','')[:-1]
        price = int(price)
        print('가격 : ',price)
        print('평점 : ',rating)
        print('평가 수 : ',num)
        num2 = list.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div.product_item__MDtDF > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > span.product_etc__LGVaW > span').text.strip().replace(',','')
        print('찜 정보 :',num2)
        a_list.append([name, price, rating, num, num2])
    except Exception as e:
      print('예외처리',e)
 





