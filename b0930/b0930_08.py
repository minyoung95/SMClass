# 리스트 추가 방법 : appeend - 제일 뒤에 추가, insert - 윈하는 위치에 추가

a_list = [1, 2, 3]
print(a_list)
a_list.append(4)
print(a_list)
a_list.append(10)
print(a_list)
a_list.insert(0, 50) # 0번째 배열에 50 추가
print(a_list)
a_list.insert(3, 20)
print(a_list)

# 리스트 삭제 방법 : del - index위치의 데이터 삭제, remove - 데이터값 삭제

del a_list[0]
print(a_list)
del a_list[2]
print(a_list)
a_list.remove(4) # 리스트 안에 값 4를 삭제
print(a_list) 
a_list.remove(1)
print(a_list)

stu = [1, '유관순', 100, 100, 100, 99]

#합계, 평균 추가하여 출력

stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/4)
print(stu)