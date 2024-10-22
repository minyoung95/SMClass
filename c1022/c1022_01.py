import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

### 태그를 활용한 검색
# find, find_all, select_one, select

# print(soup.find('h2',{'class':'rankingnews_tit'}).text)
# print(soup.select_one('h2.rankingnews_tit').text)
# print(soup.select_one('div#header'))

print()
rank_box = soup.select_one('div.rankingnews_box_wrap').select('div.rankingnews_box')
for id,rl in enumerate(rank_box):
  tit = rl.select_one('strong.rankingnews_name').text
  print(f"[{id+1} 언론사 ]: ",tit)
  list = rl.select_one('ul.rankingnews_list')
  lists = list.select('li')
  # lists = rank_box.select('ul.rankingnews_list>li') > : 자식요소
  for idx,li in enumerate(lists):
    print(f"{idx+1} : ",li.select_one('div.list_content').text)


# print(lists.find('div',{'class':'list_content'}).text)