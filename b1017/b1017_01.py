subject = ["국어", "영어"]
score = []

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호 입력")
  
  if choice == "1":
    s_input = input("원하는 과목 입력")
    subject.append(s_input)
  elif choice == "0":
    break

for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.")))

# num1 = int(input("국어점수를 입력하세요"))
# num2 = int(input("영어점수를 입력하세요"))
# num3 = int(input("수학점수를 입력하세요"))
# num4 = int(input("과학점수를 입력하세요"))
# num5 = int(input("역사점수를 입력하세요"))

sum = 0
for i in range(len(subject)):
  print(f"{subject[i]} : ",score[i])
  sum += score[i]
print("합계 : ",sum)

# print("국어 : ",num1)
# print("영어 : ",num2)
# print("수학 : ",num3)
# print("과학 : ",num4)
# print("역사 : ",num5)
# print("합계 : ",num1+num2+num3+num4+num5)


# def output(subject):
#   print("과목")
#   print("-"*20)
#   # subject를 세로로 출력
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요. >>")
#   subject.append(s_input) # list - append
#   output(subject)


# ------------------------------------------------

# a = 10 # 전역변수

# def func():
#   global a ## a=10을 가리킴
#   # a = 50 # 지역변수 - 함수를 종료하면 모두 제거
#   print("함수 내 a: ",a) # a = 50 ## a = 10
#   a += 50 ## 전역변수 a = 10을 60으로 변경

# func()
# # 함수 종료 : a = 50은 없어짐 (전역변수 a는 바뀌지않음)
# print("함수 밖 a: ",a) # a = 10 ## a = 60

# ------------------------------------------------

### 변수는 넘겨주고 리턴받기

# a = 10 # 전역변수

# def func(a): # a를 받아옴
#   print("함수 내 a: ",a) # a = 10
#   a += 50
#   return a # a를 함수 밖으로 반환

# a = func(a) # a에 값을 다시 대입
# print("함수 밖 a: ",a) # a = 60

# ------------------------------------------------

# a = 10
# b = 20
# sum = 0

# def add(a,b):
#   return a+b # a+b값을 반환

# sum = add(a,b)
# print("합계 : ",sum)

# ------------------------------------------------

## 함수를 사용하여, a+b+c의 합을 a에 저장해서 출력
# a = 10
# b = 20
# c = 30

# def add(a,b,c): # 함수내에 새롭게 선언된 지역변수 a,b,c (x,y,z로 바꿔도 상관x) // 값은 10,20,30 같지만 전역변수와 다른공간
#   a = a+b+c
#   return a

# add(a,b,c) # 전역변수 a,b,c(10,20,30)
# print("합계 : ",a)