## 학생성적 프로그램
## 1. 학생성적입력
## 2. 학생성적출력
## 3. 학생성적검색
## 시퀀스 students_seq 생성
## students 테이블 사용 번호,김유신,99,98,96,합계,평균,등수,입력일

import oracledb

def connects():
    user = 'ora_user'
    password = '1111'
    dsn = 'localhost:1521/xe'
    try : conn = oracledb.connect(user=user,password=password,dsn=dsn)
    except Exception as e : print('예외처리 : ',e) 
    return conn

print('1.학생성적입력')
print('2.학생성적출력')
print('3.학생성적검색')
choice = input('원하는 번호 입력 >> ')

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
if choice == '1':
    print('[ 학생성적 입력 ]')
    name = input('이름을 입력하세요. >>')
    kor = int(input('국어점수를 입력하세요. >>'))
    eng = int(input('영어점수를 입력하세요. >>'))
    math = int(input('수학점수를 입력하세요. >>'))
    total = kor+eng+math
    avg = total/3    
    
    s_list = [name,kor,eng,math,total,avg]
    
    conn = connects()
    cursor = conn.cursor()
    sql = "insert into students values(students_seq.nextval,:1,:2,:3,:4,:5,:6,1,sysdate)"
    cursor.execute(sql,s_list)
    conn.commit()
    conn.close()
    
    print('학생성적이 저장되었습니다.')

elif choice == '2':
    print('[ 학생성적 출력 ]')
    
    for s in s_title:
        print(s,end='\t')
    print();print('-'*80)
    
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    for row in rows:
        for i,r in enumerate(row):
            if i == 1:
                print(f'{r:10s}',end='\t')
                continue
            if i == 6:
                print(f'{r:.2f}',end='\t')
                continue
            if i == 8:
                print(r.strftime('%Y-%m-%d'),end='\t')
                continue
            print(r,end='\t')
        print()
    
    conn.close()

elif choice == '3':
    print('[ 학생성적 검색 ]')
    
    name = input('검색하고 싶은 학생 이름을 입력하세요. >> ')
    
    for s in s_title:
        print(s,end='\t')
    print();print('-'*80)
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from students where name=:name"
    cursor.execute(sql,name=name)
    rows = cursor.fetchall()
    for row in rows:
        for i,r in enumerate(row):
            if i == 1:
                print(f'{r:10s}',end='\t')
                continue
            if i == 6:
                print(f'{r:.2f}',end='\t')
                continue
            if i == 8:
                print(r.strftime('%Y-%m-%d'),end='\t')
                continue
            print(r,end='\t')
        print()

    conn.close()
    
    