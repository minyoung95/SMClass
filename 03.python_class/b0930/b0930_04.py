#### 변수
# 정수형(intVar), 실수형(floatVar), 문자형(strVar), 논리형(boolVar)

name = input("이름을 입력하세요.")
kor = input("국어점수를 입력하세요.")
eng = input("영어점수를 입력하세요.")
math = input("수학점수를 입력하세요.")
total = int(kor)+int(eng)+int(math)
avg = (int(kor)+int(eng)+int(math))/3

print("이름 : {} kor : {} eng : {} math : {} 합계 : {} 평균 : {:.2f}".format(name, kor, eng, math, total, avg))
print(f"이름 : {name} kor : {kor} eng : {eng} math : {math} 합계 : {total} 평균 : {avg:.2f}")

# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b) # 문자연결연산자 : 이어져서 나옴 100200
# print(int(a)+int(b)) # int() 타입변경
# # print(int(name)) # 문자를 숫자로 변경 불가
# c = "3.14"
# print(int(float(c))) # 실수형으로 변경 후 정수형으로
# # print(int(c)) # 실수인 문자는 정수로 바로 변경 불가
# print(str(c)) # 실수형을 문자형으로 바꿈

# d = "True"
# print(bool(d)) # 문자논리형을 논리형으로 변경


# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True # True, False : 첫자 대문자로 넣어야 함
# print(type(a_bool))

# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3

# print(var4)

# v4 = v3 = v2 = v1 = 100
# print(v4)