### 리스트에 대한 정렬
students = [
  [1,"홍길동",100,100,99,299,99.67,0],
  [2,"유관순",80,80,85,245,81.67,0],
  [3,"이순신",90,90,91,271,90.33,0],
  [4,"강감찬",60,65,67,192,64.00,0],
  [5,"김구",100,100,84,284,94.67,0]
]

# sort() : 리스트에만 지원되는 정렬함수
print(students)
print("-"*60)
students.sort(key=lambda x:x['name'])

print(students)

# 함수를 사용하여 순차정렬
def stu_sort(x):
  return x[1]
students.sort(key=stu_sort)

students.sort(key=lambda x:x[1]) # lambda x(리스트 하나하나를 x에) :x[1] (리스트x의 x[1]를 기준으로) 순차정렬
students.sort(key=lambda x:x[1],reverse=True) # 역순정렬
students.sort(key=lambda x:x[5],) # 순차정렬
students.sort(key=lambda x:-x[5]) # 역순정렬 (숫자는 -만 붙이면 된다.)

x = sorted(students,key=lambda x:x[1]) # sorted함수를 사용하여 정렬 (자체데이터(students) 변경 x)
print(x)
print(students)

## 정렬
aArr = [4,5,6,1,2]
aArr.sort() # 순차정렬 [1,2,4,5,6]
aArr.sort(reverse=True) # 역순정렬 [6,5,4,2,1]
aArr.reverse() # 리스트의 순서를 거꾸로 [2,1,6,5,4]

# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0}
# ]
