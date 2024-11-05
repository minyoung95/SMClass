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


## 메인 메뉴 출력함수
def main_print():
    print('[ 학생성적 프로그램 ]')
    print('1. 학생성적 입력')
    print('2. 학생성적 출력')
    print('3. 학생성적 검색')
    print('4. 학생성적 정렬') # 이름 순차,역순 / 합계 순차,역순
    print('5. 등수 처리')
    print('0. 프로그램 종료')
    choice = input('원하는 번호를 입력하세요. >> ')
    return choice


## 학생성적 입력함수
def stu_insert():
    conn = connects()
    cursor = conn.cursor()
    name = input('학생 이름을 입력하세요.')
    kor = int(input('국어점수를 입력하세요.'))
    eng = int(input('영어점수를 입력하세요.'))
    math = int(input('수학점수를 입력하세요.'))
    # insert, update, delete 경우 conn.commit() 해야함
    sql = "insert into students values(students_seq.nextval,:name,:kor,:eng,:math,:kor+:eng+:math,(:kor+:eng+:math)/3,1,sysdate)"
    cursor.execute(sql,name=name,kor=kor,eng=eng,math=math)
    conn.commit()
    conn.close()
    print('학생성적이 저장되었습니다.')


## 학생성적 출력함수
def stu_output():
    for s in s_title:
        print(s,end='\t')
    print();print('-'*80)
    # db연결
    conn = connects()
    cursor = conn.cursor()
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) < 1:
        print('데이터가 없습니다.')
        return # 함수반환
    for row in rows:
        for i,r in enumerate(row):
            print(r,end='\t')
        print()
    conn.close()
    print('학생성적 출력완료')
    
def stu_search():
    print('1. 이름으로 검색')
    print('2. 합계순으로 검색')
    choice = input('원하는 번호를 입력하세요. >> ')
    
    if choice == '1':
        print('[ 이름으로 검색 ]')
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
            return
        for row in rows:
            for i,r in enumerate(row):
                print(r,end='\t')
            print()
    if choice == '2':
        print('[ 합계순으로 검색 ]')
        print()
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total"
        for s in s_title:
            print(s,end='\t')
        print();print('-'*80)
        # db연결
        conn = connects()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) < 1:
            print('데이터가 없습니다.')
            return
        for row in rows:
            for i,r in enumerate(row):
                print(r,end='\t')
            print()
        conn.close()

def stu_order():
    print('1. 이름순차정렬')
    print('2. 이름역순정렬')
    print('3. 합계순차정렬')
    print('4. 합계역순정렬')
    choice = input('원하는 번호를 입력하세요.')
    
    if choice == '1':
        print('[ 이름 순차정렬 ]')
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name"
    elif choice == '2':
        print('[ 이름 역순정렬 ]')
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name desc"
    elif choice == '3':
        print('[ 합계 순차정렬 ]')
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total"
    elif choice == '4':
        print('[ 합계 역순정렬 ]')
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total desc"
        
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) < 1:
        print('데이터가 없습니다.')
        return
    for row in rows:
        for i,r in enumerate(row):
            print(r,end='\t')
        print()
    conn.close()

def stu_rank():
    sql = "update students a set rank =(\
            select ranks from(\
            select no,rank()over(order by total desc) ranks from students)b\
            where a.no = b.no)"
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print('등수 처리를 완료하였습니다.')
    print()
    # ----------------------- 등수처리
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) < 1:
        print('데이터가 없습니다.')
        return
    for row in rows:
        for i,r in enumerate(row):
            print(r,end='\t')
        print()        
    conn.close()
  