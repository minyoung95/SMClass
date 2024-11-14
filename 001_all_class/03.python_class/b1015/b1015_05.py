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

# ss = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠"
# print(ss.find("공부"))
# print(ss.find("자바")) # find : 없을때 -1이 리턴
# print(ss.index("공부"))
# print(ss.index("자바")) # index : 없으면 에러

print("[ 학생성적 검색 ]")
print()

while True:
  name = input("검색하려는 이름을 입력하세요.")
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
    stu_output(s_title,sArr)