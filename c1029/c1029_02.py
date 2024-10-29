## 학생성적 출력
import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe') # sql developer 열기
cursor = conn.cursor() # sql창 열기
sql = 'select * from students' # sql 작성
cursor.execute(sql) # sql 실행
rows = cursor.fetchall() # sql 모든창 열기


s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

print("[ 학생성적 출력 ]")
for s in s_title:
    print(f'{s}',end='\t')
print();print('-'*70)

for row in rows:
    for i,r in enumerate(row):
        if i == 1:
            print(f'{r:10s}',end='\t')
            continue # 맨 밑 print(r 에서 한번 더 찍힘)
        if i == 6:
            print(f'{r:.2f}',end='\t')
            continue
        if i == 8:
            print(r.strftime("%Y-%m-%d"),end='\t')
            continue
        print(r,end='\t')
    print()