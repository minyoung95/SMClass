from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
## email 발송 관련 
import smtplib
from email.mime.text import MIMEText
## 파일 첨부 관련
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

url = 'https://news.naver.com/main/ranking/popularDay.naver'

browser = webdriver.Chrome()
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
f = open('c1025/news.txt','w',encoding='utf-8')

data = soup.select_one('#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div')
lists = data.select('div.rankingnews_box')
print(len(lists))
lis = data.select_one('div.rankingnews_box').select('li')
print(len(lis))
## 랭킹뉴스 1~5 1.txt 이메일발송

title = lists[0].select_one('strong').text
print("언론사 명 :",title)
f.write(f'{title}\n')
for li in lis:
  name = li.select_one('div.list_content > a').text
  print('제목 명 : ',name)
  f.write(f'{name}\n')


f.close()

## smtp 이름 포트 입력
smtpName = 'smtp.naver.com'
smtpPort = 587

## 받는사람 이메일, 보내는사람 이메일, 비밀번호

sendEmail = 'mylim52@naver.com'
pw = 'dla1954613'
recvEmail = 'mylim52@naver.com'

## 제목, 내용 적기
title = '파이썬 수업'
content = '이메일 보내보기'

### 텍스트 보내기
# msg = MIMEText(content)
# msg['Subject'] = title # 제목
# msg['From'] = recvEmail # 받는사람
# msg['To'] = sendEmail # 보내는사람
# print('msg 데이터 :',msg.as_string())

# s = smtplib.SMTP(smtpName,smtpPort) # smtp 연결?
# s.starttls()
# s.login(sendEmail,pw) # 로그인 (아이디, 패스워드)
# s.sendmail(sendEmail,recvEmail,msg.as_string()) # 메일보내기 (보내는사람, 받는사람)
# s.quit() # 나가기?

msg = MIMEMultipart()
msg['Subject'] = title
msg['From'] = recvEmail
msg['To'] = sendEmail
msg.attach(MIMEText(content)) ## attach 로 텍스트 이메일 첨부해주기

with open('c1025/news.txt','rb') as f:
  attachment = MIMEApplication(f.read()) # MIMEApplication(이메일에 파일을 첨부하기 위한 클래스) f파일을 읽어 이메일 파일로 변환
  attachment.add_header('Content-Disposition','attachment',filename = 'mainNews.txt') # 첨부파일이 어떻게 처리되어야하는지 > 첨부파일로 전송되어야함 // 파일명을 mainNews.txt로 지정
  msg.attach(attachment) # attachment를 이메일에 첨부

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() # 보안인증
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print('msg: ')
print(msg.as_string())
s.quit()



print('메일 전송 완료')