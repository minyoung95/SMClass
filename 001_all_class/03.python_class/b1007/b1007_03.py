numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# ## 100 이상의 값만 출력하시오.

for n in numbers: # numbers 리스트에 있는 모든 값을 하나하나씩 비교
  if n >= 100: # 그 값들 중 100 이상이면
    print(n) # 출력

numbers.sort() # 순차정렬 - 낮은 수 부터
numbers.sort(reverse=True) # 역순정렬 - 높은 수 부터
numbers.reverse() # 순서를 역순으로
print(numbers)