import oracledb
import random


def connects():
    try:
        conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print('예외발생',e)
    return conn
conn = connects()
cursor = conn.cursor()

user_id = input('아이디를 입력하세요. >>') # eee
user_pw = input('패스워드를 입력하세요. >>') #2222

sql = 'update member set pw=:pw where id=:id' # 데이터 수정
cursor.execute(sql, id=user_id,pw=user_pw)

conn.commit()
print('파일이 수정되었습니다.')
cursor.close()

## 임시비밀번호
# a_list = [0,1,2,3,4,5,6,7,8,9]
# a = random.randrange(0,10000) # 랜덤숫자 9999까지
# ran_num = f"{a:04}"
# print(ran_num)

