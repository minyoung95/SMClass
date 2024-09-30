a = [1, 2, 3, 4, 5] # 값이 여러 개일 경우 a01이라는 주소값 공간에 저장된다.
b = a # a의 값들을 복사하는게 아님, 주소값(a01)을 가져온다. b의 값을 바꾸게되면 a01도 바뀌게 되기 때문에 a의 값도 바뀐다.

print(a) # [1, 2, 3, 4, 5]

b[0] = 100

print(a) # [100, 2, 3, 4, 5] // b[0]을 바꾸면 a[0]도 바뀐다.