import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

url = 'https://flight.naver.com/'

browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[1]/div/input').send_keys('김포')
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b/span[1]').click()
time.sleep(random.randint(1,3))

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[1]/div/input').send_keys('제주')
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b/span[1]').click()
time.sleep(random.randint(1,3))

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()
time.sleep(random.randint(1,3))

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(random.randint(1,3))

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
time.sleep(random.randint(1,3))
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

time.sleep(8)

while True:
  prev_height = browser.execute_script('return document.body.scrollHeight')
  print("최초 높이 : ",prev_height)
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  time.sleep(2)
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print("현재 높이 : ",curr_height)

soup = BeautifulSoup(browser.page_source, 'lxml')
with open('c1023/flight.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

browser.quit()











