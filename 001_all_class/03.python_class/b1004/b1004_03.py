# for 변수 in range(x): 범위
# x번 반복해라 (0부터 1씩 증가)

for i in range(10):
  print(i)
print("-"*50)

for j in range(5, 10): # 5부터 9까지(10 이전)
  print(j)
print("-"*50)

for o in range(1, 10, 2): # (시작값, 끝값+1, 증가값)
  for p in range(1, 10):
    print(f"{o} * {p} = {o * p}")

a_list = [1, 2, 3, 4, 5]
for k in a_list:
  print(k)
print("-"*50)

### 리스트 타입
b_list = [3, 5, 9, 20, 30, 3, 3, 10, 5, 20]
for m in b_list:
  print(m)
print("-"*50)

print(len(b_list)) # 배열(리스트)의 길이
print(b_list.count(3)) # 배열(리스트) 안에 해당되는 숫자가 몇개 인지 확인 (3이 몇개인지)

print("-"*50)

# 리스트 추가 - append, insert, extend([2,3]) : 리스트를 추가
b_list.extend([2,3])
print(b_list)
# 리스트 삭제 - del, remove, clear(모두삭제)

### 딕셔너리타입 - {} : json 타입과 모양이 같음. 키:값(key:value)
dic = {
  "번호" : 1,
  "이름" : "홍길동",
  "국어" : 100,
  "영어" : 100,
  "수학" : 100
}
print(dic["번호"]) # 번호(key 값)의 value가 출력

for n in dic: # dic에서 key값을 n에 넣어줌
  print(n) # key값이 출력
  print(dic[n]) # value 값 출력