import datetime

member = []
member_key = ["id",'pw',"name","nicName","address","money"]
# member.txt파일 읽기
f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])

  member.append(dict(zip(member_key, m)))

####################################### m 에 값 채워보기
cartNo = 0
cart = []

cart_key = ['cNo','id','name','pCode','pName','price','date']
f = open('cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  ca = line.strip().split(",")
  ca[0] = int(ca[0])
  ca[5] = int(ca[5])

  member.append(dict(zip(cart_key,ca)))
f.close()

product = [
  {"pNo":1,"pCode":"t001","pName":"삼성 TV","price":2000000,"color":"black"},
  {"pNo":2,"pCode":"g001","pName":"LG 냉장고","price":3000000,"color":"white"},
  {"pNo":3,"pCode":"h001","pName":"하마카돈 스피커","price":500000,"color":"gray"},
  {"pNo":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]
session_info = {}
p_title = ["번호", "아이디", "이름", "코드", "상품명", "가격", "구매일자"]


### 상품구매 함수
def buy(choice,cartNo):
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  # 로그인 정보(session_info)
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {"cNo":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  session_info['money'] -= product[choice-1]['price']
  cart.append(c)
  cartNo += 1
  return cartNo
#-------------------------------------------

### 내용저장 함수
def buy_save():
  f = open('member.txt','w',encoding='utf-8')
  for m in member:
    f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n")
  f.close()
  
  f = open('cart.txt','a', encoding='utf-8')
  for c in cart:
    f.write(f"{c['cNo']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
  f.close()
  
  print("내용이 저장되었습니다.")
#-------------------------------------------

### 구매내역 함수
def buy_output():
  print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:15s}\t\t{p_title[5]}\t{p_title[6]}")
  print("-"*100)
  
  sum = 0
  for c in cart:
    sum += c['price']
    print(f"{c['cNo']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:15s}\t\t{c['price']}\t{c['date']}")
  
  print()
  print(f"총 구매 금액 : {sum}")
  print(f"총 구매 건수 : {len(cart)}")
#-------------------------------------------

### 금액충전 함수
def money_input():
  print(f"현재 남은 금액 : {session_info['money']}")
  money_plus = int(input("충전 금액 : "))
  session_info['money'] += money_plus

  print(f"충전된 금액 : {session_info['money']}")
  print()
#-------------------------------------------

##### 프로그램 시작 #####
while True:
  print("[ 로그인 화면 ]")
  input_id = input("아이디를 입력하세요. >> ")
  input_pw = input("패스워드를 입력하세요. >> ")
  flag = 0
  for m in member:
    if m['id'] == input_id and m['pw'] == input_pw:
      session_info = m
      print(f"{session_info['nicName']} 님 SM SHOP에 오신것을 환영합니다.")
      print()
      flag = 1
      break # for문

  if flag == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else:
    break # while 문

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
    cartNo = buy(choice,cartNo) # 함수호출 (상품구매)
  elif choice == 2:
    cartNo = buy(choice,cartNo) # 함수호출 (상품구매)
  elif choice == 3:
    cartNo = buy(choice,cartNo) # 함수호출 (상품구매)
  elif choice == 4:
    cartNo = buy(choice,cartNo) # 함수호출 (상품구매)
  elif choice == 7:
    buy_save()                  # 함수호출 (내용저장)
  elif choice == 8:
    print("[ 8. 구매 내역 ]")
    buy_output()
  
  elif choice == 9:
    print("[ 9. 금액 충전 ]")
    money_input()