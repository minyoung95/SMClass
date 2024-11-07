from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

s_list = []
for syear in range(2020,2024):
  with open(f'd1107/screen{syear}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    print(f'{syear}년도 ------------------------')
    # 기준점
    data = soup.select_one('#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul')
    screens = data.select('li')
    # 웹스크래핑 시작
    for i,screen in enumerate(screens):
        print(f'{i+1}.')
        s_img = screen.select_one('.wrap_thumb img')['src']
        title = screen.select_one('.tit-g.clamp-g').text.strip()
        number = screen.select_one('.conts-desc.clamp-g').text.strip()[3:-2].replace(',','')
        sdate = screen.select_one('.conts-subdesc.clamp-g').text.strip()[:-1]
        s_list.append([title,number,sdate])
        # 파일저장을 하지 않고, s_list 모든 데이터를 담아서, 뒤에서 저장
        
topTitle = ['제목','관객수','날짜']
# f.write('제목,관객수,날짜\n') # 첫번째 1번만 글 저장 (for문 밖으로)
with open('screens.csv','w',encoding='utf-8') as f:
    f.write('제목,관객수,날짜\n')
    for s in s_list:
        f.write(','.join(s)+'\n')

f.close()        




















# a_list = ['서울의 봄',100,'2024-11-07']
# with open('d1107/s3.csv','w',encoding='utf-8') as f:
#     a_title = ['제목','관객수','날짜']
#     f.write(','.join(a_title)+'\n')
#     for i in range(10):
#         f.write(f'{a_list[0],{a_list[1]},{a_list[2]}}\n') 
#         # f.write(f','.join(a_title)+'\n') # 리스트가 문자형이 아닐경우 에러
# print('프로그램 완료')