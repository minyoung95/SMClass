subject = ["이름", "국어", "영어", "수학", "합계", "평균"]
students = []

### 함수선언
def stuScore_update(k_title,s_title):
  print(f"현재 {k_title} 점수 : ",s[s_title])
  s[s_title] = int(input("변경 점수를 입력하세요."))
  print()
  print(students)

while True:
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  choice = input("원하는 번호 입력 >> ")

  if choice == "1":
    name = input("이름을 입력하세요.")

    score = [] # 과목 별 점수가 들어감
    sum = 0
    for i in range(3): # 과목이 늘어날수록 range 범위 증가
      num = int(input(f"{subject[i+1]}점수를 입력하세요."))
      score.append(num)
      sum += num # 과목이 추가될때마다 sum에 +
    avg = sum/len(score)
    s = {'name':name, 'kor':score[0], 'eng':score[1], 'math':score[2], 'total':sum, 'avg':avg}
    students.append(s)
    print(students)
  
  elif choice == "3":
    search = input("찾고자 하는 학생 이름을 입력하세요.")
    for s in students: # students에 있는 하나하나 검색
      if s['name'] == search:
        print("[수정과목 선택]")
        print("1. 국어, 2. 영어, 3. 수학, 4. 이전화면")
        choice = int(input("원하는 번호를 입력하세요."))

        if choice == 1:
          stuScore_update(subject[choice],'kor')
        elif choice == 2:
          stuScore_update("영어","eng")
        elif choice == 3:
          stuScore_update("수학","math")
        elif choice == 4:
          print("이전화면 이동")
          break