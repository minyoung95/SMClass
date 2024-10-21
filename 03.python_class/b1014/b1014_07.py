stu_title = ['국어', '영어', '수학']
students = {"국어":100, "영어":100, "수학":99, "합계":299}

print("[ 점수 수정 ]")
print("1. 국어점수")
print("2. 영어점수")
print("3. 수학점수")
choice = int(input("수정하고자 하는 과목 번호를 입력해주세요."))

def s_modify(choice):
  print("현재 {}점수 : {}".format(stu_title[choice-1],students[stu_title[choice-1]]))
  students[stu_title[choice-1]] = int(input(f"변경하고자 하는 {stu_title[choice-1]}점수를 입력하세요."))

if choice == 1:
  s_modify(choice)
elif choice == 2:
  s_modify(choice)
elif choice == 3:
  s_modify(choice)

students["합계"] = students["국어"] + students["영어"] + students["수학"]
print("변경 : ",students)