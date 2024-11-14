# 1, 10까지 for문을 사용하여 출력
for i in range(1,10+1):
  print(i)

# 1, 3, 5, 7, 9
for j in range(1, 10+1):
  if j%2 == 1:
    print(j)

# 구구단을 출력
for k in range(2, 9+1):
  print(f"[{k} 단]")
  for l in range(1, 9+1):
    print(f"{k} * {l} = {k * l}")
  print("-"*50)


# 구구단 1, 3, 5, 7, 9
for m in range(2, 9+1):
  if m % 2 == 1:
    print(f"[{m}단]")
    for n in range(1, 9+1):
      print(f"{m} * {n} = {m * n}")

for o in range(1, 10, 2): # 1부터 9까지 2씩 증가
  for p in range(1, 10):
    print(f"{o} * {p} = {o * p}")

print("-"*50)

# for 문을 사용해서
# *
# **
# ***
# ****
# *****
for q in range(1, 6):
  print("*" * q)

# *****
# ****
# ***
# **
# *

for r in range(5, 0, -1): # -1씩 감소
  print("*" * r)

for s in [1, 2, 3]:
  print("안녕하세요. \n" * s, end="") # end="" : 맨마지막 역슬래시 없애기
  print("-"*30)

# for s in [1, 2, 3]:
#   for t in range(s):
#     print("안녕하세요.")
#   print("-"*30)

for t in range(3):
  print(f"{t} : 안녕하세요.")
print("-"*30)

# 변수를 쓰지 않아도 될때
# for _ in range(3):

# 1, 100까지 숫자의 합을 구하시오
sum = 0
# for u in range(1, 100+1):
#   sum += u
# print("합계 : ",sum)

# 홀수 합
# for v in range(1, 100+1):
#   if v%2 == 1:
#     sum += v
# print(sum)

# 두 수를 입력받아, 두 숫자 사이의 합계를 구하시오.
# ex ) 3,8 > 3+4+5+6+7+8

a = int(input("숫자1을 입력하세요"))
b = int(input("숫자2를 입력하세요"))
### 1. if 문 사용
min_num = a
max_num = b
if a > b:
  min_num = b
  max_num = a
  # min_num = b; max_num = a : 한줄로 쓸땐 중간에 ;

### 2. if 문 사용2
# if a > b :
# a, b = b, a (두개 변수 치환 - 파이썬만)
# c = a; a = b; b = c (두개 변수 치환할때 c라는 변수가 필요 - 다른언어)

### 3. min, max 함수 사용
# min_num = min(a, b); max_num = max(a, b)

for w in range(min_num, max_num + 1):
# for w in range(a, b + 1): - 2. if문 사용2
# for w in range(min(a, b), max(a, b) + 1): - 3. min, max 함수 사용

  sum += w
print("합계 :",sum)
