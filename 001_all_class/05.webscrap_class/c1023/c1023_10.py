# flight.html 금액이 50000원 미만 항공권 출력

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

with open('c1023/flight.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

data = soup.select_one('#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB')
lists = data.select('div.domestic_Flight__8bR_b')

for idx,list in enumerate(lists):
  print(f"{idx+1}번")
  print("항공사 명 : ",list.select_one('div.domestic_heading__eXCgv').text.strip())
  print("출발시간 : ",list.select_one('span.route_airport__tBD9o').select_one('b').text.strip())
  print("도착시간 : ",list.select_one('span.route_airport__tBD9o').find_next_sibling('b'))