### 10-5, 20-7, 30-3 끼리 사칙연산

num1 = [10, 20, 30]
num2 = [5, 7, 3]

for i in range(len(num1)):
  print(f"두수 더하기 : {num1[i]+num2[i]}")
  print(f"두수 빼기 : {num1[i]-num2[i]}")
  print(f"두수 곱하기 : {num1[i]*num2[i]}")
  print(f"두수 나누기 : {num1[i]/num2[i]}")

def calc(num1,num2):
  print(f"두수 더하기 : {num1+num2}")
  print(f"두수 빼기 : {num1-num2}")
  print(f"두수 곱하기 : {num1*num2}")
  print(f"두수 나누기 : {num1/num2}")

for i in range(len(num1)):
  calc(num1[i],num2[i])

### 두수를 입력받아 사칙연산

num1 = int(input("숫자 1을 입력하세요."))
num2 = int(input("숫자 2를 입력하세요."))

def calc(num1,num2):
  print(f"두수 더하기 : {num1+num2}")
  print(f"두수 빼기 : {num1-num2}")
  print(f"두수 곱하기 : {num1*num2}")
  print(f"두수 나누기 : {num1/num2}")

calc(num1,num2)

###

numStr = input("숫자를 입력하세요. (12, 5)")
numStr2 = numStr.split(",")

num1 = int(numStr2[0])
num2 = int(numStr2[1])

def calc(num1,num2):
  print(f"두수 더하기 : {num1+num2}")
  print(f"두수 빼기 : {num1-num2}")
  print(f"두수 곱하기 : {num1*num2}")
  print(f"두수 나누기 : {num1/num2}")

calc(num1,num2)

### 3개의 숫자를 입력받아 숫자를 계산

numStr = input("숫자를 입력하세요. (12 ,5 ,7)")
numStr2 = numStr.split(",")

num1 = int(numStr2[0])
num2 = int(numStr2[1])
num3 = int(numStr2[2])

def calc(num1,num2,num3):
  print(f"두수 더하기 : {num1+num2+num3}")
  print(f"두수 빼기 : {num1-num2-num3}")
  print(f"두수 곱하기 : {num1*num2*num3}")
  print(f"두수 나누기 : {num1/num2/num3}")

calc(num1,num2,num3)

### ★★★배열★★★

numStr = input("숫자를 입력하세요. (12 ,5 ,7)")
numStr2 = numStr.split(",")
numStr2 = [ int(i) for i in numStr2]
print(numStr2)

def calc(n):
  s1 = 0
  s2 = 0
  s3 = 1
  s4 = 1
  for i in range(len(numStr2)):
    s1 += numStr2[i]
    s2 -= numStr2[i]
    s3 *= numStr2[i]
    s4 /= numStr2[i]
  print(f"수 더하기 : {s1}")
  print(f"수 빼기 : {s2}")
  print(f"수 곱하기 : {s3}")
  print(f"수 나누기 : {s4}")

calc(numStr2)

### 가변 매개변수(*n) : 튜플타입으로 변수를 받음
def calc(*n):
  print(n)
  print(len(n))

calc(1,2,3)

### 키워드 매개변수(n1 = x) : 변수를 지정하지 않았을때 x로 받음
def calc(n1 = 10, n2 = 20):
  print(n1)
  print(n2)

calc() # 10 20
calc(20) # 20(키가 없으므로 첫번째(n1)) 20(n2)

print(1,2,3,sep=":",end="\t") # 숫자 : 가변 매개변수, sep/end : 키워드 매개변수


### ★★★전역변수, 지역변수★★★

## 함수 내에 선언된 변수는 외부에서 사용할 수 없음
def calc(v1,v2):
  global sum # global : 전역변수 ((1)을 끌고옴)
  # sum = 0 # 지역변수
  for i in range(v1,v2+1):
    sum += i
  return sum # 리턴으로 외부로 sum 반환

sum = 100 # (1) 외부의 변수를 사용해서 계산을 하고 싶을 경우
sum = calc(1, 10)
print(sum)

###
def calc(n1,n2):
  s1 = n1+n2
  s2 = n1-n2
  s3 = n1*n2
  s4 = n1/n2
  s5 = [s1, s2, s3, s4]
  return s5

s5 = calc(10,5)
print(s5)

### 매개변수가 일반변수 일 경우 return 하지 않으면 변수값 변동이 없음.
hh = 100
def add(hh):
  hh = hh + 100 # hh = 200이지만 리턴이없음

add(hh) 
print(hh) # hh = 100

### 매개변수가 복합변수(변수 하나의 여러개의 값이 저장되어있음 ex) 리스트, 딕셔너리) 일 경우 : hong(복합변수)를 h(매개변수)로
hong = [1, 2, 3, 4, 5]
def add(h):
  for i in range(len(h)): 
    h[i] = h[i] + 100 # 리턴이 없지만 값이 변경되어 hong으로 전달

add(hong)
print(hong)


### ★★★ 전역변수인 경우 함수 외부, 내부 둘다 사용이 가능함.★★★
### ★★★ 지역변수는 return 없이는 값이 함수 밖으로 나가지 못함.★★★
def calc():
  global sum # 전역변수인 경우, 함수에서 변경시 외부에서도 같이 변경된다.
  sum = 100 # sum의 값을 100으로 변경

sum = 10
calc()
print(sum)