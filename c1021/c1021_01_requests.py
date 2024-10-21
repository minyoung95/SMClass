### 웹스크래핑 세팅


import requests
### requests 정보를 가져올 시 jqury, javascript, 외부페이지, react, vue.. (비동기식으로 작동되는)정보(소스)는 가져오지 못함


# res = requests.get("http://www.google.com/") # 정보(html소스) 가져오기
res = requests.get("http://www.naver.com/") # 정보(html소스) 가져오기
# res = requests.get("https://www.melon.com/index.htm") # 정보(html소스) 가져오기
res.raise_for_status() # 에러(raise) 시 자동종료 
print(res.text) # html 소스 출력

# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근 할 수 없습니다.")

# print("응답코드 : ",res.status_code) # 200 : 서버 요청을 성공적으로 처리

### 웹 소스코드 파일 저장
## f.close를 안해도 자동으로 닫히게 with as f
with open('c1021/naver.html','w',encoding='utf-8') as f:
  f.write(res.text)

# f = open('a.html','w',encoding='utf-8')
# f.write(res.text)
# f.close()

print("총 문자 길이 : ",len(res.text))
