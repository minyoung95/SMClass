### 입력한 달 이상의 입사한 사원을 출력하시오.
import oracledb

def connects():
    user = 'ora_user'
    password = '1111'
    dsn = 'localhost:1521/xe'
    try:conn = oracledb.connect(user=user,password=password,dsn=dsn)
    except Exception as e: print('예외처리 : ',e)
    return conn

conn = connects()
cursor = conn.cursor()
d_day = int(input('숫자를 입력하세요.')) # d_day를 int로 바꿔준다
sql = "select emp_name,hire_date,substr(hire_date,4,2) from employees where substr(hire_date,4,2) >:d" ## 숫자형타입(:d)이기 때문에 
cursor.execute(sql,d=d_day)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()