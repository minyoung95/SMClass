### 클래스 생성 후 데이터를 직접 받아, 클래스 선언 후 저장
### 번호- 자동부여, 이름,국어,영어,수학,합계,평균,등수
### 클래스 전체 출력, 클래스 수정

class Student:
  count = 0
  students = []

  @classmethod
  def output(cls):
    print(*s_title,sep='\t')
    print("-"*60)
    for i in cls.students:
      print(str(i))


  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    
    Student.students.append(self)

  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}\t"

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  choice = int(input("원하는 번호를 입력하세요."))

  if choice == 1:
    print("[ 학생성적 입력 ]")
    print()

    name = input("이름을 입력하세요.")
    score = []
    for i in range(2, 5):
      score.append(int(input(f"{s_title[i]}점수를 입력하세요.")))
    Student(name,*score)

    for s in Student.students:
      print(s)
  
  elif choice == 2:
    print("[ 학생성적 출력 ]")
    print()

    Student.output()
  
  elif choice == 3:
    print("[ 학생성적 수정 ]")
    print()

    flag = 0
    name1 = input("수정하고자 하는 학생 이름을 입력하세요.")
    for s in Student.students:
      if s.name == name1 : # s.name : 참조변수.변수명 (클래스 출력할때) // s[0] 리스트 // s['name'] 딕셔너리
        print(f"{name1} 학생을 찾았습니다.")
        print("1. 국어과목 수정")
        print("2. 영어과목 수정")
        print("3. 수학과목 수정")
        choice = int(input("원하는 과목을 선택하세요."))

        if choice == 1:
          print("현재 국어 점수",s.kor)
          s.kor = int(input("변경 국어 점수 : "))
        elif choice == 2:
          print("현재 영어 점수",s.eng)
          s.kor = int(input("변경 영어 점수 : "))
        elif choice == 3:
          print("현재 수학 점수",s.math)
          s.kor = int(input("변경 수학 점수 : "))

        s.total = s.kor+s.eng+s.math
        s.avg = s.total/3

        print(f"{name1} 학생의 성적이 수정되었습니다.")
        flag = 1
      
    if flag == 0:
      print("학생 정보를 찾지 못하였습니다. 다시 입력해주세요.")
      print()

        



