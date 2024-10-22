import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

data = soup.select_one('#frm > div > table')
lists = data.select('tr')


### lists[0] : 상단 타이틀

tits = lists[0].select('th')
title = []
for tit in tits:
  title.append(tit.text.strip())
#   print(tit.text.strip())
# print(title)


### 1-100위 리스트 출력
for i in range(1,101):
  if not os.path.exists('c1022/melon'): # 폴더가 존재하는지 확인
    os.makedirs('c1022/melon') # 폴더 만들기
  with open(f'c1022/melon/{i}.jpg','wb') as f:
    lis = lists[i].select('td')
    print("순위 : ",lis[1].select_one('span').text)
    print("앨범사진 : ",lis[3].select_one('img')['src'])
    img = requests.get(lis[3].select_one('img')['src'])
    f.write(img.content)
    songs = lis[5].select('div.ellipsis')
    print("곡 정보 : ",songs[0].select_one('a').text,end = '')
    singers = songs[1].select('a')
    if len(singers) != 4:
      print("가수 명 : ",singers[0].text)
    else:
      print("가수 명 : ",singers[0].text+','+singers[1].text)  
