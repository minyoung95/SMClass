### [ 문제 ]
### 학생성적입력 : 클래스의 참조변수를 입력해서 출력
### 클래스 1개가 생성, 클래스의 참조변수(__str__) 출력


### 클래스 만들 떄
### 1. 생성자 만들기 > 2. 객체 선언 (s1 = Student() // 참조변수 = 클래스명)

class Student:
  student = []
  count = 0

  @classmethod
  def stu_print(cls):
    for s in cls.student:
      print(str(s))

  ## __ __ : 클래스 내에서 사용가능한 특별 함수 (__init__, __str__, 비교함수)
  def __init__(self,name,kor,eng,math): # 입력받을 변수를 괄호안에 입력
    Student.count += 1
    self.no = Student.count
    self.name = name # 인스턴스 변수(객체 선언할때 만들어짐, 객체마다 변수가 다름) = 입력받은 변수 (self를 붙여야 클래스에 적용)
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

    Student.student.append(self) # 클래스 변수 student에 추가

  def __str__(self): # 참조변수를 출력해서 원하는 데이터를 출력할 때 사용 print
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}" # 리턴값은 문자열이여야 함

  def print(self):
    return {'no':self.no,'name':self.name,'kor':self.kor,'eng':self.eng,'math':self.math,'total':self.total,'avg':self.avg,'rank':self.rank}


s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  choice = int(input("원하는 번호를 입력"))

  if choice == 1:
    print("[ 학생성적 입력 ]")

    name = input("이름을 입력하세요.")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]} 점수를 입력하세요.")))
    Student(name,*score)

    # print(Student.student[0]) : 학생 1개의 정보만 출력 >> 여러개 출력 (for문)
    for s in Student.student:
      print(s) ## 참조변수를 출력?

  elif choice == 2:
    print("[ 학생성적 출력 ]")
    Student.stu_print()