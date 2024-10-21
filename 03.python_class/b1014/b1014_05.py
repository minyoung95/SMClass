### 구구단을 출력하시오

def gugudan(n1,n2):
  for i in range(n1,n2+1):
    print("[ {} 단 ]".format(i))
    for j in range(1, 10):
      print(f"{i} * {j} = {i*j}")
  print("-"*60)

gugudan(2,5)

def gugudan(n):
  for i in range(2,n+1):
    print("[ {} 단 ]".format(i))
    for j in range(1, 10):
      print(f"{i} * {j} = {i*j}")

nArr = [9, 5, 7]

for i in nArr: # 9, 5, 7이 하나씩 i에 들어감
  gugudan(i)
  print("-"*50)

subName = ["국어", "영어", "수학"]
score = {"국어":100, "영어":90, "수학":90}

# print(f"{subName[0]} : {score[subName[0]]}")
# print(f"{subName[1]} : {score[subName[1]]}")
# print(f"{subName[2]} : {score[subName[2]]}")

for i in subName:
  print(i,":",score[i])

# for k,v in score.item():
#   print(k,":",v)