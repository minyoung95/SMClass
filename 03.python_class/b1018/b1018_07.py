class Student:
  def __init__(self,name,kor,eng,math):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

  ## == 식이 있는 곳에 호출되는 함수 : __eq__
  def __eq__(self, value): # self : 현재 자신의 객체, value : 비교 할 다른 객체
    return self.total == value.total
  ## != 식이 있는 곳에 호출되는 함수 : __ne__ 
  def __ne__(self, value): 
    return self.total != value.total
  ## > 식이 있는 곳에 호출되는 함수 : __gt__
  def __gt__(self, value): 
    return self.total > value.total
  ## >= 식이 있는 곳에 호출되는 함수 : __ge__
  def __ge__(self, value): 
    return self.total >= value.total
  ## < 식이 있는 곳에 호출되는 함수 : __lt__
  def __lt__(self, value): 
    return self.total < value.total
  ## <= 식이 있는 곳에 호출되는 함수 : __le__
  def __le__(self, value): 
    return self.total <= value.total
  

s1 = Student("홍길동",100,100,90) # 290
s2 = Student("유관순",90,100,95) # 285

if (s1!=s2): ## s1:self, s2:value
  print("객체 비교 : 참입니다.")
else:
  print("객체 비교 : 거짓입니다.")
# s1 = Student("홍길동",100,100,90)
# print(s1)

# print(s1.print())
# students.append(s1.print())
# s2 = Student("유관순",90,90,80)
# print(s2.print())
# students.append(s2.print())
# print("-"*60)
# print(students)


# s1 = Student("홍길동",100,100,90) # 객체선언
# print(s1.name)
# print("s1.count : ",s1.count)
# s2 = Student("유관순",90,90,80)
# print(s2.name)
# print("s2.count : ",s2.count) # 변수가 2로 증가
# print("s1.count : ",s1.count) # 동일한 변수를 사용하기 때문에 2로 증가

