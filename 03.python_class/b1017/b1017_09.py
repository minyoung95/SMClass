import os

members = []
mem_key = []

f = open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line:break
  print(line.strip())

# exists : 파일이 존재하는지 확인, isfile : 파일인지 아닌지 확인, isdir : 디렉토리인지 확인
if os.path.exists("b1017/cart.txt"):
  print("파일이 존재합니다.")
else:
  print("파일이 존재하지않습니다.")

while True:
  print("1.회원등록")
  print("2.회원검색")
  choice = input("번호 입력")

  if choice == "1":
    id = input("아이디를 입력하세요.")
    flag = 0
    for m in members:
      if m['id'] == id:
        print(f"{id} : 동일한 아이디가 존재합니다. 다시 입력해주세요.")
        flag = 1
        break
    if flag == 1: continue # for문으로 돌아가기
    else:
      print(f"{id} : 사용 가능합니다.")
    pw = input("패스워드를 입력하세요.")
    name = input("이름을 입력하세요.")
    nicName = input("닉네임을 입력하세요.")
    address = input("주소를 입력하세요.")
    money = int(input("충전금액을 입력하세요."))
    m_list = [id, pw, name, nicName, address, money]
    members.append(dict(zip(mem_key,m_list)))

    print(f"{id} 님의 회원가입이 완료되었습니다.")
    print(m_list)
    print("-"*50)
    print(members)

  else:
    ### 아이디 검색
    # members 리스트에서 입력한 문자로 검색된 데이터를 모두 출력 (a가 들어가있는 아이디를 출력)
    search = input("검색할 아이디를 입력하세요.")
    check = 0
    mArr = []
    for m in members:
      if m['id'].find(search) != -1:
        mArr.append(m)
        check = 1

    if check == 0:
      print("검색된 회원이 없습니다.")
    else:
      print(mArr)
      print("총 검색 수 : ",len(mArr))