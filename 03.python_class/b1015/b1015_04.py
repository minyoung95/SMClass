students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
choice = 0
check = 0

# 학생성적 출력함수
def stu_output(s_title,students):
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
def stu_update(s_title,students):
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
      stu_output(s_title,[s]) # s 한명의 데이터만 함수로 보냄 
      # s는 딕셔너리 타입이므로 리스트로 바꿔줌, 함수의 매개변수 students가 리스트 타입이므로 타입을 맞춰줌
      check = 1
    
  # 학생이 검색되지 않았을 때
  if check == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
    print()
# --------------------------------------

choice = input("원하는 번호를 선택하세요.")

if choice == "3":
  stu_update(s_title,students)