students = [
  {"no":1,"name":"홍길동"},
  {"no":2,"name":"유관순"},
  {"no":3,"name":"이순신"},
]
stuNo = len(students)

def stu_input(stuNo,students):
  while True:
    no = stuNo+1
    print("no :",no)
    name = input(f"{no}번째 학생이름을 입력하세요. (0. 이전페이지)")
    if name == "0":
      break
    students.append({"no":no, "name":name})
    print(students)
    stuNo += 1
  return stuNo


stuNo = stu_input(stuNo,students)
print("stuNo :",stuNo)
print(students)