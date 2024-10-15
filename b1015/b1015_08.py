from SS import * ## SS모듈 함수를 다 가져옴 (함수 뿐만 아니라 위 데이터(s_title)도 다 가져옴)
# import SS

# import math
# from math import *
import math as m # m으로 줄여서 사용 가능
print(m.floor(1.23)) # 버림
print(m.ceil(1.23)) # 올림
# print(m.roud(1.23)) #반올림

from urllib import request

target = request.urlopen("http://www.google.com")
output = target.read() # 웹스크랩핑

print(output)


students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

stu_output(students) # students 가 모듈에 없으므로 모듈로 보내줘야된다. (매개변수를 통해)
print(s_title)

### import SS 로 모듈을 가져올 경우
## SS.stu_output(students)
## print(SS.s_title)



