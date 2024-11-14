import oracledb

## oracle 연결 - sql developer
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

print(conn.version) # 연결확인


## 1개 검색된 데이터 내용 호출
# cursor = conn.cursor() # sql 실행창 열기
# sql = 'select count(*) from member'
# cursor.execute(sql)
# count1 = cursor.fetchone(sql)
# print('개수 : ',count1)

## 여러개 검색된 데이터 내용 호출
cursor = conn.cursor() # sql 실행창 열기
sql = 'select * from member'
cursor.execute(sql)
rows = cursor.fetchall()


s_students = ['번호','이름','국어','영어','수학','합계','평균','등수']

for s in s_students:
    print(f'{s}\t',end='')
print();print('-'*60)

for row in rows: # 테이블을 리스트타입으로
    print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t')

conn.close()