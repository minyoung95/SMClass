# dictionary : 중괄호로 묶어 키(key):값(value)로 구성

dic1 = {"번호":1, "이름":"홍길동", "kor":100, "eng":100}
print(dic1)
print(dic1["이름"]) # 키를 입력하면 값을 출력
print(dic1.get("이름")) # 없는 키 입력 시 None (에러 x)

if dic1.get("이름") != None: # 이름이 None 이 아닐경우
  print(dic1.get("이름")) # 출력하세요

dic1["math"] = 90 # 없는 키와 값을 입력 시 추가
dic1['kor'] = 50 # 있는 키의 값을 입력 시 수정
del(dic1['eng']) # del(키) 입력하면 삭제
print(dic1)

print(dic1.keys()) # 모든 키 값 출력

### 모든 키 출력
for key in dic1.keys():
  print(key)
  print(dic1[key]) # value 값 출력
  print(key, dic1[key]) # key, value 출력

print(type(dic1.keys())) # type : class(객체)타입

list(dic1.keys()) # 리스트타입으로 변경

print(list(dic1.keys()))
print(list(dic1.keys())[0])

### 값만 출력
print(dic1.values()) # type : class(객체)타입
print(list(dic1.values()))

### 키, 값을 모두 출력

print(dic1.items()) # 튜플 타입 (수정x)
print(list(dic1.items())) 

## 키만 추출
for key in dic1:
  print(key)

## 값(value)만 추출
for key in dic1:
  print(dic1[key])

## 키, 값을 추출
for key,val in dic1.items():
  print(key,val)

# 평균이 없을때만 평균을 추가
if '평균' not in dic1:
  dic1['평균'] = 99.0

print(dic1)