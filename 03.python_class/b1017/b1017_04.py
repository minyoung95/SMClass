list1 = [52,273,32,72,100]

try:
  n_input = int(input("리스트의 순번을 입력하세요."))
  print(f"{n_input}번째 리스트의 값은 {list1[n_input]}")
# except Exception as e: # Exception : 모든 오류를 알려줌
#   print("모든 예외처리의 부모") 맨위에서 처리하면 밑의 except 처리는 적용 안된다. 마지막에 위치해야함
except ValueError as e: # 벨류에러일때 적용
  print("값을 잘못 입력하셨습니다..",type(e),e)
except IndexError as e: # 인덱스에러일때 적용
  print("숫자가 범위 밖입니다.",type(e),e)
except Exception as e: # Exception : 모든 오류를 알려줌 , as e : 예외에 대한 설명문, type(e) : 예외객체
  print("모든 예외처리의 부모")

 # IndexError : 리스트의 범위 밖을 호출했을 때 에러
 # ValueError : 입력된 값의 변환 에러

print("1")
print("2")
try:
  print("3")
  print("4")
  raise NotImplementedError("프로그램을 구현해야 함.") # 프로그램이 구현되어 있지 않음 (raise : 강제 에러 유발) e로 전달
  print(3/0)
  print("5")

except Exception as e:
  print(e)
  print("6")
  print("7")

finally:
  print("8")
  print("9")

print("10")
print("프로그램을 종료합니다.")