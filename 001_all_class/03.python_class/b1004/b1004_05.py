### 구구단 입력한 단까지을 출력하시오.
### 3 > 1,2,3단

a = int(input("숫자를 입력하세요."))

for i in range(2, a+1):
  print(f"[{i}단]")
  for j in range(1, 9+1):
    print(f"{i} * {j} = {i * j}")

### 000 ~ 999 까지 출력

for k in range(0, 9+1):
  for l in range(0, 9+1):
    for m in range(0, 9+1):
      print(f"{k}{l}{m}")

# for n in range(1000):
#   print(f"{n:03d}")


for p in range(2, 9+1):
  print(f"[{p} 단]", end="\t\t")
print() # 한칸 내리기
for n in range(1, 9+1):
  for o in range(2, 9+1):
    print(f"{o} * {n} = {o*n}", end="\t")
  print()