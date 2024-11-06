import oracledb

## sqldeveloper 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor() ## sql창 열림(명령어 입력가능)

## sql 작성, 실행
sql = 'select * from students'
cursor.execute(sql)

## 데이터 가져오기
rows = cursor.fetchall() # fetchall() : 모든데이터, fetchone() : 1개, fetchmany(x) : 정해진 숫자(x)만큼
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

for s in s_title:
    print(s,end='\t')
print(); print("-"*70)

for row in rows:
    for i,r in enumerate(row):
        if i == 1:
            print(f'{r:10s}',end='\t')
            continue
        if i == 6:
            print(f'{r:.2f}',end='\t')
            continue
        if i == 8:
            print(r.strftime("%Y-%m-%d"),end='\t') # strftime() : 날짜 포멧함수 %Y(2024),%y(24)
            continue
        print(r,end='\t')
    print()
## 종료
conn.close()