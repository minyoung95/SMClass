import os
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# ## 링크주소, 이미지주소, 제목, 금액, 평점, 평가수
# data = soup.select_one('#productList')
# lists = data.select_one('li')
# print("1. 링크 주소 : ","https://www.coupang.com"+lists.select_one('a')['href'])
# print("2. 이미지 주소 :","https:/"+lists.select_one('dt.image>img')['src'][1:])
# print("3. 제목: ",lists.select_one('div.name').text)
# price = int(lists.select_one('strong.price-value').text.replace(',',''))
# print("4. 금액 : ",price)
# rating = float(lists.select_one('span.star').text)
# print("5. 평점 : ",rating)
# num = int(lists.select_one('span.rating-total-count').text[1:-1]) # slice로 () 자름
# print("6. 평가 수 : ",num)

# ### slice
# a = "(안녕하세요)"
# print(a[1:])
# print(a[1:-1])
# print(a[:3])

# list = [1,2,3,4,5,6,7,8]
# print(list[1:-1])

### 금액 : 90만원 이상, 평점 4,5 이상, 평가수 100명 이상 ###
data = soup.select_one('#productList')
lists = data.select('li')
n_lists = []
for idx,list in enumerate(lists):
  n_list = [] # 제목, 금액, 평점, 평가수, 링크, 이미지
  n = ''
  try:
    price = int(list.select_one('strong.price-value').text.replace(',',''))
    rating = float(list.select_one('em.rating').text)
    num = int(list.select_one('span.rating-total-count').text[1:-1]) # slice로 () 자름
    if price >= 900000 and rating >= 4.5 and num >= 100:
      # n = "https://www.coupang.com"+list.select_one('a')['href']
      # n += "https:/"+list.select_one('dt.image>img')['src']
      # n += list.select_one('div.name').text
      # n += price
      # n += rating
      # n += num
      print(f"{[idx+1]}")
      print("1. 링크 주소 : ","https://www.coupang.com"+list.select_one('a')['href'])
      print("2. 이미지 주소 :","https:/"+list.select_one('dt.image>img')['src'][1:])
      print("3. 제목: ",list.select_one('div.name').text)
      print("4. 금액 : ",price)
      print("5. 평점 : ",rating)
      print("6. 평가 수 : ",num)
      print("-"*50)
    else:
      print(f"[ {idx} 번째 ] : 제외")     
  except Exception as e:
    print(f"{idx+1}:에러", e)
    pass


### 정렬
# while True:
#   print("1. 금액정렬")
#   print("2. 금액역순정렬")
#   print("3. 평점정렬")
#   print("4. 평점역순정렬")
#   print("0. 금액정렬")
#   print("-"*50)
#   choice = input("원하는 번호를 입력하세요.")

#   if choice == "1":
#     print("[ 금액정렬 ]")
#     pass
#   elif choice == "2":
#     print("[ 금액역순정렬 ]")
#     pass
#   elif choice == "3":
#     print("[ 평점정렬 ]")
#     pass
#   elif choice == "4":
#     print("[ 평점역순정렬 ]")
#     pass
