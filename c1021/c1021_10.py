import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

hot = soup.find('div',{'class':'hot_issue'}).find('li',{'class':'issue_list04'})
print(len(hot))
list = hot.find_all('dl')

for idx,lists in enumerate(list):
  print("제목 : ",lists.find('span',{'class':'title'}).text)
  print("이미지 url : ", lists.find('img'))

  with open(f'c1021/n{idx}.jpg','wb') as f:
    re_img = requests.get(lists.find('img'))
    f.write(re_img.content)
