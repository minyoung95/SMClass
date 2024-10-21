### 절차적인 형태의 프로그램 구현
### 반지름을 입력받아, 원의 둘레와 넓이를 출력

# r = int(input("반지름을 입력하세요"))

# print("원의 둘레 : ",2*3.14*r)
# print("원의 넓이 : ",3.14*(r**2))

# 클래스 생성
class Circle:
  def __init__(self,r):
    self.__r = r # 변수에 접근제한 걸기 (__변수) - 캡슐화

  # 원의 넓이
  def get_area(self):
    return 3.14*(self.__r**2)
  
  def get_circum(self):
    return 2*3.14*self.__r


# 클래스 선언
c1 = Circle(int(input("반지름을 입력하세요.")))
c1.r = 7
print("넓이 : ",c1.get_area())
print("둘레 : ",c1.get_circum())