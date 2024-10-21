import random

## 1, 25 사이의 랜덤숫자를 생성하여 출력하시오.

num = int(random.random()*25)+1
num = random.randint(1, 25)

## 1, 25 사이의 리스트를 중복없이 만들기

a_list = []
while len(a_list)<25: # 리스트길이가 25가 될때까지
  for i in range(25): # 25번 반복
    num = random.randint(1, 25)
    if num not in a_list: # 리스트에 랜덤숫자가 없으면
        a_list.append(num) # 추가해라
  print(a_list)

###########################################

a_list = []
for i in range(25):
  a_list.append(i+1)

# 1-25까지 랜덤으로 배치 - random.choices()
# 범위 리스트, 25개 추출 (중복 o)
b_list = random.choices(a_list, k=25)

# 1-25까지 랜덤으로 배치 - random.sample()
# 범위 리스트, 25개 추출 (중복 x)
c_list = random.sample(a_list, 25)

print(b_list)
print(c_list)