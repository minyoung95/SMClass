import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

print()
rankingnews_warp = soup.find('div',{'class':'rankingnews_box_wrap'}) # find : 1개 검색
rankingnews_boxs = rankingnews_warp.find_all('div',{'rankingnews_box'}) # find_all : 여러개 검색
print(len(rankingnews_boxs))
print(soup.find('strong',{'class':'rankingnews_name'}).text)

print(soup.title) # 제일 먼저 찾아지는 것을 출력
print(soup.find('title')) # 특정 위치의 태그와 속성을 출력
newLists = soup.find('div',{'class':'rankingnews_box_wrap'}).find('div',{'class':'rankingnews_box'}) # 앞 정보에서 한번 더 찾기
print(1,"-"*20)
### next : 검색태그 다음뒤에 오는 태그를 찾아줌
print(newLists)
print(1,"-"*20)
### next_sibling: 검색태그 다음뒤에 오는 형제태그를 찾아줌 (<>previous_sibling)
print(newLists.next_sibling.next_sibling) 

# print("여러개 갯수 확인 : ",len(newLists))

# for newList in newLists:
#   print(newList.find('strong',{'class':'rankingnews_name'}).text)