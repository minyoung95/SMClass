# 10은 2의 배수입니다.
print("%d은 %d의 배수입니다." % (10, 2))
a = 10
b = 2

# 출력 자리수
# print("%d" % b)
# print("%5d" % b) # 띄어쓰기 5칸
# print("%05d" % b) # 다섯자리

# num = 1
# num2 = 10
# num3 = 100

# print("%03d" % num)
# print("%03d" % num2)
# print("%.2f" % num3)
# print("%03d %03d %.2f" % (num, num2, num3))

# print("%5d" % (-10))

print("%.2f" % 758.12345678)
print("%013.2f"% 25.05)
num = 150.15
print("%d" % num)
print("%f" % num)
print("%s" % num)

print("*"*10)

# 10*2 = 20
# print("%d * %d = %d" % (a,b,a*b))

# 사용표시
# %s : 문자열, %c : 문자 1개, %f : 실수(.2 : 소숫점 둘째자리까지), %d : 정수
# 홍길동 총합 : 299, 평균 : 99.33333
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# print("%s 총합 : %d, 평균 : %.2f" % (name, kor+eng+math, (kor+eng+math)/3))


# #### print 사용형태
# print(a,b)
# # print(a + "은 " + b + "의 배수입니다.") 타입이 다르면 + 안댐
# print(a,"은 ",b,"의 배수입니다.") # 쉼표(,)
# print("%d은 %d의 배수입니다." % (a,b)) # %
# print("{}은 {}의 배수입니다.".format(a,b)) # format
# print(f"{a}은 {b}의 배수입니다.") # f