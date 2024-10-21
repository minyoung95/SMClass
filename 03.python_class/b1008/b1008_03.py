# 25개 1차원 리스트 (1, 25까지) 입력한 후 랜덤으로 출력
# [5,5] 2차원 리스트 입력 후 출력
import random

aArr = []
for i in range(25):
  aArr.append(i+1)

random.shuffle(aArr) # 섞기
print(aArr)

## 2차원 리스트 만들기
a_list = []

for i in range(5):
  a = []
  for j in range(5):
    a.append(aArr[5*i + j]) # aArr 리스트를 01234 56789 1011121314 1516171819 2021222324 형식으로
  a_list.append(a)

print(a_list)

## 2차원 리스트를 5,5로 만들기
while True:
  print("\t0\t1\t2\t3\t4") # 위쪽 상단메뉴? 
  print("-"*60)
  for i in range(5):
    print(i,"|",end= "\t") # 왼쪽 메뉴
    for j in range(5):
      print(a_list[i][j], end="\t")
    print()

## 값을 입력하면 좌표가 나오게
  input1 = int(input("값을 입력하세요."))
  if input1 < 0 or input1 > 26:
    print("1에서 25사이의 값만 입력하세요.")
    continue

  for i in range(5):
    for j in range(5):
      if a_list[i][j] == input1:
        print(f"좌표 값 : {i,j}")
        a_list[i][j] = 0 # 값을 0으로 바꾸기
        break
  

## 좌표를 입력하면 값이 나오게
  # input1 = input("좌표를 입력하세요. (0,0) >>")
  # input2 = input1.split(".")
  # print("좌표 값 : ",a_list[int(input2[0])][int(input2[1])])
  