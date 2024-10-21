# # 두수를 입력받아 더하기 , 빼기, 곱하기, 나누기를 출력하시오.
# + - * /(소수점이 있는 몫), % 나머지, //(정수 몫), ** 제곱

# a = int(input("숫자1을 입력하시오."))
# b = int(input("숫자2을 입력하시오."))

# #print("{}, {}, {}, {}".format(a+b, a-b, a*b, a/b))

# print(a+b)
# print(type(a+b))
# print(a-b)
# print(type(a-b))
# print(a*b)
# print(type(a*b))
# print(a/b)
# print(type(a/b)) # 나누기는 실수로 타입이 바뀐다.

a = 0

for i in range(1, 11): # 1~10까지
  a += i
# a = a + i
print(a)

b = (10>100)
print(b) # False
print(type(b))
c = (10<100)
print(c) # True

# 함수 
d = 10 # 전역변수
def add():
  print(10 + 9)
  e = 20 # 지역변수