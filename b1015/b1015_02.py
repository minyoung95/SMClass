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

## 학생성적입력 함수
def stu_input(stuNo,students):
  while True:
    print("[ 1. 학생성적 입력 ]")
    print()

    no = stuNo + 1
    name = input(f"{no}번째 학생이름을 입력하세요. (0. 이전화면)")
    if name == "0":
      print("이전화면으로 이동")
      break
    score = []
    total = 0
    for i in range(3):
      s_input = int(input(f"{s_title[i+2]}점수를 입력하세요."))
      total += s_input
      score.append(s_input)

    # kor = int(input("국어점수를 입력하세요."))
    # eng = int(input("영어점수를 입력하세요."))
    # math = int(input("수학점수를 입력하세요."))
    # total = kor+eng+math

    avg = total/3
    rank = 0

    s = {"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank}
    students.append(s)
    stuNo += 1

    print(f"{name} 학생의 성적이 저장되었습니다.")
    print()
    print(students)
  return stuNo


## 프로그램 시작 ##
choice = input("원하는 번호를 입력하세요.")

if choice == "1":
  stuNo = stu_input(stuNo,students)
  print("현재 학생번호 : ",stuNo)
