import random

# 1-25까지 랜덤의 숫자 25개를 중복없이 추출
# [5,5] 2차원 리스트에 입력해서 출력

a_list = []
for i in range(25):
  a_list.append(i+1)

b_list = random.sample(a_list, 25) # random.shuffle(a_list) # a_list의 값들을 섞음

print(b_list)

c_list = []
for i in range(0, len(b_list), 5): # for i in range(0, len(a_list), 5):
  c_list.append(b_list[i:i+5])

print(c_list)

#c_list 를 랜덤으로 섞어서 1-25까지 [5,5] 2차원 리스트

while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*60)

  for i in range(5):
    print(i,end="\t")
    for j in range(5):
      print(c_list[i][j],end="\t")
    print()
  input1 = input("좌표를 입력하세요. [0,1] >>")
  input2 = input1.split(",") # 배열의 형태로 나눠준다 : ['0', '1']
  print(f"{input1} 좌표의 값 : ",c_list[int(input2[0])][int(input2[1])])

  

## print(c_list)

# while len(a_list) < 25:
#   num = random.randint(1, 25)
#   if num not in a_list:
#     a_list.append(num)
