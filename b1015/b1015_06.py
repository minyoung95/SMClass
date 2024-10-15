students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"김관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순동","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강홍찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구길","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
choice = 0
stuNo = 0 # 학생번호
stuNo = len(students) # 리스트에 이미 학생이 차 있을 시 그 이후 번호로 지정해줌
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0 # 성적처리에 필요한 변수
count = 1 # 등수처리
check = 0 # 체크할때 변수

print("[ 5. 학생성적 삭제 ]")
print()

name = input("찾고자 하는 학생의 이름을 입력하세요.")
check = 0
for idx,s in enumerate(students):
  if s['name'] == name:
    check = 1
    print(f"{name} 학생 성적을 삭제하시겠습니까? (삭제 시 복구불가)")
    choice = input("1. 삭제 2. 취소 >>")
    if choice == "1":
      del students[idx]
      print(f"{name} 학생의 성적이 삭제되었습니다.")
    else:
      print("학생성적 삭제가 취소되었습니다.")
      break

if check == 0:
  print(f"{name} 학생이 없습니다. 다시 입력하세요.")
  print()

#stu_output(s_title,students)