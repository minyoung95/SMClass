# 오라클 db에서는 타입결정
# 문자형(숫자만) 타입 + 숫자와 사칙연산 가능
# 파이썬에 호출한 타입의 결과값은?

import oracledb

def connects():
    user = 'ora_user'
    password = '1111'
    dsn = 'localhost:1521/xe'
    try : conn = oracledb.connect(user=user,password=password,dsn=dsn)
    except Exception as e : print('예외처리',e)
    return conn

conn = connects()
cursor = conn.cursor()
# number, number, varchar2, varchar2 - chartable
# number, number, number, number - chartable2
sql = "select no,kor,to_char(kor,'00000000'),to_char(kor,'999,999,999') from chartable"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(f"두수의 합 : {row[1]+row[2]}") # 숫자 + 문자 : 오라클에선 되지만 파이썬에선 안됨
    print(row)
    
print('검색완료')
conn.close()