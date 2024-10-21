a_list = ['홍길동', '유관순', '이순신', '강감찬', '김구', '김유신', '홍길자']

a_list = [a+"님" for a in a_list]
print(a_list)

for a in a_list:
  print(a)

# enumerate() : index (번호)를 같이 출력 (index와 value값)
for i, a in enumerate(a_list):
  print(f"{i} : {a}")

b_list = [1, 2, 3, 4, 5]
# c_list = [1*1, 2*2, 3*3, 4*4, 5*5]

### 리스트 값을 변경하여 리스트에 저장
for idx, b in enumerate(b_list):
  b_list[idx] = b**2

#b_list = [b**2 for b in b_list] : 리스트 내포(for문)

print(b_list)


### 리스트 슬라이싱 0부터 4 앞까지 (3번까지)
print(b_list[0:4])

print(b_list[0:10]) # 리스트 범위보다 넘어서 출력하면, 에러가 나지 않고 범위까지 출력된다.

### 리스트 값 변경