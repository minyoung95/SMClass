import oracledb
import func

while True:
    # 시작화면 출력
    choice = func.screen()

    if choice == '1':    # 로그인
        print('[ 로그인 ]')
        func.mem_login()
    elif choice == '2':    # 비밀번호 찾기    
        print('[ 비밀번호 찾기 ]')
        func.search_pw()
    elif choice == '3':
        print('[ 회원가입 ]')
        pass
        