class Circle:
  def __init__(self,length):
    self.__length = length
  
  ## getter, setter
  def get_length(self):
    return self.__length
  
  def set_length(self,length):
    self.__length = length

  ## 원의 넓이
  def get_area(self):
    return 3.14*(self.__length**2)
  
  def get_circum(self):
    return 2*3.14*self.__length

  ## 참조 변수를 출력할때 리턴되는 함수 : __str__()
  def __str__(self):
    c_str = "원의 반지름 : {}, 원의 넓이 : {}, 원의 둘레 : {}".format(self.__length,self.get_area(),self.get_circum())
    return c_str

### _, __ 내부적으로 캡슐화 하겠다 선언
# c1 = Circle(10)           # 값을 입력 10
# print(c1.get_length())    # getter 값출력 10
# c1.set_length(200)        # setter 값입력 200
# print(c1.get_length())    # getter 값출력 200
# c1.__length = 100           # 변수 직접입력 100
# print(c1.__length)          # 변수 직접출력 100
# print(c1.get_length())    # getter 값출력 200 // 직접입력이 적용이 안된다. (캡슐화)

c1 = Circle(10)
print(c1)

### no getter를 사용하지 않으면 접근불가

def get_no(self): # 출력
  return self.__no 
def set_no(self,no): # 입력
  if no < 0 : raise "0 이하는 입력 할 수 없음" # 에러를 발생시켜서 0이하 입력 못하게함
  self.__no = no

# s1 = Student()
# s1.set_no(100)
# print(s1.get_no())

#-------------------------------------