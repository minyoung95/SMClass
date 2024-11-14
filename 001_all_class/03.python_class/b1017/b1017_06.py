a = ['19', 'ukubyszeki', '90', '52', '77', '219', '73', '1']
b = ['18', '76', '59', '77', '212', '70.6666666667', '1']
t_title = ['no','name','kor','eng','math','total','avg','rank']
c = []
students = []

def t_float(n): # isdigit
  try:
    int(n)
    return True
  except:
    return False

# 문자열인지 아닌지
for idx,i in enumerate(a):
  if i.isdigit(): # isdigit : 정수면 True, 아니면 False
    print(f"{idx}번째 {i}는 숫자입니다.")
  else:
    print(f"{idx}번째 {i}는 문자입니다.")

# 정수로 변경
for i in b:
  if t_float(i):
    i = int(i)
  else:
    i = float(i)
  c.append(i)

print(c)

students.append(dict(zip(t_title,c)))

print(students)

