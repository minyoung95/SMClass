import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

data = soup.select_one('#contentarea > div.box_type_l > table')
# data = soup.select_one('tbody') # 크롬 자체적으로 만든거라 소스코드에는 없음
stocks = data.select('tr') # 리스트 타입으로 정렬되어있음
# print("개수 : ",len(stocks))

### 타이틀, 주식정보 파일 저장하기
f = open('c1022/stock.txt','w',encoding='utf-8')

## 상단타이틀 출력
tits = stocks[0].select('th')
title = []
for tit in tits:
  title.append(tit.text)
  print(tit.text,end='\t')
print()
print("-"*100)
f.write(','.join(title)+'\n') ## 타이틀 저장


## 하단(주식정보) 출력 / 리스트 추가
st_lists = []
for i in range(2,50):
  st_list = []
  sts = stocks[i].select('td')
  if len(sts) <= 1: continue # tr 안 td가 1개 이하 일 때 제외
  for idx,st in enumerate(sts):
    s = ""
    if idx == 4:
      s = st.select_one('span').text
      s += st.select_one('span').next.next.next.text.strip()
      print(st.select_one('span').text,end='')
      print(st.select_one('span').next.next.next.text.strip(),end='\t')
    else:
      s = st.text.strip()
      print(st.text.strip(),end='\t')
    st_list.append(s)
  f.write(','.join(st_list)+'\n') ## 주식정보 저장
  st_lists.append(st_list)
  print()
  print('-'*30)

print(title)
print(st_lists)

f.close()

### join : 합치기
# title = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']

# a = ','.join(title)+'\n'
# print(a)

# with open('c1022/a.txt','w',encoding='utf-8') as f:
#   f.write(a)