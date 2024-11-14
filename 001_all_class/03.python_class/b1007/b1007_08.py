import random

# 25개 1차원 리스트
# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오
# for i in range(25):
#   if i < 5:
#     a_list.append(1)
#   else:
#     a_list.append(0)

a_list = [0] * 20 + [1] * 5
random.shuffle(a_list)

print(a_list)

# [5,5] 2차원 리스트에 a_list의 값을 입력한 후 출력하시오.
# b_list = []
# for i in range(5):
#   a = []
#   for j in range(5):
#      a.append(a_list[5*i+j])  # 0,1,2,3,....24 # a_list 5개를 리스트에 추가
#   b_list.append(a)   # a리스트를 b_list리스트에 추가
# print(b_list)

b_list = []
for i in range(0, len(a_list), 5):
  b_list.append(a_list[i:i+5])

while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*60)

  for i in range(5):
    print(i, end="\t")
    for j in range(5):
      print(b_list[i][j], end="\t")
    print()

  input1 = input("좌표를 입력하세요. [0,1] >")
  input2 = input1.split(",")
  print(b_list[int(input2[0])][int(input2[1])])