# 1차원 리스트 25개
a_list = []
for i in range(25):
  a_list.append(i+1)
print(a_list)

## 1차원 리스트 -> 2차원 리스트
b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(5*i + (j+1))
  b_list.append(a)

print(b_list)

## (0,25,5) 0~25까지 5씩 증가
b_list = []
for i in range(0, len(a_list), 5):
  b_list.append(a_list[i:i+5]) # 0:5 5:10 10:15 ...

print(b_list)