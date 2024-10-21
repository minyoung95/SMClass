def func(v):
  return v*2

print(func(2))

aArr = [1,2,3,4]

bArr = []
for a in aArr:
  bArr.append(func(a))

print("bArr : ",bArr)

## 리스트 내포
cArr = [a*2 for a in aArr]
print("cArr : ",cArr)

## map 함수 : map(함수, 반복가능한 자료형(리스트,튜플,딕셔너리)) - 리스트의 내용을 1개씩 함수에 전달하여(전부) 결과값을 저장
dArr = list(map(func, aArr)) # list타입으로 변경
print(type(dArr)) # map 타입이므로
print("dArr : ",dArr)

eArr = list(map(lambda x:x*2,aArr)) # lambda x(매개변수v):x*2(v*2)(수식) >> x*2의 값을 eArr에
print("eArr : ",eArr)

## 짝수만 있는 리스트 만들기 (기본함수사용방법)
def function(v):
  if v%2 == 0:
    return v
fArr = []
for i in aArr:
  if function(i) != None:
   fArr.append(function(i))
print("fArr : ",fArr)

## filter 함수 사용방법(함수, 반복가능한 자료형(리스트,튜플,딕셔너리))

def fun(v):
  if v%2 == 0:
    return True
  else:
    return False

gArr = list(filter(fun,aArr)) # aArr 값 중 함수의 조건에 맞는 경우(2의 배수인경우)만 결과값 저장
print("gArr : ",gArr)

## 람다식 변경
def f(v1,v2):
  return v1*v2

lambda v1,v2:v1*v2

hArr = list(filter(lambda x:x%2==0,aArr))
print("hArr : ",hArr)

## zip 함수 : 2개의 리스트를 1개로 묶음
a = [1,2,3,4]
b = [10,20,30,40]

print(list(zip(a,b))) # 튜플타입 [(1, 10), (2, 20), (3, 30), (4, 40)]
print(dict(zip(a,b))) # 딕셔너리타입 {1: 10, 2: 20, 3: 30, 4: 40}

### 문제

c = [1,2,3,4]
d = [10,20,30,40]

# 리스트내포
iArr = [i+j for i,j in zip(a,b)]
print("iArr : ",iArr)

# lambda
jArr = list(map(lambda i,j:i+j,a,b)) # map(lambda 매개변수1,매개변수2:리턴값,복합자료형1,복합자료형2)
print("jArr : ",jArr)

# 함수사용
kArr = []
def fu(a,b): # 매개변수가 두개일땐
  for i,j in zip(a,b): # for문에서 zip으로 묶어서 i,j에 보냄
    kArr.append(i+j)
  return kArr

print(fu(a,b))

### 문제
### a리스트에 전부 10을 더해서 리스트에 담아 출력하시오
### 리스트내포, map 람다식 이용
a = [1,2,3,4,5]

lArr = [i+10 for i in a]
print("lArr : ",lArr)

mArr = list(map(lambda x:x+10,a)) # 앞에 x는 걍 아무거나 변수지정, 복합자료형이 함수의 매개변수 a,b 같은거
print("mArr : ",mArr)

### 4*3*2*1
result = 1
for i in range(1,5):
  result *= i
