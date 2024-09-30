stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [[1, '유관순', 100, 100, 100, 99],
             [2, '이순신', 100, 99, 98, 99], 
             [3, '홍길동', 80, 100, 90, 99],
             [4, '김구', 80, 100, 90, 99],
             [5, '김유신', 80, 100, 90, 99],
             ]

for s_t in stu_title:
  print("{}".format(s_t),end="\t")
print()
print("-"*60)

for s in stu_datas:
  s.append(s[2]+s[3]+s[4]+s[5]) # s에 append를 하면 stu_datas에도 append가 된다.
  s.append((s[2]+s[3]+s[4]+s[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))
