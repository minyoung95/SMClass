# a = 5; b = 3 # 한줄로 쓸때 ;
# s1, s2, s3 = 1, 2, 3
# c, d = 10, 20
# # / % // **
# print("{}, {}, {}, {}".format(a/b, a%b, a//b, a**b))

# a = "100"
# b = "10.5"
# print(float(a))
# print(int(b))

# a = 10
# a += 5; print(a)
# a -= 5; print(a)
# a *= 5; print(a)
# a /= 5; print(a)
# a //= 5; print(a)
# a **= 5; print(a)
# a %= 5; print(a)

# 반지름을 입력받아 원의 넓이를 구하시오

# r = int(input("반지름을 입력하세요."))
# print(3.14*(r**2))

# #길이를 입력받아 삼각형의 넓이와, 사각형의 넓이를 구하시오
# a = int(input("변의 길이를 입력하시오."))
# h = int(input("높이를 입력하시오."))
# area1 = (a*h)/2
# area2 = a*h

# print("삼각형의 넓이 : {}".format(area1))
# print("사각형의 넓이 : {}".format(area2))

# length = input("두개의 길이를 입력하시오.") # 띄어쓰기로 두개 입력가능
# print(length.split(" ")) # 배열로 나눠줌

# l_list = length.split(" ")
# print("삼각형의 넓이 : {}".format((float(l_list[0])*float(l_list[1]))/2))
# print("사각형의 넓이 : {}".format((float(l_list[0])*float(l_list[1]))))

stu_data = ['홍길동', 100, 100, 100, 99]

# for s in stu_data:
#   print(s)

# 학생이름 : 홍길동
# 국어 : 100
# 영어 : 100
# 수학 : 100
# 과학 : 99
# 합계 :
# 평균 : 
total = stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4]
avg = total / 4

print("학생이름 : {}, 국어 : {}, 영어 : {}, 수학 : {}, 과학 : {}, 합계 : {}, 평균 : {}".format(stu_data[0], stu_data[1], stu_data[2], stu_data[3], stu_data[4], total, avg))

stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [[1, '유관순', 100, 100, 100, 99], [2, '이순신', 100, 99, 98, 99], [3, '김구', 80, 100, 90, 99]]
# 이순신의 평균 출력
# print("이순신의 평균 : {}".format((stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4]+stu_datas[1][5])/4))

# print("                  [ 학생성적 프로그램]")
# print("{}\t{}\t {}\t {}\t {}\t {}\t {}\t {}".format(stu_title[0], stu_title[1], stu_title[2], stu_title[3], stu_title[4], stu_title[5], stu_title[6],stu_title[7]))

# print("-"*60)

for s_t in stu_title: # stu_title 하나하나를 s_t 변수에 받는다.
  print("{}".format(s_t),end='\t') # end ' ' : 빈공백을 주면 띄어쓰기 (옆쪽으로) 출력된다. end = \n : 맨 끝 엔터키
print()
print("-"*60)

for s in stu_datas:
  print("{}\t{}\t {}\t {}\t {}\t {}\t {}\t {:.2f}".format(s[0], s[1], s[2], s[3], s[4], s[5], s[2]+s[3]+s[4]+s[5], (s[2]+s[3]+s[4]+s[5])/4))