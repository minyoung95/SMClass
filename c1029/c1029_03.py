
import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe') # sql developer 열기
cursor = conn.cursor() # sql창 열기
num1 = input('숫자1,2,3를 입력하세요. >> (,)')
n_list = num1.split(',')

### sql 작성 (문자열함수 f사용)
# sql = f'select * from students where no>={num}'

### execute함수에 변수추가 : sql의 :no에 변수 num을 넣는다.
# sql = 'select * from students where no in (:no1,:no2,:no3)' # sql 작성
# cursor.execute(sql,no1=num1,no2=num2,no3=num3) # sql 실행

### execute함수에 리스트 값 전달
# n_list = [num1,num2,num3]
# num2 = input('숫자2를 입력하세요. >>')
# num3 = input('숫자3를 입력하세요. >>')
sql = 'select * from students where no in (:1,:2,:3)' # sql 작성
cursor.execute(sql,n_list) # sql 실행 
rows = cursor.fetchall() # sql 모든창 열기

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']



## 학생성적 출력
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