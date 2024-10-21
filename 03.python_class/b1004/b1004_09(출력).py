stu_datas = [[1, '유관순', 100, 100, 100],
             [2, '이순신', 100, 99, 98], 
             [3, '홍길동', 80, 100, 90],
             [4, '김구', 80, 100, 90],
             [5, '김유신', 80, 100, 90],
             ]

for s in stu_datas:
  s.append(s[2]+s[3]+s[4]) # s에 append를 하면 stu_datas에도 append가 된다.
  s.append((s[2]+s[3]+s[4])/3)
  s.append(0)

# 출력

s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

for s in s_title:
  print(s, end="\t")
print()
print("-"*60)

# 학생성적 출력

for s in stu_datas:
  print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
