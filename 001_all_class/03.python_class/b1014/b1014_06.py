import random
tName = ["이름", "국어", "영어", "수학", "합계"]
fName = ["바나나", "오렌지", "체리", "파인애플", "코코넛"] 
# fName = list(fruit.keys())
fruit = {
  "바나나":"banana", 
  "오렌지":"orange", 
  "체리":"cherry", 
  "파인애플":"pineapple", 
  "코코넛":"coconut"
  }

## 바나나를 입력하면 영어로 banana로 나오게

print(fruit["바나나"]) # 키를 입력하면 밸류값이 나오는 것을 이용

search = input("과일이름을 입력하세요.")
if search in fruit:
  print("영문으로 : ",fruit[search])
else:
  print("찾는 단어가 없습니다.")

### 순서대로 영문퀴즈

print("[ 영단어 맞추기 ]")
for key in fruit.keys(): # 키값만 뽑아오기
  search = input(f"{key}의 영문을 입력하세요.")
  if fruit[key] == search:
    print("정답입니다.",fruit[key],search)
  else:
    print("오답입니다.",fruit[key],search)

### fName의 랜덤순서로 영문퀴즈

random.shuffle(tName) # 원본이 변경이 된다.
print(tName)

re_fName = random.sample(fName,5) # 중복없이 섞기
for i in re_fName:
  search = input(f"{i}의 영문을 입력하세요.")
  if fruit[i] == search:
    print("정답입니다.",fruit[i],search)
  else:
    print("오답입니다.",fruit[i],search)