### 파일에서 불러와서 읽기

# students = [
#   {1,"홍길동",100,100,90,290,96.67,0},
#   {2,"유관순",90,90,80,260,86.67,0},
#   {3,"이순신",80,80,70,230,76.67,0}
# ]

stu_key = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]
students = []

## 리스트 두개를 합친 후 딕셔너리 타입으로 바꾸기
# a = ["홍길동", "유관순", "이순신"]
# b = [100,90,80]

# c = zip(a,b)
# print(dict(c))

## 파일 읽기 (r)
f = open('a.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  s = line.strip().split(",")
  # for i,v in enumerate(s):
  #   if i == 1: continue
  #   elif i == 6: v[6] = float(v[6])
  #   else: v[i] = int(v[i])
  s[0] = int(s[0])
  s[2] = int(s[2])
  s[3] = int(s[3])
  s[4] = int(s[4])
  s[5] = int(s[5])
  s[6] = float(s[6])
  s[7] = int(s[7])
  students.append(dict(zip(stu_key,s)))
  print(line.strip()) # strip : \n을 없애줌

f.close()

print(students)