stu_datas = []
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
choice = 0
stuNo = 0 # 학생번호
stuNo = len(stu_datas)
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0 # 성적처리에 필요한 변수
count = 1 # 등수
check = 0 # 체크변수

while True:
  print("[ 학생성적 프로그램 ]")
  print("-"*60)
  print("[ 1. 학생성적 입력 ]")
  print("[ 2. 학생성적 출력 ]")
  print("[ 3. 학생성적 수정 ]")
  print("[ 4. 학생성적 검색 ]")
  print("[ 5. 학생성적 삭제 ]")
  print("[ 6. 등수처리 ]")
  print("[ 7. 학생성적 정렬 ]")
  print("[ 0. 프로그램 종료 ]")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요. >>")

  if choice == "1":
    while True:
      print("[ 1. 학생성적 입력 ]")
      print()

      no = stuNo+1
      name = input(f"{no}번째 학생 이름을 적어주세요. (상위메뉴 : 0)")
      if name == "0":
        print("성적 입력이 취소되었습니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0

      stu_datas.append([no, name, kor, eng, math, total, avg, rank])
      stuNo += 1
      print(f"{name}학생 성적입력이 완료되었습니다.")
      print()
    
  elif choice == "2":
    print("[ 2. 학생성적 출력 ]")
    print()

    for t in s_title:
      print(f"{t}\t", end="")
    print(); print("-"*60)

    for s in stu_datas:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
      print()
  elif choice == "3":
    print("[ 3. 학생성적 수정 ]")
    print()

    name = input("수정하고자 하는 학생 이름을 입력하세요.")
    for s in stu_datas: # 찾으려고 데이터에서 뺑뺑이
      if s[1] == name:
        print(f"{name} 학생의 정보를 찾았습니다.")
        print()
        print("[ 수정과목 선택 ]")
        print("1. 국어점수 수정 ")
        print("2. 영어점수 수정 ")
        print("3. 수학점수 수정 ")
        choice = input("원하시는 번호를 입력하세요.")

        if choice == "1":
          print(f"현재 국어점수 : {s[2]}")
          s[2] = int(input("변경하고자 하는 국어점수 : "))
        elif choice == "2":
          print(f"현재 영어점수 : {s[3]}")
          s[3] = int(input("변경하고자 하는 영어점수 : "))
        elif choice == "3":
          print(f"현재 수학점수 : {s[4]}")
          s[4] = int(input("변경하고자 하는 수학점수 : "))
        s[5] = s[2]+s[3]+s[4]
        s[6] = s[5]/3      

        print(f"{name}학생의 성적이 수정되었습니다.")
        print()
        check = 1

    if check == 0:
      print(f"{name} 학생이 없습니다. 다시 입력해주세요.")
      print()
          
  elif choice == "4":
    print("[ 4. 학생성적 검색 ]")
    print()

    name = input("찾고자 하는 학생 이름을 입력하세요.")
    for s in stu_datas: # 찾으려고 데이터에서 뺑뺑이
      if s[1] == name:
        print(f"{name} 학생의 정보를 찾았습니다.")
        print()

        for t in s_title:
          print(f"{t}\t", end="")
        print(); print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
        print()
        check = 1
  
    if check == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")
      print()


  elif choice == "5":
    print("[ 5. 학생성적 삭제 ]")
    print()

    name = input("삭제하고자 하는 학생 이름을 입력하세요.")
    for s in stu_datas: # 찾으려고 데이터에서 뺑뺑이
      if s[1] == name:
        print(f"{name} 학생의 정보를 찾았습니다.")
        print()

  elif choice == "6":
    print("[ 6. 등수처리 ]")
    print()

  elif choice == "7":
    print("[ 7. 학생성적 정렬 ]")
    print()

