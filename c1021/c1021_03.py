## naver 파일 저장, 리솜리조트 파일 저장

import requests

### 하나의 파일 저장할 때
# url = "http://www.melon.com"
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# print(res.text)

# with open(f'c1021/coupang.html','w',encoding='utf-8') as f:
#   f.write(res.text)

### 여러개 파일 한번에 저장할 때 (list, for문 사용)

url = [
  "https://www.naver.com/",
  "https://www.resom.co.kr/",
  "http://www.daum.net/" #http 보안x // https 보안o
]


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
for i in range(len(url)):
  res = requests.get(url[i],headers=headers)
  res.raise_for_status()

  with open(f'c1021/{i}.html','w',encoding='utf-8') as f:
    f.write(res.text)
    

print("프로그램 종료")