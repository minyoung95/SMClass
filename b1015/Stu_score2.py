students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
choice = 0
stuNo = 0 # 학생번호
stuNo = len(students) # 리스트에 이미 학생이 차 있을 시 그 이후 번호로 지정해줌
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0 # 성적처리에 필요한 변수
check = 0 # 체크할때 변수
count = 1 # 등수처리

### 학생성적 입력함수
def stu_input(stuNo):
  while True:
    no = stuNo + 1
    name = input("학생 이름을 입력하세요. (0. 이전화면)")
    if name == "0":
      print("이전화면으로 돌아갑니다.")
      break

    score = []
    total = 0
    for i in range(3):
      s = int(input(f"{s_title[i+2]}점수를 입력하세요."))
      total += s
      score.append(s)
    
    avg = total/3
    rank = 0

    ss = {"no" : no, "name" : name, "kor" : score[0], "eng" : score[1], "math" : score[2], "total" : total, "avg" : f"{avg:.2f}", "rank" : rank}

    students.append(ss)
    stuNo += 1
    
    print(f"{name} 학생의 성적이 저장되었습니다.")
    print()
  return stuNo
#-----------------------------------------------

### 학생성적 출력함수
def stu_output(students):
  for t in s_title:
    print(f"{t}\t",end="")
  print(); print("-"*60)

  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
  print()
#-----------------------------------------------

### 학생성적 수정함수
def stu_update(students):

  name = input("수정하고자 하는 학생 이름을 입력하세요.")

  for s in students:
    check = 0
    if s['name'] == name:
      print(f"{name} 학생의 정보를 찾았습니다.")
      print("[ 수정과목 선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("수정하고자 하는 과목번호를 선택하세요.")

      if choice == "1":
        print("이전 국어점수 :",s['kor'])
        s['kor'] = int(input("변경 국어점수 : "))
      elif choice == "2":
        print("이전 영어점수 :",s['eng'])
        s['eng'] = int(input("변경 영어점수 : "))
      elif choice == "3":
        print("이전 수학점수 :",s['math'])
        s['math'] = int(input("변경 수학점수 : "))
      
      s['total'] = s['kor']+s['eng']+s['math']
      s['avg'] = s['total']/3

      print(f"{name} 학생의 성적이 수정되었습니다.")
      check = 1
      stu_output([s])

  if check == 0:
    print(f"{name} 학생의 정보가 없습니다. 다시 입력해주세요.")
    print()
#-----------------------------------------------

### 학생성적 검색함수
def stu_search(students):

  while True:
    check = 0
    name = input("검색하고자 하는 학생 이름을 입력하세요. (0. 이전화면)")
    if name == "0":
      break
    sArr = []
    for idx,s in enumerate(students):
      if s['name'].find(name) != -1: 
        sArr.append(s)
        check = 1
    if check == 0:
      print("찾는 학생이 없습니다.")
    else:
      print(f"{name}의 이름으로 {len(sArr)}명이 검색되었습니다.")
      stu_output(sArr)
#-----------------------------------------------

### 학생성적 삭제함수
def stu_delete(students):

  name = input("삭제하고자 하는 학생 이름을 입력하세요.")



while True:
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
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == "1":
    print("[ 1. 학생성적 입력 ]")
    print()
    stuNo = stu_input(stuNo)

  elif choice == "2":
    print("[ 2. 학생성적 출력 ]")
    print()
    stu_output(students)
  elif choice == "3":
    print("[ 3. 학생성적 수정 ]")
    print()
    stu_update(students)
  elif choice == "4":
    print("[ 4. 학생성적 검색 ]")
    print()
    stu_search(students)
  elif choice == "5":
    print("[ 5. 학생성적 삭제 ]")
    print()
    stu_delete(students)
  elif choice == "6":
    pass
  elif choice == "0":
    print("[ 0.프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break