### 리스트 (정수, 문자열, 실수 등 서로 다른 데이터형도 묶기 가능) // 배열 (동일한 데이터형만 묶을수 있음)

a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
total = 0

### a,b,c,d,e 의 변수에 숫자를 입력받아 합계를 출력하시오.

a = int(input("숫자 1을 입력하세요."))
b = int(input("숫자 2을 입력하세요."))
c = int(input("숫자 3을 입력하세요."))
d = int(input("숫자 4을 입력하세요."))
e = int(input("숫자 5을 입력하세요."))
f = int(input("숫자 6을 입력하세요."))
g = int(input("숫자 7을 입력하세요."))

total = a+b+c+d+e+f+g
print("합계 : ",total)

############################

a_list = [0, 0, 0, 0, 0, 0, 0]
total = 0

for idx, a in enumerate(a_list):
  a = int(input(f"{idx+1}번쨰 숫자를 입력하세요."))
  total += a

print("합계 : ",total)

############################

a_list = []
total = 0

for i in range(7):
  j = int(input(f"{i+1}번째 숫자를 입력하세요."))
  a_list.append(j)
  total += j

print("합계 : ",total)

############################

a_list = []
total = 0
## 1부터 100까지 들어가있는 리스트를 출력하시오.

for i in range(1, 101):
  a_list.append(i)
  total += i

print(a_list)
print("합계 :",total)

############################

a_list = [1, 2, 3.0, "안녕", True, False]

print(a_list[0])
print(a_list[3])
print(a_list[-1]) # 음수는 거꾸로

############################

a_list = [1, 2, 3, 4, 5]

## 역순 출력
for i in range(1, 5+1):
  print(a_list[-(i)])

print("-"*60)

for i in range(1, len(a_list)+1):
  print(a_list[-i])

############################

a_list = [1, 2, 3, 4, 5]
## b_list = a_list >> 얕은 복사 (같은 주소)
## b_list = a_list[:] >> 깊은 복사 (다른 주소) [:] : 처음부터 끝 >> [0:3] : 0부터 3 앞까지
b_list = a_list[::-1] # 새로운 주소로 생성 [::-1] : 처음부터 끝을(:) 역순으로(:-1) 

print(a_list)
print(b_list)

a_list[0] = 100 # b_list에는 적용 안된다.
print(a_list)
print(b_list)

############################

# ##리스트 출력방법 

a_list = [1, 2, 3, 4, 5]
b_list = [50, 100]

print(a_list[0:3])  
print(a_list[2:4])  
print(a_list[:3]) # 처음부터 3 앞
print(a_list[3:]) # 3부터 끝 
print(a_list+b_list) # a리스트 뒤에 b리스트
print(b_list*3) # 3번 반복
print(a_list[::2]) # 2칸씩

############################

# ## 리스트 수정
a_list = [1, 2, 3, 4, 5, 6, 7]
a_list[3] = 50
a_list[1:2] = [20, 30] # 2개 변경
a_list[4] = [10, 20] # 4번자리에 [10, 20] 배열이 들어감

print(a_list)

############################

# ## 리스트 삭제
a_list = [1, 2, 3, 4, 5]
del a_list[0]
a_list[1:3] = [] # [2, 3] 삭제
a_list = []; a_list = None; # 전체삭제 : [], None // del(a_list) : 리스트 자체를 삭제

print(a_list)

############################

# ## 리스트 함수
a_list = [1, 2, 3, 4, 5]
print(len(a_list)) # 리스트 갯수
print(a_list.count(3)) # 입력된 값의 갯수 (3이 몇개냐 >> 1개)
a_list.append(200) # 뒤 쪽에 값(200) 추가
a_list.insert(0, 100) # insert(x, y) : x번째(index위치)에 y를 입력(값 저장) // 수정 아님 추가
print(a_list.pop(2)) # 해당 위치의 값을 삭제
a_list.remove(3) # 리스트에 입력된 값을 삭제 (3을 삭제)
del(a_list[4]) # 해당 위치의 리스트 삭제
a_list.clear() # 전체삭제
print(a_list)