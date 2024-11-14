aArr = [1, 2, 3, 4, 5]
# a_list = [1, 4, 9, 16, 25]

# # 리스트 내포

a_list = [i*i for i in aArr]

print(a_list)

# ### 1-20 중에 3의 배수만 리스트에 추가하시오.
a_list = []

for i in range(20):
  if i % 3 == 0:
    a_list.append(i)
print(a_list)

# ### 리스트 내포 [값 for문 조건식]
b_list = [i for i in range(20) if i % 3 == 0]
print(b_list)

### 글자 찾는법
ss = "파이썬 수업 중 타입 문자열, 정수형, 실수형, 논리형 타입이 있습니다."
i_str = input("글자를 입력하세요.")
if i_str in ss:
  print("있습니다.")
else:
  print("없습니다.")
# 위치값 찾는법 - find() // index() : 없을땐 에러남
idx = ss.find(i_str)
print("위치값 : ",idx)

# 글자 갯수 검색 - count()
idx1 = ss.count(i_str)
print("갯수 : ", idx1)

print("-"*60)

a_list = []
idx2 = 0
search = input("검색 단어 입력")
for i in range(ss.count(i_str)):
  num = ss.find(search,idx2)
  a_list.append(num)
  idx2 = num+1

print(f"검색개수 : {len(a_list)}, 위치값 : {a_list}")

# replace("x","y") : x를 y로 바꿔준다
sss = ss.replace(" ","")
print(sss)

# "x".join(y) : y글자 사이사이에 x를 넣어준다.
a_str = "파이썬"
a = "-".join(a_str)

print(a_str)