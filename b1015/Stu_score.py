# import S_func # import : 모듈(함수의 모음?)을 가져옴
from S_func import *


# 학생성적프로그램
while True:
  choice = title_program() # 함수호출 (메뉴 출력)

  if choice == "1":
    stuNo = stu_input(stuNo) # 함수호출 (학생성적 입력)

  elif choice == "2":
    stu_output() # 함수호출 (학생성적 출력)
    
  elif choice == "3":
    stu_update() # 함수호출 (학생성적 수정)

  elif choice == "4":
    stu_select() # 함수호출 (학생성적 검색)

  elif choice == "5":
    stu_delete() # 함수호출 (학생성적 삭제)

  elif choice == "6":
    stu_rank() # 함수호출 (등수처리)
    
  elif choice == "7":
    stu_sort() # 함수호출 (학생성적 정렬)

  elif choice == "0":
    print("[ 0. 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break