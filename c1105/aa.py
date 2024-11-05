import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

## db 연결함수
def connects():
    user = 'ora_user'
    password = '1111'
    dsn = 'localhost:1521/xe'
    try : conn = oracledb.connect(user=user,password=password,dsn=dsn)
    except Exception as e: print('예외처리 : ',e)
    return conn

while True:
    search = input('찾고자 하는 이름을 입력하세요. >> ')
    search = '%'+search+'%'
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students where name like :search"
    for s in s_title:
        print(s,end='\t')
    print();print('-'*80)
    # db연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    if len(rows) < 1:
        print('데이터가 없습니다.')
        break
    for row in rows:
        for i,r in enumerate(row):
            print(r,end='\t')
        print()