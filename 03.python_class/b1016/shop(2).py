import datetime

### member 파일 읽어오기 , member 딕셔너리 저장
member = []
m_key = ['id','pw','name','nicName','address','money']

f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])

  member.append(dict(zip(m_key,m)))
f.close()
#--------------------------------

### cart 파일 읽어오기, cart 딕셔너리 저장
cart = []
c_key = ['cNo','id','name','pCode','pName','price','date']

f = open('cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])

  cart.append(dict(zip(c_key,c)))
f.close()

#--------------------------------
product = [
  {"pNo":1,"pCode":"t001","pName":"삼성 TV","price":2000000,"color":"black"},
  {"pNo":2,"pCode":"g001","pName":"LG 냉장고","price":3000000,"color":"white"},
  {"pNo":3,"pCode":"h001","pName":"하마카돈 스피커","price":500000,"color":"gray"},
  {"pNo":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

cartNo = 0
session_info = {} # 로그인정보
p_title = ['번호', '아이디', '이름', '코드', '상품명', '가격', '구매일자']
### 상품구매 함수
def buy(cartNo,choice): # 바깥에서 함수로 가져오고 싶은 변수
  print(f"{product[0]['pName']}를 구매하셨습니다.") # 0은 choice - 1로 바꿔주면 다른상품도 다 같이 사용가능
  print("구매내역에 등록합니다.")

  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  # c를 cart 리스트에 추가
  c = {"cNo":cartNo+1, "id":session_info['id'], "name":session_info['name'], "pCode":product[choice-1]['pCode'], "pName":product[choice-1]['pName'], "price":product[choice-1]['price'], "date":today}
  session_info['money'] -= product[choice-1]['price'] # 기존 금액에서 구매 금액 차감

  cart.append(c)
  cartNo += 1
  return cartNo
#-------------------------------------------

### 구매내역 함수
def buy_output():
  print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]}\t{p_title[5]}\t{p_title[6]}")
  print("-"*100)

  sum = 0 # 총 구매액 설정을 위해
  for c in cart:
    sum += c['price']
    print(f"{c['cNo']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']}\t{c['price']}\t{c['date']}")
  
  print()
  print(f"총 구매 금액 : {sum}")
  print(f"총 구매 건수 : {len(cart)}")
#-------------------------------------------


  
##### 프로그램 시작 #####  

while True:
  print("[ 로그인 화면 ]")
  input_id = input("아이디를 입력하세요.")
  input_pw = input("패스워드를 입력하세요.")
  flag = 0
  for m in member:
    session_info = m
    if m['id'] == input_id and m['pw'] == input_pw:
      print(f"{m['nicName']}님 환영합니다.")
      print()
      flag = 1
      break
  
  if flag == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else: break

while True:
  print("            [SM-SHOP]")
  print(f"                       닉네임:{m['nicName']} 님")
  print(f"                       금액  :{m['money']}   원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG 냉장고 - 3,000,000")
  print("3. 하만카돈 스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액충전")
  choice = int(input("원하시는 번호를 입력하세요. >> "))

  if choice == 1:
    print("[ 삼성 TV ]")
    cartNo = buy(cartNo,choice)
  elif choice == 2:
    print("[ LG 냉장고 ]")
    cartNo = buy(cartNo,choice)
  elif choice == 3:
    print("[ 하만카돈 스피커 ]")
    cartNo = buy(cartNo,choice)
  elif choice == 4:
    print("[ 세탁기 ]")
    cartNo = buy(cartNo,choice)
  elif choice == 7:
    print("[ 내용저장 ]")
  elif choice == 8:
    print("[ 구매내역 ]")
    buy_output()
  elif choice == 9:
    print("[ 금액충전 ]")
