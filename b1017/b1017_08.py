import datetime
import os
members = []
mem_key = ['id','pw','name','nicName','address','money']
mem = []

#### members csv 파일 불러오기
f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])

  members.append(dict(zip(mem_key,m)))
f.close()

#### cart.txt 파일 불러오기
cartNo = 0
cart = []
cart_key = ['cNo','id','name','pCode','pName','price','date']

if os.path.exists("b1017/cart.txt"): # exists : 파일이 존재하는지 확인, isfile : 파일인지 아닌지 확인, isdir : 디렉토리인지 확인
  f = open('b1017/cart.txt','r',encoding='utf-8')
  while True:
    line = f.readline()
    if not line: break
    ca = line.strip().split(",")
    ca[0] = int(ca[0])
    ca[5] = int(ca[5])

    cart.append(dict(zip(cart_key,ca)))
  f.close()
  
session_info = {}
p_title = ["번호", "아이디", "이름", "코드", "상품명", "가격", "구매일자"]
product = [ 
  {"pNo":1,"pCode":"t001","pName":"삼성 TV","price":2000000,"color":"black"},
  {"pNo":2,"pCode":"g001","pName":"LG 냉장고","price":3000000,"color":"white"},
  {"pNo":3,"pCode":"h001","pName":"하마카돈 스피커","price":500000,"color":"gray"},
  {"pNo":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
  ]
pd_key = ['pNo', 'id', 'name', 'pCode', 'pName', 'price']

### 파일 저장 후 불러오기
f = open('b1017/product.txt','w',encoding='utf-8')
for p in product:
  f.write(f"{p["pNo"]},{p["pCode"]},{p["pName"]},{p["price"]},{p["color"]}\n")
f.close()

f = open('b1017/product.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  pd = line.strip().split(",")
  pd[0] = int(pd[0])
  pd[4] = int(pd[4])
  print(pd)
  product.append(dict(zip(pd_key,pd)))

#### 상품 구매함수
def buy(cartNo):
  print(f"{product[0]['pName']}을 구매하셨습니다.")
  print("구매 내역에 등록합니다.")
  ## 구매내역 등록
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {"cNo": cartNo+1, "id": session_info['id'], "name": session_info['name'], "pCode": product[choice-1]['pCode'], "pName": product[choice-1]['pName'], "price": product[choice-1]['price'], "date": today}
  session_info['money'] -= product[choice-1]['price']
  cart.append(c)
  cartNo += 1
  return cartNo
#-------------------------------------------

##### 프로그램 시작 #####
while True:
  print("[ 메인 화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.")

  if choice == "1":
    print("[ 로그인 ]")
    input_id = input("아이디를 입력하세요. >> ")
    input_pw = input("패스워드를 입력하세요. >> ")
    flag = 0
    for m in members:
      if m['id'] == input_id and m['pw'] == input_pw:
        session_info = m
        print(f"{session_info['nicName']} 님 로그인에 성공하셨습니다.")
        flag = 1
        break # for문
    
    if flag == 0:
      print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력해주세요.")
      print()
    else:
      break # while문

  elif choice == "2":
    print("[ 회원가입 ]")
    id = input("아이디를 입력하세요. >> ")
    flag = 0
    for m in members:
      if m['id'] == id:
        print("이미 존재하는 아이디입니다. 다시 입력해주세요.")
        flag = 1
        break #### 질문
    if flag == 1: continue
    else:
      print(f"{id}는 사용 가능합니다.")
    pw = input("패스워드를 입력하세요. >> ")
    name = input("이름을 입력해주세요.")
    nicName = input("닉네임을 입력해주세요.")
    address = input("주소를 입력해주세요.")
    money = int(input("충전금액을 입력해주세요."))
    m_list = [id, pw, name, nicName, address, money]
    members.append(dict(zip(mem_key,m_list)))

    print(f"{nicName} 님의 회원가입이 완료되었습니다.")
    # print(m_list) ## 출력 모양 수정하기
    # print("-"*30)
    # print(members) ## 출력 모양 수정하기

  elif choice == "0":
    print("프로그램을 종료합니다.")
    break


while True:
  print("           [SM-SHOP ]")
  print(f"                      닉네임:{session_info['nicName']} 님")
  print(f"                      금액  :{session_info['money']:,}  원")
  print()
  print("1. 삼성 TV - 2,000,000")
  print("2. LG 냉장고 - 3,000,000")
  print("3. 하만카돈 스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액충전")
  choice = int(input("구매하려는 상품번호를 입력하세요. >> "))

  if choice == 1:
    print("[ 삼성 TV - 2,000,000 ]")
    cartNo = buy(cartNo)
  if choice == 2:
    print("[ LG 냉장고 - 3,000,000 ]")
    cartNo = buy(cartNo)
  if choice == 3:
    print("[ 하만카돈 스피커 - 500,000 ]")
    cartNo = buy(cartNo)
  if choice == 4:
    print("[ 세탁기 - 1,000,000 ]")
    cartNo = buy(cartNo)
  if choice == 7:
    print("[ 내용 저장 ]")
    pass
  if choice == 7:
    print("[ 구매 내역 ]")
    pass
  if choice == 7:
    print("[ 금액 충전 ]")
    pass