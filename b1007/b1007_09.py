import random
lotto = [0]*6 + [1]*3
random.shuffle(lotto)
a_list = [
  [0,1,0],
  [1,0,0],
  [0,0,1]
]

for i in range(3):
  for j in range(3):
    a_list[i][j] = lotto[3*i+j]

aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

while True: # 실행을 한번 시켜도 꺼지지 않게
  money = int(input("얼마를 투자하시겠습니까?"))

  print("         [i,j 좌표]")
  print("\t0\t1\t2\t")
  print("-"*25)
  for i in range(3):
    print(i,"|", end= "\t")
    for j in range(3):
      print(aa_list[i][j], end= "\t") # end ="\t" : 옆쪽으로
    print() # j가 3번이 돈 후에 엔터키(\n)
  
  code = input("좌표를 입력하세요. (0.0) >> ")
  cArr = code.split(".") # code에 input 된 값을 나눠서 배열형태로 만듬
# print(a_list[int(cArr[0])][int(cArr[1])]) # 배열형태로 만든 값들을 a_list의 i,j값에 넣어줌
  if a_list[int(cArr[0])][int(cArr[1])] == 1:
    aa_list[int(cArr[0])][int(cArr[1])] = "당첨"
    print(f"{cArr} 당첨금 : {money*10:,d}")
  else:
    aa_list[int(cArr[0])][int(cArr[1])] = "꽝"
    print(f"{cArr} 다음기회에 : {money}")