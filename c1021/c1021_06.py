import requests
from bs4 import BeautifulSoup


url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

print()
newsTitle = soup.find('div',{'class':'rankingnews_box_wrap'}).find_all('div',{'rankingnews_box'})
print("갯수 : ",len(newsTitle))
print("타이틀 : ",newsTitle)
newsList = soup.find('ul',{'class':'rankingnews_list'})
rank = newsList.find_all("li")
## 5번 반복
for i,t in enumerate(rank):
  print(i+1, ":", t.find("a").text)