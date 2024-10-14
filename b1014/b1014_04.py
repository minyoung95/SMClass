num1 = int(input("숫자1를 입력하세요"))
num2 = int(input("숫자2를 입력하세요"))
op = input("+, -, *, / 중 하나를 선택하세요.")


def carl(num1,num2,op):
  # result = 0
  if op == "+":
    result = num1+num2
  elif op == "-":
    result = num1-num2
  elif op == "*":
    result = num1*num2
  elif op == "/":
    result = num1/num2
  
  return result
  
print(carl(num1,num2,op))