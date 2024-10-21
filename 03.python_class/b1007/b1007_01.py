stu_datas = []
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
choice = 0
stuNo = 0 # 학생번호
stuNo = len(stu_datas) # 리스트에 이미 학생이 차 있을 시 그 이후 번호로 지정해줌
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0 # 성적처리에 필요한 변수
check = 0 # 체크할때 변수
count = 1 # 등수?처리

while True:
  print("[ 학생성적 프로그램 ]")
  print("-"*60)
  print("[ 1. 학생성적 입력 ]")
  print("[ 2. 학생성적 출력 ]")
  print("[ 3. 학생성적 수정 ]")
  print("[ 4. 학생성적 검색 ]")
  print("[ 5. 학생성적 삭제 ]")
  print("[ 6. 등수처리 ]")
  print("[ 0. 프로그램 종료 ]")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요. >>")

  if choice == "1":
    while True:
      print("[ 1. 학생성적 입력 ]")
      print()

      no = stuNo + 1 # 리스트 - 학생 수
      name = input(f"{no}번째 학생이름을 입력하세요.(0. 이전화면)")
      if name == "0":
        print("성적 입력을 취소합니다.")
        print()
        break # while True 쪽으로 되돌아감
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0

      stu_datas.append([no, name, kor, eng, math, total, avg, rank])  # 빈 리스트에 변수를 추가해줌
      stuNo += 1 # 다음 학생 번호를 1 증가
      print(f"{name} 학생의 성적이 저장되었습니다.")
      print()
  elif choice == "2":
    print("[ 2. 학생성적 출력 ]")
    print()
    ## 상단 타이틀 출력
    for title in s_title: # s_title 에서 한개씩 뽑아옴
      print(f"{title}\t", end="") # end="" : 마지막에 엔터키 x (기본값 end = "\n"(엔터키))
    print()
    print("-"*60)
    
    # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n") // 위 3줄과 같음

    ## 학생 정보 출력
    for s in stu_datas:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
      print()

  elif choice == "3":
    print("[ 3. 학생성적 수정 ]")
    print()

    name = input("수정하고자 하는 학생의 이름을 입력하세요.")
    for s in stu_datas: # stu_datas 에서 뺑뺑이 돌리기
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print()
        print("[ 수정과목 선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("수정을 하고자하는 과목 번호를 입력하세요.")

        if choice == "1":
          print("현재 국어점수는 : {}".format(s[2]))
          s[2] = int(input("변경하고자 하는 국어점수 : "))
        elif choice == "2":
          print("현재 영어점수는 : {}".format(s[3]))
          s[3] = int(input("변경하고자 하는 영어점수 : "))
        elif choice == "3":
          print("현재 수학점수는 : {}".format(s[4]))
          s[4] = int(input("변경하고자 하는 수학점수 : "))
        s[5] = s[2]+s[3]+s[4]
        s[6] = s[5]/3

        print(f"{name} 학생의 성적이 수정되었습니다.")
        check = 1

    if check == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")
      print()

  elif choice == "4":
    print("[ 4. 학생성적 검색 ]")
    print()

    name = input("찾고자 하는 학생의 이름을 입력하세요.")
    for s in stu_datas: # stu_datas 에서 뺑뺑이 돌리기
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        ## 학생정보 출력
        for title in s_title: # s_title 에서 한개씩 뽑아옴
          print(f"{title}\t", end="") # end="" : 마지막에 엔터키 x (기본값 end = "\n"(엔터키))
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print()
        check = 1 # check 를 넣지 않으면 학생이 없을때와 있을때 데이터가 같이 출력된다.

    # 모든 학생의 비교(for문)가 끝난 후 cheak 확인
    if check == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")
      print()

  elif choice == "5":
    print("[ 5. 학생성적 삭제 ]")
    print()

    name = input("찾고자 하는 학생의 이름을 입력하세요.")
    for idx,s in enumerate(stu_datas):
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        check = 1 # break 아래에 두면 적용이 안되어서 위로올림
        choice = input(f"{name} 학생의 성적을 삭제하시겠습니까? (삭제 시 복구불가)\n1. 삭제 2. 취소 >> ")
        if choice == "1":
          del stu_datas[idx]
          print(f"{name} 학생의 성적이 삭제되었습니다.")
        else:
          print("학생성적 삭제가 취소되었습니다.")
          break

    # 모든 학생의 비교(for문)가 끝난 후 cheak 확인
    if check == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")
      print()

  elif choice == "6":
    print("[ 6. 등수처리 ]")
    print()

    for s in stu_datas:
      count = 1 # 1등인 데이터
      for st in stu_datas:
        if s[5] < st[5]: # 다른 데이터와 비교(작을 경우)
          count += 1 # 2등으로 밀려남
        s[7] = count # 등수 입력

    print("등수처리가 완료되었습니다.")
    print()

  elif choice == "0":
    print("[ 0. 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break