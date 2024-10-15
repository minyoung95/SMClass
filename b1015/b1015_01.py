### 함수정의
# def calc(st,end):
#   for i in range(st,end+1):
#     print(f"[ {i} 단 ]")
#     for j in range(1,9+1):
#       print(f"{i} * {j} = {i*j}")

# calc(2,9) # 함수호출

### 매개변수 : 기본, 가변, 키워드
## 기본 매개변수 : 정의에서 매개변수가 2개이면 호출도 2개로 
# def plus(n1,n2):
#   sum = n1+n2
#   print("합계 : ",sum)

# plus(10,20)

## 가변 매개변수 : 호출 갯수와 상관없이 받을 수 있음
# def plus(a,*n1):
#   print("a :",a) # (a, *n1) : 제일 앞에 있는 변수를 a에 할당해주고 나머지는 *n1 // (*n1, a) : *n1에서 모든변수를 할당 받기때문에 a에는 할당을 안해줌 (에러)
#   for i in n1:
#     print(i)
#   print(type(n1)) # 매개변수를 리스트(튜플)타입으로 받음

# plus(1,2,3,4,5) 

## 키워드 매개변수
def plus(k = 10,m = 5): # 호출할때 매개변수가 없으면 기본값으로 사용
  print("m :",k)
  print("m :",m)

plus() # 매개변수의 갯수가 일치하지 않아도 에러 x
plus(1) # 첫번째 자리(10) 대신에 1을 할당
plus(m=1,k=2) # 앞뒤 바뀌어도 상관x

print("-"*60)

## 가변매개변수와 키워드 매개변수를 같이 사용할 경우
def plus(*n, k=10):
  print("k :",k)
  for i in n:
    print(i)

plus(1,2,3,4,5,k=20) # 키워드 매개변수가 뒤쪽에 와야함