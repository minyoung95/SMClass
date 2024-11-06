import oracledb

## db연결 함수선언
def connections():
    try:
        conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
        print('db연결',conn.version)
    except Exception as e: print('예외발생',e)
    return conn

## 함수호출
conn = connections()
cursor = conn.cursor()

## 키워드 검색 (번호는 가능)
# no = input('번호 입력하세요.')
# sql = "select * from employees where employee_id >=:no"
# cursor.execute(sql,no=no)

## 번호순서 (execute 변수에 리스트타입)
# no = input('번호 입력하세요.')
# sql = "select * from employees where employee_id >=:1"
# cursor.execute(sql,[no])

# 검색기능
# search = input('검색할 이름을 입력하세요. >>')
# search = '%' + search + '%'
# sql = "select * from employees where emp_name like :search" # %:search%라고 입력을 해놓으면 %% 안쪽의 글자를 찾는다는 느낌(:search를 찾을수 없습니다.) >> 검색이 안된다.
# cursor.execute(sql,search=search) # 변수는 리스트, 튜플 타입으로 주어야함

## 월급 4000~8000사이에 있는 사원을 모두 출력
num1 = input('숫자1 입력')
num2 = input('숫자2 입력')
sql = "select employee_id,emp_name,salary from employees where salary >=:1 and salary <=:2 order by salary" # order by 순차정렬
cursor.execute(sql,(num1,num2))


title = ['employee_id','emp_name','salary']
a_list = []

rows = cursor.fetchall()
for row in rows:
    a_list.append(dict(zip(title,row)))

print(a_list)
conn.close()





# employees 테이블에서 이름이 a가 포함되어있는 모든컬럼 출력