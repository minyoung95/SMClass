### for문은 조건을 결정 후 횟수만큼 반복, while문은 조건식이 참일 때 반복

# i = 0
# while (i < 10):
#   print(i)
#   i += 1

# for i in range(10):
#   print(i)

## while 문 구구단
# i = 1
# while i < 10:
#   j = 1 # while j 문이 한바퀴 돌고 while i 문이 한바퀴 돌때 다시 j = 1(초기값)이 설정되게
#   while j < 10:
#     print(f"{i} * {j} = {i * j}")
#     j += 1
#   i += 1


# for i in range(1, 9+1):
#   for j in range(1, 9+1):
#     print(f"{i} * {j} = {i * j}")

# p = 0
# while True: # 무한반복
#   print(i); i += 1

## 입력한 숫자를 계속 더하는 프로그램 만들기
## 0이 입력되면 프로그램을 종료 할 것. (break)

# while True:
#   i_num = int(input("숫자를 입력하세요.")) 
#   sum = 0
#   if i_num == 0:
#     print("프로그램 종료")
#     break
#   sum += i_num
#   print("합계 : ",sum)

# i = 0; j = 0

# while i < 10:
#   print("번호 1 : ",i)
#   while j < 10:
#     if j == 5:
#       break # 반복문 종료
#     print("번호 2 : ",j)
#     j += 1
#   i += 1

## 이중 while 문 i는 1~10번, j는 1~10번 중 1,3,5,7,9

# i = 1; j = 1 # i, j = 1, 1

# while i < 10:
#   j = 1
#   while j < 10:
#     if j % 2 != 1:
#       j += 1
#       continue
#     print(i, j)
#     j += 1
#   i += 1

## 두수를 입력받아 + - * /

# while True:
#   num = int(input("숫자1를 입력하세요."))
#   num2 = int(input("숫자2를 입력하세요. (종료:0)"))

#   if num2 == 0:
#     break
#   print("[ 두 수의 사칙연산 ]")
#   print("-"*50)
#   print("1. 두 수 더하기")
#   print("2. 두 수 빼기")
#   print("3. 두 수 곱하기")
#   print("4. 두 수 나누기")
#   print("-"*50)
#   choice = int(input("원하시는 번호를 입력하세요. >>"))
#   if choice == 1:
#     print("결과값 : ", num+num2)
#   elif choice == 2:
#     print("결과값 : ", num-num2)
#   elif choice == 3:
#     print("결과값 : ", num*num2)
#   else:
#     print("결과값 : ", num/num2)

## 이름, 국어, 영어, 수학을 입력받아 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오

s_list = []
no = 1
while True:
  name = input("이름을 입력하세요. (종료 0)")
  if name == "0":
    break
  kor = int(input("국어점수를 입력하세요"))
  eng = int(input("영어점수를 입력하세요"))
  math = int(input("수학점수를 입력하세요"))
  print(f"번호 : {no}, 이름 : {name}, 국어점수 : {kor}, 영어점수 : {eng}, 수학점수 : {math}, 합계 : {kor+eng+math}, 평균 : {(kor+eng+math)/3:.2f}")
  no += 1

print("프로그램을 종료합니다.")