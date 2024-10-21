### [4, 5] 2차원 리스트

a_list = []

for i in range(4):
  a = []
  for j in range(5):
    a.append(15*i +(j*3))
   # a.append(j+1) : [12345] [12345] [12345] [12345]
   # a.append(5*i + (j+1)) : [12345] [678910] [1112131415] [1617181920]
  a_list.append(a)


for i in range(4):
  for j in range(5):
    print(a_list[i][j], end="\t")
  print()

### 0, 3, 6, 9 ... 57 1차원
aArr = []

for i in range(20):
  aArr.append(i*3)

print(aArr)

### 2차원 [4, 5]

a_list = []

for i in range(4):
  a = []
  for j in range(5):
    a.append(aArr[5*i + j])
  a_list.append(a)

print(a_list)