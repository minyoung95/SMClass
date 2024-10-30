import oracledb
import random
import smtplib
from email.mime.text import MIMEText


def connects():
    try:
        conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print('예외발생',e)
    return conn

while True:
    print('[ 커뮤니티 ]')
    print('1. 로그인')
    print('2. 비밀번호 찾기')
    print('3. 회원가입')
    print('0. 프로그램 종료')
    print('-'*30)
    choice = input('원하는 번호를 입력하세요. >>')
    
    if choice == '1':
        print('[ 로그인 ]')
        user_id = input('아이디를 입력하세요. >>')
        user_pw = input('패스워드를 입력하세요. >>')
        
        # 오라클 db에 접속하여 member 테이블에서 검색
        conn = connects()
        cursor = conn.cursor()
        sql = 'select * from member where id=:id and pw=:pw'
        cursor.execute(sql, id=user_id,pw=user_pw)
        row = cursor.fetchone() # None 비교
        print(row)
        if row != None:
            print(f'로그인 성공! {row[2]}님 환영합니다.')
        else:
            print('아이디 또는 패스워드가 일치하지 않습니다.')
        
        cursor.close()
        # if user_id == 'aaa' and user_pw == '1111':
        #     print('로그인 성공')
        # else:
        #     print('로그인 실패')
        #     continue
        # print('학생성적 프로그램에 접속합니다.')
        ### 프로그램 구현
    elif choice == '2':
        print('[ 비밀번호 찾기 ]')
        search = input('해당 아이디를 입력하세요.')
        conn = connects()
        cursor = conn.cursor()
        sql = 'select * from member where id=:id'
        cursor.execute(sql,id=search)
        row = cursor.fetchone()
        print(row)
        if row[1] != None:
            print('아이디가 존재합니다. 임시패스워드를 발급합니다.')
            # 임시비밀번호 생성 > 이메일로 보내기
            # 임시비밀번호로 로그인 했을 경우 로그인 성공할 수 있게
            p_pw = random.randrange(0,10000)
            p_pw = f'{p_pw:04}'
            smtpName = 'smtp.naver.com'
            smtpPort = 587
            
            sendemail = 'mylim52@naver.com'
            pw = 'DSTZPVRL8Q8L'
            recvemail = 'mylim52@naver.com'
            
            title = '임시비밀번호입니다.'
            content = f'{p_pw}'
            
            msg = MIMEText(content)
            msg['Subject'] = title
            msg['From'] = sendemail
            msg['To'] = recvemail
            
            s = smtplib.SMTP(smtpName,smtpPort)
            s.starttls()
            s.login(sendemail, pw)
            s.sendmail(sendemail, recvemail, msg.as_string())
            s.quit()
            
            print('임시비밀번호를 이메일로 발송했습니다.')
            
            sql = 'update member set pw=:pw where id=:id'
            cursor.execute(sql,id=search,pw=p_pw)
            print('임시비밀번호로 수정되었습니다.')
            print(row)
            conn.commit()

        else:
            print('아이디가 존재하지 않습니다.')
        
        cursor.close()
    elif choice == '3':
        pass
    elif choice == '0':
        print('프로그램을 종료합니다.')
        break