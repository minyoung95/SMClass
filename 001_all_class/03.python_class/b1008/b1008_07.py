import operator
## 딕셔너리 정렬

nameDic = {'홍길동':100, '유관순':80, '이순신':70, '강감찬':60, '김구':90}
print(nameDic)

# key - nameDic.keys()
# value - nameDic.values()
# key, value - nameDic.items()
# (key, value) : key - [0], value - [1]

# lambda x:x[0], lambda x:x[1]

nameDics = sorted(nameDic.items()) # [0]번째(key값)를 기준으로 순차정렬
nameDics = sorted(nameDic.items(), reverse=True) # [0]번째(key값)를 기준으로 역순정렬
nameDics = sorted(nameDic.items(), key=lambda x:x[0])
nameDics = sorted(nameDic.items(), key=operator.itemgetter(1)) # [1]번째(value값)을 기준으로 순차정렬
nameDics = sorted(nameDic.items(), key=operator.itemgetter(1), reverse=True) # [1]번째(value값)을 기준으로 역순정렬
nameDics = sorted(nameDic.items(), key=lambda x:x[1])
print("-"*50)
print(nameDics)

# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0}
# ]

numList = []

for i in range(5):
  numList.append(i+1)

## for 문을 1줄로 사용 : 리스트내포, 컴프리헨션

name = ["홍길동", "유관순", "이순신"]
score = [100, 90, 95]

nList = [i+1 for i in range(5)]

a_list = [i*i for i in range(5)]

b_list = [str(i) for i in range(5)]

c_list = ["5", "9", "0", "6", "1",]
cc_list = [int(i) for i in c_list]

# d_str = "1, 2, 23, 5, 9"
# d_sp = [int(i) for i in d_str.split(",")] # 배열로 묶기

score = input("좌표입력 (0,0) >>")
sc = [int(i) for i in score.split(",")]
print(score)
print(sc)

# zip() 함수 : 동시에 여러개 리스트에 접근
n_list = []
for n,s in zip(name,score):
  n_list.append([n,":",s])
  print(n_list)

n_list = list(zip(name, score)) # 튜플타입의 리스트 생성
print(n_list)

name = ["홍길동", "유관순", "이순신"]
score = [100, 90, 95]

## 딕셔너리 타입 리스트 생성

d_dic = dict(zip(name,score))
print(d_dic)