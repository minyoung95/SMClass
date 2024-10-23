import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
sum = 0
popular = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular')

print(popular.select_one('span').text)

tables = popular.select('tbody > tr')
for idx,table in enumerate(tables):
  print(f"이름 : {idx+1}.",table.select_one('a').text)
  print("금액 : ",table.select_one('td').text)
  # sps = table.select_one('td').find_next_sibling('td').select('span')
  # print(len(sps))
  # for sp in sps:
  #   print(sp.text.strip())
  print("등락 : ",table.select_one('td').next_sibling.next_sibling.select_one('span').text)
  print("등락폭 : ",table.select_one('td').find_next_sibling('td').select_one('span').next.next.text)
  sum += int(table.select_one('td').text.replace(',','')) # replace("삭제할거","바꿀거")
  print("합계 : ",sum )
  # next_sibling 형제요소 // find_next_sibling('td') 형제요소 중 검색
