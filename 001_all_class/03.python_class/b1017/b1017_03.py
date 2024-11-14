### 예외(런타임 에러)처리 : try: - except:

## 구문에러 : 프로그램이 실행 전에 오류가 남
## 런타임에러 : 프로그램 실행 도중 오류가 남
# print("프로그램 시작")

# try:
#   print(list_a) # 런타임 에러
# except:
#   print("에러가 발생") # 에러가 발생했을 때 처리할 수 있는 문구

# print("프로그램 종료")

# n_str = input("반지름을 입력하세요. >>")
# # if n_str.isdigit(): # isdigit : 정수이냐 아니냐 판단
# try:
#   num = int(n_str)
#   print("원 넓이 : ",(num**2)*3.14)
#   print("원 둘레 : ", 2*3.14*num)

# # else:
# except Exception as e : # Exception as e : 어떤 에러가 났는지 알려줌 (에러는 따로 백업해두기(프로그램 수정))
#   print("정수가 아닙니다. 정수를 입력하세요.",e)

### 숫자에 **2를 하는 프로그램을 구현
# list_a = [1,2,3,4,5,"홍길동",5,6]
# list_b = []
# try:
#   for a in list_a:
#     list_b.append(a**2)

# except Exception as e: # 홍길동에서 오류가 나서 for문을 빠져나왔기때문에 5,6은 찍히지 않음
#   print(e)
# print(list_b)

### try - except : try에 에러가 발생하면 except로 넘어가서 실행
### try - except - else : try에 에러가 발생하지 않으면 else 실행
### try - except - finally : 에러 발생 여부와 상관없이 finally 실행

# print("1")
# try:
#   print("2")
#   #print(4/0) # try 구문에 에러가 발생해야 except 구문을 실행시킴
#   print(3/0) # 에러가 발생하면 except 구문으로 넘어감 (3,4 x)
#   print("3")
#   print("4")

# except:
#   print("5")
#   print("6")

# else: # 에러가 발생하지 않았을 때 실행할 코드
#   print("7")
#   print("8")

# finally: #에러의 발생 여부와 상관없이 실행
#   print("9")
#   print("10")

# f = open("b1017/a.txt","w",encoding="utf-8")
# try:
#   f.write("안녕하세요.1\n")
#   f.write("안녕하세요.2\n")
#   f.write({"a":1})
#   f.write("안녕하세요.4")
#   # f.close() # 파일을 무조건 닫아줘야 되기 때문에
# except Exception as e:
#   print(e)
#   # f.close() # 중복해서 적어주어야 함
# finally:
#   f.close() # 이런 상황일때 finally 사용

numbers = [52,273,32,103,90,10,275,1,2,1,2,12]

try:
  print(numbers.index(52))
  print(numbers.index(1))
  print(numbers.index(3))
  print(numbers.index(32))
  print(numbers.index(90))

except Exception as e:
  print("찾는 번호가 없습니다.",e)
