def num_sum(st, end): # def 함수이름(매개변수, 매개변수)
  sum = 0
  for i in range(st, end+1):
    sum += i
  print("합계 : ",sum)

# # 1~10까지 합계
num_sum(1, 10)

# # 1-100까지 합계
num_sum(1, 100)

# # 2-50까지 합계
num_sum(2, 50)

# # 100-1000까지 합계
num_sum(100, 1000)

### 두 수를 입력받아, 그 사이의 숫자 합을 구하시오.

num1 = int(input("숫자1을 입력하세요."))
num2 = int(input("숫자2을 입력하세요."))

num_sum(num1, num2)

### 2-50, 3-7, 5-50 의 합들을 모두 더해서 출력하시오

def num_sum(st,end):
  sum = 0
  for i in range(st,end+1):
    sum += i
  return sum # 호출하는 곳으로 값을 반환해줌

print(f"2-50까지의 합 : {num_sum(2,50):,d}")
print("3-7까지의 합 : ",num_sum(3,7))
print(f"5-50까지의 합 : {num_sum(5,50):,d}")

total = num_sum(2,50) + num_sum(3,7) + num_sum(5,50)

print("합계 : {:,d}".format(total))

def plus(n1,n2):
  result = n1+n2
  return result

# return의 정확한 개념?

# def plus(n1,n2):
#   return n1+n2

print(plus(1,2))
print(plus(55,45))
print(plus(50,50))

### 두 수를 입력받아 더하기를 출력하시오

num1 = int(input("숫자 1을 입력하세요"))
num2 = int(input("숫자 2을 입력하세요"))

def plus(num1,num2):
  return num1+num2

print(plus(num1,num2))