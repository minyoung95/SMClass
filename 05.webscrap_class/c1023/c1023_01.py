import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

data = soup.select_one('#contentarea > div.box_type_l > table')
stocks = data.select('tr')
print(len(stocks))

# ###리스트 생성 방법
# sts = stocks[0].select('th') # select 라서 text를 하나하나씩 바꿔줄수 없음 (for문)
# st_list = []
# for st in sts:
#   st_list.append(st.text)
# print(st_list)
f = open('c1023/stock.csv','w',encoding='utf-8-sig', newline='')
writer = csv.writer(f)
st_list = [st.text for st in stocks[0].select('th')] # 리스트 내포
print(len(st_list)) # 상단타이틀 길이(갯수) : 12개
writer.writerow(st_list)


sto_list = [sto.text.strip().replace('\t','').replace('\n','') for sto in stocks[2].select('td')] # 리스트 내포
sto_lists = []
for st in range(50):
  sto = [sto.text.strip().replace('\t','').replace('\n','') for sto in stocks[st].select('td')]
  if len(sto) != 12 : continue
  sto_lists.append(sto)
  writer.writerow(sto_lists)

f.close()
# with open('c1023/sto_list.csv','w',encoding='utf-8-sig') as f:
#   writer = csv.writer(f)
#   writer.writerow(sto_lists)
