stu_datas = {}

stu_datas['no'] = 1
stu_datas['name'] = input("이름을 입력하세요.")
stu_datas['kor'] = int(input("국어점수를 입력하세요."))
stu_datas['eng'] = int(input("영어점수를 입력하세요."))
stu_datas['math'] = int(input("수학점수를 입력하세요."))
stu_datas['total'] = stu_datas['kor']+stu_datas['eng']+stu_datas['math']
stu_datas['avg'] = stu_datas['total']/3
stu_datas['rank'] = 0

print(stu_datas)

stu_datas = []
stu = {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1}
stu1 = {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1}

stu_datas.append(stu)
stu_datas.append(stu1)

# print(stu_datas)