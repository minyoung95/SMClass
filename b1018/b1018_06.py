class Student:
  count = 0 # 클래스 변수 = 모든 객체가 동일한 변수를 사용
  students = []
  # 클래스 함수 선언
  @classmethod # 클래스 함수 표시
  def stu_print(cls):
    print(*s_title,sep='\t')
    print("-"*80)    
    for s in cls.students:
      print(str(s))
    print()


  def __init__(self,name,kor,eng,math):
    # self.no = no # 인스턴스 변수 - 객체 선언을 할 경우 변수는 개별적으로 생성
    Student.count += 1
    self.no = Student.count # 클래스이름.변수 : 공용 변수
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

    ## 클래스 리스트 students에 추가
    Student.students.append(self)


  # 객체를 문자열로 반환 - 리턴 : 문자열로 되어야한다.
  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"
  
  def print(self):
    return {'no':self.no,'name':self.name,\
            'kor':self.kor,'eng':self.eng,'math':self.math,\
            'total':self.total,'avg':self.avg,'rank':self.rank}
  

s_t = ['no','name','kor','eng','math','total','avg','rank']  
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

while True:
  print("[ 학생성적 프로그램]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 홍길동, 유관순 비교")
  choice = int(input("원하는 번호를 입력하세요. >>"))

  if choice == 1:
    print("[ 학생성적 입력 ]")
    name = input("이름을 입력하세요.")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]} 점수를 입력하세요.")))
    Student(name,*score) #*score (전개연산자) : score[0], score[1], score[2]

    # 클래스 변수 접근 방법 : 클래스명.변수명
    for s in Student.students:
      print(s)

  elif choice == 2:
    print("[ 학생성적 출력 ]")
    Student.stu_print()
    # 클래스 함수 : 클래스명.함수명
  
  elif choice == 3:
    s1 = Student("홍길동",100,100,90)
    s2 = Student("유관순",90,90,80)

    ## 홍길동과 유관순 합계를 비교