import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

box = soup.select_one('div.box_type_l').select_one('table.type_5')
table = box.select_one('tr.type1')
ths = table.select('th')
for th in ths:
  print(th.text,end='\t')

trs = box.select_one('tbody')
