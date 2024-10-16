students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0 # 성적처리에 필요한 변수
check = 0 # 체크할때 변수
count = 1 # 등수처리
choice = 0
stuNo = len(students) # 리스트에 이미 학생이 차 있을 시 그 이후 번호로 지정해줌

students_key = ['no','name','kor','eng','math','total','avg','rank']
f = open('students.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  s = line.strip().split(",")
  s[0] = int(s[0])
  s[2] = int(s[2])
  s[3] = int(s[3])
  s[4] = int(s[4])
  s[5] = int(s[5])
  s[6] = float(s[6])
  s[7] = int(s[7])

  students.append(dict(zip(students_key,s)))
print(students)

# 메뉴 출력함수
def title_program():
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ") # 일반변수 - return 필요
  return choice
# --------------------------------------

# 학생성적 입력함수
def stu_input(stuNo): # stuNo가 일반변수이므로 매개변수 적용
  while True:
    print("[ 1. 학생성적 입력 ]")
    print()

    no = stuNo + 1 # 리스트 - 학생 수
    name = input(f"{no}번째 학생이름을 입력하세요.(0. 이전화면)")
    if name == "0":
      print("성적 입력을 취소합니다.")
      print()
      break # while True 쪽으로 되돌아감
    kor = int(input("국어점수를 입력하세요."))
    eng = int(input("영어점수를 입력하세요."))
    math = int(input("수학점수를 입력하세요."))
    total = kor+eng+math
    avg = total/3
    rank = 0

    ss = {"no" : no, "name" : name, "kor" : kor, "eng" : eng, "math" : math, "total" : total, "avg" : avg, "rank" : rank}
    students.append(ss)
    stuNo += 1 # 다음 학생 번호를 1 증가

    # 파일쓰기
    f = open('students.txt','w',encoding='utf-8')
    data = f"{ss['no']},{ss['name']},{ss['kor']},{ss['eng']},{ss['math']},{ss['total']},{ss['avg']},{ss['rank']}"
    f.write(data)
    f.close()

    print(f"{name} 학생의 성적이 저장되었습니다.")
    print()
  return stuNo # 일반매개변수이므로 return으로 반환해주어야 함


# --------------------------------------

# 학생성적 출력함수
def stu_output():
  print("[ 2. 학생성적 출력 ]")
  print()

  for t in s_title:
    print(f"{t}\t", end="")
  print(); print("-"*60)

  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
  print()
# --------------------------------------

# 학생성적 수정함수
def stu_update():
  print("[ 3. 학생성적 수정 ]")
  print()

  name = input("수정하고자 하는 학생 이름을 입력해주세요.")

  # 전체학생과 입력한 이름을 비교
  for s in students:
    if name == s['name']:
      print(f"{name} 학생을 찾았습니다.")
      print()
      
      print("[ 수정과목 선택 ]")
      print("1. 국어과목 수정")
      print("2. 영어과목 수정")
      print("3. 수학과목 수정")
      print("0. 이전 메뉴")
      choice = input("원하는 번호를 입력하세요.")

      if choice == "1":
        print("이전 국어점수 : {}".format(s['kor']))
        s['kor'] = int(input("변경 국어점수 : "))
      elif choice == "2":
        print("이전 영어점수 : {}".format(s['eng']))
        s['eng'] = int(input("변경 영어점수 : "))
      elif choice == "3":
        print("이전 수학점수 : {}".format(s['math']))
        s['math'] = int(input("변경 수학점수 : "))

      s['total'] = s['kor']+s['eng']+s['math']
      s['avg'] = s['total']/3

      print(f"{name} 학생 성적이 수정되었습니다.")

      # 수정된 학생 정보 출력
      stu_output([s]) # s 한명의 데이터만 함수로 보냄 
      # s는 딕셔너리 타입이므로 리스트로 바꿔줌, 함수의 매개변수 students가 리스트 타입이므로 타입을 맞춰줌
      check = 1
    
  # 학생이 검색되지 않았을 때
  if check == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
    print()
# --------------------------------------

# 학생성적 검색함수
def stu_select():
  print("[ 4. 학생성적 검색 ]")
  print()

  while True:
    check = 0
    name = input("검색하려는 이름을 입력하세요. (0. 이전화면)")
    if name == "0":
      break
    sArr = []
    for idx,s in enumerate(students):
      if s['name'].find(name) != -1:
        # print(f"{idx}번째,{name} 학생을 찾았습니다.", s['name'])
        sArr.append(s)
        check = 1

    
    if check == 0:
      print("찾는 학생이 없습니다.")
    else:
      print(f"{name} 이름으로 {len(sArr)}명 검색되었습니다.")
      stu_output(sArr)
# --------------------------------------

# 학생성적 삭제함수
def stu_delete():
  print("[ 5. 학생성적 삭제 ]")
  print()

  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  check = 0
  dArr = []
  for idx,s in enumerate(students):
    if s['name'] == name:
      check = 1
      print(f"{name} 학생 성적을 삭제하시겠습니까? (삭제 시 복구불가)")
      choice = input("1. 삭제 2. 취소 >>")
      if choice == "1":
        dArr.append(s)
        del students[idx]
        print(f"{name} 학생의 성적이 삭제되었습니다.")
      else:
        print("학생성적 삭제가 취소되었습니다.")
      break

  if check == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
    print()
  else:
    stu_output([s])
# --------------------------------------

# 등수처리 함수
def stu_rank():
  print("[ 6. 등수처리 ]")
  print()

  for s in students:
    count = 1 # 1등인 데이터
    for st in students:
      if s['total'] < st['total']: # 다른 데이터와 비교(작을 경우)
        count += 1 # 2등으로 밀려남
      s['rank'] = count # 등수 입력

  print("등수처리가 완료되었습니다.")
  print()
  stu_output(students)
# --------------------------------------

# 학생성적 정렬함수
def stu_sort():
  while True:
    print("[ 7.학생성적 정렬 ]")
    print("1. 이름 순차정렬")
    print("2. 이름 역순정렬")
    print("3. 합계 순차정렬")
    print("4. 합계 역순정렬")
    print("5. 번호 순차정렬")
    print("0. 이전메뉴")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.")

    if choice == "1":
      print("[ 이름 순차정렬 ]")
      students.sort(key=lambda x:x['name'])
    elif choice == "2":
      print("[ 이름 역순정렬 ]")
      students.sort(key=lambda x:x['name'],reverse=True)
    elif choice == "3":
      print("[ 합계 순차정렬 ]")
      students.sort(key=lambda x:x['total'])
    elif choice == "4":
      print("[ 합계 역순정렬 ]")
      students.sort(key=lambda x:x['total'],reverse=True)
    elif choice == "5":
      print("[ 번호 역순정렬 ]")
      students.sort(key=lambda x:x['no'])
    elif choice == "0":
      print("이전페이지로 이동합니다.")
      break

    print("정렬이 완료되었습니다.")
# --------------------------------------
