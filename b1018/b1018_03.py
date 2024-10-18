### 클래스 생성
class Car:
  def __init__(self,color,speed,tire,gear):
    self.color = color
    self.__speed = speed
    self.tire = tire
    self.gear = gear

  def upSpeed(self,value):
    if value > 0: self.__speed += value
    else: raise "값을 잘못 넣었습니다." # raise : 에러메세지 띄우기

  def downSpeed(self,value):
    self.__speed -= value


### 클래스를 사용하려면 클래스 선언을 해야함

c1 = Car("흰색",4,"auto",0)
c1.color = "블루"
print(c1.color)
c1.speed = 300
print(c1.speed)

c2 = Car("흰색",4,"auto",0) # 다른공간
c2.color = "빨강"
print(c2.color)
print(c1.color) # c2를 바꿔도 c1에 적용되지않음

## 속도 0 > 100
c1.upSpeed(100)
print(c1.speed)
