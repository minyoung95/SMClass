stu_datas = []
no = 1
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

while True:
  print("[ 학생성적 프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요. (종료 : 0)")

###########
  if choice == "1":
    print("[ 학생성적 입력 ]")
    print()
    while True:
      name = input("이름을 입력하세요. (상위메뉴로 이동 : 0)")
      if name == "0":
        print("메뉴화면으로 이동합니다.")
        break
      kor = int(input("국어점수를 입력하세요"))
      eng = int(input("영어점수를 입력하세요"))
      math = int(input("수학점수를 입력하세요"))
      total = kor+eng+math
      avg = (kor+eng+math)/3
      rank = 0
      print(f"번호 : {no}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {total}, 평균 : {avg:.2f}")

      s = [no, name, kor, eng, math, total, avg, rank] # s: list타입
      stu_datas.append(s)

      no += 1
      
###########
  elif choice == "2":
    print("[ 학생성적 출력 ]")
    # 출력

    for s in s_title:
      print(s, end="\t")
    print(); print("-"*60)

    # 학생성적 출력
    for s in stu_datas:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
      print()

###########     
  elif choice == "3":
    print("[ 학생성적 수정 ]")
    print()
    name = input("수정하고자 하는 학생이름을 입력하세요. : ")
    #stu_datas에서 검색
    count = 0
    for s in stu_datas:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print("[ 과목선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("0. 성적수정 취소")
        choice = input("원하는 번호를 입력하세요. >>")

        if choice == "1":
          print("현재 국어점수는 : ", s[2])
          s[2] = int(input("국어점수 변경 : "))
        elif choice == "2":
          print("현재 영어점수는 : ", s[3])
          s[3] = int(input("영어점수 변경 : "))
        elif choice == "3":
          print("현재 수학점수는 : ", s[4])
          s[4] = int(input("수학점수 변경 : "))
        elif choice == "0":
          print("성적 수정을 취소합니다.")
          count = 1

        if choice != "0":
          s[5] = s[2] + s[3] + s[4] # 합계변경
          s[6] = s[5] / 3           # 평균변경
          print(f"{name} 학생의 성적이 수정되었습니다.")
          count = 1
      #없을경우
    if count == 0:
      print("수정하고자 하는 학생이름이 없습니다.")
      print()

###########
  elif choice == "4":
    print("[ 학생성적 검색 ]")
    print()

    name = input("찾고자 하는 학생이름을 입력하세요. : ")
    #stu_datas에서 검색
    count = 0
    for s in stu_datas:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.") # 번호나 성적으로 출력하는것도 해보기
        #찾은 학생의 데이터를 출력

        for st in s_title:
          print(st, end="\t")
        print(); print("-"*60)

        # 학생성적 출력
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print()
        count = 1
        break
    if(count == 0):
      print("찾고자 하는 학생이름이 없습니다.")
      print()

###########
  elif choice == "5":
    print("[ 학생성적 삭제 ]")
    print()

###########
  elif choice == "6":
    print("[ 등수처리 ]")
    print()
    
###########
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
# 이름, 국어, 영어, 수학 입력-> 번호, 이름, 국어, 영어, 수학, 합계, 평균 출력
# 0을 입력시 프로그램 종료

# no = 1
# while True:
#   name = input("이름을 입력하세요. (종료 : 0)")
#   if name == "0":
#     break
#   kor = int(input("국어점수를 입력하세요"))
#   eng = int(input("영어점수를 입력하세요"))
#   math = int(input("수학점수를 입력하세요"))
#   total = kor+eng+math
#   avg = (kor+eng+math)/3
#   print(f"번호 : {no}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {total}, 평균 : {avg:.2f}")

#   s = [no, name, kor, eng, math, total, avg] # s: list타입
#   stu_datas.append(s)

#   no += 1

# print("프로그램을 종료합니다.")
# print(stu_datas)