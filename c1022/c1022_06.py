import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# print(soup.prettify())

## 순위, 사진(링크주소), 제목, 가수명 

data = soup.select_one('#frm > div > table')
trs = data.select('tr')

f = open('c1022/melon.txt','w',encoding='utf-8')

tits = trs[0].select('th')
title = []
for tit in tits:
  title.append(tit.text.strip())
  print(tit.text,end='\t')
print()
print('-'*100)
print(title)
f.write(','.join(title)+'\n')

rank_list = []
for i in range(1,101):
  s = ''
  rank = trs[i].select('td')
  s = rank[1].select_one('span').text
  s += rank[5].select_one('span>a').text
  s += rank[5].select_one('div>a').text
  print(rank[1].select_one('span').text)
  print(rank[3].select_one('img'))
  print(rank[5].select_one('span>a').text)
  print(rank[5].select_one('div>a').text)
  rank_list.append(s)
print(rank_list)
f.write(','.join(rank_list)+'\n')