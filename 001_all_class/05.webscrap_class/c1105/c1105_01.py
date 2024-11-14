import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

# ## 함수선언 (기본매개변수)
# def func(num1,num2):
#     print(num1)
#     print(num2)
    
# ## 함수호출
# func(10,20)
# ## 함수의 매개변수 개수를 정확히 맞춰야 에러 x // ex) func(10), func(10,20,30)

## 함수선언 (가변매개변수)
def func(*num):
    print(num) # tuple 타입
    print(len(num))
    
## 함수호출
func(10)
func(10,20)
func(10,20,30)