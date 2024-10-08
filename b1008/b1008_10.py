### 튜플 : 리스트타입과 같음, 순서가 있음

t = (1, 2, 3, 4)
print(type(t))
print(t)
print(t[0])

# t[0] = 100 : 튜플은 수정 불가
# t.append(100) : 추가 불가
print(len(t))

for i in t:
  print(i)

t = t + (3, 5) # 더하기 연산자로 추가 가능
print(t)
tt = (1, 2, 3)
tArr = tt * 2
print(tArr)

### 리스트 벗기기
aArr = [[1, 2], [[1, 2,], [3, 4]], [5, 6], [7, 8]]
a_list = [1, 2, 1, 2, 3, 4, 5, 6, 7, 8]

b_list = []
for i in aArr:
  if type(i) == list:
    for j in i:
      if type(j) == list:
        for k in j:
          b_list.append(k)
      else:
        b_list.append(j)    
print(b_list)

### 두 수의 치환
a = '우유'
b = '커피'
c = ''
print(a, b)
# 기본적인 a, b 치환
c = a; a = b; b = c
print(a, b)
# 파이썬 a, b 치환
a, b = b, a
print(a, b)

### 문자열을 tuple 타입으로 변경 >> 한 글자씩 잘림
a_str = 'abcde'
print(a_str)
print(a_str[1])

a_tu = tuple(a_str)
list(a_tu)
print(list(a_tu))

a = ((1, 2), (3, 4), (5, 6))
print(a[0][1])