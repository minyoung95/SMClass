# a = 1
# b = 2

# a_list = [a,b]
# print(a_list)

# print(type(a_list))

# a_tuple = (a,b)
# print(type(a_tuple))

# b_tuple = (a)   # 타입 : int
# print(type(b_tuple))

# b_tuple = (a,)   # 타입 : tuple >> 변수 한개일때 ,를 붙여줘야 tuple이 된다.
# print(type(b_tuple))

# select * from employees where emp_name like '%a%'

# name = '홍길동'
# a = '안녕하세요. 이름은 %s'%name
# print(a)

# print("hello. my name is {}".format(name))

title = ['e_id','e_name','salary']
a = [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]
aa= []
for ad in a:
    aa.append(dict(zip(title,ad)))
    
print(aa)
    
