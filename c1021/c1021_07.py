import requests
from bs4 import BeautifulSoup


url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()

# soup : html 전체
soup = BeautifulSoup(res.text, 'lxml')

con = soup.find('div',{'class':'rankingnews_box_wrap _popularRanking'})
# 뉴스 12개
rankLists = con.find_all('div',{'class':'rankingnews_box'})
with open("c1021/1.txt",'w',encoding='utf-8') as f:
  print("갯수 : ",len(rankLists))
  f.write(f"갯수 : {len(rankLists)}\n")
  # 언론사 이름
  for idx,rankList in enumerate(rankLists):
    print(f"[ {idx+1}. 언론사 ]", rankList.find('strong',{'class':'rankingnews_name'}).text)
    f.write(f"[ {idx+1}. 언론사 ] {rankList.find('strong',{'class':'rankingnews_name'}).text}\n")
    news = soup.find('ul',{'class':'rankingnews_list'})
    newsLists = news.find_all('li')
    print("랭킹박스 안 뉴스 갯수 : ", len(newsLists))
    for i,newsList in enumerate(newsLists):
      print(f"{i+1} : ",newsList.find("a").text)
      f.write(f"{i+1} : {newsList.find("a").text}\n")

  ### 1줄씩 파일 저장
