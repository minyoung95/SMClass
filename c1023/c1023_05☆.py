from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# selenium 정보 가져오기 - 1회
# for i in range(5): ### 페이지 5개
#   url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false&page={i+1}"
#   browser = webdriver.Chrome()
#   # 이동하려는 주소 입력
#   browser.get(url)
#   time.sleep(3) # 이미지를 가져오는 여유시간 두기
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   # 파일 저장하기
#   with open(f'c1023/yeogi{i+1}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일에서 불러오기 - BeautifulSoup 으로 파싱(변환)
for i in range(5):
  with open(f'c1023/yeogi{i+1}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  data = soup.select_one('#__next > div > main > section > div.css-1qumol3')
  sells = data.select('a')

  print("[ 강릉 숙소 ]")
  # 20개 출력 // 평점 9.0 이상, 평가수 500명 이상, 금액 : 120000 이하만 출력 (파일 5개를 모두 검색)
  for idx,sell in enumerate(sells):
    try:
      rating = float(sell.select_one('span.css-9ml4lz').text.strip())
      num = sell.select_one('.css-oj6onp').text.strip()[:-4]
      num = int(num.replace(',',''))
      price = sell.select_one('div.css-yeouz0>.css-5r5920').text.strip()
      price = int(price.replace(',',''))
      if rating < 9.0 or num < 500 or price > 120000:
        print(f"{(i*20)+idx+1}번 제외")
        print('-'*50)
        continue
      print(f"{(i*20)+idx+1}.")
      print('상품명 : ',sell.select_one('.css-8fn780>h3').text.strip())
      print('평점 : ',rating)
      print('평가수 : ',num)
      print('금액 : ',price)
      # img = sell.select_one('div.css-gvoll6')
      # print('금액 : ',img)
      link = sell['href']
      print('링크주소 : ','https://www.yeogi.com'+link)
      print('-'*50)
    
    except Exception as e:
      print((i*20)+idx+1, '예외처리',e)



# time.sleep(100)

### 제목,평점,평가수,금액,이미지,링크주소








### requests 정보 가져오기
# url = 'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, 'lxml')

# with open('c1023/yeogi.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

# data = soup.select_one('#__next > div > main > section > div.css-1qumol3') ## None
# print(data)