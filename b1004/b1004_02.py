import random

r_num = random.randint(1,100) # 1부터 100까지 한가지 숫자(정수)를 랜덤으로 뽑아준다.
count = 0

# 10번 도전에서 입력한 숫자가 더 크면 작은 수를 입력하셔야 합니다.
# 10번 도전에서 입력한 숫자가 더 작으면 큰 수를 입력하셔야 합니다.
# 10번 도전에서 맞추지 못하면, 10번 도전에 실패했습니다. 랜덤숫자 : x
# 10번 도전에서 맞추면, 도전에 성공했습니다. 랜덤숫자 : x

for i in range(10): # 조건식

  input_num = int(input(f"{i+1}번 째 숫자 입력"))
  #비교
  if r_num < input_num:
    print("입력한 숫자가 큽니다.")
  elif r_num > input_num:
    print("입력한 숫자가 작습니다.")
  else:
    print(f"성공 랜덤숫자 : {r_num}")
    count = 1
    break
  
  # 10번 도전 실패
if count == 0:
  print("10번 도전 실패")

# #### while
# r_num = random.randint(1,100)

# i = 0 # 반복되는 변수
# count = 0 # 확인하는 변수

# while (i < 10): # 조건식
#   input_num = int(input(f"{i+1}번 째 숫자를 입력하세요."))

#   if r_num < input_num
#     print()