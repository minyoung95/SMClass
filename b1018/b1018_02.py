#### Class 생성방법

## 학생 1명 정보
# 번호,이름,국어,영어,수학,합계,평균,등수
# 학생클래스 설계도(구조) 생성
class Student:
  # 기본 생성자
  # def __init__(self):
  #   None

  def __init__(self,no,name,kor,eng,math):
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
  def print(self):
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank))
  
#### Class 사용방법
# class 선언(class 복사)
s1 = Student(1,"홍길동",100,100,100) # students[0]
# print(s1) : s1의 주소값이 나옴
s1.print()

# # 클래스명.변수명 = 값 : 변수가 생성되어 클래스에 변수가 저장된다.
# 기본 생성자 사용해서 값을 개별적으로 입력
# s1 = Student()
# s1.no = 1
# s1.name = "홍길동"
# s1.kor = 100
# s1.eng = 100
# s1.math = 100

# #클래스 내 변수출력
# print(s1.no)
# print(s1.name)
# s2 = Student() # 다른공간
# s2.no = 2
# s2.name = "유관순"
# s2.kor = 100
# s2.eng = 100
# s2.math = 100
  

# ## 전체 학생 리스트 정보
# class Students:
#   pass