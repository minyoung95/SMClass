## 2차원 리스트

a_list = [1,2,3,4,5,6,7,8,9]
b_list = []
for i in range(9):
   b = []
   if i//3==0:
      b_list.append(i)
print(b_list)

# for문을 2번 작성해서 1,25까지 [5,5] 리스트 생성하시오.
a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(5*i+(j+1))
  a_list.append(a)
print(a_list)

a_list = [] #a_list[0],a_list[1],....
for i in range(9):
  a_list.append(i+1)
b_list = []
for i in range(9):
  b = []