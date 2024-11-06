import requests # 정보를 가져옴
from bs4 import BeautifulSoup # html 소스코드를 명령어가 들어갈 수 있게 바꿔줌

### 파일 가져오기 구문
url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)
#------------------------------

### 파일 저장
# with open('c1021/1.html','w',encoding='utf-8') as f:
#   f.write(res.text)

soup = BeautifulSoup(res.text,'lxml') # html 태그, css 정보를 가진 소스로 변경

### 정보 찾기
# print(res.text.find()) # str이기 때문에 find() 나 index()로 찾기
print(soup.title) # title의 태그와 내용을 가져옴 : <title> xxx </title>
print(soup.title.get_text()) # 태그 안의 내용만 가져옴 : xxx (1) 없는 태그 입력 시 에러 // raise_for_status() 입력하여 프로그램이 계속 진행될 수 있게
print(soup.title.text) # 태그 안의 내용만 가져옴 : xxx (2)

print("없는 태그 : ",soup.titletitletitle) # 없는 태그 입력 시 None
# print("없는 태그 : ",soup.titletitletitle.get_text()) # 없는 태그 입력 시 에러
print(soup.a) # 제일 첫 번째 a
print(soup.a.next) # 앞 태그의 다음 태그와 내용 
print(soup.a.next.text) # 앞 태그의 다음 태그 안의 내용 
print(soup.a.attrs) # 태그의 속성 값을 가져옴 : 딕셔너리 형태
print(soup.a['href']) # href의 속성값(value값?)

### 특정정보 출력
# print(soup.find('div',attrs={'id':'header'})) # div에 id가 header인 것 찾기
# print(soup.find('div',{'id':'header'})) # div에 id가 header인 것 찾기
print(soup.find('h2',{'class':'rankingnews_tit'})) # h2태그에 class 네임이 rankingnews_tit인 것 찾기
print(soup.find('h2',{'class':'rankingnews_tit'}).text) # h2의 내용
print(soup.find_all('div')) # 모든 div 태그 출력
print(len(soup.find_all('div'))) # 모든 div 태그 갯수 출력
print(type(soup.find_all('div'))) # ResultSet : 객체의 리스트


# with open('c1021/2.html','w',encoding='utf8') as f:
#   f.write(soup.prettify()) # soup.prettify() : 소스가 정리되어 저장된다.


print("완료")
