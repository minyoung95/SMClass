### 함수 - 매개변수 (일반변수, 복합변수)

### 1. 함수 일반매개변수 (return없으면 반환불가 >> 값 변경 x)
def calc(h):
  h += 100
  return h

h = 20
h = calc(h)
calc(h) # 호출만 함 (값은 넣어주지 않아서 변경이 되지않음.)
print(h)

### 2. 전역변수 (return없이 함수밖으로 값을 반환할수있음)
def calc():
  global h
  h +=100

h = 20
calc()
print(h)

a = 10
def calc(a):
  a += 10
  print(a)

calc(a)

### 3. 함수 복합매개변수 (return없이 함수밖으로 값을 반환할 수 있음)
def calc(hArr):
  for i in range(len(hArr)):
    hArr[i] += 100

hArr = [1, 2, 3, 4, 5] # 복합변수(리스트) : 주소값 저장
calc(hArr)
print(hArr)
