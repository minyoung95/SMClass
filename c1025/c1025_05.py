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

smtpName = 'smtp.naver.com'
smtpPort = 587

### id, pw, 받는사람 이메일주소
sendEmail = 'mylim52@naver.com'
pw = ''
recvEmail = 'mylim52@naver.com'

title = '제목 : 파이썬 이메일보내기'
content = """\
파이썬에서 이메일을 보냅니다.
여러줄 쓰기 형태 
네이버 smtp 서버를 사용해서 보냅니다."""

## 설정
msg = MIMEText(content)
msg['Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail
print('msg 데이터 : ',msg.as_string())

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail, pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()

print('메일을 발송했습니다.')