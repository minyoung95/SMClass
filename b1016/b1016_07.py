# while True:
#   score = 100
#   print("[나눗셈 프로그램]")
#   nstr = input("숫자만 입력가능 >>")

#   ### try except: 프로그램 에러 처리
#   try:
#     num = int(nstr)
#     print("입력된 숫자로 100을 나눔 : ",score/num) # 에러가 발생할 가능성이 있는 코드 (숫자가 아닌것을 입력, 0을 입력하면 에러)
#   except:
#     print("숫자로 변환 안됨") # 에러가 발생했을때 실행할 코드

try:
  print("입력된 숫자 : ",int(input("숫자를 입력하세요. >")))
except:
  pass